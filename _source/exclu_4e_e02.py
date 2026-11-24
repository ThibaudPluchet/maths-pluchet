"""Empreintes des questions des sujets de l'évaluation commune 4e E02 (N11 quatrième proportionnelle, N12 proportionnalité et graphique, 35 min).

Usage : python3 _source/exclu_4e_e02.py <PDF de tous les sujets : A, B et PAP de chaque classe, corrigés de préférence>...
Affiche le tableau JSON d'empreintes FNV-1a à coller dans la constante EXCLU de exos/4e-e02-eval.html.
Clés (nombres écrits avec une virgule décimale, ex. 4,2) :
  q4:<facteur 1>|<facteur 2>|<diviseur>   tout calcul « a × b ÷ c » (quatrième proportionnelle, problème, bonus) ; facteurs triés
  mul:<facteur 1>|<facteur 2>            tout produit « a × b = c » (produits en croix, calcul hors du graphique) ; facteurs triés
  tb:<a>|<b>|<c>|<d>                      tableaux à deux lignes [a b / c d] lus dans les sujets élèves
"""
import json, re, subprocess, sys

def fnv(s):
    h = 0x811c9dc5
    for ch in s.encode("utf-8"):
        h ^= ch; h = (h * 0x01000193) & 0xffffffff
    return "%08x" % h

def n(x):
    v = float(x.replace(" ", "").replace(" ", "").replace(",", "."))
    return ("%g" % v).replace(".", ",")

NUM = r"(\d+(?:[  ]\d{3})*(?:,\d+)?)"
keys = set()
for path in sys.argv[1:]:
    t = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True).stdout
    t = t.replace("−", "-")
    for a, b, c in re.findall(NUM + r"\s*×\s*" + NUM + r"\s*÷\s*" + NUM, t):
        x, y = sorted([n(a), n(b)])
        keys.add("q4:%s|%s|%s" % (x, y, n(c)))
    for a, b in re.findall(NUM + r"\s*×\s*" + NUM + r"\s*=", t):
        x, y = sorted([n(a), n(b)])
        keys.add("mul:%s|%s" % (x, y))
print(len(keys), "clés :", sum(k.startswith("q4") for k in keys), "quatrièmes proportionnelles,",
      sum(k.startswith("mul") for k in keys), "produits", file=sys.stderr)
print(json.dumps(sorted(fnv(k) for k in keys)))
