#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".chptr-fleet" / "managed.json"
SECRET_PATTERNS = (
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"lin_api_[A-Za-z0-9]{20,}"),
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not MANIFEST.exists():
        fail("missing managed repository manifest")
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    required = data.get("required_files", [])
    missing = [path for path in required if not (ROOT / path).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))
    empty = [path for path in required if (ROOT / path).stat().st_size == 0]
    if empty:
        fail("empty required files: " + ", ".join(empty))

    for relative in data.get("json_files", []):
        path = ROOT / relative
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"invalid JSON {relative}: {exc}")

    for relative in data.get("scan_files", []):
        path = ROOT / relative
        if not path.exists() or path.stat().st_size > 1_000_000:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"credential-shaped value found in {relative}")

    generated = ROOT / "generated" / "manifest.json"
    if generated.exists():
        payload = json.loads(generated.read_text(encoding="utf-8"))
        for entry in payload.get("files", []):
            path = ROOT / entry["path"]
            if not path.exists():
                fail(f"generated file missing: {entry['path']}")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != entry["sha256"]:
                fail(f"generated file is stale: {entry['path']}")
        language_count = len(payload.get("languages", []))
        if language_count and language_count < 20:
            fail(f"expected at least 20 generated languages, found {language_count}")

    print(json.dumps({
        "repository": data.get("repository"),
        "role": data.get("role"),
        "required_files": len(required),
        "status": "ok",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
