"""Roulement sur 5 sessions : garde les sujets des années [R-4 ; R], R = année de la dernière rentrée
(septembre à décembre : année en cours ; janvier à août : année précédente). Exemple : en 2026-2027, 2022 à 2026.
Usage : python3 rotation.py <dépôt> [--annee R] [--simuler]
Retire des catalogues (_source/annales.json, _source/annales-sujets.json, data.json, data.js) les sessions hors fenêtre
et supprime annales/<année>/ et _source/annales/<année>/. Affiche aussi les années de la fenêtre absentes du site."""
import json, re, os, sys, shutil, datetime
REPO = sys.argv[1]
args = sys.argv[2:]
t = datetime.date.today()
R = int(args[args.index('--annee') + 1]) if '--annee' in args else (t.year if t.month >= 9 else t.year - 1)
SIM = '--simuler' in args
keep = lambda an: R - 4 <= an <= R
P = lambda *p: os.path.join(REPO, *p)
cat = json.load(open(P('_source', 'annales.json'))); suj = json.load(open(P('_source', 'annales-sujets.json')))
old = sorted({p['an'] for p in cat + suj if not keep(p['an'])})
print(f'Fenêtre : {R - 4} à {R}. Sessions présentes : {sorted({p["an"] for p in cat})}. À retirer : {old or "aucune"}.')
missing = [a for a in range(R - 4, R + 1) if a not in {p['an'] for p in cat}]
print('Sessions de la fenêtre absentes du site :', missing or 'aucune')
if not old or SIM:
    sys.exit()
cat = [p for p in cat if keep(p['an'])]; suj = [p for p in suj if keep(p['an'])]
json.dump(cat, open(P('_source', 'annales.json'), 'w'), ensure_ascii=False, indent=0)
json.dump(suj, open(P('_source', 'annales-sujets.json'), 'w'), ensure_ascii=False, indent=0)
ids = {p['id'] for p in cat}
for f in ('data.json', 'data.js'):
    t = open(P(f), encoding='utf-8').read()
    m = re.match(r'(\s*[^{]*?)(\{.*\})(;?\s*)$', t, re.S); d = json.loads(m.group(2))
    d['dnb']['parts'] = cat; d['dnb']['sujets'] = suj
    d['dnb']['cls'] = {c: [i for i in L if i in ids] for c, L in d['dnb'].get('cls', {}).items()}
    open(P(f), 'w', encoding='utf-8').write(m.group(1) + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + m.group(3))
for a in old:
    for d in (P('annales', str(a)), P('_source', 'annales', str(a))):
        if os.path.isdir(d): shutil.rmtree(d)
print('Retiré :', old)
