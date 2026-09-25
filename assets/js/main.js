/* Site behaviour: nav, reveal, device carousel, privacy meter, download buttons + beacon, App Store state. */
(function () {
  var doc = document.documentElement;
  doc.classList.remove('no-js');
  var CFG = window.LOUPE_CONFIG || {};
  var T = {};
  try { T = JSON.parse(document.getElementById('i18n').textContent); } catch (e) {}
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var lang = doc.lang || 'en';

  // mobile nav
  var mb = document.querySelector('.menu-btn'), nav = document.getElementById('nav');
  if (mb && nav) mb.addEventListener('click', function () {
    var open = nav.classList.toggle('open'); mb.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // reveal on scroll
  var rev = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { rootMargin: '0px 0px -8% 0px' });
    rev.forEach(function (el) { io.observe(el); });
  } else rev.forEach(function (el) { el.classList.add('in'); });

  // device carousel (tabs)
  document.querySelectorAll('[data-carousel]').forEach(function (car) {
    var tabs = car.querySelectorAll('[role=tab]'), imgs = car.querySelectorAll('.phone img'), cap = car.querySelector('.car-cap');
    var cur = 0, auto = null;
    function show(i, focus) {
      cur = (i + tabs.length) % tabs.length;
      tabs.forEach(function (t, k) { t.setAttribute('aria-selected', k === cur ? 'true' : 'false'); t.tabIndex = k === cur ? 0 : -1; });
      imgs.forEach(function (im, k) {
        if (k === cur && im.dataset.src) { im.src = im.dataset.src; im.srcset = im.dataset.srcset || ''; delete im.dataset.src; }
        im.classList.toggle('on', k === cur); im.setAttribute('aria-hidden', k === cur ? 'false' : 'true');
      });
      if (cap) cap.textContent = tabs[cur].getAttribute('data-cap');
      if (focus) tabs[cur].focus();
    }
    tabs.forEach(function (t, k) {
      t.addEventListener('click', function () { stopAuto(); show(k); });
      t.addEventListener('keydown', function (e) {
        var rtl = doc.dir === 'rtl', nxt = rtl ? 'ArrowLeft' : 'ArrowRight', prv = rtl ? 'ArrowRight' : 'ArrowLeft';
        if (e.key === nxt) { stopAuto(); show(cur + 1, true); e.preventDefault(); }
        if (e.key === prv) { stopAuto(); show(cur - 1, true); e.preventDefault(); }
      });
    });
    function stopAuto() { clearInterval(auto); auto = null; }
    car.addEventListener('focusin', stopAuto);
    show(0);
    if (!reduce && 'IntersectionObserver' in window) {
      new IntersectionObserver(function (e) {
        if (e[0].isIntersecting && !auto) auto = setInterval(function () { show(cur + 1); }, 4200);
        else if (!e[0].isIntersecting) stopAuto();
      }).observe(car);
    }
  });

  // privacy meter
  var meter = document.getElementById('meter');
  if (meter) {
    var arc = meter.querySelector('.arc'), opsEl = document.getElementById('ops'), log = document.getElementById('netlog');
    var air = document.getElementById('airplane');
    var lines = T.log || [];
    var ops = 0, li = 0, mt = null, total = 1200;
    function addLine(html) { var d = document.createElement('div'); d.innerHTML = html; log.appendChild(d); while (log.children.length > 7) log.removeChild(log.firstChild); }
    function tick() {
      ops = Math.min(total, ops + 37); opsEl.textContent = ops.toLocaleString(lang);
      arc.style.strokeDashoffset = String(565 - 565 * ops / total);
      if (ops % 185 < 37 && lines.length) addLine(lines[li++ % lines.length]);
      if (ops < total) mt = setTimeout(tick, 60); else addLine('<span class="ok">' + (T.logDone || '') + '</span>');
    }
    function startMeter() { clearTimeout(mt); ops = 0; li = 0; log.innerHTML = ''; if (reduce) { ops = total - 37; } tick(); }
    if (air) air.addEventListener('change', function () {
      addLine('<span class="ok">' + (air.checked ? T.airOn : T.airOff) + '</span>');
      if (air.checked) startMeter();
    });
    if ('IntersectionObserver' in window) {
      var mo = new IntersectionObserver(function (e) { if (e[0].isIntersecting) { startMeter(); mo.disconnect(); } }, { threshold: 0.3 });
      mo.observe(meter);
    } else startMeter();
  }

  // Supabase configured?
  function sbReady() {
    return CFG.SUPABASE_URL && CFG.SUPABASE_ANON_KEY && CFG.SUPABASE_URL.indexOf('YOUR-') === -1 && CFG.SUPABASE_ANON_KEY.indexOf('YOUR-') === -1;
  }
  window.LoupeSB = { ready: sbReady };

  // download beacon: no cookies, no IP or user agent stored (see supabase/schema.sql)
  function beacon(platform, version) {
    if (!sbReady()) return Promise.resolve();
    var body = JSON.stringify({ platform: platform, version: version || null, locale: lang, page: location.pathname.slice(0, 100) });
    try {
      return fetch(CFG.SUPABASE_URL + '/rest/v1/download_events', {
        method: 'POST', keepalive: true, credentials: 'omit', referrerPolicy: 'no-referrer',
        headers: { 'apikey': CFG.SUPABASE_ANON_KEY, 'Authorization': 'Bearer ' + CFG.SUPABASE_ANON_KEY, 'Content-Type': 'application/json', 'Prefer': 'return=minimal' },
        body: body
      }).catch(function () {});
    } catch (e) { return Promise.resolve(); }
  }
  function wireDownload(a) {
    a.addEventListener('click', function (e) {
      if (a.getAttribute('aria-disabled') === 'true') { e.preventDefault(); var w = document.getElementById('waitlist'); if (w) { w.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' }); var f = w.querySelector('input[type=email]'); if (f) f.focus({ preventScroll: true }); } else location.href = T.waitlistHref; return; }
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) { beacon(a.dataset.platform, a.dataset.version); return; }
      e.preventDefault();
      var href = a.href, go = function () { location.href = href; };
      Promise.race([beacon(a.dataset.platform, a.dataset.version), new Promise(function (r) { setTimeout(r, 350); })]).then(go, go);
    });
  }

  // Mac: latest release in sambawy01/loupe-downloads, else "coming soon"
  var macBtns = document.querySelectorAll('[data-download=mac]');
  function macState(ok, url, version) {
    macBtns.forEach(function (a) {
      var label = a.querySelector('.lbl'), sub = a.querySelector('small');
      if (ok) {
        a.href = url; a.removeAttribute('aria-disabled'); a.dataset.version = version || '';
        if (label) label.textContent = T.macDownload; if (sub) sub.textContent = (version ? 'v' + version + ' · ' : '') + T.macReq;
      } else {
        a.href = T.waitlistHref; a.setAttribute('aria-disabled', 'true');
        if (label) label.textContent = T.macSoon; if (sub) sub.textContent = T.macSoonSub;
      }
    });
  }
  if (macBtns.length) {
    macBtns.forEach(wireDownload);
    if (CFG.MAC_AVAILABLE === true) macState(true, CFG.MAC_DOWNLOAD_URL, '');
    else if (CFG.MAC_AVAILABLE === false) macState(false);
    else {
      macState(false);
      fetch(CFG.MAC_RELEASES_API, { credentials: 'omit', referrerPolicy: 'no-referrer', headers: { 'Accept': 'application/vnd.github+json' } })
        .then(function (r) { if (!r.ok) throw 0; return r.json(); })
        .then(function (rel) {
          var dmg = (rel.assets || []).filter(function (x) { return /\.dmg$/i.test(x.name); })[0];
          if (!dmg) throw 0;
          macState(true, dmg.browser_download_url, String(rel.tag_name || '').replace(/^v/, ''));
        })
        .catch(function () { macState(false); });
    }
  }

  // iPhone: App Store badge, "Coming to the App Store" until published
  document.querySelectorAll('[data-download=ios]').forEach(function (a) {
    var sm = a.querySelector('.top'), big = a.querySelector('b');
    if (CFG.IOS_AVAILABLE) { a.href = CFG.APP_STORE_URL; a.removeAttribute('aria-disabled'); if (sm) sm.textContent = T.iosTop; if (big) big.textContent = 'App Store'; }
    else { a.href = T.waitlistHref; a.setAttribute('aria-disabled', 'true'); if (sm) sm.textContent = T.iosSoonTop; if (big) big.textContent = 'App Store'; }
    wireDownload(a);
  });

  // confirmation redirect toast (?subscribed=confirmed|unsubscribed|invalid)
  var m = /[?&]subscribed=(\w+)/.exec(location.search);
  if (m && T['toast_' + m[1]]) {
    var t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); t.textContent = T['toast_' + m[1]];
    document.body.appendChild(t); setTimeout(function () { t.remove(); }, 7000);
  }
})();
