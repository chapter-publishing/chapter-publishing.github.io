# Contributing

1. Install dependencies through zed-pkg.
2. Run `.zed/pre-build`, `.zed/pre-test`, and `.zed/pre-publish` before opening a pull request.
3. Update canonical schemas before generated clients or runtime projections.
4. Add negative fixtures for authorization, lifecycle, idempotency, sync, and telemetry changes.
5. Keep production secrets and real user/manuscript data out of repositories and test artifacts.
