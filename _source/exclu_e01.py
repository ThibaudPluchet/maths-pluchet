"""Empreintes des questions des sujets de l'évaluation commune 3e E01 (coordonnées terrestres, équations).

Usage : python3 _source/exclu_e01.py <PDF corrigés ou élève de E01>...
Affiche le tableau JSON d'empreintes FNV-1a à coller dans la constante EXCLU de exos/3e-e01-eval.html.
Clés : pt:<lat>|<lon> (points, latitudes S et longitudes O négatives), eq:<a>|<b>|<c>|<d> (équation ax+b = cx+d),
pb:<prix>|<forfait>|<prix réduit>, bb:<diviseur>|<b>|<c> (bonus x/a + b = x − c).
"""
import json, re, subprocess, sys

def fnv(s):
    h = 0x811c9dc5
    for ch in s.encode("utf-8"):
        h ^= ch; h = (h * 0x01000193) & 0xffffffff
    return "%08x" % h

def lin(side):
    s = side.replace("−", "-").replace(" ", "")
    if not re.fullmatch(r"[-+]?(\d*x|\d+)([-+](\d*x|\d+))*", s): return None
    a = b = 0
    for sg, t in re.findall(r"([-+]?)(\d*x|\d+)", s):
        k = -1 if sg == "-" else 1
        if t.endswith("x"): a += k * (int(t[:-1]) if t[:-1] else 1)
        else: b += k * int(t)
    return a, b

keys = set()
for f in sys.argv[1:]:
    t = subprocess.run(["pdftotext", "-layout", f, "-"], capture_output=True, text=True).stdout
    t = t.replace("◦", "°")
    for la, ns, lo, eo in re.findall(r"\((\d+)\s*°\s*([NS])\s*;\s*(\d+)\s*°\s*([EO])\)", t):
        keys.add("pt:%d|%d" % (int(la) * (1 if ns == "N" else -1), int(lo) * (1 if eo == "E" else -1)))
    for L, R in re.findall(r"(?<![\d/.])((?:[−\-]?\d*x(?: [+−] \d+x?)*)|(?:\d+ [+−] \d*x(?: [+−] \d+x?)*)) ?= ?([−\-]?\d*x?(?: [+−] \d+x?)*)", t):
        l, r = lin(L), lin(R)
        if l and r and (l[0] or r[0]) and not (l[0] == 1 and l[1] == 0 and r[0] == 0):
            keys.add("eq:%d|%d|%d|%d" % (l + r))
    for p, F, q in re.findall(r"co[uû]te (\d+) C\.? .*?paie (\d+) C une fois,\s*puis (\d+) C", t, re.S):
        keys.add("pb:%s|%s|%s" % (p, F, q))
    for b, c, a in re.findall(r"Résous l’équation\s*([+−]\s*\d+)\s*=\s*x\s*−\s*(\d+)\.\s*x\s*=.*?par (\d)", t, re.S):
        keys.add("bb:%s|%d|%s" % (a, int(b.replace("−", "-").replace(" ", "")), c))
print(len(keys), "questions :", sorted(k.split(":")[0] for k in keys).count("eq"), "équations", file=sys.stderr)
print(json.dumps(sorted(fnv(k) for k in keys)))
