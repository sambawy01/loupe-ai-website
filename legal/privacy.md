# Loupe Privacy Policy

**Draft for review by a qualified lawyer. Not yet in force.**
Effective date: 26 September 2026 · Applies to: Loupe for iPhone (`com.loupe-ai.ios`) and Loupe Station for Mac (`com.loupe-ai.desktop`)

## 1. Who we are

Loupe is published by Hany Sadek, trading as Loupe ("we", "us"), of Hurghada, Egypt. If Loupe later moves to a company, we will update this policy and tell you in the app.

Contact: privacy@loupe-ai.com. We are the controller only for the small amount of data described in section 6 (the online helper) and for emails you send us. For everything else, Loupe runs on your device and we never receive it.

## 2. The short version

- **Loupe decides on your device.** Its decision model, the Loupe Decision Model, runs on your iPhone or Mac. Your photos, files, calendar, contacts and mail are read there and are not sent to us.
- **No account.** You do not sign up with Loupe. We do not know who you are.
- **No analytics, advertising or tracking.** The apps contain no analytics, crash-reporting or advertising SDKs, and we do not sell or share personal information.
- **Online features are optional.** Features that need the internet are off by default, labelled **Online** each time they show a result, and can each be turned off. With them off, Loupe works offline.
- **Your keys stay on your device.** API keys and passwords you add are kept in the iOS Keychain or the macOS login Keychain.

## 3. What Loupe reads on your device

Every source is **off until you turn it on**, and the operating system asks for your permission first. Turning a source off removes its items from Loupe.

| Source | What is read | Where it stays |
|---|---|---|
| Photos (iPhone) | text recognised in images (on-device OCR), image metadata | on the device |
| Files and shared items | files and folders you choose, or send to Loupe with the Share button | on the device |
| Calendar (iPhone) | events (read only; Loupe never writes to your calendar) | on the device |
| Contacts (iPhone) | names, email addresses, phone numbers, used to spot impersonation | on the device |
| Mail | see section 4 | on the device |
| Folders (Mac) | file names, paths, sizes, dates and text of the folders you choose to scan | on the Mac |
| Web pages (Mac, browser extension) | see section 5 | on the Mac |

Loupe stores what it needs (the items it has read, its decisions, your corrections and settings) in the app's own storage on your device. Loupe Station's local server listens only on your Mac (`127.0.0.1` / `loupe.localhost`) and is not reachable from the internet.

## 4. Email

### Loupe for iPhone
- **Gmail (Google sign-in).** Loupe asks Google for one permission: **`gmail.readonly`** (read your email). It uses the Gmail API with read-only requests to download recent Inbox messages (the last 30 days, up to 200, then new ones). Messages go directly from Google to your iPhone and are stored only on your iPhone. Loupe cannot send, delete, move, label or mark mail as read. The sign-in token is kept in the iOS Keychain.
- **Other mail (IMAP).** With an app password you enter, Loupe reads mail over an encrypted connection directly from your provider (for example iCloud or Fastmail), without marking anything as read. The password stays in the iOS Keychain.
- **Microsoft / Outlook sign-in** is not yet available on iPhone.

### Loupe Station for Mac
Loupe Station can read mail and, only when you approve it, **add** `Laya/...` labels (categories on Outlook) and save a reply **draft** in the thread. It never sends, replies, forwards, deletes, archives, moves or marks mail as read.
- **Google (Gmail)** through a Google Cloud OAuth client that you create and enter yourself. Scopes: `gmail.readonly`, `gmail.labels` and `gmail.modify`. `gmail.modify` is needed only because Gmail requires it for adding a label; Loupe Station refuses every other change on your Mac before a request is sent. Reply drafts are saved with `users.drafts.create` and never sent; Loupe Station does not request `gmail.compose`.
- **Microsoft (Outlook, Microsoft 365)** through an Azure app you register. Delegated Microsoft Graph permissions: `offline_access`, `User.Read`, `Mail.ReadWrite`, `Mail.ReadWrite.Shared`. These are used to read mail, add categories and save drafts; Loupe Station never sends mail.
- **IMAP** with an app password.
- **Composio (optional).** Off unless you add a Composio key. If you choose "Log in via Composio", your Gmail or Outlook sign-in is held by Composio, Inc., and **the mail listing and message content for that account pass through Composio's servers, which store payloads under Composio's own terms**. This is the one mail option where a third party other than your mail provider handles your mail. Composio's privacy policy: <https://composio.dev/privacy>. Loupe Station's direct Google, Microsoft and IMAP options avoid this.

In all cases credentials are kept in the macOS login Keychain and mail travels between your Mac and your provider (or Composio, if you chose it). We never receive it.

### Google API Services: Limited Use
Loupe's use and transfer of information received from Google APIs to any other app will adhere to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements. In particular, Gmail data:
- is used only to provide the email features you see in Loupe (sorting, triage, phishing warnings, reminders and, if you turn it on, reply drafts);
- is **not** transferred to anyone, except to an AI provider you configure yourself, for the one email you preview and choose to send (section 6.5), or where needed for security or to comply with law;
- is **not** used for advertising, **not** sold, and **not** used to determine creditworthiness or for lending;
- is **not** used to develop, improve or train generalised AI or machine-learning models;
- is **not** read by any human at Loupe, unless you ask us to and agree (for example, you send us an email for support), it is needed for security (such as investigating abuse), or it is required by law. Because Gmail data stays on your device, in practice we have no access to it.

## 5. Browser protection (Loupe Station)
The Loupe Station browser extension (Chrome, Edge, Brave, Arc) talks only to Loupe Station on your Mac. On each page it sends to your Mac the address (without the `#` part), title, up to 4,000 characters of visible text, facts about forms (whether there is a password, card or email field and where the form posts), link counts and the site name. It **never** collects what you type, cookies, site storage, keystrokes or screenshots, and it skips private windows (unless you allow them), your trusted sites, local-network pages and browser pages. Page text is used in memory and never written. A history of checks is kept on your Mac (`browser.db`): time, host, a shortened path without query or ID segments, the verdict and reasons, a SHA-256 hash and length of the text, which browser, and any feedback you give — never the page text or title. It is kept for 30 days by default (adjustable from 1 to 365), purged at start-up and on each write, and **Clear history** deletes it at once. Separately, Loupe Station's decision ledger (`ledger.db`) keeps hashed page addresses and the decision model's answers with **no time limit by default**, until you set 30, 90, 180 or 365 days.

## 6. Optional online features
Each is **off by default**, has its own switch, and every result says **Online**, names its source and shows when it was fetched. They send the minimum needed for the request — never your files, photos, mail, decisions or corrections.

### 6.1 The Loupe web helper
A small fetch-only server we run at `loupe-web-helper-production.up.railway.app`, hosted by Railway Corporation. It fetches public facts and returns them; all decisions stay on your device. It:
- has no database and writes nothing to disk;
- logs only the method, route, status, duration and (for searches) the provider name and cache state — **never** your query, the domain, your IP address, your install ID, any key, or the results;
- receives a random install ID made by the app (`X-Loupe-Install`), used for rate limiting and to keep caches separate. It is held only in memory (as a keyed hash for caches). Loupe Station changes it monthly and when you tap "Forget cached facts";
- sees your IP address as any web server does; for domain checks a keyed hash of it is held in memory for rate limiting and never logged.

What goes through it:
- **Domain checks (phishing):** only one registrable domain (e.g. `example.com`, never the full address, page or email). The helper looks up registration data (RDAP registries, via IANA) and certificate logs (crt.sh) and keeps the answer in memory, per install, for **up to 6 hours**, never shared between installs and lost on restart.
- **Web searches (iPhone):** currency rates ([Frankfurter](https://frankfurter.dev), data from the European Central Bank and other central banks; cached up to 1 hour), weather ([Open-Meteo](https://open-meteo.com); place or coordinates you enter; up to 15 minutes) and UK live train boards ([National Rail Enquiries / Darwin](https://www.nationalrail.co.uk); station codes; up to 30 seconds). Caches are in memory and per install.
- **Flight search (iPhone):** your search and your own Duffel key are passed to [Duffel](https://duffel.com). The key is used only for that request and never stored or logged. Loupe shows offers; it never books or pays.

On Loupe Station, domain age can also be looked up **directly from your Mac** with the registry, and the helper route is off unless you set its address.

### 6.2 Phishing lists
The lists (Phishing.Database, MIT licence; optionally OpenPhish, off by default, and PhishTank) are **downloaded whole** to your device and matched there. Nothing about the links you visit is sent. When you turn the lists on, Phishing.Database is included by default. On iPhone, an optional DNS check sends a domain to your own DNS resolver, as any app opening a link would.

### 6.3 Google Safe Browsing (iPhone)
Uses **your own** Google API key. Your iPhone keeps Google's list of hash prefixes; only if a link matches it locally are **4-byte hash prefixes** sent to Google (Safe Browsing API v5) — never the link. Governed by [Google's Privacy Policy](https://policies.google.com/privacy). (On Loupe Station this option is not yet available.)

### 6.4 Loupe Decision Model download
The decision model (about 418 MB) is downloaded once, after you agree, on iPhone from [MODEL HOST], which receives a normal download request (your IP address, device type). On Mac, the model is downloaded from Hugging Face ([privacy policy](https://huggingface.co/privacy)) into `~/Library/Application Support/Loupe Station/models/hub`. Until a host is set, the iPhone app makes no request.

### 6.5 Writing assistant (off by default)
If you configure an AI provider, Loupe can draft replies or give a second opinion. Before anything is sent you see **exactly** what will be sent (on iPhone: the one email's own text, or one item's text and your question) and the provider's name; nothing is sent until you tap Send. Drafts are labelled and wait for your approval; Loupe never sends mail itself. The text goes to **the provider you chose, with your own key**: for example DeepSeek, or any OpenAI-compatible service such as OpenAI or OpenRouter, whose own terms and privacy policy then apply. Or you can use a model on your own Mac or network (such as Ollama), in which case nothing leaves it. Loupe Station also uses this for question drafting, folder-scan explanations and social-post drafts, and warns when a feature reading your mail or files would leave your Mac. The assistant never makes Loupe's decisions.

### 6.6 App updates (Loupe Station)
Loupe Station checks for updates with Sparkle at `https://loupe-ai.com/updates/appcast.xml`; updates are EdDSA-signed and downloaded from `loupe-ai.com/download/`. No system profile is sent; our server sees your IP address and a User-Agent containing the app and Sparkle versions. [WEBSITE HOST AND ITS LOG RETENTION] iPhone updates come through the App Store.

## 7. Data we hold
- On our side: only the transient, in-memory helper data in 6.1, and emails you send to privacy@loupe-ai.com, which we keep for [RETENTION PERIOD] to answer you.
- We do not use cookies or trackers on loupe-ai.com [CONFIRM FOR THE WEBSITE].
- Apple (App Store, TestFlight) and Microsoft/Google (for your accounts) process data under their own policies; we may receive aggregated App Store or TestFlight statistics and crash reports **only if you choose to share them with developers in your device settings** [CONFIRM].

## 8. Retention and deletion
- Everything Loupe keeps is on your device. **Deleting Loupe for iPhone deletes its app data.** Keys, passwords and sign-in tokens in the iOS Keychain **may remain after you delete the app**; to remove them, first remove keys under Me and sign out or remove mailboxes under Sources, then delete the app. On Mac, delete Loupe Station and its data folder `~/Library/Application Support/Loupe Station/` (files are readable only by your user account), and remove its items in Keychain Access.
- Removing a source or mailbox deletes its items (and its password).
- **Export my data** (iPhone: Me) gives you your decisions, corrections and settings as a zip file.
- Helper caches expire within 6 hours and vanish on restart.
- To disconnect Google: <https://myaccount.google.com/permissions>.

## 9. Security
Keys and passwords: Keychain (on iPhone, "when unlocked, this device only"). Network traffic: HTTPS/TLS. The helper stores no keys or queries. Downloaded model files are checked against pinned SHA-256 hashes. No method is perfect; if we learn of a security incident affecting you we will notify you and regulators as the law requires.

## 10. Children
Loupe is not directed to children under 13 (under 16 in the EEA and UK, or the higher age where you live — see section 13). We do not knowingly collect children's data; in any case we receive none.

## 11. International transfers
Using Loupe offline involves no transfer. The optional online features send the minimum request data to the helper on Railway ([RAILWAY REGION], operated by Railway Corporation, a United States company) and on to the providers in section 6, which may be in other countries, including the United States and the EU. Where the law requires, we rely on [adequacy decisions / Standard Contractual Clauses / your explicit request for the service — LAWYER TO CONFIRM]. Providers you configure yourself (AI, Composio, Google) are chosen by you.

## 12. Your rights — what they mean here
Wherever you live, you control your Loupe data directly: see, correct, export (Export my data) or delete it on your device. Because we hold no account, profile or copy of your content, a request to us for access or deletion will usually find nothing to return; we will tell you so and explain what we checked. Helper data cannot be linked to you and is gone within hours. You can still contact privacy@loupe-ai.com; we answer within one month (or the shorter legal period). We will not discriminate against you for exercising rights. You may complain to your data protection authority.

## 13. Regional information
Legal grounds we rely on (where the law uses them): **performance of a contract / providing the service you ask for** for the online features you turn on; **consent** for sources and features you switch on (withdraw by switching off); **legitimate interests** for rate-limiting and security of the helper. [LAWYER TO CONFIRM PER REGION]

| Region & law | Your rights | Children | Complaints / authority | Representative |
|---|---|---|---|---|
| **EU/EEA** — GDPR | access, rectification, erasure, restriction, portability, objection, withdraw consent (Arts 15–21, 7(3)) | 16 (member states may set 13–15; Art. 8) | your national DPA ([list](https://edpb.europa.eu/about-edpb/about-edpb/members_en)) | No EU representative appointed: we rely on the Art. 27(2) exemption (occasional, low-risk processing; your data stays on your device). A lawyer will confirm this before an EU launch. |
| **UK** — UK GDPR, DPA 2018 | as GDPR | 13 | [ICO](https://ico.org.uk/make-a-complaint/) | No UK representative appointed, on the same basis (UK GDPR Art. 27(2)); a lawyer will confirm this before a UK launch. |
| **California** — CCPA/CPRA | know, delete, correct, opt out of sale/sharing (we do neither), limit sensitive data use, non-discrimination | under 16: no sale (none happens) | [California Privacy Protection Agency](https://cppa.ca.gov) | — |
| **Other US states** (e.g. VA, CO, CT, TX) | similar rights to access, delete, correct, port, opt out; appeal a refusal by replying to our answer | 13 (COPPA) | your state Attorney General | — |
| **Egypt** — Law 151 of 2020 | know, access, correct, delete, object, be told of breaches | [VERIFY — child defined as under 18 under Egyptian law] | Personal Data Protection Centre | local licensing/representative: [VERIFY/DECIDE] |
| **Saudi Arabia** — PDPL | be informed, access, copy, correct, destroy | [VERIFY — guardian consent for those lacking full capacity] | SDAIA | local representative: [VERIFY/DECIDE] |
| **UAE** — Federal Decree-Law 45/2021 | access, portability, correction, erasure, restriction, objection | [VERIFY] | UAE Data Office | [VERIFY/DECIDE] |
| **Brazil** — LGPD | confirmation, access, correction, anonymisation/deletion, portability, information on sharing, revoke consent (Art. 18) | under 12 need parental consent (Art. 14) | [ANPD](https://www.gov.br/anpd) | encarregado (DPO): Hany Sadek (privacy@loupe-ai.com) |
| **Canada** — PIPEDA (and Québec Law 25) | access, correction, withdraw consent | [VERIFY — 13 / 14 in Québec] | [Office of the Privacy Commissioner](https://www.priv.gc.ca) | privacy officer: Hany Sadek (privacy@loupe-ai.com) |
| **Australia** — Privacy Act 1988 | access, correction (APPs 12–13) | [VERIFY] | [OAIC](https://www.oaic.gov.au) (complain to us first) | — (may be exempt as small business; [LAWYER TO CONFIRM]) |
| **India** — DPDP Act 2023 | access to information, correction, erasure, grievance redress, nominate someone | under 18: verifiable parental consent (s. 9) | our grievance contact privacy@loupe-ai.com, then the Data Protection Board of India | — |

An Arabic translation is available at loupe-ai.com/privacy/ar. If the versions differ, the English version controls.

## 14. Changes
We will post changes here with a new effective date and, for material changes, say so in the app before they apply.

## 15. Contact
Hany Sadek, trading as Loupe · Hurghada, Egypt · privacy@loupe-ai.com
