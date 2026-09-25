# -*- coding: utf-8 -*-
"""All site copy, English and Arabic. Honest numbers only: every figure here is a measurement from
jevistication/docs/BUILD.md, ios/README.md or laya-studio/README.md, and says where it was measured."""

CONSENT_VERSION = "2026-09-25.v1"

EN = {
  "lang": "en", "dir": "ltr", "prefix": "", "other": "ar", "other_label": "العربية", "other_name": "Arabic",
  "skip": "Skip to content", "menu": "Menu",
  "nav": {"features": "Features", "download": "Download", "privacy": "Privacy"},
  "cta_wait": "Join the waitlist",
  "site_desc": "Loupe is an on-device decision engine. Teach it judgments in plain words; it applies them across your photos, files, mail, calendar and contacts, shows what it's unsure about, and nothing leaves your device.",
  "foot_tag": "An on-device decision engine. Judgments in plain words, decided on your device.",
  "foot_prod": "Product", "foot_legal": "Legal",
  "foot_copy": "© 2026 Hany Sadek, trading as Loupe · Hurghada, Egypt",
  "foot_contact": "privacy@loupe-ai.com",
  "draft_badge": "Draft — under legal review",
  # JS strings
  "js": {
    "macDownload": "Download for Mac", "macReq": "macOS 14+ · Apple Silicon",
    "macSoon": "Loupe Station — coming soon", "macSoonSub": "Join the waitlist to hear first",
    "iosTop": "Download on the", "iosSoonTop": "Coming to the",
    "waitlistHref": "/download/#waitlist",
    "log": ["<span class='dim'>read</span>   receipt-0412.pdf   <span class='ok'>on device</span>",
            "<span class='dim'>ocr</span>    IMG_2231.HEIC      <span class='ok'>on device</span>",
            "<span class='dim'>ask</span>    \"receipt for tax?\" <span class='ok'>Laya · local</span>",
            "<span class='dim'>check</span>  passport scan      <span class='ok'>masked</span>",
            "<span class='dim'>net</span>    requests: 0        <span class='ok'>0 B out</span>",
            "<span class='dim'>ledger</span> +1 row             <span class='ok'>this device</span>",
            "<span class='dim'>queue</span>  2 need you         <span class='ok'>local</span>"],
    "logDone": "done · 1,200 local steps · 0 bytes out",
    "airOn": "✈ airplane mode on — still deciding. 0 bytes out.",
    "airOff": "airplane mode off — still 0 bytes out (online sources are off by default).",
    "errEmail": "Please enter a valid email address.",
    "errAck": "Please confirm you have read the privacy policy.",
    "errRate": "Too many sign-ups from here just now. Please try again in a few minutes.",
    "errGeneric": "Something went wrong. Please try again, or email privacy@loupe-ai.com.",
    "notConfigured": "Sign-ups are not open yet (the site's backend is not connected). Please check back soon.",
    "sending": "Sending…",
    "ok": "Almost done — check your email to confirm. Nothing is sent to you until you click the link.",
    "toast_confirmed": "You're confirmed. Thanks — we'll only email you about what you ticked.",
    "toast_unsubscribed": "You're unsubscribed. We won't email you again.",
    "toast_invalid": "That link has expired or was already used.",
  },
}

AR = {
  "lang": "ar", "dir": "rtl", "prefix": "/ar", "other": "en", "other_label": "English", "other_name": "English",
  "skip": "انتقل إلى المحتوى", "menu": "القائمة",
  "nav": {"features": "الميزات", "download": "التنزيل", "privacy": "الخصوصية"},
  "cta_wait": "انضم إلى قائمة الانتظار",
  "site_desc": "Loupe محرّك قرارات يعمل على جهازك. علّمه أحكامًا بكلمات بسيطة فيطبّقها على صورك وملفاتك وبريدك وتقويمك وجهات اتصالك، ويُريك ما لا يثق به، ولا يغادر جهازك شيء.",
  "foot_tag": "محرّك قرارات على جهازك. أحكام بكلمات بسيطة، تُقرَّر على جهازك.",
  "foot_prod": "المنتج", "foot_legal": "قانوني",
  "foot_copy": "© 2026 هاني صادق، بالاسم التجاري Loupe · الغردقة، مصر",
  "foot_contact": "privacy@loupe-ai.com",
  "draft_badge": "مسودة — قيد المراجعة القانونية",
  "js": {
    "macDownload": "تنزيل لأجهزة Mac", "macReq": "macOS 14 أو أحدث · Apple Silicon",
    "macSoon": "Loupe Station — قريبًا", "macSoonSub": "انضم إلى قائمة الانتظار لتعرف أولًا",
    "iosTop": "حمّله من", "iosSoonTop": "قريبًا على",
    "waitlistHref": "/ar/download/#waitlist",
    "log": ["<span class='dim'>قراءة</span>  receipt-0412.pdf   <span class='ok'>على الجهاز</span>",
            "<span class='dim'>OCR</span>    IMG_2231.HEIC      <span class='ok'>على الجهاز</span>",
            "<span class='dim'>سؤال</span>   «إيصال للضرائب؟»   <span class='ok'>Laya · محلي</span>",
            "<span class='dim'>فحص</span>    صورة جواز سفر      <span class='ok'>مُقنَّع</span>",
            "<span class='dim'>شبكة</span>   الطلبات: 0         <span class='ok'>0 بايت للخارج</span>",
            "<span class='dim'>سجل</span>    +1 صف              <span class='ok'>هذا الجهاز</span>",
            "<span class='dim'>طابور</span>  2 تحتاجك           <span class='ok'>محلي</span>"],
    "logDone": "انتهى · 1,200 خطوة محلية · 0 بايت للخارج",
    "airOn": "✈ وضع الطيران مفعّل — ما زال يقرّر. 0 بايت للخارج.",
    "airOff": "وضع الطيران متوقف — وما زال 0 بايت للخارج (المصادر المتصلة بالإنترنت متوقفة افتراضيًا).",
    "errEmail": "يرجى إدخال بريد إلكتروني صحيح.",
    "errAck": "يرجى تأكيد أنك قرأت سياسة الخصوصية.",
    "errRate": "عدد كبير من التسجيلات من هنا الآن. حاول مرة أخرى بعد دقائق.",
    "errGeneric": "حدث خطأ. حاول مرة أخرى أو راسلنا على privacy@loupe-ai.com.",
    "notConfigured": "التسجيل غير مفتوح بعد (لم تُربط الواجهة الخلفية للموقع). عُد قريبًا.",
    "sending": "جارٍ الإرسال…",
    "ok": "خطوة أخيرة — افحص بريدك لتأكيد الاشتراك. لن نرسل لك شيئًا قبل أن تضغط الرابط.",
    "toast_confirmed": "تم التأكيد. شكرًا — لن نراسلك إلا بما اخترته.",
    "toast_unsubscribed": "تم إلغاء اشتراكك. لن نراسلك مجددًا.",
    "toast_invalid": "انتهت صلاحية هذا الرابط أو استُخدم من قبل.",
  },
}

# ---------------------------------------------------------------- home
HOME = {
 "en": {
  "title": "Loupe — judgments in plain words, decided on your device",
  "eyebrow": "On-device decision engine",
  "h1": "Teach it a judgment.<br><span class=\"accent\">It decides on your device.</span>",
  "lede": "Write what you care about in plain words — “receipts I'll need at tax time”, “is this really from my bank?”. Loupe applies it across your photos, files, mail, calendar and contacts, shows you what it's unsure about, learns from your answers, and nothing leaves the device.",
  "cta_mac": "Download for Mac", "cta_ios_top": "Coming to the",
  "stats": [("10–14", "decisions/s · iPhone simulator, measured"), ("0 B", "sent from your stuff"), ("100+", "languages the model reads")],
  "stage_caption": "Illustration of the app's live run view, animated in your browser",
  "hud": ["items decided", "per second"],
  "canvas": {"read": "Read", "decide": "Decide", "q1": "receipt?", "q2": "for tax?", "q3": "sure?", "sorted": "Sorted", "needs": "Needs you", "flag": "Flagged",
             "answers": [["yes", "no"], ["yes", "no"], ["sure", "unsure"]]},
  "mascot_alt": "Loupe's robot mascot, the engine at the centre of the live run view",

  "diff_eyebrow": "What makes it different",
  "diff_h": "Ten things no cloud assistant can promise",
  "diff_p": "Loupe is not a chatbot. It doesn't write about your data — it makes typed decisions (yes/no, pick one, score) with a small model that runs where your data already is.",

  "demo_eyebrow": "Try it",
  "demo_h": "Teach a judgment, watch it sort",
  "demo_p": "Pick a judgment. The items below sort into “yes”, “no” and “needs you”, with a confidence bar and the keyword rule's answer beside each — the way the app shows results.",
  "demo_label": "Demo · made-up items · scripted answers, not the model",
  "demo_bins": ["Yes", "No", "Needs you"],
  "demo_l": {"yes": "yes", "no": "no", "unsure": "unsure", "kw": "keyword rule", "reading": "reading", "done": "done · every answer stays in this browser",
             "decided": "decided", "queue": "sent to you", "agreeKw": "agrees with keyword rule",
             "summary": "Sorted. {d} decided, {u} sent to you, {a} agree with the keyword rule."},
  "demo_note": "In the real app the keyword rule is measured against your own corrections, and when it wins, Loupe tells you and offers to use it.",

  "priv_eyebrow": "Privacy you can check",
  "priv_h": "0 bytes out. Turn on airplane mode — it still works.",
  "priv_p": "Laya, the decision model, runs on your iPhone or Mac. Your photos, files, calendar and contacts are read there and are not sent to us or anyone else. No account. No analytics, advertising or crash-reporting SDKs.",
  "priv_list": ["Every source is off until you turn it on — and the system asks first.",
                "Online extras (mail, web templates, phishing lists, the writing assistant) are off by default, labelled <b>Online</b> with their source and time, and each has its own switch.",
                "Your keys stay in the Keychain on your device."],
  "priv_toggle": "Airplane mode",
  "priv_meter_unit": "bytes out",
  "priv_meter_sub": "local steps",
  "priv_meter_label": "Animated illustration: local steps counting up while bytes out stays at zero",

  "watch_eyebrow": "Watchers",
  "watch_h": "It notices what you'd miss",
  "watch_p": "Five watchers look for the things that cost you, at the moment they would cost you — across sources nothing else sees together. Every finding shows its evidence.",
  "watch_sample": "Sample finding",
  "watchers": [
    ("Term change", "Your premium rose 23% at renewal", "renewal letter vs last year's · <b>£412 → £507</b> · same insurer"),
    ("Expiry radar", "Passport expires in 4 months. Schengen asks for 6.", "photo of the passport page · date read on the device"),
    ("Impersonation", "“Mum” wrote from an address she's never used", "from: “Mum” &lt;mum.family@quickmail.example&gt; · <b>not in her contact card</b>"),
    ("Site fraud & phishing", "This page says it's your bank. Its domain doesn't match.", "brand vs domain · <b>form posts elsewhere</b> · domain age (online, opt-in)"),
    ("Recurring money", "14 subscriptions, 5 unused for six months", "receipts + statements counted, not summarised"),
  ],
  "watch_note": "On iPhone, impersonation runs on email and contacts — iOS gives no app access to your SMS inbox. Phishing checks add to your browser's protection; they don't replace it.",

  "run_eyebrow": "Live run view · Riverflight",
  "run_h": "Watch it decide, live",
  "run_p": "Every long job shows itself as a loop of stages around the mascot — the engine. One particle per real item, each question diamond showing its latest answer and confidence, and cards for who answered, where items went, and what asking a cloud model would have cost instead.",
  "run_p2": "<b>Riverflight</b> is a river shooter where Laya flies. It decides many times a second with its raw probability bars on screen, against a dumb autopilot on the same river.",
  "run_stats": [("60 fps", "steady, Laya flying"), ("10–14/s", "decisions"), ("~63 ms", "p50 latency"), ("~82 ms", "p95 latency")],
  "run_src": "Measured in the iPhone simulator (iPhone 17 Pro Max), 25 Sep 2026. Not yet measured on a real iPhone.",
  "run_honest": "Honest status: untuned, Laya loses to the baseline pilot — it doesn't go for fuel. Fine-tuning is the planned fix.",

  "dev_eyebrow": "The apps",
  "dev_h": "Real screens, dark neon",
  "dev_p": "Screenshots from Loupe for iPhone (iOS simulator).",
  "shots": [("now", "Now", "Now: the top finding, what needs you, and “On this phone. Nothing leaves it.”"),
            ("live-run", "Live run", "Privacy check as a live run: stages, question diamonds and the mascot as the engine."),
            ("game", "Riverflight", "Riverflight results: decisions per second, p50/p95 latency and Laya against the baseline."),
            ("web", "Web", "Web templates: online data (labelled, with source and time) ranked on the phone."),
            ("settings", "Settings", "Model settings: every value with its default and trade-off.")],
  "mac_ph": "Loupe Station screenshot — coming soon",

  "hon_eyebrow": "Where it stands",
  "hon_h": "What we can and can't claim yet",
  "hon": ["<b>The model is untuned.</b> On 45 synthetic sample items it loses to simple keyword rules on every judgment measured (receipts: 64% vs 95% on 39 hand-labelled items). The app shows you this rather than hiding it.",
          "<b>Laya beats its keyword baseline on the examples for 6 of 55 templates.</b> Fine-tuning on your own corrections is the planned fix.",
          "<b>Confidence is raw and over-confident</b> until calibrated on your corrections; the app labels it that way.",
          "<b>Speed numbers are from the iPhone simulator.</b> Real-device speed, battery and heat are not yet measured.",
          "<b>Phishing checks are a second line</b>, not a replacement for your browser's protection. A small local model is not adversarially robust.",
          "<b>Loupe for iPhone is not on the App Store yet.</b>"],

  "plat_eyebrow": "Get Loupe",
  "plat_h": "iPhone, Mac — and next",
  "wait_h": "Join the waitlist",
  "wait_p": "Hear when Loupe reaches your platform. We'll email only about what you tick below.",
 },
 "ar": {
  "title": "Loupe — أحكام بكلمات بسيطة، تُقرَّر على جهازك",
  "eyebrow": "محرّك قرارات على جهازك",
  "h1": "علّمه حُكمًا.<br><span class=\"accent\">ويقرّر على جهازك.</span>",
  "lede": "اكتب ما يهمّك بكلمات بسيطة — «الإيصالات التي سأحتاجها وقت الضرائب»، «هل هذه الرسالة من بنكي فعلًا؟». يطبّق Loupe ذلك على صورك وملفاتك وبريدك وتقويمك وجهات اتصالك، ويُريك ما لا يثق به، ويتعلّم من إجاباتك، ولا يغادر جهازك شيء.",
  "cta_mac": "تنزيل لأجهزة Mac", "cta_ios_top": "قريبًا على",
  "stats": [("10–14", "قرارًا في الثانية · مقاسة على محاكي iPhone"), ("0 بايت", "تُرسَل من بياناتك"), ("+100", "لغة يقرؤها النموذج")],
  "stage_caption": "توضيح لعرض التشغيل المباشر في التطبيق، يتحرّك داخل متصفحك",
  "hud": ["عنصرًا تقرّر", "في الثانية"],
  "canvas": {"read": "قراءة", "decide": "قرار", "q1": "إيصال؟", "q2": "للضرائب؟", "q3": "متأكد؟", "sorted": "رُتِّب", "needs": "يحتاجك", "flag": "مُعلَّم",
             "answers": [["نعم", "لا"], ["نعم", "لا"], ["متأكد", "غير متأكد"]]},
  "mascot_alt": "روبوت Loupe، المحرّك في مركز عرض التشغيل المباشر",

  "diff_eyebrow": "ما الذي يميّزه",
  "diff_h": "عشرة أشياء لا يستطيع أي مساعد سحابي أن يَعِد بها",
  "diff_p": "Loupe ليس روبوت محادثة. لا يكتب عن بياناتك — بل يتخذ قرارات محدّدة النوع (نعم/لا، اختر واحدًا، درجة) بنموذج صغير يعمل حيث توجد بياناتك أصلًا.",

  "demo_eyebrow": "جرّبه",
  "demo_h": "علّمه حُكمًا وشاهده يرتّب",
  "demo_p": "اختر حُكمًا. تُرتَّب العناصر إلى «نعم» و«لا» و«يحتاجك»، مع شريط الثقة وإجابة قاعدة الكلمات المفتاحية بجانب كلٍّ منها — كما يعرض التطبيق النتائج.",
  "demo_label": "عرض توضيحي · عناصر مُختلَقة · إجابات مكتوبة مسبقًا، وليست النموذج",
  "demo_bins": ["نعم", "لا", "يحتاجك"],
  "demo_l": {"yes": "نعم", "no": "لا", "unsure": "غير متأكد", "kw": "قاعدة الكلمات", "reading": "قراءة", "done": "انتهى · كل إجابة تبقى في هذا المتصفح",
             "decided": "تقرّر", "queue": "أُرسل إليك", "agreeKw": "يتفق مع قاعدة الكلمات",
             "summary": "تم الترتيب. {d} تقرّر، {u} أُرسل إليك، {a} تتفق مع قاعدة الكلمات."},
  "demo_note": "في التطبيق الحقيقي تُقاس قاعدة الكلمات المفتاحية على تصحيحاتك أنت، وحين تتفوّق يخبرك Loupe ويعرض استخدامها.",

  "priv_eyebrow": "خصوصية يمكنك التحقق منها",
  "priv_h": "0 بايت للخارج. فعّل وضع الطيران — وما زال يعمل.",
  "priv_p": "Laya، نموذج القرار، يعمل على iPhone أو Mac. تُقرأ صورك وملفاتك وتقويمك وجهات اتصالك هناك ولا تُرسَل إلينا ولا إلى أي أحد. لا حساب. لا أدوات تحليلات أو إعلانات أو تقارير أعطال.",
  "priv_list": ["كل مصدر متوقف حتى تشغّله — والنظام يستأذنك أولًا.",
                "الإضافات المتصلة بالإنترنت (البريد، قوالب الويب، قوائم التصيّد، مساعد الكتابة) متوقفة افتراضيًا، وتحمل وسم <b>Online</b> مع مصدرها ووقتها، ولكلٍّ منها مفتاح خاص.",
                "مفاتيحك تبقى في Keychain على جهازك."],
  "priv_toggle": "وضع الطيران",
  "priv_meter_unit": "بايت للخارج",
  "priv_meter_sub": "خطوة محلية",
  "priv_meter_label": "توضيح متحرك: الخطوات المحلية تزداد بينما يبقى ما يخرج صفرًا",

  "watch_eyebrow": "المراقِبات",
  "watch_h": "يلاحظ ما قد يفوتك",
  "watch_p": "خمسة مراقِبات تبحث عمّا يكلّفك، في اللحظة التي سيكلّفك فيها — عبر مصادر لا يراها غيره معًا. كل نتيجة تعرض دليلها.",
  "watch_sample": "نتيجة نموذجية",
  "watchers": [
    ("تغيّر الشروط", "ارتفع قسط التأمين 23% عند التجديد", "خطاب التجديد مقابل العام الماضي · <b>£412 → £507</b> · الشركة نفسها"),
    ("رادار الانتهاء", "جواز سفرك ينتهي بعد 4 أشهر. شنغن تطلب 6.", "صورة صفحة الجواز · التاريخ قُرئ على الجهاز"),
    ("انتحال الشخصية", "«ماما» راسلتك من عنوان لم تستخدمه قط", "من: «ماما» &lt;mum.family@quickmail.example&gt; · <b>ليس في بطاقة جهة الاتصال</b>"),
    ("احتيال المواقع والتصيّد", "هذه الصفحة تدّعي أنها بنكك. نطاقها لا يطابق.", "العلامة مقابل النطاق · <b>النموذج يُرسَل لجهة أخرى</b> · عمر النطاق (عبر الإنترنت، اختياري)"),
    ("المدفوعات المتكررة", "14 اشتراكًا، 5 لم تُستخدم منذ ستة أشهر", "الإيصالات والكشوف تُعدّ، لا تُلخَّص"),
  ],
  "watch_note": "على iPhone يعمل كشف الانتحال على البريد وجهات الاتصال — لا يتيح iOS لأي تطبيق قراءة صندوق الرسائل النصية. فحوص التصيّد تُضاف إلى حماية متصفحك ولا تحلّ محلّها.",

  "run_eyebrow": "عرض التشغيل المباشر · Riverflight",
  "run_h": "شاهده يقرّر مباشرةً",
  "run_p": "كل مهمة طويلة تعرض نفسها كحلقة من المراحل حول الروبوت — المحرّك. جسيم لكل عنصر حقيقي، وكل معيّن سؤال يعرض آخر إجابة وثقتها، وبطاقات لمن أجاب، وأين ذهبت العناصر، وكم كان سيكلّف سؤال نموذج سحابي بدلًا من ذلك.",
  "run_p2": "<b>Riverflight</b> لعبة إطلاق نار على نهر يقودها Laya. يقرّر مرات عديدة في الثانية وأشرطة احتمالاته الخام على الشاشة، في مواجهة طيّار آلي بسيط على النهر نفسه.",
  "run_stats": [("60 fps", "ثابتة، Laya يقود"), ("10–14/ث", "قرارًا"), ("~63 ms", "زمن p50"), ("~82 ms", "زمن p95")],
  "run_src": "مقاسة على محاكي iPhone ‏(iPhone 17 Pro Max)، 25 سبتمبر 2026. لم تُقَس بعد على iPhone حقيقي.",
  "run_honest": "الحالة بصراحة: دون ضبط، يخسر Laya أمام الطيّار الأساسي — لا يتجه نحو الوقود. الضبط الدقيق هو الحل المخطط.",

  "dev_eyebrow": "التطبيقات",
  "dev_h": "شاشات حقيقية، نيون داكن",
  "dev_p": "لقطات من Loupe لأجهزة iPhone (محاكي iOS).",
  "shots": [("now", "الآن", "الآن: أهم نتيجة، وما يحتاجك، و«على هذا الهاتف. لا شيء يغادره.»"),
            ("live-run", "تشغيل مباشر", "فحص الخصوصية كتشغيل مباشر: المراحل ومعيّنات الأسئلة والروبوت كمحرّك."),
            ("game", "Riverflight", "نتائج Riverflight: القرارات في الثانية وزمن p50/p95 وLaya مقابل الأساس."),
            ("web", "الويب", "قوالب الويب: بيانات من الإنترنت (موسومة بمصدرها ووقتها) مرتّبة على الهاتف."),
            ("settings", "الإعدادات", "إعدادات النموذج: كل قيمة مع قيمتها الافتراضية والمفاضلة.")],
  "mac_ph": "لقطة Loupe Station — قريبًا",

  "hon_eyebrow": "أين نقف",
  "hon_h": "ما يمكننا ادعاؤه وما لا يمكننا بعد",
  "hon": ["<b>النموذج غير مضبوط بعد.</b> على 45 عنصرًا اصطناعيًا يخسر أمام قواعد الكلمات المفتاحية البسيطة في كل حُكم قيس (الإيصالات: 64% مقابل 95% على 39 عنصرًا مُعلَّمًا يدويًا). التطبيق يُريك ذلك ولا يخفيه.",
          "<b>يتفوّق Laya على قاعدته الأساسية في أمثلة 6 من 55 قالبًا.</b> الضبط الدقيق على تصحيحاتك هو الحل المخطط.",
          "<b>الثقة خام ومبالغ فيها</b> حتى تُعايَر على تصحيحاتك؛ والتطبيق يوسمها بذلك.",
          "<b>أرقام السرعة من محاكي iPhone.</b> السرعة والبطارية والحرارة على جهاز حقيقي لم تُقَس بعد.",
          "<b>فحوص التصيّد خط دفاع ثانٍ</b> لا بديل عن حماية متصفحك. النموذج المحلي الصغير ليس محصّنًا ضد الهجمات المتعمَّدة.",
          "<b>Loupe لأجهزة iPhone ليس على App Store بعد.</b>"],

  "plat_eyebrow": "احصل على Loupe",
  "plat_h": "iPhone وMac — وما بعدهما",
  "wait_h": "انضم إلى قائمة الانتظار",
  "wait_p": "اعرف حين يصل Loupe إلى منصتك. لن نراسلك إلا بما تختاره أدناه.",
 },
}

# icons: small inline SVGs, animated (stroke draw / spin / blink). stroke=currentColor
ICONS = {
 "words": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path class="draw" d="M8 12h24M8 20h32M8 28h18"/><path d="M30 30l6 6 8-12" stroke="#10B981" class="draw"/></svg>',
 "device": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="14" y="6" width="20" height="36" rx="4" class="draw"/><circle cx="24" cy="24" r="4" fill="#22D3EE" class="blink"/><path d="M4 24h6M38 24h6" stroke="#FF6B81" stroke-linecap="round"/><path d="M5 20l4 8M43 20l-4 8" stroke="#FF6B81" stroke-linecap="round"/></svg>',
 "unsure": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M24 6l18 18-18 18L6 24z" class="draw"/><path d="M20 20a4 4 0 118 0c0 3-4 3-4 6" stroke="#F5B544"/><circle cx="24" cy="31" r="1.4" fill="#F5B544" class="blink"/></svg>',
 "cross": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><g class="spin"><circle cx="24" cy="8" r="4"/><circle cx="38" cy="32" r="4"/><circle cx="10" cy="32" r="4"/></g><circle cx="24" cy="24" r="5" fill="#2F6BFF" stroke="#22D3EE"/></svg>',
 "watch": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 24s7-12 20-12 20 12 20 12-7 12-20 12S4 24 4 24z" class="draw"/><circle cx="24" cy="24" r="6"/><circle cx="24" cy="24" r="2" fill="#22D3EE" class="blink"/></svg>',
 "where": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="20" cy="20" r="11" class="draw"/><path d="M28 28l12 12"/><path d="M15 20h10" stroke="#10B981" class="blink"/></svg>',
 "shield": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M24 5l16 6v12c0 10-7 17-16 20C15 40 8 33 8 23V11z" class="draw"/><path d="M17 24l5 5 9-10" stroke="#10B981" class="draw"/></svg>',
 "live": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="24" cy="24" r="16" stroke-dasharray="3 5"/><g class="orbit"><circle cx="24" cy="8" r="3" fill="#22D3EE" stroke="none"/></g><circle cx="24" cy="24" r="6" fill="#13235A"/></svg>',
 "game": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M10 4c6 10-6 20 0 40M38 4c-6 10 6 20 0 40" class="draw"/><path d="M24 34l-5 6h10z" fill="#22D3EE" stroke="none"/><rect x="21" y="12" width="6" height="8" stroke="#10B981" class="blink"/></svg>',
 "write": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M8 40l4-12 20-20 8 8-20 20z" class="draw"/><path d="M8 40h32" stroke="#F5B544" stroke-dasharray="3 4"/></svg>',
}

DIFFS = {
 "en": [
  ("words", "Judgments in plain words, run on the device", "Write a question the way you'd ask a friend. Laya — a ~320M-parameter decision model — turns it into a yes/no, pick-one or score decision and runs it on your phone or Mac. It doesn't generate text; it decides.", "~10 decisions/s · iPhone simulator, measured"),
  ("device", "Nothing leaves the device", "Your photos, files, calendar and contacts are read on the device and never sent to us. No account, no analytics. Airplane mode: everything still works.", "0 bytes out"),
  ("unsure", "It shows what it's unsure about — and when a keyword search beats it", "You only review what it's torn on. Every judgment is measured against the dumb version — a keyword rule — and if the rule wins, Loupe says so and offers to use it.", "baseline check on every judgment"),
  ("cross", "Cross-source decisions", "One judgment spans everything: “receipts I'll need at tax time” returns email attachments, photographed paper, PDFs and spreadsheet rows in one list.", "photos · files · mail · calendar · contacts · web"),
  ("watch", "Watchers", "Price rises (+23% insurance at renewal), expiring documents, impersonation (“Mum” from an address or number that isn't hers), fake sites and phishing — each with its evidence.", "5 watchers"),
  ("where", "Verifiable results — “Show where”", "Every result names the item, its source and date, with Open original. Privacy findings re-find the match on tap and show where it is, masked.", "no black boxes"),
  ("shield", "The privacy check", "Finds ID and passport numbers, card numbers, IBANs, keys and tokens, contact lists, payroll sheets and duplicate files in your own sources. Masked previews; nothing proposed happens until you approve.", "rules on the device, no model needed"),
  ("live", "Live run view, with the mascot as the engine", "Watch a job run: stages on a loop, question diamonds with their latest answer, one particle per real item, who answered, and the cost of asking a cloud model instead.", "EN + AR, mirrored in RTL"),
  ("game", "Riverflight — watch the model decide live", "A river shooter where Laya flies, with its raw probability bars on screen, against a dumb autopilot on the same seed. Honest: untuned, it loses — for now.", "60 fps · p50 ~63 ms · simulator"),
  ("write", "Writing assistant: opt-in, your key, drafts only", "Off by default. Bring your own provider key (or Ollama on your network) and it drafts replies and second opinions — labelled drafts that wait for your approval. Judgments never depend on it.", "never sends anything as you"),
 ],
 "ar": [
  ("words", "أحكام بكلمات بسيطة، تعمل على الجهاز", "اكتب سؤالًا كما تسأل صديقًا. يحوّله Laya — نموذج قرار بحجم ~320 مليون معامل — إلى قرار نعم/لا أو اختيار أو درجة، ويشغّله على هاتفك أو Mac. لا يولّد نصًا؛ بل يقرّر.", "~10 قرارات/ث · مقاسة على محاكي iPhone"),
  ("device", "لا شيء يغادر الجهاز", "تُقرأ صورك وملفاتك وتقويمك وجهات اتصالك على الجهاز ولا تُرسَل إلينا أبدًا. لا حساب ولا تحليلات. في وضع الطيران يعمل كل شيء.", "0 بايت للخارج"),
  ("unsure", "يُريك ما لا يثق به — وحين يتفوّق عليه بحث الكلمات", "لا تراجع إلا ما يتردد فيه. كل حُكم يُقاس مقابل النسخة البسيطة — قاعدة كلمات مفتاحية — وإن تفوّقت القاعدة يقول Loupe ذلك ويعرض استخدامها.", "مقارنة بالأساس لكل حُكم"),
  ("cross", "قرارات عبر المصادر", "حُكم واحد يشمل كل شيء: «الإيصالات التي سأحتاجها للضرائب» يعيد مرفقات البريد والأوراق المصوّرة وملفات PDF وصفوف الجداول في قائمة واحدة.", "صور · ملفات · بريد · تقويم · جهات اتصال · ويب"),
  ("watch", "المراقِبات", "ارتفاع الأسعار (+23% في التأمين عند التجديد)، والوثائق المنتهية، وانتحال الشخصية («ماما» من عنوان أو رقم ليس لها)، والمواقع المزيفة والتصيّد — كلٌّ مع دليله.", "5 مراقِبات"),
  ("where", "نتائج قابلة للتحقق — «أرني أين»", "كل نتيجة تسمّي العنصر ومصدره وتاريخه، مع «فتح الأصل». نتائج الخصوصية تعيد إيجاد التطابق عند اللمس وتُريك موضعه مُقنَّعًا.", "لا صناديق سوداء"),
  ("shield", "فحص الخصوصية", "يجد أرقام الهويات وجوازات السفر والبطاقات وIBAN والمفاتيح والرموز وقوائم الاتصال وكشوف الرواتب والملفات المكررة في مصادرك. معاينات مُقنَّعة؛ ولا يُنفَّذ أي اقتراح قبل موافقتك.", "قواعد على الجهاز، دون حاجة للنموذج"),
  ("live", "عرض التشغيل المباشر، والروبوت هو المحرّك", "شاهد مهمة تعمل: مراحل على حلقة، ومعيّنات أسئلة بآخر إجابة، وجسيم لكل عنصر حقيقي، ومن أجاب، وكلفة سؤال نموذج سحابي بدلًا من ذلك.", "عربي وإنجليزي، معكوس لليمين"),
  ("game", "Riverflight — شاهد النموذج يقرّر مباشرةً", "لعبة نهر يقودها Laya وأشرطة احتمالاته الخام على الشاشة، في مواجهة طيّار آلي بسيط على البذرة نفسها. بصراحة: دون ضبط، يخسر — حاليًا.", "60 fps · p50 ~63 ms · محاكي"),
  ("write", "مساعد الكتابة: اختياري، بمفتاحك، مسودات فقط", "متوقف افتراضيًا. أحضر مفتاح مزوّدك (أو Ollama على شبكتك) فيكتب مسودات الردود والآراء الثانية — مسودات موسومة تنتظر موافقتك. الأحكام لا تعتمد عليه أبدًا.", "لا يرسل شيئًا باسمك"),
 ],
}

# Demo: made-up items, scripted scores. p = scripted confidence of "yes"; kw = what a keyword rule says.
DEMO = {
 "en": [
  {"q": "Is this a receipt I'll need at tax time?", "sub": "yes/no · photos, mail, PDFs, sheets", "items": [
    {"t": "Invoice INV-2031 — accountant fees", "src": "PDF", "p": 0.93, "kw": 1},
    {"t": "Photo of a pharmacy receipt", "src": "Photos", "p": 0.81, "kw": 0},
    {"t": "“Your receipt from the coffee app”", "src": "Mail", "p": 0.58, "kw": 1},
    {"t": "Row 14: office chair, £189", "src": "Sheet", "p": 0.77, "kw": 0},
    {"t": "Holiday photo, beach", "src": "Photos", "p": 0.04, "kw": 0},
    {"t": "Newsletter: “Receipts of the week”", "src": "Mail", "p": 0.12, "kw": 1},
    {"t": "Council tax statement 2026", "src": "PDF", "p": 0.88, "kw": 0},
    {"t": "Screenshot of a parking payment", "src": "Photos", "p": 0.46, "kw": 0},
    {"t": "Lease agreement draft", "src": "Files", "p": 0.21, "kw": 0}]},
  {"q": "Does this email need a reply from me?", "sub": "yes/no · mail", "items": [
    {"t": "“Can you send the signed form by Friday?”", "src": "Mail", "p": 0.92, "kw": 1},
    {"t": "Weekly digest from a forum", "src": "Mail", "p": 0.05, "kw": 0},
    {"t": "“Thanks, all sorted!”", "src": "Mail", "p": 0.18, "kw": 0},
    {"t": "Delivery update: out for delivery", "src": "Mail", "p": 0.03, "kw": 0},
    {"t": "“Are you free Tuesday or Wednesday?”", "src": "Mail", "p": 0.89, "kw": 1},
    {"t": "“FYI — minutes attached, reply if anything's wrong”", "src": "Mail", "p": 0.52, "kw": 1},
    {"t": "Invitation: team lunch (RSVP)", "src": "Calendar", "p": 0.74, "kw": 0},
    {"t": "Password reset you didn't request", "src": "Mail", "p": 0.35, "kw": 0}]},
  {"q": "Is this page really who it says it is?", "sub": "yes/no · web pages, links in mail", "items": [
    {"t": "bank login page on the bank's own domain", "src": "Web", "p": 0.9, "kw": 1},
    {"t": "“Bank secure” page on a 9-day-old domain", "src": "Web", "p": 0.06, "kw": 1},
    {"t": "Parcel fee page asking for card + PIN", "src": "Link", "p": 0.03, "kw": 0},
    {"t": "Your gym's booking page", "src": "Web", "p": 0.84, "kw": 1},
    {"t": "Login form that posts to another site", "src": "Web", "p": 0.28, "kw": 1},
    {"t": "Shop with a look-alike letter in its name", "src": "Link", "p": 0.4, "kw": 1},
    {"t": "Government tax portal", "src": "Web", "p": 0.87, "kw": 1}]},
  {"q": "Is this a document that expires?", "sub": "pick one · photos, PDFs, mail", "items": [
    {"t": "Passport photo page", "src": "Photos", "p": 0.95, "kw": 1},
    {"t": "Car insurance certificate", "src": "PDF", "p": 0.88, "kw": 0},
    {"t": "Warranty card for a kettle", "src": "Photos", "p": 0.66, "kw": 0},
    {"t": "Birthday party invite", "src": "Mail", "p": 0.09, "kw": 0},
    {"t": "Visa approval letter", "src": "Mail", "p": 0.91, "kw": 1},
    {"t": "Gym membership terms", "src": "Files", "p": 0.55, "kw": 0},
    {"t": "Recipe screenshot", "src": "Photos", "p": 0.02, "kw": 0}]},
 ],
 "ar": [
  {"q": "هل هذا إيصال سأحتاجه وقت الضرائب؟", "sub": "نعم/لا · صور، بريد، PDF، جداول", "items": [
    {"t": "فاتورة INV-2031 — أتعاب المحاسب", "src": "PDF", "p": 0.93, "kw": 1},
    {"t": "صورة إيصال صيدلية", "src": "صور", "p": 0.81, "kw": 0},
    {"t": "«إيصالك من تطبيق القهوة»", "src": "بريد", "p": 0.58, "kw": 1},
    {"t": "الصف 14: كرسي مكتب، 189 جنيهًا", "src": "جدول", "p": 0.77, "kw": 0},
    {"t": "صورة عطلة على الشاطئ", "src": "صور", "p": 0.04, "kw": 0},
    {"t": "نشرة: «إيصالات الأسبوع»", "src": "بريد", "p": 0.12, "kw": 1},
    {"t": "كشف ضريبة عقارية 2026", "src": "PDF", "p": 0.88, "kw": 0},
    {"t": "لقطة شاشة لدفع موقف سيارات", "src": "صور", "p": 0.46, "kw": 0},
    {"t": "مسودة عقد إيجار", "src": "ملفات", "p": 0.21, "kw": 0}]},
  {"q": "هل تحتاج هذه الرسالة ردًّا مني؟", "sub": "نعم/لا · بريد", "items": [
    {"t": "«هل ترسل النموذج الموقّع قبل الجمعة؟»", "src": "بريد", "p": 0.92, "kw": 1},
    {"t": "ملخص أسبوعي من منتدى", "src": "بريد", "p": 0.05, "kw": 0},
    {"t": "«شكرًا، تمّ كل شيء!»", "src": "بريد", "p": 0.18, "kw": 0},
    {"t": "تحديث الشحن: في الطريق إليك", "src": "بريد", "p": 0.03, "kw": 0},
    {"t": "«هل أنت متاح الثلاثاء أم الأربعاء؟»", "src": "بريد", "p": 0.89, "kw": 1},
    {"t": "«للعلم — المحضر مرفق، ردّ إن كان فيه خطأ»", "src": "بريد", "p": 0.52, "kw": 1},
    {"t": "دعوة: غداء الفريق (تأكيد الحضور)", "src": "تقويم", "p": 0.74, "kw": 0},
    {"t": "إعادة تعيين كلمة مرور لم تطلبها", "src": "بريد", "p": 0.35, "kw": 0}]},
  {"q": "هل هذه الصفحة هي فعلًا من تدّعي أنها؟", "sub": "نعم/لا · صفحات ويب وروابط البريد", "items": [
    {"t": "صفحة دخول البنك على نطاقه الرسمي", "src": "ويب", "p": 0.9, "kw": 1},
    {"t": "صفحة «البنك الآمن» على نطاق عمره 9 أيام", "src": "ويب", "p": 0.06, "kw": 1},
    {"t": "صفحة رسوم طرد تطلب البطاقة والرقم السري", "src": "رابط", "p": 0.03, "kw": 0},
    {"t": "صفحة حجز النادي الرياضي", "src": "ويب", "p": 0.84, "kw": 1},
    {"t": "نموذج دخول يُرسَل إلى موقع آخر", "src": "ويب", "p": 0.28, "kw": 1},
    {"t": "متجر في اسمه حرف مشابه", "src": "رابط", "p": 0.4, "kw": 1},
    {"t": "بوابة الضرائب الحكومية", "src": "ويب", "p": 0.87, "kw": 1}]},
  {"q": "هل هذه وثيقة لها تاريخ انتهاء؟", "sub": "اختر واحدًا · صور، PDF، بريد", "items": [
    {"t": "صفحة صورة جواز السفر", "src": "صور", "p": 0.95, "kw": 1},
    {"t": "شهادة تأمين السيارة", "src": "PDF", "p": 0.88, "kw": 0},
    {"t": "بطاقة ضمان غلاية", "src": "صور", "p": 0.66, "kw": 0},
    {"t": "دعوة حفلة عيد ميلاد", "src": "بريد", "p": 0.09, "kw": 0},
    {"t": "خطاب الموافقة على التأشيرة", "src": "بريد", "p": 0.91, "kw": 1},
    {"t": "شروط عضوية النادي", "src": "ملفات", "p": 0.55, "kw": 0},
    {"t": "لقطة شاشة لوصفة طعام", "src": "صور", "p": 0.02, "kw": 0}]},
 ],
}

# ---------------------------------------------------------------- features (full lists)
FEATURES = {
 "en": {
  "title": "Features — Loupe for iPhone and Loupe Station for Mac",
  "h1": "Everything Loupe does",
  "lede": "The differentiators first, then every feature in each app. Where a number appears, it was measured, and we say where.",
  "ios_h": "Loupe for iPhone", "ios_sub": "iOS 17+ · not yet on the App Store · English and Arabic",
  "mac_h": "Loupe Station for Mac", "mac_sub": "macOS 14+ · Apple Silicon · powered by Laya",
  "ios": [
   ("Now", "The top finding, what needs you, the privacy check and mail triage cards, and the last sort's real counts (“45 sorted, 32 need you”)."),
   ("Judgments library", "55 ready-made templates in 10 categories — search, read the criteria and baseline, “Use this”."),
   ("Write your own judgment", "Plain words with a live lint: yes/no (options that say what they mean), score with named bands, or pick one."),
   ("Results you can check", "Each answer with its confidence, source, “answered by rule” when a rule decided, and unsure markers."),
   ("Unsure queue", "Only what it's torn on, most torn first — plus a random fifth of confident answers, so it can't drift unseen. One tap per answer, Skip, Undo."),
   ("Measure", "Agreement with you from 10 corrections; calibration (ECE, Brier, reliability) from 30; the model vs the keyword baseline on your corrected items, with “Use the baseline” when it wins."),
   ("Threshold slider", "Move it and see what would have changed over your logged decisions before you commit."),
   ("Five watchers", "Expiry radar, recurring-money census with a monthly total, term changes, impersonation, site fraud — with evidence, Confirm / Dismiss / Not relevant."),
   ("Sort while charging", "Off by default. Sweeps every judgment over every enabled source in the background; stops when the phone is hot or in Low Power Mode."),
   ("Sources, each off by default", "Photos (text read on the device), Files and “Send to Loupe” from the share sheet, Calendar (read only), Contacts, Mail (IMAP with an app password, or Gmail read-only — Online)."),
   ("Items inbox", "Import CSV/TSV (a row per item), .eml, .mbox, ZIP or pasted text."),
   ("Privacy check", "IDs and passports, card numbers, IBANs, keys and tokens, contact lists, payroll, duplicate files — masked, with Show where."),
   ("Mail triage and link checks", "Possible phishing and needs-a-reply, with the evidence grouped as warning signs, reassuring facts and “also noticed”."),
   ("Review queue", "Anything a check proposes — remove a duplicate copy, confirm phishing — waits for your Approve."),
   ("Preset packs", "Import a pack of judgments from Files, try the example pack, or export yours."),
   ("Web templates (Online, opt-in)", "Currency, weather and UK trains, with ready questions in English and Arabic or your own; Laya ranks the fetched rows on the phone, with the rule baseline beside it."),
   ("Online phishing checks (opt-in)", "Known-phishing lists matched on the phone; DNS facts; each result labelled Online with its source."),
   ("Writing assistant (opt-in)", "Your own OpenAI-compatible key or Ollama on your network. Drafts replies and second opinions, labelled, waiting for approval."),
   ("Model settings", "Every setting with its value, default and trade-off, and Reset."),
   ("Show where / Open original", "Every row names its item, source and date, and opens the original."),
   ("Live run view", "Every long job, in place: stages, question diamonds, particles, who answered, cost of asking."),
   ("Riverflight", "Fly it yourself or watch Laya fly, with raw probability bars, a speed panel and a results card against the baseline."),
   ("Export my data", "Your decisions, corrections and settings as a zip — portable files you own."),
   ("The Laya model", "A consented one-time download (~418 MB, SHA-256 checked). 322M parameters, Apache-2.0 weights, 100+ languages."),
  ],
  "mac": [
   ("Playground", "Ask Laya typed questions (choice, score, yes/no) about any text or JSON and see every probability. About 40 ms a decision on Apple silicon."),
   ("Two checkpoints, routed for you", "English (ModernBERT-large) and multilingual (mmBERT-base) — Arabic and other languages go to the multilingual one automatically."),
   ("Memory modes", "Full, balanced or low — so the model fits the Mac you have, with unloading when idle."),
   ("Workflow templates and template library", "Ready-made decision workflows; your business specifics go in preset packs you import."),
   ("Folder Scan", "What's in a folder and what looks risky: secrets and tokens, exposed personal or business data, duplicates, large and old files."),
   ("Arrangement plan", "A tidier layout proposed with a reason per move; nothing moves until you tick it, and every move can be undone."),
   ("Email triage", "Gmail (your own OAuth client), Outlook / Microsoft 365 (your own Azure app) or IMAP. Categories, phishing evidence, needs-reply."),
   ("Labels and reply drafts — only with approval", "It may add a label or save a draft in the thread. It never sends, deletes, archives or moves mail."),
   ("Decision ledger", "Every decision with its full distribution, so accuracy and thresholds can be measured honestly."),
   ("Measure: Laya against simple rules", "Each judgment compared with its keyword baseline on your data."),
   ("Calibration, spot-check queue, thresholds", "See where it's over-confident and set thresholds from evidence."),
   ("Sources", "Accounts, mail archives, scanned folders, statements and attachments."),
   ("Watchers", "The same five watchers as on iPhone, across your Mac's sources and mail history."),
   ("Live run view", "Every long job shows itself in place with the mascot as the engine."),
   ("Review queue", "Agents can propose, never apply. Every proposal waits for a person."),
   ("Second opinion (opt-in)", "A language model you choose re-answers uncertain questions; you decide per question."),
   ("Browser protection", "An extension for Chrome, Edge, Brave and Arc scores pages on your Mac — address, forms and page text. Nothing is looked up online unless you turn it on."),
   ("Local API with per-agent keys", "The server listens only on your Mac (127.0.0.1). Give each agent its own key."),
   ("Automatic updates", "Signed updates via Sparkle from loupe-ai.com."),
  ],
 },
 "ar": {
  "title": "الميزات — Loupe لأجهزة iPhone وLoupe Station لأجهزة Mac",
  "h1": "كل ما يفعله Loupe",
  "lede": "الميزات المميِّزة أولًا، ثم كل ميزة في كل تطبيق. حيث يظهر رقم فقد قيس، ونذكر أين.",
  "ios_h": "Loupe لأجهزة iPhone", "ios_sub": "iOS 17 أو أحدث · ليس على App Store بعد · العربية والإنجليزية",
  "mac_h": "Loupe Station لأجهزة Mac", "mac_sub": "macOS 14 أو أحدث · Apple Silicon · يعمل بـ Laya",
  "ios": [
   ("الآن", "أهم نتيجة، وما يحتاجك، وبطاقتا فحص الخصوصية وفرز البريد، والأعداد الحقيقية لآخر ترتيب («رُتِّب 45، و32 تحتاجك»)."),
   ("مكتبة الأحكام", "55 قالبًا جاهزًا في 10 فئات — ابحث واقرأ المعايير والأساس، ثم «استخدم هذا»."),
   ("اكتب حُكمك", "كلمات بسيطة مع تدقيق فوري: نعم/لا (بخيارات واضحة المعنى)، أو درجة بنطاقات مسمّاة، أو اختيار واحد."),
   ("نتائج يمكنك فحصها", "كل إجابة مع ثقتها ومصدرها، و«أجابت قاعدة» حين تقرّر قاعدة، وعلامات عدم اليقين."),
   ("طابور غير المؤكَّد", "فقط ما يتردد فيه، الأكثر ترددًا أولًا — مع خُمس عشوائي من الإجابات الواثقة كي لا ينحرف دون أن تراه. لمسة لكل إجابة، تخطٍّ، تراجع."),
   ("القياس", "الاتفاق معك بعد 10 تصحيحات؛ والمعايرة (ECE وBrier والموثوقية) بعد 30؛ والنموذج مقابل قاعدة الكلمات على عناصرك المصحَّحة، مع «استخدم الأساس» حين يتفوّق."),
   ("منزلق العتبة", "حرّكه وشاهد ما كان سيتغير في قراراتك المسجّلة قبل أن تعتمده."),
   ("خمسة مراقِبات", "رادار الانتهاء، وإحصاء المدفوعات المتكررة مع مجموع شهري، وتغيّر الشروط، والانتحال، واحتيال المواقع — مع الدليل وأزرار تأكيد/رفض/غير مهم."),
   ("الترتيب أثناء الشحن", "متوقف افتراضيًا. يمرّ بكل حُكم على كل مصدر مفعّل في الخلفية؛ ويتوقف إن سخن الهاتف أو في وضع توفير الطاقة."),
   ("مصادر، كلٌّ منها متوقف افتراضيًا", "الصور (يُقرأ النص على الجهاز)، والملفات و«أرسل إلى Loupe» من قائمة المشاركة، والتقويم (قراءة فقط)، وجهات الاتصال، والبريد (IMAP بكلمة مرور تطبيق، أو Gmail للقراءة فقط — عبر الإنترنت)."),
   ("صندوق العناصر", "استيراد CSV/TSV (صف لكل عنصر) و‎.eml و‎.mbox وZIP أو نص ملصوق."),
   ("فحص الخصوصية", "الهويات والجوازات وأرقام البطاقات وIBAN والمفاتيح والرموز وقوائم الاتصال والرواتب والملفات المكررة — مُقنَّعة، مع «أرني أين»."),
   ("فرز البريد وفحص الروابط", "تصيّد محتمل ويحتاج ردًّا، مع الأدلة مجمّعة: علامات تحذير، وحقائق مطمئنة، و«لوحظ أيضًا»."),
   ("طابور المراجعة", "أي اقتراح من الفحوص — حذف نسخة مكررة، تأكيد تصيّد — ينتظر موافقتك."),
   ("حزم جاهزة", "استورد حزمة أحكام من الملفات، أو جرّب الحزمة المثال، أو صدّر أحكامك."),
   ("قوالب الويب (عبر الإنترنت، اختيارية)", "العملات والطقس وقطارات بريطانيا، بأسئلة جاهزة بالعربية والإنجليزية أو سؤالك؛ يرتّب Laya الصفوف المجلوبة على الهاتف مع قاعدة الأساس بجانبها."),
   ("فحوص التصيّد عبر الإنترنت (اختيارية)", "قوائم التصيّد المعروفة تُطابَق على الهاتف؛ حقائق DNS؛ وكل نتيجة موسومة Online مع مصدرها."),
   ("مساعد الكتابة (اختياري)", "مفتاحك المتوافق مع OpenAI أو Ollama على شبكتك. يكتب مسودات ردود وآراء ثانية، موسومة، تنتظر الموافقة."),
   ("إعدادات النموذج", "كل إعداد مع قيمته وقيمته الافتراضية والمفاضلة، وزر إعادة الضبط."),
   ("أرني أين / افتح الأصل", "كل صف يسمّي عنصره ومصدره وتاريخه، ويفتح الأصل."),
   ("عرض التشغيل المباشر", "كل مهمة طويلة في مكانها: مراحل، ومعيّنات أسئلة، وجسيمات، ومن أجاب، وكلفة السؤال."),
   ("Riverflight", "قُدها بنفسك أو شاهد Laya يقودها، مع أشرطة الاحتمالات الخام ولوحة السرعة وبطاقة نتائج مقابل الأساس."),
   ("صدّر بياناتي", "قراراتك وتصحيحاتك وإعداداتك في ملف zip — ملفات قابلة للنقل تملكها."),
   ("نموذج Laya", "تنزيل لمرة واحدة بموافقتك (~418 ميغابايت، مع تحقق SHA-256). 322 مليون معامل، أوزان Apache-2.0، أكثر من 100 لغة."),
  ],
  "mac": [
   ("ساحة التجربة", "اسأل Laya أسئلة محدّدة النوع (اختيار، درجة، نعم/لا) عن أي نص أو JSON وشاهد كل احتمال. نحو 40 ms للقرار على Apple silicon."),
   ("نقطتا تحقق، يُوجَّه بينهما تلقائيًا", "الإنجليزية (ModernBERT-large) ومتعددة اللغات (mmBERT-base) — العربية واللغات الأخرى تذهب تلقائيًا إلى متعددة اللغات."),
   ("أوضاع الذاكرة", "كاملة أو متوازنة أو منخفضة — ليناسب النموذج جهازك، مع تفريغ عند الخمول."),
   ("قوالب سير العمل ومكتبة القوالب", "سير عمل قرارات جاهزة؛ وتفاصيل عملك تذهب في حزم تستوردها."),
   ("فحص المجلدات", "ما في المجلد وما يبدو خطِرًا: أسرار ورموز، وبيانات شخصية أو تجارية مكشوفة، وتكرارات، وملفات كبيرة وقديمة."),
   ("خطة الترتيب", "تخطيط أنظف مقترح بسبب لكل نقل؛ لا يُنقل شيء قبل أن تختاره، وكل نقل يمكن التراجع عنه."),
   ("فرز البريد", "Gmail (عميل OAuth خاص بك)، أو Outlook / Microsoft 365 (تطبيق Azure خاص بك)، أو IMAP. فئات، وأدلة تصيّد، ويحتاج ردًّا."),
   ("وسوم ومسودات ردود — بموافقتك فقط", "قد يضيف وسمًا أو يحفظ مسودة في المحادثة. لا يرسل ولا يحذف ولا يؤرشف ولا ينقل البريد أبدًا."),
   ("سجل القرارات", "كل قرار بتوزيعه الكامل، لتُقاس الدقة والعتبات بصدق."),
   ("القياس: Laya مقابل القواعد البسيطة", "كل حُكم يُقارن بأساس الكلمات المفتاحية على بياناتك."),
   ("المعايرة وطابور الفحص والعتبات", "اعرف أين يبالغ في ثقته واضبط العتبات بالأدلة."),
   ("المصادر", "الحسابات وأرشيفات البريد والمجلدات المفحوصة والكشوف والمرفقات."),
   ("المراقِبات", "المراقِبات الخمسة نفسها كما في iPhone، عبر مصادر Mac وسجل البريد."),
   ("عرض التشغيل المباشر", "كل مهمة طويلة تعرض نفسها في مكانها والروبوت هو المحرّك."),
   ("طابور المراجعة", "الوكلاء يقترحون ولا ينفّذون أبدًا. كل اقتراح ينتظر إنسانًا."),
   ("رأي ثانٍ (اختياري)", "نموذج لغوي تختاره يعيد الإجابة عن الأسئلة غير المؤكدة؛ وأنت تقرّر لكل سؤال."),
   ("حماية المتصفح", "إضافة لـ Chrome وEdge وBrave وArc تقيّم الصفحات على جهازك — العنوان والنماذج والنص. لا شيء يُبحث عنه عبر الإنترنت ما لم تفعّله."),
   ("واجهة برمجية محلية بمفاتيح لكل وكيل", "الخادم يستمع على جهازك فقط (127.0.0.1). امنح كل وكيل مفتاحه."),
   ("تحديثات تلقائية", "تحديثات موقّعة عبر Sparkle من loupe-ai.com."),
  ],
 },
}

DOWNLOAD = {
 "en": {"title": "Download Loupe — iPhone, Mac, and what's next", "h1": "Download Loupe",
        "lede": "Loupe Station for Mac and Loupe for iPhone. Android, Windows and Linux are coming — join the waitlist and we'll tell you first.",
        "mac_p": "The full desktop engine: playground, folder scan, mail triage, browser protection, watchers and the live run view.",
        "mac_req": "macOS 14 or later · Apple Silicon · signed and notarised, auto-updates",
        "ios_p": "The phone app: judgments across your photos, files, mail, calendar and contacts, the watchers, the privacy check and Riverflight.",
        "ios_req": "iOS 17 or later · English and Arabic",
        "soon_p": "Coming soon. Tell us which one you need.",
        "soon": "Coming soon"},
 "ar": {"title": "تنزيل Loupe — iPhone وMac وما بعدهما", "h1": "تنزيل Loupe",
        "lede": "Loupe Station لأجهزة Mac وLoupe لأجهزة iPhone. أندرويد وويندوز ولينكس قادمة — انضم إلى قائمة الانتظار وسنخبرك أولًا.",
        "mac_p": "محرّك سطح المكتب الكامل: ساحة التجربة، وفحص المجلدات، وفرز البريد، وحماية المتصفح، والمراقِبات، وعرض التشغيل المباشر.",
        "mac_req": "macOS 14 أو أحدث · Apple Silicon · موقّع ومُوثَّق، يتحدّث تلقائيًا",
        "ios_p": "تطبيق الهاتف: أحكام عبر صورك وملفاتك وبريدك وتقويمك وجهات اتصالك، والمراقِبات، وفحص الخصوصية، وRiverflight.",
        "ios_req": "iOS 17 أو أحدث · العربية والإنجليزية",
        "soon_p": "قريبًا. أخبرنا أيّها تحتاج.",
        "soon": "قريبًا"},
}

FORM = {
 "en": {"email": "Email", "email_hint": "(required)", "name": "Name", "name_hint": "(optional)",
        "platforms": "Platforms you're interested in", "country": "Country", "country_none": "Prefer not to say",
        "language": "Email language", "consent_h": "What may we email you about? Each one is optional.",
        "c": {"product_updates": "Product updates and launches — when Loupe reaches your platform, and major releases.",
              "promotions": "Promotions and offers — discounts and special offers on Loupe.",
              "beta_invites": "Beta testing invitations — early builds to try before release.",
              "research": "Research and feedback surveys — occasional questions about how you'd use Loupe."},
        "ack": "I have read the <a href=\"/privacy/#website\">privacy policy</a>, including how the website stores my sign-up.",
        "ack_req": "(required)",
        "submit": "Join the waitlist",
        "fine": "Double opt-in: we'll email you a link to confirm. You can unsubscribe from every email. Consent text version " + CONSENT_VERSION + "."},
 "ar": {"email": "البريد الإلكتروني", "email_hint": "(مطلوب)", "name": "الاسم", "name_hint": "(اختياري)",
        "platforms": "المنصات التي تهمّك", "country": "الدولة", "country_none": "أفضّل عدم الإفصاح",
        "language": "لغة الرسائل", "consent_h": "عمّ يمكننا مراسلتك؟ كلٌّ منها اختياري.",
        "c": {"product_updates": "تحديثات المنتج والإطلاقات — حين يصل Loupe إلى منصتك، والإصدارات الكبرى.",
              "promotions": "العروض والتخفيضات — خصومات وعروض خاصة على Loupe.",
              "beta_invites": "دعوات الاختبار التجريبي — إصدارات مبكرة لتجربتها قبل الإطلاق.",
              "research": "استبيانات البحث والآراء — أسئلة متفرقة عن طريقة استخدامك لـ Loupe."},
        "ack": "قرأت <a href=\"/ar/privacy/#website\">سياسة الخصوصية</a>، بما في ذلك كيف يحفظ الموقع تسجيلي.",
        "ack_req": "(مطلوب)",
        "submit": "انضم إلى قائمة الانتظار",
        "fine": "تأكيد مزدوج: سنرسل إليك رابطًا للتأكيد. يمكنك إلغاء الاشتراك من كل رسالة. إصدار نص الموافقة " + CONSENT_VERSION + "."},
}

COUNTRIES = [("EG","Egypt","مصر"),("SA","Saudi Arabia","السعودية"),("AE","United Arab Emirates","الإمارات"),("KW","Kuwait","الكويت"),("QA","Qatar","قطر"),("BH","Bahrain","البحرين"),("OM","Oman","عُمان"),("JO","Jordan","الأردن"),("LB","Lebanon","لبنان"),("MA","Morocco","المغرب"),("DZ","Algeria","الجزائر"),("TN","Tunisia","تونس"),("IQ","Iraq","العراق"),("GB","United Kingdom","المملكة المتحدة"),("US","United States","الولايات المتحدة"),("CA","Canada","كندا"),("DE","Germany","ألمانيا"),("FR","France","فرنسا"),("NL","Netherlands","هولندا"),("ES","Spain","إسبانيا"),("IT","Italy","إيطاليا"),("SE","Sweden","السويد"),("IE","Ireland","أيرلندا"),("AU","Australia","أستراليا"),("IN","India","الهند"),("PK","Pakistan","باكستان"),("TR","Türkiye","تركيا"),("BR","Brazil","البرازيل"),("JP","Japan","اليابان"),("SG","Singapore","سنغافورة"),("ZZ","Other","أخرى")]

NOTFOUND = {
 "en": {"title": "Page not found — Loupe", "h1": "Nothing here.", "p": "Loupe looked and is confident: this page doesn't exist. Try the home page, or the features.", "home": "Home"},
 "ar": {"title": "الصفحة غير موجودة — Loupe", "h1": "لا شيء هنا.", "p": "بحث Loupe وهو واثق: هذه الصفحة غير موجودة. جرّب الصفحة الرئيسية أو الميزات.", "home": "الرئيسية"},
}

# Added to the privacy policy: the website, kept separate from the apps.
WEBSITE_PRIVACY = {
 "en": """
<section class="site-section" id="website" aria-labelledby="website-h">
<h2 id="website-h">The website (loupe-ai.com) — separate from the apps</h2>
<p><strong>Everything above is about the apps, and the apps collect nothing about you.</strong> This section is about the website only: the waitlist sign-up and the download counts. Nothing here comes from, or is linked to, the Loupe apps or anything on your devices.</p>
<h3>Waitlist and email sign-up</h3>
<ul>
<li><strong>What we store when you sign up:</strong> your email address; your name, if you give it; the platforms you ticked; the country and email language you chose; the page language; each of the four email purposes you did or did not tick (product updates and launches; promotions and offers; beta testing invitations; research and feedback surveys), <strong>the exact wording you were shown and its version</strong>; your acknowledgement of this policy; timestamps; your status (pending, confirmed or unsubscribed); and a one-way hash of the confirmation link's token.</li>
<li><strong>Country from the connection:</strong> at sign-up our database records the two-letter country code our hosting provider derives from your connection. <strong>We do not store your IP address or your browser's user agent.</strong></li>
<li><strong>Double opt-in:</strong> nothing is sent to you except the confirmation email until you click its link. Unconfirmed sign-ups are deleted after [30 DAYS — CONFIRM].</li>
<li><strong>Why (legal basis):</strong> your consent, given separately for each purpose. You can withdraw it at any time with the unsubscribe link in every email or by writing to privacy@loupe-ai.com.</li>
<li><strong>Audit trail:</strong> each consent given, confirmed or withdrawn is kept as an append-only record so we can show what you agreed to and when. After you unsubscribe we keep only what we need to prove that and to not email you again, for [RETENTION PERIOD — LAWYER TO CONFIRM].</li>
<li><strong>Who processes it for us:</strong> Supabase (database) [REGION — CONFIRM] and Resend (sending email). We don't sell or share it, and we don't use it for advertising.</li>
</ul>
<h3>Download counts</h3>
<ul>
<li>When you click a download button the site records: the platform, the app version, the page language and path, the time, and the two-letter country code derived from the connection.</li>
<li><strong>No cookies, no IP address, no user agent, no identifier</strong> — a count cannot be linked to you or to your sign-up.</li>
</ul>
<h3>Everything else on the website</h3>
<ul>
<li>No cookies, analytics, advertising or tracking scripts. Fonts are served from loupe-ai.com itself.</li>
<li>The site's host may keep standard server logs (including IP addresses) for security, under its own policy: [HOST — e.g. GitHub Pages — CONFIRM].</li>
<li>The Mac download link points to our public downloads repository on GitHub; downloading a file from it is handled by GitHub under its own policy.</li>
</ul>
</section>
""",
 "ar": """
<section class="site-section" id="website" aria-labelledby="website-h">
<h2 id="website-h">الموقع (loupe-ai.com) — منفصل عن التطبيقات</h2>
<p><strong>كل ما سبق يخص التطبيقات، والتطبيقات لا تجمع عنك شيئًا.</strong> هذا القسم يخص الموقع فقط: التسجيل في قائمة الانتظار وأعداد التنزيل. لا شيء هنا يأتي من تطبيقات Loupe أو من أجهزتك، ولا يرتبط بها.</p>
<h3>قائمة الانتظار والتسجيل بالبريد</h3>
<ul>
<li><strong>ما نحفظه عند تسجيلك:</strong> بريدك الإلكتروني؛ واسمك إن ذكرته؛ والمنصات التي اخترتها؛ والدولة ولغة الرسائل اللتين اخترتهما؛ ولغة الصفحة؛ وكلًّا من أغراض المراسلة الأربعة التي اخترتها أو لم تخترها (تحديثات المنتج والإطلاقات؛ العروض والتخفيضات؛ دعوات الاختبار التجريبي؛ استبيانات البحث والآراء)، <strong>والنص الدقيق الذي عُرض عليك وإصداره</strong>؛ وإقرارك بهذه السياسة؛ والطوابع الزمنية؛ وحالتك (معلّق، مؤكَّد، ملغى)؛ وتجزئة أحادية الاتجاه لرمز رابط التأكيد.</li>
<li><strong>الدولة من الاتصال:</strong> عند التسجيل تسجّل قاعدة بياناتنا رمز الدولة المكوّن من حرفين الذي يستنتجه مزوّد الاستضافة من اتصالك. <strong>لا نحفظ عنوان IP ولا بيانات متصفحك (user agent).</strong></li>
<li><strong>تأكيد مزدوج:</strong> لا نرسل إليك شيئًا سوى رسالة التأكيد حتى تضغط رابطها. التسجيلات غير المؤكدة تُحذف بعد [30 يومًا — للتأكيد].</li>
<li><strong>الأساس القانوني:</strong> موافقتك، مُعطاة لكل غرض على حدة. يمكنك سحبها في أي وقت برابط إلغاء الاشتراك في كل رسالة أو بمراسلة privacy@loupe-ai.com.</li>
<li><strong>سجل التدقيق:</strong> كل موافقة تُعطى أو تُؤكَّد أو تُسحب تُحفظ في سجل للإضافة فقط لنثبت ما وافقت عليه ومتى. بعد إلغاء اشتراكك نحتفظ فقط بما يلزم لإثبات ذلك ولعدم مراسلتك مجددًا، لمدة [مدة الاحتفاظ — يؤكدها المحامي].</li>
<li><strong>من يعالجها نيابةً عنا:</strong> Supabase (قاعدة البيانات) [المنطقة — للتأكيد] وResend (إرسال البريد). لا نبيعها ولا نشاركها ولا نستخدمها للإعلانات.</li>
</ul>
<h3>أعداد التنزيل</h3>
<ul>
<li>عند الضغط على زر تنزيل يسجّل الموقع: المنصة، وإصدار التطبيق، ولغة الصفحة ومسارها، والوقت، ورمز الدولة المكوّن من حرفين المستنتج من الاتصال.</li>
<li><strong>بلا ملفات تعريف ارتباط، وبلا عنوان IP، وبلا user agent، وبلا أي معرّف</strong> — لا يمكن ربط العدد بك أو بتسجيلك.</li>
</ul>
<h3>كل ما عدا ذلك في الموقع</h3>
<ul>
<li>لا ملفات تعريف ارتباط ولا تحليلات ولا إعلانات ولا نصوص تتبّع. الخطوط تُقدَّم من loupe-ai.com نفسه.</li>
<li>قد يحتفظ مستضيف الموقع بسجلات خادم معتادة (تشمل عناوين IP) لأغراض الأمان وفق سياسته: [المستضيف — مثل GitHub Pages — للتأكيد].</li>
<li>رابط تنزيل Mac يشير إلى مستودع التنزيلات العام على GitHub؛ وتنزيل ملف منه تتولاه GitHub وفق سياستها.</li>
</ul>
</section>
""",
}
