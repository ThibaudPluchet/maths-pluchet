"""Publie (ou republie) une session d'annales dans le dépôt.
Usage : python3 publish.py <dépôt> <dossier de travail> <année> <dossier db>
- <dossier de travail>/spec/spec_<code>.py : TOUS les sujets de la session (anciens recopiés depuis _source/annales/<année>/ + nouveaux) ;
- <dossier de travail>/out/enonce|corrige/<id>.pdf : PDF construits par build.py (s'ils manquent, ceux déjà publiés sont gardés) ;
- <dossier de travail>/full/*.pdf + sujets.json : produits par full.py ;
- <dossier db> : exports ArtifactData (suivi/, suivi3e/ : un JSON par notion) pour débloquer tout de suite les parties.
Met à jour annales/<année>/, _source/annales.json, _source/annales-sujets.json (ordre chronologique), data.json et data.js."""
import json, re, shutil, glob, os, sys, importlib.util
REPO, W, Y, DB = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
MOIS = {m: i for i, m in enumerate(['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'], 1)}
def quand(label):
    m = re.search(r'(?:(\d+)(?:er)?\s+)?(' + '|'.join(MOIS) + r')\s+(\d{4})', label)
    return (int(m.group(3)), MOIS[m.group(2)], int(m.group(1) or 15)) if m else (9999, 0, 0)
def mod(f):
    s = importlib.util.spec_from_file_location('s', f); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
R = lambda *p: os.path.join(REPO, *p)
os.makedirs(R('annales', str(Y)), exist_ok=True); os.makedirs(R('_source', 'annales', str(Y)), exist_ok=True)
specs = sorted(((mod(f), f) for f in glob.glob(f'{W}/spec/spec_*.py')), key=lambda x: quand(x[0].SOURCE[1]))
new = []
for m, f in specs:
    for p in m.PARTS:
        i = p['id']; assert i.startswith(f'{Y}-'), i
        for src, dst in ((f'{W}/out/enonce/{i}.pdf', R('annales', str(Y), f'{i}.pdf')), (f'{W}/out/corrige/{i}.pdf', R('annales', str(Y), f'{i}-corrige.pdf'))):
            if os.path.exists(src): shutil.copyfile(src, dst)
            assert os.path.exists(dst), 'PDF manquant : ' + dst
        new.append({'id': i, 'an': Y, 'src': m.SOURCE[1], 'ex': p['ex'], 'titre': p['titre'].replace('--', '–'), 'theme': p['theme'],
                    's3': p['s3'], 'n3': p['n3'], 's4': p['s4'], 'n4': p['n4'], 'e': f'annales/{Y}/{i}.pdf', 'c': f'annales/{Y}/{i}-corrige.pdf'})
    shutil.copyfile(f, R('_source', 'annales', str(Y), os.path.basename(f)))
for f in glob.glob(f'{W}/full/*.pdf'): shutil.copy(f, R('annales', str(Y)))
cat = [p for p in json.load(open(R('_source', 'annales.json'))) if p['an'] != Y] + new
json.dump(cat, open(R('_source', 'annales.json'), 'w'), ensure_ascii=False, indent=0)
fs = {x['id']: x for x in json.load(open(f'{W}/full/sujets.json'))}
codes = [os.path.basename(f)[5:-3] for m, f in specs]
suj = [x for x in json.load(open(R('_source', 'annales-sujets.json'))) if x['an'] != Y] + [fs[f'{Y}-{c}'] for c in codes if f'{Y}-{c}' in fs]
json.dump(suj, open(R('_source', 'annales-sujets.json'), 'w'), ensure_ascii=False, indent=0)
state = lambda col: {os.path.basename(f)[:-5]: json.load(open(f)) for f in glob.glob(f'{DB}/{col}/*.json')}
S = {'3e': state('suivi3e'), '4e': state('suivi')}
for f in ('data.json', 'data.js'):
    t = open(R(f), encoding='utf-8').read()
    m = re.match(r'(\s*[^{]*?)(\{.*\})(;?\s*)$', t, re.S); d = json.loads(m.group(2))
    d['dnb']['parts'] = cat; d['dnb']['sujets'] = suj
    for lv, key in (('3e', 'n3'), ('4e', 'n4')):
        for k, c in enumerate(d['classes'].get(lv, [])):
            L = [x for x in d['dnb']['cls'].get(c, []) if not x.startswith(f'{Y}-')]
            L += [p['id'] for p in new if p[key] is not None and all((S[lv].get('n%02d' % n) or {}).get(f'c{k + 1}') for n in p[key])]
            d['dnb']['cls'][c] = L
            if f == 'data.json': print(c, sum(1 for x in L if x.startswith(f'{Y}-')), f'parties {Y} visibles')
    open(R(f), 'w', encoding='utf-8').write(m.group(1) + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + m.group(3))
print(len(new), 'parties ;', sum(1 for x in suj if x['an'] == Y), f'sujets complets {Y}')
