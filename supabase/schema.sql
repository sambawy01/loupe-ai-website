-- loupe-ai.com backend: waitlist subscribers, consent audit trail, download counts.
-- Run once in the Supabase SQL editor (or `supabase db push`). Idempotent where practical.
--
-- Security model
--   * The website uses the ANON key. anon may INSERT into subscribers and download_events only.
--     It can never SELECT, UPDATE or DELETE anything (no policies grant it; table privileges revoked).
--   * Status changes (confirm / unsubscribe) and confirmation tokens are handled only by Edge Functions
--     using the service role, which bypasses RLS. The service-role key never ships to the browser.
--   * No IP address and no user agent is stored anywhere. Country is a 2-letter code read from the
--     request's country header (Supabase's API sits behind Cloudflare: cf-ipcountry). VERIFY the header
--     name on your project: select current_setting('request.headers', true); from a REST call.

create extension if not exists pgcrypto;
create extension if not exists citext;

-- ------------------------------------------------------------------ helpers
create or replace function public.request_country() returns text
language plpgsql stable as $$
declare h json; c text;
begin
  begin
    h := nullif(current_setting('request.headers', true), '')::json;
  exception when others then return null;
  end;
  if h is null then return null; end if;
  c := upper(coalesce(h->>'cf-ipcountry', h->>'x-country', h->>'x-vercel-ip-country'));
  if c ~ '^[A-Z]{2}$' and c not in ('XX', 'T1') then return c; end if;
  return null;
end $$;

-- ------------------------------------------------------------------ subscribers
create table if not exists public.subscribers (
  id                        uuid primary key default gen_random_uuid(),
  email                     citext not null,
  name                      text,
  platforms                 text[] not null default '{}',
  country_declared          text,                 -- what the person picked (optional)
  country_from_header       text default public.request_country(),  -- set server-side, not by the client
  language                  text not null default 'en',
  locale                    text not null default 'en',              -- page language at sign-up
  -- four separate purposes, all opt-in
  consent_product_updates   boolean not null default false,
  consent_promotions        boolean not null default false,
  consent_beta_invites      boolean not null default false,
  consent_research          boolean not null default false,
  privacy_ack               boolean not null,
  consent_record            jsonb not null,       -- exact text shown for each purpose + version + page
  consent_text_version      text not null,
  status                    text not null default 'pending',
  confirm_token_hash        text,                 -- sha256 hex of the emailed token; never the token
  confirm_token_expires_at  timestamptz,
  unsubscribe_token_hash    text,
  confirmation_sent_at      timestamptz,
  created_at                timestamptz not null default now(),
  updated_at                timestamptz not null default now(),
  confirmed_at              timestamptz,
  unsubscribed_at           timestamptz,

  constraint subscribers_status_chk   check (status in ('pending', 'confirmed', 'unsubscribed')),
  constraint subscribers_email_chk    check (char_length(email) between 3 and 254 and email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  constraint subscribers_name_chk     check (name is null or char_length(name) <= 120),
  constraint subscribers_lang_chk     check (language in ('en', 'ar') and locale in ('en', 'ar')),
  constraint subscribers_country_chk  check (country_declared is null or country_declared ~ '^[A-Z]{2}$'),
  constraint subscribers_platforms_chk check (platforms <@ array['android','windows','linux','iphone','mac']::text[] and cardinality(platforms) <= 5),
  constraint subscribers_ack_chk      check (privacy_ack = true),
  constraint subscribers_record_chk   check (jsonb_typeof(consent_record) = 'object' and pg_column_size(consent_record) < 8192),
  constraint subscribers_version_chk  check (char_length(consent_text_version) between 1 and 40)
);
create unique index if not exists subscribers_email_key on public.subscribers (email);
create index if not exists subscribers_status_idx on public.subscribers (status, created_at);

-- ------------------------------------------------------------------ consent_events (append-only audit)
create table if not exists public.consent_events (
  id             bigint generated always as identity primary key,
  subscriber_id  uuid not null references public.subscribers(id) on delete cascade,
  event          text not null check (event in ('signed_up', 'confirmed', 'unsubscribed', 'consent_changed')),
  consents       jsonb not null,           -- the four booleans at the time of the event
  consent_record jsonb,                    -- exact text shown (for signed_up / consent_changed)
  consent_text_version text,
  source         text not null default 'website',
  created_at     timestamptz not null default now()
);
create index if not exists consent_events_sub_idx on public.consent_events (subscriber_id, created_at);

create or replace function public.consent_events_append_only() returns trigger
language plpgsql as $$
begin
  raise exception 'consent_events is append-only';
end $$;
drop trigger if exists consent_events_no_update on public.consent_events;
create trigger consent_events_no_update before update or delete on public.consent_events
  for each row execute function public.consent_events_append_only();
-- (Deleting a subscriber cascades; to allow erasure requests, delete the subscriber as service role with
--  `set session_replication_role = replica;` in the same transaction, or drop the cascade and keep the
--  audit rows keyed by an email hash. LAWYER TO CONFIRM the retention rule.)

-- ------------------------------------------------------------------ subscriber triggers
-- Anything the client sends for server-owned columns is overwritten here.
create or replace function public.subscribers_before_insert() returns trigger
language plpgsql security definer set search_path = public as $$
declare recent int;
begin
  new.id := gen_random_uuid();
  new.email := lower(trim(new.email));
  new.status := 'pending';
  new.confirm_token_hash := null;
  new.confirm_token_expires_at := null;
  new.unsubscribe_token_hash := null;
  new.confirmation_sent_at := null;
  new.confirmed_at := null;
  new.unsubscribed_at := null;
  new.created_at := now();
  new.updated_at := now();
  new.country_from_header := public.request_country();

  -- Coarse global rate limit: refuse bursts (spam / abuse). Tune to your traffic.
  select count(*) into recent from public.subscribers where created_at > now() - interval '1 minute';
  if recent >= 30 then
    raise exception 'rate limited' using errcode = 'PT429';
  end if;
  return new;
end $$;
drop trigger if exists subscribers_bi on public.subscribers;
create trigger subscribers_bi before insert on public.subscribers
  for each row execute function public.subscribers_before_insert();

create or replace function public.subscribers_after_insert() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into public.consent_events (subscriber_id, event, consents, consent_record, consent_text_version)
  values (new.id, 'signed_up',
          jsonb_build_object('product_updates', new.consent_product_updates, 'promotions', new.consent_promotions,
                             'beta_invites', new.consent_beta_invites, 'research', new.consent_research),
          new.consent_record, new.consent_text_version);
  return new;
end $$;
drop trigger if exists subscribers_ai on public.subscribers;
create trigger subscribers_ai after insert on public.subscribers
  for each row execute function public.subscribers_after_insert();

create or replace function public.touch_updated_at() returns trigger language plpgsql as $$
begin new.updated_at := now(); return new; end $$;
drop trigger if exists subscribers_bu on public.subscribers;
create trigger subscribers_bu before update on public.subscribers
  for each row execute function public.touch_updated_at();

-- ------------------------------------------------------------------ download_events
create table if not exists public.download_events (
  id          bigint generated always as identity primary key,
  platform    text not null check (platform in ('mac', 'ios', 'android', 'windows', 'linux')),
  version     text check (version is null or version ~ '^[0-9A-Za-z.+-]{1,32}$'),
  locale      text check (locale is null or locale in ('en', 'ar')),
  page        text check (page is null or char_length(page) <= 100),
  country     text default public.request_country(),
  created_at  timestamptz not null default now()
  -- deliberately no IP address, no user agent, no identifier of any kind
);
create index if not exists download_events_time_idx on public.download_events (created_at);

create or replace function public.download_events_before_insert() returns trigger
language plpgsql security definer set search_path = public as $$
declare recent int;
begin
  new.country := public.request_country();
  new.created_at := now();
  select count(*) into recent from public.download_events where created_at > now() - interval '1 minute';
  if recent >= 600 then raise exception 'rate limited' using errcode = 'PT429'; end if;
  return new;
end $$;
drop trigger if exists download_events_bi on public.download_events;
create trigger download_events_bi before insert on public.download_events
  for each row execute function public.download_events_before_insert();

-- ------------------------------------------------------------------ RLS + privileges
alter table public.subscribers     enable row level security;
alter table public.consent_events  enable row level security;
alter table public.download_events enable row level security;
alter table public.subscribers     force row level security;
alter table public.consent_events  force row level security;
alter table public.download_events force row level security;

revoke all on public.subscribers, public.consent_events, public.download_events from anon, authenticated;
grant insert (email, name, platforms, country_declared, language, locale,
              consent_product_updates, consent_promotions, consent_beta_invites, consent_research,
              privacy_ack, consent_record, consent_text_version)
  on public.subscribers to anon;
grant insert (platform, version, locale, page) on public.download_events to anon;
-- identity sequence for download_events is "generated always": no sequence grant needed for inserts.

drop policy if exists subscribers_anon_insert on public.subscribers;
create policy subscribers_anon_insert on public.subscribers
  for insert to anon
  with check (status = 'pending' and privacy_ack = true and confirm_token_hash is null);

drop policy if exists download_events_anon_insert on public.download_events;
create policy download_events_anon_insert on public.download_events
  for insert to anon with check (true);

-- No select/update/delete policies exist for anon or authenticated: those operations are denied.
-- consent_events has no anon policy at all: only the triggers (security definer) and service role write it.

-- ------------------------------------------------------------------ housekeeping (schedule with pg_cron)
-- Delete unconfirmed sign-ups after 30 days (CONFIRM the period in the privacy policy):
--   select cron.schedule('purge-pending', '17 3 * * *',
--     $$ delete from public.subscribers where status = 'pending' and created_at < now() - interval '30 days' $$);
-- Aggregate download counts instead of keeping rows forever, if you like:
--   select platform, version, country, date_trunc('day', created_at) d, count(*) from public.download_events group by 1,2,3,4;

-- ------------------------------------------------------------------ rate limiting guidance
-- 1. The triggers above cap bursts globally (30 sign-ups/min, 600 downloads/min). They are a backstop.
-- 2. Better per-client limits: put the insert behind an Edge Function with Cloudflare Turnstile, or use
--    Supabase's API rate limits / a WAF rule on POST /rest/v1/subscribers.
-- 3. The form has a honeypot field; the front end treats 409 (duplicate email) like success so the form
--    never reveals who is subscribed.
-- 4. Resend has its own sending limits; send-confirmation sends one email per new row only.
