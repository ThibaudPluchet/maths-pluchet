# DNB Métropole – Antilles-Guyane, 19 septembre 2024
SOURCE = ('dnb_metropole_sept_2024.pdf', 'Métropole – Antilles-Guyane, 19 septembre 2024')
E1 = (1, 278, 338)
E4 = (3, 721, 792)
PARTS = [
dict(id='2024-mets-1a', s='mets', ex=1, titre='Exercice 1 -- Vrai ou faux, affirmation 1', theme='Décomposition en facteurs premiers',
     regions=[E1, (1, 338, 371)], s3=24, n3=[], s4=6, n4=[14],
     corr=r'''
\q{1}{260 = 4 × 5 × 13 est-elle sa décomposition en facteurs premiers ?}
\begin{reponse}
Le produit vaut bien 260, mais 4 n'est pas un nombre premier ($4 = 2 \times 2$). La décomposition est $260 = 2^2 \times 5 \times 13$.\\
L'affirmation 1 est \textbf{fausse}.
\end{reponse}
'''),
dict(id='2024-mets-1b', s='mets', ex=1, titre='Exercice 1 -- Vrai ou faux, affirmation 2', theme='Probabilités',
     regions=[E1, (1, 371, 489)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{2}{Rouge plus probable que la lettre C ?}
\begin{reponse}
Première urne : $3 + 4 + 8 = 15$ boules dont 8 rouges, $p = \dfrac{8}{15}$. \quad Seconde urne : $1 + 1 + 3 = 5$ boules dont 3 marquées C, $p = \dfrac35 = \dfrac{9}{15}$.\\
$\dfrac{8}{15} < \dfrac{9}{15}$ : la probabilité d'obtenir une boule rouge est plus petite. L'affirmation 2 est \textbf{fausse}.
\end{reponse}
'''),
dict(id='2024-mets-1c', s='mets', ex=1, titre='Exercice 1 -- Vrai ou faux, affirmation 3', theme='Équation du premier degré',
     regions=[E1, (1, 489, 522)], s3=7, n3=[], s4=16, n4=[38],
     corr=r'''
\q{3}{La solution de $7x + 5 = 2x - 2$ est $-1{,}4$.}
\begin{reponse}
\[ 7x + 5 = 2x - 2 \iff 7x - 2x = -2 - 5 \iff 5x = -7 \iff x = \frac{-7}{5} = -1{,}4. \]
L'affirmation 3 est \textbf{vraie}.
\end{reponse}
'''),
dict(id='2024-mets-1d', s='mets', ex=1, titre='Exercice 1 -- Vrai ou faux, affirmation 4', theme='Volume du cylindre',
     regions=[E1, (1, 522, 583)], s3=21, n3=[34], s4=None, n4=None,
     corr=r'''
\q{4}{Le volume des 10 pièces empilées est d'environ 6 cm³.}
\begin{reponse}
Les 10 pièces forment un cylindre de rayon $1{,}9 \div 2 = 0{,}95$ cm et de hauteur $10 \times 0{,}2 = 2$ cm :
\[ V = \pi \times 0{,}95^2 \times 2 \approx 5{,}67 \approx 6 \text{ cm}^3. \]
L'affirmation 4 est \textbf{vraie}.
\end{reponse}
'''),
dict(id='2024-mets-1e', s='mets', ex=1, titre='Exercice 1 -- Vrai ou faux, affirmation 5', theme='Vitesses, conversion',
     regions=[E1, (1, 583, 628)], s3=14, n3=[], s4=15, n4=[35, 36],
     corr=r'''
\q{5}{Un éléphant à 5 m/s est-il plus rapide qu'un cochon à 17 km/h ?}
\begin{reponse}
5 m en 1 s, c'est $5 \times 3\,600 = 18\,000$ m en 1 h, soit 18 km/h. $18 > 17$ : l'affirmation 5 est \textbf{vraie}.
\end{reponse}
'''),
dict(id='2024-mets-2a', s='mets', ex=2, titre='Exercice 2 -- Le champ de blé, questions 1 et 2', theme='Théorème de Thalès',
     consigne='Traite les questions 1 et 2.', regions=[(2, 146, 699)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{1.a}{Montrer que BG = 60 m.}
\begin{reponse}
5 passages de 12 m de large : $BG = 5 \times 12 = 60$ m.
\end{reponse}
\q{1.b}{En déduire CG.}
\begin{reponse}
$G$ est sur le segment $[BC]$ : $CG = BC - BG = 150 - 60 = 90$ m.
\end{reponse}
\q{2}{Démontrer que GF = 120 m.}
\begin{reponse}
Les points $C$, $G$, $B$ et $C$, $F$, $A$ sont alignés, et $(GF) \parallel (AB)$ (les bandes sont parallèles à $(AB)$). D'après le théorème de Thalès :
\[ \frac{CG}{CB} = \frac{GF}{BA} \qquad\text{soit}\qquad \frac{90}{150} = \frac{GF}{200} \qquad\text{donc}\qquad GF = \frac{90 \times 200}{150} = 120 \text{ m}. \]
\end{reponse}
'''),
dict(id='2024-mets-2b', s='mets', ex=2, titre='Exercice 2 -- Le champ de blé, questions 3 et 4', theme='Aire, proportionnalité, théorème de Pythagore',
     consigne='Traite les questions 3 et 4 (GF = 120 m et CG = 90 m).', regions=[(2, 146, 650), (2, 698, 775), (3, 128, 190)], s3=2, n3=[], s4=4, n4=[10, 11],
     corr=r'''
\q{3.a}{Aire du triangle CGF.}
\begin{reponse}
Le triangle $CGF$ est rectangle en $G$ : $\mathcal{A} = \dfrac{CG \times GF}{2} = \dfrac{90 \times 120}{2} = 5\,400$ m².
\end{reponse}
\q{3.b}{Temps pour moissonner CGF.}
\begin{reponse}
Le temps est proportionnel à la surface : 9\,600 m² en 80 min, donc 5\,400 m² en $\dfrac{5\,400 \times 80}{9\,600} = \mathbf{45}$ min.
\end{reponse}
\q{4}{Longueur de clôture.}
\begin{reponse}
Le triangle $ABC$ est rectangle en $B$, d'hypoténuse $[AC]$. D'après le théorème de Pythagore :
\[ AC^2 = AB^2 + BC^2 = 200^2 + 150^2 = 40\,000 + 22\,500 = 62\,500 \qquad\text{donc}\qquad AC = \sqrt{62\,500} = 250 \text{ m}. \]
Périmètre : $200 + 150 + 250 = \mathbf{600}$ m de clôture.
\end{reponse}
'''),
dict(id='2024-mets-3a', s='mets', ex=3, titre='Exercice 3 -- Les panneaux solaires, questions 1 et 2', theme='Étendue, moyenne, pourcentage',
     consigne='Traite les questions 1 et 2.', regions=[(3, 190, 434)], s3=23, n3=[], s4=15, n4=[24, 34],
     corr=r'''
\q{1.a}{Jour de plus grande production.}
\begin{reponse}
Le \textbf{samedi} (405 kWh).
\end{reponse}
\q{1.b}{Étendue des productions.}
\begin{reponse}
$405 - 322 = \mathbf{83}$ kWh.
\end{reponse}
\q{1.c}{Production moyenne par jour.}
\begin{reponse}
\[ \frac{381 + 363 + 322 + 329 + 393 + 405 + 376}{7} = \frac{2\,569}{7} = \mathbf{367} \text{ kWh}. \]
\end{reponse}
\q{2}{Gain de la revente de 15 \% à 8 centimes le kWh.}
\begin{reponse}
15 \% de 2\,569 kWh : $2\,569 \times 0{,}15 = 385{,}35$ kWh. \quad Gain : $385{,}35 \times 0{,}08 \approx \mathbf{30{,}83}$ €.
\end{reponse}
'''),
dict(id='2024-mets-3b', s='mets', ex=3, titre='Exercice 3 -- Les panneaux solaires, question 3', theme='Trigonométrie (sinus)',
     consigne='Traite la question 3.', regions=[(3, 190, 226), (3, 433, 722)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{3}{La pente du toit est-elle comprise entre 30° et 35° ?}
\begin{reponse}
Dans le triangle $OLV$ rectangle en $V$, $[OV]$ est le côté opposé à l'angle $\widehat{OLV}$ et $[OL]$ l'hypoténuse :
\[ \sin\widehat{OLV} = \frac{OV}{OL} = \frac{7}{13{,}5} \qquad\text{donc}\qquad \widehat{OLV} \approx 31{,}2^\circ. \]
$31{,}2^\circ$ est compris entre $30^\circ$ et $35^\circ$ : \textbf{oui}, la production est maximale.
\end{reponse}
'''),
dict(id='2024-mets-4a', s='mets', ex=4, titre='Exercice 4 -- La fonction f, questions 1 et 2', theme='Image, tableur, antécédent',
     consigne='Traite les questions 1 et 2.', regions=[E4, (4, 128, 320)], s3=8, n3=[5, 12], s4=None, n4=None,
     corr=r'''
\q{1}{Image de 6 par $f$.}
\begin{reponse}
$f(6) = 6^2 + 10 \times 6 + 16 = 36 + 60 + 16 = 112$.
\end{reponse}
\q{2.a}{Formule saisie en B2.}
\begin{reponse}
\texttt{=B1*B1+10*B1+16} : elle utilise le nombre de la cellule juste au-dessus (B1) et, étirée vers la droite, devient C1, D1, \ldots
\end{reponse}
\q{2.b}{Un antécédent de 0.}
\begin{reponse}
Dans la colonne D, $f(-2) = 0$ : \textbf{$-2$} est un antécédent de 0.
\end{reponse}
'''),
dict(id='2024-mets-4b', s='mets', ex=4, titre='Exercice 4 -- La fonction f, question 3', theme='Double distributivité, équation produit',
     consigne='Traite la question 3 (−2 est un antécédent de 0 par f).', regions=[E4, (4, 320, 354)], s3=19, n3=[14, 18, 32], s4=None, n4=None,
     corr=r'''
\q{3.a}{Démontrer que $f(x) = (x + 2)(x + 8)$.}
\begin{reponse}
$(x + 2)(x + 8) = x^2 + 8x + 2x + 16 = x^2 + 10x + 16 = f(x)$.
\end{reponse}
\q{3.b}{Un autre antécédent de 0.}
\begin{reponse}
$(x + 2)(x + 8) = 0 \iff x + 2 = 0$ ou $x + 8 = 0 \iff x = -2$ ou $x = -8$. L'autre antécédent de 0 est \textbf{$-8$}.
\end{reponse}
'''),
dict(id='2024-mets-5', s='mets', ex=5, titre='Exercice 5 -- Le losange, questions 1 et 2 (Scratch)', theme='Losange, angles, Scratch',
     consigne='Traite les questions 1 et 2.', regions=[(5, 146, 656)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1.a}{Reproduire ABCD en vraie grandeur.}
\begin{reponse}
On trace le triangle équilatéral $ABC$ de côté 5 cm, puis le triangle équilatéral $ACD$ de côté 5 cm de l'autre côté de $[AC]$.
\end{reponse}
\q{1.b}{Nature de ABCD.}
\begin{reponse}
Ses quatre côtés mesurent 5 cm : $ABCD$ est un \textbf{losange}.
\end{reponse}
\q{1.c}{Démontrer que $\widehat{BCD}$ mesure 120°.}
\begin{reponse}
Les angles d'un triangle équilatéral mesurent $60^\circ$ : $\widehat{BCA} = 60^\circ$ et $\widehat{ACD} = 60^\circ$. Donc $\widehat{BCD} = 60^\circ + 60^\circ = 120^\circ$.
\end{reponse}
\q{2}{Compléter les lignes 5 et 6.}
\begin{reponse}
Ligne 5 : \texttt{avancer de 50 pas} (le côté de 5 cm) ; ligne 6 : \texttt{tourner de 120 degrés}.\\
\small (Le lutin tourne de $180^\circ - 120^\circ = 60^\circ$ au sommet d'angle $120^\circ$, puis de $180^\circ - 60^\circ = 120^\circ$ au sommet d'angle $60^\circ$.)
\end{reponse}
'''),
]
