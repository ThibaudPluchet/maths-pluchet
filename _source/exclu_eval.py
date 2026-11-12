"""Empreintes des questions des vrais sujets d'évaluation (PDF élève) à exclure des exerciseurs.

Usage : python3 _source/exclu_eval.py docs/4e/n01/eleve-4-evaluation-*.pdf
Affiche un tableau JSON d'empreintes FNV-1a (8 hex) à coller dans la constante EXCLU de l'exerciseur.
Seules les empreintes sont publiées : les nombres des sujets n'apparaissent pas dans la page.
"""
import json, re, subprocess, sys

def fnv(s):
    h = 0x811c9dc5
    for ch in s.encode("utf-8"):
        h ^= ch; h = (h * 0x01000193) & 0xffffffff
    return "%08x" % h

def n(x):
    x = x.replace("−", "-").replace(",", ".").replace("+", "")
    v = float(x); return str(int(v)) if v == int(v) else str(v)

R = r"([+−]?\d+(?:,\d+)?)"
keys = set()
for f in sys.argv[1:]:
    t = subprocess.run(["pdftotext", "-layout", f, "-"], capture_output=True, text=True).stdout
    t = re.sub(r"[ \t]+", " ", t)
    for a, b in re.findall(r"[abcd]\) \(" + R + r"\) \+ \(" + R + r"\) =", t): keys.add("add:" + n(a) + "|" + n(b))
    for a, b in re.findall(r"[ABCD] = \(" + R + r"\) − \(" + R + r"\)", t): keys.add("sub:" + n(a) + "|" + n(b))
    m = re.search(r"E = \(" + R + r"\) \+ \(" + R + r"\) − \(" + R + r"\) − \(" + R + r"\)", t)
    if m: keys.add("E:" + ",".join(n(x) for x in m.groups()))
    m = re.search(r"F = (−?\d+) ([+−]) (\d+) ([+−]) (\d+) ([+−]) (\d+) ([+−]) (\d+)", t)
    if m:
        g = m.groups(); vals = [n(g[0])] + [n(("-" if g[i] == "−" else "") + g[i + 1]) for i in (1, 3, 5, 7)]
        keys.add("F:" + ",".join(vals))
    m = re.search(r"a\) \(" + R + r"\) − [. ]+= " + R, t)
    if m: keys.add("b1:" + n(m.group(1)) + "|" + n(m.group(2)))
    m = re.search(r"b\) [. ]+\+ \(" + R + r"\) − \(" + R + r"\) = " + R, t)
    if m: keys.add("b2:" + "|".join(n(x) for x in m.groups()))
    m = re.search(r"il fait (−?\d+) °C à.*?monte de (\d+) °C.*?baisse de (\d+) °C", t, re.S)
    if m: keys.add("pb:" + n(m.group(1)) + "|" + n(m.group(2)) + "|" + n("-" + m.group(3)))
    m = re.search(r"trouve à (−?\d+) m.*?descend de (\d+) m, puis\s+remonte de (\d+) m", t, re.S)
    if m: keys.add("pb:" + n(m.group(1)) + "|" + n("-" + m.group(2)) + "|" + n(m.group(3)))
print(len(keys), "questions", file=sys.stderr)
print(json.dumps(sorted(fnv(k) for k in keys)))
