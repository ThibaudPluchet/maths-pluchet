# DNB Martinique, 3 juillet 2024
SOURCE = ('dnb_martinique_juil_2024.pdf', 'Martinique, 3 juillet 2024')
QCM = (2, 128, 152)
E3 = (2, 612, 668)
PARTS = [
dict(id='2024-mart-1a', s='mart', ex=1, titre='Exercice 1 -- Les dragées, question 1', theme='Probabilités',
     consigne='Traite la question 1.', regions=[(1, 132, 240)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{1.a}{Nombre total de dragées.}
\begin{reponse}
$630 + 810 = \mathbf{1\,440}$ dragées.
\end{reponse}
\q{1.b}{Probabilité d'obtenir une dragée blanche.}
\begin{reponse}
Les dragées sont indiscernables : $p = \dfrac{810}{1\,440} = \dfrac{9}{16} = 0{,}5625$.
\end{reponse}
'''),
dict(id='2024-mart-1b', s='mart', ex=1, titre='Exercice 1 -- Les ballotins, question 2', theme='Diviseurs, décomposition, répartition',
     consigne='Traite la question 2 (630 dragées roses et 810 dragées blanches).', regions=[(1, 132, 162), (1, 240, 404)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{2.a}{Peuvent-ils réaliser 21 ballotins ?}
\begin{reponse}
$630 = 21 \times 30$, mais $810 \div 21 \approx 38{,}6$ n'est pas un nombre entier : 21 ne divise pas 810. \textbf{Non}.
\end{reponse}
\q{2.b}{Décomposer 630 et 810.}
\begin{reponse}
$630 = 2 \times 3^2 \times 5 \times 7$ \qquad et \qquad $810 = 2 \times 3^4 \times 5$.
\end{reponse}
\q{2.c}{Nombre maximum de ballotins et composition.}
\begin{reponse}
Le nombre de ballotins doit diviser 630 et 810. Le plus grand diviseur commun reprend les facteurs communs : $2 \times 3^2 \times 5 = 90$.\\
Ils peuvent faire \textbf{90 ballotins}, chacun avec $630 \div 90 = 7$ dragées roses et $810 \div 90 = 9$ dragées blanches.
\end{reponse}
'''),
dict(id='2024-mart-2q1', s='mart', ex=2, titre='Exercice 2 -- QCM, question 1', theme='Écriture scientifique',
     regions=[(1, 404, 500), QCM, (2, 152, 193)], s3=25, n3=[], s4=13, n4=[31],
     corr=r'''
\q{1}{Écriture scientifique de 13 420.}
\begin{reponse}
$13\,420 = 1{,}342 \times 10\,000 = 1{,}342 \times 10^4$ : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2024-mart-2q2', s='mart', ex=2, titre='Exercice 2 -- QCM, question 2', theme='Médiane',
     regions=[(1, 404, 500), QCM, (2, 193, 288)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{2}{Médiane des onze performances.}
\begin{reponse}
Les 11 valeurs sont rangées dans l'ordre croissant : la médiane est la $6^{\text{e}}$, \textbf{85,74} m : \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2024-mart-2q3', s='mart', ex=2, titre='Exercice 2 -- QCM, questions 3 et 4', theme='Symétrie axiale, rotation',
     regions=[(1, 404, 500), QCM, (2, 288, 465)], s3=11, n3=[17], s4=None, n4=None,
     corr=r'''
\q{3}{Image du motif gris par la symétrie d'axe (d).}
\begin{reponse}
L'axe $(d)$ passe entre les motifs 2 et 3 : 2 et 3 sont symétriques, puis 1 et 4, puis le motif gris et le motif 5 : \textbf{réponse C}.
\end{reponse}
\q{4}{Image du motif gris par la rotation de centre O, de 90° dans le sens antihoraire.}
\begin{reponse}
La rosace a 16 motifs : un quart de tour, c'est $16 \div 4 = 4$ motifs. En tournant dans le sens contraire des aiguilles d'une montre : 15, 14, 13, \textbf{12} : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2024-mart-2q5', s='mart', ex=2, titre='Exercice 2 -- QCM, questions 5 et 6', theme='Lecture graphique, coefficient directeur',
     regions=[(1, 404, 500), QCM, (2, 465, 612)], s3=17, n3=[13, 28], s4=None, n4=None,
     corr=r'''
\q{5}{Image de 2 par la fonction $f$.}
\begin{reponse}
Le point de la droite d'abscisse 2 a pour ordonnée 0 : $f(2) = 0$, \textbf{réponse A}.
\end{reponse}
\q{6}{Coefficient directeur de la droite (d).}
\begin{reponse}
La droite passe par $(0\,;\,4)$ et $(2\,;\,0)$ : quand $x$ augmente de 2, $y$ diminue de 4. Le coefficient directeur est $\dfrac{-4}{2} = -2$ : \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2024-mart-3a', s='mart', ex=3, titre='Exercice 3 -- La course d’Oscar, questions 1 à 5', theme='Réciproque de Pythagore, parallélisme, Thalès',
     consigne='Traite les questions 1 à 5.', regions=[E3, (3, 128, 397)], s3=13, n3=[], s4=19, n4=[22, 32],
     corr=r'''
\q{1}{Montrer que DK = 480 m.}
\begin{reponse}
$K$ est sur le segment $[DL]$ : $DK = DL - KL = 600 - 120 = 480$ m.
\end{reponse}
\q{2}{Montrer que DKJ est rectangle en K.}
\begin{reponse}
Le plus grand côté est $[DJ]$. \quad $DJ^2 = 520^2 = 270\,400$ \quad et \quad $DK^2 + KJ^2 = 480^2 + 200^2 = 230\,400 + 40\,000 = 270\,400$.\\
$DJ^2 = DK^2 + KJ^2$ : d'après la réciproque du théorème de Pythagore, $DKJ$ est rectangle en $K$.
\end{reponse}
\q{3}{Justifier que (KJ) et (LA) sont parallèles.}
\begin{reponse}
$(KJ) \perp (DL)$ (question 2) et $(LA) \perp (DL)$ (triangle $DLA$ rectangle en $L$). Deux droites perpendiculaires à une même droite sont parallèles : $(KJ) \parallel (LA)$.
\end{reponse}
\q{4}{Montrer que DA = 650 m.}
\begin{reponse}
Les points $D$, $K$, $L$ et $D$, $J$, $A$ sont alignés, et $(KJ) \parallel (LA)$. D'après le théorème de Thalès :
\[ \frac{DK}{DL} = \frac{DJ}{DA} \qquad\text{soit}\qquad \frac{480}{600} = \frac{520}{DA} \qquad\text{donc}\qquad DA = \frac{600 \times 520}{480} = 650 \text{ m}. \]
\end{reponse}
\q{5}{Longueur du trajet DKJA.}
\begin{reponse}
$JA = DA - DJ = 650 - 520 = 130$ m. \quad $DK + KJ + JA = 480 + 200 + 130 = \mathbf{810}$ m.
\end{reponse}
'''),
dict(id='2024-mart-3b', s='mart', ex=3, titre='Exercice 3 -- La course d’Oscar, question 6', theme='Trigonométrie',
     consigne='Traite la question 6 (DL = 600 m et DA = 650 m).', regions=[E3, (3, 128, 312), (3, 396, 470)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{6}{L'angle $\widehat{LDA}$ est-il inférieur à 25° ?}
\begin{reponse}
Dans le triangle $DLA$ rectangle en $L$, $[DL]$ est le côté adjacent à $\widehat{LDA}$ et $[DA]$ l'hypoténuse :
\[ \cos\widehat{LDA} = \frac{DL}{DA} = \frac{600}{650} \qquad\text{donc}\qquad \widehat{LDA} \approx 22{,}6^\circ. \]
$22{,}6^\circ < 25^\circ$ : \textbf{oui}, la caméra peut filmer toute la course.
\end{reponse}
'''),
dict(id='2024-mart-4a', s='mart', ex=4, titre='Exercice 4 -- Programme de calcul, questions 1, 2 et 5', theme='Programme de calcul, expression littérale, Scratch',
     consigne='Traite les questions 1, 2 et 5.', regions=[(3, 474, 654), (3, 687, 702), (4, 128, 426)], s3=1, n3=[], s4=8, n4=[18, 20],
     corr=r'''
\q{1}{Avec 5 comme nombre de départ.}
\begin{reponse}
$5^2 = 25$ ; $25 - 3 \times 5 = 25 - 15 = 10$ ; $10 - 4 = 6$.
\end{reponse}
\q{2}{Résultat en fonction de $x$.}
\begin{reponse}
$x \longrightarrow x^2 \longrightarrow x^2 - 3x \longrightarrow \mathbf{x^2 - 3x - 4}$.
\end{reponse}
\q{5}{Compléter les lignes 4 et 6 du programme.}
\begin{reponse}
Ligne 4 : \texttt{mettre y à x * x} ; \quad ligne 6 : \texttt{mettre Résultat à y - z - 4}.
\end{reponse}
'''),
dict(id='2024-mart-4b', s='mart', ex=4, titre='Exercice 4 -- Programme de calcul, questions 3 et 4', theme='Double distributivité, équation produit',
     consigne='Traite les questions 3 et 4 (le résultat du programme est x² − 3x − 4).', regions=[(3, 474, 603), (3, 652, 688)], s3=19, n3=[18, 32], s4=None, n4=None,
     corr=r'''
\q{3}{Vérifier que le résultat s'écrit $(x + 1)(x - 4)$.}
\begin{reponse}
$(x + 1)(x - 4) = x^2 - 4x + x - 4 = x^2 - 3x - 4$ : c'est bien le résultat du programme.
\end{reponse}
\q{4}{Nombres de départ qui donnent 0.}
\begin{reponse}
Je résous $(x + 1)(x - 4) = 0$ : $x + 1 = 0$ ou $x - 4 = 0$, soit $x = -1$ ou $x = 4$.\\
Il faut choisir \textbf{$-1$ ou 4}.
\end{reponse}
'''),
dict(id='2024-mart-5', s='mart', ex=5, titre='Exercice 5 -- La piscine octogonale', theme='Aires, volume, débit',
     regions=[(4, 425, 768), (5, 128, 198)], s3=14, n3=[], s4=15, n4=[36],
     corr=r'''
\q{1.a}{Montrer que AE = 1,4 m.}
\begin{reponse}
Les quatre triangles retirés sont identiques, donc $AE = FB$. Sur le côté $[AB]$ : $AE + EF + FB = 5$, soit $2 \times AE + 2{,}2 = 5$, donc $AE = \dfrac{5 - 2{,}2}{2} = 1{,}4$ m.
\end{reponse}
\q{1.b}{Aire du triangle AEL.}
\begin{reponse}
Le triangle $AEL$ est rectangle isocèle en $A$ : $AL = AE = 1{,}4$ m. \quad $\mathcal{A} = \dfrac{1{,}4 \times 1{,}4}{2} = 0{,}98$ m².
\end{reponse}
\q{1.c}{Aire de l'octogone.}
\begin{reponse}
$\mathcal{A} = 5 \times 5 - 4 \times 0{,}98 = 25 - 3{,}92 = 21{,}08$ m².
\end{reponse}
\q{2.a}{Volume d'eau pour remplir la piscine aux trois quarts.}
\begin{reponse}
Hauteur d'eau : $\dfrac34 \times 1{,}5 = 1{,}125$ m. \quad $V = 21{,}08 \times 1{,}125 = 23{,}715 \approx 24$ m³.
\end{reponse}
\q{2.b}{Durée de remplissage de 24 m³ à 12 L/min.}
\begin{reponse}
$24$ m³ $= 24\,000$ L. \quad $24\,000 \div 12 = 2\,000$ min. \quad $2\,000 = 33 \times 60 + 20$ : \textbf{33 h 20 min}.
\end{reponse}
'''),
]
