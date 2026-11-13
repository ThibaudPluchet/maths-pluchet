"""Empreintes des questions des sujets de l'évaluation 4e N10 (théorème de Pythagore).

Usage : python3 _source/exclu_n10_4e.py <PDF des sujets (élève ou corrigé)>...
Affiche le tableau JSON d'empreintes FNV-1a à coller dans la constante EXCLU de exos/4e-n10-eval.html.
Clés : tr:<lettres triées>|<sommet de l'angle droit> (triangles nommés), hy:<petit côté>|<grand côté> (calcul de l'hypoténuse),
pb:<hypoténuse>|<côté connu> (problème), rc:<petit>|<grand> (diagonale du rectangle), is:<hypoténuse> (triangle rectangle isocèle).
Nombres écrits avec une virgule décimale (ex. 6,5).
"""
import json, re, subprocess, sys, math

def fnv(s):
    h = 0x811c9dc5
    for ch in s.encode("utf-8"):
        h ^= ch; h = (h * 0x01000193) & 0xffffffff
    return "%08x" % h

def n(x):
    v = float(str(x).replace(",", "."))
    return ("%g" % v).replace(".", ",")

keys = set()
for f in sys.argv[1:]:
    t = subprocess.run(["pdftotext", "-layout", f, "-"], capture_output=True, text=True).stdout
    for name, r in re.findall(r"([A-Z] ?[A-Z] ?[A-Z]) (?:est )?rectangle en ([A-Z])", t):
        keys.add("tr:%s|%s" % ("".join(sorted(name.replace(" ", ""))), r))
    for a, b in re.findall(r"est rectangle en [A-Z], [A-Z] ?[A-Z] = ([\d,]+) cm et [A-Z] ?[A-Z] = ([\d,]+) cm", t):
        x, y = sorted([float(a.replace(",", ".")), float(b.replace(",", "."))])
        keys.add("hy:%s|%s" % (n(x), n(y)))
    for H, L, D in re.findall(r"(?=(?<![\d,])([\d,]+) − ([\d,]+) = ([\d,]+))", t):   # « 100 − 36 = 64 » (carrés)
        H, L, D = (float(v.replace(",", ".")) for v in (H, L, D))
        if abs(H - L - D) < 1e-6 and abs(math.sqrt(H) * 10 - round(math.sqrt(H) * 10)) < 1e-6:
            keys.add("pb:%s|%s" % (n(math.sqrt(H)), n(math.sqrt(L))))
    for a, b in re.findall(r"rectangle mesure ([\d,]+) cm sur ([\d,]+) cm", t):
        x, y = sorted([float(a.replace(",", ".")), float(b.replace(",", "."))])
        keys.add("rc:%s|%s" % (n(x), n(y)))
    for c in re.findall(r"isocèle a une hypoténuse de ([\d,]+) cm", t):
        keys.add("is:%s" % n(c))
print(len(keys), "clés :", sorted(keys), file=sys.stderr)
print(json.dumps(sorted(fnv(k) for k in keys)))
