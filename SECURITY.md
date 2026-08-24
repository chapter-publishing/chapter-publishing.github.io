# Security policy

Report vulnerabilities privately to the Chapter Publishing maintainers. Do not include live credentials, access tokens, unpublished manuscripts, or user telemetry in issues.

Repository invariants: no service-role keys in clients; least-privilege project authorization; private per-user/per-session telemetry topics; idempotent mutation keys; revision checks on publishing transitions; encrypted deployment secrets; and test-only synthetic fixtures in `chapter-publishing-test`.
