"""Sujets complets (PDF officiel) et corrigés complets (style du cours) de chaque centre.
Usage : python3 full.py <dossier spec> <dossier de sortie>
Un spec par centre (spec_<code>.py, parties dans l'ordre du sujet, ids « <année>-<code>-… ») ; écrit les PDF et sujets.json."""
import sys, os, re, glob, shutil, subprocess, importlib.util, json
T = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, T)
from build import SUBJ, PRE, SRC, BLD
specdir, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
cat = []
for f in sorted(glob.glob(specdir + '/spec_*.py')):
    s = importlib.util.spec_from_file_location('s', f); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    code = os.path.basename(f)[5:-3]
    pdf, src = getattr(m, 'SOURCE', None) or SUBJ[code]
    an = int(m.PARTS[0]['id'][:4])
    body, cur = [], None
    for p in m.PARTS:
        if p.get('extra'): continue   # parties extraites d'une autre (déjà dans le corrigé complet)
        if p['ex'] != cur:
            cur = p['ex']; name = p['titre'].split(',')[0]
            body.append('\\partie{' + name + '}')
        body.append(p['corr'])
    tex = (PRE + '\n\\rfoot{\\small DNB ' + src + '}\n\\begin{document}\n\\corrigetrue\n'
           '\\bandeaudnb{Sujet complet}{Brevet des collèges -- ' + src + '}\n' + '\n'.join(body) + '\n\\end{document}\n')
    base = BLD + '/full-' + code
    open(base + '.tex', 'w').write(tex)
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-output-directory', BLD, base + '.tex'], capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(code + ' : ' + ' | '.join([l for l in r.stdout.split('\n') if l.startswith('!') or l.startswith('l.')][:4]))
    shutil.copyfile(base + '.pdf', f'{out}/{an}-{code}-corrige-complet.pdf')
    shutil.copyfile(SRC + '/' + pdf, f'{out}/{an}-{code}-sujet-complet.pdf')
    cat.append({'id': f'{an}-{code}', 'an': an, 'src': src,
                'e': f'annales/{an}/{an}-{code}-sujet-complet.pdf', 'c': f'annales/{an}/{an}-{code}-corrige-complet.pdf'})
    print('ok', code)
json.dump(cat, open(out + '/sujets.json', 'w'), ensure_ascii=False, indent=0)
