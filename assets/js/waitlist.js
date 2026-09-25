/* Waitlist / subscribe form → Supabase REST insert into public.subscribers (anon may INSERT only).
   Double opt-in: the row starts "pending"; the send-confirmation Edge Function emails a link.
   The exact consent text shown is stored with the row, with its version. */
(function () {
  var form = document.getElementById('waitlist-form');
  if (!form) return;
  var CFG = window.LOUPE_CONFIG || {};
  var T = JSON.parse(document.getElementById('i18n').textContent);
  var status = form.querySelector('.form-status');
  var btn = form.querySelector('button[type=submit]');

  function say(msg, cls) { status.textContent = msg; status.className = 'form-status ' + (cls || ''); }
  function textOf(id) { var el = document.getElementById(id); return el ? el.textContent.replace(/\s+/g, ' ').trim() : ''; }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    say('');
    var email = form.email.value.trim();
    if (!form.email.checkValidity() || !email) { say(T.errEmail, 'err'); form.email.focus(); return; }
    if (!form.ack_privacy.checked) { say(T.errAck, 'err'); form.ack_privacy.focus(); return; }
    if (form.website && form.website.value) { say(T.ok, 'ok'); form.reset(); return; } // honeypot: quietly drop bots

    var platforms = Array.prototype.map.call(form.querySelectorAll('input[name=platforms]:checked'), function (x) { return x.value; });
    var consent = {};
    ['product_updates', 'promotions', 'beta_invites', 'research'].forEach(function (k) {
      consent[k] = { granted: !!form['c_' + k].checked, text: textOf('t_' + k) };
    });
    var row = {
      email: email.toLowerCase(),
      name: form.name.value.trim() || null,
      platforms: platforms,
      country_declared: form.country.value || null,
      language: form.language.value || document.documentElement.lang,
      locale: document.documentElement.lang,
      consent_product_updates: consent.product_updates.granted,
      consent_promotions: consent.promotions.granted,
      consent_beta_invites: consent.beta_invites.granted,
      consent_research: consent.research.granted,
      privacy_ack: true,
      consent_record: {
        version: CFG.CONSENT_TEXT_VERSION,
        shown_at: new Date().toISOString(),
        page: location.pathname,
        purposes: consent,
        privacy_ack_text: textOf('t_ack')
      },
      consent_text_version: CFG.CONSENT_TEXT_VERSION
    };

    if (!(window.LoupeSB && window.LoupeSB.ready())) { say(T.notConfigured, 'err'); return; }
    btn.disabled = true; say(T.sending);
    fetch(CFG.SUPABASE_URL + '/rest/v1/subscribers', {
      method: 'POST', credentials: 'omit', referrerPolicy: 'no-referrer',
      headers: { 'apikey': CFG.SUPABASE_ANON_KEY, 'Authorization': 'Bearer ' + CFG.SUPABASE_ANON_KEY, 'Content-Type': 'application/json', 'Prefer': 'return=minimal' },
      body: JSON.stringify(row)
    }).then(function (r) {
      // 201 created; 409 = this address is already on the list. Same answer either way, so the form
      // never reveals whether an address is subscribed.
      if (r.status === 201 || r.status === 409) { say(T.ok, 'ok'); form.reset(); }
      else if (r.status === 429) say(T.errRate, 'err');
      else say(T.errGeneric, 'err');
    }).catch(function () { say(T.errGeneric, 'err'); })
      .then(function () { btn.disabled = false; });
  });
})();
