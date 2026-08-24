# Reference-organization pattern audit

This repository is augmented from a live, read-only inventory of twenty sibling organizations.
The audit is used to select recurring repository roles; it is not a blind source-code copy.

- Organizations requested: **20**
- Organizations read successfully: **20**
- Repositories classified: **337**

## Organization coverage

| Organization | Repositories inventoried |
|---|---:|
| `3FA-app` | 14 |
| `anticaptrad` | 14 |
| `apostille-me` | 19 |
| `canonical-cloud` | 15 |
| `declarative-migrations` | 6 |
| `discrete-event-systems` | 4 |
| `ecma-d` | 12 |
| `elenkos-systems` | 14 |
| `embedded-alerts` | 18 |
| `fiducia-cloud` | 36 |
| `hypesiege` | 26 |
| `memebank` | 38 |
| `messaging-intel` | 16 |
| `opto-sync` | 6 |
| `ores-otel` | 6 |
| `quaestor-ledger` | 13 |
| `shared-auth` | 13 |
| `sonus-auris` | 19 |
| `streempilot` | 21 |
| `zed-pkg` | 27 |

## Recurring roles

| Role | Matches | Representative examples |
|---|---:|---|
| `api-server` | 20 | `3FA-app/3fa-backend.rs`, `anticaptrad/act-api-server.rs`, `apostille-me/apme-api`, `canonical-cloud/canonical-api-server.rs` |
| `cli` | 18 | `3FA-app/3FA-app-cli`, `anticaptrad/act-cli`, `apostille-me/apme-cli`, `canonical-cloud/canonical-cli` |
| `clients` | 21 | `3FA-app/3fa-clients`, `anticaptrad/act-clients`, `apostille-me/apme-clients`, `apostille-me/apostille-me-clients` |
| `desktop` | 8 | `3FA-app/3FA-desktop.rs`, `anticaptrad/act-desktop-app.rs`, `ecma-d/ecmad-desktop-app.rs`, `elenkos-systems/elenkos-desktop-app.rs` |
| `e2e` | 18 | `3FA-app/3fa-app-e2e`, `anticaptrad/act-e2e`, `apostille-me/apme-e2e`, `canonical-cloud/canonical-e2e` |
| `flutter` | 10 | `anticaptrad/act-flutter`, `canonical-cloud/canonical-flutter`, `ecma-d/ecmad-flutter`, `elenkos-systems/elenkos-flutter` |
| `infra` | 18 | `3FA-app/3fa-infra`, `anticaptrad/act-infra`, `apostille-me/apme-infra`, `apostille-me/apostille-me-infra` |
| `interfaces` | 20 | `3FA-app/3fa-interfaces`, `anticaptrad/act-interfaces`, `apostille-me/apme-interfaces`, `canonical-cloud/canonical-interfaces` |
| `lib-core` | 21 | `apostille-me/apme-libs`, `apostille-me/apostille-me-libs`, `canonical-cloud/canonical-lib`, `ecma-d/ecmad-lib-core` |
| `mcp` | 17 | `3FA-app/3FA-mcp-server.rs`, `anticaptrad/act-mcp-server.rs`, `apostille-me/apme-mcp-server.rs`, `canonical-cloud/canonical-mcp-server.rs` |
| `monorepo` | 18 | `3FA-app/threefa-monorepo`, `anticaptrad/act-monorepo`, `apostille-me/apme-monorepo`, `apostille-me/apostille-me-monorepo` |
| `sync` | 20 | `3FA-app/3fa-app-sync`, `anticaptrad/act-sync`, `apostille-me/apme-sync`, `ecma-d/ecmad-sync` |
| `telemetry` | 3 | `fiducia-cloud/fiducia-telemetry.rs`, `ores-otel/ores-otel.github.io`, `ores-otel/ores.otel.log` |
| `web-server` | 46 | `3FA-app/3fa-app.github.io`, `3FA-app/3fa-web-server.rs`, `anticaptrad/act-web-server.rs`, `apostille-me/apme-web-dioxus` |

## Applied Chapter Publishing topology

The resulting fleet uses the recurring interfaces → generated clients → shared domain core → API/web/CLI/Flutter/desktop/sync → E2E pattern, with infrastructure kept outside the monorepo and CI-heavy validation placed in `chapter-publishing-test`.

Every managed repository also receives zed-pkg lifecycle hooks and an ores-otel session-telemetry boundary.
