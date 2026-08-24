-- Template migration. Replace :project_slug only through trusted deployment tooling.
-- Browser/Flutter clients never receive the service-role key and never select a table name.
create table if not exists public.chptr_session_events (
  event_id uuid primary key,
  project_id text not null,
  user_id uuid not null references auth.users(id) on delete cascade,
  session_id text not null,
  occurred_at timestamptz not null,
  severity text not null check (severity in ('trace','debug','info','warn','error','fatal')),
  event_name text not null,
  trace_id text,
  span_id text,
  attributes jsonb not null default '{}'::jsonb,
  received_at timestamptz not null default now(),
  unique (project_id, user_id, session_id, event_id)
);

alter table public.chptr_session_events enable row level security;
revoke all on public.chptr_session_events from anon, authenticated;

-- The trusted ores-otel collector inserts through service_role after validating a
-- short-lived registration. End users may read only their own rows through a view/API.
create policy chptr_session_events_select_own
  on public.chptr_session_events for select to authenticated
  using (auth.uid() = user_id);
