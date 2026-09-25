#!/usr/bin/env python3
"""Builds the static site (English + Arabic) from tools/content.py and the legal Markdown in legal/.
Run: python3 tools/build.py   (needs: pip install markdown)"""
import json, os, re, html
import markdown
from content import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://loupe-ai.com"
L = {"en": EN, "ar": AR}
ASSET_V = "4"

def esc(s): return html.escape(s, quote=True)

def url(lang, path):
    return (L[lang]["prefix"] + path) if path != "/" or lang == "en" else L[lang]["prefix"] + "/"

def head(lang, path, title, desc, extra=""):
    t = L[lang]
    other = t["other"]
    return f"""<!doctype html>
<html lang="{lang}" dir="{t['dir']}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#070B18">
<link rel="canonical" href="{SITE}{url(lang, path)}">
<link rel="alternate" hreflang="en" href="{SITE}{url('en', path)}">
<link rel="alternate" hreflang="ar" href="{SITE}{url('ar', path)}">
<link rel="alternate" hreflang="x-default" href="{SITE}{url('en', path)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Loupe">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{url(lang, path)}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{'ar_EG' if lang=='ar' else 'en_GB'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
{'<link rel="preload" href="/assets/fonts/rajdhani-latin-700.woff2" as="font" type="font/woff2" crossorigin>' if lang=='en' else ''}
{'<link rel="preload" href="/assets/fonts/noto-kufi-arabic-arabic.woff2" as="font" type="font/woff2" crossorigin>' if lang=='ar' else ''}
<link rel="stylesheet" href="/assets/css/fonts.css?v={ASSET_V}">
<link rel="stylesheet" href="/assets/css/site.css?v={ASSET_V}">
{extra}
<script type="application/json" id="i18n">{json.dumps(t['js'], ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
"""

def header(lang, path):
    t = L[lang]
    def a(p, label):
        cur = ' aria-current="page"' if p == path else ''
        return f'<a href="{url(lang, p)}"{cur}>{label}</a>'
    return f"""<header class="site-head">
<div class="wrap">
<a class="brand" href="{url(lang, '/')}" aria-label="Loupe — {'الرئيسية' if lang=='ar' else 'home'}"><img src="/assets/img/loupe-wordmark.webp" alt="Loupe" width="112" height="22"></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">{t['menu']}</button>
<nav id="nav" class="nav" aria-label="{'الرئيسية' if lang=='ar' else 'Main'}">
{a('/features/', t['nav']['features'])}
{a('/download/', t['nav']['download'])}
{a('/privacy/', t['nav']['privacy'])}
<a class="lang" href="{url(t['other'], path)}" hreflang="{t['other']}" lang="{t['other']}">{t['other_label']}</a>
<a class="btn btn-primary" href="{url(lang, '/download/')}#waitlist" style="min-height:40px;padding:8px 16px">{t['cta_wait']}</a>
</nav>
</div>
</header>
"""

def footer(lang, scripts=()):
    t = L[lang]
    ar = lang == 'ar'
    s = "\n".join(f'<script src="{x}?v={ASSET_V}" defer></script>' for x in ("/assets/config.js", "/assets/js/main.js") + tuple(scripts))
    return f"""<footer class="site-foot">
<div class="wrap">
<div><img src="/assets/img/loupe-wordmark.webp" alt="Loupe" width="112" height="22" loading="lazy" style="height:22px;width:auto;margin-bottom:14px"><p>{t['foot_tag']}</p><p>{t['foot_copy']}<br><a href="mailto:privacy@loupe-ai.com">privacy@loupe-ai.com</a></p></div>
<div><h2>{t['foot_prod']}</h2><ul>
<li><a href="{url(lang,'/features/')}">{t['nav']['features']}</a></li>
<li><a href="{url(lang,'/download/')}">{t['nav']['download']}</a></li>
<li><a href="{url(lang,'/download/')}#waitlist">{t['cta_wait']}</a></li></ul></div>
<div><h2>{t['foot_legal']}</h2><ul>
<li><a href="{url(lang,'/privacy/')}">{'سياسة الخصوصية' if ar else 'Privacy policy'}</a></li>
<li><a href="{url(lang,'/terms/')}">{'شروط الخدمة' if ar else 'Terms of service'}</a></li>
<li><a href="{url(t['other'],'/')}" lang="{t['other']}" hreflang="{t['other']}">{t['other_label']}</a></li></ul></div>
</div>
</footer>
{s}
</body>
</html>
"""

APPLE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.4 12.6c0-2.6 2.1-3.8 2.2-3.9-1.2-1.8-3.1-2-3.7-2-1.6-.2-3.1.9-3.9.9-.8 0-2-.9-3.3-.9-1.7 0-3.3 1-4.2 2.5-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8 1.6 0 2 .8 3.4.8 1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9 0 0-2.8-1-2.8-4zM13.9 5c.7-.9 1.2-2 1-3.2-1 0-2.3.7-3 1.6-.7.8-1.2 2-1.1 3.1 1.2.1 2.3-.6 3.1-1.5z"/></svg>'

def mac_button(lang):
    t = L[lang]['js']
    return f'<a class="btn btn-primary" href="{t["waitlistHref"]}" data-download="mac" data-platform="mac" aria-disabled="true">{APPLE.replace("<svg", "<svg width=22 height=22")}<span class="btn-stack"><span class="lbl">{t["macSoon"]}</span><small>{t["macSoonSub"]}</small></span></a>'

def ios_badge(lang):
    t = L[lang]['js']
    return f'<a class="appstore" href="{t["waitlistHref"]}" data-download="ios" data-platform="ios" aria-disabled="true">{APPLE}<span><span class="top">{t["iosSoonTop"]}</span><b>App Store</b></span></a>'

def waitlist_form(lang):
    f = FORM[lang]
    plats = [("android","Android"),("windows","Windows"),("linux","Linux"),("iphone","iPhone"),("mac","Mac")]
    chips = "".join(f'<label class="chip"><input type="checkbox" name="platforms" value="{v}"><span>{n}</span></label>' for v, n in plats)
    ci = 1 if lang == 'en' else 2
    countries = "".join(f'<option value="{c[0]}">{esc(c[ci])}</option>' for c in COUNTRIES)
    cons = "".join(f'<label class="check"><input type="checkbox" name="c_{k}"><span id="t_{k}">{esc(v)}</span></label>' for k, v in f['c'].items())
    return f"""<form id="waitlist-form" class="form" novalidate>
<div class="row2">
<div class="field"><label for="wl-email">{f['email']} <span class="hint">{f['email_hint']}</span></label><input id="wl-email" name="email" type="email" required autocomplete="email" inputmode="email" maxlength="254"></div>
<div class="field"><label for="wl-name">{f['name']} <span class="hint">{f['name_hint']}</span></label><input id="wl-name" name="name" type="text" autocomplete="name" maxlength="120"></div>
</div>
<fieldset class="field"><legend>{f['platforms']}</legend><div class="chips">{chips}</div></fieldset>
<div class="row2">
<div class="field"><label for="wl-country">{f['country']}</label><select id="wl-country" name="country"><option value="">{f['country_none']}</option>{countries}</select></div>
<div class="field"><label for="wl-lang">{f['language']}</label><select id="wl-lang" name="language"><option value="en"{' selected' if lang=='en' else ''}>English</option><option value="ar"{' selected' if lang=='ar' else ''}>العربية</option></select></div>
</div>
<fieldset class="consents"><legend class="field" style="font-weight:600;padding:0 4px">{f['consent_h']}</legend>{cons}</fieldset>
<label class="check"><input type="checkbox" name="ack_privacy" required><span><span id="t_ack">{f['ack']}</span> <b>{f['ack_req']}</b></span></label>
<div class="hp" aria-hidden="true"><label>Website <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<div><button class="btn btn-primary" type="submit">{f['submit']}</button></div>
<p class="form-status" role="status" aria-live="polite"></p>
<p class="small">{f['fine']}</p>
</form>"""

def platforms(lang, with_form=True):
    d = DOWNLOAD[lang]; ar = lang == 'ar'
    soon = "".join(f'<div class="plat"><h3>{n}</h3><span class="pill soon">{d["soon"]}</span><p>{d["soon_p"]}</p><a href="#waitlist" class="btn btn-ghost">{L[lang]["cta_wait"]}</a></div>' for n in ("Android", "Windows", "Linux"))
    return f"""<div class="plat-grid">
<div class="plat"><h3>Loupe Station <span class="small">· Mac</span></h3><p>{d['mac_p']}</p><div class="req">{d['mac_req']}</div>{mac_button(lang)}</div>
<div class="plat"><h3>Loupe <span class="small">· iPhone</span></h3><p>{d['ios_p']}</p><div class="req">{d['ios_req']}</div><div>{ios_badge(lang)}</div></div>
{soon}
</div>"""

def page_home(lang):
    h = HOME[lang]; t = L[lang]; ar = lang == 'ar'
    stats = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in h['stats'])
    diffs = ""
    for i, (ic, title, body, fact) in enumerate(DIFFS[lang]):
        lead = " lead" if i < 2 else ""
        diffs += f'<article class="card reveal{lead}"><span class="num mono">{i+1:02d}</span><div class="ico">{ICONS[ic]}</div><h3>{title}</h3><p>{body}</p><span class="fact">{fact}</span></article>'
    demo_btns = "".join(f'<button type="button" class="judg" aria-pressed="false">{esc(j["q"])}<small>{esc(j["sub"])}</small></button>' for j in DEMO[lang])
    demo_json = json.dumps({"judgments": DEMO[lang], "l": h['demo_l']}, ensure_ascii=False)
    b = h['demo_bins']
    watch = "".join(f'<article class="finding reveal"><span class="tag">{tag}</span> <span class="pill demo">{h["watch_sample"]}</span><div class="big">{big}</div><div class="ev">{ev}</div></article>' for tag, big, ev in h['watchers'])
    rstats = "".join(f'<div class="stat"><b>{a}</b><span>{b2}</span></div>' for a, b2 in h['run_stats'])
    tabs = ""; imgs = ""
    for i, (key, lab, cap) in enumerate(h['shots']):
        tabs += f'<button role="tab" id="tab-{key}" aria-controls="shot-panel" aria-selected="{"true" if i==0 else "false"}" data-cap="{esc(cap)}">{lab}</button>'
        srcattr = 'src' if i == 0 else 'data-src'; ssattr = 'srcset' if i == 0 else 'data-srcset'
        imgs += f'<img {srcattr}="/assets/img/shots/{key}-360.webp" {ssattr}="/assets/img/shots/{key}-360.webp 360w, /assets/img/shots/{key}-720.webp 720w" sizes="300px" alt="{esc(cap)}" width="360" height="782" loading="lazy" decoding="async"{" class=on" if i==0 else ""}>'
    hon = "".join(f"<li>{x}</li>" for x in h['hon'])
    pl = "".join(f"<li>{x}</li>" for x in h['priv_list'])
    canvas_labels = esc(json.dumps(h['canvas'], ensure_ascii=False))
    body = f"""{header(lang, '/')}
<main id="main">
<section class="hero grid-bg">
<div class="wrap">
<div>
<p class="eyebrow"><span class="live-dot" aria-hidden="true"></span>{h['eyebrow']}</p>
<h1>{h['h1']}</h1>
<p class="lede">{h['lede']}</p>
<div class="cta-row">{mac_button(lang)}{ios_badge(lang)}</div>
<div class="hero-stats">{stats}</div>
</div>
<div class="stage" role="img" aria-label="{esc(h['stage_caption'])}">
<canvas id="pipeline" data-labels="{canvas_labels}"></canvas>
<picture><source srcset="/assets/img/mascot-320.webp" type="image/webp"><img class="mascot" src="/assets/img/mascot-320.png" alt="" width="287" height="320" fetchpriority="high"></picture>
<div class="stage-hud mono" aria-hidden="true"><b id="hud-count">0</b> {h['hud'][0]}<br><b id="hud-rate">0.0</b> {h['hud'][1]}</div>
<p class="stage-caption">{h['stage_caption']}</p>
</div>
</div>
</section>

<section id="different">
<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">{h['diff_eyebrow']}</p><h2>{h['diff_h']}</h2><p>{h['diff_p']}</p></div>
<div class="diff-grid">{diffs}</div>
</div>
</section>

<section id="demo-sec" class="alt">
<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">{h['demo_eyebrow']}</p><h2>{h['demo_h']}</h2><p>{h['demo_p']}</p></div>
<div class="demo" id="demo">
<div class="judg-list" role="group" aria-label="{h['demo_h']}">{demo_btns}</div>
<div class="demo-panel">
<div class="demo-top"><span class="demo-q"></span><span class="pill demo">{h['demo_label']}</span></div>
<div class="feed mono" aria-hidden="true"></div>
<div class="bins">
<div class="bin yes"><h4><span>{b[0]}</span><span class="c">0</span></h4><ul></ul></div>
<div class="bin no"><h4><span>{b[1]}</span><span class="c">0</span></h4><ul></ul></div>
<div class="bin unsure"><h4><span>{b[2]}</span><span class="c">0</span></h4><ul></ul></div>
</div>
<div class="demo-foot"></div>
<p class="sr-only" aria-live="polite"></p>
<p class="small" style="margin:14px 0 0">{h['demo_note']}</p>
</div>
</div>
<script type="application/json" id="demo-data">{demo_json}</script>
</div>
</section>

<section id="privacy-sec">
<div class="wrap meter-wrap">
<div class="reveal">
<p class="eyebrow">{h['priv_eyebrow']}</p><h2>{h['priv_h']}</h2><p style="color:var(--ink2)">{h['priv_p']}</p>
<ul style="color:var(--ink2);padding-inline-start:20px">{pl}</ul>
<label class="toggle"><input type="checkbox" id="airplane" role="switch"> <span>✈ {h['priv_toggle']}</span></label>
<div class="netlog" id="netlog" aria-live="off"></div>
</div>
<div class="meter" id="meter" role="img" aria-label="{esc(h['priv_meter_label'])}">
<svg viewBox="0 0 220 220" aria-hidden="true">
<defs><linearGradient id="mg" x1="0" x2="1"><stop offset="0" stop-color="#2F6BFF"/><stop offset="1" stop-color="#22D3EE"/></linearGradient></defs>
<circle cx="110" cy="110" r="90" fill="none" stroke="#13235A" stroke-width="14"/>
<circle class="arc" cx="110" cy="110" r="90" fill="none" stroke="url(#mg)" stroke-width="14" stroke-linecap="round" stroke-dasharray="565" stroke-dashoffset="565" transform="rotate(-90 110 110)" style="transition:stroke-dashoffset .3s"/>
<circle cx="110" cy="110" r="70" fill="none" stroke="#1E3170" stroke-dasharray="2 6"/>
</svg>
<div class="readout"><b class="mono">0</b><span>{h['priv_meter_unit']}</span><span style="color:var(--ink3);margin-top:10px"><span id="ops">0</span> {h['priv_meter_sub']}</span></div>
</div>
</div>
</section>

<section id="watchers" class="alt">
<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">{h['watch_eyebrow']}</p><h2>{h['watch_h']}</h2><p>{h['watch_p']}</p></div>
<div class="watch-grid">{watch}</div>
<p class="note" style="margin-top:22px">{h['watch_note']}</p>
</div>
</section>

<section id="live">
<div class="wrap split">
<div class="reveal">
<p class="eyebrow">{h['run_eyebrow']}</p><h2>{h['run_h']}</h2><p style="color:var(--ink2)">{h['run_p']}</p><p style="color:var(--ink2)">{h['run_p2']}</p>
<div class="stats">{rstats}</div>
<p class="small">{h['run_src']}</p>
<p class="note">{h['run_honest']}</p>
</div>
<div class="reveal" style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
<div class="phone" style="width:min(250px,42vw)"><div class="screen"><img class="on" src="/assets/img/shots/live-run-360.webp" srcset="/assets/img/shots/live-run-360.webp 360w, /assets/img/shots/live-run-720.webp 720w" sizes="250px" alt="{esc(h['shots'][1][2])}" width="360" height="782" loading="lazy" decoding="async"></div></div>
<div class="phone" style="width:min(250px,42vw)"><div class="screen"><img class="on" src="/assets/img/shots/game-360.webp" srcset="/assets/img/shots/game-360.webp 360w, /assets/img/shots/game-720.webp 720w" sizes="250px" alt="{esc(h['shots'][2][2])}" width="360" height="782" loading="lazy" decoding="async"></div></div>
</div>
</div>
</section>

<section id="devices" class="alt">
<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">{h['dev_eyebrow']}</p><h2>{h['dev_h']}</h2><p>{h['dev_p']}</p></div>
<div class="devices" data-carousel>
<div class="phone"><div class="screen" id="shot-panel" role="tabpanel" aria-live="polite">{imgs}</div></div>
<div>
<div class="car-ctl" role="tablist" aria-label="{h['dev_h']}">{tabs}</div>
<p class="car-cap"></p>
<div class="mac" style="margin-top:22px"><div class="screen"><div class="ph"><img src="/assets/img/mascot-320.webp" alt="" width="90" height="100" loading="lazy">{h['mac_ph']}</div></div><div class="base"></div></div>
</div>
</div>
</div>
</section>

<section id="honest">
<div class="wrap">
<div class="honest reveal"><p class="eyebrow" style="color:var(--amber)">{h['hon_eyebrow']}</p><h2>{h['hon_h']}</h2><ul>{hon}</ul></div>
</div>
</section>

<section id="get" class="alt">
<div class="wrap">
<div class="sec-head reveal"><p class="eyebrow">{h['plat_eyebrow']}</p><h2>{h['plat_h']}</h2></div>
{platforms(lang)}
<div id="waitlist" style="margin-top:56px;scroll-margin-top:80px">
<div class="sec-head"><h2>{h['wait_h']}</h2><p>{h['wait_p']}</p></div>
{waitlist_form(lang)}
</div>
</div>
</section>
</main>
"""
    return head(lang, '/', h['title'], t['site_desc']) + body + footer(lang, ("/assets/js/hero.js", "/assets/js/demo.js", "/assets/js/waitlist.js"))

def page_features(lang):
    F = FEATURES[lang]; h = HOME[lang]
    diffs = "".join(f'<article class="card reveal"><span class="num mono">{i+1:02d}</span><div class="ico">{ICONS[ic]}</div><h3>{ti}</h3><p>{bo}</p><span class="fact">{fa}</span></article>' for i, (ic, ti, bo, fa) in enumerate(DIFFS[lang]))
    lst = lambda items: "".join(f"<li><b>{a}</b>{b}</li>" for a, b in items)
    body = f"""{header(lang, '/features/')}
<main id="main">
<section class="page-hero grid-bg"><div class="wrap"><p class="eyebrow">{h['diff_eyebrow']}</p><h1>{F['h1']}</h1><p>{F['lede']}</p></div></section>
<section style="padding-top:30px"><div class="wrap"><div class="diff-grid">{diffs}</div></div></section>
<section class="alt"><div class="wrap feat-cols">
<div><h2>{F['ios_h']}</h2><p class="small mono">{F['ios_sub']}</p><ul class="feat-list">{lst(F['ios'])}</ul></div>
<div><h2>{F['mac_h']}</h2><p class="small mono">{F['mac_sub']}</p><ul class="feat-list">{lst(F['mac'])}</ul></div>
</div></section>
<section><div class="wrap"><div class="honest"><p class="eyebrow" style="color:var(--amber)">{h['hon_eyebrow']}</p><h2>{h['hon_h']}</h2><ul>{"".join(f"<li>{x}</li>" for x in h['hon'])}</ul></div>
<div class="cta-row" style="margin-top:32px">{mac_button(lang)}{ios_badge(lang)}</div></div></section>
</main>
"""
    return head(lang, '/features/', F['title'], L[lang]['site_desc']) + body + footer(lang)

def page_download(lang):
    D = DOWNLOAD[lang]; h = HOME[lang]
    body = f"""{header(lang, '/download/')}
<main id="main">
<section class="page-hero grid-bg"><div class="wrap"><p class="eyebrow"><span class="live-dot" aria-hidden="true"></span>{h['plat_eyebrow']}</p><h1>{D['h1']}</h1><p>{D['lede']}</p></div></section>
<section style="padding-top:30px"><div class="wrap">{platforms(lang)}
<div id="waitlist" style="margin-top:56px;scroll-margin-top:80px"><div class="sec-head"><h2>{h['wait_h']}</h2><p>{h['wait_p']}</p></div>{waitlist_form(lang)}</div>
</div></section>
</main>
"""
    return head(lang, '/download/', D['title'], L[lang]['site_desc']) + body + footer(lang, ("/assets/js/waitlist.js",))

def legal_html(lang, kind):
    src = os.path.join(ROOT, "legal", f"{kind}{'.ar' if lang=='ar' else ''}.md")
    md = open(src, encoding="utf-8").read()
    lines = md.split("\n")
    title = lines[0].lstrip("# ").strip()
    md = "\n".join(lines[1:])
    # the draft notice becomes the site's banner
    md = re.sub(r"^\*\*(Draft for review[^\n]*|مسودة للمراجعة[^\n]*)\*\*\s*$", "", md, count=1, flags=re.M)
    md = md.replace("loupe-ai.com/privacy/ar", "loupe-ai.com/ar/privacy/").replace("(https://loupe-ai.com/privacy)", "(/privacy/)")
    md = md.replace("We do not use cookies or trackers on loupe-ai.com [CONFIRM FOR THE WEBSITE].",
                    "The website uses no cookies, analytics or trackers. It does keep the waitlist sign-ups and download counts described in [The website](#website) below — separate from the apps, which collect nothing.")
    out = markdown.markdown(md, extensions=["tables", "sane_lists"])
    out = out.replace("<table>", '<div class="table-scroll"><table>').replace("</table>", "</table></div>")
    if kind == "privacy":
        marker = re.search(r"<h2>(14\. Changes|10\. التغييرات)", out)
        block = WEBSITE_PRIVACY[lang]
        out = out[:marker.start()] + block + out[marker.start():] if marker else out + block
    return title, out

def page_legal(lang, kind):
    title, content = legal_html(lang, kind)
    path = f"/{kind}/"
    note = ("مسودة — قيد المراجعة القانونية. ليست سارية بعد. النسخة الإنجليزية هي المعتمدة." if lang == 'ar'
            else "Draft — under legal review. Not yet in force.")
    sep = ("<p class=\"small\">التطبيقات لا تجمع شيئًا عنك؛ ما يحفظه الموقع (التسجيل وأعداد التنزيل) موضّح في قسم <a href=\"#website\">الموقع</a>.</p>" if lang == 'ar'
           else "<p class=\"small\">The apps collect nothing about you; what the website keeps (sign-ups and download counts) is set out separately in <a href=\"#website\">The website</a>.</p>") if kind == "privacy" else ""
    body = f"""{header(lang, path)}
<main id="main">
<section class="page-hero"><div class="wrap legal">
<div class="draft" role="note"><span aria-hidden="true">⚠</span><span>{note}</span></div>
<h1>{esc(title)}</h1>{sep}
{content}
</div></section>
</main>
"""
    return head(lang, path, f"{title} — Loupe", L[lang]['site_desc']) + body + footer(lang)

def page_404():
    n = NOTFOUND['en']; a = NOTFOUND['ar']
    body = f"""{header('en', '/404')}
<main id="main"><section class="page-hero grid-bg"><div class="wrap" style="text-align:center">
<img src="/assets/img/mascot-320.webp" alt="" width="200" height="223" style="margin:0 auto 20px;width:200px">
<p class="eyebrow mono">404 · confidence 0.99</p><h1>{n['h1']}</h1><p style="margin-inline:auto">{n['p']}</p>
<div class="cta-row" style="justify-content:center"><a class="btn btn-primary" href="/">{n['home']}</a><a class="btn btn-ghost" href="/features/">Features</a></div>
<p lang="ar" dir="rtl" style="margin-top:40px">{a['p']} <a href="/ar/">{a['home']}</a></p>
</div></section></main>
"""
    return head('en', '/404', n['title'], EN['site_desc'], '<meta name="robots" content="noindex">') + body + footer('en')

def write(rel, s):
    p = os.path.join(ROOT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)

def main():
    for lang in ("en", "ar"):
        pre = "" if lang == "en" else "ar/"
        write(pre + "index.html", page_home(lang))
        write(pre + "features/index.html", page_features(lang))
        write(pre + "download/index.html", page_download(lang))
        write(pre + "privacy/index.html", page_legal(lang, "privacy"))
        write(pre + "terms/index.html", page_legal(lang, "terms"))
    write("404.html", page_404())
    urls = []
    for p in ("/", "/features/", "/download/", "/privacy/", "/terms/"):
        for lang in ("en", "ar"):
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l2}" href="{SITE}{url(l2, p)}"/>' for l2 in ("en", "ar"))
            urls.append(f"<url><loc>{SITE}{url(lang, p)}</loc>{alts}</url>")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    print("built")

if __name__ == "__main__":
    main()
