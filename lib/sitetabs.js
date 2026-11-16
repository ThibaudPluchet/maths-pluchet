/* Barre d'onglets du site élèves, partagée par index.html, auto.html, lexique.html, animations.html, curiosites.html et cahier-vacances.html / cahier-vacances-4e.html (onglet « Cahier de vacances » : toujours pour l'adresse enseignant, pour les élèves de 3e et de 4e du 15 juin au 31 août).
   index.html enregistre la liste des onglets de la classe (localStorage « mp:tabs ») à chaque affichage ;
   les autres pages la relisent pour afficher exactement la même barre. Un clic vers un onglet de index.html
   passe par sessionStorage « mp:vue », lu au chargement de index.html. */
(function(){
'use strict';
var SVG = {
  dm:'<rect x="4" y="3" width="16" height="13" rx="1.5"/><path d="M8 7h8M8 10.5h5"/><path d="M9 16l-2.5 5M15 16l2.5 5M12 16v3"/>',
  cours:'<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21V5"/><path d="M8 7.5h7M8 11h5"/>',
  evals:'<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V2.8h6V4"/><path d="m9 13 2.2 2.2L15.5 11"/>',
  brevet:'<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2.2 9 2.2 12 0v-5"/><path d="M22 9v6"/>',
  auto:'<path d="M13 2 4.5 13.5H11L10 22l8.5-11.5H12z"/>',
  lexique:'<path d="M4 4.5A1.5 1.5 0 0 1 5.5 3H19v15H5.5A1.5 1.5 0 0 0 4 19.5z"/><path d="M4 19.5A1.5 1.5 0 0 0 5.5 21H19v-3"/><path d="m9 13 2.5-6.5L14 13M9.9 11h3.2"/>',
  animations:'<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M10 8.2v5.6l4.8-2.8z"/><path d="M8 21h8M12 17v4"/>',
  curio:'<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.8.8 1 1.6 1 2.5h6c0-.9.2-1.7 1-2.5A6 6 0 0 0 12 3z"/>',
  vacances4e:null,
  vacances:'<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8"/>'
};
SVG.vacances4e = SVG.vacances;
var CSS = '.sitetabs{display:flex;flex-wrap:wrap;gap:6px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:4px;width:max-content;max-width:100%}' +
  '.sitetabs button{display:inline-flex;align-items:center;gap:7px;border:0;background:transparent;color:var(--muted);font:700 15px "Atkinson Hyperlegible",sans-serif;padding:9px 14px;border-radius:9px;cursor:pointer;min-height:44px;white-space:nowrap}' +
  '.sitetabs button[aria-current="page"]{background:var(--soft);color:var(--accent)}' +
  '.sitetabs .ico{width:19px;height:19px;display:inline-grid;place-items:center;flex:none}' +
  '.sitetabs .ico svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}' +
  '.sitetabs .tdot{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--new,#d6336c);margin-left:2px}' +
  '@media (max-width:620px){.sitetabs{flex-wrap:nowrap;overflow-x:auto;width:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch;scroll-snap-type:x proximity}' +
  '.sitetabs::-webkit-scrollbar{display:none}.sitetabs button{padding:9px 12px;scroll-snap-align:start}}';
function store(k, v){ try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch(e){ return null; } }
function addCss(){ if (document.getElementById('sitetabs-css')) return; var s = document.createElement('style'); s.id = 'sitetabs-css'; s.textContent = CSS; document.head.appendChild(s); }
function icon(k){ var s = document.createElement('span'); s.className = 'ico'; s.setAttribute('aria-hidden', 'true'); s.innerHTML = '<svg viewBox="0 0 24 24">' + (SVG[k] || '') + '</svg>'; return s; }
// list : [[clé, libellé, point rouge ?], …] ; cur : clé de l'onglet affiché ; go(clé) : action au clic
function build(list, cur, go){
  addCss();
  var nav = document.createElement('nav'); nav.className = 'sitetabs'; nav.setAttribute('aria-label', 'Rubriques');
  list.forEach(function(t){
    var b = document.createElement('button'); b.type = 'button'; b.appendChild(icon(t[0])); b.appendChild(document.createTextNode(t[1]));
    if (t[2]){ var d = document.createElement('span'); d.className = 'tdot'; d.title = 'Nouveau'; b.appendChild(d); }
    if (t[0] === cur) b.setAttribute('aria-current', 'page');
    b.onclick = function(){ go(t[0]); };
    nav.appendChild(b);
  });
  // l'onglet affiché reste visible quand la barre défile horizontalement (téléphone)
  setTimeout(function(){ var a = nav.querySelector('[aria-current]'); if (!a || nav.scrollWidth <= nav.clientWidth) return; var r = a.getBoundingClientRect(), n = nav.getBoundingClientRect(); if (r.right > n.right - 8) nav.scrollLeft += r.right - n.right + 40; }, 0);
  return nav;
}
function href(k){ return k === 'auto' ? 'auto.html' : k === 'curio' ? 'curiosites.html' : k === 'lexique' ? 'lexique.html' : k === 'animations' ? 'animations.html' : k === 'vacances' ? 'cahier-vacances.html' : k === 'vacances4e' ? 'cahier-vacances-4e.html' : 'index.html'; }
// onglets qui ouvrent une autre page que index.html
function page(k){ return k === 'auto' || k === 'curio' || k === 'lexique' || k === 'animations' || k === 'vacances' || k === 'vacances4e'; }
// pages autres que index.html : barre enregistrée par index.html (ou barre par défaut)
function mount(where, cur){
  var list = null; try { list = JSON.parse(store('mp:tabs') || 'null'); } catch(e){}
  if (!Array.isArray(list) || !list.length) list = [['cours', 'Mes cours'], ['evals', 'Évaluations'], ['auto', 'Automatismes'], ['lexique', 'Lexique'], ['animations', 'Animations'], ['curio', 'Curiosités']];
  var nav = build(list, cur, function(k){
    if (k === cur) return;
    if (!page(k)) try { sessionStorage.setItem('mp:vue', k); } catch(e){}
    location.href = href(k) + location.hash;
  });
  where.parentNode.insertBefore(nav, where);
  var back = document.getElementById('back'); if (back) back.style.display = 'none';
  return nav;
}
window.SiteTabs = {build: build, mount: mount, href: href, page: page, save: function(list){ store('mp:tabs', JSON.stringify(list)); }};
})();
