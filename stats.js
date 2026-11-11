/* Statistiques de fréquentation (GoatCounter : sans cookie, sans donnée personnelle).
   Les navigateurs de l'enseignant (lien personnel du mode classe déjà ouvert) ne sont jamais comptés.
   Seul le nom de la classe est envoyé, jamais la clé secrète de l'adresse. */
(function(){
  var PROF_HASH = '5a7300999345ce2278c87b182fb492e326f26abe7aae5be0d23e14ddfda3aab7', q = [], ready = false, off = false;
  function get(k){ try { return localStorage.getItem(k); } catch(e){ return null; } }
  function set(k, v){ try { localStorage.setItem(k, v); } catch(e){} }
  window.stat = function(path, title, event){ if (off) return; if (ready && window.goatcounter && goatcounter.count) send(path, title, event); else q.push([path, title, event]); };
  function send(path, title, event){ try { goatcounter.count({path: path, title: title || path, event: !!event}); } catch(e){} }
  function load(){
    var s = document.createElement('script');
    s.async = true; s.src = 'https://gc.zgo.at/count.js';
    s.setAttribute('data-goatcounter', 'https://thibaudpluchet.goatcounter.com/count');
    s.setAttribute('data-goatcounter-settings', '{"no_onload": true}');
    s.onload = function(){ ready = true; q.splice(0).forEach(function(a){ send(a[0], a[1], a[2]); }); };
    document.head.appendChild(s);
  }
  function hex(b){ return Array.prototype.map.call(new Uint8Array(b), function(x){ return ('0' + x.toString(16)).slice(-2); }).join(''); }
  var m = location.hash.match(/prof=([A-Za-z0-9_-]+)/), t = m ? m[1] : get('prof');
  if (get('skipgc') === 't'){ off = true; return; }
  if (!t || !window.crypto || !crypto.subtle){ load(); return; }
  crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)).then(function(b){
    if (hex(b) === PROF_HASH){ off = true; q = []; set('skipgc', 't'); } else load();
  }, load);
})();
