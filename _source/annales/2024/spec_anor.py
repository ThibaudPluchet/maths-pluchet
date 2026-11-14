# DNB Amérique du Nord, 29 mai 2024
SOURCE = ('dnb_ameri_nord_mai_2024.pdf', 'Amérique du Nord, 29 mai 2024')
H1 = (1, 132, 197)
E2 = (1, 622, 664)
PARTS = [
dict(id='2024-anor-1a', s='anor', ex=1, titre='Exercice 1 -- Vrai ou faux, affirmations A et B', theme='Moyenne, médiane',
     regions=[H1, (1, 197, 280)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{A}{La moyenne des prix est 11,40 €.}
\begin{reponse}
\[ \bar{x} = \frac{12 + 15 + 10 + 7 + 13}{5} = \frac{57}{5} = 11{,}4 \text{ €}. \]
L'affirmation A est \textbf{vraie}.
\end{reponse}
\q{B}{La médiane des prix est 10 €.}
\begin{reponse}
Je range les prix dans l'ordre croissant : 7 ; 10 ; \textbf{12} ; 13 ; 15. Il y a 5 valeurs : la médiane est la $3^{\text{e}}$, soit 12 €.\\
L'affirmation B est \textbf{fausse}.
\end{reponse}
'''),
dict(id='2024-anor-1b', s='anor', ex=1, titre='Exercice 1 -- Vrai ou faux, affirmation C', theme='Vitesse',
     regions=[H1, (1, 280, 313)], s3=14, n3=[], s4=15, n4=[35],
     corr=r'''
\q{C}{Sa vitesse moyenne était de 14 km/h.}
\begin{reponse}
20 m en 6 s, c'est $20 \times 10 = 200$ m en 60 s, puis $200 \times 60 = 12\,000$ m en 3\,600 s : 12 km en 1 h.\\
Sa vitesse moyenne est de 12 km/h, pas 14 km/h : l'affirmation C est \textbf{fausse}.
\end{reponse}
'''),
dict(id='2024-anor-1c', s='anor', ex=1, titre='Exercice 1 -- Vrai ou faux, affirmation D', theme='Probabilités, nombres premiers',
     regions=[H1, (1, 313, 365)], s3=22, n3=[], s4=20, n4=[14, 47],
     corr=r'''
\q{D}{La probabilité de tirer un nombre premier est $\frac{7}{15}$.}
\begin{reponse}
Les nombres premiers entre 1 et 15 sont 2 ; 3 ; 5 ; 7 ; 11 ; 13 : il y en a 6 (1 n'est pas premier).\\
Les 15 boules ont la même chance d'être tirées : $p = \dfrac{6}{15} = \dfrac{2}{5}$, et non $\dfrac{7}{15}$.\\
L'affirmation D est \textbf{fausse}.
\end{reponse}
'''),
dict(id='2024-anor-1d', s='anor', ex=1, titre='Exercice 1 -- Vrai ou faux, affirmation E', theme='Homothétie, aires',
     regions=[H1, (1, 365, 620)], s3=18, n3=[30], s4=None, n4=None,
     corr=r'''
\q{E}{L'aire de A$'$B$'$C$'$ est égale à 3 fois l'aire de ABC.}
\begin{reponse}
Une homothétie de rapport $-3$ multiplie les longueurs par 3 (la valeur absolue du rapport), donc les aires par $3^2 = 9$.\\
L'aire de $A'B'C'$ est 9 fois l'aire de $ABC$ : l'affirmation E est \textbf{fausse}.
\end{reponse}
'''),
dict(id='2024-anor-2a', s='anor', ex=2, titre='Exercice 2 -- Programme de calcul, questions 1 à 3', theme='Programme de calcul, expression littérale',
     consigne='Traite les questions 1 à 3.', regions=[E2, (2, 128, 530)], s3=1, n3=[], s4=8, n4=[2, 6, 19],
     corr=r'''
\q{1}{Avec 2 comme nombre de départ.}
\begin{reponse}
À gauche : $2 + 2 = 4$ puis $4 \times 4 = 16$. À droite : $2 \times 5 = 10$ puis $10 - 3 = 7$.\\
Résultat : $16 \times 7 = 112$.
\end{reponse}
\q{2}{Avec $-3$ comme nombre de départ.}
\begin{reponse}
À gauche : $-3 + 2 = -1$ puis $-1 \times 4 = -4$. À droite : $-3 \times 5 = -15$ puis $-15 - 3 = -18$.\\
Résultat : $(-4) \times (-18) = \mathbf{72}$.
\end{reponse}
\q{3}{Expressions qui donnent le résultat.}
\begin{reponse}
À gauche on obtient $(x + 2) \times 4 = 4x + 8$ ; à droite $5x - 3$. Le résultat est $(x + 2) \times 4 \times (5x - 3) = (4x + 8)(5x - 3)$.\\
Les bonnes expressions sont la \textbf{C} et la \textbf{D}.
\end{reponse}
'''),
dict(id='2024-anor-2b', s='anor', ex=2, titre='Exercice 2 -- Programme de calcul, questions 4 et 5', theme='Équation produit, double distributivité',
     consigne='Traite les questions 4 et 5 (le résultat du programme est (4x + 8)(5x − 3)).', regions=[E2, (2, 128, 402), (2, 528, 566)], s3=19, n3=[18, 32], s4=None, n4=None,
     corr=r'''
\q{4}{Les deux nombres de départ qui donnent 0.}
\begin{reponse}
Je résous l'équation produit $(4x + 8)(5x - 3) = 0$. Un produit est nul si l'un de ses facteurs est nul :
\[ 4x + 8 = 0 \iff x = -2 \qquad\text{ou}\qquad 5x - 3 = 0 \iff x = \frac35 = 0{,}6. \]
Les deux nombres sont \textbf{$-2$ et 0,6}.
\end{reponse}
\q{5}{Développer et réduire l'expression B.}
\begin{reponse}
\[ (4x + 2)(5x - 3) = 20x^2 - 12x + 10x - 6 = \mathbf{20x^2 - 2x - 6}. \]
\end{reponse}
'''),
dict(id='2024-anor-3a', s='anor', ex=3, titre='Exercice 3 -- Le cinéma, questions 1 et 2', theme='Calculs de prix',
     consigne='Traite les questions 1 et 2.', regions=[(2, 575, 730)], s3=17, n3=[], s4=9, n4=[21],
     corr=r'''
\q{1}{Prix de trois entrées au tarif « Classique ».}
\begin{reponse}
$3 \times 11 = 33$ €.
\end{reponse}
\q{2}{Prix de huit entrées au tarif « Essentiel ».}
\begin{reponse}
$50 + 8 \times 5 = 50 + 40 = 90$ €.
\end{reponse}
'''),
dict(id='2024-anor-3b', s='anor', ex=3, titre='Exercice 3 -- Le cinéma, questions 3 à 5', theme='Fonctions affines, lecture graphique',
     consigne='Traite les questions 3 à 5.', regions=[(2, 575, 665), (2, 728, 790), (3, 128, 530)], s3=17, n3=[13, 26], s4=None, n4=None,
     corr=r'''
\q{3}{Associer chaque fonction à son tarif.}
\begin{reponse}
$f : x \mapsto 50 + 5x$ : tarif « Essentiel » ; $g : x \mapsto 240$ : tarif « Liberté » ; $h : x \mapsto 11x$ : tarif « Classique ».
\end{reponse}
\q{4}{Tarif proportionnel au nombre d'entrées.}
\begin{reponse}
Le tarif \textbf{« Classique »} : $h(x) = 11x$ est une fonction linéaire ; sa représentation $(d_1)$ est une droite qui passe par l'origine.
\end{reponse}
\q{5.a}{Nombre maximal d'entrées avec 150 € au tarif « Essentiel ».}
\begin{reponse}
Sur $(d_2)$, l'ordonnée 150 correspond à l'abscisse 20 : \textbf{20 entrées} (en effet $50 + 20 \times 5 = 150$).
\end{reponse}
\q{5.b}{À partir de combien d'entrées « Liberté » est-il le plus intéressant ?}
\begin{reponse}
$(d_2)$ passe au-dessus de $(d_3)$ après l'abscisse 38 ($50 + 38 \times 5 = 240$) : à partir de \textbf{39 entrées}.
\end{reponse}
\q{5.c}{Tarif qui donne le plus d'entrées avec 200 €.}
\begin{reponse}
Avec 200 € : 18 entrées au tarif « Classique » ($200 \div 11 \approx 18{,}2$), 30 entrées au tarif « Essentiel » ; le tarif « Liberté » coûte 240 €.\\
C'est le tarif \textbf{« Essentiel »}.
\end{reponse}
'''),
dict(id='2024-anor-4a', s='anor', ex=4, titre='Exercice 4 -- La terrasse, questions 1 et 2', theme='Théorème de Pythagore, périmètre',
     consigne='Traite les questions 1 et 2.', regions=[(3, 545, 732), (4, 128, 364)], s3=2, n3=[], s4=4, n4=[10],
     corr=r'''
\q{1}{Montrer que FJ = 4 m.}
\begin{reponse}
$EFGH$ est un rectangle, donc $EF = HG = 6$ m. Les points $E$, $F$, $J$ sont alignés : $FJ = EJ - EF = 10 - 6 = 4$ m.
\end{reponse}
\q{2}{Longueur minimale de planches.}
\begin{reponse}
$FG = EH = 3$ m. Le triangle $FGJ$ est rectangle en $F$, d'hypoténuse $[GJ]$. D'après le théorème de Pythagore :
\[ GJ^2 = FG^2 + FJ^2 = 3^2 + 4^2 = 9 + 16 = 25 \qquad\text{donc}\qquad GJ = \sqrt{25} = 5 \text{ m}. \]
Le tour de la terrasse : $EJ + JG + GH + HE = 10 + 5 + 6 + 3 = 24$ m. Il faut au minimum \textbf{24 m} de planches.
\end{reponse}
'''),
dict(id='2024-anor-4b', s='anor', ex=4, titre='Exercice 4 -- La terrasse, questions 3.a et 3.b', theme='Volume d’un prisme, proportionnalité',
     consigne='Traite les questions 3.a et 3.b.', regions=[(3, 545, 732), (4, 128, 318), (4, 362, 427)], s3=21, n3=[], s4=17, n4=[],
     corr=r'''
\q{3.a}{Le volume de la terrasse est inférieur à 4 m³.}
\begin{reponse}
La base du prisme est la surface $EJGH$ : le rectangle $EFGH$ plus le triangle rectangle $FJG$.
\[ \mathcal{A} = 6 \times 3 + \frac{4 \times 3}{2} = 18 + 6 = 24 \text{ m}^2. \]
La hauteur est 15 cm, soit 0,15 m : $V = 24 \times 0{,}15 = 3{,}6 \text{ m}^3$, et $3{,}6 < 4$.
\end{reponse}
\q{3.b}{Masse de ciment pour 4 m³ de béton.}
\begin{reponse}
$4 \times 250 = \mathbf{1\,000}$ kg de ciment.
\end{reponse}
'''),
dict(id='2024-anor-4c', s='anor', ex=4, titre='Exercice 4 -- La terrasse, question 3.c', theme='Ratio',
     consigne='Traite la question 3.c (il faut 1 000 kg de ciment pour 4 m³ de béton).', regions=[(3, 545, 603), (4, 362, 383), (4, 428, 470)], s3=14, n3=[22], s4=None, n4=None,
     corr=r'''
\q{3.c}{Masses de gravier et de sable (ratio 2 : 7 : 5).}
\begin{reponse}
Il faut 1\,000 kg de ciment, qui correspondent à 2 parts : une part pèse $1\,000 \div 2 = 500$ kg.\\
Gravier : $7 \times 500 = \mathbf{3\,500}$ kg. \quad Sable : $5 \times 500 = \mathbf{2\,500}$ kg.
\end{reponse}
'''),
dict(id='2024-anor-4d', s='anor', ex=4, titre='Exercice 4 -- La terrasse, question 4', theme='Aire, pourcentages, coût minimum',
     consigne='Traite la question 4 (la terrasse a une aire de 24 m²).', regions=[(3, 545, 603), (4, 128, 318), (4, 469, 755)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{4}{Type et nombre de pots pour un coût minimum.}
\begin{reponse}
Deux couches sur 24 m², c'est comme peindre $2 \times 24 = 48$ m². Il faut $48 \div 5 = 9{,}6$ litres de peinture.\\
\begin{itemize}
\item Un pot B (10 L) : 129,90 €.
\item Deux pots A (10 L), le deuxième à $-50$ \% : $79{,}90 + 79{,}90 \div 2 = 79{,}90 + 39{,}95 = 119{,}85$ €.
\end{itemize}
Le moins cher : \textbf{deux pots A}, pour 119,85 €.
\end{reponse}
'''),
dict(id='2024-anor-5a', s='anor', ex=5, titre='Exercice 5 -- La figure, partie A', theme='Triangle équilatéral, angles, parallélisme',
     consigne='Traite la partie A.', regions=[(5, 132, 392)], s3=20, n3=[], s4=19, n4=[45],
     corr=r'''
\q{1}{Montrer que le triangle ABC est équilatéral.}
\begin{reponse}
D'après le codage, $\widehat{BAC} = \widehat{ABC} = 60^\circ$. La somme des angles d'un triangle vaut $180^\circ$ :
\[ \widehat{ACB} = 180^\circ - 60^\circ - 60^\circ = 60^\circ. \]
Les trois angles mesurent $60^\circ$ : le triangle $ABC$ est équilatéral.
\end{reponse}
\q{2}{Montrer que (DE) et (AB) sont parallèles.}
\begin{reponse}
D'après le codage, $CD = CE = DE$ : le triangle $CDE$ est équilatéral, donc $\widehat{CED} = 60^\circ$.\\
Les angles $\widehat{CED}$ et $\widehat{CAB}$ sont alternes-internes (les points $A$, $C$, $E$ sont alignés) et ils ont la même mesure, $60^\circ$ : les droites $(DE)$ et $(AB)$ sont parallèles.\\
\small (Autre méthode : $\dfrac{CE}{CA} = \dfrac{80}{240} = \dfrac13$ et $\dfrac{CD}{CB} = \dfrac{80}{240} = \dfrac13$, la réciproque du théorème de Thalès permet de conclure.)
\end{reponse}
'''),
dict(id='2024-anor-5b', s='anor', ex=5, titre='Exercice 5 -- Le programme, partie B (Scratch)', theme='Algorithmique (Scratch)',
     consigne='Traite la partie B.', regions=[(5, 132, 334), (5, 392, 772), (6, 128, 488)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Coordonnées du point de départ du lutin.}
\begin{reponse}
$(-180\,;\,-150)$ : c'est l'instruction de la ligne 2.
\end{reponse}
\q{2}{Valeur à saisir à la ligne 4.}
\begin{reponse}
\textbf{240} : le premier triangle tracé est le grand triangle $ABC$, de côté 240 mm, soit 240 pas.
\end{reponse}
\q{3}{Case du lutin après la ligne 7.}
\begin{reponse}
Après le grand triangle, le lutin est revenu en $A$ (case D8), orienté vers la droite. Il tourne de $60^\circ$ vers la gauche puis avance de 240 pas sur le côté $[AC]$ prolongé : il arrive en $C$, case \textbf{G3}.
\end{reponse}
\q{4}{Rôle de « côté / 3 » à la ligne 8.}
\begin{reponse}
Le petit triangle $CDE$ a pour côté $80 = 240 \div 3$ mm : la variable côté est divisée par 3 pour tracer ce triangle trois fois plus petit.
\end{reponse}
'''),
]
