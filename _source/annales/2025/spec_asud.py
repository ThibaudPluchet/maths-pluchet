# DNB Amérique du Sud, novembre 2025
H1 = (1, 182, 238)   # en-tête de l'exercice 1
PARTS = [
dict(id='2025-asud-1s1', s='asud', ex=1, titre='Exercice 1 -- Situation 1', theme='Décomposition en facteurs premiers',
     regions=[H1, (1, 236, 274)], s3=24, n3=[], s4=6, n4=[14],
     corr=r'''
\q{1}{Décomposer 390 en produit de facteurs premiers.}
\begin{reponse}
$390 = 2 \times 195 = 2 \times 3 \times 65 = 2 \times 3 \times 5 \times 13$ (2, 3, 5 et 13 sont premiers).
\end{reponse}
'''),
dict(id='2025-asud-1s2', s='asud', ex=1, titre='Exercice 1 -- Situation 2', theme='Trigonométrie (calcul d’angle)',
     regions=[H1, (1, 272, 324)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{2}{Mesure de l'angle $\widehat{ABC}$ (ABC rectangle en A, AB = 10 cm, BC = 20 cm).}
\begin{reponse}
Dans le triangle $ABC$ rectangle en $A$, l'hypoténuse est $[BC]$ et $[AB]$ est le côté adjacent à l'angle $\widehat{ABC}$ :
\[ \cos\widehat{ABC} = \frac{AB}{BC} = \frac{10}{20} = 0{,}5 \qquad\text{donc}\qquad \widehat{ABC} = \arccos(0{,}5) = 60^\circ. \]
\end{reponse}
'''),
dict(id='2025-asud-1s3', s='asud', ex=1, titre='Exercice 1 -- Situation 3', theme='Probabilités',
     regions=[H1, (1, 322, 388)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{3}{Probabilité d'obtenir un nombre inférieur ou égal à 5.}
\begin{reponse}
Les jetons 1, 2, 3, 4 et 5 conviennent : 5 jetons sur 12, tirés au hasard. $p = \dfrac{5}{12}$.
\end{reponse}
'''),
dict(id='2025-asud-1s4', s='asud', ex=1, titre='Exercice 1 -- Situation 4', theme='Fonctions : image, fonction linéaire',
     regions=[H1, (1, 386, 687)], s3=8, n3=[12, 13, 26], s4=None, n4=None,
     corr=r'''
\q{1}{Image de 2 par la fonction $f$.}
\begin{reponse}
Dans le tableau de valeurs, sous $x = 2$ on lit $f(2) = -3$.
\end{reponse}
\q{2}{Image de $-1$ par la fonction $f$.}
\begin{reponse}
Sur la représentation graphique, le point d'abscisse $-1$ a pour ordonnée 3 : $f(-1) = 3$.
\end{reponse}
\q{3}{La fonction $f$ est-elle linéaire ?}
\begin{reponse}
Non : sa représentation graphique est une droite qui ne passe pas par l'origine ($f(0) = 1 \neq 0$). $f$ est une fonction affine non linéaire.
\end{reponse}
'''),
dict(id='2025-asud-1s5', s='asud', ex=1, titre='Exercice 1 -- Situation 5', theme='Double distributivité, identité',
     regions=[H1, (1, 685, 760)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{1}{Montrer que l'égalité est vraie pour $x = 2$.}
\begin{reponse}
Membre de gauche : $(2 \times 2 - 3)(4 \times 2 + 5) = 1 \times 13 = 13$.\\
Membre de droite : $8 \times 2^2 - 2 \times 2 - 15 = 32 - 4 - 15 = 13$. Les deux membres sont égaux : l'égalité est vraie pour $x = 2$.
\end{reponse}
\q{2}{L'égalité est-elle vraie quelle que soit la valeur de $x$ ?}
\begin{reponse}
Je développe le membre de gauche :
\[ (2x - 3)(4x + 5) = 8x^2 + 10x - 12x - 15 = 8x^2 - 2x - 15. \]
On retrouve le membre de droite : l'égalité est vraie pour toutes les valeurs de $x$.
\end{reponse}
'''),
dict(id='2025-asud-2a', s='asud', ex=2, titre='Exercice 2 -- Les réseaux sociaux, partie 1', theme='Moyenne, étendue, proportion',
     consigne='Traite la partie 1.', regions=[(2, 145, 366)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{1}{Nombre d'élèves dans ce groupe.}
\begin{reponse}
Il y a 9 durées : \textbf{9 élèves}.
\end{reponse}
\q{2}{Temps moyen passé sur les réseaux sociaux.}
\begin{reponse}
\[ \frac{135 + 82 + 104 + 200 + 102 + 17 + 143 + 118 + 62}{9} = \frac{963}{9} = 107 \text{ min}. \]
\end{reponse}
\q{3}{Étendue de la série.}
\begin{reponse}
$200 - 17 = 183$ min.
\end{reponse}
\q{4}{« Plus de 50 \% des élèves passent au moins 1 h 30 min par jour sur les réseaux sociaux. »}
\begin{reponse}
1 h 30 min $= 90$ min. Les durées d'au moins 90 min sont 135, 104, 200, 102, 143 et 118 : 6 élèves sur 9.
\[ \frac{6}{9} = \frac23 \approx 67\ \% > 50\ \%. \]
L'affirmation est \textbf{vraie}.
\end{reponse}
'''),
dict(id='2025-asud-2b', s='asud', ex=2, titre='Exercice 2 -- Les réseaux sociaux, partie 2', theme='Pourcentages, tableur',
     consigne='Traite la partie 2.', regions=[(2, 145, 214), (2, 364, 660)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{1}{Les répondants représentent-ils plus de 60 \% des élèves du collège ?}
\begin{reponse}
$\dfrac{400}{640} = 0{,}625 = 62{,}5\ \%$ : c'est bien plus de 60 \%.
\end{reponse}
\q{2}{Formule à entrer dans la cellule F2.}
\begin{reponse}
\texttt{=SOMME(B2:E2)}
\end{reponse}
\q{3}{Nombre d'élèves qui passent moins de 1 h par jour sur les réseaux sociaux.}
\begin{reponse}
$30 + 12 + 1 + 7 = 50$ élèves.
\end{reponse}
\q{4}{Pourcentage d'élèves qui passent moins de 1 h 30 min par jour.}
\begin{reponse}
Moins de 1 h : 50 élèves ; entre 1 h et 1 h 29 : 101 élèves. Total : $50 + 101 = 151$ élèves.
\[ \frac{151}{400} = 0{,}3775 = 37{,}75\ \%, \text{ soit environ } 38\ \%. \]
\end{reponse}
'''),
dict(id='2025-asud-3', s='asud', ex=3, titre='Exercice 3 -- Les triangles (Scratch)', theme='Algorithmique (Scratch)',
     regions=[(3, 145, 790)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Compléter les lignes 3 et 5 du bloc « triangle ».}
\begin{reponse}
\texttt{3\quad répéter \fbox{3} fois}\qquad\texttt{5\quad tourner de \fbox{120} degrés}\\
Pour un triangle équilatéral, le lutin tourne de $180 - 60 = 120^\circ$ à chaque sommet ($3 \times 120 = 360$).
\end{reponse}
\q{2}{Associer chaque programme à son dessin.}
\begin{reponse}
Après le bloc « triangle », le lutin est revenu à son point de départ, dans la même direction.\\
\textbf{Programme A $\to$ dessin 2} : il tourne de $90^\circ$ entre deux triangles, les 4 triangles tournent autour du point de départ.\\
\textbf{Programme B $\to$ dessin 3} : il avance d'un côté entre deux triangles, les 4 triangles sont alignés côte à côte.
\end{reponse}
\q{3}{Construire le dessin obtenu (1 cm pour 10 pas).}
\begin{reponse}
Le côté vaut successivement 20, 40, 80 puis 160 pas, soit 2 cm, 4 cm, 8 cm et 16 cm, et le lutin repart chaque fois du même point dans la même direction.\\
On obtient \textbf{quatre triangles équilatéraux emboîtés}, de côtés 2 cm, 4 cm, 8 cm et 16 cm, qui ont un sommet commun (le point de départ) et un côté sur la même demi-droite horizontale.
\end{reponse}
'''),
dict(id='2025-asud-4', s='asud', ex=4, titre='Exercice 4 -- Géométrie', theme='Parallélisme, Thalès, Pythagore, aires',
     regions=[(4, 145, 398)], s3=9, n3=[], s4=19, n4=[10, 22],
     corr=r'''
\q{1}{Montrer que les droites (AD) et (BC) sont parallèles.}
\begin{reponse}
Les droites $(AD)$ et $(BC)$ sont toutes les deux perpendiculaires à la droite $(AB)$. Or deux droites perpendiculaires à une même droite sont parallèles : $(AD) \parallel (BC)$.
\end{reponse}
\q{2}{Calculer la longueur AD.}
\begin{reponse}
Les points $A$, $E$, $C$ et $D$, $E$, $B$ sont alignés, et $(AD) \parallel (BC)$. D'après le théorème de Thalès :
\[ \frac{EA}{EC} = \frac{ED}{EB} = \frac{AD}{CB} \qquad\text{soit}\qquad \frac{9{,}6}{5{,}4} = \frac{AD}{9} \qquad\text{donc}\qquad AD = \frac{9 \times 9{,}6}{5{,}4} = 16 \text{ cm}. \]
\end{reponse}
\q{3}{Montrer que BE = 7,2 cm.}
\begin{reponse}
$(BD) \perp (AC)$, donc le triangle $BEC$ est rectangle en $E$, d'hypoténuse $[BC]$. D'après le théorème de Pythagore :
\[ BE^2 = BC^2 - CE^2 = 9^2 - 5{,}4^2 = 81 - 29{,}16 = 51{,}84 \qquad\text{donc}\qquad BE = \sqrt{51{,}84} = 7{,}2 \text{ cm}. \]
\end{reponse}
\q{4}{L'aire du triangle ABE est-elle le tiers de l'aire du triangle ABD ?}
\begin{reponse}
Triangle $ABE$, rectangle en $E$ : $\mathcal{A}_{ABE} = \dfrac{BE \times AE}{2} = \dfrac{7{,}2 \times 9{,}6}{2} = 34{,}56 \text{ cm}^2$.\\
Calcul de $AB$ : dans le triangle $ABE$ rectangle en $E$, $AB^2 = 7{,}2^2 + 9{,}6^2 = 51{,}84 + 92{,}16 = 144$, donc $AB = 12$ cm.\\
Triangle $ABD$, rectangle en $A$ : $\mathcal{A}_{ABD} = \dfrac{AB \times AD}{2} = \dfrac{12 \times 16}{2} = 96 \text{ cm}^2$.\\
$\dfrac{96}{3} = 32 \neq 34{,}56$ : c'est \textbf{faux} (l'aire de $ABE$ représente $\dfrac{34{,}56}{96} = 36\ \%$ de celle de $ABD$).
\end{reponse}
'''),
dict(id='2025-asud-5a', s='asud', ex=5, titre='Exercice 5 -- Les glaçons, partie 1', theme='Volume du pavé, conversions',
     consigne='Traite la partie 1.', regions=[(4, 396, 790)], s3=21, n3=[], s4=17, n4=[],
     corr=r'''
\q{1}{Nombre de glaçons avec 12 moules.}
\begin{reponse}
Un moule donne $4 \times 5 = 20$ glaçons, donc 12 moules donnent $12 \times 20 = 240$ glaçons.
\end{reponse}
\q{2}{Montrer qu'un glaçon a un volume d'environ 19 mL.}
\begin{reponse}
$V = 5 \times 2{,}5 \times 1{,}5 = 18{,}75 \text{ cm}^3 = 18{,}75$ mL, soit environ 19 mL.
\end{reponse}
\q{3}{5 litres d'eau suffisent-ils pour remplir les 12 moules ?}
\begin{reponse}
$240 \times 18{,}75 = 4\,500$ mL $= 4{,}5$ L. Comme $4{,}5 < 5$, \textbf{oui}, 5 litres suffisent.
\end{reponse}
'''),
dict(id='2025-asud-5b', s='asud', ex=5, titre='Exercice 5 -- Les verres, partie 2', theme='Volume du cylindre, conversions',
     consigne='Traite la partie 2.', regions=[(4, 396, 527), (5, 128, 330)], s3=21, n3=[34], s4=None, n4=None,
     corr=r'''
\q{4}{Montrer que le verre a un volume d'environ 295 mL.}
\begin{reponse}
Le verre est un cylindre de diamètre 5 cm (rayon 2,5 cm) et de hauteur 15 cm :
\[ V = \pi \times 2{,}5^2 \times 15 = 93{,}75\pi \approx 294{,}5 \text{ cm}^3, \text{ soit environ } 295 \text{ mL}. \]
\end{reponse}
\q{5.a}{Nombre de verres de 25 cL avec 30 litres de cocktail.}
\begin{reponse}
30 L $= 3\,000$ cL et $3\,000 \div 25 = 120$ : on peut remplir \textbf{120 verres}.
\end{reponse}
\q{5.b}{Hauteur $h$ du liquide pour 25 cL, au dixième.}
\begin{reponse}
25 cL $= 250$ mL $= 250 \text{ cm}^3$. Je cherche $h$ tel que $\pi \times 2{,}5^2 \times h = 250$ :
\[ h = \frac{250}{6{,}25\pi} \approx 12{,}7 \text{ cm}. \]
\end{reponse}
'''),
]
