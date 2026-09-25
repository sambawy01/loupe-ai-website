# loupe-ai.com

Static site for Loupe (Loupe for iPhone, Loupe Station for Mac). English + Arabic (RTL) mirror under `/ar/`.
No framework, no CDN, no cookies, no analytics. Fonts are self-hosted (Rajdhani, JetBrains Mono, Noto Kufi Arabic — SIL OFL).

## Layout
- `index.html`, `features/`, `download/`, `privacy/`, `terms/`, `404.html` — generated; `ar/` is the Arabic mirror.
- `tools/build.py` + `tools/content.py` — all copy lives in `content.py`; legal text in `legal/*.md`.
  Rebuild: `pip install markdown && python3 tools/build.py`.
- `assets/config.js` — **placeholders** (Supabase URL/anon key, Mac download, App Store URL/flag).
- `assets/js/` — `main.js` (nav, carousel, privacy meter, download buttons + beacon), `hero.js` (live pipeline canvas),
  `demo.js` (teach-a-judgment demo: made-up data, scripted answers, labelled as such), `waitlist.js`.
- `supabase/schema.sql`, `supabase/functions/{send-confirmation,confirm,unsubscribe}` — backend.
- `updates/appcast.xml` — empty Sparkle feed (Loupe Station reads `https://loupe-ai.com/updates/appcast.xml`).
- `CNAME` (loupe-ai.com), `.nojekyll`, `robots.txt`, `sitemap.xml`, `site.webmanifest`.

Preview locally: `python3 -m http.server 8811` then open http://127.0.0.1:8811/.

## Setup
1. **Supabase project** → SQL editor → run `supabase/schema.sql`. Check the country header:
   `select current_setting('request.headers', true);` from a REST call; adjust `request_country()` if needed.
2. **Edge Functions** (Supabase CLI):
   ```
   supabase functions deploy send-confirmation
   supabase functions deploy confirm --no-verify-jwt
   supabase functions deploy unsubscribe --no-verify-jwt
   supabase secrets set RESEND_API_KEY=... WEBHOOK_SECRET=<long random> \
     MAIL_FROM="Loupe <hello@loupe-ai.com>" FUNCTIONS_URL=https://<ref>.functions.supabase.co SITE_URL=https://loupe-ai.com
   ```
   Keys live only in Supabase secrets — never in this repo.
3. **Database webhook**: Database → Webhooks → on INSERT into `public.subscribers` → HTTP POST to the
   `send-confirmation` function URL with header `Authorization: Bearer <WEBHOOK_SECRET>`.
4. **Resend**: verify the loupe-ai.com sending domain (SPF/DKIM).
5. **assets/config.js**: set `SUPABASE_URL` and `SUPABASE_ANON_KEY` (anon key is public by design; RLS allows INSERT only).
   Until then the form says sign-ups aren't open and no beacon is sent.
6. **Mac download**: once `sambawy01/loupe-downloads` is public with a `.dmg` release, set `MAC_AVAILABLE: null`
   (auto-detect latest release via the GitHub API) or `true` (always link `MAC_DOWNLOAD_URL`). Default `false` = "coming soon"
   (the repo currently 404s, and auto-detect would log a console error).
7. **iPhone**: set `APP_STORE_URL` and `IOS_AVAILABLE: true` when published.
8. **Appcast**: add signed `<item>`s from laya-studio `macos/dist/appcast-item.xml`, newest first, after uploading the DMG.
9. Pick scheduled purge of unconfirmed sign-ups (pg_cron example in schema.sql) and fill the `[...]` placeholders in `legal/privacy*.md`.
10. GitHub Pages: push, enable Pages on `main`, point DNS for loupe-ai.com.

## Consent
Four separate unticked purposes + required privacy acknowledgement. The exact text shown for each purpose, the
acknowledgement text and `CONSENT_TEXT_VERSION` are stored in `subscribers.consent_record`; every change is appended
to `consent_events`. Bump `CONSENT_TEXT_VERSION` in `config.js` and `CONSENT_VERSION` in `tools/content.py` whenever wording changes.

## Honesty rule
Only measured numbers (with where they were measured) — see `tools/content.py`. No invented stats, reviews or customers.
