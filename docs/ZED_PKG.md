# zed-pkg lifecycle

`.zpkg.toml` is the source of dependency/publication truth. `.zed/` provides convention-based lifecycle hooks for install, build, test, and publish. Hooks are deterministic, non-interactive, and safe to run repeatedly.

The pre-publish gate validates managed files, generated hashes, JSON, and credential hygiene, then rejects an uncommitted worktree. Native manifests (`Cargo.toml`, `pubspec.yaml`, `package.json`, and similar) are generated or maintained projections; they must not silently diverge from the zed dependency graph.
