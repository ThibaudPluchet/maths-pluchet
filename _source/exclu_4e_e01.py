"""Empreintes des questions des sujets de l'évaluation 4e E01 (N10, théorème de Pythagore, 35 min).

Usage : python3 _source/exclu_4e_e01.py <PDF de tous les sujets : A, B et PAP de chaque classe, élève ou corrigé>...
Affiche le tableau JSON d'empreintes FNV-1a à coller dans la constante EXCLU de exos/4e-e01-eval.html.
Clés (nombres écrits avec une virgule décimale, ex. 6,5) :
  tr:<lettres triées>|<sommet de l'angle droit>   triangles nommés
  hy:<petit côté>|<grand côté>                      calcul de l'hypoténuse (exercice 3)
  co:<hypoténuse>|<côté connu>                      calcul d'un côté de l'angle droit (exercices 4 et 5)
  pb:<hypoténuse>|<côté connu>                      tout calcul « H² − L² = D » avec des longueurs à une décimale (problème)
  rc:<petit>|<grand>, ca:<côté>, is:<hypoténuse>, eq:<côté>, qd:<petit>|<grand>, ec:<échelle>|<pied>|<recul>   bonus
"""
import json, re, subprocess, sys, math

def fnv(s):
    h = 0x811c9dc5
    for ch in s.encode("utf-8"):
        h ^= ch; h = (h * 0x01000193) & 0xffffffff
    return "%08x" % h

def f(x): return float(str(x).replace(",", "."))
def n(x): return ("%g" % f(x)).replace(".", ",")
def one_dec(v): return abs(v * 10 - round(v * 10)) < 1e-6

keys = set()
for path in sys.argv[1:]:
    t = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True).stdout
    t = re.sub(r"\s+", " ", t).replace(" ,", ",")
    t = re.sub(r"(?<=[A-Z]) (?=[A-Z](?![a-zé]))", "", t)   # « K LM » -> « KLM »
    L = r"([A-Z] ?[A-Z] ?[A-Z])"
    for name, r in re.findall(L + r" (?:est )?rectangle en ([A-Z])", t):
        keys.add("tr:%s|%s" % ("".join(sorted(name.replace(" ", ""))), r))
    # « ABC est rectangle en B, BC = 8 cm et AB = 5 cm. Calcule AC » / « …, avec AB = 17 cm et AC = 8 cm »
    for name, r, s1, a, s2, b in re.findall(L + r" est rectangle en ([A-Z]), (?:avec )?([A-Z] ?[A-Z]) = ([\d,]+) cm et ([A-Z] ?[A-Z]) = ([\d,]+) cm", t):
        s1 = s1.replace(" ", "")
        if r in s1:                                  # deux côtés de l'angle droit : on calcule l'hypoténuse
            x, y = sorted([f(a), f(b)]); keys.add("hy:%s|%s" % (n(x), n(y)))
        else:                                        # hypoténuse puis un côté : on calcule l'autre côté
            keys.add("co:%s|%s" % (n(a), n(b)))
    for H, Lq, D in re.findall(r"(?=(?<![\d,])([\d,]+) − ([\d,]+) (?:\[0,5\] )?= ([\d,]+))", t):
        H, Lq, D = f(H), f(Lq), f(D)
        if abs(H - Lq - D) < 1e-6 and one_dec(math.sqrt(H)) and one_dec(math.sqrt(Lq)):
            keys.add("pb:%s|%s" % (n(math.sqrt(H)), n(math.sqrt(Lq))))
    for a, b in re.findall(r"rectangle mesure ([\d,]+) cm sur ([\d,]+) cm", t):
        x, y = sorted([f(a), f(b)]); keys.add("rc:%s|%s" % (n(x), n(y)))
    for c in re.findall(r"carré a des côtés de ([\d,]+) cm", t): keys.add("ca:%s" % n(c))
    for c in re.findall(r"isocèle a une hypoténuse de ([\d,]+) cm", t): keys.add("is:%s" % n(c))
    for c in re.findall(r"équilatéral a des côtés de ([\d,]+) cm", t): keys.add("eq:%s" % n(c))
    for a, b in re.findall(r"de ([\d,]+) carreaux vers la droite puis de ([\d,]+) carreaux", t):
        x, y = sorted([f(a), f(b)]); keys.add("qd:%s|%s" % (n(x), n(y)))
    for e, p, d in re.findall(r"échelle de ([\d,]+) m est posée contre un mur vertical, son pied à ([\d,]+) m du mur\. On recule le pied de ([\d,]+) m", t):
        keys.add("ec:%s|%s|%s" % (n(e), n(p), n(d)))
print(len(keys), "clés :", sorted(keys), file=sys.stderr)
print(json.dumps(sorted(fnv(k) for k in keys)))
