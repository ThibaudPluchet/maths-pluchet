/* Automatismes du DNB – générateurs de questions et vérification des réponses.
   Thème disponible : « Nombres et calculs ». Chaque générateur renvoie une question :
   { html : énoncé, ans : réponse attendue (pour la correction automatique),
     corr : réponse attendue mise en forme, meth : méthode, pre/suf : texte autour de la zone de réponse }.
   Les autres thèmes (géométrie, données, fonctions, algorithmique) viendront s'ajouter dans THEMES. */
(function (root) {
'use strict';

/* ---------- hasard ---------- */
function ri(a, b) { return a + Math.floor(Math.random() * (b - a + 1)); }
function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
function chance(p) { return Math.random() < p; }
function nz(a, b) { var x; do { x = ri(a, b); } while (x === 0); return x; }
function sgn() { return chance(0.5) ? 1 : -1; }
function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }

/* ---------- nombres rationnels exacts ---------- */
function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { var t = a % b; a = b; b = t; } return a; }
function lcm(a, b) { return a / gcd(a, b) * b; }
function Q(n, d) { if (d === undefined) d = 1; if (d < 0) { n = -n; d = -d; } var g = gcd(n, d) || 1; return { n: n / g, d: d / g }; }
function qadd(a, b) { return Q(a.n * b.d + b.n * a.d, a.d * b.d); }
function qsub(a, b) { return Q(a.n * b.d - b.n * a.d, a.d * b.d); }
function qmul(a, b) { return Q(a.n * b.n, a.d * b.d); }
function qdiv(a, b) { return Q(a.n * b.d, a.d * b.n); }
function qeq(a, b) { return a.n * b.d === b.n * a.d; }
function qcmp(a, b) { var x = a.n * b.d - b.n * a.d; return x < 0 ? -1 : x > 0 ? 1 : 0; }
function D(s) { // "2,5" ou 2.5 -> rationnel exact
  s = String(typeof s === 'number' ? +s.toFixed(10) : s).replace(',', '.');
  var neg = s[0] === '-'; if (neg) s = s.slice(1);
  var p = s.split('.'), fr = p[1] || '', n = parseInt((p[0] || '') + fr, 10) || 0;
  return Q(neg ? -n : n, Math.pow(10, fr.length));
}
function isDec(q) { var d = q.d; while (d % 2 === 0) d /= 2; while (d % 5 === 0) d /= 5; return d === 1; }
function qv(q) { return q.n / q.d; }

/* ---------- mise en forme (HTML) ---------- */
var MINUS = '−', NB = ' ';
function grp(s) { return s.length > 4 ? s.replace(/\B(?=(\d{3})+(?!\d))/g, NB) : s; }
function decStr(q) {
  var neg = q.n < 0, n = Math.abs(q.n), k = 0;
  while (Math.pow(10, k) % q.d !== 0 && k < 12) k++;
  var s = String(n * (Math.pow(10, k) / q.d)), ip = s, fp = '';
  if (k > 0) { while (s.length <= k) s = '0' + s; ip = s.slice(0, -k); fp = s.slice(-k).replace(/0+$/, ''); }
  return (neg && (ip !== '0' || fp) ? MINUS : '') + grp(ip) + (fp ? ',' + fp : '');
}
function fr(n, d) { return '<span class="fr"><span>' + n + '</span><span>' + d + '</span></span>'; }
function frs(n, d) { return (n < 0 ? MINUS : '') + fr(Math.abs(n), d); }
function frq(q) { return q.d === 1 ? decStr(q) : (q.n < 0 ? MINUS : '') + fr(Math.abs(q.n), q.d); }
function nq(q) { return isDec(q) ? decStr(q) : frq(q); }
function f(x) { return typeof x === 'object' ? nq(x) : decStr(D(x)); }       // nombre
function fp(x) { var neg = typeof x === 'object' ? x.n < 0 : x < 0; return neg ? '(' + f(x) + ')' : f(x); } // entre parenthèses s'il est négatif
function V(x) { return '<i>' + x + '</i>'; }
function sup(e) { return '<sup>' + (typeof e === 'number' ? f(e) : e) + '</sup>'; }
function pw(b, e) { return b + sup(e); }
function eqs(name, s) { return '<span class="nw">' + name + ' = ' + s + '</span>'; }
function strong(s) { return '<b>' + s + '</b>'; }
var X = ' × ', P = ' + ', M = ' ' + MINUS + ' ';
// terme suivant d'une somme : « + 3 » ou « − 3 »
function plus(x) { var neg = typeof x === 'object' ? x.n < 0 : x < 0; return (neg ? M : P) + f(typeof x === 'object' ? Q(Math.abs(x.n), x.d) : Math.abs(x)); }
function deg(k) { return k === 2 ? '²' : k === 3 ? '³' : k > 1 ? sup(k) : ''; }
// polynôme {2:a,1:b,0:c} -> « 3x² − 2x + 1 » (HTML) et « 3*x^2-2*x+1 » (texte pour la vérification)
function poly(c, v) {
  v = v || 'x'; var s = '';
  Object.keys(c).map(Number).sort(function (a, b) { return b - a; }).forEach(function (k) {
    var a = c[k]; if (!a) return;
    var abs = Math.abs(a), vv = k === 0 ? '' : V(v) + deg(k), t = (k > 0 && abs === 1) ? vv : f(abs) + vv;
    s += s ? (a < 0 ? M : P) + t : (a < 0 ? MINUS : '') + t;
  });
  return s || '0';
}
function polyTxt(c, v) {
  v = v || 'x'; var s = '';
  Object.keys(c).map(Number).sort(function (a, b) { return b - a; }).forEach(function (k) {
    var a = c[k]; if (!a) return;
    s += (a < 0 ? '-' : (s ? '+' : '')) + Math.abs(a) + (k ? '*' + v + (k > 1 ? '^' + k : '') : '');
  });
  return s || '0';
}
function lin(a, b, v) { var c = {}; c[1] = a; c[0] = b; return poly(c, v); }

/* ---------- lecture des réponses ---------- */
function norm(s) {
  return String(s == null ? '' : s).replace(/[−–—‐]/g, '-').replace(/[×·∙⋅]/g, '*')
    .replace(/÷/g, '/').replace(/\s+/g, '');
}
function parseNumber(s) {
  s = norm(s).replace(/^[a-zA-Z]=/, '').replace(/,/g, '.');
  var m = /^([+-]?)(\d+\.?\d*|\.\d+)$/.exec(s);
  if (m) return { q: D((m[1] === '-' ? '-' : '') + (m[2][0] === '.' ? '0' + m[2] : m[2])), form: m[2].indexOf('.') > -1 ? 'dec' : 'int' };
  m = /^([+-]?)\(?([+-]?)(\d+)\)?\/\(?([+-]?)(\d+)\)?$/.exec(s);
  if (m && +m[5] !== 0) {
    var neg = (m[1] === '-') !== (m[2] === '-') !== (m[4] === '-');
    return { q: Q((neg ? -1 : 1) * +m[3], +m[5]), form: 'frac', irr: gcd(+m[3], +m[5]) === 1 && +m[5] !== 1 };
  }
  return null;
}
function plain(s) { return String(s == null ? '' : s).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/œ/g, 'oe').replace(/[^a-z0-9]+/g, ' ').trim(); }
function parseInteger(s) { var p = parseNumber(s); return p && p.q.d === 1 && p.form !== 'frac' ? p.q.n : null; }

/* Expressions littérales : 3x² − 2(x + 1), x(x + 5), (3x − 5)(3x + 5)… */
function tokenize(s) {
  s = norm(s).replace(/,/g, '.').replace(/pi/gi, 'π');
  var t = [], i = 0;
  while (i < s.length) {
    var c = s[i];
    if (/[0-9.]/.test(c)) {
      var j = i; while (j < s.length && /[0-9.]/.test(s[j])) j++;
      var str = s.slice(i, j); if ((str.match(/\./g) || []).length > 1 || str === '.') throw new Error('nombre');
      t.push({ k: 'n', v: D(str[0] === '.' ? '0' + str : str) }); i = j; continue;
    }
    if (/[a-zA-Z]/.test(c)) { t.push({ k: 'v', v: c.toLowerCase() }); i++; continue; }
    if (c === 'π') { t.push({ k: 'pi' }); i++; continue; }
    if (c === '²' || c === '³') { t.push({ k: 'sq', v: c === '²' ? 2 : 3 }); i++; continue; }
    if ('+-*/^()'.indexOf(c) > -1) { t.push({ k: c }); i++; continue; }
    throw new Error('caractère');
  }
  return t;
}
function parseExpr(s) {
  var t = tokenize(s), p = 0;
  function expr() {
    var terms = [{ s: 1, e: term() }];
    while (p < t.length && (t[p].k === '+' || t[p].k === '-')) { var sg = t[p++].k === '-' ? -1 : 1; terms.push({ s: sg, e: term() }); }
    return terms.length === 1 ? terms[0].e : { t: 'add', terms: terms };
  }
  function startsAtom(k) { return k && (k.k === 'n' || k.k === 'v' || k.k === '(' || k.k === 'pi'); }
  function term() {
    var fs = [unary()], ops = [];
    while (p < t.length) {
      var k = t[p];
      if (k.k === '*' || k.k === '/') { p++; ops.push(k.k); fs.push(unary()); }
      else if (startsAtom(k)) { ops.push('*'); fs.push(power()); }
      else break;
    }
    return fs.length === 1 ? fs[0] : { t: 'mul', fs: fs, ops: ops };
  }
  function unary() {
    var k = t[p];
    if (k && (k.k === '-' || k.k === '+')) { p++; var e = unary(); return k.k === '-' ? { t: 'neg', e: e } : e; }
    return power();
  }
  function power() {
    var b = atom();
    while (p < t.length) {
      var k = t[p];
      if (k.k === '^') { p++; b = { t: 'pow', b: b, e: unary() }; }
      else if (k.k === 'sq') { p++; b = { t: 'pow', b: b, e: { t: 'num', q: Q(k.v) } }; }
      else break;
    }
    return b;
  }
  function atom() {
    var k = t[p++]; if (!k) throw new Error('fin');
    if (k.k === 'n') return { t: 'num', q: k.v };
    if (k.k === 'v') return { t: 'var', v: k.v };
    if (k.k === 'pi') return { t: 'pi' };
    if (k.k === '(') { var e = expr(); if (!t[p] || t[p].k !== ')') throw new Error('parenthèse'); p++; return { t: 'par', e: e }; }
    throw new Error('symbole');
  }
  var r = expr(); if (p !== t.length) throw new Error('reste'); return r;
}
function evalE(n, env) {
  switch (n.t) {
    case 'num': return qv(n.q);
    case 'var': return env[n.v] === undefined ? NaN : env[n.v];
    case 'pi': return Math.PI;
    case 'par': return evalE(n.e, env);
    case 'neg': return -evalE(n.e, env);
    case 'pow': return Math.pow(evalE(n.b, env), evalE(n.e, env));
    case 'add': return n.terms.reduce(function (s, x) { return s + x.s * evalE(x.e, env); }, 0);
    case 'mul': var v = evalE(n.fs[0], env);
      for (var i = 1; i < n.fs.length; i++) v = n.ops[i - 1] === '/' ? v / evalE(n.fs[i], env) : v * evalE(n.fs[i], env);
      return v;
  }
  return NaN;
}
function varsOf(n, acc) {
  acc = acc || {};
  if (n.t === 'var') acc[n.v] = 1;
  ['e', 'b'].forEach(function (k) { if (n[k] && typeof n[k] === 'object' && n[k].t) varsOf(n[k], acc); });
  if (n.terms) n.terms.forEach(function (x) { varsOf(x.e, acc); });
  if (n.fs) n.fs.forEach(function (x) { varsOf(x, acc); });
  return acc;
}
function close(a, b) { return Math.abs(a - b) <= 1e-9 * Math.max(1, Math.abs(a), Math.abs(b)); }
function sameValue(a, b) {
  var vs = Object.keys(varsOf(b, varsOf(a))), pts = [0.73, -1.37, 2.91, -3.17, 1.93, 5.29], ok = 0;
  for (var i = 0; i < pts.length; i++) {
    var env = {}; vs.forEach(function (v, j) { env[v] = pts[(i + j * 2) % pts.length] + j * 0.11; });
    var x = evalE(a, env), y = evalE(b, env);
    if (!isFinite(y)) continue;
    if (!isFinite(x) || !close(x, y)) return false;
    ok++;
  }
  return ok > 0;
}
function hasPar(n) {
  if (n.t === 'par') return n.e.t !== 'num' && !(n.e.t === 'neg' && n.e.e.t === 'num');
  if (n.e && n.e.t && hasPar(n.e)) return true;
  if (n.b && hasPar(n.b)) return true;
  if (n.terms) return n.terms.some(function (x) { return hasPar(x.e); });
  if (n.fs) return n.fs.some(hasPar);
  return false;
}
function mono(n) { // monôme : {deg, nums, vars} ou null
  switch (n.t) {
    case 'num': return { deg: 0, nums: 1, vars: 0 };
    case 'pi': return { deg: 0, nums: 0, vars: 0 };
    case 'var': return { deg: 1, nums: 0, vars: 1 };
    case 'neg': return mono(n.e);
    case 'par': return n.e.t === 'num' || (n.e.t === 'neg' && n.e.e.t === 'num') ? { deg: 0, nums: 1, vars: 0 } : null;
    case 'pow':
      if (n.e.t !== 'num' || n.e.q.d !== 1) return null;
      if (n.b.t === 'var') return { deg: n.e.q.n, nums: 0, vars: 1 };
      if (n.b.t === 'num') return { deg: 0, nums: 1, vars: 0 };
      return null;
    case 'mul':
      var r = { deg: 0, nums: 0, vars: 0 };
      for (var i = 0; i < n.fs.length; i++) {
        var m = mono(n.fs[i]); if (!m) return null;
        if (i > 0 && n.ops[i - 1] === '/') { if (m.vars) return null; }
        else r.deg += m.deg;
        r.nums += m.nums; r.vars += m.vars;
      }
      return r;
  }
  return null;
}
function isReduced(n) {
  var terms = n.t === 'add' ? n.terms.map(function (x) { return x.e; }) : [n], seen = {};
  for (var i = 0; i < terms.length; i++) {
    var m = mono(terms[i]);
    if (!m || m.nums > 1 || m.vars > 1 || seen[m.deg]) return false;
    seen[m.deg] = 1;
  }
  return true;
}
function isFactored(n) {
  while (n.t === 'neg' || (n.t === 'par' && n.e.t === 'mul')) n = n.e;
  if (n.t === 'pow') return n.b.t === 'par' && n.b.e.t === 'add';
  if (n.t !== 'mul' || n.ops.indexOf('/') > -1) return false;
  var hasSum = false;
  for (var i = 0; i < n.fs.length; i++) {
    var x = n.fs[i];
    if (x.t === 'num' && x.q.d === 1 && Math.abs(x.q.n) === 1) return false;
    if ((x.t === 'par' && x.e.t === 'add') || (x.t === 'pow' && x.b.t === 'par' && x.b.e.t === 'add')) hasSum = true;
  }
  return hasSum;
}

/* ---------- correction automatique ----------
   ans.k : num (nombre), sym (<, > ou =), sci (notation scientifique), pow (puissance de 10), expr (expression), fn (réponse ouverte)
   Renvoie {ok} ou {ok:false, msg} ; {invalid:true, msg} si la réponse est illisible (l'élève peut la corriger). */
function check(ans, raw) {
  var s, p;
  switch (ans.k) {
    case 'num':
      var pct = /%/.test(String(raw));
      s = String(raw == null ? '' : raw).replace(/%|[kcdm]?m[²³]|[kcdm]?m\b|[mcd]?L\b|kg|g\b|€|°|min|h\b|s\b/g, '').trim();
      if (!s) return { invalid: true, msg: 'Écris ta réponse.' };
      if (/^[^/]*\/\s*$|^\s*\//.test(s)) return { invalid: true, msg: 'Complète le numérateur et le dénominateur de ta fraction.' };
      p = parseNumber(s);
      if (!p) return { invalid: true, msg: 'Je n’arrive pas à lire ce nombre. Exemples d’écriture : 2,5 · −3 · 3/4' };
      if (pct && ans.pct) p.q = qdiv(p.q, Q(100));
      if (!qeq(p.q, ans.q)) return { ok: false };
      if (ans.form === 'dec' && p.form === 'frac') return { ok: false, msg: 'La valeur est juste, mais on attendait l’écriture décimale.' };
      if (ans.form === 'frac' && p.form === 'dec') return { ok: false, msg: 'La valeur est juste, mais on demandait une fraction.' };
      if (ans.irr && p.form === 'frac' && !p.irr) return { ok: false, msg: 'La valeur est juste, mais la fraction n’est pas irréductible : simplifie-la.' };
      return { ok: true };
    case 'sym':
      if (!raw) return { invalid: true, msg: 'Choisis un symbole.' };
      return { ok: raw === ans.v };
    case 'pow':
      s = norm(raw).replace(/^10\^/, '');
      if (!s) return { invalid: true, msg: 'Écris l’exposant.' };
      p = parseInteger(s);
      if (p === null) return { invalid: true, msg: 'L’exposant doit être un nombre entier (par exemple 3 ou −2).' };
      return { ok: p === ans.e };
    case 'sci':
      raw = raw || ['', ''];
      if (!String(raw[0]).trim() || !String(raw[1]).trim()) return { invalid: true, msg: 'Complète les deux cases.' };
      var m = parseNumber(raw[0]), e = parseInteger(raw[1]);
      if (!m || m.form === 'frac' || e === null) return { invalid: true, msg: 'Écris un nombre décimal dans la première case et un entier dans la seconde.' };
      var a = Math.abs(qv(m.q)), same = qeq(qmul(m.q, Q(Math.pow(10, Math.max(e, 0)), Math.pow(10, Math.max(-e, 0)))),
        qmul(ans.m, Q(Math.pow(10, Math.max(ans.e, 0)), Math.pow(10, Math.max(-ans.e, 0)))));
      if (!same) return { ok: false };
      if (a < 1 || a >= 10) return { ok: false, msg: 'L’égalité est juste, mais ce n’est pas l’écriture scientifique : le nombre devant la puissance doit être compris entre 1 et 10 (10 exclu).' };
      return { ok: true };
    case 'expr':
      s = String(raw == null ? '' : raw).trim().replace(/^[A-Z]\s*=\s*/, '');
      if (ans.pi) s = s.replace(/\s*(mm|cm|dm|km|m)[²³]?\s*$/, '');
      if (!s) return { invalid: true, msg: 'Écris ta réponse.' };
      var ast, ref;
      try { ast = parseExpr(s); } catch (err) { return { invalid: true, msg: 'Je n’arrive pas à lire cette expression. Exemples : 3x + 2 · x² − 4 · 2(x + 1)' }; }
      ref = parseExpr(ans.ref);
      var vs = Object.keys(varsOf(ast));
      if (vs.some(function (v) { return v !== ans.v; })) return { ok: false, msg: ans.v ? 'Utilise la lettre ' + ans.v + '.' : 'Ta réponse ne doit pas contenir de lettre' + (ans.pi ? ' (à part π).' : '.') };
      if (!sameValue(ast, ref)) {
        if (ans.pi && !vs.length) { var sv = evalE(ast, {}), rv = evalE(ref, {}); if (isFinite(sv) && Math.abs(sv - rv) <= 0.02 * Math.abs(rv)) return { ok: false, msg: 'C’est une valeur approchée : on demande la valeur exacte, écrite avec π.' }; }
        return { ok: false };
      }
      if (ans.form === 'red' && hasPar(ast)) return { ok: false, msg: 'L’expression est bien égale, mais elle n’est pas développée : il reste des parenthèses.' };
      if (ans.form === 'red' && !isReduced(ast)) return { ok: false, msg: 'L’expression est bien égale, mais elle n’est pas réduite.' };
      if (ans.form === 'fact' && !isFactored(ast)) return { ok: false, msg: 'L’expression est bien égale, mais elle n’est pas factorisée : on attend un produit.' };
      return { ok: true };
    case 'pair':
      raw = raw || ['', ''];
      if (!String(raw[0]).trim() || !String(raw[1]).trim()) return { invalid: true, msg: 'Complète l’abscisse et l’ordonnée.' };
      var px = parseNumber(raw[0]), py = parseNumber(raw[1]);
      if (!px || !py) return { invalid: true, msg: 'Écris un nombre dans chaque case.' };
      if (qeq(px.q, ans.x) && qeq(py.q, ans.y)) return { ok: true };
      if (qeq(px.q, ans.y) && qeq(py.q, ans.x)) return { ok: false, msg: 'Tu as inversé l’abscisse et l’ordonnée : on écrit d’abord l’abscisse (axe horizontal).' };
      return { ok: false };
    case 'txt':
      s = plain(raw); if (!s) return { invalid: true, msg: 'Écris ta réponse.' };
      return { ok: ans.v.some(function (v) { return plain(v) === s.replace(/^(le |la |point |figure |triangle )+/, ''); }) };
    case 'words':
      s = ' ' + plain(raw); if (s === ' ') return { invalid: true, msg: 'Écris ta réponse.' };
      var hasW = function (w) { return s.indexOf(' ' + w) > -1; };
      if ((ans.forbid || []).some(hasW)) return { ok: false };
      if (ans.need.every(function (g) { return g.some(hasW); })) return { ok: true };
      var nr = (ans.near || []).filter(function (n) { return hasW(n.has); })[0];
      return nr ? { ok: false, msg: nr.msg } : { ok: false };
    case 'ratio':
      s = norm(raw).toUpperCase().replace(/[:÷]/g, '/');
      var mr = /^\(?([A-Z]{2})\)?\/\(?([A-Z]{2})\)?$/.exec(s);
      if (!mr) return { invalid: true, msg: 'Écris un quotient de deux longueurs, par exemple AB/BC.' };
      var sg = function (a, b) { return a.split('').sort().join('') === b.split('').sort().join(''); };
      if (sg(mr[1], ans.n) && sg(mr[2], ans.d)) return { ok: true };
      if (sg(mr[1], ans.d) && sg(mr[2], ans.n)) return { ok: false, msg: 'C’est l’inverse : le cosinus est inférieur à 1, l’hypoténuse va au dénominateur.' };
      return { ok: false };
    case 'pyeq':
      s = norm(raw).toUpperCase().replace(/\^2/g, '²').replace(/\*/g, '');
      var sides = s.split('=');
      var terms = function (x) { var t = x.split('+'); return t.every(function (y) { return /^[A-Z]{2}²$/.test(y); }) ? t.map(function (y) { return y.slice(0, 2).split('').sort().join(''); }) : null; };
      if (sides.length !== 2 || !terms(sides[0]) || !terms(sides[1])) return { invalid: true, msg: 'Écris une égalité de la forme BC² = AB² + AC².' };
      var L1 = terms(sides[0]), L2 = terms(sides[1]), one = L1.length === 1 ? L1 : L2, two = L1.length === 1 ? L2 : L1;
      if (one.length !== 1 || two.length !== 2) return { ok: false, msg: 'Il faut un carré d’un côté de l’égalité et une somme de deux carrés de l’autre.' };
      var hy = ans.h.split('').sort().join(''), legs = ans.l.map(function (x) { return x.split('').sort().join(''); }).sort();
      if (one[0] === hy && two.slice().sort().join() === legs.join()) return { ok: true };
      if (two.indexOf(hy) > -1) return { ok: false, msg: 'Le carré de l’hypoténuse ' + ans.h + ' (le côté opposé à l’angle droit) doit être seul de son côté.' };
      return { ok: false };
    case 'fn':
      s = String(raw == null ? '' : raw).trim();
      if (!s) return { invalid: true, msg: 'Écris ta réponse.' };
      return ans.f(s);
  }
  return { ok: false };
}

/* ---------- générateurs « Nombres et calculs » ----------
   req : notions qui doivent avoir été vues en classe (étiquettes déduites des titres des notions, voir TAGS).
   gen(c) : c.lv = '4e' ou '3e', c.has(étiquette) indique si une notion a été vue. */
function methDec(n, d) {
  var q = Q(n, d);
  if (d === 1) return fr(n, 1) + ' = ' + n + ' : diviser par 1 ne change rien.';
  if (n % d === 0) return fr(n, d) + ' = ' + n + ' ÷ ' + d + ' = ' + decStr(q) + '.';
  if (d === 10 || d === 100 || d === 1000) return fr(n, d) + ' = ' + n + ' ÷ ' + d + ' = ' + decStr(q) + '.';
  var t = [10, 100, 1000].filter(function (x) { return x % d === 0; })[0];
  if (t) { var k = t / d; return fr(n, d) + ' = ' + fr(n + X + k, d + X + k) + ' = ' + fr(n * k, t) + ' = ' + decStr(q) + '.'; }
  return fr(n, d) + ' = ' + n + ' ÷ ' + d + ' = ' + decStr(q) + '.';
}
function digitsSum(n) { return String(Math.abs(n)).split('').reduce(function (s, c) { return s + (+c); }, 0); }

var NC = [
{
  id: 'frac-dec', titre: 'Écriture décimale d’une fraction simple', ex: fr(3, 4) + ' = 0,75', req: [],
  gen: function () {
    var pool = [[1,2],[1,4],[3,4],[3,2],[4,2],[5,2],[1,10],[100,100],[7,1],[1,5],[2,5],[3,5],[4,5],[7,10],[3,10],[9,10],[1,100],[7,100],[9,4],[5,4],[7,4],[7,2],[1,20],[3,20],[6,5],[12,10],[25,100],[150,100],[1,8],[11,2],[15,10]];
    var p = pick(pool), n = p[0], d = p[1], q = Q(n, d);
    if (chance(0.3) && [2, 4, 5, 10, 20].indexOf(d) > -1 && n % d) {
      return { html: 'Compléter : ' + decStr(q) + ' = ' + fr('…', d), ans: { k: 'num', q: Q(n), form: 'int' }, pre: '… =',
        corr: decStr(q) + ' = ' + fr(strong(n), d),
        meth: methDec(n, d) + ' Donc … = ' + n + '.' };
    }
    return { html: 'Donner l’écriture décimale de ' + fr(n, d) + '.', ans: { k: 'num', q: q, form: 'dec' },
      corr: fr(n, d) + ' = ' + strong(decStr(q)), meth: methDec(n, d) };
  }
},
{
  id: 'frac-part', titre: 'Fraction ou pourcentage d’un nombre', ex: 'le tiers de 18 · 25 % de 64', req: [],
  gen: function (c) {
    var v = pick(['tiers', 'quart', 'moitie', 'frac', 'pct', 'pct', 'pct']), n, r, html, meth;
    if (v === 'tiers') { n = 3 * ri(3, c.lv === '3e' ? 33 : 15); r = n / 3; html = 'Calculer le tiers de ' + f(n) + '.'; meth = 'Le tiers, c’est diviser par 3 : ' + f(n) + ' ÷ 3 = ' + f(r) + '.'; }
    else if (v === 'quart') { n = 4 * ri(2, c.lv === '3e' ? 25 : 12); r = n / 4; html = 'Calculer le quart de ' + f(n) + '.'; meth = 'Le quart, c’est diviser par 4 : ' + f(n) + ' ÷ 4 = ' + f(r) + '.'; }
    else if (v === 'moitie') { n = ri(13, 99); r = n / 2; html = 'Calculer la moitié de ' + f(n) + '.'; meth = 'La moitié, c’est diviser par 2 : ' + f(n) + ' ÷ 2 = ' + f(r) + '.'; }
    else if (v === 'frac') {
      var fq = pick([[2, 3], [3, 4], [2, 5], [3, 5], [4, 5], [3, 10], [5, 6]]), u = ri(2, 12);
      n = fq[1] * u; r = u * fq[0];
      html = 'Calculer les ' + fr(fq[0], fq[1]) + ' de ' + f(n) + '.';
      meth = 'On divise par ' + fq[1] + ' puis on multiplie par ' + fq[0] + ' : ' + f(n) + ' ÷ ' + fq[1] + ' = ' + u + ', puis ' + u + X + fq[0] + ' = ' + f(r) + '.';
    } else {
      var a = pick(c.lv === '3e' ? [100, 50, 25, 10, 1, 75, 20] : [100, 50, 25, 10, 1]);
      n = a === 100 ? ri(12, 250) : a === 50 ? ri(11, 99) * (chance(0.6) ? 2 : 1) : a === 25 || a === 75 ? 4 * ri(3, 30) : a === 20 ? 5 * ri(3, 30) : a === 10 ? ri(11, 400) : 50 * ri(2, 18);
      r = n * a / 100;
      html = 'Calculer ' + a + ' % de ' + f(n) + '.';
      meth = {
        100: '100 %, c’est la totalité : 100 % de ' + f(n) + ' = ' + f(r) + '.',
        50: '50 %, c’est la moitié : ' + f(n) + ' ÷ 2 = ' + f(r) + '.',
        25: '25 %, c’est le quart : ' + f(n) + ' ÷ 4 = ' + f(r) + '.',
        75: '75 %, ce sont les trois quarts : ' + f(n) + ' ÷ 4 = ' + f(n / 4) + ', puis ' + f(n / 4) + X + '3 = ' + f(r) + '.',
        20: '20 %, c’est un cinquième : ' + f(n) + ' ÷ 5 = ' + f(r) + '.',
        10: '10 %, c’est un dixième : ' + f(n) + ' ÷ 10 = ' + f(r) + '.',
        1: '1 %, c’est un centième : ' + f(n) + ' ÷ 100 = ' + f(r) + '.'
      }[a];
    }
    return { html: html, ans: { k: 'num', q: D(r), form: 'any' }, corr: strong(f(r)), meth: meth };
  }
},
{
  id: 'formes', titre: 'Un même nombre sous plusieurs formes', ex: '1,2 = ' + fr(6, 5) + ' = 120 %', req: [],
  gen: function () {
    var v = pick(['d2p', 'p2d', 'f2p', 'd2f', 'un']), x, q, html, meth, ans, corr, suf, pre;
    if (v === 'd2p') {
      x = D(pick(['0,5', '0,25', '0,75', '0,1', '0,05', '1,2', '1,5', '0,35', '0,08', '2', '0,6', '1,25', '0,02', '0,9', '2,5']));
      q = qmul(x, Q(100)); html = 'Écrire ' + f(x) + ' sous la forme d’un pourcentage.'; suf = '%';
      ans = { k: 'num', q: q, form: 'any' }; corr = f(x) + ' = ' + strong(f(q) + ' %');
      meth = f(x) + ' = ' + fr(f(q), 100) + ' = ' + f(q) + ' % (on multiplie par 100).';
    } else if (v === 'p2d') {
      var pc = pick([50, 25, 75, 10, 5, 120, 150, 35, 8, 1, 200, 60, 12, 3, 45]);
      q = Q(pc, 100); html = 'Écrire ' + pc + ' % sous forme décimale.';
      ans = { k: 'num', q: q, form: 'dec' }; corr = pc + ' % = ' + strong(decStr(q));
      meth = pc + ' % = ' + fr(pc, 100) + ' = ' + pc + ' ÷ 100 = ' + decStr(q) + '.';
    } else if (v === 'f2p') {
      var pr = pick([[1,2],[1,4],[3,4],[1,5],[2,5],[3,5],[4,5],[1,10],[3,10],[7,10],[1,20],[7,20],[9,20],[6,5],[3,2],[1,25],[3,25]]);
      var k = 100 / pr[1]; q = Q(pr[0] * k);
      html = 'Écrire ' + fr(pr[0], pr[1]) + ' sous la forme d’un pourcentage.'; suf = '%';
      ans = { k: 'num', q: q, form: 'any' }; corr = fr(pr[0], pr[1]) + ' = ' + strong(f(q) + ' %');
      meth = fr(pr[0], pr[1]) + ' = ' + fr(pr[0] + X + k, pr[1] + X + k) + ' = ' + fr(f(q), 100) + ' = ' + f(q) + ' %.';
    } else if (v === 'd2f') {
      var ds = pick(['0,5', '0,25', '0,75', '0,2', '0,4', '0,6', '0,8', '1,2', '1,5', '0,125', '2,5', '0,05', '1,25', '0,35', '1,4']);
      x = D(ds); var dd = Math.pow(10, ds.split(',')[1].length), nn = Math.round(qv(x) * dd);
      html = 'Écrire ' + f(x) + ' sous la forme d’une fraction irréductible.';
      ans = { k: 'num', q: x, form: 'frac', irr: true }; corr = f(x) + ' = ' + strong(frq(x));
      meth = f(x) + ' = ' + fr(nn, dd) + ' = ' + frq(x) + ' (on simplifie par ' + (dd / x.d) + ').';
    } else {
      var d = pick([2, 4, 5, 10]), n = ri(1, d - 1); while (gcd(n, d) !== 1) n = ri(1, d - 1);
      var ip = ri(1, 3); x = qadd(Q(ip), Q(n, d));
      html = 'Compléter : ' + f(x) + ' = ' + ip + ' + ' + fr('…', d); pre = '… =';
      ans = { k: 'num', q: Q(n), form: 'int' }; corr = f(x) + ' = ' + ip + ' + ' + fr(strong(n), d);
      meth = f(x) + ' = ' + ip + ' + ' + f(Q(n, d)) + ' et ' + f(Q(n, d)) + ' = ' + fr(n, d) + ' (car ' + methDec(n, d).replace(/\.$/, '') + ').';
    }
    return { html: html, ans: ans, corr: corr, meth: meth, suf: suf, pre: pre };
  }
},
{
  id: 'dec-cmp', titre: 'Comparer des nombres décimaux', ex: MINUS + '2,5 < ' + MINUS + '2,35', req: [],
  gen: function () {
    var v = pick(['same', 'same', 'neg', 'neg', 'opp', 'eq']), I = ri(0, 15), a, b, sa, sb, meth;
    var t = ri(1, 9), u; do { u = ri(11, 99); } while (u % 10 === 0 || Math.floor(u / 10) === t);
    sa = I + ',' + t; sb = I + ',' + (u < 10 ? '0' : '') + u;
    if (v === 'same') {
      meth = 'Même partie entière (' + I + ') : on compare les dixièmes, ' + t + ' et ' + Math.floor(u / 10) + '. Attention, ' + sb.split(',')[1] + ' centièmes n’est pas plus grand que ' + t + ' dixièmes juste parce qu’il a plus de chiffres.';
    } else if (v === 'neg') {
      meth = 'Pour deux nombres négatifs, le plus petit est celui qui est le plus loin de zéro. On compare d’abord ' + sa + ' et ' + sb + ', puis on inverse.';
      sa = '-' + sa; sb = '-' + sb;
    } else if (v === 'opp') {
      sa = '-' + I + ',' + t; sb = '0,' + (chance(0.5) ? t : '0' + t);
      if (I === 0 && chance(0.5)) sb = String(ri(0, 3)) + ',' + ri(1, 9);
      meth = 'Un nombre négatif est toujours plus petit qu’un nombre positif.';
    } else {
      sa = I + ',' + t; sb = I + ',' + t + '0';
      meth = 'Ajouter un zéro à la fin de la partie décimale ne change pas le nombre : ' + sb.replace('.', ',') + ' = ' + sa + '.';
    }
    if (chance(0.5)) { var tmp = sa; sa = sb; sb = tmp; }
    a = D(sa); b = D(sb);
    var r = qcmp(a, b), sym = r < 0 ? '<' : r > 0 ? '>' : '=';
    var show = function (s) { return s.replace('-', MINUS); };
    return { html: 'Compléter avec &lt;, &gt; ou = : &nbsp;' + show(sa) + ' … ' + show(sb), ans: { k: 'sym', v: sym },
      corr: show(sa) + ' ' + strong(sym === '<' ? '&lt;' : sym === '>' ? '&gt;' : '=') + ' ' + show(sb), meth: meth };
  }
},
{
  id: 'dec-calc', titre: 'Calculer avec des décimaux, y compris négatifs', ex: '2,5 ' + MINUS + ' 5,5 + 3 × 4', req: [],
  gen: function (c) {
    var vs = ['prio', 'add', 'sub'];
    if (c.has('relx')) vs.push('mul', 'mul', 'prio2');
    var v = pick(vs), a, b, cc, d, r, html, meth;
    function dec1() { return D(ri(11, 99) / 10); }
    if (v === 'prio') {
      a = dec1(); b = dec1(); cc = ri(2, 9); d = ri(2, 9); var p = cc * d, s1 = qsub(a, b); r = qadd(s1, Q(p));
      html = 'Calculer : ' + eqs('A', f(a) + M + f(b) + P + cc + X + d);
      meth = 'La multiplication est prioritaire : ' + cc + X + d + ' = ' + p + '. Puis de gauche à droite : ' + f(a) + M + f(b) + ' = ' + f(s1) + ', et ' + f(s1) + P + p + ' = ' + f(r) + '.';
    } else if (v === 'add') {
      a = qmul(dec1(), Q(sgn())); b = qmul(dec1(), Q(a.n > 0 ? -1 : sgn())); r = qadd(a, b);
      html = 'Calculer : ' + eqs('A', f(a) + P + fp(b));
      meth = (a.n < 0) === (b.n < 0) ? 'Les deux nombres ont le même signe : on additionne leurs distances à zéro et on garde le signe.'
        : 'Les deux nombres sont de signes contraires : on soustrait les distances à zéro et on prend le signe de celui qui est le plus loin de zéro.';
      meth += ' ' + f(a) + P + fp(b) + ' = ' + f(r) + '.';
    } else if (v === 'sub') {
      a = dec1(); do { b = D(ri(Math.round(qv(a) * 10) + 5, 129) / 10); } while (qeq(a, b));
      r = qsub(a, b);
      html = 'Calculer : ' + eqs('A', f(a) + M + f(b));
      meth = 'Soustraire, c’est ajouter l’opposé : ' + f(a) + M + f(b) + ' = ' + f(a) + P + '(' + f(qmul(b, Q(-1))) + ') = ' + f(r) + '.';
    } else if (v === 'mul') {
      a = qmul(D(pick([0.5, 1.5, 2.5, 0.2, 0.3, 1.2, 0.4, 0.25])), Q(sgn())); b = Q(nz(2, 9) * (a.n > 0 ? -1 : sgn()));
      if (chance(0.5)) { var tt = a; a = b; b = tt; }
      r = qmul(a, b);
      html = 'Calculer : ' + eqs('A', fp(a) + X + fp(b));
      meth = 'Signe : ' + ((a.n < 0) !== (b.n < 0) ? 'un seul facteur négatif, le produit est négatif.' : 'deux facteurs négatifs, le produit est positif.') + ' Puis ' + f(Q(Math.abs(a.n), a.d)) + X + f(Q(Math.abs(b.n), b.d)) + ' = ' + f(Q(Math.abs(r.n), r.d)) + '.';
    } else {
      a = Q(ri(1, 9)); b = Q(ri(2, 6)); cc = qmul(D(pick([0.5, 1.5, 2.5, 0.2, 1.2])), Q(-1)); var pr = qmul(b, cc); r = qsub(a, pr);
      html = 'Calculer : ' + eqs('A', f(a) + M + f(b) + X + fp(cc));
      meth = 'La multiplication est prioritaire : ' + f(b) + X + fp(cc) + ' = ' + f(pr) + '. Puis ' + f(a) + M + fp(pr) + ' = ' + f(a) + P + f(qmul(pr, Q(-1))) + ' = ' + f(r) + '.';
    }
    return { html: html, ans: { k: 'num', q: r, form: 'any' }, corr: 'A = ' + strong(f(r)), meth: meth };
  }
},
{
  id: 'frac-simp', titre: 'Simplifier une fraction', ex: fr(18, 24) + ' = ' + fr(3, 4), req: [],
  gen: function (c) {
    var p, q; do { q = ri(2, 12); p = ri(1, 2 * q); } while (gcd(p, q) !== 1);
    var k = ri(2, c.lv === '3e' ? 15 : 9), n = p * k, d = q * k;
    return { html: 'Écrire ' + fr(n, d) + ' sous la forme d’une fraction irréductible.', ans: { k: 'num', q: Q(p, q), form: 'frac', irr: true },
      corr: fr(n, d) + ' = ' + strong(fr(p, q)),
      meth: n + ' = ' + k + X + p + ' et ' + d + ' = ' + k + X + q + ', donc ' + fr(n, d) + ' = ' + fr(k + X + p, k + X + q) + ' = ' + fr(p, q) + '.' };
  }
},
{
  id: 'frac-cmp', titre: 'Comparer des fractions et des décimaux', ex: fr(3, 4) + ' > ' + fr(5, 8), req: [],
  gen: function (c) {
    var v = pick(c.lv === '3e' ? ['same', 'one', 'list', 'list'] : ['same', 'same', 'one', 'list']);
    if (v === 'list') {
      var a = ri(1, 2), vals = [], items = [], tries = 0;
      var addItem = function (q, html) { if (vals.some(function (x) { return qeq(x, q); }) || tries++ > 50) return false; vals.push(q); items.push({ q: q, html: html }); return true; };
      while (items.length < 1) { var q1 = D(a + ri(1, 9) / 10); addItem(q1, f(q1)); }
      while (items.length < 2) { var q2 = D(a + ri(11, 99) / 100); if (q2.d === 100) addItem(q2, f(q2)); }
      while (items.length < 3) { var k = ri(1, 9); addItem(Q(a * 100 + k, 100), a + ' + ' + fr(k, 100)); }
      while (items.length < 4) { var dd = pick([2, 4, 5]), nn = ri(a * dd + 1, a * dd + dd - 1); if (gcd(nn, dd) === 1) addItem(Q(nn, dd), fr(nn, dd)); }
      items = shuffle(items);
      var big = chance(0.5), best = items.reduce(function (m, x) { return (qcmp(x.q, m.q) > 0) === big ? x : m; });
      return { html: 'Parmi les nombres suivants, quel est le plus ' + (big ? 'grand' : 'petit') + ' ?<span class="nlist">' + items.map(function (x) { return '<span>' + x.html + '</span>'; }).join('') + '</span>',
        ans: { k: 'num', q: best.q, form: 'any' }, corr: 'Le plus ' + (big ? 'grand' : 'petit') + ' est ' + strong(best.html) + '.',
        meth: 'On écrit tous les nombres sous forme décimale : ' + items.map(function (x) { return x.html + ' = ' + decStr(x.q); }).join(' ; ') + '.' };
    }
    if (v === 'one') {
      var d = ri(3, 12), n = d + nz(-d + 1, d - 1);
      var sym = n < d ? '<' : '>';
      return { html: 'Compléter avec &lt;, &gt; ou = : &nbsp;' + fr(n, d) + ' … 1', ans: { k: 'sym', v: sym },
        corr: fr(n, d) + ' ' + strong(sym === '<' ? '&lt;' : '&gt;') + ' 1',
        meth: '1 = ' + fr(d, d) + '. Le numérateur ' + n + ' est ' + (n < d ? 'plus petit' : 'plus grand') + ' que le dénominateur ' + d + ', donc la fraction est ' + (n < d ? 'inférieure' : 'supérieure') + ' à 1.' };
    }
    var b = ri(2, 6), m = ri(2, 4), d2 = b * m, a1 = ri(1, 2 * b), c1;
    do { c1 = ri(1, 2 * d2); } while (c1 === a1 * m && chance(0.8));
    var r = qcmp(Q(a1, b), Q(c1, d2)), s = r < 0 ? '<' : r > 0 ? '>' : '=', sh = s === '<' ? '&lt;' : s === '>' ? '&gt;' : '=';
    var swap = chance(0.5), L = swap ? fr(c1, d2) : fr(a1, b), R = swap ? fr(a1, b) : fr(c1, d2);
    if (swap) { s = r < 0 ? '>' : r > 0 ? '<' : '='; sh = s === '<' ? '&lt;' : s === '>' ? '&gt;' : '='; }
    return { html: 'Compléter avec &lt;, &gt; ou = : &nbsp;' + L + ' … ' + R, ans: { k: 'sym', v: s },
      corr: L + ' ' + strong(sh) + ' ' + R,
      meth: 'On met au même dénominateur : ' + fr(a1, b) + ' = ' + fr(a1 + X + m, b + X + m) + ' = ' + fr(a1 * m, d2) + '. On compare ' + (a1 * m) + ' et ' + c1 + '.' };
  }
},
{
  id: 'frac-calc', titre: 'Calculer avec des fractions', ex: fr(3, 5) + M + fr(1, 4) + ' = ' + fr(7, 20), req: ['frac'],
  gen: function (c) {
    var v = pick(c.lv === '3e' ? ['add', 'add', 'sub', 'mul', 'div', 'int'] : ['add1', 'sub1', 'mul', 'mul']), a, b, cc, d, r, html, meth;
    if (v === 'add1' || v === 'sub1') {
      b = ri(2, 6); var m = ri(2, 4); d = b * m; do { a = ri(1, b * 2); } while (gcd(a, b) !== 1); do { cc = ri(1, d); } while (cc === d);
      var plusOp = v === 'add1'; r = plusOp ? qadd(Q(a, b), Q(cc, d)) : qsub(Q(a, b), Q(cc, d));
      if (chance(0.5) && plusOp) { html = fr(cc, d) + P + fr(a, b); } else html = fr(a, b) + (plusOp ? P : M) + fr(cc, d);
      meth = 'Même dénominateur : ' + fr(a, b) + ' = ' + fr(a * m, d) + '. Donc A = ' + (plusOp ? '' : '') + fr(a * m + (plusOp ? ' + ' : ' ' + MINUS + ' ') + cc, d) + ' = ' + frs(a * m + (plusOp ? cc : -cc), d) + (Q(a * m + (plusOp ? cc : -cc), d).d !== d ? ' = ' + frq(r) : '') + '.';
    } else if (v === 'add' || v === 'sub') {
      do { b = ri(2, 9); d = ri(2, 9); } while (b === d || gcd(b, d) === Math.min(b, d));
      do { a = ri(1, b + 3); } while (gcd(a, b) !== 1 || a === b); do { cc = ri(1, d + 3); } while (gcd(cc, d) !== 1 || cc === d);
      var L = lcm(b, d), plus2 = v === 'add'; r = plus2 ? qadd(Q(a, b), Q(cc, d)) : qsub(Q(a, b), Q(cc, d));
      html = fr(a, b) + (plus2 ? P : M) + fr(cc, d);
      meth = 'Dénominateur commun ' + L + ' : ' + fr(a, b) + ' = ' + fr(a * L / b, L) + ' et ' + fr(cc, d) + ' = ' + fr(cc * L / d, L) + '. Donc A = ' + fr(a * L / b + (plus2 ? ' + ' : ' ' + MINUS + ' ') + cc * L / d, L) + ' = ' + frs(a * L / b + (plus2 ? 1 : -1) * cc * L / d, L) + (r.d !== L ? ' = ' + frq(r) : '') + '.';
    } else if (v === 'mul') {
      do { a = ri(1, 9); b = ri(2, 9); cc = ri(1, 9); d = ri(2, 9); } while (gcd(a, b) !== 1 || gcd(cc, d) !== 1); r = qmul(Q(a, b), Q(cc, d));
      html = fr(a, b) + X + fr(cc, d);
      meth = 'On multiplie les numérateurs entre eux et les dénominateurs entre eux : A = ' + fr(a + X + cc, b + X + d) + ' = ' + fr(a * cc, b * d) + (r.d !== b * d || r.n !== a * cc ? ' = ' + frq(r) : '') + '.';
    } else if (v === 'div') {
      do { a = ri(1, 9); b = ri(2, 9); cc = ri(1, 9); d = ri(2, 9); } while (gcd(a, b) !== 1 || gcd(cc, d) !== 1); r = qdiv(Q(a, b), Q(cc, d));
      html = fr(a, b) + ' ÷ ' + fr(cc, d);
      meth = 'Diviser par ' + fr(cc, d) + ', c’est multiplier par son inverse ' + fr(d, cc) + ' : A = ' + fr(a, b) + X + fr(d, cc) + ' = ' + fr(a * d, b * cc) + (r.d !== b * cc || r.n !== a * d ? ' = ' + frq(r) : '') + '.';
    } else {
      var n0 = ri(1, 4); b = ri(2, 9); a = ri(1, 2 * b); while (gcd(a, b) !== 1) a = ri(1, 2 * b);
      r = qsub(Q(n0), Q(a, b));
      html = n0 + M + fr(a, b);
      meth = n0 + ' = ' + fr(n0 * b, b) + ', donc A = ' + fr(n0 * b + ' ' + MINUS + ' ' + a, b) + ' = ' + frq(r) + '.';
    }
    return { html: 'Calculer ' + eqs('A', html) + '. Donner le résultat sous la forme d’une fraction irréductible.',
      ans: { k: 'num', q: r, form: r.d === 1 ? 'any' : 'frac', irr: true }, corr: 'A = ' + strong(frq(r)), meth: meth };
  }
},
{
  id: 'sci', titre: 'Notation scientifique', ex: '45' + NB + '000 = 4,5 × 10' + sup(4), req: ['sci'],
  gen: function (c) {
    var digs = String(pick([ri(1, 9), ri(11, 99), ri(101, 999)])).replace(/0+$/, '') || '1';
    var mant = Q(+digs, Math.pow(10, digs.length - 1)), mstr = f(mant), e, num, html, meth;
    var v = pick(c.lv === '3e' ? ['big', 'small', 'prod', 'prod'] : ['big', 'big', 'small']);
    if (v === 'big') {
      e = ri(Math.max(3, digs.length), 8); num = digs + new Array(e + 2 - digs.length).join('0');
      html = 'Donner l’écriture scientifique de ' + grp(num) + '.';
      meth = 'On place la virgule après le premier chiffre : ' + mstr + ', puis on compte de combien de rangs elle s’est déplacée vers la gauche (' + e + '). Donc ' + grp(num) + ' = ' + mstr + X + pw(10, e) + '.';
    } else if (v === 'small') {
      e = -ri(1, 5); num = '0,' + new Array(-e).join('0') + digs;
      html = 'Donner l’écriture scientifique de ' + num + '.';
      meth = 'Le premier chiffre non nul est ' + digs[0] + ' : on place la virgule juste après, ' + mstr + '. La virgule s’est déplacée de ' + (-e) + ' rang' + (e < -1 ? 's' : '') + ' vers la droite, d’où l’exposant ' + f(e) + '. Donc ' + num + ' = ' + mstr + X + pw(10, e) + '.';
    } else {
      var shift = pick([1, 2, -1]), p = nz(-4, 6);
      e = p + shift;
      var g = qmul(mant, Q(Math.pow(10, Math.max(shift, 0)), Math.pow(10, Math.max(-shift, 0))));
      html = 'Donner l’écriture scientifique de ' + f(g) + X + pw(10, p) + '.';
      meth = f(g) + ' = ' + mstr + X + pw(10, shift) + ', donc ' + f(g) + X + pw(10, p) + ' = ' + mstr + X + pw(10, shift) + X + pw(10, p) + ' = ' + mstr + X + pw(10, e) + '.';
    }
    return { html: html, ans: { k: 'sci', m: mant, e: e }, corr: strong(mstr + X + pw(10, e)), meth: meth };
  }
},
{
  id: 'pow10', titre: 'Puissances de 10', ex: '10' + sup(3) + ' × 10' + sup(MINUS + '2') + ' = 10' + sup(1), req: ['pui'],
  gen: function (c) {
    var v = pick(c.lv === '3e' ? ['prod', 'quot', 'powpow', 'hundred', 'write', 'prod'] : ['prod', 'quot', 'write']), a, b, e, html, meth;
    if (v === 'prod') { a = nz(-5, 8); b = nz(-6, 6); e = a + b; html = pw(10, a) + X + pw(10, b); meth = 'On additionne les exposants : ' + pw(10, a) + X + pw(10, b) + ' = ' + pw(10, f(a) + ' + ' + fp(b)) + ' = ' + pw(10, e) + '.'; }
    else if (v === 'quot') { a = nz(-3, 9); b = nz(-4, 6); e = a - b; html = fr(pw(10, a), pw(10, b)); meth = 'On soustrait les exposants : ' + fr(pw(10, a), pw(10, b)) + ' = ' + pw(10, f(a) + ' ' + MINUS + ' ' + fp(b)) + ' = ' + pw(10, e) + '.'; }
    else if (v === 'powpow') { a = nz(-3, 4); b = ri(2, 4); e = a * b; html = '(' + pw(10, a) + ')' + sup(b); meth = 'On multiplie les exposants : (' + pw(10, a) + ')' + sup(b) + ' = ' + pw(10, f(a) + X + b) + ' = ' + pw(10, e) + '.'; }
    else if (v === 'hundred') { var base = pick([100, 1000]), k = base === 100 ? 2 : 3; a = ri(2, 3); b = nz(-6, 4); e = k * a + b; html = pw(grp(String(base)), a) + X + pw(10, b); meth = grp(String(base)) + ' = ' + pw(10, k) + ', donc ' + pw(grp(String(base)), a) + ' = ' + pw(10, k * a) + ' et ' + pw(10, k * a) + X + pw(10, b) + ' = ' + pw(10, e) + '.'; }
    else { e = nz(-5, 7); var w = e > 0 ? grp('1' + new Array(e + 1).join('0')) : '0,' + new Array(-e).join('0') + '1'; html = w; meth = e > 0 ? w + ' s’écrit avec ' + e + ' zéro' + (e > 1 ? 's' : '') + ' après le 1 : ' + w + ' = ' + pw(10, e) + '.' : 'Le 1 est au rang des ' + ['dixièmes', 'centièmes', 'millièmes', 'dix-millièmes', 'cent-millièmes'][-e - 1] + ' : ' + w + ' = ' + pw(10, e) + '.'; }
    return { html: 'Écrire sous la forme d’une puissance de 10 : ' + eqs('B', html) + '.', ans: { k: 'pow', e: e }, corr: 'B = ' + strong(pw(10, e)), meth: meth };
  }
},
{
  id: 'pow-calc', titre: 'Calculer avec des puissances', ex: '2' + sup(3) + ' = 8 · 3,1 × 10' + sup(2) + ' = 310', req: ['pui'],
  gen: function (c) {
    var vs = ['small', 'sum', 'dec', 'tenp'];
    if (c.has('relx')) vs.push('neg');
    if (c.lv === '3e') vs.push('trap', 'mix', 'mix');
    var v = pick(vs), r, html, meth;
    if (v === 'small') { var b = ri(2, 5), e = b === 2 ? ri(3, 6) : b === 3 ? ri(2, 4) : ri(2, 3); r = Q(Math.pow(b, e)); html = pw(b, e); meth = pw(b, e) + ' = ' + new Array(e + 1).join(b + X).slice(0, -3) + ' = ' + f(r) + '.'; }
    else if (v === 'sum') { var a = ri(2, 9), bb = ri(2, 4); r = Q(a * a + Math.pow(bb, 3)); html = pw(a, 2) + P + pw(bb, 3); meth = pw(a, 2) + ' = ' + a * a + ' et ' + pw(bb, 3) + ' = ' + Math.pow(bb, 3) + ', donc ' + a * a + P + Math.pow(bb, 3) + ' = ' + f(r) + '.'; }
    else if (v === 'dec') { var k = ri(1, 4); r = Q(1, Math.pow(10, k)); html = null; var decQ = 'Donner l’écriture décimale de ' + pw(10, -k) + '.'; meth = pw(10, -k) + ' = ' + fr(1, pw(10, k)) + ' = ' + decStr(r) + '.'; }
    else if (v === 'tenp') { var m1 = D(ri(11, 99) / 10), p = ri(2, 4); r = qmul(m1, Q(Math.pow(10, p))); html = f(m1) + X + pw(10, p); meth = 'Multiplier par ' + pw(10, p) + ', c’est décaler la virgule de ' + p + ' rangs vers la droite : ' + f(r) + '.'; }
    else if (v === 'neg') { var nb = ri(2, 5), ne = ri(2, 4); r = Q(Math.pow(-nb, ne)); html = '(' + MINUS + nb + ')' + sup(ne); meth = '(' + MINUS + nb + ')' + sup(ne) + ' = ' + new Array(ne + 1).join('(' + MINUS + nb + ')' + X).slice(0, -3) + ' = ' + f(r) + ' (' + ne + ' facteurs négatifs : produit ' + (ne % 2 ? 'négatif' : 'positif') + ').'; }
    else if (v === 'trap') { var tb = ri(2, 6); r = Q(-tb * tb); html = MINUS + pw(tb, 2); meth = 'Attention : le carré porte seulement sur ' + tb + ', pas sur le signe. ' + MINUS + pw(tb, 2) + ' = ' + MINUS + '(' + tb + X + tb + ') = ' + f(r) + '.'; }
    else {
      var a1 = D(ri(11, 99) / 10), a2 = ri(2, 9), a3 = D(ri(11, 99) / 10);
      var t1 = qmul(a1, Q(100)), t2 = Q(a2 * 10), t3 = qmul(a3, Q(1, 10)); r = qadd(qsub(t1, t2), t3);
      html = f(a1) + X + pw(10, 2) + M + a2 + X + '10' + P + f(a3) + X + pw(10, -1);
      meth = f(a1) + X + pw(10, 2) + ' = ' + f(t1) + ' ; ' + a2 + X + '10 = ' + f(t2) + ' ; ' + f(a3) + X + pw(10, -1) + ' = ' + f(t3) + '. Donc B = ' + f(t1) + M + f(t2) + P + f(t3) + ' = ' + f(r) + '.';
    }
    if (html === null) return { html: decQ, ans: { k: 'num', q: r, form: 'dec' }, corr: pw(10, f(-Math.round(Math.log10(r.d)))) + ' = ' + strong(f(r)), meth: meth };
    return { html: 'Calculer : ' + eqs('B', html), ans: { k: 'num', q: r, form: 'any' }, corr: 'B = ' + strong(f(r)), meth: meth };
  }
},
{
  id: 'carres', titre: 'Carrés de 1 à 12 et racines carrées', ex: '7² = 49 · √81 = 9', req: [],
  gen: function (c) {
    var v = pick(c.has('rac') ? ['sq', 'sq', 'rac', 'aire', 'inv'] : ['sq']), n = ri(c.lv === '3e' ? 4 : 2, 12), html, ans, corr, meth, suf;
    if (v === 'sq') { html = 'Calculer ' + n + '².'; ans = Q(n * n); corr = n + '² = ' + strong(n * n); meth = n + '² = ' + n + X + n + ' = ' + n * n + '.'; }
    else if (v === 'rac') { html = 'Calculer √' + n * n + '.'; ans = Q(n); corr = '√' + n * n + ' = ' + strong(n); meth = n + '² = ' + n * n + ' et ' + n + ' est positif, donc √' + n * n + ' = ' + n + '.'; }
    else if (v === 'aire') { html = 'Quel est le côté d’un carré d’aire ' + n * n + ' cm² ?'; ans = Q(n); suf = 'cm'; corr = strong(n + ' cm'); meth = 'Le côté c vérifie c × c = ' + n * n + '. Comme ' + n + X + n + ' = ' + n * n + ', le côté mesure √' + n * n + ' = ' + n + ' cm.'; }
    else { html = 'Quel nombre positif a pour carré ' + n * n + ' ?'; ans = Q(n); corr = strong(n); meth = n + '² = ' + n * n + ', donc c’est ' + n + ' (c’est √' + n * n + ').'; }
    return { html: html, ans: { k: 'num', q: ans, form: 'any' }, corr: corr, meth: meth, suf: suf };
  }
},
{
  id: 'divis', titre: 'Critères de divisibilité par 2, 3, 5 et 9', ex: 'un nombre divisible par 9 se terminant par 7', req: [],
  gen: function () {
    var crit = {
      2: 'Un nombre est divisible par 2 s’il se termine par 0, 2, 4, 6 ou 8.',
      3: 'Un nombre est divisible par 3 si la somme de ses chiffres est un multiple de 3.',
      5: 'Un nombre est divisible par 5 s’il se termine par 0 ou 5.',
      9: 'Un nombre est divisible par 9 si la somme de ses chiffres est un multiple de 9.'
    };
    if (chance(0.55)) {
      var cases = [
        { d: [9], end: ri(1, 9), len: pick([4, 5]) },
        { d: [3], end: ri(1, 9), len: pick([3, 4]) },
        { d: [3, 5], len: pick([3, 4]) },
        { d: [2, 9], len: pick([3, 4]) },
        { d: [2, 3], end: pick([2, 4, 6, 8]), len: 4 },
        { d: [9], not: 2, len: 3 }
      ];
      var cs = pick(cases), txt = 'divisible par ' + cs.d.join(' et par ');
      if (cs.end !== undefined) txt += ' et se terminant par ' + cs.end;
      if (cs.not) txt += ' mais pas par ' + cs.not;
      var ok = function (n) { return cs.d.every(function (d) { return n % d === 0; }) && (cs.end === undefined || n % 10 === cs.end) && (!cs.not || n % cs.not !== 0); };
      var sample = 0, lo = Math.pow(10, cs.len - 1); for (var t = 0; t < 2000 && !sample; t++) { var x = ri(lo, lo * 10 - 1); if (ok(x)) sample = x; }
      var lens = ['', '', '', 'trois', 'quatre', 'cinq'][cs.len];
      return { html: 'Donner un nombre entier à ' + lens + ' chiffres ' + txt + '.', sample: String(sample),
        ans: { k: 'fn', f: function (s) {
          s = s.replace(/[\s .]/g, '');
          if (!/^\d+$/.test(s)) return { invalid: true, msg: 'Écris un nombre entier, sans virgule.' };
          if (s.length !== cs.len || s[0] === '0') return { ok: false, msg: 'Ton nombre doit avoir ' + lens + ' chiffres.' };
          var n = +s, why = [];
          if (cs.end !== undefined && n % 10 !== cs.end) why.push('il ne se termine pas par ' + cs.end);
          cs.d.forEach(function (d) { if (n % d) why.push('il n’est pas divisible par ' + d + (d === 3 || d === 9 ? ' (somme des chiffres : ' + digitsSum(n) + ')' : '')); });
          if (cs.not && n % cs.not === 0) why.push('il est divisible par ' + cs.not);
          return why.length ? { ok: false, msg: 'Ce nombre ne convient pas : ' + why.join(', ') + '.' } : { ok: true };
        } },
        corr: 'Par exemple ' + strong(grp(String(sample))) + ' (d’autres réponses sont possibles).',
        meth: cs.d.map(function (d) { return crit[d]; }).join(' ') + (cs.not ? ' ' + crit[cs.not].replace('est divisible', 'n’est pas divisible').replace('s’il se termine', 's’il ne se termine pas') : '') + ' Vérification : somme des chiffres de ' + sample + ' = ' + digitsSum(sample) + '.' };
    }
    var dv = pick([3, 9, 3]), digits = [ri(1, 9), ri(0, 9), ri(0, 9), ri(0, 9)], pos = ri(1, 3);
    var known = digits.reduce(function (s, x, i) { return i === pos ? s : s + x; }, 0);
    var good = []; for (var g = 0; g <= 9; g++) if ((known + g) % dv === 0) good.push(g);
    var shown = digits.map(function (x, i) { return i === pos ? '<span class="blank">■</span>' : x; }).join('');
    return { html: 'Quel chiffre peut-on écrire à la place de ■ pour que le nombre ' + shown + ' soit divisible par ' + dv + ' ? (donner une réponse)', sample: String(good[0]),
      ans: { k: 'fn', f: function (s) {
        s = s.replace(/\s/g, '');
        if (!/^\d$/.test(s)) return { invalid: true, msg: 'Écris un seul chiffre, de 0 à 9.' };
        return good.indexOf(+s) > -1 ? { ok: true } : { ok: false, msg: 'Avec ' + s + ', la somme des chiffres vaut ' + (known + +s) + ', qui n’est pas un multiple de ' + dv + '.' };
      } },
      corr: (good.length > 1 ? 'Au choix : ' : '') + strong(good.join(' ; ')),
      meth: crit[dv] + ' Sans le chiffre manquant, la somme vaut ' + known + ' ; il faut lui ajouter ' + good.join(', ') + ' pour obtenir un multiple de ' + dv + '.' };
  }
},
{
  id: 'n-expr', titre: 'Exprimer en fonction d’un entier ' + V('n'), ex: 'le successeur de ' + V('n') + ' : ' + V('n') + ' + 1', req: [],
  gen: function (c) {
    var it = [['son double', '2n', '2' + V('n'), 'Le double, c’est multiplier par 2.'],
      ['son triple', '3n', '3' + V('n'), 'Le triple, c’est multiplier par 3.'],
      ['sa moitié', 'n/2', fr(V('n'), 2) + ' (ou 0,5' + V('n') + ')', 'La moitié, c’est diviser par 2.'],
      ['son prédécesseur', 'n-1', V('n') + M + '1', 'Le prédécesseur d’un entier est l’entier juste avant : on enlève 1.'],
      ['son successeur', 'n+1', V('n') + P + '1', 'Le successeur d’un entier est l’entier juste après : on ajoute 1.'],
      ['son carré', 'n^2', V('n') + '²', 'Le carré, c’est ' + V('n') + X + V('n') + '.']];
    if (c.lv === '3e') it = it.concat([['le double de son successeur', '2(n+1)', '2(' + V('n') + P + '1)', 'Son successeur est ' + V('n') + ' + 1 ; on le multiplie par 2.'],
      ['la somme de ' + V('n') + ' et de son successeur', 'n+n+1', V('n') + P + '(' + V('n') + P + '1) = 2' + V('n') + P + '1', 'On ajoute ' + V('n') + ' et ' + V('n') + ' + 1.'],
      ['le carré de son successeur', '(n+1)^2', '(' + V('n') + P + '1)²', 'Son successeur est ' + V('n') + ' + 1 ; on l’élève au carré (parenthèses obligatoires).'],
      ['le successeur de son double', '2n+1', '2' + V('n') + P + '1', 'Son double est 2' + V('n') + ' ; on ajoute 1.']]);
    var x = pick(it);
    return { html: V('n') + ' désigne un nombre entier. Exprimer en fonction de ' + V('n') + ' : ' + x[0] + '.', ans: { k: 'expr', ref: x[1], form: 'any', v: 'n' }, kb: 'n',
      corr: strong(x[2]), meth: x[3] };
  }
},
{
  id: 'litt-red', titre: 'Réduire une expression littérale', ex: '5' + V('x') + ' + 3 ' + MINUS + ' 2' + V('x') + ' + 7 = 3' + V('x') + ' + 10', req: ['red'],
  gen: function (c) {
    var v = pick(c.lv === '3e' || c.has('dev') ? ['lin', 'lin', 'prod', 'dist', 'deg2'] : ['lin', 'lin', 'prod']), L = pick(['x', 'x', 'x', 'a', 'y']), html, cf, meth;
    if (v === 'lin') {
      var a = nz(-9, 9), b = nz(-9, 9), cc = nz(-9, 9), d = nz(-9, 9); if (a + cc === 0) cc += 1; if (!cc) cc = 2;
      if (a < 0 && chance(0.6)) a = -a;
      html = lin(a, b, L) + (cc < 0 ? M : P) + (Math.abs(cc) === 1 ? V(L) : Math.abs(cc) + V(L)) + plus(d);
      cf = { 1: a + cc, 0: b + d };
      meth = 'On regroupe les termes en ' + V(L) + ' et les nombres : (' + f(a) + plus(cc) + ')' + V(L) + ' + (' + f(b) + plus(d) + ') = ' + poly(cf, L) + '.';
    } else if (v === 'prod') {
      var p1 = ri(2, 9), p2 = ri(2, 9), two = chance(0.6);
      html = two ? p1 + V(L) + X + p2 + V(L) : p1 + X + V(L) + X + p2;
      cf = two ? { 2: p1 * p2 } : { 1: p1 * p2 };
      meth = two ? p1 + V(L) + X + p2 + V(L) + ' = ' + p1 + X + p2 + X + V(L) + X + V(L) + ' = ' + poly(cf, L) + '.' : 'On multiplie les nombres entre eux : ' + p1 + X + p2 + ' = ' + p1 * p2 + ', donc ' + poly(cf, L) + '.';
    } else if (v === 'dist') {
      var a1 = ri(2, 9), b1 = nz(-6, 6), k = ri(2, 6), c1 = ri(1, 5), d1 = nz(-5, 5), minus = chance(0.6);
      var sk = minus ? -k : k;
      html = poly({ 1: a1, 0: b1 }, L) + (minus ? M : P) + k + '(' + lin(c1, d1, L) + ')';
      cf = { 1: a1 + sk * c1, 0: b1 + sk * d1 };
      meth = 'On développe d’abord : ' + (minus ? MINUS : '') + k + '(' + lin(c1, d1, L) + ') = ' + lin(sk * c1, sk * d1, L) + '. Puis ' + poly({ 1: a1, 0: b1 }, L) + (sk * c1 < 0 ? M : P) + Math.abs(sk * c1) + V(L) + plus(sk * d1) + ' = ' + poly(cf, L) + '.';
    } else {
      var q1 = ri(2, 6), q2 = nz(-5, 5), q3 = ri(1, 4), q4 = nz(-6, 6); if (q1 === q3) q3++;
      html = q1 + V(L) + '²' + plus(q2) + V(L) + M + (q3 === 1 ? '' : q3) + V(L) + '²' + plus(q4) + V(L);
      html = html.replace(/([+−] )1<i>/g, '$1<i>');
      cf = { 2: q1 - q3, 1: q2 + q4 };
      meth = 'On regroupe les termes en ' + V(L) + '² et les termes en ' + V(L) + ' : (' + q1 + M + q3 + ')' + V(L) + '² + (' + f(q2) + plus(q4) + ')' + V(L) + ' = ' + poly(cf, L) + '.';
    }
    return { html: 'Réduire l’expression : ' + eqs('A', html) + '.', ans: { k: 'expr', ref: polyTxt(cf, L), form: 'red', v: L }, kb: L,
      corr: 'A = ' + strong(poly(cf, L)), meth: meth };
  }
},
{
  id: 'litt-val', titre: 'Calculer la valeur d’une expression', ex: '3' + V('x') + '² ' + MINUS + ' 2' + V('x') + ' + 1 pour ' + V('x') + ' = ' + MINUS + '2', req: [],
  gen: function (c) {
    var neg = c.has('relx'), v = pick(['lin', 'quad', 'quad', 'two']), r, html, meth, xv;
    if (v === 'lin') {
      var a = ri(2, 9), b = nz(-9, 9); xv = neg && chance(0.5) ? -ri(1, 6) : ri(2, 9); r = a * xv + b;
      html = 'Calculer ' + lin(a, b) + ' pour ' + V('x') + ' = ' + f(xv) + '.';
      meth = a + X + fp(xv) + plus(b) + ' = ' + f(a * xv) + plus(b) + ' = ' + f(r) + '.';
    } else if (v === 'quad') {
      var qa = ri(1, 4), qb = nz(-6, 6), qc = nz(-9, 9); xv = neg ? nz(-4, 4) : ri(1, 4); r = qa * xv * xv + qb * xv + qc;
      html = 'Calculer ' + poly({ 2: qa, 1: qb, 0: qc }) + ' pour ' + V('x') + ' = ' + f(xv) + '.';
      meth = (qa === 1 ? '' : qa + X) + fp(xv) + '²' + (qb < 0 ? M : P) + Math.abs(qb) + X + fp(xv) + plus(qc) + ' = ' + (qa === 1 ? '' : qa + X) + xv * xv + plus(qb * xv) + plus(qc) + ' = ' + f(r) + '. (Le carré se calcule avant la multiplication.)';
    } else {
      var p = ri(2, 5), q = nz(-5, 5), av = ri(1, 6), bv = neg ? nz(-6, 6) : ri(1, 6); r = p * av + q * bv;
      html = 'Calculer ' + p + V('a') + (q < 0 ? M : P) + (Math.abs(q) === 1 ? '' : Math.abs(q)) + V('b') + ' pour ' + V('a') + ' = ' + f(av) + ' et ' + V('b') + ' = ' + f(bv) + '.';
      meth = p + X + fp(av) + (q < 0 ? M : P) + Math.abs(q) + X + fp(bv) + ' = ' + f(p * av) + plus(q * bv) + ' = ' + f(r) + '.';
    }
    return { html: html, ans: { k: 'num', q: Q(r), form: 'any' }, corr: strong(f(r)), meth: meth };
  }
},
{
  id: 'dev', titre: 'Développer une expression', ex: '3(2' + V('x') + ' + 5) = 6' + V('x') + ' + 15', req: ['dev'],
  gen: function (c) {
    var vs = ['k', 'k', 'neg', 'x']; if (c.has('dev2')) vs.push('dd', 'dd');
    var v = pick(vs), html, cf, meth;
    if (v === 'k' || v === 'neg') {
      var k = ri(2, 9) * (v === 'neg' ? -1 : 1), a = nz(-9, 9), b = nz(-9, 9); if (a < 0 && chance(0.7)) a = -a;
      html = (k < 0 ? MINUS : '') + Math.abs(k) + '(' + lin(a, b) + ')'; cf = { 1: k * a, 0: k * b };
      var aT = a < 0 ? '(' + MINUS + (a === -1 ? '' : -a) + V('x') + ')' : (a === 1 ? '' : a) + V('x');
      meth = 'On distribue ' + f(k) + ' à chaque terme : ' + f(k) + X + aT + ' + ' + fp(k) + X + fp(b) + ' = ' + poly(cf) + '.';
    } else if (v === 'x') {
      var a2 = ri(1, 6), b2 = nz(-9, 9); html = V('x') + '(' + lin(a2, b2) + ')'; cf = { 2: a2, 1: b2 };
      meth = V('x') + X + (a2 === 1 ? '' : a2) + V('x') + ' + ' + V('x') + X + fp(b2) + ' = ' + poly(cf) + '.';
    } else {
      var p = ri(1, 4), q = nz(-7, 7), r = ri(1, 3), s = nz(-7, 7);
      html = '(' + lin(p, q) + ')(' + lin(r, s) + ')'; cf = { 2: p * r, 1: p * s + q * r, 0: q * s };
      meth = 'Double distributivité : ' + poly({ 2: p * r }) + plus(p * s) + V('x') + plus(q * r) + V('x') + plus(q * s) + ' = ' + poly(cf) + '.';
      meth = meth.replace(/([+−] )1<i>/g, '$1<i>');
    }
    return { html: 'Développer et réduire : ' + eqs('A', html) + '.', ans: { k: 'expr', ref: polyTxt(cf), form: 'red', v: 'x' }, kb: 'x',
      corr: 'A = ' + strong(poly(cf)), meth: meth };
  }
},
{
  id: 'fact', titre: 'Factoriser une expression', ex: '6' + V('x') + ' + 9 = 3(2' + V('x') + ' + 3)', req: ['fact'],
  gen: function (c) {
    var vs = ['k', 'k', 'x']; if (c.has('id')) vs.push('id', 'id');
    var v = pick(vs), html, ref, corr, meth;
    if (v === 'k') {
      var k = ri(2, 9), a, b; do { a = ri(1, 7); b = nz(-9, 9); } while (gcd(a, b) !== 1);
      html = lin(k * a, k * b); ref = k + '(' + polyTxt({ 1: a, 0: b }) + ')'; corr = k + '(' + lin(a, b) + ')';
      meth = 'Le facteur commun est ' + k + ' : ' + lin(k * a, k * b) + ' = ' + k + X + (a === 1 ? '' : a) + V('x') + (b < 0 ? M : P) + k + X + Math.abs(b) + ' = ' + corr + '.';
    } else if (v === 'x') {
      var a2 = ri(1, 5), b2 = nz(-9, 9); html = poly({ 2: a2, 1: b2 }); ref = 'x(' + polyTxt({ 1: a2, 0: b2 }) + ')'; corr = V('x') + '(' + lin(a2, b2) + ')';
      meth = 'Le facteur commun est ' + V('x') + ' : ' + html + ' = ' + V('x') + X + (a2 === 1 ? '' : a2) + V('x') + (b2 < 0 ? M : P) + V('x') + X + Math.abs(b2) + ' = ' + corr + '.';
    } else {
      var p = ri(1, 4), q; do { q = ri(1, 9); } while (gcd(p, q) !== 1); html = poly({ 2: p * p, 0: -q * q }); ref = '(' + polyTxt({ 1: p, 0: -q }) + ')(' + polyTxt({ 1: p, 0: q }) + ')';
      corr = '(' + lin(p, -q) + ')(' + lin(p, q) + ')';
      meth = 'On reconnaît ' + V('a') + '² ' + MINUS + ' ' + V('b') + '² = (' + V('a') + M + V('b') + ')(' + V('a') + P + V('b') + ') avec ' + V('a') + ' = ' + (p === 1 ? '' : p) + V('x') + ' et ' + V('b') + ' = ' + q + ' : ' + html + ' = ' + (p === 1 ? V('x') : '(' + p + V('x') + ')') + '²' + M + q + '² = ' + corr + '.';
    }
    return { html: 'Factoriser : ' + eqs('A', html) + '.', ans: { k: 'expr', ref: ref, form: 'fact', v: 'x' }, kb: 'x', corr: 'A = ' + strong(corr), meth: meth };
  }
},
{
  id: 'eq', titre: 'Résoudre une équation', ex: '3' + V('x') + ' ' + MINUS + ' 2 = 25', req: ['eq'],
  gen: function (c) {
    var v = pick(c.lv === '3e' ? ['ax', 'xb', 'axb', 'axb', 'two', 'two'] : ['ax', 'xb', 'axb', 'axb']), sol, html, meth;
    sol = nz(-12, 12);
    if (v === 'ax') {
      var a = nz(-9, 9); if (Math.abs(a) === 1) a = 4;
      if (c.lv === '3e' && chance(0.3)) { var cc = nz(-20, 20); sol = Q(cc, a); html = poly({ 1: a }) + ' = ' + f(cc); meth = 'On divise les deux membres par ' + f(a) + ' : ' + V('x') + ' = ' + f(cc) + ' ÷ ' + fp(a) + ' = ' + frq(sol) + '.'; }
      else { sol = Q(sol); html = poly({ 1: a }) + ' = ' + f(a * sol.n); meth = 'On divise les deux membres par ' + f(a) + ' : ' + V('x') + ' = ' + f(a * sol.n) + ' ÷ ' + fp(a) + ' = ' + f(sol) + '.'; }
    } else if (v === 'xb') {
      var b = nz(-15, 15); html = lin(1, b) + ' = ' + f(sol + b); meth = 'On ' + (b > 0 ? 'soustrait ' + b : 'ajoute ' + (-b)) + ' aux deux membres : ' + V('x') + ' = ' + f(sol + b) + plus(-b) + ' = ' + f(sol) + '.'; sol = Q(sol);
    } else if (v === 'axb') {
      var a2 = ri(2, 9) * (c.has('relx') && chance(0.25) ? -1 : 1), b2 = nz(-12, 12), rhs = a2 * sol + b2;
      html = lin(a2, b2) + ' = ' + f(rhs);
      meth = 'On ' + (b2 > 0 ? 'soustrait ' + b2 : 'ajoute ' + (-b2)) + ' aux deux membres : ' + poly({ 1: a2 }) + ' = ' + f(rhs - b2) + '. Puis on divise par ' + f(a2) + ' : ' + V('x') + ' = ' + f(sol) + '.'; sol = Q(sol);
    } else {
      var a3 = ri(2, 9), c3; do { c3 = ri(1, 8); } while (c3 === a3);
      var b3 = nz(-12, 12), d3 = (a3 - c3) * sol + b3;
      html = lin(a3, b3) + ' = ' + lin(c3, d3);
      meth = 'On regroupe les ' + V('x') + ' dans un membre : ' + lin(a3 - c3, b3) + ' = ' + f(d3) + ', puis ' + poly({ 1: a3 - c3 }) + ' = ' + f(d3 - b3) + ', donc ' + V('x') + ' = ' + f(sol) + '.'; sol = Q(sol);
      meth = meth.replace(/>1<i>/g, '><i>');
    }
    return { html: 'Déterminer la solution de l’équation : ' + '<span class="nw">' + html + '</span>', ans: { k: 'num', q: sol, form: 'any' }, pre: V('x') + ' =',
      corr: V('x') + ' = ' + strong(nq(sol)), meth: meth };
  }
},
{
  id: 'droite', titre: 'Lire une abscisse sur une droite graduée', ex: 'graduations en quarts, dixièmes…', req: [],
  gen: function (c) {
    var s = pick(c.lv === '3e' ? [2, 4, 5, 10, 3, 4, 5] : [2, 4, 5, 10, 4, 5]), L = ri(c.has('relx') || c.lv === '3e' ? -3 : 0, 4);
    var units = s >= 10 ? 2 : 3, ticks = units * s, startOff = s >= 10 ? 0 : ri(0, 1) * s; // graduation de L
    var k; do { k = ri(1, ticks - 1); } while (k === startOff || k === startOff + s || k % s === 0 && chance(0.85));
    var pos = Q((L - startOff / s) * s + k, s), W = 560, x0 = 30, x1 = 530, step = (x1 - x0) / ticks, svg = [];
    svg.push('<svg class="droite" viewBox="0 0 ' + W + ' 96" role="img" aria-label="Droite graduée">');
    svg.push('<line x1="10" y1="52" x2="' + (W - 12) + '" y2="52" stroke="currentColor" stroke-width="2"/><path d="M' + (W - 12) + ' 52l-10 -6v12z" fill="currentColor"/>');
    for (var i = 0; i <= ticks; i++) {
      var X0 = (x0 + i * step).toFixed(1), big = (i - startOff) % s === 0;
      svg.push('<line x1="' + X0 + '" y1="' + (big ? 42 : 46) + '" x2="' + X0 + '" y2="' + (big ? 62 : 58) + '" stroke="currentColor" stroke-width="' + (big ? 2 : 1.4) + '"/>');
    }
    [startOff, startOff + s].forEach(function (i, j) { var X1 = (x0 + i * step).toFixed(1); svg.push('<text x="' + X1 + '" y="84" text-anchor="middle" class="dl">' + f(L + j) + '</text>'); });
    var XA = (x0 + k * step).toFixed(1);
    svg.push('<circle cx="' + XA + '" cy="52" r="5" class="dp"/><text x="' + XA + '" y="30" text-anchor="middle" class="dA">A</text></svg>');
    var gv = Q(1, s), n = k - startOff;
    return { html: 'Quelle est l’abscisse du point A ?' + svg.join(''), ans: { k: 'num', q: pos, form: 'any' },
      corr: 'A(' + strong(nq(pos)) + ')',
      meth: 'Une unité est partagée en ' + s + ' graduations : une graduation vaut ' + fr(1, s) + (isDec(gv) ? ' = ' + decStr(gv) : '') + '. A est à ' + Math.abs(n) + ' graduation' + (Math.abs(n) > 1 ? 's' : '') + ' ' + (n >= 0 ? 'à droite' : 'à gauche') + ' de ' + f(L) + ', donc son abscisse est ' + f(L) + (n >= 0 ? P : M) + fr(Math.abs(n), s) + ' = ' + nq(pos) + '.' };
  }
}
];

/* Thèmes de la liste officielle d'automatismes (les autres arrivent progressivement) */
var THEMES = [
  { id: 'nc', titre: 'Nombres et calculs', gens: NC },
  { id: 'geo', titre: 'Espace et géométrie', gens: [] },
  { id: 'data', titre: 'Données et probabilités', gens: [] },
  { id: 'fct', titre: 'Proportionnalité et fonctions', gens: [] },
  { id: 'algo', titre: 'Algorithmique et programmation', gens: [] }
];

/* Étiquettes déduites des titres des notions vues en classe.
   En 3e, tout le programme de 4e est considéré comme acquis. */
var TAGS = {
  relx: /multipli\w* des (nombres )?relatifs|diviser des (nombres )?relatifs|opérations sur les (nombres )?relatifs/i,
  frac: /fraction/i, pui: /puissance/i, sci: /scientifique/i, rac: /racine|carrés parfaits/i,
  red: /réduire/i, dev: /développer|distributivité/i, dev2: /double distributivit/i,
  fact: /factoris/i, id: /identit|remarquable|différence de deux carrés/i, eq: /équation/i,
  pyth: /pythagore/i, thales: /thal[eè]s/i, cos: /cosinus|trigonom/i, transl: /translation/i, med: /médiane/i,
  pyr: /pyramide|cône/i, pct: /pourcentage/i, fct: /fonction/i
};
var ACQUIS = { '4e': [], '3e': ['relx', 'frac', 'pui', 'sci', 'rac', 'red', 'dev', 'fact', 'eq', 'pyth', 'thales', 'cos', 'transl', 'med', 'pyr', 'pct'] };
function tagsFrom(lv, titles) {
  var t = {}; (ACQUIS[lv] || []).forEach(function (k) { t[k] = 1; });
  titles.forEach(function (ti) { for (var k in TAGS) if (TAGS[k].test(ti)) t[k] = 1; });
  return t;
}

/* Réponse « modèle » d'une question (sert aux tests automatiques) */
function sampleAnswer(q) {
  var a = q.ans;
  switch (a.k) {
    case 'num': return a.form !== 'frac' && isDec(a.q) ? decStr(a.q).replace(MINUS, '-').replace(/ /g, '') : a.q.n + '/' + a.q.d;
    case 'sym': return a.v;
    case 'pow': return String(a.e);
    case 'sci': return [decStr(a.m), String(a.e)];
    case 'expr': return a.ref;
    case 'fn': case 'words': case 'pyeq': return q.sample;
    case 'pair': return [decStr(a.x).replace(MINUS, '-'), decStr(a.y).replace(MINUS, '-')];
    case 'txt': return a.v[0];
    case 'ratio': return a.n + '/' + a.d;
  }
}

var H = { ri: ri, pick: pick, chance: chance, nz: nz, sgn: sgn, shuffle: shuffle, gcd: gcd, lcm: lcm, Q: Q, qadd: qadd, qsub: qsub, qmul: qmul, qdiv: qdiv, qeq: qeq, qcmp: qcmp, D: D, isDec: isDec, qv: qv,
  MINUS: MINUS, NB: NB, grp: grp, decStr: decStr, fr: fr, frs: frs, frq: frq, nq: nq, f: f, fp: fp, V: V, sup: sup, pw: pw, eqs: eqs, strong: strong, X: X, P: P, M: M, plus: plus, poly: poly, polyTxt: polyTxt, lin: lin, plain: plain };
var API = { H: H, THEMES: THEMES, TAGS: TAGS, tagsFrom: tagsFrom, check: check, parseExpr: parseExpr, parseNumber: parseNumber, sampleAnswer: sampleAnswer, shuffle: shuffle, pick: pick };
if (typeof module !== 'undefined' && module.exports) module.exports = API; else root.AUTO = API;
})(this);
