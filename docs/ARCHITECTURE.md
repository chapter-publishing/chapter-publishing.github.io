# Architecture: chapter-publishing/chapter-publishing.github.io

**Role:** `website`  
**Environment:** `production source`

The canonical contract lives in `chapter-publishing/chptr-interfaces`. Generated language packages live in `chptr-clients`; domain invariants live in `chptr-lib-core`. API writes and web reads remain separate deployment boundaries. `chptr-sync` owns offline replication. Flutter and Rust desktop applications consume APIs and generated clients rather than duplicating persistence rules. `chptr-infra` is deliberately not a monorepo submodule.

Authentication is dual-boundary Shared-Auth/Supabase. Telemetry follows the private session model in `docs/OBSERVABILITY.md`. All dependency and publication lifecycle decisions are represented through zed-pkg hooks.
