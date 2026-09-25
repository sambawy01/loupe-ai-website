/* "Teach a judgment" demo. Made-up sample items with scripted answers, sorted client-side.
   It shows how Loupe presents results (answer, confidence, unsure queue, keyword baseline);
   it is not the model and its numbers are not measurements. */
(function () {
  var root = document.getElementById('demo');
  var dataEl = document.getElementById('demo-data');
  if (!root || !dataEl) return;
  var D = JSON.parse(dataEl.textContent);
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var buttons = root.querySelectorAll('.judg');
  var qEl = root.querySelector('.demo-q');
  var feed = root.querySelector('.feed');
  var lists = { yes: root.querySelector('.bin.yes ul'), no: root.querySelector('.bin.no ul'), unsure: root.querySelector('.bin.unsure ul') };
  var counts = { yes: root.querySelector('.bin.yes .c'), no: root.querySelector('.bin.no .c'), unsure: root.querySelector('.bin.unsure .c') };
  var foot = root.querySelector('.demo-foot');
  var live = root.querySelector('[aria-live]');
  var timer = null;

  function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function bin(p) { return p >= 0.7 ? 'yes' : p <= 0.3 ? 'no' : 'unsure'; }
  function run(idx) {
    var J = D.judgments[idx];
    clearTimeout(timer);
    buttons.forEach(function (b, i) { b.setAttribute('aria-pressed', i === idx ? 'true' : 'false'); });
    qEl.textContent = '“' + J.q + '”';
    Object.keys(lists).forEach(function (k) { lists[k].innerHTML = ''; counts[k].textContent = '0'; });
    foot.innerHTML = '';
    var n = { yes: 0, no: 0, unsure: 0 }, agree = 0, decided = 0, i = 0;
    function next() {
      if (i >= J.items.length) return finish();
      var it = J.items[i++], b = bin(it.p);
      var kwYes = !!it.kw, modelYes = b === 'yes';
      if (b !== 'unsure') { decided++; if (kwYes === modelYes) agree++; }
      var li = document.createElement('li'); li.className = 'item';
      li.innerHTML = '<div class="src"><span>' + esc(it.src) + '</span><span>' + (b === 'unsure' ? D.l.unsure : (b === 'yes' ? D.l.yes : D.l.no)) + ' ' + it.p.toFixed(2) + '</span></div>' +
        esc(it.t) + '<div class="bar"><i style="width:' + Math.round((b === 'no' ? 1 - it.p : it.p) * 100) + '%"></i></div>' +
        '<div class="kw' + (b !== 'unsure' && kwYes !== modelYes ? ' dis' : '') + '">' + D.l.kw + ': ' + (kwYes ? D.l.yes : D.l.no) + '</div>';
      lists[b].appendChild(li); n[b]++; counts[b].textContent = n[b];
      feed.textContent = D.l.reading + ' ' + it.t;
      timer = setTimeout(next, reduce ? 0 : 380);
    }
    function finish() {
      feed.textContent = D.l.done;
      foot.innerHTML = '<span>' + D.l.decided + ' <b>' + decided + '/' + J.items.length + '</b></span>' +
        '<span>' + D.l.queue + ' <b>' + n.unsure + '</b></span>' +
        '<span>' + D.l.agreeKw + ' <b>' + agree + '/' + decided + '</b></span>';
      if (live) live.textContent = D.l.summary.replace('{d}', decided).replace('{u}', n.unsure).replace('{a}', agree);
    }
    next();
  }
  buttons.forEach(function (b, i) { b.addEventListener('click', function () { run(i); }); });
  var started = false;
  function kick() { if (!started) { started = true; run(0); } }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (e) { if (e[0].isIntersecting) { kick(); io.disconnect(); } }, { threshold: 0.25 });
    io.observe(root);
  } else kick();
})();
