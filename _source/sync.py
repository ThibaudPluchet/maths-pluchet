"""Synchronise le site élèves avec la page enseignant (artifact « Progressions 4e et 3e »).

Usage :
  python3 sync.py plan  <page.html> <db_dir> <repo_dir>             -> écrit <db_dir>/need.json (PDF à récupérer)
  python3 sync.py build <page.html> <db_dir> <repo_dir> <pdf_dir>   -> met à jour docs/ et data.js dans le dépôt

<db_dir> contient les exports ArtifactData : suivi/*.json, suivi3e/*.json, config/classes.json, config/classes3e.json.
Cases de la page enseignant, par notion : d<k> = documents élèves publiés pour la classe k (hors évaluations),
e<k> = évaluation (sujet élève) et sa correction (version PROF) publiées pour la classe k.
Si l'évaluation existe en plusieurs sujets (PDF du dossier Evaluation, champs c = classe et s = sujet dans DOCS),
la classe k ne reçoit que ses propres sujets et leurs corrections.
Les PDF d'évaluation peuvent être regroupés par la page enseignant dans un paquet docs/<niveau>/nXX/evaluations.json
(champ z dans DOCS : {chemin du PDF: contenu en base64}) : plan demande alors le paquet, et build en extrait les PDF.
Seuls les PDF ÉLÈVE cochés sont copiés dans le dépôt, sauf le cours (version PROF, complétée) et la correction de l'évaluation.
L'évaluation aménagée (PAP) n'est jamais publiée.
"""
import json, os, re, sys, glob, shutil, base64

STORE = {"4e": ("suivi", "classes"), "3e": ("suivi3e", "classes3e")}
TYPES = {"Activité": "activite", "Cours à trous": "cours", "Exercices": "exercices", "Évaluation": "evaluation",
         "Correction": "correction", "Carte mentale": "carte", "Fiche de révision": "revision"}
LABELS = {"Cours à trous": "Cours (complété)", "Exercices": "Fiche d'exercices", "Correction": "Correction de l'évaluation"}
EVALS = {"evaluation", "correction"}
# Versions PROF publiées : cours complété et correction de l'évaluation (sous un autre libellé)
PROF_OK = {"Cours à trous": "Cours à trous", "Évaluation": "Correction"}


def js_const(html, name):
    m = re.search(r"const " + name + r" = (\{.*?\});\n", html, re.S)
    if not m:
        sys.exit(f"Constante {name} introuvable dans la page enseignant")
    return json.loads(m.group(1))


def load(page, dbdir):
    html = open(page, encoding="utf-8").read()
    levels, docs = js_const(html, "LEVELS"), js_const(html, "DOCS")
    classes, data, wanted = {}, {"niveaux": {}}, {}
    global BUNDLE
    BUNDLE = {d["p"]: d["z"] for lv in docs["levels"].values() for L in lv.values() for d in L if d.get("z")}
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
                    # Cours : version PROF (complétée) à la place du cours à trous ; évaluation : sujet ÉLÈVE + correction PROF
                    if d["w"] == "PROF":
                        if d["l"] not in PROF_OK:
                            continue
                        lab = PROF_OK[d["l"]]
                    elif d["l"] == "Cours à trous" or d["l"] not in TYPES:
                        continue
                    else:
                        lab = d["l"]
                    t = TYPES[lab]
                    cls = show_eval if t in EVALS else show_docs
                    label = LABELS.get(lab, lab)
                    # Évaluation en plusieurs sujets (dossier Evaluation) : chaque PDF porte sa classe (c) et
                    # son sujet (s) ; il n'est publié que pour cette classe, si sa case « Éval » est cochée.
                    if d.get("c"):
                        cls = [c for c in cls if c == d["c"]]
                        if d.get("s"):
                            label += " (sujet " + d["s"] + ")"
                    if not cls:
                        continue
                    items.append({"type": t, "label": label, "href": d["p"], "cls": cls, "_s": d.get("s") or ""})
                    wanted[d["p"]] = d.get("b")
                items.sort(key=lambda i: (list(TYPES.values()).index(i["type"]), i.pop("_s")))
                if n.get("alea") and show_docs:
                    items.append({"type": "alea", "label": "Exercices en ligne (MathALÉA)", "href": n["alea"], "cls": show_docs})
                for v in n.get("vids") or []:
                    items.append({"type": "video", "label": "Vidéo : " + v["l"], "href": v["u"], "cls": sorted(set(show_docs) | set(show_eval))})
                notions.append({"num": n["n"], "titre": n["t"], "cls": sorted(set(show_docs) | set(show_eval)), "items": items})
            if notions:
                seqs.append({"num": seq["n"], "titre": seq["t"], "notions": notions})
        data["niveaux"][lv] = seqs
    data["classes"] = classes
    return data, wanted


BUNDLE = {}


def main():
    mode, page, dbdir, repo = sys.argv[1:5]
    data, wanted = load(page, dbdir)
    if mode == "plan":
        missing = [p for p, b in wanted.items() if not os.path.exists(os.path.join(repo, p)) or (b and os.path.getsize(os.path.join(repo, p)) != b)]
        # PDF rangés dans un paquet evaluations.json : on demande le paquet (une seule fois) plutôt que le PDF
        need = list(dict.fromkeys(BUNDLE.get(p, p) for p in missing))
        print(f"{len(missing)} PDF à mettre à jour")
        json.dump(need, open(f"{dbdir}/need.json", "w"), ensure_ascii=False)
        print(f"{len(wanted)} PDF publiés au total, {len(need)} fichier(s) à récupérer")
        return
    pdfdir = sys.argv[5]
    bundles = {}
    for p in wanted:
        dst = os.path.join(repo, p)
        src = os.path.join(pdfdir, p)
        z = BUNDLE.get(p)
        if not os.path.exists(src) and z and os.path.exists(os.path.join(pdfdir, z)):
            if z not in bundles:
                bundles[z] = json.load(open(os.path.join(pdfdir, z), encoding="utf-8"))
            if p in bundles[z]:
                raw = base64.b64decode(bundles[z][p])
                if raw[:5] != b"%PDF-":
                    sys.exit(f"Contenu invalide dans {z} : {p}")
                if wanted[p] and len(raw) != wanted[p]:
                    sys.exit(f"Taille inattendue pour {p} dans {z} : {len(raw)} au lieu de {wanted[p]}")
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                open(dst, "wb").write(raw)
                continue
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)
        elif not os.path.exists(dst):
            sys.exit(f"PDF manquant : {p}")
    removed = 0
    for f in glob.glob(os.path.join(repo, "docs", "**", "*.pdf"), recursive=True):
        if os.path.relpath(f, repo).replace(os.sep, "/") not in wanted:
            os.remove(f); removed += 1
    json.dump(data, open(os.path.join(repo, "data.json"), "w", encoding="utf-8"), ensure_ascii=False)
    # data.js : gardé pour les navigateurs qui ont encore l'ancienne page en cache
    open(os.path.join(repo, "data.js"), "w", encoding="utf-8").write(
        "window.SITE_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n")
    print(f"{len(wanted)} PDF en ligne, {removed} retiré(s)")


if __name__ == "__main__":
    main()
