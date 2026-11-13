"""Synchronise le site élèves avec la page enseignant (artifact « Progressions »).

Usage :
  python3 sync.py plan  <page.html> <db_dir> <repo_dir>             -> écrit <db_dir>/need.json (PDF à récupérer)
  python3 sync.py build <page.html> <db_dir> <repo_dir> <pdf_dir>   -> met à jour docs/ et data.js dans le dépôt

<db_dir> contient les exports ArtifactData de chaque niveau présent dans la constante LEVELS de la page (6e, 5e, 4e, 3e) :
la 4e garde les noms d'origine (suivi/, evals/, config/classes.json), les autres niveaux ajoutent leur nom
(suivi3e/, evals3e/, config/classes3e.json ; suivi5e/, evals5e/, config/classes5e.json…).
« python3 sync.py collections <page.html> » affiche la liste des collections à exporter.
Cases de la page enseignant, par notion : d<k> = documents élèves publiés pour la classe k (hors évaluations),
Évaluations : pilotées par l'onglet Évaluations de la page enseignant (collection « evaluations », une évaluation déclarée
= {lv, ns, dates, doc: "N12" | "E01" | "", f: {k: faite}, r: {k: correction publiée}}) : pour la classe k, le sujet ÉLÈVE
est publié dès que l'évaluation est cochée « Faite » (f), la correction (évaluation version PROF) quand elle est cochée
« Correction » (r). doc = "N12" : évaluation de la notion 12 ; doc = "E01" : évaluation commune E01. Les anciennes cases
e<k> (onglet Notions) et c<k> des collections evals… ne publient plus rien.
Si l'évaluation existe en plusieurs sujets (PDF du dossier Evaluation, champs c = classe et s = sujet dans DOCS),
la classe k ne reçoit que ses propres sujets et leurs corrections.
Les PDF d'évaluation peuvent être regroupés par la page enseignant dans un paquet docs/<niveau>/nXX/evaluations.json
(champ z dans DOCS : {chemin du PDF: contenu en base64}) : plan demande alors le paquet, et build en extrait les PDF.
Jauge « Imprimé / Distribué / Complété » de la page enseignant (champs pd<k><a|c|e|r> = 0 à 3, pour Activité, Cours,
Exercices, Fiche de révision) : un document élève est aussi publié pour la classe k dès qu'il y est au moins « Distribué » (2),
même sans d<k> ; le cours distribué entraîne aussi carte mentale, vidéos, MathALÉA et animations de la notion.
c<k> (Fait en classe) + d<k> (ou fiche d'exercices distribuée) = correction de la fiche d'exercices (version PROF) publiée pour la classe k.
Seuls les PDF ÉLÈVE cochés sont copiés dans le dépôt, sauf le cours (version PROF, complétée) et les corrections (évaluation, fiche d'exercices).
L'évaluation aménagée (PAP) n'est jamais publiée.
Évaluations communes à plusieurs notions (constante EVALS de la page : {niveau: [{id: "E01", ns: [15, 16, 17], docs}]}) :
publiées comme ci-dessus (évaluation déclarée reliée à E01) ; affichées après la dernière notion évaluée.
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

ORDER = ["6e", "5e", "4e", "3e"]


def suivi_of(lv):
    return "suivi" if lv == "4e" else "suivi" + lv


def cfg_of(lv):
    return "classes" if lv == "4e" else "classes" + lv


def evals_of(lv):
    return "evals" if lv == "4e" else "evals" + lv


def level_list(levels):
    return [l for l in ORDER if l in levels] + [l for l in levels if l not in ORDER]
TYPES = {"Activité": "activite", "Cours à trous": "cours", "Exercices": "exercices",
         "Correction exercices": "correction-exo", "Évaluation": "evaluation",
         "Correction": "correction", "Carte mentale": "carte", "Fiche de révision": "revision"}
LABELS = {"Cours à trous": "Cours (complété)", "Exercices": "Fiche d'exercices", "Correction": "Correction de l'évaluation",
          "Correction exercices": "Correction de la fiche d'exercices"}
EVALS = {"evaluation", "correction"}
PDKEY = {"activite": "a", "cours": "c", "exercices": "e", "revision": "r"}   # jauge de la page enseignant (pd<k><clé>)
# Versions PROF publiées : cours complété, correction de l'évaluation et correction de la fiche d'exercices
PROF_OK = {"Cours à trous": "Cours à trous", "Évaluation": "Correction", "Exercices": "Correction exercices"}


def js_const(html, name):
    m = re.search(r"const " + name + r" = (\{.*?\});\n", html, re.S)
    if not m:
        sys.exit(f"Constante {name} introuvable dans la page enseignant")
    return json.loads(m.group(1))


def js_const_opt(html, name):
    m = re.search(r"^const " + name + r" = ", html, re.M)
    return json.JSONDecoder().raw_decode(html, m.end())[0] if m else {}


# Animations : liens LINKS de la page enseignant vers des artifacts claude.ai (privés) ;
# leur page HTML est recopiée dans anim/<id>.html pour être accessible aux élèves.
ANIM_RE = re.compile(r"^https://claude\.ai/artifact/([A-Za-z0-9]+)(#.*)?$")
ANIMS = set()


def load(page, dbdir):
    html = open(page, encoding="utf-8").read()
    levels, docs = js_const(html, "LEVELS"), js_const(html, "DOCS")
    links = js_const_opt(html, "LINKS")
    try:
        inter = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "interactifs.json"), encoding="utf-8"))
    except FileNotFoundError:
        inter = {}
    evals = js_const_opt(html, "EVALS")
    ANIMS.clear()
    classes, data, wanted = {}, {"niveaux": {}}, {}
    global SECRET
    SECRET = {}
    global BUNDLE
    BUNDLE = {d["p"]: d["z"] for lv in docs["levels"].values() for L in lv.values() for d in L if d.get("z")}
    BUNDLE.update({d["p"]: d["z"] for L in evals.values() for e in L for d in e.get("docs", []) if d.get("z")})
    plans = []
    for f in sorted(glob.glob(f"{dbdir}/evaluations/*.json")):
        plans.append(json.load(open(f)))
    for lv in level_list(levels):
        suivi, cfg = suivi_of(lv), cfg_of(lv)
        try:
            noms = json.load(open(f"{dbdir}/config/{cfg}.json")).get("noms") or []
        except FileNotFoundError:
            noms = []
        noms = [n for n in noms if n]
        classes[lv] = noms
        state = {}
        for f in glob.glob(f"{dbdir}/{suivi}/*.json"):
            state[os.path.basename(f)[:-5]] = json.load(open(f))
        # évaluations déclarées : classes où le sujet (faite) et la correction sont publiés, par document relié (N12, E01)
        on = lambda p, fld, k: bool((p.get(fld) or {}).get(str(k + 1)) or (p.get(fld) or {}).get(k + 1))
        suj, cor = {}, {}
        for p in plans:
            if p.get("lv") != lv or not re.fullmatch(r"[NE]\d+", p.get("doc") or ""):
                continue
            for k in range(len(noms)):
                if on(p, "f", k):
                    suj.setdefault(p["doc"], set()).add(noms[k])
                    if on(p, "r", k):
                        cor.setdefault(p["doc"], set()).add(noms[k])
        seqs = []
        for seq in levels[lv]["seqs"]:
            notions = []
            # évaluations communes dont la dernière notion est dans cette séquence
            seq_nums = [n["n"] for n in seq["notions"]]
            for e in evals.get(lv, []):
                last = max(e["ns"])
                if last not in seq_nums:
                    continue
                show = sorted(suj.get(e["id"], ()))
                if not show:
                    continue
                items = eval_items(e["docs"], show, sorted(cor.get(e["id"], ())), wanted)
                if items:
                    titres = {x["n"]: x["t"] for sq in levels[lv]["seqs"] for x in sq["notions"]}
                    seq.setdefault("_ev", []).append((last, {"num": e["id"], "titre": "Évaluation commune · " + ", ".join("N%02d" % x for x in e["ns"]),
                                                             "ns": [{"num": x, "titre": titres.get(x, "")} for x in e["ns"]],
                                                             "cls": show, "items": items}))
            for n in seq["notions"]:
                s = state.get("n%02d" % n["n"], {})
                # document distribué (jauge ≥ 2) à la classe k : publié pour elle, même sans la case « Élèves » (d<k>)
                dist = lambda k, key: s.get(f"d{k+1}") or (s.get(f"pd{k+1}{key}") or 0) >= 2
                by_type = {t: [noms[k] for k in range(len(noms)) if dist(k, key)] for t, key in PDKEY.items()}
                # autres ressources (carte mentale, vidéos, MathALÉA, animations) : avec le cours
                show_docs = by_type["cours"]
                show_any = sorted({c for v in by_type.values() for c in v})
                show_eval = sorted(suj.get("N%d" % n["n"], ()))          # sujet : évaluation déclarée cochée « Faite »
                show_corr = sorted(cor.get("N%d" % n["n"], ()))          # correction : cochée « Correction »
                # Correction de la fiche d'exercices : quand la notion est « Fait en classe » (et la fiche publiée)
                show_fait = [noms[k] for k in range(len(noms)) if s.get(f"c{k+1}") and dist(k, "e")]
                if not show_any and not show_eval:
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
                    cls = show_eval if t == "evaluation" else show_corr if t == "correction" else show_fait if t == "correction-exo" else by_type.get(t, show_docs)
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
                for k in (inter.get(lv, {}).get(str(n["n"])) or []) if show_docs else []:
                    items.append({"type": "exo", "label": k["l"], "href": k["u"], "cls": show_docs})
                if n.get("alea") and show_docs:
                    items.append({"type": "alea", "label": "Exercices en ligne (MathALÉA)", "href": n["alea"], "cls": show_docs})
                for k in (links.get(lv, {}).get(str(n["n"])) or []) if show_docs else []:
                    m = ANIM_RE.match(k.get("u", ""))
                    if m:
                        ANIMS.add(m.group(1))
                        href = f"anim/{m.group(1)}.html" + (m.group(2) or "")
                    elif k.get("u", "").startswith("https://"):
                        href = k["u"]
                    else:
                        continue
                    items.append({"type": "anim", "label": k.get("l") or "Animation", "href": href, "cls": show_docs})
                for v in n.get("vids") or []:
                    items.append({"type": "video", "label": "Vidéo : " + v["l"], "href": v["u"], "cls": sorted(set(show_docs) | set(show_eval))})
                notions.append({"num": n["n"], "titre": n["t"], "cls": sorted(set(show_any) | set(show_eval)), "items": items})
            for last, ev in seq.pop("_ev", []):
                i = 0                                   # juste après la dernière notion évaluée (et les évaluations déjà placées)
                for j, x in enumerate(notions):
                    if isinstance(x["num"], int) and x["num"] <= last or isinstance(x["num"], str) and j <= i:
                        i = j + 1
                notions.insert(i, ev)
            if notions:
                seqs.append({"num": seq["n"], "titre": seq["t"], "notions": notions})
        data["niveaux"][lv] = seqs
    data["classes"] = classes
    data["planned"] = planned_evals(dbdir, levels, classes, inter)
    return data, wanted


def blanc_of(x):
    return (x.get("u") if isinstance(x, dict) else x) or ""


def planned_evals(dbdir, levels, classes, inter):
    """Évaluations déclarées dans la page enseignant (collection « evaluations ») : date par classe, notions, évaluation blanche.
    Chaque élève voit l'évaluation à venir de sa classe jusqu'au jour J inclus (le site compare la date au jour courant) ;
    une classe dont l'évaluation est cochée « faite » (f<k>) n'est plus listée."""
    out, blancs = [], inter.get("blancs", {})
    for f in sorted(glob.glob(f"{dbdir}/evaluations/*.json")):
        p = json.load(open(f))
        lv = p.get("lv")
        if lv not in levels or not classes.get(lv):
            continue
        noms, done = classes[lv], p.get("f") or {}
        dates = {noms[int(k) - 1]: d for k, d in (p.get("dates") or {}).items()
                 if d and str(k).isdigit() and 0 < int(k) <= len(noms) and not done.get(k) and not done.get(int(k))}
        if not dates:
            continue
        titles = {n["n"]: n["t"] for s in levels[lv]["seqs"] for n in s["notions"]}
        ns = [{"num": n, "titre": titles.get(n, "")} for n in p.get("ns") or []]
        doc = p.get("doc") or ""
        out.append({"id": os.path.basename(f)[:-5], "lv": lv, "nom": p.get("nom") or "", "doc": doc, "ns": ns, "dates": dates,
                    "commune": doc.startswith("E") or len(ns) > 1, "blanc": blanc_of(blancs.get(lv, {}).get(doc)),
                    "parNotion": (blancs.get(lv, {}).get(doc) or {}).get("notions", []) if isinstance(blancs.get(lv, {}).get(doc), dict) else []})
    return out


BUNDLE = {}
SECRET = {}


def eval_items(docs, show_eval, show_corr, wanted):
    """Sujets ÉLÈVE (classes show_eval) et corrections PROF (classes show_corr) d'une évaluation commune,
    chacun pour sa classe (jamais les PAP ni le préambule)."""
    items = []
    for d in docs:
        if d["w"] == "PROF":
            if d["l"] != "Évaluation":
                continue
            lab = "Correction"
        elif d["l"] != "Évaluation":
            continue
        else:
            lab = "Évaluation"
        cls = [c for c in (show_corr if lab == "Correction" else show_eval) if not d.get("c") or c == d["c"]]
        if not cls:
            continue
        label = LABELS.get(lab, lab) + (" (sujet " + d["s"] + ")" if d.get("s") else "")
        items.append({"type": TYPES[lab], "label": label, "href": d["p"], "cls": cls, "_s": d.get("s") or ""})
        wanted[d["p"]] = d.get("b")
    items.sort(key=lambda i: (list(TYPES.values()).index(i["type"]), i.pop("_s")))
    return items


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
    if sys.argv[1] == "collections":
        levels = js_const(open(sys.argv[2], encoding="utf-8").read(), "LEVELS")
        print(json.dumps([c for lv in level_list(levels) for c in (suivi_of(lv), evals_of(lv))] + ["config", "evaluations"]))
        return
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
        anim_need = [f"https://claude.ai/artifact/{a}" for a in sorted(ANIMS) if not os.path.exists(os.path.join(repo, "anim", a + ".html"))]
        json.dump(anim_need, open(f"{dbdir}/need_anim.json", "w"), ensure_ascii=False)
        print(f"{len(ANIMS)} animation(s) publiée(s), {len(anim_need)} à récupérer (need_anim.json)")
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
    # Animations : copie des pages récupérées (W/pdf/anim/<id>/index.html), retrait de celles qui ne sont plus publiées
    for a in ANIMS:
        src, dst = os.path.join(pdfdir, "anim", a, "index.html"), os.path.join(repo, "anim", a + ".html")
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)
    missing_anim = {a for a in ANIMS if not os.path.exists(os.path.join(repo, "anim", a + ".html"))}
    if missing_anim:
        print("ATTENTION : animation(s) non récupérée(s), lien masqué :", ", ".join(sorted(missing_anim)))
        for s in [s for l in data["niveaux"].values() for s in l]:
            for n in s["notions"]:
                n["items"] = [i for i in n["items"] if not (i["type"] == "anim" and i["href"].split("/")[1].split(".")[0] in missing_anim)]
    for f in glob.glob(os.path.join(repo, "anim", "*.html")):
        if os.path.basename(f)[:-5] not in ANIMS:
            os.remove(f)
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
