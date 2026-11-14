# DNB Nouvelle-Calédonie, 7 décembre 2023
SOURCE = ('dnb_caledonie_dec_2023.pdf', 'Nouvelle-Calédonie, 7 décembre 2023')
QCM = (1, 177, 295)
PARTS = [
dict(id='2023-ncal-1q1', s='ncal', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Puissances de 10',
     regions=[QCM, (1, 295, 350)], s3=25, n3=[], s4=13, n4=[30, 31],
     corr=r'''
\q{1}{Probabilité d'une attaque mortelle par un requin.}
\begin{reponse}
Une probabilité est comprise entre 0 et 1 : seul $2{,}7 \times 10^{-7} = 0{,}000\,000\,27$ convient (\textbf{réponse A}).
\end{reponse}
'''),
dict(id='2023-ncal-1q2', s='ncal', ex=1, titre='Exercice 1 -- QCM, question 2', theme='Calculs avec des fractions',
     regions=[QCM, (1, 350, 382)], s3=5, n3=[], s4=18, n4=[42, 43],
     corr=r'''
\q{2}{$\frac35 - \frac25 \times \frac74$.}
\begin{reponse}
La multiplication d'abord : $\dfrac25 \times \dfrac74 = \dfrac{14}{20} = \dfrac{7}{10}$, puis $\dfrac35 - \dfrac{7}{10} = \dfrac{6}{10} - \dfrac{7}{10} = -\dfrac{1}{10}$ : \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2023-ncal-1q3', s='ncal', ex=1, titre='Exercice 1 -- QCM, question 3', theme='Pourcentage de réduction',
     regions=[QCM, (1, 382, 423)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{3}{Pourcentage de réduction de 80 € à 60 €.}
\begin{reponse}
Réduction : 20 € sur 80 € : $\dfrac{20}{80} = 0{,}25$, soit \textbf{25 \%} (réponse B).
\end{reponse}
'''),
dict(id='2023-ncal-1q4', s='ncal', ex=1, titre='Exercice 1 -- QCM, question 4', theme='Homothétie',
     regions=[QCM, (1, 423, 563)], s3=18, n3=[30], s4=None, n4=None,
     corr=r'''
\q{4}{L'homothétie de centre A qui transforme B en F\ldots}
\begin{reponse}
D'après le codage, $F$ est le milieu de $[AB]$ : le rapport est $\dfrac12$. $E$, centre du parallélogramme, est le milieu de $[AC]$ : l'homothétie \textbf{transforme C en E} (réponse C).
\end{reponse}
'''),
dict(id='2023-ncal-1q5', s='ncal', ex=1, titre='Exercice 1 -- QCM, question 5', theme='Médiane',
     regions=[QCM, (1, 563, 628)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{5}{Médiane de la série.}
\begin{reponse}
Dans l'ordre : 3 ; 5 ; 8 ; 10 ; \textbf{11} ; 12 ; 14 ; 17 ; 20. Il y a 9 valeurs : la médiane est la $5^{\text{e}}$, \textbf{11} (réponse C).
\end{reponse}
'''),
dict(id='2023-ncal-2', s='ncal', ex=2, titre='Exercice 2 -- Paniers de légumes', theme='Décomposition, diviseurs, multiples',
     regions=[(1, 644, 790), (2, 128, 305)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{1.a}{Décomposer 78 et 51.}
\begin{reponse}
$78 = 2 \times 3 \times 13$ \qquad et \qquad $51 = 3 \times 17$.
\end{reponse}
\q{1.b}{Nombre maximal de paniers.}
\begin{reponse}
$39 = 3 \times 13$. Le seul facteur commun aux trois nombres est 3 : \textbf{3 paniers}.
\end{reponse}
\q{1.c}{Composition d'un panier.}
\begin{reponse}
$39 \div 3 = 13$ salades, $78 \div 3 = 26$ carottes et $51 \div 3 = 17$ aubergines.
\end{reponse}
\q{2.a}{Aubergines non utilisées avec 13 paniers.}
\begin{reponse}
$51 = 13 \times 3 + 12$ : \textbf{12 aubergines} ne sont pas utilisées.
\end{reponse}
\q{2.b}{Aubergines à cueillir en plus.}
\begin{reponse}
Le multiple de 13 suivant est $13 \times 4 = 52$ : il suffit d'en cueillir \textbf{1}.
\end{reponse}
\q{3}{Nombre maximal de tomates (entre 110 et 125).}
\begin{reponse}
Il faut un multiple de 13 : $13 \times 8 = 104$, $13 \times 9 = 117$, $13 \times 10 = 130$. Seul \textbf{117} est entre 110 et 125 (9 tomates par panier).
\end{reponse}
'''),
dict(id='2023-ncal-3a', s='ncal', ex=3, titre='Exercice 3 -- Isolation, questions 1 à 3', theme='Trigonométrie, aire',
     consigne='Traite les questions 1 à 3.', regions=[(2, 306, 760)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{1}{Justifier que DE = 1,8 m.}
\begin{reponse}
$ABEC$ est un rectangle, donc $BE = AC = 2{,}5$ m. $E$ est sur $[BD]$ : $DE = BD - BE = 4{,}3 - 2{,}5 = 1{,}8$ m.
\end{reponse}
\q{2}{Montrer que DF = 3,6 m.}
\begin{reponse}
Dans le triangle $DEF$ rectangle en $E$, $[DE]$ est le côté opposé à l'angle $\widehat{EFD}$ et $[DF]$ l'hypoténuse :
\[ \sin 30^\circ = \frac{DE}{DF} \qquad\text{donc}\qquad DF = \frac{1{,}8}{\sin 30^\circ} = \frac{1{,}8}{0{,}5} = 3{,}6 \text{ m}. \]
\end{reponse}
\q{3}{Nombre de rouleaux de laine de roche.}
\begin{reponse}
Aire : $12 \times 3{,}6 = 43{,}2$ m². \quad $43{,}2 \div 6 = 7{,}2$ : il faut \textbf{8 rouleaux}.
\end{reponse}
'''),
dict(id='2023-ncal-3b', s='ncal', ex=3, titre='Exercice 3 -- Isolation, questions 4 et 5', theme='Théorème de Pythagore, volume, masse',
     consigne='Traite les questions 4 et 5 (DE = 1,8 m).', regions=[(2, 306, 638), (2, 760, 790), (3, 128, 277)], s3=2, n3=[], s4=4, n4=[10, 36],
     corr=r'''
\q{4}{Montrer que CD = 8,2 m.}
\begin{reponse}
$CE = AB = 8$ m. Le triangle $CDE$ est rectangle en $E$, d'hypoténuse $[CD]$. D'après le théorème de Pythagore :
\[ CD^2 = CE^2 + DE^2 = 8^2 + 1{,}8^2 = 64 + 3{,}24 = 67{,}24 \qquad\text{donc}\qquad CD = \sqrt{67{,}24} = 8{,}2 \text{ m}. \]
\end{reponse}
\q{5}{Masse de ouate de cellulose.}
\begin{reponse}
Volume : $12 \times 8{,}2 \times 0{,}1 = 9{,}84$ m³. \quad Masse : $9{,}84 \times 40 = \mathbf{393{,}6}$ kg.
\end{reponse}
'''),
dict(id='2023-ncal-4', s='ncal', ex=4, titre='Exercice 4 -- Les roches de la Ouaïème', theme='Théorème de Thalès, vitesse, durée',
     regions=[(3, 277, 790), (4, 128, 193)], s3=9, n3=[], s4=10, n4=[22, 35],
     corr=r'''
\q{1}{Justifier que (PN) et (VM) sont parallèles.}
\begin{reponse}
D'après le codage, $(PN) \perp (DM)$ et $(VM) \perp (DM)$ : deux droites perpendiculaires à une même droite sont parallèles.
\end{reponse}
\q{2}{Altitude au panneau P.}
\begin{reponse}
Les points $D$, $P$, $V$ et $D$, $N$, $M$ sont alignés, et $(PN) \parallel (VM)$. D'après le théorème de Thalès :
\[ \frac{DP}{DV} = \frac{PN}{VM} \qquad\text{soit}\qquad \frac{3}{3{,}8} = \frac{PN}{0{,}741} \qquad\text{donc}\qquad PN = \frac{3 \times 0{,}741}{3{,}8} = 0{,}585 \text{ km}. \]
Fabienne est à \textbf{585 m} d'altitude.
\end{reponse}
\q{3}{Vitesse moyenne sur [DP].}
\begin{reponse}
3 km en 2 h : $3 \div 2 = \mathbf{1{,}5}$ km/h.
\end{reponse}
\q{4}{A-t-elle dépassé 2 h 30 min ?}
\begin{reponse}
Il reste $3{,}8 - 3 = 0{,}8$ km à 1,2 km/h : $\dfrac{0{,}8}{1{,}2} = \dfrac23$ h $= 40$ min. Durée totale : 2 h 40 min, plus que 2 h 30 min : \textbf{oui}.
\end{reponse}
'''),
dict(id='2023-ncal-5a', s='ncal', ex=5, titre='Exercice 5 -- Fonctions, questions 1 et 2', theme='Lecture graphique, tableur, fonction affine',
     consigne='Traite les questions 1 et 2 (le graphique et le tableau sont en annexe).', regions=[(4, 193, 432), (6, 180, 690)], s3=17, n3=[13, 14, 26, 28], s4=None, n4=None,
     corr=r'''
\q{1.a}{La fonction $f$ est-elle affine ?}
\begin{reponse}
\textbf{Non} : sa représentation graphique n'est pas une droite.
\end{reponse}
\q{1.b}{Compléter le tableau.}
\begin{reponse}
$f(-1) = -4$ ; $f(0) = -3$ ; $f(1) = 0$ ; $f(2) = 5$.
\end{reponse}
\q{1.c}{Formule saisie en B2.}
\begin{reponse}
\texttt{=(B1+3)*(B1-1)}.
\end{reponse}
\q{2.a}{Image de $-2$ par $g$.}
\begin{reponse}
$g(-2) = 2 \times (-2) + 1 = \mathbf{-3}$.
\end{reponse}
\q{2.b}{Calculer $g(3)$.}
\begin{reponse}
$g(3) = 2 \times 3 + 1 = \mathbf{7}$.
\end{reponse}
\q{2.c}{Antécédent de 2 par $g$.}
\begin{reponse}
$2x + 1 = 2 \iff 2x = 1 \iff x = \mathbf{0{,}5}$.
\end{reponse}
\q{2.d}{Tracer la représentation de $g$.}
\begin{reponse}
Une droite qui passe par $(0\,;\,1)$ et $(3\,;\,7)$.
\end{reponse}
'''),
dict(id='2023-ncal-5b', s='ncal', ex=5, titre='Exercice 5 -- Fonctions, question 3', theme='Double distributivité, équation x² = a',
     consigne='Traite la question 3 (g(x) = 2x + 1).', regions=[(4, 193, 210), (4, 432, 497)], s3=19, n3=[18, 32], s4=None, n4=None,
     corr=r'''
\q{3.a}{Développer $(x + 3)(x - 1)$.}
\begin{reponse}
$(x + 3)(x - 1) = x^2 - x + 3x - 3 = \mathbf{x^2 + 2x - 3}$.
\end{reponse}
\q{3.b}{Valeurs de $x$ telles que $f(x) = g(x)$.}
\begin{reponse}
$x^2 + 2x - 3 = 2x + 1 \iff x^2 = 4 \iff x = 2$ ou $x = -2$.
\end{reponse}
'''),
dict(id='2023-ncal-6', s='ncal', ex=6, titre='Exercice 6 -- Hexagone régulier (Scratch)', theme='Angles, algorithmique (Scratch)',
     consigne='Le bloc « Hexagone » est en annexe.', regions=[(4, 495, 790), (5, 128, 582), (7, 145, 415)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1.a}{Mesure de l'angle $\widehat{XBC}$.}
\begin{reponse}
$A$, $B$, $X$ sont alignés : $\widehat{XBC} = 180^\circ - 120^\circ = \mathbf{60^\circ}$.
\end{reponse}
\q{1.b}{Compléter le bloc Hexagone.}
\begin{reponse}
Répéter \textbf{6} fois ; tourner de \textbf{60} degrés (l'angle extérieur).
\end{reponse}
\q{2.a}{Nombre d'hexagones tracés.}
\begin{reponse}
\textbf{5} (boucle « répéter 5 fois »).
\end{reponse}
\q{2.b}{Côté du 1\textsuperscript{er} hexagone.}
\begin{reponse}
\textbf{32}.
\end{reponse}
\q{2.c}{Côté du 2\textsuperscript{e} hexagone.}
\begin{reponse}
$32 \times 1{,}5 = \mathbf{48}$.
\end{reponse}
\q{2.d}{Dessin correspondant.}
\begin{reponse}
Le lutin ne se déplace pas entre deux hexagones : ils ont tous le même point de départ et grandissent. C'est le \textbf{dessin 3}.
\end{reponse}
'''),
]
