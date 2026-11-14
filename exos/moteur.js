/* Moteur commun des pages « S'entraîner » (exos/<niveau>-sXX.html).
   La page charge ce fichier, définit ses exercices avec les outils M.*, puis appelle M.start({key, EX, NOTIONS}).
   Chaque exercice : {id, lv (1 à 3), nq (nombre de questions, 5 par défaut), n, t, d, c (consigne), a (aide), g(): question}.
   Une question : {q, svg?, key?, steps: [lignes], type, …}
     type 'num'  : v (attendu), x (valeur exacte), d (arrondi, décimales) ou undefined si exact, lab, unit, traps [[valeur, message]]
     type 'frac' : f [num, den] (irréductible), lab, dec (accepter l'écriture décimale exacte), traps
     type 'expr' : P (polynôme {degré: coef}), mode 'dev' (développé réduit) ou 'fact' (produit), lab, traps [[P, message]]
     type 'ch'   : ch [choix], ans (indice) ; la correction s'affiche dès la réponse */
(function(){
'use strict';
var M = window.M = {};
var MINUS = M.MINUS = '−', SQ = M.SQ = '²', RAC = M.RAC = '√';
function el(tag, cls, txt){ var e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; }
var rnd = M.rnd = function(a, b){ return a + Math.floor(Math.random() * (b - a + 1)); };
M.rnz = function(a, b){ var v; do { v = rnd(a, b); } while (v === 0); return v; };
var pick = M.pick = function(a){ return a[Math.floor(Math.random() * a.length)]; };
M.shuffle = function(a){ for (var i = a.length - 1; i > 0; i--){ var j = rnd(0, i), t = a[i]; a[i] = a[j]; a[j] = t; } return a; };
function store(k, v){ try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch(e){ return null; } }
var rd = M.rd = function(x, d){ var p = Math.pow(10, d); return Math.round(x * p + (x >= 0 ? 1e-9 : -1e-9)) / p; };
var cl = M.cl = function(x){ return rd(x, 6); };
M.sq = function(x){ return cl(x * x); };
M.isInt = function(x){ return Math.abs(x - Math.round(x)) < 1e-9; };
var gcd = M.gcd = function(a, b){ a = Math.abs(a); b = Math.abs(b); while (b){ var t = a % b; a = b; b = t; } return a || 1; };
// écriture française d'un nombre : virgule, espace fine des milliers (à partir de 5 chiffres), signe −
var fr = M.fr = function(x){ x = cl(x); var neg = x < 0, t = String(Math.abs(x)).split('.'), ip = t[0];
  if (ip.length > 4) ip = ip.replace(/\B(?=(\d{3})+$)/g, ' ');
  return (neg ? MINUS : '') + ip + (t[1] ? ',' + t[1] : ''); };
M.pf = function(x){ return x < 0 ? '(' + fr(x) + ')' : fr(x); };          // (−4) ; 9
// fractions [n, d] avec d > 0
var red = M.red = function(n, d){ if (d < 0){ n = -n; d = -d; } var g = gcd(n, d); return [n / g, d / g]; };
var ftx = M.ftx = function(f){ return f[1] === 1 ? fr(f[0]) : (f[0] < 0 ? MINUS : '') + Math.abs(f[0]) + '/' + f[1]; };
M.fadd = function(a, b){ return red(a[0] * b[1] + b[0] * a[1], a[1] * b[1]); };
M.fmul = function(a, b){ return red(a[0] * b[0], a[1] * b[1]); };
M.fval = function(f){ return f[0] / f[1]; };
M.letters = function(k){ var L = 'ABCDEFGHIJKLMNPRSTUVWXYZ'.split(''); M.shuffle(L); return L.slice(0, k || 3); };
M.figTri = function(T, a, b, lab, ang){
  var ra = a, rb = b, rr = ra / rb; if (rr > 2.3) ra = 2.3 * rb; if (rr < 1 / 2.3) rb = 2.3 * ra;
  var th = Math.random() * 2 * Math.PI, fl = Math.random() < 0.5 ? -1 : 1;
  var ux = Math.cos(th), uy = Math.sin(th), vx = -Math.sin(th) * fl, vy = Math.cos(th) * fl;
  var P0 = [0, 0], P1 = [ra * ux, ra * uy], P2 = [rb * vx, rb * vy];
  var xs = [P0[0], P1[0], P2[0]], ys = [P0[1], P1[1], P2[1]];
  var W = 300, H = 210, pad = 40, mnx = Math.min.apply(0, xs), mxx = Math.max.apply(0, xs), mny = Math.min.apply(0, ys), mxy = Math.max.apply(0, ys);
  var k = Math.min((W - 2 * pad) / (mxx - mnx || 1), (H - 2 * pad) / (mxy - mny || 1));
  var ox = (W - k * (mxx - mnx)) / 2 - k * mnx, oy = (H - k * (mxy - mny)) / 2 - k * mny;
  function m(p){ return [ox + k * p[0], oy + k * p[1]]; }
  var A = m(P0), B = m(P1), C = m(P2), G = [(A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3];
  function f(v){ return v.toFixed(1); }
  function out(p, d){ var dx = p[0] - G[0], dy = p[1] - G[1], l = Math.hypot(dx, dy) || 1; return [p[0] + dx / l * d, p[1] + dy / l * d]; }
  function lbl(p, t, cls){ return '<text x="' + f(p[0]) + '" y="' + f(p[1]) + '" class="' + (cls || 'pt') + '" text-anchor="middle" dominant-baseline="central">' + t + '</text>'; }
  function mid(p, q, t){ var M = [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2], dx = q[0] - p[0], dy = q[1] - p[1], l = Math.hypot(dx, dy), nx = -dy / l, ny = dx / l;
    if ((M[0] + nx - G[0]) * nx + (M[1] + ny - G[1]) * ny < 0){ nx = -nx; ny = -ny; }
    var w = t.length * 4.3 + 6; return lbl([M[0] + nx * (14 + Math.abs(nx) * w * 0.6), M[1] + ny * 15], t, t === '?' ? 'qm' : 'ln'); }
  var s = 12, U = [(B[0] - A[0]) / Math.hypot(B[0] - A[0], B[1] - A[1]), (B[1] - A[1]) / Math.hypot(B[0] - A[0], B[1] - A[1])], V = [(C[0] - A[0]) / Math.hypot(C[0] - A[0], C[1] - A[1]), (C[1] - A[1]) / Math.hypot(C[0] - A[0], C[1] - A[1])];
  var sqp = [A, [A[0] + U[0] * s, A[1] + U[1] * s], [A[0] + U[0] * s + V[0] * s, A[1] + U[1] * s + V[1] * s], [A[0] + V[0] * s, A[1] + V[1] * s]];
  var h = '<svg viewBox="0 0 ' + W + ' ' + H + '" class="fig" role="img" aria-label="Triangle ' + T.name + ' rectangle en ' + T.R + '">';
  h += '<polygon points="' + [A, B, C].map(function(p){ return f(p[0]) + ',' + f(p[1]); }).join(' ') + '" class="tr"/>';
  h += '<line x1="' + f(B[0]) + '" y1="' + f(B[1]) + '" x2="' + f(C[0]) + '" y2="' + f(C[1]) + '" class="hy"/>';
  h += '<polyline points="' + sqp.map(function(p){ return f(p[0]) + ',' + f(p[1]); }).join(' ') + '" class="ra"/>';
  h += lbl(out(A, 15), T.R) + lbl(out(B, 15), T.P) + lbl(out(C, 15), T.Q);
  if (lab.a) h += mid(A, B, lab.a); if (lab.b) h += mid(A, C, lab.b); if (lab.c) h += mid(B, C, lab.c);
  if (ang){ var V0 = ang.at === 'P' ? B : C, O1 = A, O2 = ang.at === 'P' ? C : B, r = 26;
    var a1 = Math.atan2(O1[1] - V0[1], O1[0] - V0[0]), a2 = Math.atan2(O2[1] - V0[1], O2[0] - V0[0]), da = a2 - a1;
    while (da > Math.PI) da -= 2 * Math.PI; while (da < -Math.PI) da += 2 * Math.PI;
    var E1 = [V0[0] + r * Math.cos(a1), V0[1] + r * Math.sin(a1)], E2 = [V0[0] + r * Math.cos(a1 + da), V0[1] + r * Math.sin(a1 + da)];
    h += '<path class="an" d="M' + f(E1[0]) + ',' + f(E1[1]) + ' A' + r + ',' + r + ' 0 0 ' + (da > 0 ? 1 : 0) + ' ' + f(E2[0]) + ',' + f(E2[1]) + '"/>';
    var am = a1 + da / 2; if (ang.t) h += lbl([V0[0] + (r + 16) * Math.cos(am), V0[1] + (r + 16) * Math.sin(am)], ang.t, ang.t === '?' ? 'qm' : 'ln'); }
  return h + '</svg>';
};

var ARR = M.ARR = {0: 'à l’unité', 1: 'au dixième', 2: 'au centième'};
// polynômes {degré: coef}
var mono = M.mono = function(c, d){ var x = d === 0 ? '' : d === 1 ? 'x' : 'x' + (d === 2 ? '²' : d === 3 ? '³' : '^' + d), a = Math.abs(c);
  return (c < 0 ? MINUS : '') + (d > 0 && a === 1 ? '' : fr(a)) + x; };
M.poly = function(P){ var s = '', first = true;
  [4, 3, 2, 1, 0].forEach(function(d){ var c = P[d] || 0; if (!c) return;
    var m = mono(Math.abs(c), d); s += first ? (c < 0 ? MINUS : '') + m : (c < 0 ? ' ' + MINUS + ' ' : ' + ') + m; first = false; });
  return first ? '0' : s; };
M.terms = function(T){ return T.map(function(t, i){ var c = t[0], m = mono(Math.abs(c), t[1]);
  return i === 0 ? (c < 0 ? MINUS : '') + m : (c < 0 ? ' ' + MINUS + ' ' : ' + ') + m; }).join(''); };
var sameP = M.sameP = function(A, B){ for (var d = 0; d <= 6; d++) if (Math.abs((A[d] || 0) - (B[d] || 0)) > 1e-9) return false; return true; };
function padd(A, B, s){ var R = {}, d; for (d = 0; d <= 6; d++){ var v = (A[d] || 0) + s * (B[d] || 0); if (Math.abs(v) > 1e-12) R[d] = cl(v); } return R; }
function pmul(A, B){ var R = {}; for (var i in A) for (var j in B){ var d = +i + +j; R[d] = cl((R[d] || 0) + A[i] * B[j]); } for (var k in R) if (!R[k]) delete R[k]; return R; }
M.pmul = pmul; M.padd = padd;
/* Lecture d'une expression littérale : renvoie {P, paren, prod, reduit, fois} ou null.
   prod : l'expression est un produit (pas de + ou − au premier niveau). */
var parseExpr = M.parseExpr = function(s){
  s = String(s || '').replace(/[−–—]/g, '-').replace(/\s+/g, '').replace(/,/g, '.').replace(/[×·*]/g, '*').replace(/X/g, 'x')
       .replace(/²/g, '^2').replace(/³/g, '^3').replace(/x(\d)(?![\d.])/g, 'x^$1');
  if (!s) return null;
  var i = 0, terms0 = 0, info = {paren: /[()]/.test(s), fois: /\*/.test(s)};
  function peek(){ return s[i]; }
  function expr(top){ var P = {}, first = true, n = 0, sign = 1;
    while (i < s.length && peek() !== ')'){
      sign = 1;
      if (peek() === '+' || peek() === '-'){ sign = peek() === '-' ? -1 : 1; i++; }
      else if (!first) return null;
      var T = term(); if (!T) return null; P = padd(P, T, sign); n++; first = false; }
    if (top) terms0 = n; return P; }
  function term(){ var P = {0: 1}, k = 0;
    while (i < s.length){ var c = peek(), F;
      if (c === '*'){ if (!k) return null; i++; continue; }
      if (/[\d.]/.test(c)){ var m = s.slice(i).match(/^\d+(\.\d+)?/); if (!m) return null; i += m[0].length; F = {0: parseFloat(m[0])}; }
      else if (c === 'x'){ i++; F = {1: 1}; }
      else if (c === '('){ i++; F = expr(false); if (!F || peek() !== ')') return null; i++; }
      else break;
      if (peek() === '^'){ i++; var m2 = s.slice(i).match(/^\d/); if (!m2) return null; i++; var e = +m2[0], G = {0: 1}; while (e--) G = pmul(G, F); F = G; }
      P = pmul(P, F); k++; }
    return k ? P : null; }
  var P = expr(true); if (!P || i !== s.length) return null;
  // réduit : pas de parenthèses, pas de ×, chaque degré une fois, pas deux nombres dans un terme
  var red2 = !info.paren && !info.fois, seen = {};
  if (red2) s.replace(/^[+-]?/, '').split(/[+-]/).forEach(function(t){
    var d = (t.match(/x(\^(\d))?/) || [])[2] !== undefined ? +(t.match(/x\^(\d)/)[1]) : /x/.test(t) ? 1 : 0;
    if ((t.match(/x/g) || []).length > 1 || (t.match(/\d+(\.\d+)?/g) || []).length > (/x\^/.test(t) ? 2 : 1) || seen[d]) red2 = false; seen[d] = 1; });
  return {P: P, paren: info.paren, fois: info.fois, reduit: red2, prod: terms0 === 1 && info.paren};
};
var parseNum = M.parseNum = function(s){ s = String(s || '').replace(/[≈~]/g, '').replace(/[−–—]/g, '-').replace(/\s+/g, '').replace(/[a-zA-Zµ°²³/%€]+\.?$/, '').replace(/,/g, '.');
  return /^-?\d+(\.\d+)?$/.test(s) ? parseFloat(s) : null; };
function nDec(s){ s = String(s || '').replace(/\s+/g, '').replace(/[a-zA-Z°²%€]+$/, ''); var m = s.match(/[.,](\d+)$/); return m ? m[1].length : 0; }

/* ---------- vérification ---------- */
function checkQ(Q, raw){
  if (!String(raw || '').trim()) return {blank: true};
  var tr = Q.traps || [], i;
  if (Q.type === 'num'){
    var v = parseNum(raw); if (v === null) return {why: 'Je n’arrive pas à lire ta réponse : écris seulement un nombre, par exemple 8,6.'};
    var tol = Q.d === undefined ? 1e-9 : Math.pow(10, -Q.d);
    if (Q.d === undefined){ if (Math.abs(v - Q.v) < 1e-9) return {ok: true}; }
    else {
      if (Math.abs(v - Q.v) < 1e-9) return nDec(raw) > Q.d ? {why: 'Ta réponse a trop de chiffres après la virgule : arrondis ' + ARR[Q.d] + '.'} : {ok: true};
      if (Math.abs(v - Q.x) < tol) return {why: 'Presque : vérifie l’arrondi ' + ARR[Q.d] + '.'};
    }
    for (i = 0; i < tr.length; i++) if (Math.abs(v - tr[i][0]) < (Q.d === undefined ? 1e-9 : tol)) return {why: tr[i][1]};
    return {why: 'Ce n’est pas le bon résultat.'};
  }
  if (Q.type === 'frac'){
    var t = String(raw).replace(/[−–—]/g, '-').replace(/\s+/g, '').replace(/,/g, '.'), m = t.match(/^(-?)\(?(-?\d+)\)?\/\(?(-?\d+)\)?$/), f, val;
    if (m){ var nn = +m[2] * (m[1] ? -1 : 1), dd = +m[3]; if (!dd) return {why: 'Le dénominateur ne peut pas être 0.'}; f = [nn, dd]; val = nn / dd; }
    else { val = parseNum(t); if (val === null) return {why: 'Je n’arrive pas à lire ta réponse : écris une fraction comme 7/12, ou un entier.'}; }
    var good = Q.f[0] / Q.f[1];
    if (Math.abs(val - good) < 1e-9){
      if (!m){ if (M.isInt(val) || Q.dec) return {ok: true}; return {why: 'C’est la bonne valeur, mais donne le résultat sous forme de fraction.'}; }
      var r = red(f[0], f[1]); if (r[0] !== f[0] * (f[1] < 0 ? -1 : 1) || r[1] !== Math.abs(f[1])) return {why: 'Le résultat est juste, mais la fraction n’est pas irréductible : simplifie-la.'};
      if (f[1] < 0) return {why: 'Juste, mais écris le signe − devant la fraction (dénominateur positif).'};
      if (Q.f[1] === 1) return {why: 'Juste, mais simplifie : le résultat est un nombre entier.'};
      return {ok: true}; }
    for (i = 0; i < tr.length; i++) if (Math.abs(val - tr[i][0]) < 1e-9) return {why: tr[i][1]};
    return {why: 'Ce n’est pas le bon résultat.'};
  }
  if (Q.type === 'expr'){
    var R = parseExpr(raw);
    if (!R) return {why: 'Je n’arrive pas à lire ta réponse : écris par exemple 3x² ' + MINUS + ' 5x + 2' + (Q.mode === 'fact' ? ' ou (x + 3)(x ' + MINUS + ' 3)' : '') + '.'};
    if (!sameP(R.P, Q.P)){
      for (i = 0; i < tr.length; i++) if (sameP(R.P, tr[i][0])) return {why: tr[i][1]};
      return {why: 'Ce n’est pas le bon résultat.'}; }
    if (Q.mode === 'fact'){ if (!R.prod) return {why: 'C’est égal, mais ce n’est pas factorisé : il faut un produit.'}; return {ok: true}; }
    if (R.paren) return {why: 'Il reste des parenthèses : il faut les supprimer.'};
    if (!R.reduit) return {why: 'Le résultat est juste, mais il n’est pas réduit au maximum' + (R.fois ? ' (il reste un ×)' : '') + '.'};
    return {ok: true};
  }
  return {why: ''};
}
M.checkQ = checkQ;

/* ---------- affichage ---------- */
var P, main, tomenu, kbar;
var N = 5, LV = ['', 'Facile', 'Moyen', 'Difficile'], lastInput = null;
function best(id){ return parseInt(store(P.key + ':' + id) || '0', 10) || 0; }
function lvl(v){ var e = el('span', 'lvl l' + v); e.title = 'Difficulté : ' + LV[v];
  e.appendChild(el('span', 'st', '★★★'.slice(0, v) + '☆☆☆'.slice(0, 3 - v))); e.appendChild(document.createTextNode(' ' + LV[v])); return e; }
function menu(focus){
  main.textContent = ''; tomenu.hidden = true; kbar.hidden = true;
  P.NOTIONS.forEach(function(no){
    var sec = el('section', 'notion'); sec.id = no.n.toLowerCase();
    var h = el('h2'); h.appendChild(el('span', 'code', no.n)); h.appendChild(document.createTextNode(no.t)); sec.appendChild(h);
    sec.appendChild(el('p', 'rap', 'À retenir : ' + no.r));
    var g = el('div', 'grid');
    P.EX.filter(function(x){ return x.n === no.n; }).sort(function(a, b){ return a.lv - b.lv; }).forEach(function(x){
      var b = el('button', 'tile'); b.type = 'button';
      b.appendChild(lvl(x.lv)); b.appendChild(el('b', null, x.t)); b.appendChild(el('span', 'd', x.d));
      var r = best(x.id), nq = x.nq || N; if (r) b.appendChild(el('span', 'rec', 'Meilleur score : ' + r + ' / ' + nq + (r === nq ? ' ✓' : '')));
      b.onclick = function(){ location.hash = x.id; };
      g.appendChild(b);
    });
    sec.appendChild(g); main.appendChild(sec);
  });
  if (focus){ var t = document.getElementById(focus); if (t) t.scrollIntoView(); } else window.scrollTo(0, 0);
}
function keybar(keys){
  kbar.textContent = '';
  keys.forEach(function(k){
    var b = el('button', null, k[0]); b.type = 'button';
    b.onmousedown = function(e){ e.preventDefault(); };
    b.onclick = function(){ var f = lastInput; if (!f || f.disabled) return;
      var s = f.selectionStart != null ? f.selectionStart : f.value.length, e2 = f.selectionEnd != null ? f.selectionEnd : s;
      if (k[1] === null){ if (s === e2 && s > 0) s--; f.value = f.value.slice(0, s) + f.value.slice(e2); f.setSelectionRange(s, s); }
      else { f.value = f.value.slice(0, s) + k[1] + f.value.slice(e2); f.setSelectionRange(s + k[1].length, s + k[1].length); }
      f.focus(); };
    kbar.appendChild(b);
  });
}
function run(x){
  main.textContent = ''; tomenu.hidden = false; window.scrollTo(0, 0);
  var p = el('section', 'panel'), ph = el('div', 'ph'), no = P.NOTIONS.filter(function(z){ return z.n === x.n; })[0];
  ph.appendChild(el('p', 'kick', x.n + ' · ' + no.t)); ph.appendChild(el('h2', null, x.t)); ph.appendChild(lvl(x.lv)); p.appendChild(ph);
  p.appendChild(el('p', 'consigne', x.c)); p.appendChild(el('p', 'aide', '💡 ' + x.a));
  var NQ = x.nq || N, items = el('div', 'items'), qs = [], seen = {};
  (x.last || []).forEach(function(k){ seen[k] = 1; });          // pas les mêmes questions que la série précédente
  for (var i = 0; i < NQ; i++) qs.push(item(i));
  x.last = qs.map(function(Q){ return Q.key || Q.q; });
  function item(i){
    var Q, k = 0; do { Q = x.g(); } while (seen[Q.key || Q.q] && ++k < 80); seen[Q.key || Q.q] = 1;
    var it = el('div', 'item'), q = el('div', 'q'); q.appendChild(el('span', 'nm', (i + 1) + '.')); q.appendChild(document.createTextNode(Q.q));
    it.appendChild(q);
    if (Q.svg){ var fw = el('div', 'figw' + (Q.wide ? ' wide' : '')); fw.innerHTML = Q.svg; it.appendChild(fw); }   // SVG produit par la page elle-même
    if (Q.type === 'ch'){
      var vf = el('div', 'vf'); Q.btns = Q.ch.map(function(lab, j){ var b = el('button', null, lab); b.type = 'button'; b.setAttribute('aria-pressed', 'false');
        b.onclick = function(){ if (Q.done) return; Q.btns.forEach(function(o){ o.setAttribute('aria-pressed', String(o === b)); }); Q.choice = j; }; vf.appendChild(b); return b; });
      it.appendChild(vf);
    } else {
      var ln = el('div', 'ln'); if (Q.lab) ln.appendChild(el('span', 'eq', Q.lab));
      var f = el('input', 'w'); f.type = 'text'; f.autocomplete = 'off'; f.spellcheck = false; f.setAttribute('autocapitalize', 'off');
      f.inputMode = Q.type === 'num' ? 'decimal' : 'text'; f.placeholder = Q.type === 'num' ? 'nombre' : Q.type === 'frac' ? 'ex. 7/12' : 'ta réponse';
      f.setAttribute('aria-label', 'Réponse ' + (i + 1));
      f.onfocus = function(){ lastInput = this; };
      f.onkeydown = function(e){ if (e.key === 'Enter'){ e.preventDefault(); var all = main.querySelectorAll('input.w'), j = [].indexOf.call(all, this); if (all[j + 1]) all[j + 1].focus(); else check(); } };
      ln.appendChild(f); if (Q.unit) ln.appendChild(el('span', 'un', Q.unit)); it.appendChild(ln); Q.f = f;
    }
    Q.it = it; items.appendChild(it); return Q;
  }
  p.appendChild(items);
  var row = el('div', 'row'), bc = el('button', 'btn main', 'Vérifier'), bn = el('button', 'btn', 'Nouvelle série');
  bc.type = bn.type = 'button'; row.appendChild(bc); row.appendChild(bn); p.appendChild(row);
  var res = el('div', 'res'); res.hidden = true; p.appendChild(res);
  main.appendChild(p);
  var hasE = qs.some(function(Q){ return Q.type === 'expr'; }), hasF = qs.some(function(Q){ return Q.type === 'frac'; });
  kbar.hidden = !(hasE || hasF);
  if (hasE) keybar([['x', 'x'], ['x²', 'x²'], ['(', '('], [')', ')'], [MINUS, '-'], ['+', '+'], ['⌫', null]]);
  else if (hasF) keybar([['/', '/'], [MINUS, '-'], ['⌫', null]]);
  bn.onclick = function(){ run(x); };
  function check(){
    var score = 0;
    qs.forEach(function(Q){
      if (Q.done) { score += Q.ok ? 1 : 0; return; }
      var ok = false, why = '', blank = false;
      if (Q.type === 'ch'){
        if (Q.choice === undefined) blank = true; else ok = Q.choice === Q.ans;
        Q.btns.forEach(function(b){ b.classList.remove('okF', 'koF'); if (b.getAttribute('aria-pressed') === 'true') b.classList.add(ok ? 'okF' : 'koF'); });
      } else { var r = checkQ(Q, Q.f.value); ok = !!r.ok; blank = !!r.blank; why = r.why || ''; }
      if (blank) why = 'Tu n’as pas répondu.';
      if (Q.f){ Q.f.classList.remove('okF', 'koF'); Q.f.classList.add(ok ? 'okF' : 'koF'); }
      Q.it.classList.remove('okI', 'koI'); Q.it.classList.add(ok ? 'okI' : 'koI');
      var old = Q.it.querySelector('.corr'); if (old) old.remove();
      var c = el('div', 'corr ' + (ok ? 'ok' : 'ko')); c.appendChild(el('span', 'cv', ok ? '✓ Bravo !' : '✗ ' + (why || 'Ce n’est pas ça.')));
      // correction : tout de suite pour un choix ; sinon après 2 essais faux, ou sur demande (jamais sans réponse)
      if (!ok && !blank) Q.tries = (Q.tries || 0) + 1;
      function showSol(){ var cs = el('div', 'cs');
        if (Q.type === 'ch') cs.appendChild(el('div', null, (Q.ch.length > 2 || Q.ch[0] !== 'Vrai' ? 'Réponse : ' + Q.ch[Q.ans] + '. ' : '') + Q.steps.join(' ')));
        else cs.appendChild(el('div', 'sl', Q.steps.join('\n')));
        c.appendChild(cs); }
      if (Q.type === 'ch' ? !blank : (!ok && Q.tries >= 2)) showSol();
      else if (!ok && !blank){ var sb = el('button', 'btn', 'Voir la correction'); sb.type = 'button'; sb.style.alignSelf = 'flex-start'; sb.style.minHeight = '36px'; sb.style.padding = '6px 12px';
        sb.onclick = function(){ sb.remove(); showSol(); Q.tries = 2; }; c.appendChild(sb); c.appendChild(el('span', null, 'Essaie de corriger ta réponse, puis clique à nouveau sur « Vérifier ».')); }
      Q.it.appendChild(c);
      if (ok || (Q.type === 'ch' && !blank)) { Q.done = true; Q.ok = ok; if (Q.f) Q.f.disabled = ok; }
      score += ok ? 1 : 0;
    });
    res.hidden = false; res.className = 'res ' + (score === NQ ? 'ok' : score >= NQ / 2 ? 'mid' : 'ko');
    res.textContent = score + ' / ' + NQ + (score === NQ ? ' : parfait !' : '');
    res.appendChild(el('small', null, score === NQ ? 'Tu peux passer à l’exercice suivant ou faire une nouvelle série.' : 'Corrige les réponses en rouge puis clique à nouveau sur « Vérifier », ou lis la correction.'));
    if (score > best(x.id)) store(P.key + ':' + x.id, String(score));
    res.scrollIntoView({block: 'nearest'});
  }
  bc.onclick = check;
}
function route(){
  var h = location.hash.slice(1), x = P.EX.filter(function(e){ return e.id === h; })[0];
  if (x) run(x); else menu(/^n\d\d$/.test(h) ? h : null);
}
M.start = function(page){
  P = M.page = page; main = document.getElementById('main'); tomenu = document.getElementById('tomenu'); kbar = document.getElementById('kbar');
  tomenu.onclick = function(){ var h = location.hash.slice(1); location.hash = h.slice(0, 3); };
  window.addEventListener('hashchange', route);
  route();
};
})();
