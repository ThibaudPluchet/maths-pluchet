"""Construit le site élèves à partir de notions.json + distribution.json.
Seuls les PDF distribués à au moins une classe sont copiés dans le site."""
import json, os, re, shutil, unicodedata, configparser, glob
SRC = "/mnt/user-data/uploads/Tests IA"
OUT = "/home/claude/site"
DOCS = [("activite","1. Activité","Activité"),("cours","2. Cours à trous","Cours à trous"),
        ("exercices","3. Exercices","Exercices"),("evaluation","4. Évaluation","Évaluation"),
        ("evaluation-pap","4. Évaluation PAP","Évaluation (aménagée)"),
        ("carte","5. Carte mentale","Carte mentale"),("revision","6. Fiche de révision","Fiche de révision")]
CLASSES = {"4e":["4G3","4G4","4G5"],"3e":["3B","3D","3E"]}
N = json.load(open("notions.json"))
dist = json.load(open("distribution.json"))
def strip(s): return unicodedata.normalize("NFC", s)
def url_of(p):
    for line in open(p, encoding="utf-8", errors="ignore"):
        if line.startswith("URL="): return line[4:].strip()
data = {"classes": CLASSES, "niveaux": {}}
needed = set(x for c in dist.values() for x in c)
os.makedirs(OUT, exist_ok=True)
if os.path.isdir(f"{OUT}/docs"): shutil.rmtree(f"{OUT}/docs")
for lvl, L in N.items():
    seqs = []
    for s, n, vids in L:
        sn, nn = int(s[1:3]), int(n[1:3])
        code = f"{lvl}-N{nn:02d}"
        d = f"{SRC}/{lvl}/{s}/{n}"
        pre = f"{lvl} - S{sn}N{nn} - ELEVE - "
        items = []
        for key, fname, label in DOCS:
            iid = f"{code}-{key}"
            it = {"id": iid, "type": key, "label": label}
            if iid in needed:
                src = f"{d}/{pre}{fname}.pdf"
                dst = f"docs/{lvl}/N{nn:02d}-{key}.pdf"
                if not os.path.exists(src): raise SystemExit(f"PDF manquant : {src}")
                os.makedirs(os.path.dirname(f"{OUT}/{dst}"), exist_ok=True)
                shutil.copy(src, f"{OUT}/{dst}"); it["href"] = dst
            items.append(it)
        for i, v in enumerate(vids):
            p = f"{d}/{pre}" + ("7. Vidéo.url" if not v else f"7. Vidéo ({v}).url")
            items.append({"id": f"{code}-video{i+1}", "type": "video",
                          "label": "Vidéo" + (f" : {v}" if v else ""), "href": url_of(p)})
        seq = s[6:]
        if not seqs or seqs[-1]["titre"] != seq: seqs.append({"num": sn, "titre": seq, "notions": []})
        seqs[-1]["notions"].append({"code": code, "num": nn, "titre": n[6:], "items": items})
    data["niveaux"][lvl] = seqs
# on ne garde, pour chaque classe, que les identifiants ; les href des docs non distribués n'existent pas
data["distribution"] = dist
open(f"{OUT}/data.js", "w", encoding="utf-8").write("window.SITE_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n")
shutil.copy("index.html", f"{OUT}/index.html")
open(f"{OUT}/.nojekyll","w").close()
print("PDF publiés :", len(glob.glob(f"{OUT}/docs/*/*.pdf")))
