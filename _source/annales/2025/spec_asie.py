# DNB Asie, 16 juin 2025
QCM = (1, 210, 290)
PARTS = [
dict(id='2025-asie-1q1', s='asie', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Probabilités',
     regions=[QCM, (1, 288, 419)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{1}{Probabilité d'obtenir une boule violette.}
\begin{reponse}
L'urne contient $4 + 6 + 7 + 3 = 20$ boules, dont 6 violettes : $p = \dfrac{6}{20} = \dfrac{3}{10}$. \textbf{Réponse C.}
\end{reponse}
'''),
dict(id='2025-asie-1q2', s='asie', ex=1, titre='Exercice 1 -- QCM, question 2', theme='Pourcentages',
     regions=[QCM, (1, 417, 505)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{2}{Calculer 70 \% d'une quantité revient à la multiplier par\ldots}
\begin{reponse}
$70\ \% = \dfrac{70}{100} = 0{,}70$. \textbf{Réponse B.}\\
(1,30 et 1,70 correspondent à des hausses de 30 \% et de 70 \%, 0,30 à une baisse de 70 \%.)
\end{reponse}
'''),
dict(id='2025-asie-1q3', s='asie', ex=1, titre='Exercice 1 -- QCM, question 3', theme='Étendue, médiane, moyenne',
     regions=[QCM, (1, 503, 600)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{3}{Série 7 ; 18 ; 12 ; 13 ; 15 : quelle affirmation est vraie ?}
\begin{reponse}
Rangée dans l'ordre : 7 ; 12 ; 13 ; 15 ; 18.\\
Étendue : $18 - 7 = 11$ (pas 8).\quad Médiane : 13 (pas 12).\quad Moyenne : $\dfrac{7 + 18 + 12 + 13 + 15}{5} = \dfrac{65}{5} = 13$.\\
\textbf{Réponse D} : la moyenne de cette série est 13.
\end{reponse}
'''),
dict(id='2025-asie-1q4', s='asie', ex=1, titre='Exercice 1 -- QCM, question 4', theme='Fonction affine : expression',
     regions=[QCM, (1, 598, 812)], s3=17, n3=[28], s4=None, n4=None,
     corr=r'''
\q{4}{Expression de la fonction affine représentée.}
\begin{reponse}
La droite coupe l'axe des ordonnées en 4 : l'ordonnée à l'origine est $b = 4$.\\
Quand $x$ augmente de 1 (de 0 à 1), $f(x)$ passe de 4 à 2 : il diminue de 2, donc $a = -2$.\\
$f(x) = -2x + 4$. \textbf{Réponse C.}
\end{reponse}
'''),
dict(id='2025-asie-2a', s='asie', ex=2, titre='Exercice 2 -- Géométrie, questions 1 à 3', theme='Pythagore, aire, théorème de Thalès',
     consigne='Traite les questions 1 à 3.', regions=[(2, 134, 364)], s3=9, n3=[], s4=10, n4=[10, 22],
     corr=r'''
\q{1}{Montrer que DE = 19,5 cm.}
\begin{reponse}
Le triangle $CDE$ est rectangle en $D$, d'hypoténuse $[CE]$. D'après le théorème de Pythagore :
\[ DE^2 = CE^2 - CD^2 = 29{,}1^2 - 21{,}6^2 = 846{,}81 - 466{,}56 = 380{,}25 \qquad\text{donc}\qquad DE = \sqrt{380{,}25} = 19{,}5 \text{ cm}. \]
\end{reponse}
\q{2}{Aire du triangle CDE.}
\begin{reponse}
Le triangle est rectangle en $D$ : $\mathcal{A} = \dfrac{CD \times DE}{2} = \dfrac{21{,}6 \times 19{,}5}{2} = 210{,}6 \text{ cm}^2$.
\end{reponse}
\q{3}{Longueur GF, arrondie au millimètre.}
\begin{reponse}
Les points $G$, $C$, $E$ et $F$, $C$, $D$ sont alignés, et $(GF) \parallel (DE)$. D'après le théorème de Thalès :
\[ \frac{CF}{CD} = \frac{CG}{CE} = \frac{GF}{DE} \qquad\text{soit}\qquad \frac{17{,}2}{21{,}6} = \frac{GF}{19{,}5} \qquad\text{donc}\qquad GF = \frac{19{,}5 \times 17{,}2}{21{,}6} \approx 15{,}5 \text{ cm}. \]
\end{reponse}
'''),
dict(id='2025-asie-2b', s='asie', ex=2, titre='Exercice 2 -- Géométrie, question 4', theme='Aires, triangles semblables',
     consigne="Traite la question 4 (l'aire du triangle CDE est 210,6 cm² et DE = 19,5 cm).", regions=[(2, 134, 312), (2, 362, 710)], s3=10, n3=[16], s4=None, n4=None,
     corr=r'''
\q{4.a}{Montrer que l'aire de ABC est $\frac19$ de l'aire de CDE.}
\begin{reponse}
$\dfrac19 \times 210{,}6 = 23{,}4 \text{ cm}^2$ : c'est bien l'aire affichée pour le triangle $ABC$.
\end{reponse}
\q{4.b}{Les triangles ABC et EDC sont semblables : déterminer AB.}
\begin{reponse}
Le triangle $ABC$ est une réduction du triangle $EDC$. Les aires sont multipliées par $\frac19 = \left(\frac13\right)^2$, donc les longueurs sont multipliées par $\frac13$.\\
Les angles droits se correspondent ($\widehat{B}$ et $\widehat{D}$), ainsi que l'angle $\widehat{C}$ commun : $[AB]$ correspond à $[ED]$.
\[ AB = \frac13 \times DE = \frac{19{,}5}{3} = 6{,}5 \text{ cm}. \]
\end{reponse}
'''),
dict(id='2025-asie-3a', s='asie', ex=3, titre='Exercice 3 -- Rectangle et carré, partie A', theme='Expressions littérales, périmètres',
     consigne='Traite la partie A.', regions=[(3, 134, 517)], s3=1, n3=[], s4=8, n4=[18],
     corr=r'''
\q{1}{Périmètre du carré EFGH (x = 1,5 cm).}
\begin{reponse}
$EF = 2 \times 1{,}5 = 3$ cm, donc le périmètre est $4 \times 3 = 12$ cm.
\end{reponse}
\q{2}{Calculer AB.}
\begin{reponse}
$AB = 16 - 2 \times 1{,}5 = 16 - 3 = 13$ cm.
\end{reponse}
\q{3}{Construire le rectangle ABCD.}
\begin{reponse}
Rectangle de longueur $AB = 13$ cm et de largeur $AD = 1{,}5$ cm, tracé à la règle et à l'équerre.
\end{reponse}
\q{4}{Les périmètres sont-ils égaux ?}
\begin{reponse}
Périmètre du rectangle : $2 \times (13 + 1{,}5) = 29$ cm. $29 \neq 12$ : les périmètres ne sont pas égaux.
\end{reponse}
'''),
dict(id='2025-asie-3b', s='asie', ex=3, titre='Exercice 3 -- Rectangle et carré, partie B', theme='Tableur, expression littérale, équation',
     consigne='Traite la partie B.', regions=[(3, 134, 408), (3, 517, 735)], s3=7, n3=[], s4=16, n4=[8, 38, 39],
     corr=r'''
\q{1.a}{Formule saisie en B2.}
\begin{reponse}
Le périmètre du carré est $4 \times 2x = 8x$ : \texttt{=8*B1}.
\end{reponse}
\q{1.b}{Le tableau permet-il de trouver une valeur de $x$ qui convient ?}
\begin{reponse}
Non : pour $x = 3$, le carré a le plus petit périmètre (24 contre 26) ; pour $x = 4$, c'est le rectangle (24 contre 32). La valeur cherchée est entre 3 et 4 et n'est pas dans le tableau.
\end{reponse}
\q{2.a}{Montrer que le périmètre du rectangle s'écrit $-2x + 32$.}
\begin{reponse}
$2 \times (AB + AD) = 2 \times (16 - 2x + x) = 2 \times (16 - x) = 32 - 2x = -2x + 32$.
\end{reponse}
\q{2.b}{Résoudre le problème par une équation.}
\begin{reponse}
Je résous $8x = -2x + 32$ : \quad $10x = 32$ \quad donc \quad $x = 3{,}2$.\\
Les périmètres sont égaux pour $x = 3{,}2$ cm (ils valent alors $8 \times 3{,}2 = 25{,}6$ cm).
\end{reponse}
'''),
dict(id='2025-asie-4', s='asie', ex=4, titre="Exercice 4 -- L'hexagone (Scratch)", theme='Algorithmique (Scratch)',
     regions=[(4, 134, 755), (5, 128, 541)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Compléter les lignes 2, 3 et 4 du script « triangle équilatéral ».}
\begin{reponse}
\texttt{2\quad répéter \fbox{3} fois}\\
\texttt{3\quad avancer de \fbox{50} pas}\\
\texttt{4\quad tourner de \fbox{120} degrés}
\end{reponse}
\q{2}{Quel programme trace l'hexagone souhaité ?}
\begin{reponse}
Les 6 triangles doivent se suivre autour du centre : on tourne de $360 \div 6 = 60^\circ$ entre deux triangles. C'est le \textbf{programme A}.
\end{reponse}
\q{B}{Recopier et compléter le bloc « répéter ».}
\begin{reponse}
\texttt{répéter \fbox{6} fois}\\
\texttt{\quad avancer de 50 pas}\\
\texttt{\quad tourner de 60 degrés}\\
Un hexagone régulier a 6 côtés ; à chaque sommet, le lutin tourne de $180 - 120 = 60^\circ$.
\end{reponse}
'''),
dict(id='2025-asie-5a', s='asie', ex=5, titre='Exercice 5 -- Les poissons, partie A', theme='Décomposition, diviseurs, répartition en lots',
     consigne='Traite la partie A.', regions=[(5, 539, 790), (6, 128, 170)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{1}{Décomposition de 300 en produit de facteurs premiers.}
\begin{reponse}
\textbf{Proposition 2} : $2 \times 2 \times 3 \times 5 \times 5 = 300$ et tous les facteurs sont premiers (15 et 22 ne le sont pas).
\end{reponse}
\q{2}{Décomposition de 350.}
\begin{reponse}
$350 = 2 \times 175 = 2 \times 5 \times 35 = 2 \times 5^2 \times 7$.
\end{reponse}
\q{3}{Nombre maximal de lots.}
\begin{reponse}
Le nombre de lots doit diviser 350 et 300. Les facteurs communs aux deux décompositions sont $2 \times 5^2 = 50$ : c'est le plus grand diviseur commun.\\
On peut faire au maximum \textbf{50 lots}.
\end{reponse}
\q{4}{Nombre de poissons de chaque type par lot.}
\begin{reponse}
$350 \div 50 = 7$ poissons de type A et $300 \div 50 = 6$ poissons de type B par lot.
\end{reponse}
'''),
dict(id='2025-asie-5b', s='asie', ex=5, titre="Exercice 5 -- Les poissons combattants, question 1", theme='Volumes (cylindre, pavé), conversions',
     consigne='Traite la question 1 de la partie B.', regions=[(5, 539, 568), (6, 168, 452)], s3=21, n3=[34], s4=None, n4=None,
     corr=r'''
\q{1}{Quel aquarium choisir (au moins 15 L, rempli aux $\frac45$ de sa hauteur) ?}
\begin{reponse}
\textbf{Aquarium 1} (cylindre de rayon 15 cm) : hauteur d'eau $\frac45 \times 25 = 20$ cm.
\[ V_1 = \pi \times 15^2 \times 20 = 4\,500\pi \approx 14\,137 \text{ cm}^3 \approx 14{,}1 \text{ L} < 15 \text{ L}. \]
\textbf{Aquarium 2} (pavé droit) : hauteur d'eau $\frac45 \times 30 = 24$ cm.
\[ V_2 = 28 \times 28 \times 24 = 18\,816 \text{ cm}^3 \approx 18{,}8 \text{ L} > 15 \text{ L}. \]
Il faut choisir l'\textbf{aquarium 2}.
\end{reponse}
'''),
dict(id='2025-asie-5c', s='asie', ex=5, titre="Exercice 5 -- Les poissons combattants, question 2", theme='Pourcentages',
     consigne='Traite la question 2 de la partie B.', regions=[(5, 539, 568), (6, 168, 215), (6, 450, 515)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{2}{Prix payé avec une remise de 15 \% sur le total.}
\begin{reponse}
Prix total : $15 + 40 = 55$ €. Une remise de 15 \%, c'est multiplier par $1 - 0{,}15 = 0{,}85$ :
\[ 55 \times 0{,}85 = 46{,}75 \text{ €}. \]
(Ou : 15 \% de 55 € font $8{,}25$ €, et $55 - 8{,}25 = 46{,}75$ €.)
\end{reponse}
'''),
]
