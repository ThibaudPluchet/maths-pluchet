# DNB Polynésie, juin 2024
SOURCE = ('dnb_polynesie_juin_2024.pdf', 'Polynésie, juin 2024')
QCM = (1, 272, 347)
E3 = (3, 722, 790)
PARTS = [
dict(id='2024-polj-1q1', s='polj', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Réciproque du théorème de Pythagore',
     regions=[QCM, (1, 347, 402)], s3=13, n3=[], s4=14, n4=[32],
     corr=r'''
\q{1}{AB = 20 cm, BC = 21 cm, AC = 29 cm : que peut-on affirmer ?}
\begin{reponse}
Le plus grand côté est $[AC]$. \quad $AC^2 = 29^2 = 841$ \quad et \quad $AB^2 + BC^2 = 400 + 441 = 841$.\\
$AC^2 = AB^2 + BC^2$ : d'après la réciproque du théorème de Pythagore, $ABC$ est \textbf{rectangle en B}.
\end{reponse}
'''),
dict(id='2024-polj-1q2', s='polj', ex=1, titre='Exercice 1 -- QCM, question 2', theme='Fonction affine : expression',
     regions=[QCM, (1, 402, 598)], s3=17, n3=[28], s4=None, n4=None,
     corr=r'''
\q{2}{Expression de la fonction $f$.}
\begin{reponse}
La droite coupe l'axe des ordonnées en 1 : l'ordonnée à l'origine est 1. Quand $x$ augmente de 2, $y$ augmente de 1 : le coefficient directeur est $\dfrac12$.\\
$f(x) = \dfrac{x}{2} + 1$ : \textbf{quatrième réponse}.
\end{reponse}
'''),
dict(id='2024-polj-1q3', s='polj', ex=1, titre='Exercice 1 -- QCM, question 3', theme='Homothétie',
     regions=[QCM, (1, 598, 758)], s3=18, n3=[30], s4=None, n4=None,
     corr=r'''
\q{3}{Transformation qui envoie le carré 1 sur le carré 2.}
\begin{reponse}
Le carré 2 est deux fois plus grand et de l'autre côté du point $O$ : $E$ est l'image de $C$, avec $OE = 2 \times OC$ et $O$ entre $C$ et $E$.\\
C'est l'\textbf{homothétie de centre O et de rapport $-2$}.
\end{reponse}
'''),
dict(id='2024-polj-1q4', s='polj', ex=1, titre='Exercice 1 -- QCM, question 4', theme='Ratio',
     regions=[QCM, (1, 758, 792), (2, 128, 186)], s3=14, n3=[22], s4=None, n4=None,
     corr=r'''
\q{4}{Jus de fruit de la passion pour 90 cL (ratio 10 : 6 : 2).}
\begin{reponse}
$10 + 6 + 2 = 18$ parts pour 90 cL : une part fait $90 \div 18 = 5$ cL. Jus de fruit de la passion : $6 \times 5 = \mathbf{30}$ cL, \textbf{deuxième réponse}.
\end{reponse}
'''),
dict(id='2024-polj-1q5', s='polj', ex=1, titre='Exercice 1 -- QCM, question 5', theme='Diviseurs communs, répartition',
     regions=[QCM, (2, 186, 270)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{5}{Plus grand nombre de sacs avec 408 pommes et 168 poires.}
\begin{reponse}
$408 = 2^3 \times 3 \times 17$ et $168 = 2^3 \times 3 \times 7$. Le plus grand diviseur commun est $2^3 \times 3 = 24$.\\
\textbf{24 sacs}, avec 17 pommes et 7 poires chacun.
\end{reponse}
'''),
dict(id='2024-polj-2', s='polj', ex=2, titre='Exercice 2 -- Le coût des jeux Olympiques', theme='Lecture de graphique, pourcentage, moyenne',
     regions=[(3, 146, 725)], s3=23, n3=[], s4=15, n4=[24, 34],
     corr=r'''
\q{1}{Éditions avec un coût réel d'au moins 10 milliards d'euros.}
\begin{reponse}
Athènes (10), Pékin (31), Londres (11), Rio (16,5) et Tokyo (12,1) : \textbf{5 éditions}.
\end{reponse}
\q{2}{Pourcentage d'augmentation pour Rio 2016.}
\begin{reponse}
Coût prévisionnel 9 milliards, coût réel 16,5 milliards : $\dfrac{16{,}5 - 9}{9} \times 100 \approx 83$ \%. Le coût a augmenté d'environ \textbf{83 \%}.
\end{reponse}
\q{3}{Coût réel moyen entre 1992 et 2021.}
\begin{reponse}
\[ \frac{9{,}3 + 2{,}3 + 5{,}5 + 10 + 31 + 11 + 16{,}5 + 12{,}1}{8} = \frac{97{,}7}{8} \approx 12{,}2 \text{ milliards d'euros}. \]
\end{reponse}
\q{4.a}{« La moitié des éditions ont coûté plus de 12,2 milliards. »}
\begin{reponse}
C'est faux : seules Pékin (31) et Rio (16,5) dépassent 12,2 milliards, soit 2 éditions sur 8. Le journaliste confond la moyenne et la médiane ; la moyenne est tirée vers le haut par Pékin.
\end{reponse}
\q{4.b}{Coût prévisionnel des JO de Paris 2024.}
\begin{reponse}
Il y a 9 éditions de 1992 à 2024. Somme des 8 coûts prévisionnels connus : $3{,}5 + 1{,}8 + 3 + 5{,}3 + 2{,}6 + 4{,}8 + 9 + 13 = 43$.\\
La moyenne est 5,5 : la somme des 9 coûts vaut $9 \times 5{,}5 = 49{,}5$. Coût prévisionnel de Paris : $49{,}5 - 43 = \mathbf{6{,}5}$ milliards d'euros.
\end{reponse}
'''),
dict(id='2024-polj-3a', s='polj', ex=3, titre='Exercice 3 -- Le centre aquatique, question 1', theme='Théorème de Pythagore, théorème de Thalès',
     consigne='Traite la question 1.', regions=[E3, (4, 128, 467)], s3=9, n3=[], s4=19, n4=[10, 22],
     corr=r'''
\q{1.a}{Calculer AB.}
\begin{reponse}
Le triangle $ABC$ est rectangle en $C$, d'hypoténuse $[AB]$. D'après le théorème de Pythagore :
\[ AB^2 = AC^2 + CB^2 = 15^2 + 27^2 = 225 + 729 = 954 \qquad\text{donc}\qquad AB = \sqrt{954} \approx \mathbf{31} \text{ m}. \]
\end{reponse}
\q{1.b}{Vérifier que JD $\approx$ 24 m.}
\begin{reponse}
$(JH) \perp (FE)$ et $(DE) \perp (FE)$ : les droites $(JH)$ et $(DE)$ sont parallèles. Les points $F$, $J$, $D$ et $F$, $H$, $E$ sont alignés. D'après le théorème de Thalès :
\[ \frac{FJ}{FD} = \frac{FH}{FE} \qquad\text{soit}\qquad \frac{15}{FD} = \frac{7}{18} \qquad\text{donc}\qquad FD = \frac{15 \times 18}{7} \approx 38{,}6 \text{ m}. \]
$JD = FD - FJ \approx 38{,}6 - 15 \approx 23{,}6$, soit environ 24 m.
\end{reponse}
\q{1.c}{Qui est le plus proche d'un bord de la piscine ?}
\begin{reponse}
$24 < 31$ : c'est \textbf{Jules}.
\end{reponse}
'''),
dict(id='2024-polj-3b', s='polj', ex=3, titre='Exercice 3 -- Le centre aquatique, question 2', theme='Trigonométrie (tangente)',
     consigne='Traite la question 2.', regions=[E3, (4, 128, 382), (4, 466, 501)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{2}{L'angle $\widehat{ABC}$ dépasse-t-il 35° ?}
\begin{reponse}
Dans le triangle $ABC$ rectangle en $C$, $[AC]$ est le côté opposé à l'angle $\widehat{ABC}$ et $[BC]$ le côté adjacent :
\[ \tan\widehat{ABC} = \frac{AC}{BC} = \frac{15}{27} \qquad\text{donc}\qquad \widehat{ABC} \approx 29{,}1^\circ. \]
$29{,}1^\circ < 35^\circ$ : les gradins Nord \textbf{respectent} la norme.
\end{reponse}
'''),
dict(id='2024-polj-3c', s='polj', ex=3, titre='Exercice 3 -- Le centre aquatique, questions 3 et 4', theme='Aire, volume, proportionnalité',
     consigne='Traite les questions 3 et 4.', regions=[E3, (4, 500, 790)], s3=14, n3=[], s4=5, n4=[11],
     corr=r'''
\q{3}{Énergie produite par les panneaux du toit.}
\begin{reponse}
Un panneau a une aire de $1 \times 1{,}7 = 1{,}7$ m². Nombre de panneaux : $4\,678{,}4 \div 1{,}7 = 2\,752$.\\
Énergie : $2\,752 \times 350 = 963\,200$ kWh par an.
\end{reponse}
\q{4}{Énergie pour chauffer l'eau de la piscine.}
\begin{reponse}
Volume d'eau : $50 \times 25 \times 3 = 3\,750$ m³. \quad Énergie : $3\,750 \times 9{,}3 = \mathbf{34\,875}$ kWh.
\end{reponse}
'''),
dict(id='2024-polj-4', s='polj', ex=4, titre='Exercice 4 -- Les boules numérotées', theme='Probabilités, tableau à double entrée, décomposition',
     consigne='Le tableau à compléter est en annexe.', regions=[(5, 146, 515), (7, 205, 305)], s3=22, n3=[], s4=20, n4=[14, 47],
     corr=r'''
\q{1}{Tableau des résultats.}
\begin{reponse}
\begin{tabular}{|c|c|c|}\hline
\entete $\times$ & 3 & 5 \\\hline
5 & 15 & 25 \\\hline
2 & 6 & 10 \\\hline
3 & 9 & 15 \\\hline
\end{tabular}
\end{reponse}
\q{2}{Probabilité d'obtenir 15.}
\begin{reponse}
Les 6 issues sont équiprobables ; 15 apparaît 2 fois : $p = \dfrac26 = \dfrac13$.
\end{reponse}
\q{3}{« 2 chances sur 3 d'obtenir un multiple de 3. »}
\begin{reponse}
Multiples de 3 : 15, 6, 9 et 15, soit 4 issues sur 6 : $p = \dfrac46 = \dfrac23$. L'affirmation est \textbf{vraie}.
\end{reponse}
\q{4}{Nombres des boules de la troisième boîte.}
\begin{reponse}
$165 = 3 \times 5 \times 11$ : les deux premières boules donnent 15, la troisième porte \textbf{11}.\\
$78 = 2 \times 3 \times 13$ : les deux premières boules donnent 6, la troisième porte \textbf{13}.
\end{reponse}
'''),
dict(id='2024-polj-5a', s='polj', ex=5, titre='Exercice 5 -- Les fonctions f et g, partie A', theme='Image, antécédent',
     consigne='Traite la partie A.', regions=[(5, 515, 665)], s3=8, n3=[5, 14], s4=None, n4=None,
     corr=r'''
\q{1}{Calculer $f(-4)$.}
\begin{reponse}
$f(-4) = (-4 + 2)^2 - (-4) = (-2)^2 + 4 = 4 + 4 = \mathbf{8}$.
\end{reponse}
\q{2}{Un antécédent de 3 par $g$.}
\begin{reponse}
Je résous $7x + 4 = 3$ : $7x = -1$, donc $x = -\dfrac17$. Un antécédent de 3 est $\mathbf{-\dfrac17}$.
\end{reponse}
'''),
dict(id='2024-polj-5b', s='polj', ex=5, titre='Exercice 5 -- Les fonctions f et g, partie B', theme='Tableur, Scratch, identité remarquable, équation produit',
     consigne='Traite la partie B (le programme est en annexe).', regions=[(5, 515, 598), (5, 664, 752), (6, 128, 495), (7, 305, 568)], s3=19, n3=[5, 18, 25, 32], s4=None, n4=None,
     corr=r'''
\q{3.a}{Formule saisie en B3.}
\begin{reponse}
\texttt{=7*B1+4}
\end{reponse}
\q{3.b}{Solution(s) trouvée(s) par Paul.}
\begin{reponse}
Seule la colonne E donne la même valeur pour $f$ et $g$ ($f(0) = g(0) = 4$) : Paul trouve la solution \textbf{0}.
\end{reponse}
\q{4.a}{Compléter la ligne 4.}
\begin{reponse}
\texttt{mettre image par g à 7 * réponse + 4}.
\end{reponse}
\q{4.b}{Réponse du programme pour 0.}
\begin{reponse}
$f(0) = 2^2 - 0 = 4$ et $g(0) = 4$ : le programme dit « le nombre choisi est une solution de f(x)=g(x) ».
\end{reponse}
\q{4.c}{Une solution de $f(x) = g(x)$.}
\begin{reponse}
\textbf{0}.
\end{reponse}
\q{5.a}{Se ramener à $x^2 - 4x = 0$.}
\begin{reponse}
$f(x) = (x + 2)^2 - x = x^2 + 4x + 4 - x = x^2 + 3x + 4$.
\[ x^2 + 3x + 4 = 7x + 4 \iff x^2 + 3x - 7x + 4 - 4 = 0 \iff x^2 - 4x = 0. \]
\end{reponse}
\q{5.b}{Factoriser $x^2 - 4x$.}
\begin{reponse}
$x^2 - 4x = x(x - 4)$.
\end{reponse}
\q{5.c}{Solutions de $f(x) = g(x)$.}
\begin{reponse}
$x(x - 4) = 0 \iff x = 0$ ou $x - 4 = 0$. Les solutions sont \textbf{0 et 4}.
\end{reponse}
\q{6}{Qui a résolu l'équation ?}
\begin{reponse}
Seule \textbf{Morgane} l'a résolue : elle trouve toutes les solutions, 0 et 4. Paul (entiers de $-3$ à 3) et Jane (entiers de $-5$ à 3) n'ont testé que quelques valeurs : ils trouvent 0 mais pas 4, et ne peuvent pas savoir s'il existe d'autres solutions.
\end{reponse}
'''),
dict(id='2024-polj-5fac', s='polj', ex=5, extra=True, titre='Exercice 5 -- Factoriser x² − 4x', theme='Factoriser par un facteur commun',
     consigne='Traite seulement la question 5.b.', regions=[(6, 398, 447)], s3=16, n3=[25], s4=3, n4=[7],
     corr=r'''
\q{5.b}{Factoriser l'expression $x^2 - 4x$.}
\begin{reponse}
$x^2 = x \times x$ et $4x = 4 \times x$ : le facteur commun est $x$.
\[ x^2 - 4x = x \times x - 4 \times x = \mathbf{x(x - 4)}. \]
\end{reponse}
'''),
]
