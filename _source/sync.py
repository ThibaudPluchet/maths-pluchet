"""Synchronise le site élèves avec la page enseignant (artifact « Progressions 4e et 3e »).

Usage :
  python3 sync.py plan  <page.html> <db_dir> <repo_dir>             -> écrit <db_dir>/need.json (PDF à récupérer)
  python3 sync.py build <page.html> <db_dir> <repo_dir> <pdf_dir>   -> met à jour docs/ et data.js dans le dépôt

<db_dir> contient les exports ArtifactData : suivi/*.json, suivi3e/*.json, config/classes.json, config/classes3e.json.
Cases de la page enseignant, par notion : d<k> = documents élèves publiés pour la classe k (hors évaluations),
e<k> = évaluations publiées pour la classe k. Seuls les PDF ÉLÈVE cochés sont copiés dans le dépôt.
"""
import json, os, re, sys, glob, shutil

STORE = {"4e": ("suivi", "classes"), "3e": ("suivi3e", "classes3e")}
TYPES = {"Activité": "activite", "Cours à trous": "cours", "Exercices": "exercices", "Évaluation": "evaluation",
         "Évaluation PAP": "evaluation-pap", "Carte mentale": "carte", "Fiche de révision": "revision"}
LABELS = {"Évaluation PAP": "Évaluation (aménagée)"}
EVALS = {"evaluation", "evaluation-pap"}


def js_const(html, name):
    m = re.search(r"const " + name + r" = (\{.*?\});\n", html, re.S)
    if not m:
        sys.exit(f"Constante {name} introuvable dans la page enseignant")
    return json.loads(m.group(1))


def load(page, dbdir):
    html = open(page, encoding="utf-8").read()
    levels, docs = js_const(html, "LEVELS"), js_const(html, "DOCS")
    classes, data, wanted = {}, {"niveaux": {}}, {}
    for lv, (suivi, cfg) in STORE.items():
        try:
            noms = json.load(open(f"{dbdir}/config/{cfg}.json")).get("noms") or []
        except FileNotFoundError:
            noms = []
        noms = [n for n in noms if n]
        classes[lv] = noms
        state = {}
        for f in glob.glob(f"{dbdir}/{suivi}/*.json"):
            state[os.path.basename(f)[:-5]] = json.load(open(f))
        seqs = []
        for seq in levels[lv]["seqs"]:
            notions = []
            for n in seq["notions"]:
                s = state.get("n%02d" % n["n"], {})
                show_docs = [noms[k] for k in range(len(noms)) if s.get(f"d{k+1}")]
                show_eval = [noms[k] for k in range(len(noms)) if s.get(f"e{k+1}")]
                if not show_docs and not show_eval:
                    continue
                items = []
                for d in docs["levels"].get(lv, {}).get(str(n["n"]), []):
                    if d["w"] != "ELEVE" or d["l"] not in TYPES:
                        continue
                    t = TYPES[d["l"]]
                    cls = show_eval if t in EVALS else show_docs
                    if not cls:
                        continue
                    items.append({"type": t, "label": LABELS.get(d["l"], d["l"]), "href": d["p"], "cls": cls})
                    wanted[d["p"]] = d.get("b")
                items.sort(key=lambda i: list(TYPES.values()).index(i["type"]))
                for v in n.get("vids") or []:
                    items.append({"type": "video", "label": "Vidéo : " + v["l"], "href": v["u"], "cls": sorted(set(show_docs) | set(show_eval))})
                notions.append({"num": n["n"], "titre": n["t"], "cls": sorted(set(show_docs) | set(show_eval)), "items": items})
            if notions:
                seqs.append({"num": seq["n"], "titre": seq["t"], "notions": notions})
        data["niveaux"][lv] = seqs
    data["classes"] = classes
    return data, wanted


def main():
    mode, page, dbdir, repo = sys.argv[1:5]
    data, wanted = load(page, dbdir)
    if mode == "plan":
        need = [p for p, b in wanted.items() if not os.path.exists(os.path.join(repo, p)) or (b and os.path.getsize(os.path.join(repo, p)) != b)]
        json.dump(need, open(f"{dbdir}/need.json", "w"), ensure_ascii=False)
        print(f"{len(wanted)} PDF publiés au total, {len(need)} à récupérer")
        return
    pdfdir = sys.argv[5]
    for p in wanted:
        dst = os.path.join(repo, p)
        src = os.path.join(pdfdir, p)
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)
        elif not os.path.exists(dst):
            sys.exit(f"PDF manquant : {p}")
    removed = 0
    for f in glob.glob(os.path.join(repo, "docs", "**", "*.pdf"), recursive=True):
        if os.path.relpath(f, repo).replace(os.sep, "/") not in wanted:
            os.remove(f); removed += 1
    open(os.path.join(repo, "data.js"), "w", encoding="utf-8").write(
        "window.SITE_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n")
    print(f"{len(wanted)} PDF en ligne, {removed} retiré(s)")


if __name__ == "__main__":
    main()
