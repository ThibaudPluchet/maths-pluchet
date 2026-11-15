/* Écriture des quotients : toute division notée « a/b » dans le texte affiché devient une fraction
   avec un trait horizontal. Les unités (km/h, m/s, L/min, g/cm³…), les scores (3 / 5) et les
   consignes de saisie (« écris une fraction comme 7/12 ») gardent leur barre oblique.
   Fichier commun à toutes les pages d'exercices : il agit sur le texte dès qu'il est affiché. */
(function(){
'use strict';
var css = '.frac{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 .12em;line-height:1.15;font-size:.92em;text-align:center}' +
  '.frac>span{display:block;padding:0 .18em;white-space:nowrap}' +
  '.frac>.fd{border-top:.09em solid currentColor}';
var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

var SP = '[ \\u00a0\\u202f\\u2009]';
var NUM = '\\d+(?:' + SP + '\\d{3}(?!\\d))*(?:,\\d+)?°?';
var WORD = '\\d*(?:[A-Za-zÀ-ÖØ-öø-ÿπ]+(?:[²³]|\\d(?![\\d,]))?′?)+';
var PAR = '\\((?:[^()]|\\([^()]*\\))*\\)';
var OPD = '(?:' + PAR + '|' + WORD + '|' + NUM + '|\\?)';
var RE = new RegExp('(' + OPD + ')([ \\u00a0\\u202f]?)\\/(?!\\/)\\2([−-]?' + OPD + ')', 'g');
var UL = /^(?:km|hm|dam|m|m³|m²|dm|cm|mm|L|l|mL|cL|dL|g|kg|mg|t|€|W|kW|kWh|Wh|Mo|Go|ko|To|octets?|tr|battements|hab|habitants?|pers|personnes?|places?|euros?|litres?|mètres?|kilomètres?)$/;
var UR = /^(?:h|s|min|j|jours?|ans?|mois|semaines?|kg|g|L|l|m|m²|m³|km|km²|cm|cm²|cm³|dm³|mL|pers|personnes?|habitants?|élèves?|kWh|heures?|secondes?|minutes?)$/;
var SKIP = /^(?:SCRIPT|STYLE|TEXTAREA|INPUT|SELECT|OPTION|CODE|PRE)$/;

function bare(t){ return /^\(.*\)$/.test(t) && balanced(t.slice(1, -1)) ? t.slice(1, -1) : t; }
function balanced(t){ var d = 0; for (var i = 0; i < t.length; i++){ if (t[i] === '(') d++; else if (t[i] === ')' && --d < 0) return false; } return d === 0; }
function skipNode(n){
  for (var e = n.parentNode; e && e.nodeType === 1; e = e.parentNode){
    if (SKIP.test(e.nodeName) || e.namespaceURI === 'http://www.w3.org/2000/svg') return true;
    if (e.classList && (e.classList.contains('res') || e.classList.contains('pts') || e.classList.contains('kbar') || e.classList.contains('rec') || e.classList.contains('note') || e.classList.contains('nofrac'))) return true;
  }
  return false;
}
function piece(txt){ var s = document.createElement('span'); s.textContent = txt; return s; }

function setText(node){
  var t = node.nodeValue;
  if (t.indexOf('/') < 0 || /:\/\//.test(t) || /(?:^|[^A-Za-zÀ-ÿ])(?:écris|écrire|tape|taper)\b[^.]*\d\/[−-]?\d/i.test(t) || skipNode(node)) return;
  var out = [], last = 0, m, any = false; RE.lastIndex = 0;
  while ((m = RE.exec(t))){
    var a = m[1], b = m[3], i = m.index;
    if ((UL.test(a) && UR.test(b)) || (UL.test(a) && /^\s(?:km|kg|g|m|L)\b/.test(t.slice(i + m[0].length))) || /^\s*points?\b/.test(t.slice(i + m[0].length)) || (/^\d+$/.test(b) && b === '20' && /note|\/20\b.*note|sur 20/i.test(t))){ RE.lastIndex = i + 1; continue; }
    // pas de fraction au milieu d'une date (12/06/2026) ni d'un nom de fichier
    if (/[\d\/.]/.test(t.charAt(i + m[0].length)) && t.charAt(i + m[0].length) === '/') { RE.lastIndex = i + m[0].length; continue; }
    if (i > 0 && t.charAt(i - 1) === '/') { RE.lastIndex = i + 1; continue; }
    if (i > last) out.push(document.createTextNode(t.slice(last, i)));
    var f = document.createElement('span'); f.className = 'frac';
    var fn = piece(bare(a)); fn.className = 'fn'; var fd = piece(bare(b)); fd.className = 'fd';
    f.appendChild(fn); f.appendChild(fd);
    f.setAttribute('aria-label', bare(a) + ' sur ' + bare(b));
    out.push(f); last = i + m[0].length; any = true;
  }
  if (!any) return;
  if (last < t.length) out.push(document.createTextNode(t.slice(last)));
  var p = node.parentNode; out.forEach(function(o){ p.insertBefore(o, node); }); p.removeChild(node);
}
function scan(root){
  if (root.nodeType === 3){ setText(root); return; }
  if (root.nodeType !== 1 || SKIP.test(root.nodeName) || root.namespaceURI === 'http://www.w3.org/2000/svg') return;
  var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), L = [], n;
  while ((n = w.nextNode())) if (n.nodeValue.indexOf('/') >= 0) L.push(n);
  L.forEach(setText);
}
window.MFrac = {scan: scan};
function go(){
  scan(document.body);
  new MutationObserver(function(ms){ ms.forEach(function(m){
    if (m.type === 'characterData') setText(m.target);
    else m.addedNodes.forEach(scan); }); })
    .observe(document.body, {childList: true, subtree: true, characterData: true});
}
if (document.body) go(); else document.addEventListener('DOMContentLoaded', go);
})();
