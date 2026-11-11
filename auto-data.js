/* Automatismes du DNB – thèmes « Données et probabilités », « Proportionnalité et fonctions », « Algorithmique et programmation ». */
(function (root) {
'use strict';
var A = (typeof module !== 'undefined' && module.exports) ? require('./auto-gen.js') : root.AUTO;
if (typeof module !== 'undefined' && module.exports) require('./auto-geo.js');
var H = A.H, G = A.G, ri = H.ri, pick = H.pick, chance = H.chance, nz = H.nz, shuffle = H.shuffle, Q = H.Q, D = H.D, f = H.f, fp = H.fp, fr = H.fr,
  frq = H.frq, nq = H.nq, strong = H.strong, X = H.X, P = H.P, M = H.M, MINUS = H.MINUS, qmul = H.qmul, qadd = H.qadd, qsub = H.qsub, qdiv = H.qdiv, qv = H.qv, NB = H.NB, V = H.V;
var L = G.L, PL = G.PL, T = G.T, DOT = G.DOT, svg = G.svg, words = G.words, add = G.add;
function themeGens(id) { return A.THEMES.filter(function (t) { return t.id === id; })[0].gens; }
function frIrr(n, d) { var q = Q(n, d); return fr(n, d) + (q.d !== d ? ' = ' + frq(q) : ''); }
function list(xs) { return xs.map(f).join(' ; '); }
function parseList(s) {
  var parts = String(s).replace(/\bet\b/g, ';').split(/[;/]|\s{2,}/).map(function (x) { return x.trim(); }).filter(Boolean);
  if (parts.length === 1 && /\s/.test(parts[0])) parts = parts[0].split(/\s+/);
  var out = []; for (var i = 0; i < parts.length; i++) { var p = A.parseNumber(parts[i]); if (!p) return null; out.push(p.q); }
  return out;
}

/* grille + repère pour les graphiques */
function axes(o) { // o : x0,x1,y0,y1,ux,uy,stepX,stepY,labX,labY (fonctions de libellé), titreX, titreY
  var W = (o.x1 - o.x0) * o.ux + 70, Hh = (o.y1 - o.y0) * o.uy + 56, ox = 46 - o.x0 * o.ux, oy = 16 + o.y1 * o.uy, b = '';
  var sp = function (x, y) { return [ox + x * o.ux, oy - y * o.uy]; };
  for (var x = o.x0; x <= o.x1 + 1e-9; x += o.gx) b += L(sp(x, o.y0), sp(x, o.y1), 'grid');
  for (var y = o.y0; y <= o.y1 + 1e-9; y += o.gy) b += L(sp(o.x0, y), sp(o.x1, y), 'grid');
  var yA = Math.max(o.y0, Math.min(0, o.y1)), xA = Math.max(o.x0, Math.min(0, o.x1));
  b += L(sp(o.x0, yA), add(sp(o.x1, yA), [10, 0]), 'ax') + L(sp(xA, o.y0), add(sp(xA, o.y1), [0, -10]), 'ax');
  for (x = o.x0; x <= o.x1 + 1e-9; x += o.lx) if (Math.abs(x) > 1e-9 || o.zero) b += T(add(sp(x, yA), [0, 14]), f(Math.round(x * 100) / 100), 'lt');
  for (y = o.y0; y <= o.y1 + 1e-9; y += o.ly) if (Math.abs(y) > 1e-9) b += T(add(sp(xA, y), [-8, 0]), f(Math.round(y * 100) / 100), 'lt', 'end');
  if (!o.zero) b += T(add(sp(0, 0), [-8, 12]), '0', 'lt', 'end');
  if (o.tx) b += T(add(sp(o.x1, yA), [8, -14]), o.tx, 'lt', 'end');
  if (o.ty) b += T(add(sp(xA, o.y1), [8, -6]), o.ty, 'lt', 'start');
  return { sp: sp, b: b, W: W, H: Hh };
}

/* ======================= Données et probabilités ======================= */
var DATA = [
{
  id: 'proba', titre: 'Calculer une probabilité simple', ex: 'tirer une boule rouge', req: [],
  gen: function () {
    var v = pick(['sac', 'sac', 'de', 'contr', 'sac2']), html, q, meth, corr;
    if (v === 'sac' || v === 'sac2') {
      var cols = shuffle([['rouges', 'rouge'], ['noires', 'noire'], ['jaunes', 'jaune'], ['vertes', 'verte'], ['bleues', 'bleue']]).slice(0, 3), n = cols.map(function () { return ri(1, 9); }), tot = n[0] + n[1] + n[2];
      var desc = 'Un sac contient ' + cols.map(function (c, i) { return n[i] + ' boule' + (n[i] > 1 ? 's ' + c[0] : ' ' + c[1]); }).join(', ').replace(/, ([^,]*)$/, ' et $1') + ', indiscernables au toucher. On tire une boule au hasard.';
      if (v === 'sac') { var k = ri(0, 2); q = Q(n[k], tot); html = desc + ' Quelle est la probabilité de tirer une boule ' + cols[k][1] + ' ?'; meth = 'Il y a ' + n[k] + ' boule' + (n[k] > 1 ? 's' : '') + ' ' + cols[k][1] + (n[k] > 1 ? 's' : '') + ' sur ' + tot + ' boules en tout, chacune a la même chance d’être tirée : ' + frIrr(n[k], tot) + '.'; corr = frIrr(n[k], tot); }
      else { var k1 = ri(0, 2), s = tot - n[k1]; q = Q(s, tot); html = desc + ' Quelle est la probabilité de ne pas tirer une boule ' + cols[k1][1] + ' ?'; meth = 'Il y a ' + s + ' boules qui ne sont pas ' + cols[k1][1] + 's sur ' + tot + ' : ' + frIrr(s, tot) + ' (ou 1 − ' + fr(n[k1], tot) + ', événement contraire).'; corr = frIrr(s, tot); }
    } else if (v === 'de') {
      var ev = pick([['un nombre pair', 3], ['un multiple de 3', 2], ['un nombre supérieur ou égal à 5', 2], ['le 6', 1], ['un nombre inférieur à 3', 2], ['un nombre impair', 3], ['un nombre inférieur à 7', 6], ['le 7', 0]]);
      q = Q(ev[1], 6); html = 'On lance un dé équilibré à six faces numérotées de 1 à 6. Quelle est la probabilité d’obtenir ' + ev[0] + ' ?';
      corr = ev[1] === 0 ? '0 (événement impossible)' : ev[1] === 6 ? '1 (événement certain)' : frIrr(ev[1], 6);
      meth = ev[1] + ' issue' + (ev[1] > 1 ? 's' : '') + ' favorable' + (ev[1] > 1 ? 's' : '') + ' sur 6 issues équiprobables.';
    } else {
      if (chance(0.5)) { var p = ri(1, 9); q = Q(10 - p, 10); html = 'La probabilité qu’un événement A se réalise est 0,' + p + '. Quelle est la probabilité de l’événement contraire « non A » ?'; corr = f(q); meth = 'P(non A) = 1 − P(A) = 1 − 0,' + p + ' = ' + f(q) + '.'; }
      else { var d = ri(3, 12), nn = ri(1, d - 1); q = Q(d - nn, d); html = 'La probabilité qu’un événement A se réalise est ' + fr(nn, d) + '. Quelle est la probabilité de l’événement contraire « non A » ?'; corr = frIrr(d - nn, d); meth = 'P(non A) = 1 − ' + fr(nn, d) + ' = ' + fr(d, d) + ' − ' + fr(nn, d) + ' = ' + frIrr(d - nn, d) + '.'; }
    }
    return { html: html, ans: { k: 'num', q: q, form: 'any', pct: true }, corr: strong(corr), meth: meth.replace(/ − /g, M) };
  }
},
{
  id: 'freq', titre: 'Exprimer une fréquence', ex: '10 élèves sur 25 : ' + fr(10, 25) + ' = 0,4 = 40 %', req: [],
  gen: function () {
    var tot = pick([20, 25, 50, 10, 40, 200, 30]), n; do { n = ri(1, tot - 1); } while ((n * 100) % tot !== 0);
    var ctx = pick([['élèves d’une classe', 'viennent au collège à vélo'], ['personnes interrogées', 'préfèrent le chocolat noir'], ['lancers', 'ont donné « pile »'], ['spectateurs', 'sont venus en famille']]);
    var pc = chance(0.4), q = Q(n, tot);
    var html = 'Sur ' + tot + ' ' + ctx[0] + ', ' + n + ' ' + ctx[1] + '. ' + (pc ? 'Exprimer cette fréquence en pourcentage.' : 'Quelle est la fréquence correspondante ?');
    return { html: html, ans: pc ? { k: 'num', q: qmul(q, Q(100)), form: 'any' } : { k: 'num', q: q, form: 'any', pct: true }, suf: pc ? '%' : undefined,
      corr: strong(pc ? f(qmul(q, Q(100))) + ' %' : fr(n, tot)) + (pc ? '' : ' = ' + f(q) + ' = ' + f(qmul(q, Q(100))) + ' %'),
      meth: 'Fréquence = effectif ÷ effectif total = ' + fr(n, tot) + ' = ' + f(q) + (pc ? ', soit ' + f(qmul(q, Q(100))) + ' %.' : '.') };
  }
},
{
  id: 'moy', titre: 'Calculer une moyenne', ex: 'moyenne de 12 ; 15 ; 8 ; 13', req: [],
  gen: function (c) {
    var weighted = c.lv === '3e' && chance(0.3);
    if (weighted) {
      var vals = shuffle([8, 10, 12, 14, 15, 16, 9, 11]).slice(0, 3).sort(function (a, b) { return a - b; }), eff, S, N;
      do { eff = vals.map(function () { return ri(1, 5); }); N = eff.reduce(function (s, x) { return s + x; }, 0); S = vals.reduce(function (s, x, i) { return s + x * eff[i]; }, 0); } while (!H.isDec(Q(S, N)) || Q(S, N).d > 10);
      var tbl = '<table class="tbl"><tr><th>Note</th>' + vals.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr><tr><th>Effectif</th>' + eff.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr></table>';
      return { html: 'Voici les notes obtenues par un groupe d’élèves. Calculer la note moyenne.' + tbl, ans: { k: 'num', q: Q(S, N), form: 'any' }, corr: strong(f(Q(S, N))),
        meth: 'Moyenne = (' + vals.map(function (x, i) { return x + ' × ' + eff[i]; }).join(' + ') + ') ÷ ' + N + ' = ' + S + ' ÷ ' + N + ' = ' + f(Q(S, N)) + '.' };
    }
    var n = ri(4, 6), m = ri(c.has('relx') && chance(0.3) ? -3 : 6, c.has('relx') && chance(0.3) ? 4 : 15), xs, sum;
    do { xs = []; for (var i = 0; i < n - 1; i++) xs.push(m + nz(-5, 5)); var last = n * m - xs.reduce(function (s, x) { return s + x; }, 0) + (c.lv === '3e' && chance(0.4) ? pick([1, n / 2]) : 0); xs.push(last); sum = xs.reduce(function (s, x) { return s + x; }, 0); } while (Math.abs(xs[n - 1] - m) > 7 || !H.isDec(Q(sum, n)) || Q(sum, n).d > 10);
    xs = shuffle(xs); var q = Q(sum, n);
    return { html: 'Calculer la moyenne de cette série : ' + list(xs) + '.', ans: { k: 'num', q: q, form: 'any' }, corr: strong(f(q)),
      meth: 'On additionne toutes les valeurs puis on divise par leur nombre : (' + xs.map(fp).join(' + ') + ') ÷ ' + n + ' = ' + f(sum) + ' ÷ ' + n + ' = ' + f(q) + '.' };
  }
},
{
  id: 'med', titre: 'Déterminer une médiane (et l’étendue)', ex: 'médiane de 3 ; 7 ; 8 ; 12 ; 15', req: ['med'],
  gen: function () {
    var n = pick([5, 7, 6, 8, 5]), xs = []; for (var i = 0; i < n; i++) xs.push(ri(1, 25));
    var s = xs.slice().sort(function (a, b) { return a - b; });
    if (chance(0.2)) { var e = s[n - 1] - s[0]; return { html: 'Déterminer l’étendue de cette série : ' + list(xs) + '.', ans: { k: 'num', q: Q(e), form: 'any' }, corr: strong(e), meth: 'Étendue = plus grande valeur − plus petite valeur = ' + s[n - 1] + ' − ' + s[0] + ' = ' + e + '.'.replace(/ − /g, M) }; }
    var med, meth;
    if (n % 2) { med = Q(s[(n - 1) / 2]); meth = 'On range les valeurs dans l’ordre croissant : ' + list(s) + '. Il y a ' + n + ' valeurs, la médiane est la ' + (n + 1) / 2 + 'e : ' + f(med) + '.'; }
    else { med = Q(s[n / 2 - 1] + s[n / 2], 2); meth = 'On range les valeurs dans l’ordre croissant : ' + list(s) + '. Il y a ' + n + ' valeurs (nombre pair) : la médiane est entre la ' + n / 2 + 'e et la ' + (n / 2 + 1) + 'e valeur, ' + s[n / 2 - 1] + ' et ' + s[n / 2] + ', soit ' + f(med) + '.'; }
    return { html: 'Déterminer la médiane de cette série : ' + list(xs) + '.', ans: { k: 'num', q: med, form: 'any' }, corr: strong(f(med)), meth: meth };
  }
},
{
  id: 'lect', titre: 'Lire un diagramme ou un tableau', ex: 'diagramme en barres', req: [],
  gen: function () {
    var ctx = pick([['Nombre de frères et sœurs', [0, 1, 2, 3, 4], 'élèves'], ['Nombre de jours de sport par semaine', [1, 2, 3, 4, 5], 'élèves'], ['Pointure', [36, 37, 38, 39, 40], 'élèves']]);
    var cats = ctx[1], eff = cats.map(function () { return ri(1, 12); }), maxY = 12;
    var g = axes({ x0: 0, x1: cats.length, y0: 0, y1: maxY, ux: 60, uy: 16, gx: 100, gy: 1, lx: 100, ly: 2, ty: 'Effectif' });
    var b = g.b;
    cats.forEach(function (c, i) { var p0 = g.sp(i + 0.2, 0), p1 = g.sp(i + 0.8, eff[i]); b += '<rect x="' + p0[0] + '" y="' + p1[1] + '" width="' + (p1[0] - p0[0]) + '" height="' + (p0[1] - p1[1]) + '" class="bar"/>' + T(add(g.sp(i + 0.5, 0), [0, 14]), String(c), 'lt'); });
    b += T([g.W / 2, g.H - 4], ctx[0], 'lt');
    var fig = svg(g.W, g.H + 6, b, 'wide'), v = pick(['one', 'one', 'tot', 'atl']), k = ri(0, cats.length - 1), q, html, meth;
    var tot = eff.reduce(function (s, x) { return s + x; }, 0);
    if (v === 'one') { q = eff[k]; html = 'D’après le diagramme, combien d’' + ctx[2] + ' ont répondu ' + cats[k] + ' ?'; meth = 'On lit la hauteur de la barre « ' + cats[k] + ' » : ' + q + '.'; }
    else if (v === 'tot') { q = tot; html = 'D’après le diagramme, combien d’' + ctx[2] + ' ont été interrogés en tout ?'; meth = 'On additionne les effectifs de toutes les barres : ' + eff.join(' + ') + ' = ' + q + '.'; }
    else { var k2 = ri(1, cats.length - 2); q = eff.slice(k2).reduce(function (s, x) { return s + x; }, 0); html = 'D’après le diagramme, combien d’' + ctx[2] + ' ont répondu ' + cats[k2] + ' ou plus ?'; meth = 'On additionne les effectifs des barres à partir de ' + cats[k2] + ' : ' + eff.slice(k2).join(' + ') + ' = ' + q + '.'; }
    return { html: html + fig, ans: { k: 'num', q: Q(q), form: 'int' }, corr: strong(q), meth: meth };
  }
}
];

/* ======================= Proportionnalité et fonctions ======================= */
var FCT = [
{
  id: 'prop-rec', titre: 'Reconnaître une situation de proportionnalité', ex: 'tableau ou situation', req: [],
  gen: function () {
    if (chance(0.45)) {
      var s = pick([['Le prix payé pour des pommes vendues 2,50 € le kilo, en fonction de la masse achetée.', 1, 'Le prix est égal à 2,5 × la masse.'],
        ['Le périmètre d’un carré en fonction de la longueur de son côté.', 1, 'Le périmètre est égal à 4 × le côté.'],
        ['L’aire d’un carré en fonction de la longueur de son côté.', 0, 'Si le côté double, l’aire est multipliée par 4 : ce n’est pas proportionnel.'],
        ['La taille d’un enfant en fonction de son âge.', 0, 'La taille n’est pas multipliée par 2 quand l’âge double.'],
        ['Le prix d’une course de taxi avec une prise en charge de 4 € puis 1,50 € par kilomètre, en fonction de la distance.', 0, 'À cause de la prise en charge, 2 fois plus de kilomètres ne coûtent pas 2 fois plus cher.'],
        ['La distance parcourue par un cycliste roulant à vitesse constante, en fonction de la durée du trajet.', 1, 'Distance = vitesse × durée, la vitesse étant constante.'],
        ['La quantité d’essence consommée par une voiture à consommation constante, en fonction de la distance parcourue.', 1, 'Consommation constante : la quantité est proportionnelle à la distance.']]);
      return { html: s[0] + ' Est-ce une situation de proportionnalité ?', ans: words([[s[1] ? 'oui' : 'non']], { forbid: [s[1] ? 'non' : 'oui'] }), sample: s[1] ? 'oui' : 'non',
        corr: strong(s[1] ? 'Oui' : 'Non') + '.', meth: s[2] };
    }
    var k = D(pick([1.5, 2, 2.5, 3, 4, 0.5, 1.2, 5, 0.8])), xs = shuffle([1, 2, 3, 4, 5, 6, 8, 10, 12]).slice(0, 4).sort(function (a, b) { return a - b; });
    var ys = xs.map(function (x) { return qmul(Q(x), k); }), prop = chance(0.5), bad = ri(1, 3);
    if (!prop) ys[bad] = qadd(ys[bad], Q(pick([-1, 1]) * (qv(k) >= 2 ? 1 : 1), qv(k) < 1 ? 10 : 1));
    var tbl = '<table class="tbl"><tr><th>Masse (kg)</th>' + xs.map(function (x) { return '<td>' + x + '</td>'; }).join('') + '</tr><tr><th>Prix (€)</th>' + ys.map(function (y) { return '<td>' + f(y) + '</td>'; }).join('') + '</tr></table>';
    return { html: 'Ce tableau est-il un tableau de proportionnalité ?' + tbl, ans: words([[prop ? 'oui' : 'non']], { forbid: [prop ? 'non' : 'oui'] }), sample: prop ? 'oui' : 'non',
      corr: strong(prop ? 'Oui' : 'Non') + '.',
      meth: 'On calcule les quotients prix ÷ masse : ' + xs.map(function (x, i) { return f(ys[i]) + ' ÷ ' + x + ' = ' + f(qdiv(ys[i], Q(x))); }).join(' ; ') + '. ' + (prop ? 'Ils sont tous égaux : c’est un tableau de proportionnalité.' : 'Ils ne sont pas tous égaux : ce n’est pas un tableau de proportionnalité.') };
  }
},
{
  id: 'prop-calc', titre: 'Résoudre un problème de proportionnalité', ex: '3 cahiers coûtent 4,50 € ; 7 cahiers ?', req: [],
  gen: function () {
    var ctx = pick([['cahiers', 'coûtent', '€', 'cahiers'], ['croissants', 'coûtent', '€', 'croissants'], ['kg de pommes', 'coûtent', '€', 'kg'], ['litres d’essence', 'coûtent', '€', 'litres']]);
    var u, n1, n2, v = pick(['mul', 'div', 'unit', 'unit', 'rec']);
    if (v === 'rec') {
      var pers1 = pick([4, 6, 8]), q1 = pick([100, 150, 200, 250, 300, 60]), pers2 = pick([2, 3, 6, 10, 12, 4]); if (pers2 === pers1) pers2 = pers1 / 2;
      var res = Q(q1 * pers2, pers1); if (!H.isDec(res)) { pers2 = pers1 * 2; res = Q(q1 * 2); }
      return { html: 'Pour ' + pers1 + ' personnes, une recette demande ' + q1 + ' g de farine. Quelle masse de farine faut-il pour ' + pers2 + ' personnes ?', ans: { k: 'num', q: res, form: 'any' }, suf: 'g',
        corr: strong(f(res) + ' g'), meth: 'Pour 1 personne : ' + q1 + ' ÷ ' + pers1 + ' = ' + f(Q(q1, pers1)) + ' g. Pour ' + pers2 + ' personnes : ' + f(Q(q1, pers1)) + ' × ' + pers2 + ' = ' + f(res) + ' g.' };
    }
    u = D(pick([0.5, 0.7, 1.2, 1.5, 2.5, 0.8, 3, 1.25, 0.6, 1.4]));
    if (v === 'mul') { n1 = ri(2, 5); n2 = n1 * ri(2, 4); }
    else if (v === 'div') { n2 = ri(2, 5); n1 = n2 * ri(2, 4); }
    else { do { n1 = ri(2, 9); n2 = ri(2, 12); } while (n1 === n2 || n2 % n1 === 0 || n1 % n2 === 0); }
    var p1 = qmul(u, Q(n1)), p2 = qmul(u, Q(n2)), meth;
    if (v === 'mul') meth = n2 + ' = ' + n1 + ' × ' + n2 / n1 + ', donc le prix est multiplié par ' + n2 / n1 + ' : ' + f(p1) + ' × ' + n2 / n1 + ' = ' + f(p2) + ' €.';
    else if (v === 'div') meth = n2 + ' = ' + n1 + ' ÷ ' + n1 / n2 + ', donc le prix est divisé par ' + n1 / n2 + ' : ' + f(p1) + ' ÷ ' + n1 / n2 + ' = ' + f(p2) + ' €.';
    else meth = 'Retour à l’unité : 1 ' + ctx[3].replace(/s$/, '') + ' coûte ' + f(p1) + ' ÷ ' + n1 + ' = ' + f(u) + ' €, donc ' + n2 + ' coûtent ' + f(u) + ' × ' + n2 + ' = ' + f(p2) + ' €.';
    return { html: n1 + ' ' + ctx[0] + ' ' + ctx[1] + ' ' + f(p1) + ' €. Combien coûtent ' + n2 + ' ' + ctx[0] + ' ?', ans: { k: 'num', q: p2, form: 'any' }, suf: '€', corr: strong(f(p2) + ' €'), meth: meth };
  }
},
{
  id: 'pct-var', titre: 'Appliquer une augmentation ou une diminution en %', ex: '15 € augmenté de 20 % : 18 €', req: ['pct'],
  gen: function (c) {
    var p = pick([10, 20, 25, 50, 5, 30, 15, 40, 75]), up = chance(0.5), pr, res;
    do { pr = pick([ri(2, 40), ri(2, 20) * 5, ri(1, 30) * 10, 120, 80, 60]); res = Q(pr * (100 + (up ? p : -p)), 100); } while (res.d > 10);
    var part = Q(pr * p, 100), coef = D((100 + (up ? p : -p)) / 100);
    var meth = p + ' % de ' + pr + ' = ' + pr + ' × ' + p + ' ÷ 100 = ' + f(part) + ', puis ' + pr + (up ? ' + ' : M) + f(part) + ' = ' + f(res) + ' €.' + (c.lv === '3e' ? ' (Ou directement : ' + pr + ' × ' + f(coef) + ' = ' + f(res) + '.)' : '');
    return { html: 'Un article coûte ' + pr + ' €. Son prix ' + (up ? 'augmente' : 'baisse') + ' de ' + p + ' %. Quel est son nouveau prix ?', ans: { k: 'num', q: res, form: 'any' }, suf: '€',
      corr: strong(f(res) + ' €'), meth: meth };
  }
},
{
  id: 'graph', titre: 'Lire un graphique', ex: 'image, antécédent, lecture de valeurs', req: [],
  gen: function (c) {
    if (!c.has('fct') || chance(0.3)) {
      var ys = [0], tt = 6; for (var i = 1; i <= tt; i++) ys.push(ys[i - 1] + (chance(0.2) ? 0 : pick([10, 10, 20, 20, 30])));
      while (ys[tt] > 100) { ys = ys.map(function (y) { return y - (y > 50 ? 10 : 0); }); }
      var top = Math.ceil(ys[tt] / 10) * 10 || 10;
      var g = axes({ x0: 0, x1: tt, y0: 0, y1: top, ux: 52, uy: 200 / top, gx: 0.5, gy: 5, lx: 1, ly: 10, tx: 'Durée (h)', ty: 'Distance (km)', zero: false });
      var b = g.b + PL(ys.map(function (y, k) { return g.sp(k, y); }), 'acc');
      var fig = svg(g.W + 10, g.H, b, 'wide');
      if (chance(0.5)) { var x0 = ri(1, tt); return { html: 'Ce graphique représente la distance parcourue par un randonneur en fonction de la durée de marche. Quelle distance a-t-il parcourue au bout de ' + x0 + ' h ?' + fig, ans: { k: 'num', q: Q(ys[x0]), form: 'any' }, suf: 'km', corr: strong(ys[x0] + ' km'), meth: 'On part de ' + x0 + ' sur l’axe horizontal, on monte jusqu’à la courbe, puis on lit la valeur sur l’axe vertical : ' + ys[x0] + ' km.' }; }
      var cand = []; for (i = 1; i <= tt; i++) if (ys[i] > ys[i - 1]) cand.push(i);
      var k = pick(cand);
      return { html: 'Ce graphique représente la distance parcourue par un randonneur en fonction de la durée de marche. Au bout de combien de temps a-t-il parcouru ' + ys[k] + ' km ?' + fig, ans: { k: 'num', q: Q(k), form: 'any' }, suf: 'h', corr: strong(k + ' h'), meth: 'On part de ' + ys[k] + ' km sur l’axe vertical, on va jusqu’à la courbe, puis on lit la durée sur l’axe horizontal : ' + k + ' h.' };
    }
    var x0 = -4, x1 = 4, pts, tries = 0, ask, res, ok = false;
    while (!ok && tries++ < 200) {
      pts = []; var y = ri(-3, 4); for (var x = x0; x <= x1; x++) { pts.push([x, y]); y = Math.max(-4, Math.min(5, y + pick([-2, -1, 1, 2, 0, 1, -1]))); }
      if (chance(0.5)) { var a = ri(x0 + 1, x1 - 1); if (a !== 0 || chance(0.3)) { ask = 'img'; res = pts[a - x0][1]; ok = true; var aImg = a; } }
      else {
        var bb = ri(-3, 4), sols = [], bad = false;
        for (var i2 = 0; i2 < pts.length; i2++) {
          var p = pts[i2], q = pts[i2 + 1];
          if (p[1] === bb) { if (q && q[1] === bb) bad = true; sols.push(p[0]); }
          if (q && (p[1] - bb) * (q[1] - bb) < 0) { var xs = p[0] + (bb - p[1]) / (q[1] - p[1]); if (Math.abs(xs * 2 - Math.round(xs * 2)) > 1e-9) bad = true; sols.push(xs); }
        }
        if (!bad && sols.length >= 1 && sols.length <= 3) { ask = 'ant'; res = sols; ok = true; var bAnt = bb; }
      }
    }
    var g2 = axes({ x0: -4, x1: 4, y0: -4, y1: 5, ux: 32, uy: 26, gx: 0.5, gy: 0.5, lx: 1, ly: 1 });
    var b2 = g2.b + PL(pts.map(function (p) { return g2.sp(p[0], p[1]); }), 'acc') + T(add(g2.sp(x0, pts[0][1]), [-4, pts[0][1] > 3 ? 16 : -14]), '𝒞<tspan font-size="12" dy="4">f</tspan>', 'it', 'end');
    var fig2 = svg(g2.W, g2.H, b2);
    if (ask === 'img') return { html: 'La courbe ci-dessous représente une fonction ' + V('f') + '. Lire l’image de ' + f(aImg) + ' par ' + V('f') + '.' + fig2, ans: { k: 'num', q: Q(res), form: 'any' },
      corr: V('f') + '(' + f(aImg) + ') = ' + strong(f(res)), meth: 'L’image de ' + f(aImg) + ' se lit sur l’axe des ordonnées : on part de ' + f(aImg) + ' sur l’axe des abscisses, on rejoint la courbe, et on lit ' + f(res) + '.' };
    var sorted = res.slice().sort(function (a, b) { return a - b; }), qs = sorted.map(function (x) { return D(x); });
    return { html: 'La courbe ci-dessous représente une fonction ' + V('f') + '. Lire le ou les antécédents de ' + f(bAnt) + ' par ' + V('f') + '. (S’il y en a plusieurs, les séparer par « ; ».)' + fig2,
      sample: sorted.map(function (x) { return f(x).replace(MINUS, '-'); }).join(' ; '),
      ans: { k: 'fn', f: function (s) {
        var got = parseList(s); if (!got) return { invalid: true, msg: 'Écris un ou plusieurs nombres séparés par « ; ».' };
        var hit = got.filter(function (g) { return qs.some(function (q) { return H.qeq(q, g); }); }).length, uniq = got.filter(function (g, i) { return got.findIndex(function (h) { return H.qeq(g, h); }) === i; });
        if (hit === got.length && uniq.length === qs.length) return { ok: true };
        if (hit === got.length) return { ok: false, msg: 'Ce que tu as trouvé est juste, mais il y a ' + qs.length + ' antécédent' + (qs.length > 1 ? 's' : '') + '.' };
        return { ok: false };
      } },
      corr: strong(sorted.map(f).join(' ; ')), meth: 'On part de ' + f(bAnt) + ' sur l’axe des ordonnées, on trace une ligne horizontale et on lit les abscisses des points d’intersection avec la courbe : ' + sorted.map(f).join(' ; ') + '.' };
  }
},
{
  id: 'fct-img', titre: 'Calculer une image ou un antécédent', ex: V('f') + '(' + V('x') + ') = 3' + V('x') + ' ' + MINUS + ' 2 : ' + V('f') + '(4) = 10', req: ['fct'],
  gen: function () {
    var v = pick(['aff', 'aff', 'quad', 'ant', 'map']), a = nz(-6, 6), b = nz(-9, 9), x0 = nz(-5, 6), res, html, meth;
    if (Math.abs(a) === 1) a = 3;
    if (v === 'aff' || v === 'map') { res = a * x0 + b; html = v === 'map' ? 'On considère la fonction ' + V('g') + ' : ' + V('x') + ' ↦ ' + H.lin(a, b) + '. Calculer l’image de ' + f(x0) + ' par ' + V('g') + '.' : 'On considère la fonction ' + V('f') + ' définie par ' + V('f') + '(' + V('x') + ') = ' + H.lin(a, b) + '. Calculer ' + V('f') + '(' + f(x0) + ').'; meth = a + ' × ' + fp(x0) + H.plus(b) + ' = ' + f(a * x0) + H.plus(b) + ' = ' + f(res) + '.'; }
    else if (v === 'quad') { var k = ri(1, 3); x0 = nz(-4, 4); res = k * x0 * x0 + b; html = 'On considère la fonction ' + V('f') + ' définie par ' + V('f') + '(' + V('x') + ') = ' + H.poly({ 2: k, 0: b }) + '. Calculer ' + V('f') + '(' + f(x0) + ').'; meth = (k > 1 ? k + ' × ' : '') + fp(x0) + '²' + H.plus(b) + ' = ' + (k > 1 ? k + ' × ' : '') + x0 * x0 + H.plus(b) + ' = ' + f(res) + '.'; }
    else { a = ri(2, 6); res = x0; var y = a * x0 + b; html = 'On considère la fonction ' + V('f') + ' définie par ' + V('f') + '(' + V('x') + ') = ' + H.lin(a, b) + '. Quel est l’antécédent de ' + f(y) + ' par ' + V('f') + ' ?'; meth = 'On résout ' + H.lin(a, b) + ' = ' + f(y) + ' : ' + a + V('x') + ' = ' + f(y - b) + ', donc ' + V('x') + ' = ' + f(x0) + '.'; }
    return { html: html, ans: { k: 'num', q: Q(res), form: 'any' }, corr: strong(f(res)), meth: meth };
  }
}
];

/* ======================= Algorithmique et programmation ======================= */
function sb(cls, h) { return '<div class="sb ' + cls + '">' + h + '</div>'; }
function vv(x) { return '<span class="v">' + x + '</span>'; }
function vr(x) { return '<span class="v r">' + x + '</span>'; }
function rep(n, inner) { return '<div class="sb ctl">répéter ' + vv(n) + ' fois<div class="in">' + inner + '</div></div>'; }
function script(blocks) { return '<div class="scr">' + sb('ev', 'quand le drapeau vert est cliqué') + blocks + '</div>'; }
var CW = '↻', CCW = '↺';

var ALGO = [
{
  id: 'prog-calc', titre: 'Programme de calcul', ex: 'choisir un nombre, ajouter 4…', req: [],
  gen: function (c) {
    var ops = [], nsteps = ri(3, 4), hasSq = false;
    for (var i = 0; i < nsteps; i++) {
      var o = pick(['add', 'sub', 'mul', 'mul', 'sq', 'dbl', 'start']);
      if (o === 'sq' && (hasSq || i === 0)) o = 'add'; if (o === 'start' && i === 0) o = 'mul';
      if (o === 'sq') hasSq = true;
      ops.push({ o: o, a: o === 'mul' ? ri(2, 5) : ri(1, 9) });
    }
    var label = function (s) { return { add: 'Ajouter ' + s.a, sub: 'Soustraire ' + s.a, mul: 'Multiplier par ' + s.a, sq: 'Élever le résultat au carré', dbl: 'Prendre le double du résultat', start: 'Soustraire le nombre de départ' }[s.o]; };
    var run = function (x0) { var x = x0, tr = []; ops.forEach(function (s) { var p = x; x = s.o === 'add' ? x + s.a : s.o === 'sub' ? x - s.a : s.o === 'mul' ? x * s.a : s.o === 'sq' ? x * x : s.o === 'dbl' ? 2 * x : x - x0; tr.push(f(x)); }); return { r: x, tr: tr }; };
    var x0 = c.has('relx') && chance(0.4) ? -ri(1, 5) : ri(1, 7), R = run(x0);
    var steps = '<ol class="steps"><li>Choisir un nombre</li>' + ops.map(function (s) { return '<li>' + label(s) + '</li>'; }).join('') + '</ol>';
    var inv = c.lv === '3e' && !hasSq && ops.every(function (s) { return s.o !== 'start'; }) && chance(0.4);
    if (inv) return { html: 'Voici un programme de calcul :' + steps + 'Quel nombre faut-il choisir au départ pour obtenir ' + f(R.r) + ' ?', ans: { k: 'num', q: Q(x0), form: 'any' }, corr: strong(f(x0)),
      meth: 'On « remonte » le programme en faisant les opérations inverses dans l’ordre inverse, en partant de ' + f(R.r) + '. Vérification : en partant de ' + f(x0) + ', on obtient ' + R.tr.join(', puis ') + '.' };
    return { html: 'Voici un programme de calcul :' + steps + 'Quel résultat obtient-on en choisissant ' + f(x0) + ' comme nombre de départ ?', ans: { k: 'num', q: Q(R.r), form: 'any' }, corr: strong(f(R.r)),
      meth: 'On applique les étapes une par une à partir de ' + f(x0) + ' : ' + R.tr.join(', puis ') + '.' };
  }
},
{
  id: 'scratch-move', titre: 'Script de déplacement (Scratch)', ex: 'quelle figure trace le lutin ?', req: [],
  gen: function () {
    var v = pick(['fig', 'angle', 'repeat', 'long', 'cren', 'cren']);
    if (v === 'cren') {
      var k = ri(3, 7), inner = sb('mo', 'avancer de ' + vv(30) + ' pas') + sb('mo', 'tourner ' + CCW + ' de ' + vv(90) + ' degrés') + sb('mo', 'avancer de ' + vv(10) + ' pas') + sb('mo', 'tourner ' + CW + ' de ' + vv(90) + ' degrés') + sb('mo', 'avancer de ' + vv(30) + ' pas') + sb('mo', 'tourner ' + CW + ' de ' + vv(90) + ' degrés') + sb('mo', 'avancer de ' + vv(10) + ' pas') + sb('mo', 'tourner ' + CCW + ' de ' + vv(90) + ' degrés');
      var scr = script(sb('mo', 'aller à x: ' + vv(-200) + ' y: ' + vv(0)) + sb('pen', 'stylo en position d’écriture') + rep('…', inner));
      var pts = [[0, 30]], x = 0; for (var i = 0; i < k; i++) { pts.push([x + 30, 30], [x + 30, 10], [x + 60, 10], [x + 60, 30]); x += 60; }
      var fig = svg(x * 1.2 + 20, 50, PL(pts.map(function (p) { return [10 + p[0] * 1.2, p[1] + 2]; }), 'acc'), 'wide');
      return { html: 'Par quelle valeur faut-il remplacer les pointillés pour obtenir la figure ci-dessous ?' + scr + fig, ans: { k: 'num', q: Q(k), form: 'int' }, corr: strong(k),
        meth: 'À chaque répétition, le lutin trace un « créneau » (avancer 30, monter 10, avancer 30, descendre 10). La figure contient ' + k + ' créneaux.' };
    }
    var n = pick([3, 4, 5, 6, 8]), Lg = pick([50, 80, 100, 60]), a = 360 / n, nm = { 3: 'triangle équilatéral', 4: 'carré', 5: 'pentagone régulier', 6: 'hexagone régulier', 8: 'octogone régulier' }[n];
    var body = function (nn, aa) { return sb('pen', 'stylo en position d’écriture') + rep(nn, sb('mo', 'avancer de ' + vv(Lg) + ' pas') + sb('mo', 'tourner ' + CW + ' de ' + vv(aa) + ' degrés')); };
    if (v === 'fig') return { html: 'Quelle figure le lutin trace-t-il avec ce script ?' + script(body(n, a)), ans: words([[{ 3: 'triangle', 4: 'carre', 5: 'pentagone', 6: 'hexagone', 8: 'octogone' }[n]]]), sample: nm,
      corr: 'Un ' + strong(nm) + ' de côté ' + Lg + ' pas.', meth: 'Le lutin trace ' + n + ' côtés de même longueur en tournant de ' + a + '° à chaque fois (360 ÷ ' + n + ' = ' + a + ') : c’est un ' + nm + '.' };
    if (v === 'angle') return { html: 'Par quelle valeur faut-il remplacer les pointillés pour que le lutin trace un ' + nm + ' ?' + script(body(n, '…')), ans: { k: 'num', q: Q(a), form: 'any' }, suf: '°', corr: strong(a + '°'),
      meth: 'Pour revenir à son point de départ, le lutin fait un tour complet (360°) en ' + n + ' fois : 360 ÷ ' + n + ' = ' + a + '°.' };
    if (v === 'repeat') return { html: 'Par quelle valeur faut-il remplacer les pointillés pour que le lutin trace la figure complète, sans repasser sur un côté ?' + script(body('…', a)), ans: { k: 'num', q: Q(n), form: 'int' }, corr: strong(n),
      meth: 'À chaque tour, le lutin tourne de ' + a + '° ; il lui faut 360 ÷ ' + a + ' = ' + n + ' répétitions pour revenir à son point de départ.' };
    return { html: 'Quelle est la longueur totale, en pas, du tracé réalisé par ce script ?' + script(body(n, a)), ans: { k: 'num', q: Q(n * Lg), form: 'any' }, suf: 'pas', corr: strong(n * Lg + ' pas'),
      meth: 'Le lutin avance ' + n + ' fois de ' + Lg + ' pas : ' + n + ' × ' + Lg + ' = ' + n * Lg + ' pas.' };
  }
},
{
  id: 'scratch-calc', titre: 'Script de calcul (Scratch)', ex: 'que dit le lutin ?', req: [],
  gen: function (c) {
    var start = c.has('relx') && chance(0.3) ? -ri(1, 6) : ri(2, 9), x = start, blocks = '', tr = [];
    var input = chance(0.5);
    if (input) blocks += sb('lk', 'demander ' + vv('Choisis un nombre') + ' et attendre') + sb('var', 'mettre ' + vr('nombre') + ' à ' + vr('réponse'));
    else blocks += sb('var', 'mettre ' + vr('nombre') + ' à ' + vv(f(start)));
    var nOps = ri(2, 3);
    for (var i = 0; i < nOps; i++) {
      var o = pick(['add', 'mul', 'sub', 'sq']), a = o === 'mul' ? ri(2, 5) : ri(1, 9);
      if (o === 'sq' && i === 0) o = 'mul';
      if (o === 'add') { x += a; blocks += sb('var', 'ajouter ' + vv(a) + ' à ' + vr('nombre')); }
      else if (o === 'sub') { x -= a; blocks += sb('var', 'mettre ' + vr('nombre') + ' à ' + vr(vr('nombre') + ' − ' + vv(a))); }
      else if (o === 'mul') { x *= a; blocks += sb('var', 'mettre ' + vr('nombre') + ' à ' + vr(vr('nombre') + ' × ' + vv(a))); }
      else { x *= x; blocks += sb('var', 'mettre ' + vr('nombre') + ' à ' + vr(vr('nombre') + ' × ' + vr('nombre'))); }
      tr.push(f(x));
    }
    if (c.lv === '3e' && chance(0.4)) {
      var seuil = ri(5, 20), big = x > seuil, a1 = ri(2, 9), a2 = ri(2, 3);
      blocks += '<div class="sb ctl">si ' + vr(vr('nombre') + ' &gt; ' + vv(seuil)) + ' alors<div class="in">' + sb('var', 'mettre ' + vr('nombre') + ' à ' + vr(vr('nombre') + ' − ' + vv(a1))) + '</div>sinon<div class="in">' + sb('var', 'mettre ' + vr('nombre') + ' à ' + vr(vr('nombre') + ' × ' + vv(a2))) + '</div></div>';
      x = big ? x - a1 : x * a2; tr.push((big ? 'comme le nombre est plus grand que ' + seuil + ', on enlève ' + a1 : 'comme le nombre n’est pas plus grand que ' + seuil + ', on multiplie par ' + a2) + ' : ' + f(x));
    }
    blocks += sb('lk', 'dire ' + vr('nombre'));
    return { html: (input ? 'On répond ' + f(start) + ' à la question posée par le lutin. ' : '') + 'Que dit le lutin à la fin de ce script ?' + script(blocks), ans: { k: 'num', q: Q(x), form: 'any' }, corr: strong(f(x)),
      meth: 'La variable « nombre » vaut d’abord ' + f(start) + ', puis ' + tr.join(', puis ') + '.' };
  }
}
];

themeGens('data').push.apply(themeGens('data'), DATA);
themeGens('fct').push.apply(themeGens('fct'), FCT);
themeGens('algo').push.apply(themeGens('algo'), ALGO);
})(this);
