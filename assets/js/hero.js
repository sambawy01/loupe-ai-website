/* Hero: an illustration of Loupe's live run view. Stages on a loop around the mascot (the engine),
   question diamonds that show their latest answer, one particle per item, coloured by where it went.
   Runs client-side only; nothing is fetched. Pauses off-screen; static under reduced motion. */
(function () {
  var canvas = document.getElementById('pipeline');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var L = JSON.parse(canvas.getAttribute('data-labels') || '{}');
  var rtl = document.documentElement.dir === 'rtl';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hudCount = document.getElementById('hud-count');
  var hudRate = document.getElementById('hud-rate');
  var C = { cyan: '#22D3EE', blue: '#2F6BFF', mint: '#10B981', amber: '#F5B544', red: '#FF6B81', line: '#1E3170', ink: '#EAF2FF', ink3: '#8FA3CF', bg: '#0B1530' };
  var W = 0, H = 0, dpr = 1, running = false, visible = true, last = 0, spawnAcc = 0, count = 0;
  var particles = [];
  var ringR = 0.37;
  // angles in turns (0 = right), direction flips for RTL so the flow reads start→end
  var stages = [
    { a: 0.5, kind: 'node', label: L.read || 'Read' },
    { a: 0.625, kind: 'q', label: L.q1 || 'receipt?', ans: '', conf: 0 },
    { a: 0.75, kind: 'q', label: L.q2 || 'for tax?', ans: '', conf: 0 },
    { a: 0.875, kind: 'q', label: L.q3 || 'sure?', ans: '', conf: 0 },
    { a: 1.0, kind: 'node', label: L.decide || 'Decide' }
  ];
  var outs = [
    { a: 0.08, label: L.sorted || 'Sorted', color: C.mint, n: 0 },
    { a: 0.2, label: L.needs || 'Needs you', color: C.amber, n: 0 },
    { a: 0.32, label: L.flag || 'Flagged', color: C.red, n: 0 }
  ];
  var answers = L.answers || [['yes', 'no'], ['yes', 'no'], ['sure', 'unsure']];

  function pos(turn, r) {
    var t = turn * Math.PI * 2;
    var x = Math.cos(t) * r; if (rtl) x = -x;
    return [W / 2 + x * W, H / 2 - Math.sin(t) * r * H];
  }
  function resize() {
    var rect = canvas.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = rect.width; H = rect.height;
    canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    if (!running) draw(0);
  }
  function diamond(x, y, s, active) {
    ctx.beginPath(); ctx.moveTo(x, y - s); ctx.lineTo(x + s, y); ctx.lineTo(x, y + s); ctx.lineTo(x - s, y); ctx.closePath();
    ctx.fillStyle = C.bg; ctx.fill();
    ctx.lineWidth = 1.5; ctx.strokeStyle = active ? C.cyan : '#2A4290';
    if (active && !reduce) { ctx.shadowColor = C.cyan; ctx.shadowBlur = 14; }
    ctx.stroke(); ctx.shadowBlur = 0;
  }
  function text(str, x, y, color, size, weight, align) {
    ctx.fillStyle = color; ctx.font = (weight || 500) + ' ' + size + 'px "JetBrains Mono", "Noto Kufi Arabic", monospace';
    ctx.textAlign = align || 'center'; ctx.textBaseline = 'middle'; ctx.fillText(str, x, y);
  }
  function draw(dt) {
    ctx.clearRect(0, 0, W, H);
    var s = Math.min(W, H);
    // ring
    ctx.lineWidth = 1; ctx.strokeStyle = C.line; ctx.setLineDash([3, 6]);
    ctx.beginPath(); ctx.ellipse(W / 2, H / 2, ringR * W, ringR * H, 0, 0, Math.PI * 2); ctx.stroke(); ctx.setLineDash([]);
    // active arc (start → decide)
    var g = ctx.createLinearGradient(0, 0, W, 0); g.addColorStop(0, 'rgba(47,107,255,.7)'); g.addColorStop(1, 'rgba(34,211,238,.7)');
    ctx.strokeStyle = g; ctx.lineWidth = 2; ctx.beginPath();
    for (var i = 0; i <= 60; i++) { var p = pos(0.5 + i / 120, ringR); i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]); }
    ctx.stroke();
    // exits
    outs.forEach(function (o) {
      var a = pos(1.0, ringR), b = pos(o.a, ringR + 0.1);
      ctx.strokeStyle = 'rgba(42,66,144,.8)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(a[0], a[1]);
      ctx.quadraticCurveTo(pos(o.a * 0.5, ringR + 0.05)[0], pos(o.a * 0.5, ringR + 0.05)[1], b[0], b[1]); ctx.stroke();
      ctx.fillStyle = o.color; ctx.beginPath(); ctx.arc(b[0], b[1], 4, 0, Math.PI * 2); ctx.fill();
      var lab = pos(o.a, ringR + 0.1);
      text(o.label + ' · ' + o.n, lab[0] + (rtl ? 10 : -10) * (lab[0] > W / 2 ? -1 : 1), lab[1] + 16, C.ink3, Math.max(10, s * 0.022), 500);
    });
    // stages
    stages.forEach(function (st) {
      var p = pos(st.a, ringR);
      if (st.kind === 'q') {
        diamond(p[0], p[1], s * 0.04, st.flash > 0);
        text(st.label, p[0], p[1] - s * 0.075, C.ink, Math.max(10, s * 0.024), 600);
        if (st.ans) text(st.ans + ' ' + st.conf.toFixed(2), p[0], p[1] + s * 0.07, st.flash > 0 ? C.cyan : C.ink3, Math.max(9, s * 0.021), 500);
        if (st.flash > 0) st.flash -= dt;
      } else {
        ctx.fillStyle = C.bg; ctx.strokeStyle = '#2A4290'; ctx.lineWidth = 1.5;
        var w = s * 0.14, h = s * 0.06; roundRect(p[0] - w / 2, p[1] - h / 2, w, h, 8); ctx.fill(); ctx.stroke();
        text(st.label, p[0], p[1], C.ink, Math.max(10, s * 0.024), 600);
      }
    });
    // particles
    for (var k = 0; k < particles.length; k++) {
      var q = particles[k], xy;
      if (q.phase === 0) xy = pos(q.t, ringR);
      else { var a0 = pos(1.0, ringR), b0 = pos(q.out.a, ringR + 0.1), c0 = pos(q.out.a * 0.5, ringR + 0.05), u = q.t;
        xy = [(1 - u) * (1 - u) * a0[0] + 2 * (1 - u) * u * c0[0] + u * u * b0[0], (1 - u) * (1 - u) * a0[1] + 2 * (1 - u) * u * c0[1] + u * u * b0[1]]; }
      ctx.fillStyle = q.phase === 0 ? C.cyan : q.out.color;
      ctx.shadowColor = ctx.fillStyle; ctx.shadowBlur = 8;
      ctx.beginPath(); ctx.arc(xy[0], xy[1], 2.6, 0, Math.PI * 2); ctx.fill();
    }
    ctx.shadowBlur = 0;
  }
  function roundRect(x, y, w, h, r) {
    ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
  }
  function step(dt) {
    spawnAcc += dt * 10; // about 10 items a second: the pace measured in the iPhone simulator
    while (spawnAcc > 1) { spawnAcc -= 1; particles.push({ t: 0.5, phase: 0, qi: 1, speed: 0.16 + Math.random() * 0.04 }); }
    for (var i = particles.length - 1; i >= 0; i--) {
      var p = particles[i];
      if (p.phase === 0) {
        p.t += p.speed * dt;
        if (p.qi < 4 && p.t >= stages[p.qi].a) {
          var st = stages[p.qi], sure = Math.random();
          var ans = answers[p.qi - 1] || ['yes', 'no'];
          st.ans = sure > 0.35 ? ans[0] : ans[1]; st.conf = 0.5 + Math.random() * 0.49; st.flash = 0.18; p.qi++;
        }
        if (p.t >= 1.0) {
          p.phase = 1; p.t = 0; var r = Math.random();
          p.out = r < 0.72 ? outs[0] : r < 0.93 ? outs[1] : outs[2];
          count++; p.out.n++;
        }
      } else { p.t += dt * 1.4; if (p.t >= 1) particles.splice(i, 1); }
    }
  }
  var rateWin = [];
  function frame(ts) {
    if (!running) return;
    var dt = last ? Math.min((ts - last) / 1000, 0.05) : 0; last = ts;
    step(dt); draw(dt);
    rateWin.push([ts, count]); while (rateWin.length && ts - rateWin[0][0] > 2000) rateWin.shift();
    if (hudCount) hudCount.textContent = count.toLocaleString(document.documentElement.lang);
    if (hudRate && rateWin.length > 1) { var d = rateWin[rateWin.length - 1], e = rateWin[0]; hudRate.textContent = ((d[1] - e[1]) / ((d[0] - e[0]) / 1000 || 1)).toFixed(1); }
    requestAnimationFrame(frame);
  }
  function start() { if (running || reduce || !visible || document.hidden) return; running = true; last = 0; requestAnimationFrame(frame); }
  function stop() { running = false; }
  if (reduce) { // one static frame: a few answered diamonds, no particles
    stages[1].ans = answers[0][0]; stages[1].conf = 0.91; stages[2].ans = answers[1][0]; stages[2].conf = 0.78; stages[3].ans = answers[2][1]; stages[3].conf = 0.55;
    outs[0].n = 72; outs[1].n = 21; outs[2].n = 7;
  }
  window.addEventListener('resize', resize);
  document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
  if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { visible = e[0].isIntersecting; visible ? start() : stop(); }).observe(canvas);
  resize(); start();
})();
