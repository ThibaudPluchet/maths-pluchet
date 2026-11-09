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
c<k> (Fait en classe) + d<k> = correction de la fiche d'exercices (version PROF) publiée pour la classe k.
Seuls les PDF ÉLÈVE cochés sont copiés dans le dépôt, sauf le cours (version PROF, complétée) et les corrections (évaluation, fiche d'exercices).
L'évaluation aménagée (PAP) n'est jamais publiée.
"""
import json, os, re, sys, glob, shutil, base64, hmac, hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Corrections de fiche d'exercices : chiffrées par classe (AES-GCM) dans enc/, jamais en clair dans le dépôt public.
# Clé d'une classe = HMAC-SHA256(SITE_KEY, "classe:<nom>")[:16] ; elle n'existe que dans l'adresse secrète de la classe
# (#4e3/<clé>), si bien qu'une autre classe ne peut ni trouver ni lire ces corrections.
MASTER = os.environ.get("SITE_KEY", "")
PRIVATE = {"correction-exo"}


def classkey(c):
    return hmac.new(bytes.fromhex(MASTER), ("classe:" + c).encode(), hashlib.sha256).digest()[:16]


def b64u(b):
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def encname(key, label):
    return "enc/" + hmac.new(key, label.encode(), hashlib.sha256).hexdigest()[:20] + ".bin"


def encrypt(key, raw):
    nonce = hmac.new(key, hashlib.sha256(raw).digest(), hashlib.sha256).digest()[:12]   # déterministe : pas de changement inutile
    return nonce + AESGCM(key).encrypt(nonce, raw, None)

STORE = {"4e": ("suivi", "classes"), "3e": ("suivi3e", "classes3e")}
TYPES = {"Activité": "activite", "Cours à trous": "cours", "Exercices": "exercices",
         "Correction exercices": "correction-exo", "Évaluation": "evaluation",
         "Correction": "correction", "Carte mentale": "carte", "Fiche de révision": "revision"}
LABELS = {"Cours à trous": "Cours (complété)", "Exercices": "Fiche d'exercices", "Correction": "Correction de l'évaluation",
          "Correction exercices": "Correction de la fiche d'exercices"}
EVALS = {"evaluation", "correction"}
# Versions PROF publiées : cours complété, correction de l'évaluation et correction de la fiche d'exercices
PROF_OK = {"Cours à trous": "Cours à trous", "Évaluation": "Correction", "Exercices": "Correction exercices"}


def js_const(html, name):
    m = re.search(r"const " + name + r" = (\{.*?\});\n", html, re.S)
    if not m:
        sys.exit(f"Constante {name} introuvable dans la page enseignant")
    return json.loads(m.group(1))


def load(page, dbdir):
    html = open(page, encoding="utf-8").read()
    levels, docs = js_const(html, "LEVELS"), js_const(html, "DOCS")
    classes, data, wanted = {}, {"niveaux": {}}, {}
    global SECRET
    SECRET = {}
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
                # Correction de la fiche d'exercices : quand la notion est « Fait en classe » (et ses documents publiés)
                show_fait = [noms[k] for k in range(len(noms)) if s.get(f"c{k+1}") and s.get(f"d{k+1}")]
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
                    cls = show_eval if t in EVALS else show_fait if t == "correction-exo" else show_docs
                    label = LABELS.get(lab, lab)
                    # Évaluation en plusieurs sujets (dossier Evaluation) : chaque PDF porte sa classe (c) et
                    # son sujet (s) ; il n'est publié que pour cette classe, si sa case « Éval » est cochée.
                    if d.get("c"):
                        cls = [c for c in cls if c == d["c"]]
                        if d.get("s"):
                            label += " (sujet " + d["s"] + ")"
                    if not cls:
                        continue
                    if t in PRIVATE:
                        for c in cls:
                            SECRET.setdefault(c, []).append({"lv": lv, "num": n["n"], "type": t, "label": label, "src": d["p"], "b": d.get("b")})
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
SECRET = {}


def secret_plan():
    """{classe: [(élément, chemin chiffré)]}"""
    if not re.fullmatch(r"[0-9a-f]{64}", MASTER):
        if SECRET:
            print("ATTENTION : SITE_KEY absente, corrections chiffrées laissées telles quelles (non mises à jour)")
        return {}
    out = {}
    for c, its in SECRET.items():
        k = classkey(c)
        out[c] = [(it, encname(k, f"{it['src']}:{it['b']}")) for it in its]
    return out


def main():
    mode, page, dbdir, repo = sys.argv[1:5]
    data, wanted = load(page, dbdir)
    if mode == "plan":
        missing = [p for p, b in wanted.items() if not os.path.exists(os.path.join(repo, p)) or (b and os.path.getsize(os.path.join(repo, p)) != b)]
        # PDF rangés dans un paquet evaluations.json : on demande le paquet (une seule fois) plutôt que le PDF
        for c, lst in secret_plan().items():
            missing += [it["src"] for it, e in lst if not os.path.exists(os.path.join(repo, e))]
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
    keep = set()
    if MASTER:
        sp = secret_plan()
        noms = [c for l in data["classes"].values() for c in l]
        for c in noms:
            k = classkey(c)
            man = []
            for it, e in sp.get(c, []):
                dst = os.path.join(repo, e)
                if not os.path.exists(dst):
                    src = os.path.join(pdfdir, it["src"])
                    if not os.path.exists(src):
                        sys.exit(f"PDF manquant : {it['src']}")
                    raw = open(src, "rb").read()
                    if raw[:5] != b"%PDF-":
                        sys.exit(f"Contenu invalide : {it['src']}")
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    open(dst, "wb").write(encrypt(k, raw))
                keep.add(e)
                man.append({"lv": it["lv"], "num": it["num"], "type": it["type"], "label": it["label"], "e": e})
            e = encname(k, "manifest")
            os.makedirs(os.path.join(repo, "enc"), exist_ok=True)
            open(os.path.join(repo, e), "wb").write(encrypt(k, json.dumps(man, ensure_ascii=False, sort_keys=True).encode()))
            keep.add(e)
    else:
        secret_plan()
    removed = 0
    for f in (glob.glob(os.path.join(repo, "enc", "*.bin")) if MASTER else []):
        if os.path.relpath(f, repo).replace(os.sep, "/") not in keep:
            os.remove(f); removed += 1
    for f in glob.glob(os.path.join(repo, "docs", "**", "*.pdf"), recursive=True):
        if os.path.relpath(f, repo).replace(os.sep, "/") not in wanted:
            os.remove(f); removed += 1
    json.dump(data, open(os.path.join(repo, "data.json"), "w", encoding="utf-8"), ensure_ascii=False)
    # data.js : gardé pour les navigateurs qui ont encore l'ancienne page en cache
    open(os.path.join(repo, "data.js"), "w", encoding="utf-8").write(
        "window.SITE_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n")
    print(f"{len(wanted)} PDF en ligne, {sum(len(v) for v in SECRET.values())} correction(s) chiffrée(s), {removed} fichier(s) retiré(s)")
    if len(sys.argv) > 6 and sys.argv[6] == "--liens":
        for c in [c for l in data["classes"].values() for c in l]:
            print(f"{c} : https://thibaudpluchet.github.io/maths-pluchet/#{c}/{b64u(classkey(c))}")


if __name__ == "__main__":
    main()
