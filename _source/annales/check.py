import pymupdf, importlib.util, glob, re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build import SUBJ, SRC
for f in sorted(glob.glob(os.path.dirname(__file__) + '/../spec/spec_*.py')):
    spec = importlib.util.spec_from_file_location('s', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for p in m.PARTS:
        doc = pymupdf.open(SRC + '/' + (getattr(m, 'SOURCE', None) or SUBJ[p['s']])[0])
        for i, (pn, y0, y1) in enumerate(p['regions']):
            page = doc[pn - 1]
            lines = []
            for b in page.get_text('dict')['blocks']:
                for l in b.get('lines', []):
                    t = ''.join(s['text'] for s in l['spans']).strip()
                    if t: lines.append((l['bbox'], t))
            for (x0, ly0, x1, ly1), t in lines:
                for yb in (y0, y1):
                    if ly0 < yb - 1 and ly1 > yb + 1:
                        print(f"{p['id']} r{i} p{pn}: ligne coupée à {yb} ({round(ly0)}-{round(ly1)}) « {t[:50]} »")
            # première ligne visible de la région
            vis = sorted([(ly0, x0, t) for (x0, ly0, x1, ly1), t in lines if ly0 >= y0 - 1 and ly1 <= y1 + 1])
            if vis and i > 0:
                ly0, x0, t = vis[0]
                if not re.match(r'(Exercice|EXERCICE|Partie|PARTIE|Question|Situation|\d+\.|[a-e]\.|Annexe|Réponse|Document)', t) and x0 < 300:
                    print(f"{p['id']} r{i} p{pn}: début « {t[:60]} » (y {round(ly0)})")
