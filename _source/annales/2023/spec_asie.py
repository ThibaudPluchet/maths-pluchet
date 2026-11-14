# DNB Asie, 19 juin 2023
SOURCE = ('dnb_asie_juin_2023.pdf', 'Asie, 19 juin 2023')
QCM = [(1, 519, 606), (2, 145, 165)]
E3 = (2, 712, 730)
PARTS = [
dict(id='2023-asie-1a', s='asie', ex=1, titre='Exercice 1 -- Le centre de loisirs, questions 1 à 3', theme='Théorème de Pythagore, théorème de Thalès',
     consigne='Traite les questions 1 à 3.', regions=[(1, 146, 430)], s3=9, n3=[], s4=10, n4=[10, 22],
     corr=r'''
\q{1}{Longueur CD.}
\begin{reponse}
$E$ est sur le segment $[CD]$ : $CD = CE + ED = 30 + 10 = \mathbf{40}$ m.
\end{reponse}
\q{2}{Longueur CG, au dixième.}
\begin{reponse}
$(DG) \perp (CD)$ : le triangle $CDG$ est rectangle en $D$, d'hypoténuse $[CG]$. D'après le théorème de Pythagore :
\[ CG^2 = CD^2 + DG^2 = 40^2 + 24^2 = 1\,600 + 576 = 2\,176 \qquad\text{donc}\qquad CG = \sqrt{2\,176} \approx \mathbf{46{,}6} \text{ m}. \]
\end{reponse}
\q{3}{Montrer que EF = 18 m.}
\begin{reponse}
Les points $C$, $E$, $D$ et $C$, $F$, $G$ sont alignés, et $(EF) \parallel (DG)$. D'après le théorème de Thalès :
\[ \frac{CE}{CD} = \frac{EF}{DG} \qquad\text{soit}\qquad \frac{30}{40} = \frac{EF}{24} \qquad\text{donc}\qquad EF = \frac{30 \times 24}{40} = 18 \text{ m}. \]
\end{reponse}
'''),
dict(id='2023-asie-1b', s='asie', ex=1, titre='Exercice 1 -- Le centre de loisirs, questions 4 et 5', theme='Aires, coût',
     consigne='Traite les questions 4 et 5 (CD = 40 m et EF = 18 m).', regions=[(1, 146, 352), (1, 430, 520)], s3=9, n3=[], s4=10, n4=[],
     corr=r'''
\q{4}{Budget pour semer la zone de jeux.}
\begin{reponse}
$(EF) \parallel (DG)$ et $(DG) \perp (CD)$, donc $(EF) \perp (CD)$ : le triangle $CEF$ est rectangle en $E$.
\[ \mathcal{A}_{CEF} = \frac{CE \times EF}{2} = \frac{30 \times 18}{2} = 270 \text{ m}^2. \]
$270 \div 140 \approx 1{,}9$ : il faut 2 sacs, soit $2 \times 22{,}90 = \mathbf{45{,}80}$ €.
\end{reponse}
\q{5}{Le potager est-il plus grand que la zone de jeux ?}
\begin{reponse}
$\mathcal{A}_{CDG} = \dfrac{40 \times 24}{2} = 480$ m², donc le potager mesure $480 - 270 = 210$ m².\\
$210 < 270$ : \textbf{non}, la direction a tort.
\end{reponse}
'''),
dict(id='2023-asie-2q1', s='asie', ex=2, titre='Exercice 2 -- QCM, question 1', theme='Probabilités',
     regions=QCM + [(2, 165, 251)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{1}{Probabilité d'obtenir une bille rouge.}
\begin{reponse}
$2 + 3 + 3 = 8$ billes dont 2 rouges : $p = \dfrac28 = \dfrac14$, \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2023-asie-2q2', s='asie', ex=2, titre='Exercice 2 -- QCM, question 2', theme='Pourcentages',
     regions=QCM + [(2, 251, 283)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{2}{Coefficient pour augmenter un prix de 25 \%.}
\begin{reponse}
$1 + \dfrac{25}{100} = \mathbf{1{,}25}$ : \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2023-asie-2q3', s='asie', ex=2, titre='Exercice 2 -- QCM, question 3', theme='Homothétie',
     regions=QCM + [(2, 283, 432)], s3=18, n3=[30], s4=None, n4=None,
     corr=r'''
\q{3}{Transformation qui envoie le triangle 1 sur le triangle 2.}
\begin{reponse}
Le triangle 2 est trois fois plus grand et du même côté du point $D$ : homothétie de centre $D$ et de rapport \textbf{3}, \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2023-asie-2q4', s='asie', ex=2, titre='Exercice 2 -- QCM, question 4', theme='Fonctions linéaires et affines',
     regions=QCM + [(2, 432, 499)], s3=17, n3=[26], s4=None, n4=None,
     corr=r'''
\q{4}{$f(x) = -9 - 7x$.}
\begin{reponse}
$f(x) = -7x - 9$ est de la forme $ax + b$ avec $b \neq 0$ : c'est une fonction affine, non linéaire. \textbf{Réponse A}.
\end{reponse}
'''),
dict(id='2023-asie-2q5', s='asie', ex=2, titre='Exercice 2 -- QCM, question 5', theme='Puissances de 10, écriture scientifique',
     regions=QCM + [(2, 499, 571)], s3=25, n3=[], s4=13, n4=[30, 31],
     corr=r'''
\q{5}{9 461 milliards de km en mètres.}
\begin{reponse}
$9\,461 \times 10^9$ km $= 9{,}461 \times 10^{12}$ km $= 9{,}461 \times 10^{12} \times 10^3$ m $= \mathbf{9{,}461 \times 10^{15}}$ m : \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2023-asie-2q6', s='asie', ex=2, titre='Exercice 2 -- QCM, question 6', theme='Trigonométrie',
     regions=QCM + [(2, 571, 692)], s3=15, n3=[24], s4=None, n4=None,
     corr=r'''
\q{6}{Expression de AB.}
\begin{reponse}
Le triangle est rectangle en $A$ ; pour l'angle de $30^\circ$ en $B$, $[AB]$ est le côté adjacent et $[BC]$ l'hypoténuse (5 cm) : $\cos 30^\circ = \dfrac{AB}{5}$, donc $AB = \mathbf{5 \times \cos 30^\circ}$, \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2023-asie-3a', s='asie', ex=3, titre='Exercice 3 -- Le programme de calcul, partie A', theme='Programme de calcul, expression littérale',
     consigne='Traite la partie A.', regions=[E3, (3, 128, 345)], s3=1, n3=[], s4=8, n4=[2, 18, 20],
     corr=r'''
\q{1}{Avec 3 au départ.}
\begin{reponse}
$3^2 = 9$ ; $9 \times 5 = 45$ ; $45 + 4 = 49$ ; $49 \times 2 = 98$ ; $98 - 8 = 90$.
\end{reponse}
\q{2}{Avec 2 et avec $-2$.}
\begin{reponse}
$2^2 = 4$ et $(-2)^2 = 4$ : après la première étape, on obtient le même nombre, donc le même résultat. Ici : $4 \times 5 = 20$ ; $24$ ; $48$ ; $\mathbf{40}$ dans les deux cas.
\end{reponse}
\q{3}{Résultat en fonction de $x$.}
\begin{reponse}
$x \longrightarrow x^2 \longrightarrow 5x^2 \longrightarrow 5x^2 + 4 \longrightarrow 2(5x^2 + 4) = 10x^2 + 8 \longrightarrow 10x^2 + 8 - 8 = \mathbf{10x^2}$.
\end{reponse}
'''),
dict(id='2023-asie-3b', s='asie', ex=3, titre='Exercice 3 -- Le programme de calcul, partie B', theme='Antécédents, tableur, équation x² = a',
     consigne='Traite la partie B.', regions=[E3, (3, 128, 254), (3, 345, 600), (4, 128, 468)], s3=19, n3=[13, 32], s4=None, n4=None,
     corr=r'''
\q{4}{Antécédents de 30 (lecture graphique).}
\begin{reponse}
On lit environ \textbf{1,7} sur le graphique ; comme $f(-x) = f(x)$, l'autre antécédent est environ \textbf{$-1{,}7$}.
\end{reponse}
\q{5.a}{Formule en B2.}
\begin{reponse}
\texttt{=10*A2*A2} \quad (ou \texttt{=10*A2\^{}2}).
\end{reponse}
\q{5.b}{Nombre qui donne le résultat le plus proche de 30.}
\begin{reponse}
$30 - 29{,}929 = 0{,}071$ et $30{,}276 - 30 = 0{,}276$ : c'est \textbf{1,73}.
\end{reponse}
\q{6}{Valeur exacte du nombre positif.}
\begin{reponse}
$10x^2 = 30 \iff x^2 = 3$ : le nombre positif est $\mathbf{\sqrt3}$ ($\approx 1{,}732$).
\end{reponse}
'''),
dict(id='2023-asie-4', s='asie', ex=4, titre='Exercice 4 -- Les frises (Scratch)', theme='Algorithmique (Scratch)',
     regions=[(4, 466, 790), (5, 128, 366)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Coordonnées du lutin après le bloc 1.}
\begin{reponse}
$(-220\,;\,0)$.
\end{reponse}
\q{2}{Lignes 3 et 5 du bloc 2 (carré).}
\begin{reponse}
Ligne 3 : répéter \textbf{4} fois ; ligne 5 : tourner de \textbf{90} degrés.
\end{reponse}
\q{3}{Ce que dessine le bloc 3.}
\begin{reponse}
Un rectangle de 100 pas sur 50 pas, soit \textbf{5 cm sur 2,5 cm} à l'échelle (1 cm pour 20 pas).
\end{reponse}
\q{4.a}{Frise réalisée par le script.}
\begin{reponse}
Chaque tour de boucle dessine un carré, avance de 50 pas (la largeur du carré), dessine un rectangle puis avance de 100 pas : carré, rectangle, carré, rectangle\ldots\ C'est la \textbf{frise 1} (carrés et rectangles alternés).
\end{reponse}
\q{4.b}{Script de l'autre frise.}
\begin{reponse}
Les trois carrés puis les trois rectangles :\\
\texttt{Quand drapeau cliqué ; initialisation ;}\\
\texttt{répéter 3 fois [carré ; avancer de 50 pas] ;}\\
\texttt{répéter 3 fois [rectangle ; avancer de 100 pas]}.
\end{reponse}
'''),
dict(id='2023-asie-5a', s='asie', ex=5, titre='Exercice 5 -- Le marchand de glaces, questions 1 et 2', theme='Moyenne, pourcentage',
     consigne='Traite les questions 1 et 2.', regions=[(5, 365, 760)], s3=23, n3=[], s4=15, n4=[24, 34],
     corr=r'''
\q{1}{Nombre moyen de pots vendus par semaine.}
\begin{reponse}
Juillet : $453 + 649 + 786 + 854 = 2\,742$ ; août : $860 + 1\,003 + 957 + 838 = 3\,658$. Total : $6\,400$ pots en 8 semaines.\\
Moyenne : $6\,400 \div 8 = \mathbf{800}$ pots par semaine.
\end{reponse}
\q{2}{Recette de la période.}
\begin{reponse}
Pots à une boule : $6\,400 \times 0{,}67 = 4\,288$ ; pots à deux boules : $6\,400 - 4\,288 = 2\,112$.\\
Recette : $4\,288 \times 2{,}80 + 2\,112 \times 3{,}50 = 12\,006{,}40 + 7\,392 = \mathbf{19\,398{,}40}$ €.
\end{reponse}
'''),
dict(id='2023-asie-5b', s='asie', ex=5, titre='Exercice 5 -- Le marchand de glaces, question 3', theme='Volume de la boule, conversion',
     consigne='Traite la question 3.', regions=[(5, 365, 698), (5, 760, 790), (6, 128, 190)], s3=21, n3=[36], s4=None, n4=None,
     corr=r'''
\q{3.a}{Volume d'une boule de glace.}
\begin{reponse}
Le rayon est $4{,}2 \div 2 = 2{,}1$ cm : $V = \dfrac43 \times \pi \times 2{,}1^3 \approx 38{,}8 \approx 39$ cm³.
\end{reponse}
\q{3.b}{Nombre maximal de boules avec un bac de 10 L.}
\begin{reponse}
10 L $= 10$ dm³ $= 10\,000$ cm³. \quad $10\,000 \div 39 \approx 256{,}4$ : on peut faire au maximum \textbf{256 boules} (257 avec la valeur non arrondie $38{,}8$ cm³).
\end{reponse}
'''),
]
