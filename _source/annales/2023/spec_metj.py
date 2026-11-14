# DNB Métropole – Antilles-Guyane, 26 juin 2023
SOURCE = ('dnb_metropole_juin_2023.pdf', 'Métropole – Antilles-Guyane, 26 juin 2023')
QCM = (2, 253, 366)
E2 = (1, 437, 785)
PARTS = [
dict(id='2023-metj-1', s='metj', ex=1, titre='Exercice 1 -- Les lunettes de soleil', theme='Tableur, étendue, moyenne',
     regions=[(1, 135, 437)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{1}{Étendue des prix.}
\begin{reponse}
$160 - 75 = 85$ €.
\end{reponse}
\q{2.a}{Formule en G2.}
\begin{reponse}
\texttt{=SOMME(B2:F2)}.
\end{reponse}
\q{2.b}{Nombre total de paires vendues.}
\begin{reponse}
$1\,200 + 950 + 875 + 250 + 300 = \mathbf{3\,575}$ paires.
\end{reponse}
\q{3.a}{Montant total des ventes.}
\begin{reponse}
$1\,200 \times 75 + 950 \times 100 + 875 \times 110 + 250 \times 140 + 300 \times 160$\\
$= 90\,000 + 95\,000 + 96\,250 + 35\,000 + 48\,000 = \mathbf{364\,250}$ €.
\end{reponse}
\q{3.b}{Prix moyen d'une paire.}
\begin{reponse}
$364\,250 \div 3\,575 \approx \mathbf{101{,}89}$ €.
\end{reponse}
'''),
dict(id='2023-metj-2a', s='metj', ex=2, titre='Exercice 2 -- Rectangle et triangles, questions 1 et 2', theme='Aires, théorème de Pythagore',
     consigne='Traite les questions 1 et 2.', regions=[E2, (2, 128, 190)], s3=2, n3=[], s4=4, n4=[10],
     corr=r'''
\q{1}{Aire du rectangle BCDE.}
\begin{reponse}
$BC \times BE = 4{,}2 \times 7 = 29{,}4$ cm².
\end{reponse}
\q{2.a}{Montrer que AE = 5,6 cm.}
\begin{reponse}
Le triangle $ABE$ est rectangle en $A$, d'hypoténuse $[BE]$. D'après le théorème de Pythagore :
\[ AE^2 = BE^2 - AB^2 = 7^2 - 4{,}2^2 = 49 - 17{,}64 = 31{,}36 \qquad\text{donc}\qquad AE = \sqrt{31{,}36} = 5{,}6 \text{ cm}. \]
\end{reponse}
\q{2.b}{Aire du triangle ABE.}
\begin{reponse}
$\dfrac{AB \times AE}{2} = \dfrac{4{,}2 \times 5{,}6}{2} = \mathbf{11{,}76}$ cm².
\end{reponse}
'''),
dict(id='2023-metj-2b', s='metj', ex=2, titre='Exercice 2 -- Rectangle et triangles, question 3', theme='Parallélisme, théorème de Thalès',
     consigne='Traite la question 3 (AE = 5,6 cm).', regions=[E2, (2, 190, 222)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{3.a}{Montrer que (ED) et (HA) sont parallèles.}
\begin{reponse}
$(HA) \perp (CD)$ par construction et $(ED) \perp (CD)$ car $BCDE$ est un rectangle. Deux droites perpendiculaires à une même droite sont parallèles : $(ED) \parallel (HA)$.
\end{reponse}
\q{3.b}{Longueur AH.}
\begin{reponse}
Les points $F$, $E$, $A$ et $F$, $D$, $H$ sont alignés, et $(ED) \parallel (AH)$. $FA = FE + EA = 7 + 5{,}6 = 12{,}6$ cm et $ED = BC = 4{,}2$ cm. D'après le théorème de Thalès :
\[ \frac{FE}{FA} = \frac{ED}{AH} \qquad\text{soit}\qquad \frac{7}{12{,}6} = \frac{4{,}2}{AH} \qquad\text{donc}\qquad AH = \frac{4{,}2 \times 12{,}6}{7} = \mathbf{7{,}56} \text{ cm}. \]
\end{reponse}
'''),
dict(id='2023-metj-3q1', s='metj', ex=3, titre='Exercice 3 -- QCM, question 1', theme='Pourcentages',
     regions=[QCM, (2, 366, 421)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{1}{60 \% de 25 élèves.}
\begin{reponse}
$25 \times 0{,}6 = 15$ filles : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2023-metj-3q2', s='metj', ex=3, titre='Exercice 3 -- QCM, question 2', theme='Décomposition en facteurs premiers',
     regions=[QCM, (2, 421, 448)], s3=24, n3=[], s4=6, n4=[14],
     corr=r'''
\q{2}{Décomposition de 126.}
\begin{reponse}
$126 = 2 \times 63 = 2 \times 9 \times 7 = 2 \times 3^2 \times 7$ (9 n'est pas premier) : \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2023-metj-3q3', s='metj', ex=3, titre='Exercice 3 -- QCM, question 3', theme='Probabilités',
     regions=[QCM, (2, 448, 530)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{3}{Probabilité d'un jeton rouge ou jaune.}
\begin{reponse}
$17 + 23 + 20 = 60$ jetons, dont $17 + 23 = 40$ rouges ou jaunes : $p = \dfrac{40}{60} = \dfrac23$, \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2023-metj-3q4', s='metj', ex=3, titre='Exercice 3 -- QCM, question 4', theme='Rotation',
     regions=[QCM, (2, 530, 701)], s3=11, n3=[17], s4=None, n4=None,
     corr=r'''
\q{4}{Image de [DC] par la rotation de centre O qui envoie A sur D.}
\begin{reponse}
De $A$ à $D$, on avance de 3 sommets : la rotation fait tourner chaque sommet de 3 crans dans le même sens. $D \to G$ et $C \to F$ : l'image de $[DC]$ est $[GF]$, \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2023-metj-3q5', s='metj', ex=3, titre='Exercice 3 -- QCM, question 5', theme='Volume du pavé, conversion',
     regions=[QCM, (2, 701, 756)], s3=21, n3=[], s4=15, n4=[36],
     corr=r'''
\q{5}{Volume du pavé droit.}
\begin{reponse}
$2 \times 1{,}3 \times 1{,}5 = 3{,}9$ m³ $= 3\,900$ L : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2023-metj-4a', s='metj', ex=4, titre='Exercice 4 -- L’escalier, questions 1 et 2', theme='Trigonométrie',
     consigne='Traite les questions 1 et 2.', regions=[(3, 135, 508)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{1.a}{Nombre de marches.}
\begin{reponse}
$272 \div 17 = \mathbf{16}$ marches.
\end{reponse}
\q{1.b}{Longueur AB.}
\begin{reponse}
$16 \times 27 = 432$ cm.
\end{reponse}
\q{2.a}{Mesure de l'angle $\widehat{BAC}$.}
\begin{reponse}
Dans le triangle $ABC$ rectangle en $B$, $[BC]$ est le côté opposé à l'angle $\widehat{BAC}$ et $[AB]$ le côté adjacent :
\[ \tan\widehat{BAC} = \frac{BC}{AB} = \frac{272}{432} \qquad\text{donc}\qquad \widehat{BAC} \approx \mathbf{32^\circ}. \]
\end{reponse}
\q{2.b}{La montée est-elle agréable ?}
\begin{reponse}
$32^\circ$ est compris entre $25^\circ$ et $40^\circ$ : \textbf{oui}.
\end{reponse}
'''),
dict(id='2023-metj-4b', s='metj', ex=4, titre='Exercice 4 -- L’escalier, question 3 (Scratch)', theme='Algorithmique (Scratch)',
     consigne='Traite la question 3 (16 marches de 17 cm de haut et 27 cm de profondeur).', regions=[(3, 135, 428), (4, 128, 458)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{3}{Compléter les lignes 5, 6, 7 et 9.}
\begin{reponse}
Ligne 5 : répéter \textbf{16} fois ; ligne 6 : tourner de \textbf{90} degrés (vers la gauche, pour monter) ; ligne 7 : avancer de \textbf{17} pas (la hauteur d'une marche) ; ligne 9 : avancer de \textbf{27} pas (la profondeur d'une marche).
\end{reponse}
'''),
dict(id='2023-metj-5a', s='metj', ex=5, titre='Exercice 5 -- Deux programmes, questions 1 et 2', theme='Programmes de calcul, expression littérale',
     consigne='Traite les questions 1 et 2.', regions=[(4, 458, 677)], s3=1, n3=[], s4=8, n4=[2, 6, 19],
     corr=r'''
\q{1.a}{Programme A avec $-3$.}
\begin{reponse}
$(-3) \times (-2) = 6$ ; $6 + 5 = 11$.
\end{reponse}
\q{1.b}{Programme B avec 5,5.}
\begin{reponse}
$5{,}5 - 5 = 0{,}5$ ; $0{,}5 \times 3 = 1{,}5$ ; $1{,}5 + 11 = \mathbf{12{,}5}$.
\end{reponse}
\q{2}{Résultat du programme B en fonction de $x$.}
\begin{reponse}
$x \longrightarrow x - 5 \longrightarrow 3(x - 5) = 3x - 15 \longrightarrow 3x - 15 + 11 = 3x - 4$.
\end{reponse}
'''),
dict(id='2023-metj-5b', s='metj', ex=5, titre='Exercice 5 -- Deux programmes, questions 3 et 4', theme='Fonctions affines, équation',
     consigne='Traite les questions 3 et 4.', regions=[(4, 458, 590), (4, 636, 677), (5, 128, 406)], s3=17, n3=[13, 26, 28], s4=None, n4=None,
     corr=r'''
\q{3.a}{Associer chaque droite à sa fonction.}
\begin{reponse}
$g(x) = 3x - 4$ a un coefficient directeur positif : sa droite monte, c'est $(D_1)$. $f(x) = -2x + 5$ a un coefficient directeur négatif : sa droite descend, c'est $(D_2)$.\\
\small (On peut aussi vérifier : $(D_2)$ passe par $(0\,;\,5)$ et $f(0) = 5$.)
\end{reponse}
\q{3.b}{Nombre qui a la même image par $f$ et $g$ (lecture).}
\begin{reponse}
Les droites se coupent au point d'abscisse environ \textbf{1,8}.
\end{reponse}
\q{4}{Le calcul.}
\begin{reponse}
\[ -2x + 5 = 3x - 4 \iff 5 + 4 = 3x + 2x \iff 9 = 5x \iff x = \frac95 = \mathbf{1{,}8}. \]
\end{reponse}
'''),
]
