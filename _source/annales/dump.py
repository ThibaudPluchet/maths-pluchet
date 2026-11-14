import pymupdf, sys, re
doc = pymupdf.open(sys.argv[1])
full = len(sys.argv) > 2
for pno, page in enumerate(doc, 1):
    H = page.rect.height
    lines = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ''.join(s['text'] for s in l['spans']).strip()
            if not t: continue
            lines.append((round(l['bbox'][1]), round(l['bbox'][0]), round(l['bbox'][3]), t))
    lines.sort()
    ys = [y for y, x, y1, t in lines]
    print(f'--- page {pno} (h={round(H)}) contenu y {min(ys)}..{max(y1 for _,_,y1,_ in lines)}')
    for y, x, y1, t in lines:
        if y < 75: continue
        key = re.match(r'(Exercice|Partie|Question|Situation|\d+\.|[a-e]\.|Annexe|Document)', t)
        if full or (key and x < 120):
            print(f'{y:4d} x{x:3d} {t[:70]}')
