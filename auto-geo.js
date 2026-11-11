/* Automatismes du DNB – thème « Espace et géométrie » (figures dessinées en SVG). */
(function (root) {
'use strict';
var A = (typeof module !== 'undefined' && module.exports) ? require('./auto-gen.js') : root.AUTO;
var H = A.H, ri = H.ri, pick = H.pick, chance = H.chance, nz = H.nz, shuffle = H.shuffle, Q = H.Q, D = H.D, f = H.f, fr = H.fr,
  nq = H.nq, strong = H.strong, X = H.X, P = H.P, M = H.M, MINUS = H.MINUS, qmul = H.qmul, qv = H.qv, NB = H.NB;

/* ---------- outils de dessin ---------- */
function n1(x) { return Math.round(x * 10) / 10; }
function add(a, b) { return [a[0] + b[0], a[1] + b[1]]; }
function sub(a, b) { return [a[0] - b[0], a[1] - b[1]]; }
function mul(a, k) { return [a[0] * k, a[1] * k]; }
function len(a) { return Math.sqrt(a[0] * a[0] + a[1] * a[1]); }
function unit(a) { var l = len(a) || 1; return [a[0] / l, a[1] / l]; }
function perp(a) { return [-a[1], a[0]]; }
function mid(a, b) { return [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]; }
function cent(ps) { var s = [0, 0]; ps.forEach(function (p) { s = add(s, p); }); return mul(s, 1 / ps.length); }
function L(a, b, c) { return '<line x1="' + n1(a[0]) + '" y1="' + n1(a[1]) + '" x2="' + n1(b[0]) + '" y2="' + n1(b[1]) + '" class="' + (c || 'ln') + '"/>'; }
function PG(ps, c) { return '<polygon points="' + ps.map(function (p) { return n1(p[0]) + ',' + n1(p[1]); }).join(' ') + '" class="' + (c || 'ln') + '"/>'; }
function PL(ps, c) { return '<polyline points="' + ps.map(function (p) { return n1(p[0]) + ',' + n1(p[1]); }).join(' ') + '" class="' + (c || 'ln') + '"/>'; }
function T(p, t, c, anchor) { return '<text x="' + n1(p[0]) + '" y="' + n1(p[1]) + '" text-anchor="' + (anchor || 'middle') + '" dominant-baseline="central"' + (c ? ' class="' + c + '"' : '') + '>' + t + '</text>'; }
function DOT(p, r) { return '<circle cx="' + n1(p[0]) + '" cy="' + n1(p[1]) + '" r="' + (r || 3.5) + '" class="pt"/>'; }
function CROSS(p) { return L(add(p, [-5, -5]), add(p, [5, 5]), 'th') + L(add(p, [-5, 5]), add(p, [5, -5]), 'th'); }
function lab(p, c, t, d) { return T(add(p, mul(unit(sub(p, c)), d || 16)), t, 'it'); }        // étiquette d'un sommet, vers l'extérieur
function side(a, b, c, t, d) {                                                                // longueur écrite au milieu d'un côté, côté extérieur
  var m = mid(a, b), n = unit(perp(sub(b, a))); if ((m[0] - c[0]) * n[0] + (m[1] - c[1]) * n[1] < 0) n = mul(n, -1);
  return T(add(m, mul(n, d || 16)), t);
}
function ticks(a, b, k) {
  var m = mid(a, b), u = unit(sub(b, a)), n = perp(u), s = '';
  for (var i = 0; i < k; i++) { var o = add(m, mul(u, (i - (k - 1) / 2) * 6)); s += L(add(o, mul(n, -7)), add(o, mul(n, 7)), 'acc'); }
  return s;
}
function right(v, a, b, s) { s = s || 13; var u = mul(unit(sub(a, v)), s), w = mul(unit(sub(b, v)), s); return PL([add(v, u), add(add(v, u), w), add(v, w)], 'acc'); }
function arcAt(v, a, b, r) { // arc d'angle au sommet v, entre les directions de a et de b
  r = r || 26; var u = unit(sub(a, v)), w = unit(sub(b, v)), p1 = add(v, mul(u, r)), p2 = add(v, mul(w, r));
  var cr = u[0] * w[1] - u[1] * w[0];
  return '<path d="M' + n1(p1[0]) + ' ' + n1(p1[1]) + 'A' + r + ' ' + r + ' 0 0 ' + (cr > 0 ? 1 : 0) + ' ' + n1(p2[0]) + ' ' + n1(p2[1]) + '" class="acc"/>';
}
function rot(ps, deg, c) { var a = deg * Math.PI / 180, co = Math.cos(a), si = Math.sin(a); c = c || cent(ps); return ps.map(function (p) { var d = sub(p, c); return [c[0] + d[0] * co - d[1] * si, c[1] + d[0] * si + d[1] * co]; }); }
function svgFit(ps, body, pad, cls) { // cadre ajusté aux points
  pad = pad || 34; var xs = ps.map(function (p) { return p[0]; }), ys = ps.map(function (p) { return p[1]; });
  var x0 = Math.min.apply(0, xs) - pad, y0 = Math.min.apply(0, ys) - pad, w = Math.max.apply(0, xs) - x0 + pad, h = Math.max.apply(0, ys) - y0 + pad;
  return '<svg class="fig' + (cls ? ' ' + cls : '') + '" viewBox="' + n1(x0) + ' ' + n1(y0) + ' ' + n1(w) + ' ' + n1(h) + '" role="img" aria-label="Figure">' + body + '</svg>';
}
function svg(w, h, body, cls) { return '<svg class="fig' + (cls ? ' ' + cls : '') + '" viewBox="0 0 ' + w + ' ' + h + '" role="img" aria-label="Figure">' + body + '</svg>'; }
function ang(t) { return '<span class="ang">' + t + '</span>'; }
function seg(t) { return '[' + t + ']'; }
var LETTERS3 = [['A', 'B', 'C'], ['E', 'F', 'G'], ['R', 'S', 'T'], ['M', 'N', 'P'], ['I', 'J', 'K'], ['D', 'E', 'F']];
var LETTERS4 = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['M', 'N', 'O', 'P'], ['R', 'S', 'T', 'U'], ['I', 'J', 'K', 'L']];
function cm(x) { return f(x) + NB + 'cm'; }
function words(need, o) { o = o || {}; return { k: 'words', need: need, forbid: o.forbid, near: o.near }; }

/* triangle rectangle tourné au hasard : sommet de l'angle droit, puis les deux autres */
function rightTri(a, b, sc) {
  var R = [0, 0], Pp = [a * sc, 0], Qq = [0, -b * sc];
  var ps = rot([R, Pp, Qq], ri(0, 3) * 90 + ri(-20, 20), [0, 0]);
  if (chance(0.5)) ps = ps.map(function (p) { return [-p[0], p[1]]; });
  return ps;
}

var GEO = [
{
  id: 'coord', titre: 'Lire et repérer des coordonnées', ex: 'A(2 ; ' + MINUS + '3)', req: [],
  gen: function () {
    var U = 28, x0 = -5, x1 = 5, y0 = -4, y1 = 4, W = (x1 - x0) * U + 40, Hh = (y1 - y0) * U + 40, ox = 20 - x0 * U, oy = 20 + y1 * U;
    var sp = function (x, y) { return [ox + x * U, oy - y * U]; }, b = '';
    for (var i = x0; i <= x1; i++) b += L(sp(i, y0), sp(i, y1), 'grid');
    for (var j = y0; j <= y1; j++) b += L(sp(x0, j), sp(x1, j), 'grid');
    b += L(sp(x0, 0), add(sp(x1, 0), [12, 0]), 'ax') + L(sp(0, y0), add(sp(0, y1), [0, -12]), 'ax');
    b += PG([add(sp(x1, 0), [14, 0]), add(sp(x1, 0), [6, -4]), add(sp(x1, 0), [6, 4])], 'pt') + PG([add(sp(0, y1), [0, -14]), add(sp(0, y1), [-4, -6]), add(sp(0, y1), [4, -6])], 'pt');
    for (i = x0; i <= x1; i++) if (i) b += T(add(sp(i, 0), [0, 13]), f(i), 'lt');
    for (j = y0; j <= y1; j++) if (j) b += T(add(sp(0, j), [-12, 0]), f(j), 'lt');
    b += T(add(sp(0, 0), [-10, 12]), '0', 'lt');
    var x = ri(-5, 5), y = ri(-4, 4); if (!x && !y) x = 3; if (chance(0.7) && (!x || !y)) { x = nz(-5, 5); y = nz(-4, 4); }
    var meth = 'On lit d’abord l’abscisse sur l’axe horizontal (' + f(x) + '), puis l’ordonnée sur l’axe vertical (' + f(y) + ').';
    if (chance(0.55)) {
      b += DOT(sp(x, y), 4.5) + T(add(sp(x, y), [12, -12]), 'A', 'it');
      return { html: 'Lire les coordonnées du point A.' + svg(W, Hh, b), ans: { k: 'pair', x: Q(x), y: Q(y) }, pt: 'A', corr: 'A(' + strong(f(x) + ' ; ' + f(y)) + ')', meth: meth };
    }
    var cand = [[x, y], [y, x], [-x, y], [x, -y], [-y, -x], [y, -x]].filter(function (p, k, arr) {
      return Math.abs(p[0]) <= 5 && Math.abs(p[1]) <= 4 && arr.findIndex(function (q) { return q[0] === p[0] && q[1] === p[1]; }) === k;
    });
    var pts = [cand[0]].concat(shuffle(cand.slice(1)).slice(0, 3)), names = shuffle(pick(LETTERS4)), ans = names[0];
    pts.forEach(function (p, k) { b += DOT(sp(p[0], p[1]), 4.5) + T(add(sp(p[0], p[1]), [12, -12]), names[k], 'it'); });
    return { html: 'Quel point a pour coordonnées (' + f(x) + ' ; ' + f(y) + ') ?' + svg(W, Hh, b), ans: { k: 'txt', v: [ans] },
      corr: 'C’est le point ' + strong(ans) + '.', meth: meth };
  }
},
{
  id: 'codage', titre: 'Exploiter le codage d’une figure', ex: 'triangle isocèle, losange, médiatrice…', req: [],
  gen: function () {
    var t = pick(['iso', 'equi', 'rect', 'ri', 'rectangle', 'losange', 'carre', 'para', 'med', 'med']), ps, b = '', name, need, o = {}, corr, meth, q;
    var deg = ri(-30, 30);
    if (t === 'med') {
      var A0 = [40, 140], B0 = [260, 140], I0 = [150, 140], d1 = [150, 30], d2 = [150, 250];
      ps = rot([A0, B0, I0, d1, d2], deg); var nm = pick([['A', 'B'], ['E', 'F'], ['M', 'N']]);
      b += L(ps[0], ps[1]) + L(ps[3], ps[4], 'th') + ticks(ps[0], ps[2], 2) + ticks(ps[2], ps[1], 2) + right(ps[2], ps[1], ps[3]) + CROSS(ps[0]) + CROSS(ps[1]);
      b += T(add(ps[0], [0, 18]), nm[0], 'it') + T(add(ps[1], [0, 18]), nm[1], 'it') + T(add(ps[3], [14, 4]), '(d)', 'it');
      return { html: 'D’après le codage, que représente la droite (d) pour le segment [' + nm.join('') + '] ?' + svgFit(ps, b),
        ans: words([['mediatrice']]), sample: 'la médiatrice', corr: '(d) est la ' + strong('médiatrice') + ' du segment [' + nm.join('') + '].',
        meth: '(d) est perpendiculaire à [' + nm.join('') + '] et passe par son milieu : c’est sa médiatrice.' };
    }
    var tri = ['iso', 'equi', 'rect', 'ri'].indexOf(t) > -1, Ls = tri ? pick(LETTERS3) : pick(LETTERS4);
    var shapes = {
      iso: [[40, 200], [240, 200], [140, 50]], equi: [[50, 200], [230, 200], [140, 44]], rect: [[50, 200], [250, 200], [50, 70]], ri: [[60, 200], [200, 200], [60, 60]],
      rectangle: [[40, 60], [260, 60], [260, 180], [40, 180]], losange: [[150, 30], [250, 120], [150, 210], [50, 120]],
      carre: [[80, 50], [210, 50], [210, 180], [80, 180]], para: [[40, 180], [200, 180], [260, 60], [100, 60]]
    };
    ps = rot(shapes[t], deg); var c = cent(ps), n = ps.length;
    b += PG(ps);
    ps.forEach(function (p, k) { b += lab(p, c, Ls[k]); });
    name = Ls.join('');
    var tk = function (i, j, k) { b += ticks(ps[i], ps[j], k); };
    if (t === 'iso') { tk(2, 0, 1); tk(2, 1, 1); need = [['isocele']]; o.forbid = ['equilateral', 'rectangle']; corr = 'isocèle en ' + Ls[2]; meth = 'Les côtés [' + Ls[2] + Ls[0] + '] et [' + Ls[2] + Ls[1] + '] ont le même codage : ils ont la même longueur.'; }
    if (t === 'equi') { tk(0, 1, 1); tk(1, 2, 1); tk(2, 0, 1); need = [['equilateral']]; o.near = [{ has: 'isocele', msg: 'C’est vrai, mais on peut être plus précis : regarde les trois côtés.' }]; corr = 'équilatéral'; meth = 'Les trois côtés ont le même codage : ils ont la même longueur.'; }
    if (t === 'rect') { b += right(ps[0], ps[1], ps[2]); need = [['rectangle']]; o.forbid = ['isocele', 'equilateral']; corr = 'rectangle en ' + Ls[0]; meth = 'Le codage indique un angle droit en ' + Ls[0] + '.'; }
    if (t === 'ri') { b += right(ps[0], ps[1], ps[2]); tk(0, 1, 1); tk(0, 2, 1); need = [['rectangle'], ['isocele']]; o.near = [{ has: 'rectangle', msg: 'C’est vrai, mais il manque une information : regarde aussi les longueurs.' }, { has: 'isocele', msg: 'C’est vrai, mais il manque une information : regarde aussi l’angle.' }]; corr = 'rectangle et isocèle en ' + Ls[0]; meth = 'Il y a un angle droit en ' + Ls[0] + ' et deux côtés de même longueur.'; }
    if (t === 'rectangle') { b += right(ps[0], ps[1], ps[3]) + right(ps[1], ps[0], ps[2]) + right(ps[2], ps[1], ps[3]); need = [['rectangle']]; o.forbid = ['carre', 'losange']; corr = 'un rectangle'; meth = 'Un quadrilatère qui a trois angles droits est un rectangle.'; }
    if (t === 'losange') { tk(0, 1, 1); tk(1, 2, 1); tk(2, 3, 1); tk(3, 0, 1); need = [['losange']]; o.forbid = ['carre', 'rectangle']; o.near = [{ has: 'parallelogramme', msg: 'C’est vrai, mais on peut être plus précis : regarde les quatre côtés.' }]; corr = 'un losange'; meth = 'Un quadrilatère qui a quatre côtés de même longueur est un losange.'; }
    if (t === 'carre') { tk(0, 1, 1); tk(1, 2, 1); tk(2, 3, 1); tk(3, 0, 1); b += right(ps[0], ps[1], ps[3]); need = [['carre']]; o.near = [{ has: 'losange', msg: 'C’est vrai, mais on peut être plus précis : il a aussi un angle droit.' }, { has: 'rectangle', msg: 'C’est vrai, mais on peut être plus précis : ses quatre côtés ont la même longueur.' }]; corr = 'un carré'; meth = 'Quatre côtés de même longueur et un angle droit : c’est un carré.'; }
    if (t === 'para') { tk(0, 1, 1); tk(2, 3, 1); tk(1, 2, 2); tk(3, 0, 2); need = [['parallelogramme']]; o.forbid = ['rectangle', 'losange', 'carre']; corr = 'un parallélogramme'; meth = 'Les côtés opposés ont deux à deux la même longueur : c’est un parallélogramme.'; }
    q = tri ? 'D’après le codage, quelle est la nature du triangle ' + name + ' ?' : 'D’après le codage, quelle est la nature du quadrilatère ' + name + ' ?';
    return { html: q + svgFit(ps, b), ans: words(need, o), sample: corr.replace(/^un /, ''),
      corr: name + ' est ' + (tri ? 'un triangle ' : '') + strong(corr) + '.', meth: meth };
  }
},
{
  id: 'angles', titre: 'Reconnaître et nommer des angles', ex: 'opposés par le sommet, supplémentaires…', req: [],
  gen: function () {
    var v = pick(['opp', 'opp', 'supp', 'supp', 'nat', 'voc']), b = '', O = [160, 120], R = 110, a, t1, t2;
    var dir = function (deg) { var r = deg * Math.PI / 180; return [Math.cos(r), -Math.sin(r)]; };
    var at = function (deg, r) { return add(O, mul(dir(deg), r)); };
    var mark = function (d1, d2, txt) { var mdeg = (d1 + d2) / 2; return arcAt(O, at(d1, 10), at(d2, 10), 24) + T(at(mdeg, 44), txt); };
    if (v === 'opp' || (v === 'voc' && chance(0.5))) {
      a = ri(30, 150); t1 = ri(-15, 25); t2 = t1 + a;
      b += L(at(t1, R), at(t1 + 180, R)) + L(at(t2, R), at(t2 + 180, R)) + DOT(O);
      b += mark(t1, t2, a + '°') + mark(t1 + 180, t2 + 180, v === 'voc' ? '' : '?');
      if (v === 'voc') return { html: 'Comment appelle-t-on les deux angles marqués ?' + svg(320, 240, b), ans: words([['oppose']]), sample: 'opposés par le sommet',
        corr: 'Ils sont ' + strong('opposés par le sommet') + '.', meth: 'Ils ont le même sommet et leurs côtés sont dans le prolongement l’un de l’autre. Deux angles opposés par le sommet ont la même mesure.' };
      return { html: 'Les deux droites sont sécantes. Quelle est la mesure de l’angle marqué « ? » ?' + svg(320, 240, b), ans: { k: 'num', q: Q(a), form: 'any' }, suf: '°',
        corr: strong(a + '°'), meth: 'Les deux angles sont opposés par le sommet : ils ont la même mesure.' };
    }
    if (v === 'supp' || v === 'voc') {
      a = ri(25, 155); t1 = 0;
      b += L(at(0, R + 20), at(180, R + 20)) + L(O, at(a, R)) + DOT(O);
      b += mark(0, a, v === 'voc' ? '' : a + '°') + mark(a, 180, v === 'voc' ? '' : '?');
      if (v === 'voc') return { html: 'Les deux angles marqués forment un angle plat. Comment appelle-t-on deux angles dont la somme des mesures vaut 180° ?' + svg(320, 160, b.replace(/<line[^>]*>/, function (m) { return m; })), ans: words([['supplementaire']]), sample: 'supplémentaires',
        corr: 'Ils sont ' + strong('supplémentaires') + '.', meth: 'Deux angles dont la somme vaut 180° sont supplémentaires (s’ils ont un côté commun, ils sont aussi adjacents).' };
      return { html: 'Quelle est la mesure de l’angle marqué « ? » ?' + svg(320, 160, b), ans: { k: 'num', q: Q(180 - a), form: 'any' }, suf: '°',
        corr: strong((180 - a) + '°'), meth: 'Les deux angles forment un angle plat (180°) : 180 − ' + a + ' = ' + (180 - a) + '°.'.replace('−', MINUS) };
    }
    var k = pick(['aigu', 'aigu', 'obtus', 'obtus', 'droit', 'plat']), val = k === 'aigu' ? ri(5, 89) : k === 'obtus' ? ri(91, 179) : k === 'droit' ? 90 : 180;
    return { html: 'Un angle mesure ' + val + '°. Est-il aigu, droit, obtus ou plat ?', ans: words([[k]], { forbid: ['aigu', 'droit', 'obtus', 'plat'].filter(function (x) { return x !== k; }) }), sample: k,
      corr: 'Il est ' + strong(k) + '.', meth: 'Aigu : entre 0° et 90° ; droit : 90° ; obtus : entre 90° et 180° ; plat : 180°.' };
  }
},
{
  id: 'tri-angles', titre: 'Somme des angles d’un triangle', ex: '180° ' + MINUS + ' (50° + 65°) = 65°', req: [],
  gen: function () {
    var Ls = pick(LETTERS3), a = Ls[0], b = Ls[1], c = Ls[2], v = pick(['gen', 'gen', 'iso', 'iso2', 'rect']), x, y, r, html, meth;
    var A_ = ang(b + a + c), B_ = ang(a + b + c), C_ = ang(a + c + b);
    if (v === 'gen') { x = ri(20, 110); y = ri(15, 160 - x); r = 180 - x - y; html = 'Dans le triangle ' + Ls.join('') + ', ' + A_ + ' = ' + x + '° et ' + B_ + ' = ' + y + '°. Calculer la mesure de l’angle ' + C_ + '.'; meth = 'La somme des angles d’un triangle vaut 180° : 180 − (' + x + ' + ' + y + ') = 180 − ' + (x + y) + ' = ' + r + '°.'; }
    else if (v === 'iso') { x = 2 * ri(10, 70); r = (180 - x) / 2; html = Ls.join('') + ' est un triangle isocèle en ' + a + ' et ' + A_ + ' = ' + x + '°. Calculer la mesure de l’angle ' + B_ + '.'; meth = 'Les angles à la base d’un triangle isocèle sont égaux : (180 − ' + x + ') ÷ 2 = ' + (180 - x) + ' ÷ 2 = ' + r + '°.'; }
    else if (v === 'iso2') { x = ri(25, 85); r = 180 - 2 * x; html = Ls.join('') + ' est un triangle isocèle en ' + a + ' et ' + B_ + ' = ' + x + '°. Calculer la mesure de l’angle ' + A_ + '.'; meth = 'Les angles à la base sont égaux : ' + C_ + ' = ' + x + '°. Donc ' + A_ + ' = 180 − 2 × ' + x + ' = ' + r + '°.'; }
    else { x = ri(15, 75); r = 90 - x; html = Ls.join('') + ' est un triangle rectangle en ' + a + ' et ' + B_ + ' = ' + x + '°. Calculer la mesure de l’angle ' + C_ + '.'; meth = 'L’angle droit mesure 90°, donc 180 − 90 − ' + x + ' = ' + r + '°.'; }
    return { html: html, ans: { k: 'num', q: Q(r), form: 'any' }, suf: '°', corr: strong(r + '°'), meth: meth.replace(/ − /g, M) };
  }
},
{
  id: 'conv', titre: 'Conversions d’unités', ex: '3,5 km = 3' + NB + '500 m · 1,5 h = 90 min', req: [],
  gen: function () {
    var v = pick(['long', 'long', 'aire', 'vol', 'masse', 'cont', 'litre', 'duree', 'duree']), from, to, val, res, meth, html;
    var show = function (q) { return f(q); };
    if (['long', 'aire', 'vol', 'cont'].indexOf(v) > -1) {
      var U = { long: ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km'], aire: ['mm²', 'cm²', 'dm²', 'm²'], vol: ['mm³', 'cm³', 'dm³', 'm³'], cont: ['mL', 'cL', 'dL', 'L'] }[v];
      var base = { long: 10, aire: 100, vol: 1000, cont: 10 }[v], i, j, k;
      do {
        i = ri(0, U.length - 1); j = ri(0, U.length - 1);
        if (v === 'long' && chance(0.5)) { i = pick([6, 3, 4]); j = pick([3, 1, 0, 6]); }
        val = D(pick([ri(1, 9), ri(11, 99), ri(101, 999)]) / pick([1, 10, 100]));
        k = Math.pow(base, Math.abs(i - j)); res = i > j ? qmul(val, Q(k)) : qmul(val, Q(1, k));
      } while (i === j || Math.abs(i - j) > (base === 1000 ? 1 : base === 100 ? 2 : 3) || qv(res) > 1e6 || qv(res) < 0.001 || !H.isDec(res));
      from = U[i]; to = U[j];
      meth = (i > j ? '1 ' + from + ' = ' + f(k) + ' ' + to + ', donc on multiplie par ' + f(k) : '1 ' + to + ' = ' + f(k) + ' ' + from + ', donc on divise par ' + f(k)) + ' : ' + show(val) + ' ' + from + ' = ' + show(res) + ' ' + to + '.';
      html = 'Compléter : ' + show(val) + ' ' + from + ' = … ' + to;
    } else if (v === 'masse') {
      if (chance(0.5)) { val = D(ri(1, 99) / pick([1, 10, 100])); res = qmul(val, Q(1000)); from = 'kg'; to = 'g'; meth = '1 kg = 1' + NB + '000 g : ' + show(val) + ' × 1' + NB + '000 = ' + show(res) + ' g.'; }
      else { val = Q(pick([ri(1, 9) * 100, ri(1, 99) * 10, ri(1, 9) * 1000 + ri(1, 9) * 100, 50, 250, 750])); res = qmul(val, Q(1, 1000)); from = 'g'; to = 'kg'; meth = '1' + NB + '000 g = 1 kg : ' + show(val) + ' ÷ 1' + NB + '000 = ' + show(res) + ' kg.'; }
      html = 'Compléter : ' + show(val) + ' ' + from + ' = … ' + to;
    } else if (v === 'litre') {
      var pr = pick([['dm³', 'L', 1], ['L', 'dm³', 1], ['m³', 'L', 1000], ['L', 'm³', 1 / 1000], ['cm³', 'mL', 1], ['mL', 'cm³', 1]]);
      val = pr[2] < 1 ? Q(pick([500, 1500, 250, 2000, 3500, 750])) : D(pick([ri(1, 9), ri(11, 99) / 10, ri(1, 9) / 10, 250]));
      res = pr[2] < 1 ? qmul(val, Q(1, 1000)) : qmul(val, Q(pr[2])); from = pr[0]; to = pr[1];
      meth = (pr[2] === 1 ? '1 ' + (from === 'cm³' || from === 'mL' ? 'cm³ = 1 mL' : 'dm³ = 1 L') : '1 m³ = 1' + NB + '000 L') + ', donc ' + show(val) + ' ' + from + ' = ' + show(res) + ' ' + to + '.';
      html = 'Compléter : ' + show(val) + ' ' + from + ' = … ' + to;
    } else {
      var d = pick(['h2m', 'h2m', 'hm2m', 'm2h', 'm2s', 'j2h']);
      if (d === 'h2m') { val = D(pick([0.5, 1.5, 2.5, 0.25, 0.75, 1.25, 1.2, 0.3, 2.1, 3.5, 0.1])); res = qmul(val, Q(60)); from = 'h'; to = 'min'; html = 'Compléter : ' + show(val) + ' h = … min'; meth = '1 h = 60 min, donc ' + show(val) + ' × 60 = ' + show(res) + ' min. Attention : ' + show(val) + ' h ≠ ' + show(val).replace(',', ' h ') + ' min.'; if (qv(val) < 1 && qv(val) * 10 % 1 === 0) meth = '1 h = 60 min, donc ' + show(val) + ' × 60 = ' + show(res) + ' min.'; }
      else if (d === 'hm2m') { var hh = ri(1, 4), mm = ri(1, 11) * 5; res = Q(hh * 60 + mm); from = ''; to = 'min'; html = 'Compléter : ' + hh + ' h ' + mm + ' min = … min'; meth = hh + ' h = ' + hh * 60 + ' min, donc ' + hh * 60 + ' + ' + mm + ' = ' + (hh * 60 + mm) + ' min.'; }
      else if (d === 'm2h') { val = Q(pick([30, 90, 150, 45, 15, 120, 180, 210, 75])); res = qmul(val, Q(1, 60)); to = 'h'; html = 'Compléter : ' + show(val) + ' min = … h (écriture décimale)'; meth = '60 min = 1 h, donc ' + show(val) + ' ÷ 60 = ' + show(res) + ' h.'; }
      else if (d === 'm2s') { val = D(pick([2, 3, 5, 1.5, 0.5, 10, 2.5])); res = qmul(val, Q(60)); to = 's'; html = 'Compléter : ' + show(val) + ' min = … s'; meth = '1 min = 60 s, donc ' + show(val) + ' × 60 = ' + show(res) + ' s.'; }
      else { val = D(pick([2, 3, 0.5, 1.5, 7, 0.25])); res = qmul(val, Q(24)); to = 'h'; html = 'Compléter : ' + show(val) + ' jour' + (qv(val) > 1 ? 's' : '') + ' = … h'; meth = '1 jour = 24 h, donc ' + show(val) + ' × 24 = ' + show(res) + ' h.'; }
    }
    return { html: html, ans: { k: 'num', q: res, form: 'any' }, suf: to, corr: strong(show(res) + ' ' + to), meth: meth };
  }
},
{
  id: 'solides', titre: 'Reconnaître des solides', ex: 'cube, pavé, prisme, cylindre, pyramide, cône', req: [],
  gen: function (c) {
    var list = ['cube', 'pave', 'prisme', 'cylindre']; if (c.has('pyr')) list.push('pyramide', 'cone');
    var s = pick(list), b = '';
    function box(x0, y0, w, h, d) {
      var dx = d * 0.55, dy = -d * 0.42, F1 = [x0, y0 + h], F2 = [x0 + w, y0 + h], F3 = [x0 + w, y0], F4 = [x0, y0];
      var B = [F1, F2, F3, F4].map(function (p) { return add(p, [dx, dy]); });
      return PG([F1, F2, F3, F4]) + PL([F4, B[3], B[2], F3]) + PL([F2, B[1], B[2]]) + L(B[0], B[1], 'hid') + L(B[0], B[3], 'hid') + L(B[0], F1, 'hid');
    }
    if (s === 'cube') b = box(70, 90, 120, 120, 120);
    if (s === 'pave') b = box(40, 110, 170, 90, 110);
    if (s === 'prisme') { var T1 = [50, 200], T2 = [170, 200], T3 = [90, 100], o = [110, -55], U1 = add(T1, o), U2 = add(T2, o), U3 = add(T3, o);
      b = PG([T1, T2, T3]) + L(T3, U3) + L(T2, U2) + L(U3, U2) + L(U1, U2, 'hid') + L(U1, U3, 'hid') + L(U1, T1, 'hid'); }
    if (s === 'cylindre') b = '<ellipse cx="150" cy="60" rx="80" ry="22" class="ln"/>' + L([70, 60], [70, 200]) + L([230, 60], [230, 200]) +
      '<path d="M70 200A80 22 0 0 0 230 200" class="ln"/><path d="M70 200A80 22 0 0 1 230 200" class="hid"/>';
    if (s === 'cone') b = L([150, 30], [65, 200]) + L([150, 30], [235, 200]) + '<path d="M65 200A85 24 0 0 0 235 200" class="ln"/><path d="M65 200A85 24 0 0 1 235 200" class="hid"/>';
    if (s === 'pyramide') { var P1 = [50, 210], P2 = [200, 210], P3 = [260, 160], P4 = [110, 160], S = [150, 30];
      b = PL([P1, P2, P3]) + L(S, P1) + L(S, P2) + L(S, P3) + L(P3, P4, 'hid') + L(P4, P1, 'hid') + L(S, P4, 'hid'); }
    var fig = svg(300, 250, b, 'small');
    var counts = { cube: [6, 8, 12], pave: [6, 8, 12], prisme: [5, 6, 9], pyramide: [5, 5, 8] };
    var full = { cube: 'un cube', pave: 'un pavé droit', prisme: 'un prisme droit (à base triangulaire)', cylindre: 'un cylindre', pyramide: 'une pyramide (à base carrée)', cone: 'un cône' }[s];
    if (counts[s] && chance(0.35)) {
      var w = ri(0, 2), what = ['faces', 'sommets', 'arêtes'][w], n = counts[s][w];
      return { html: 'Combien ce solide a-t-il de ' + what + ' ?' + fig, ans: { k: 'num', q: Q(n), form: 'int' }, corr: strong(n + ' ' + what),
        meth: 'C’est ' + full + ' : ' + counts[s][0] + ' faces, ' + counts[s][1] + ' sommets et ' + counts[s][2] + ' arêtes (les arêtes cachées sont en pointillés).' };
    }
    var need = { cube: [['cube']], pave: [['pave', 'parallelepipede']], prisme: [['prisme']], cylindre: [['cylindre']], pyramide: [['pyramide']], cone: [['cone']] }[s];
    var o = s === 'cube' ? { near: [{ has: 'pave', msg: 'C’est vrai, mais on peut être plus précis : toutes ses faces sont des carrés.' }] } : s === 'pave' ? { forbid: ['cube'] } : {};
    return { html: 'Quel est le nom de ce solide ?' + fig, ans: words(need, o), sample: full.replace(/^une? /, '').replace(/ \(.*/, ''),
      corr: 'C’est ' + strong(full) + '.', meth: {
        cube: 'Six faces carrées.', pave: 'Six faces rectangulaires.', prisme: 'Deux bases triangulaires superposables reliées par des faces rectangulaires.',
        cylindre: 'Deux disques superposables reliés par une surface courbe.', pyramide: 'Une base (ici un quadrilatère) et des faces triangulaires qui se rejoignent au sommet.', cone: 'Une base en forme de disque et un sommet.' }[s] };
  }
},
{
  id: 'perim', titre: 'Périmètre d’un polygone ou d’un cercle', ex: 'cercle de rayon 5 cm : 10π cm', req: [],
  gen: function () {
    var v = pick(['rect', 'carre', 'poly', 'poly', 'cercle', 'diam']), html, ans, corr, meth;
    var dec = function () { return D(ri(4, 19) / 2); };
    if (v === 'rect') { var Lg = dec(), l; do { l = dec(); } while (H.qeq(l, Lg)); var p = qmul(H.qadd(Lg, l), Q(2)); html = 'Calculer le périmètre d’un rectangle de longueur ' + cm(Lg) + ' et de largeur ' + cm(l) + '.'; ans = { k: 'num', q: p, form: 'any' }; corr = strong(cm(p)); meth = '2 × (' + f(Lg) + ' + ' + f(l) + ') = 2 × ' + f(H.qadd(Lg, l)) + ' = ' + f(p) + ' cm.'; }
    else if (v === 'carre') { var cc = dec(), p2 = qmul(cc, Q(4)); html = 'Calculer le périmètre d’un carré de côté ' + cm(cc) + '.'; ans = { k: 'num', q: p2, form: 'any' }; corr = strong(cm(p2)); meth = '4 × ' + f(cc) + ' = ' + f(p2) + ' cm.'; }
    else if (v === 'poly') {
      var n = pick([3, 4, 5]), pts = [], R = 90;
      for (var i = 0; i < n; i++) { var a = (i / n) * 2 * Math.PI + ri(-15, 15) * Math.PI / 180, rr = R * (0.75 + Math.random() * 0.35); pts.push([150 + rr * Math.cos(a), 120 + rr * Math.sin(a)]); }
      var lens = pts.map(function () { return D(ri(4, 19) / 2); }), c = cent(pts), b = PG(pts), tot = lens.reduce(function (s, x) { return H.qadd(s, x); }, Q(0));
      pts.forEach(function (p, k) { b += side(p, pts[(k + 1) % n], c, cm(lens[k]), 18); });
      html = 'Calculer le périmètre de ce polygone (les longueurs sont en centimètres).' + svgFit(pts, b, 50);
      ans = { k: 'num', q: tot, form: 'any' }; corr = strong(cm(tot)); meth = 'On additionne les longueurs de tous les côtés : ' + lens.map(f).join(' + ') + ' = ' + f(tot) + ' cm.';
    } else {
      var r = ri(2, 12), dm = 2 * r, isD = v === 'diam';
      html = 'Donner la valeur exacte du périmètre d’un cercle de ' + (isD ? 'diamètre ' + cm(dm) : 'rayon ' + cm(r)) + '.';
      ans = { k: 'expr', ref: dm + '*pi', form: 'any', pi: true }; corr = strong(dm + 'π cm') + ' (≈ ' + f(Math.round(dm * Math.PI * 10) / 10) + ' cm)';
      meth = isD ? 'Périmètre = π × diamètre = π × ' + dm + ' = ' + dm + 'π cm.' : 'Périmètre = 2 × π × rayon = 2 × π × ' + r + ' = ' + dm + 'π cm.';
    }
    return { html: html, ans: ans, suf: ans.k === 'num' ? 'cm' : 'cm', corr: corr, meth: meth };
  }
},
{
  id: 'aires', titre: 'Aire d’un triangle, d’un rectangle, d’un disque', ex: 'disque de rayon 3 cm : 9π cm²', req: [],
  gen: function () {
    var v = pick(['rect', 'tri', 'tri', 'trirect', 'disque', 'disque', 'carre']), html, ans, corr, meth;
    if (v === 'rect') { var Lg = ri(3, 12), l = D(ri(3, 19) / 2), a = qmul(Q(Lg), l); html = 'Calculer l’aire d’un rectangle de longueur ' + cm(Lg) + ' et de largeur ' + cm(l) + '.'; ans = a; meth = 'Aire = longueur × largeur = ' + Lg + ' × ' + f(l) + ' = ' + f(a) + ' cm².'; }
    else if (v === 'carre') { var cc = ri(2, 12), a2 = Q(cc * cc); html = 'Calculer l’aire d’un carré de côté ' + cm(cc) + '.'; ans = a2; meth = 'Aire = côté × côté = ' + cc + ' × ' + cc + ' = ' + cc * cc + ' cm².'; }
    else if (v === 'tri') {
      var bs = ri(3, 12), h = ri(2, 10), A0 = [40, 200], B0 = [280, 200], xs = ri(90, 230), C0 = [xs, 60], Hf = [xs, 200];
      var b = PG([A0, B0, C0]) + L(C0, Hf, 'hid') + right(Hf, B0, C0, 11) + T([160, 222], cm(bs)) + T([xs + 8, 130], cm(h), null, 'start');
      html = 'Calculer l’aire de ce triangle.' + svg(320, 240, b, 'small'); ans = Q(bs * h, 2);
      meth = 'Aire = base × hauteur ÷ 2 = ' + bs + ' × ' + h + ' ÷ 2 = ' + f(ans) + ' cm².';
    } else if (v === 'trirect') {
      var a1 = ri(3, 12), b1 = ri(3, 12), ps = rightTri(a1, b1, 14), cT = cent(ps);
      var bb = PG(ps) + right(ps[0], ps[1], ps[2]) + side(ps[0], ps[1], cT, cm(a1), 18) + side(ps[0], ps[2], cT, cm(b1), 18);
      html = 'Calculer l’aire de ce triangle rectangle.' + svgFit(ps, bb, 46, 'small'); ans = Q(a1 * b1, 2);
      meth = 'Les deux côtés de l’angle droit sont une base et la hauteur associée : ' + a1 + ' × ' + b1 + ' ÷ 2 = ' + f(ans) + ' cm².';
    } else {
      var r = ri(2, 10), isD = chance(0.3);
      html = 'Donner la valeur exacte de l’aire d’un disque de ' + (isD ? 'diamètre ' + cm(2 * r) : 'rayon ' + cm(r)) + '.';
      return { html: html, ans: { k: 'expr', ref: r * r + '*pi', form: 'any', pi: true }, suf: 'cm²', corr: strong(r * r + 'π cm²') + ' (≈ ' + f(Math.round(r * r * Math.PI * 10) / 10) + ' cm²)',
        meth: (isD ? 'Le rayon vaut ' + 2 * r + ' ÷ 2 = ' + r + ' cm. ' : '') + 'Aire = π × rayon² = π × ' + r + '² = ' + r * r + 'π cm².' };
    }
    return { html: html, ans: { k: 'num', q: ans, form: 'any' }, suf: 'cm²', corr: strong(f(ans) + ' cm²'), meth: meth };
  }
},
{
  id: 'volumes', titre: 'Volume d’un cube, d’un pavé, d’un prisme, d’un cylindre', ex: 'cylindre : π × r² × h', req: [],
  gen: function () {
    var v = pick(['cube', 'pave', 'pave', 'prisme', 'cyl', 'cyl']), html, V, meth;
    if (v === 'cube') { var a = ri(2, 6); V = a * a * a; html = 'Calculer le volume d’un cube d’arête ' + cm(a) + '.'; meth = 'Volume = arête × arête × arête = ' + a + ' × ' + a + ' × ' + a + ' = ' + V + ' cm³.'; }
    else if (v === 'pave') { var l1 = ri(2, 10), l2 = ri(2, 6), l3 = ri(2, 5); V = l1 * l2 * l3; html = 'Calculer le volume d’un pavé droit de dimensions ' + l1 + ' cm, ' + l2 + ' cm et ' + l3 + ' cm.'; meth = 'Volume = longueur × largeur × hauteur = ' + l1 + ' × ' + l2 + ' × ' + l3 + ' = ' + V + ' cm³.'; }
    else if (v === 'prisme') { var p = ri(2, 8), q = 2 * ri(1, 4), h = ri(2, 10), B = p * q / 2; V = B * h; html = 'Un prisme droit a pour base un triangle rectangle dont les côtés de l’angle droit mesurent ' + cm(p) + ' et ' + cm(q) + '. Sa hauteur est ' + cm(h) + '. Calculer son volume.'; meth = 'Aire de la base : ' + p + ' × ' + q + ' ÷ 2 = ' + B + ' cm². Volume = aire de la base × hauteur = ' + B + ' × ' + h + ' = ' + V + ' cm³.'; }
    else { var r = ri(1, 5), hh = ri(2, 10), k = r * r * hh;
      return { html: 'Donner la valeur exacte du volume d’un cylindre de rayon ' + cm(r) + ' et de hauteur ' + cm(hh) + '.', ans: { k: 'expr', ref: k + '*pi', form: 'any', pi: true }, suf: 'cm³',
        corr: strong(k + 'π cm³'), meth: 'Volume = aire de la base × hauteur = π × ' + r + '² × ' + hh + ' = ' + k + 'π cm³.' }; }
    return { html: html, ans: { k: 'num', q: Q(V), form: 'any' }, suf: 'cm³', corr: strong(V + ' cm³'), meth: meth };
  }
},
{
  id: 'pyth', titre: 'Théorème de Pythagore', ex: 'BC² = AB² + AC²', req: ['pyth'],
  gen: function () {
    var tr = pick([[3, 4, 5], [6, 8, 10], [5, 12, 13], [8, 15, 17], [9, 12, 15], [12, 16, 20], [7, 24, 25]]), v = pick(['hyp', 'hyp', 'leg', 'leg', 'eq', 'eq', 'rec']);
    var Ls = pick(LETTERS3), R = Ls[0], Pp = Ls[1], Qq = Ls[2], hyp = Pp + Qq;
    if (v === 'rec') {
      var ok = chance(0.5), s3 = ok ? tr.slice() : [tr[0], tr[1], tr[2] + pick([-1, 1])];
      return { html: 'Un triangle a des côtés de longueurs ' + s3[0] + ' cm, ' + s3[1] + ' cm et ' + s3[2] + ' cm. Est-il rectangle ?', ans: words([[ok ? 'oui' : 'non']], { forbid: [ok ? 'non' : 'oui'] }), sample: ok ? 'oui' : 'non',
        corr: strong(ok ? 'Oui' : 'Non') + ', il ' + (ok ? 'est' : 'n’est pas') + ' rectangle.',
        meth: 'On compare le carré du plus grand côté à la somme des carrés des deux autres : ' + s3[2] + '² = ' + s3[2] * s3[2] + ' et ' + s3[0] + '² + ' + s3[1] + '² = ' + (s3[0] * s3[0] + s3[1] * s3[1]) + '. ' + (ok ? 'Égalité : il est rectangle (réciproque du théorème de Pythagore).' : 'Pas d’égalité : il n’est pas rectangle.') };
    }
    var ps = rightTri(tr[0], tr[1], 150 / tr[2]), c = cent(ps), b = PG(ps) + right(ps[0], ps[1], ps[2]);
    b += lab(ps[0], c, R) + lab(ps[1], c, Pp) + lab(ps[2], c, Qq);
    if (v === 'eq') return { html: 'Écrire l’égalité de Pythagore dans le triangle ' + R + Pp + Qq + ' rectangle en ' + R + '.' + svgFit(ps, b, 40, 'small'),
      ans: { k: 'pyeq', h: hyp, l: [R + Pp, R + Qq] }, sample: hyp + '²=' + R + Pp + '²+' + R + Qq + '²',
      corr: strong(hyp + '² = ' + R + Pp + '² + ' + R + Qq + '²'), meth: 'Le carré de l’hypoténuse [' + hyp + '] (côté opposé à l’angle droit) est égal à la somme des carrés des deux autres côtés.' };
    var res, html, meth;
    if (v === 'hyp') {
      b += side(ps[0], ps[1], c, cm(tr[0]), 18) + side(ps[0], ps[2], c, cm(tr[1]), 18);
      res = tr[2]; html = 'Calculer la longueur ' + hyp + '.';
      meth = hyp + '² = ' + R + Pp + '² + ' + R + Qq + '² = ' + tr[0] + '² + ' + tr[1] + '² = ' + tr[0] * tr[0] + ' + ' + tr[1] * tr[1] + ' = ' + tr[2] * tr[2] + ', donc ' + hyp + ' = √' + tr[2] * tr[2] + ' = ' + tr[2] + ' cm.';
    } else {
      b += side(ps[1], ps[2], c, cm(tr[2]), 18) + side(ps[0], ps[1], c, cm(tr[0]), 18);
      res = tr[1]; html = 'Calculer la longueur ' + R + Qq + '.';
      meth = hyp + '² = ' + R + Pp + '² + ' + R + Qq + '², donc ' + R + Qq + '² = ' + tr[2] + '² − ' + tr[0] + '² = ' + tr[2] * tr[2] + ' − ' + tr[0] * tr[0] + ' = ' + tr[1] * tr[1] + ' et ' + R + Qq + ' = ' + tr[1] + ' cm.';
    }
    return { html: 'Le triangle ' + R + Pp + Qq + ' est rectangle en ' + R + '. ' + html + svgFit(ps, b, 46, 'small'), ans: { k: 'num', q: Q(res), form: 'any' }, suf: 'cm',
      corr: strong(cm(res)), meth: meth.replace(/ − /g, M) };
  }
},
{
  id: 'thales', titre: 'Théorème de Thalès (triangles emboîtés)', ex: fr('AB', 'AE') + ' = ' + fr('AC', 'AD') + ' = ' + fr('BC', 'DE'), req: ['thales'],
  gen: function () {
    var k = pick([2, 3, 2, 4, 1.5, 2.5]), Ls = pick([['A', 'B', 'C', 'D', 'E'], ['O', 'M', 'N', 'R', 'S'], ['S', 'E', 'F', 'G', 'H']]);
    var a = Ls[0], b = Ls[1], c = Ls[2], d = Ls[3], e = Ls[4];
    var AB, BC; do { AB = ri(2, 8); BC = ri(2, 7); } while (!Number.isInteger(AB * k * 2) || !Number.isInteger(BC * k * 2));
    var AE = AB * k, DE = BC * k, A0 = [30, 200], E0 = [330, 200], D0 = [260, 40], B0 = add(A0, mul(sub(E0, A0), 1 / k)), C0 = add(A0, mul(sub(D0, A0), 1 / k));
    var fig = L(A0, E0) + L(A0, D0) + L(D0, E0) + L(B0, C0) + T(add(A0, [-12, 4]), a, 'it') + T(add(B0, [0, 18]), b, 'it') + T(add(E0, [10, 10]), e, 'it') + T(add(C0, [-8, -16]), c, 'it') + T(add(D0, [0, -16]), d, 'it');
    var v = pick(['AE', 'DE', 'AB']), given, ask, res, meth;
    var pre = 'Dans le triangle ' + a + d + e + ', ' + b + ' est sur [' + a + e + '], ' + c + ' est sur [' + a + d + '] et les droites (' + b + c + ') et (' + d + e + ') sont parallèles. ';
    var eqs = fr(a + b, a + e) + ' = ' + fr(a + c, a + d) + ' = ' + fr(b + c, d + e);
    if (v === 'AE') { given = a + b + ' = ' + cm(AB) + ', ' + b + c + ' = ' + cm(BC) + ' et ' + d + e + ' = ' + cm(DE) + '.'; ask = a + e; res = AE; meth = 'D’après le théorème de Thalès, ' + eqs + '. Donc ' + fr(f(AB), a + e) + ' = ' + fr(f(BC), f(DE)) + ' et ' + a + e + ' = ' + f(AB) + ' × ' + f(DE) + ' ÷ ' + f(BC) + ' = ' + f(AE) + ' cm.'; }
    else if (v === 'DE') { given = a + b + ' = ' + cm(AB) + ', ' + a + e + ' = ' + cm(AE) + ' et ' + b + c + ' = ' + cm(BC) + '.'; ask = d + e; res = DE; meth = 'D’après le théorème de Thalès, ' + eqs + '. Donc ' + fr(f(AB), f(AE)) + ' = ' + fr(f(BC), d + e) + ' et ' + d + e + ' = ' + f(AE) + ' × ' + f(BC) + ' ÷ ' + f(AB) + ' = ' + f(DE) + ' cm.'; }
    else { given = a + e + ' = ' + cm(AE) + ', ' + b + c + ' = ' + cm(BC) + ' et ' + d + e + ' = ' + cm(DE) + '.'; ask = a + b; res = AB; meth = 'D’après le théorème de Thalès, ' + eqs + '. Donc ' + fr(a + b, f(AE)) + ' = ' + fr(f(BC), f(DE)) + ' et ' + a + b + ' = ' + f(AE) + ' × ' + f(BC) + ' ÷ ' + f(DE) + ' = ' + f(AB) + ' cm.'; }
    return { html: pre + given + ' Calculer ' + ask + '.' + svg(360, 230, fig), ans: { k: 'num', q: D(res), form: 'any' }, suf: 'cm', corr: ask + ' = ' + strong(cm(D(res))), meth: meth };
  }
},
{
  id: 'cos', titre: 'Cosinus d’un angle aigu', ex: 'cos = côté adjacent ÷ hypoténuse', req: ['cos'],
  gen: function () {
    var tr = pick([[3, 4, 5], [6, 8, 10], [5, 12, 13], [8, 15, 17], [9, 12, 15]]), Ls = pick(LETTERS3), R = Ls[0], Pp = Ls[1], Qq = Ls[2];
    var ps = rightTri(tr[0], tr[1], 150 / tr[2]), c = cent(ps), b = PG(ps) + right(ps[0], ps[1], ps[2]) + arcAt(ps[1], ps[0], ps[2], 30);
    b += lab(ps[0], c, R) + lab(ps[1], c, Pp) + lab(ps[2], c, Qq);
    var angle = 'cos(' + ang(Qq + Pp + R) + ')';
    if (chance(0.5)) return { html: 'Le triangle ' + R + Pp + Qq + ' est rectangle en ' + R + '. Exprimer ' + angle + ' à l’aide des longueurs du triangle.' + svgFit(ps, b, 40, 'small'),
      ans: { k: 'ratio', n: Pp + R, d: Pp + Qq }, corr: angle + ' = ' + strong(fr(Pp + R, Pp + Qq)),
      meth: 'cosinus = côté adjacent ÷ hypoténuse. Le côté adjacent à l’angle en ' + Pp + ' est [' + Pp + R + '] ; l’hypoténuse est [' + Pp + Qq + '].' };
    b += side(ps[0], ps[1], c, cm(tr[0]), 18) + side(ps[1], ps[2], c, cm(tr[2]), 18) + side(ps[0], ps[2], c, cm(tr[1]), 18);
    var val = Q(tr[0], tr[2]);
    return { html: 'Le triangle ' + R + Pp + Qq + ' est rectangle en ' + R + '. Donner la valeur exacte de ' + angle + '.' + svgFit(ps, b, 46, 'small'),
      ans: { k: 'num', q: val, form: 'any' }, corr: angle + ' = ' + strong(fr(tr[0], tr[2])) + (H.isDec(val) ? ' = ' + f(val) : ''),
      meth: 'cos(' + ang(Qq + Pp + R) + ') = ' + fr(Pp + R, Pp + Qq) + ' = ' + fr(tr[0], tr[2]) + (val.d !== tr[2] ? ' = ' + fr(val.n, val.d) : '') + ' (côté adjacent ÷ hypoténuse).' };
  }
},
{
  id: 'transfo', titre: 'Symétries et translations', ex: 'image d’une figure sur quadrillage', req: [],
  gen: function (c) {
    var U = 24, GW = 16, GH = 10, sp = function (p) { return [12 + p[0] * U, 12 + p[1] * U]; };
    var kinds = ['axe', 'centre']; if (c.has('transl')) kinds.push('trans');
    var asked = pick(kinds), tries = 0, ok = false, base, ax, O, Mv, Nv, imgs;
    var inside = function (ps) { return ps.every(function (p) { return p[0] >= 0 && p[0] <= GW && p[1] >= 0 && p[1] <= GH; }); };
    var cc = function (ps) { return cent(ps); };
    while (!ok && tries++ < 800) {
      var bx = ri(1, 6), by = ri(1, 6);
      base = [[bx, by], [bx + ri(2, 3), by + ri(0, 1)], [bx + ri(0, 1), by + ri(2, 3)]];
      if (chance(0.5)) base.push([bx + ri(2, 3), by + ri(2, 3)]);
      ax = ri(6, 10); O = [ri(5, 11), ri(3, 7)]; Mv = [ri(1, 4), ri(0, 3)]; Nv = [Mv[0] + nz(-6, 7), Mv[1] + nz(-3, 4)];
      var vec = sub(Nv, Mv);
      var IM = {
        axe: base.map(function (p) { return [2 * ax - p[0], p[1]]; }),
        centre: base.map(function (p) { return [2 * O[0] - p[0], 2 * O[1] - p[1]]; }),
        trans: base.map(function (p) { return add(p, vec); }),
        autre: base.map(function (p) { return add(p, [vec[1] || 3, -vec[0] || 2]); })
      };
      var use = ['axe', 'centre', c.has('transl') ? 'trans' : 'autre'];
      if (chance(0.5)) use.push(c.has('transl') ? 'autre' : 'trans');
      imgs = use.map(function (k) { return { k: k, ps: IM[k] }; });
      var all = imgs.map(function (x) { return x.ps; }).concat([base]);
      ok = all.every(inside) && all.every(function (p1, i) { return all.every(function (p2, j) { return i >= j || len(sub(cc(p1), cc(p2))) >= 2.2; }); });
      // la figure ne doit pas être sa propre image
    }
    var b = '';
    for (var i = 0; i <= GW; i++) b += L(sp([i, 0]), sp([i, GH]), 'grid');
    for (var j = 0; j <= GH; j++) b += L(sp([0, j]), sp([GW, j]), 'grid');
    imgs = shuffle(imgs);
    b += PG(base.map(sp), 'soft') + T(sp(cc(base)), 'F', 'it');
    imgs.forEach(function (x, k) { b += PG(x.ps.map(sp), 'gr') + T(sp(cc(x.ps)), String(k + 1)); });
    var label = { axe: 'la symétrie d’axe (d)', centre: 'la symétrie de centre O', trans: 'la translation qui transforme M en N' }[asked];
    b += L(sp([ax, -0.3]), sp([ax, GH + 0.3]), 'acc') + T(add(sp([ax, 0]), [14, 8]), '(d)', 'it');
    b += DOT(sp(O), 4) + T(add(sp(O), [10, -10]), 'O', 'it');
    if (c.has('transl')) b += CROSS(sp(Mv)) + T(add(sp(Mv), [10, -10]), 'M', 'it') + CROSS(sp(Nv)) + T(add(sp(Nv), [10, -10]), 'N', 'it');
    var good = imgs.findIndex(function (x) { return x.k === asked; }) + 1;
    return { html: 'Quelle figure est l’image de la figure F par ' + label + ' ? (donner son numéro)' + svg(GW * U + 24, GH * U + 24, b, 'wide'),
      ans: { k: 'num', q: Q(good), form: 'int' }, corr: 'C’est la figure ' + strong(good) + '.',
      meth: { axe: 'Par la symétrie d’axe (d), la figure est « retournée » de l’autre côté de (d), à la même distance de l’axe.',
        centre: 'Par la symétrie de centre O, chaque point est envoyé de l’autre côté de O, à la même distance : la figure fait un demi-tour autour de O.',
        trans: 'Par la translation, la figure glisse, sans tourner, du même déplacement que de M à N.' }[asked] };
  }
}
];

var th = A.THEMES.filter(function (t) { return t.id === 'geo'; })[0];
th.gens.push.apply(th.gens, GEO);
A.G = { n1: n1, add: add, sub: sub, mul: mul, L: L, PG: PG, PL: PL, T: T, DOT: DOT, CROSS: CROSS, svg: svg, svgFit: svgFit, words: words, cm: cm };
})(this);
