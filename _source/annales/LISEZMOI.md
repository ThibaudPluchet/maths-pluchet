# Exercices du brevet (onglet « Exercices DNB » du site élèves)

- `2025/spec_<centre>.py` : découpage de chaque sujet en parties (pages et zones recadrées, notions requises,
  séquence de rangement) et corrigé LaTeX de chaque partie.
  - `n3` : notions de 3e nécessaires en plus du programme de 4e ; `n4` : notions de 4e (None = pas proposé en 4e) ;
  - `s3` / `s4` : séquence de rangement (0 = Algorithmique / Scratch).
- `build.py` : produit l'énoncé recadré (depuis le sujet APMEP, site2wouf.fr/coll/fiches/dnb_<centre>_<mois>_<année>.pdf,
  à placer dans `src/`) et le corrigé compilé (préambule `preamble.tex`, style des documents du cours).
- `check.py` : signale les lignes coupées en bord de zone ; `dump.py` : positions des questions dans un sujet.
- Les PDF publiés sont dans `annales/<année>/`, le catalogue dans `_source/annales.json` ;
  `sync.py` publie pour chaque classe les parties dont toutes les notions sont cochées « Fait en classe ».
- `full.py` : sujets complets (PDF officiel, copie dans `annales/<année>/<id>-sujet-complet.pdf`) et corrigés complets
  (toutes les parties d'un centre réunies, `<id>-corrige-complet.pdf`) ; catalogue `_source/annales-sujets.json`
  (ordre chronologique), affiché en 3e dans le bloc « Sujets complets ».
