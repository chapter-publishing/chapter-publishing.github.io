# Observability boundary

Chapter Publishing uses `github.com/ores-otel` as the cross-runtime logging, tracing, and metrics contract.

1. A signed-in client presents its Shared-Auth or Supabase JWT to a trusted collector.
2. The collector authorizes the project and returns a short-lived private topic shaped as `ores-otel:<project>:<user>:<session>`.
3. Browser, TypeScript, Rust, Dart, Flutter, and desktop clients send bounded envelopes over Supabase Realtime WebSockets.
4. The collector derives project/user/session identity from the registration, recursively redacts credential-shaped values, applies queue/rate limits, and performs idempotent inserts.
5. HTTP ingestion is a fallback when WebSockets are unavailable. Neither clients nor source repositories contain a Supabase service-role credential.

Required resilience: bounded queues, heartbeat and reconnect jitter, event UUID idempotency, envelope size limits, recursive redaction, clock-skew rejection, private-channel authorization, and backpressure-aware batching.
