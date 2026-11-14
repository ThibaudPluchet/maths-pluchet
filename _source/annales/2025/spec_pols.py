# DNB Polynésie, septembre 2025
QCM = (1, 624, 704)
PARTS = [
dict(id='2025-pols-1a', s='pols', ex=1, titre='Exercice 1 -- Le carrelage, questions 1 et 2', theme='Calculs de prix',
     consigne='Traite les questions 1 et 2.', regions=[(1, 195, 351)], s3=17, n3=[], s4=9, n4=[21],
     corr=r'''
\q{1}{Prix pour 20 m² avec chaque carreleur.}
\begin{reponse}
Carreleur A : $20 \times 80 = 1\,600$ €.\qquad Carreleur B : $20 \times 60 + 970 = 1\,200 + 970 = 2\,170$ €.
\end{reponse}
\q{2}{Prix pour 60 m² avec chaque carreleur.}
\begin{reponse}
Carreleur A : $60 \times 80 = 4\,800$ €.\qquad Carreleur B : $60 \times 60 + 970 = 3\,600 + 970 = 4\,570$ €.
\end{reponse}
'''),
dict(id='2025-pols-1b', s='pols', ex=1, titre='Exercice 1 -- Le carrelage, questions 3 à 5', theme='Fonctions linéaire et affine, équation',
     consigne="Traite les questions 3 à 5 (l'annexe est à la fin de l'énoncé).", regions=[(1, 195, 279), (1, 349, 622), (7, 160, 540)], s3=17, n3=[26, 27, 28], s4=None, n4=None,
     corr=r'''
\q{3.a}{Image de 70 par la fonction $f$.}
\begin{reponse}
$f(70) = 80 \times 70 = 5\,600$.
\end{reponse}
\q{3.b}{Antécédent de 2 400 par la fonction $f$.}
\begin{reponse}
Je cherche $x$ tel que $80x = 2\,400$ : $x = \dfrac{2\,400}{80} = 30$. L'antécédent de 2\,400 est \textbf{30}.
\end{reponse}
\q{3.c}{Tracer la représentation graphique de $f$.}
\begin{reponse}
$f$ est linéaire : sa représentation est une droite qui passe par l'origine. Avec $f(30) = 2\,400$ (ou $f(20) = 1\,600$), je trace la droite qui passe par $(0\,;\,0)$ et $(30\,;\,2\,400)$.
\end{reponse}
\q{4}{Aire maximale avec 2 800 € chez le carreleur B.}
\begin{reponse}
Je lis l'abscisse du point de $\mathcal{C}_g$ d'ordonnée 2\,800 : environ \textbf{30 m²}.\\
\small (Par le calcul : $60x + 970 = 2\,800 \iff 60x = 1\,830 \iff x = 30{,}5$.)
\end{reponse}
\q{5}{Aire pour laquelle les deux carreleurs coûtent le même prix.}
\begin{reponse}
\[ 80x = 60x + 970 \iff 20x = 970 \iff x = 48{,}5. \]
Les deux carreleurs coûtent le même prix pour \textbf{48,5 m²} ($80 \times 48{,}5 = 3\,880$ €).
\end{reponse}
'''),
dict(id='2025-pols-2q1', s='pols', ex=2, titre='Exercice 2 -- QCM, question 1', theme='Formule, expression littérale',
     regions=[QCM, (1, 704, 790)], s3=1, n3=[], s4=8, n4=[18],
     corr=r'''
\q{1}{Pointure d'un pied de 25 cm avec $p = 1{,}5(L + 1)$.}
\begin{reponse}
$p = 1{,}5 \times (25 + 1) = 1{,}5 \times 26 = 39$. \textbf{Réponse D.}
\end{reponse}
'''),
dict(id='2025-pols-2q2', s='pols', ex=2, titre='Exercice 2 -- QCM, question 2', theme='Trigonométrie (calcul d’angle)',
     regions=[QCM, (2, 137, 282)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{2}{Mesure de l'angle $\widehat{RMU}$, au degré près.}
\begin{reponse}
Dans le triangle $MUR$ rectangle en $U$, l'hypoténuse est $[MR]$ et $[UR]$ est le côté opposé à $\widehat{RMU}$ :
\[ \sin\widehat{RMU} = \frac{UR}{MR} = \frac{7{,}2}{9{,}7} \approx 0{,}742 \qquad\text{donc}\qquad \widehat{RMU} \approx 48^\circ. \]
\textbf{Réponse C.}
\end{reponse}
'''),
dict(id='2025-pols-2q3', s='pols', ex=2, titre='Exercice 2 -- QCM, question 3', theme='Vitesse',
     regions=[QCM, (2, 282, 360)], s3=14, n3=[], s4=15, n4=[35],
     corr=r'''
\q{3}{Vitesse en km/h d'un coureur qui fait 100 m en 10 s.}
\begin{reponse}
$100 \div 10 = 10$ m/s. En 1 h $= 3\,600$ s, il parcourrait $10 \times 3\,600 = 36\,000$ m $= 36$ km : \textbf{36 km/h}, réponse B.
\end{reponse}
'''),
dict(id='2025-pols-2q4', s='pols', ex=2, titre='Exercice 2 -- QCM, question 4', theme='Échelle',
     regions=[QCM, (2, 360, 444)], s3=14, n3=[], s4=5, n4=[11],
     corr=r'''
\q{4}{Largeur réelle d'un tableau dont le modèle au $\frac{1}{20}$ mesure 7 cm.}
\begin{reponse}
À l'échelle $\frac{1}{20}$, les longueurs réelles sont 20 fois plus grandes : $7 \times 20 = 140$ cm. \textbf{Réponse D.}
\end{reponse}
'''),
dict(id='2025-pols-2q5', s='pols', ex=2, titre='Exercice 2 -- QCM, question 5', theme='Coordonnées terrestres',
     regions=[QCM, (2, 444, 652)], s3=6, n3=[9], s4=None, n4=None,
     corr=r'''
\q{5}{Point de coordonnées (65° N ; 30° O).}
\begin{reponse}
Latitude 65° Nord : au-dessus de l'équateur. Longitude 30° Ouest : à gauche du méridien de Greenwich. C'est le point \textbf{A} : réponse A.
\end{reponse}
'''),
dict(id='2025-pols-3a', s='pols', ex=3, titre="Exercice 3 -- Le motif de l'Alhambra, partie 1", theme='Transformations (symétries, rotation, translation)',
     consigne='Traite la partie 1.', regions=[(2, 652, 760), (3, 118, 500)], s3=11, n3=[17], s4=None, n4=None,
     corr=r'''
\q{1}{Image du losange 1 par la symétrie centrale de centre A.}
\begin{reponse}
La symétrie centrale de centre $A$ est un demi-tour autour de $A$ : le losange 1 a pour image le \textbf{losange 7}.
\end{reponse}
\q{2}{Image du losange 3 par la symétrie axiale d'axe (AF).}
\begin{reponse}
En pliant le long de la droite $(AF)$, le losange 3 vient sur le \textbf{losange 5}.
\end{reponse}
\q{3}{Image du losange 7 par la rotation de centre A qui transforme 3 en 11.}
\begin{reponse}
Cette rotation fait tourner chaque losange de 4 « crans » de $60^\circ$ dans le sens inverse des aiguilles d'une montre (ou de 2 crans dans l'autre sens) : le losange 7 a pour image le \textbf{losange 3}.
\end{reponse}
\q{4}{Image du losange 8 par la translation qui transforme A en E.}
\begin{reponse}
La translation fait glisser le losange 8 vers le haut, de la longueur $AE$ : son image est le \textbf{losange 5}.
\end{reponse}
'''),
dict(id='2025-pols-3b', s='pols', ex=3, titre="Exercice 3 -- Le motif de l'Alhambra, partie 2 (Scratch)", theme='Algorithmique (Scratch)',
     consigne='Traite la partie 2 (l’annexe est à la fin de l’énoncé).', regions=[(2, 652, 760), (3, 118, 340), (3, 502, 790), (4, 128, 470), (7, 540, 765)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Compléter les lignes 3, 4 et 5 du bloc « hexagone ABCDEF ».}
\begin{reponse}
\texttt{3\quad répéter \fbox{6} fois}\\
\texttt{4\quad avancer de \fbox{50} pas}\qquad (5 cm $= 50$ pas)\\
\texttt{5\quad tourner de \fbox{60} degrés}\qquad (un hexagone régulier : $360 \div 6 = 60$)
\end{reponse}
\q{2}{Quel script trace le motif ?}
\begin{reponse}
Le motif s'obtient en faisant tourner l'hexagone autour de $A$ de $60^\circ$ en $60^\circ$, six fois (un tour complet : $6 \times 60 = 360$). C'est le \textbf{script C}.
\end{reponse}
'''),
dict(id='2025-pols-4a', s='pols', ex=4, titre='Exercice 4 -- Les canons à neige, partie 1', theme='Volumes, conversions, proportionnalité, pourcentages',
     consigne='Traite la partie 1.', regions=[(4, 469, 790), (5, 128, 353)], s3=14, n3=[], s4=15, n4=[34, 36],
     corr=r'''
\q{1.a}{Volume de neige pour une piste de 1 hectare et 30 cm de neige.}
\begin{reponse}
$S = 1 \text{ ha} = 10\,000 \text{ m}^2$ et $h = 30 \text{ cm} = 0{,}3$ m : $V = S \times h = 10\,000 \times 0{,}3 = 3\,000 \text{ m}^3$.
\end{reponse}
\q{1.b}{En déduire le volume d'eau nécessaire.}
\begin{reponse}
Il faut 1 m³ d'eau pour 2,5 m³ de neige : $3\,000 \div 2{,}5 = 1\,200 \text{ m}^3$ d'eau.
\end{reponse}
\q{1.c}{Coût de 1 200 m³ d'eau.}
\begin{reponse}
$1\,200 \times 4{,}30 = 5\,160$ €.
\end{reponse}
\q{2.a}{Coût de l'eau pour les 25 000 hectares de pistes.}
\begin{reponse}
$25\,000 \times 5\,160 = 129\,000\,000$ €, soit \textbf{129 millions d'euros}.
\end{reponse}
\q{2.b}{Pourcentage de la surface des pistes équipée de canons.}
\begin{reponse}
$\dfrac{9\,250}{25\,000} = 0{,}37 = 37\ \%$.
\end{reponse}
'''),
dict(id='2025-pols-4b', s='pols', ex=4, titre='Exercice 4 -- Le ski de fond, questions 1 et 3', theme='Pythagore, théorème de Thalès',
     consigne='Traite les questions 1 et 3 de la partie 2.', regions=[(4, 469, 544), (5, 351, 790), (6, 128, 160), (6, 182, 222)], s3=9, n3=[], s4=19, n4=[10, 22],
     corr=r'''
\q{1}{Longueur du segment [FD].}
\begin{reponse}
$FD = FE + ED = 300 + 300 = 600$ m (car $FE = ED = 300$ m).
\end{reponse}
\q{3.a}{Montrer que EB = 500 m.}
\begin{reponse}
Le triangle $BED$ est rectangle en $D$, d'hypoténuse $[EB]$. D'après le théorème de Pythagore :
\[ EB^2 = ED^2 + BD^2 = 300^2 + 400^2 = 90\,000 + 160\,000 = 250\,000 \qquad\text{donc}\qquad EB = \sqrt{250\,000} = 500 \text{ m}. \]
\end{reponse}
\q{3.b}{Calculer la longueur du segment [DK].}
\begin{reponse}
Les points $H$, $D$, $E$ et $H$, $K$, $B$ sont alignés, et $(DK) \parallel (EB)$. D'après le théorème de Thalès :
\[ \frac{HD}{HE} = \frac{HK}{HB} = \frac{DK}{EB} \qquad\text{avec}\qquad HD = 300 \text{ m et } HE = 600 \text{ m}. \]
\[ \frac{300}{600} = \frac{DK}{500} \qquad\text{donc}\qquad DK = \frac{300 \times 500}{600} = 250 \text{ m}. \]
\end{reponse}
'''),
dict(id='2025-pols-4c', s='pols', ex=4, titre='Exercice 4 -- Le ski de fond, questions 2 et 4', theme='Trigonométrie (calcul de longueur)',
     consigne='Traite les questions 2 et 4 de la partie 2 (on sait que FD = 600 m et DK = 250 m).', regions=[(4, 469, 544), (5, 351, 790), (6, 158, 182), (6, 222, 258)], s3=15, n3=[24], s4=None, n4=None,
     corr=r'''
\q{2}{Longueur du segment [AF], arrondie au mètre.}
\begin{reponse}
Dans le triangle $ACF$ rectangle en $C$, l'hypoténuse est $[AF]$ et $[AC]$ est le côté adjacent à l'angle $\widehat{CAF}$ :
\[ \cos\widehat{CAF} = \frac{AC}{AF} \qquad\text{donc}\qquad AF = \frac{AC}{\cos 30^\circ} = \frac{400}{\cos 30^\circ} \approx 462 \text{ m}. \]
\end{reponse}
\q{4}{Longueur du parcours A, F, E, D, K.}
\begin{reponse}
$AF + FE + ED + DK \approx 462 + 300 + 300 + 250 = 1\,312$ m (soit $AF + FD + DK$).
\end{reponse}
'''),
dict(id='2025-pols-5a', s='pols', ex=5, titre='Exercice 5 -- La collecte de vêtements, questions 1 et 2', theme='Pourcentage, tableur, probabilité, moyenne, médiane',
     consigne='Traite les questions 1 et 2.', regions=[(6, 258, 589)], s3=23, n3=[], s4=11, n4=[24, 34, 47],
     corr=r'''
\q{1}{Inès donne 70 \% de ses 20 tee-shirts.}
\begin{reponse}
$20 \times \dfrac{70}{100} = 20 \times 0{,}7 = 14$ : elle va en donner 14.
\end{reponse}
\q{2.a}{Formule à saisir dans la cellule H2.}
\begin{reponse}
\texttt{=SOMME(B2:G2)}
\end{reponse}
\q{2.b}{Probabilité qu'un tee-shirt pris au hasard soit à Yuna.}
\begin{reponse}
Total : $14 + 6 + 9 + 11 + 12 + 8 = 60$ tee-shirts, dont 12 à Yuna : $p = \dfrac{12}{60} = \dfrac15$.
\end{reponse}
\q{2.c}{Nombre moyen de tee-shirts donnés.}
\begin{reponse}
$60 \div 6 = 10$ tee-shirts par ami en moyenne.
\end{reponse}
\q{2.d}{Médiane du nombre de tee-shirts donnés.}
\begin{reponse}
Rangés dans l'ordre : 6 ; 8 ; 9 ; 11 ; 12 ; 14. Il y a 6 valeurs (nombre pair) : la médiane est la moyenne des $3^{\text{e}}$ et $4^{\text{e}}$ valeurs,
$\dfrac{9 + 11}{2} = 10$.
\end{reponse}
'''),
dict(id='2025-pols-5b', s='pols', ex=5, titre='Exercice 5 -- La collecte de vêtements, question 3', theme='Diviseurs, décomposition, répartition en lots',
     consigne='Traite la question 3.', regions=[(6, 258, 338), (6, 587, 695)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{3.a}{Peut-on faire 4 lots ? 3 lots ?}
\begin{reponse}
4 lots : non, car 63 n'est pas divisible par 4 ($63 = 4 \times 15 + 3$).\\
3 lots : oui, car $168 = 3 \times 56$ et $63 = 3 \times 21$ : 3 lots de 56 tee-shirts et 21 pantalons.
\end{reponse}
\q{3.b}{Décompositions en produit de facteurs premiers de 168 et de 63.}
\begin{reponse}
$168 = 2 \times 84 = 2 \times 2 \times 42 = 2 \times 2 \times 2 \times 21 = 2^3 \times 3 \times 7$\qquad et\qquad $63 = 3^2 \times 7$.
\end{reponse}
\q{3.c}{Nombre maximum de lots.}
\begin{reponse}
Le nombre de lots doit diviser 168 et 63. Le plus grand diviseur commun est $3 \times 7 = 21$.\\
On peut faire au maximum \textbf{21 lots}, contenant chacun $168 \div 21 = 8$ tee-shirts et $63 \div 21 = 3$ pantalons.
\end{reponse}
'''),
]
