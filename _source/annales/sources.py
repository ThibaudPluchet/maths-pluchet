"""Liste les sujets de DNB (série générale) publiés sur site2wouf.fr pour les années de la fenêtre
et indique ceux qui ne sont pas encore sur le site élèves.
Usage : python3 sources.py <dépôt> [--annee R]
Un sujet est « présent » si un spec de _source/annales/<année>/ a pour SOURCE ce fichier PDF.
Les sujets volontairement écartés (programme non français…) sont listés dans _source/annales/exclus.txt."""
import re, os, sys, glob, subprocess, datetime, importlib.util
REPO = sys.argv[1]; args = sys.argv[2:]
t = datetime.date.today()
R = int(args[args.index('--annee') + 1]) if '--annee' in args else (t.year if t.month >= 9 else t.year - 1)
html = subprocess.run(['curl', '-s', 'https://site2wouf.fr/annales.php'], capture_output=True, text=True).stdout
if not html:
    sys.exit('site2wouf.fr injoignable')
dispo = sorted(set(re.findall(r'(dnb_(?!pro_)[a-z_]+_\d{4}\.pdf)', html)))
exclus = set(open(os.path.join(REPO, '_source', 'annales', 'exclus.txt')).read().split()) if os.path.exists(os.path.join(REPO, '_source', 'annales', 'exclus.txt')) else set()
present = set()
for f in glob.glob(os.path.join(REPO, '_source', 'annales', '20*', 'spec_*.py')):
    src = open(f, encoding='utf-8').read()
    m = re.search(r"SOURCE\s*=\s*\('([^']+)'", src)
    if m: present.add(m.group(1))
# 2025 : specs sans SOURCE (fichiers listés dans build.py)
for f in glob.glob(os.path.join(REPO, '_source', 'annales', '2025', 'spec_*.py')):
    present.add('2025:' + os.path.basename(f))
manque = []
for f in dispo:
    an = int(re.search(r'_(\d{4})\.pdf', f).group(1))
    if not (R - 4 <= an <= R) or f in exclus or f in present:
        continue
    if an == 2025:
        continue  # session 2025 complète (specs historiques sans SOURCE)
    manque.append(f)
print(f'Fenêtre {R - 4}-{R} : {len(manque)} sujet(s) à ajouter')
for f in manque:
    print(' ', f, '| corrigé : corr_' + f)
