# DNB Métropole, 10 septembre 2025
QCM = (1, 531, 610)
PARTS = [
dict(id='2025-mets-1a', s='mets', ex=1, titre='Exercice 1 -- Les chansons, questions 1 et 2', theme='Effectifs, moyenne, durées',
     consigne='Traite les questions 1 et 2.', regions=[(1, 235, 364)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{1}{Nombre de berceuses.}
\begin{reponse}
$22 - 9 - 6 = 7$ : il y a 7 berceuses.
\end{reponse}
\q{2}{Durée moyenne d'une chanson, en minute et seconde.}
\begin{reponse}
\[ \text{moyenne} = \frac{55 \text{ min}}{22} = 2{,}5 \text{ min}. \]
Or $0{,}5 \text{ min} = 0{,}5 \times 60 \text{ s} = 30$ s : la durée moyenne d'une chanson est \textbf{2 min 30 s}.
\end{reponse}
'''),
dict(id='2025-mets-1b', s='mets', ex=1, titre='Exercice 1 -- Les chansons, question 3', theme='Probabilités, nombres premiers',
     consigne='Traite la question 3 (il y a 7 berceuses).', regions=[(1, 235, 316), (1, 362, 530)], s3=22, n3=[], s4=20, n4=[14, 47],
     corr=r'''
\q{3.a}{Probabilité que la chanson soit une comptine.}
\begin{reponse}
Il y a 6 comptines sur 22 chansons, choisies au hasard : $p = \dfrac{6}{22} = \dfrac{3}{11}$.
\end{reponse}
\q{3.b}{Probabilité que la chanson ne soit pas une berceuse.}
\begin{reponse}
Il y a 7 berceuses, donc $22 - 7 = 15$ chansons qui n'en sont pas : $p = \dfrac{15}{22}$.\\
(Ou : $1 - \dfrac{7}{22} = \dfrac{15}{22}$, avec l'évènement contraire.)
\end{reponse}
\q{3.c}{Le numéro est un nombre premier : la probabilité est-elle supérieure à $\frac13$ ?}
\begin{reponse}
Les nombres premiers entre 1 et 22 sont 2, 3, 5, 7, 11, 13, 17 et 19 : il y en a 8.
\[ p = \frac{8}{22} = \frac{4}{11} \approx 0{,}36 \qquad\text{et}\qquad \frac13 \approx 0{,}33. \]
(Ou : $\frac{4}{11} = \frac{12}{33}$ et $\frac13 = \frac{11}{33}$.) La probabilité est bien supérieure à $\frac13$.
\end{reponse}
'''),
dict(id='2025-mets-2q1', s='mets', ex=2, titre='Exercice 2 -- QCM, question 1', theme='Étendue',
     regions=[QCM, (1, 610, 721)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{1}{Étendue de la série 4 ; 8 ; 11 ; 7 ; 2 ; 3 ; 14.}
\begin{reponse}
Étendue $=$ plus grande valeur $-$ plus petite valeur $= 14 - 2 = 12$. \textbf{Réponse C.}
\end{reponse}
'''),
dict(id='2025-mets-2q2', s='mets', ex=2, titre='Exercice 2 -- QCM, question 2', theme='Unités de volume',
     regions=[QCM, (1, 721, 790)], s3=21, n3=[], s4=17, n4=[],
     corr=r'''
\q{2}{Volume correspondant à 1 L.}
\begin{reponse}
$1 \text{ L} = 1 \text{ dm}^3$ (un cube de 10 cm de côté). \textbf{Réponse C.}
\end{reponse}
'''),
dict(id='2025-mets-2q3', s='mets', ex=2, titre='Exercice 2 -- QCM, question 3', theme='Écriture scientifique',
     regions=[QCM, (2, 128, 198)], s3=25, n3=[], s4=13, n4=[31],
     corr=r'''
\q{3}{Nombre dont l'écriture scientifique est $8{,}6 \times 10^{-4}$.}
\begin{reponse}
Multiplier par $10^{-4}$, c'est diviser par $10\,000$ : la virgule se déplace de 4 rangs vers la gauche.
$8{,}6 \times 10^{-4} = 0{,}000\,86$. \textbf{Réponse B.}
\end{reponse}
'''),
dict(id='2025-mets-2q4', s='mets', ex=2, titre='Exercice 2 -- QCM, question 4', theme='Ratio',
     regions=[QCM, (2, 198, 275)], s3=14, n3=[22], s4=None, n4=None,
     corr=r'''
\q{4}{Drapeau au ratio 3 : 2, longueur 90 cm : largeur ?}
\begin{reponse}
Le ratio $3 : 2$ signifie $\dfrac{\text{longueur}}{3} = \dfrac{\text{largeur}}{2}$. Ici $90 \div 3 = 30$, donc largeur $= 2 \times 30 = 60$ cm. \textbf{Réponse D.}
\end{reponse}
'''),
dict(id='2025-mets-2q5', s='mets', ex=2, titre='Exercice 2 -- QCM, question 5', theme='Pourcentages',
     regions=[QCM, (2, 275, 350)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{5}{Prix passé de 75 € à 60 € : pourcentage de réduction ?}
\begin{reponse}
La réduction est de $75 - 60 = 15$ €, et $\dfrac{15}{75} = 0{,}2 = 20\ \%$. \textbf{Réponse D.}
\end{reponse}
'''),
dict(id='2025-mets-2q6', s='mets', ex=2, titre='Exercice 2 -- QCM, question 6', theme='Identité remarquable',
     regions=[QCM, (2, 350, 447)], s3=12, n3=[19], s4=None, n4=None,
     corr=r'''
\q{6}{Forme factorisée de $4x^2 - 25$.}
\begin{reponse}
$4x^2 - 25 = (2x)^2 - 5^2 = (2x - 5)(2x + 5)$, avec $a^2 - b^2 = (a-b)(a+b)$. \textbf{Réponse B.}
\end{reponse}
'''),
dict(id='2025-mets-3a', s='mets', ex=3, titre='Exercice 3 -- Géométrie, question 1', theme='Théorème de Thalès',
     consigne='Traite la question 1.', regions=[(2, 447, 698)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{1.a}{Montrer que CE = 4,5 cm.}
\begin{reponse}
$E$ est sur le segment $[BC]$, donc $CE = BC - BE = 7{,}5 - 3 = 4{,}5$ cm.
\end{reponse}
\q{1.b}{Démontrer que EF = 3,6 cm.}
\begin{reponse}
Les points $C$, $E$, $B$ et $C$, $F$, $D$ sont alignés, et les droites $(EF)$ et $(BD)$ sont parallèles.\\
D'après le théorème de Thalès :
\[ \frac{CE}{CB} = \frac{CF}{CD} = \frac{EF}{BD} \qquad\text{soit}\qquad \frac{4{,}5}{7{,}5} = \frac{EF}{6}. \]
\[ EF = \frac{6 \times 4{,}5}{7{,}5} = \frac{27}{7{,}5} = 3{,}6 \text{ cm}. \]
\end{reponse}
'''),
dict(id='2025-mets-3b', s='mets', ex=3, titre='Exercice 3 -- Géométrie, question 2', theme='Réciproque de Pythagore',
     consigne='Traite la question 2 (on sait que CE = 4,5 cm et EF = 3,6 cm).', regions=[(2, 447, 662), (2, 696, 712)], s3=13, n3=[], s4=14, n4=[32],
     corr=r'''
\q{2}{Démontrer que le triangle CEF est rectangle en F.}
\begin{reponse}
Dans le triangle $CEF$, le plus grand côté est $[CE]$.
\[ CE^2 = 4{,}5^2 = 20{,}25 \qquad\qquad CF^2 + EF^2 = 2{,}7^2 + 3{,}6^2 = 7{,}29 + 12{,}96 = 20{,}25. \]
$CE^2 = CF^2 + EF^2$ : d'après la réciproque du théorème de Pythagore, le triangle $CEF$ est rectangle en $F$.
\end{reponse}
'''),
dict(id='2025-mets-3c', s='mets', ex=3, titre='Exercice 3 -- Géométrie, question 3', theme='Trigonométrie, triangles semblables',
     consigne='Traite la question 3 (on sait que CEF est rectangle en F).', regions=[(2, 447, 662), (2, 711, 752)], s3=10, n3=[6, 16], s4=None, n4=None,
     corr=r'''
\q{3.a}{Mesure de l'angle $\widehat{BCA}$, arrondie au degré.}
\begin{reponse}
Dans le triangle $ABC$ rectangle en $B$, $[AB]$ est le côté opposé à $\widehat{BCA}$ et $[BC]$ le côté adjacent :
\[ \tan\widehat{BCA} = \frac{AB}{BC} = \frac{10}{7{,}5} \qquad\text{donc}\qquad \widehat{BCA} = \arctan\left(\frac{10}{7{,}5}\right) \approx 53^\circ. \]
\end{reponse}
\q{3.b}{Les triangles ABC et CEF sont-ils semblables ?}
\begin{reponse}
Le triangle $ABC$ est rectangle en $B$ et le triangle $CEF$ est rectangle en $F$ : ils ont chacun un angle droit.\\
Ils ont aussi l'angle $\widehat{C}$ en commun. Deux triangles qui ont deux angles de mêmes mesures sont semblables (leurs troisièmes angles sont alors égaux aussi) : \textbf{oui, ils sont semblables}.
\end{reponse}
'''),
dict(id='2025-mets-4a', s='mets', ex=4, titre='Exercice 4 -- La piscine, questions 1 et 2', theme='Programme de calcul, expression littérale',
     consigne='Traite les questions 1 et 2.', regions=[(3, 134, 328)], s3=1, n3=[], s4=8, n4=[6, 18, 20],
     corr=r'''
\q{1}{Temps de filtration pour une eau à 26 °C.}
\begin{reponse}
$26 + 4 = 30$ puis $30 \times 0{,}5 = 15$ : le temps de filtration est bien de 15 h.
\end{reponse}
\q{2}{Montrer que le temps de filtration s'écrit $0{,}5x + 2$.}
\begin{reponse}
$x \;\longrightarrow\; x + 4 \;\longrightarrow\; (x + 4) \times 0{,}5 = 0{,}5x + 0{,}5 \times 4 = 0{,}5x + 2$.
\end{reponse}
'''),
dict(id='2025-mets-4b', s='mets', ex=4, titre='Exercice 4 -- La piscine, question 3', theme='Fonction affine, image, proportionnalité',
     consigne='Traite la question 3.', regions=[(3, 134, 284), (3, 326, 604)], s3=17, n3=[13, 26], s4=None, n4=None,
     corr=r'''
\q{3.a}{Le temps de filtration est-il proportionnel à la température ?}
\begin{reponse}
Non : la représentation graphique de $f$ est une droite qui ne passe pas par l'origine du repère ($f(0) = 2$).
$f(x) = 0{,}5x + 2$ est une fonction affine, mais pas linéaire.
\end{reponse}
\q{3.b}{Image de 10 par la fonction $f$.}
\begin{reponse}
$f(10) = 0{,}5 \times 10 + 2 = 7$ : l'image de 10 est \textbf{7} (on le lit aussi sur le graphique).
\end{reponse}
'''),
dict(id='2025-mets-4c', s='mets', ex=4, titre='Exercice 4 -- La piscine, question 4', theme='Équation',
     consigne='Traite la question 4 (le temps de filtration est 0,5x + 2 pour une eau à x °C).', regions=[(3, 134, 284), (3, 604, 618)], s3=7, n3=[], s4=16, n4=[38],
     corr=r'''
\q{4}{Résoudre $0{,}5x + 2 = 17$ et interpréter.}
\begin{reponse}
\[ 0{,}5x + 2 = 17 \iff 0{,}5x = 15 \iff x = \frac{15}{0{,}5} = 30. \]
La solution est 30 : il faut filtrer l'eau 17 heures par jour quand elle est à 30 °C.
\end{reponse}
'''),
dict(id='2025-mets-4d', s='mets', ex=4, titre='Exercice 4 -- La piscine, question 5', theme='Grandeurs composées (kWh)',
     consigne='Traite la question 5.', regions=[(3, 134, 284), (3, 618, 778)], s3=14, n3=[23], s4=15, n4=[36],
     corr=r'''
\q{5}{Dépense liée à la filtration du 1\textsuperscript{er} juillet au 31 août.}
\begin{reponse}
Nombre de jours : juillet (31 jours) et août (31 jours), soit $31 + 31 = 62$ jours.\\
Consommation (document 3) : $0{,}8 \times 16 \times 62 = 793{,}6$ kWh.\\
Dépense (document 2) : $793{,}6 \times 0{,}23 = 182{,}528$ €, soit environ \textbf{182,53 €}.
\end{reponse}
'''),
dict(id='2025-mets-5a', s='mets', ex=5, titre='Exercice 5 -- La table, questions 1 et 2', theme='Aires, pourcentages',
     consigne='Traite les questions 1 et 2.', regions=[(4, 134, 399)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{1}{Aire du dessus de la table.}
\begin{reponse}
La table est un carré de côté 80 cm : $\mathcal{A} = 80 \times 80 = 6\,400 \text{ cm}^2$.
\end{reponse}
\q{2}{La plaque en verre représente-t-elle 25 \% de l'aire totale ?}
\begin{reponse}
Le côté de la plaque en verre est $60 - 20 = 40$ cm (ou $80 - 2 \times 20$), donc son aire est $40 \times 40 = 1\,600 \text{ cm}^2$.
\[ \frac{1\,600}{6\,400} = \frac{1}{4} = 0{,}25 = 25\ \%. \]
\end{reponse}
'''),
dict(id='2025-mets-5b', s='mets', ex=5, titre='Exercice 5 -- La table, question 3', theme='Rotation',
     consigne='Traite la question 3.', regions=[(4, 134, 368), (4, 399, 430)], s3=11, n3=[17], s4=None, n4=None,
     corr=r'''
\q{3}{Transformation qui permet de passer du rectangle n\textsuperscript{o}~1 au rectangle n\textsuperscript{o}~2.}
\begin{reponse}
Une \textbf{rotation} de centre le centre de la table et d'angle $90^\circ$ (un quart de tour).
\end{reponse}
'''),
dict(id='2025-mets-5c', s='mets', ex=5, titre='Exercice 5 -- La table, question 4 (Scratch)', theme='Algorithmique (Scratch)',
     consigne='Traite la question 4 (la table est un carré de 80 cm de côté, les plaques en bois mesurent 60 cm sur 20 cm).',
     regions=[(4, 134, 368), (4, 428, 792), (5, 128, 500)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{4.a}{Compléter les lignes 3, 5 et 6 du bloc Rectangle.}
\begin{reponse}
\texttt{3\quad répéter \fbox{2} fois}\\
\texttt{5\quad tourner de \fbox{90} degrés}\\
\texttt{6\quad avancer de \fbox{20} pas}\\
On trace deux fois « une longueur (60), un quart de tour, une largeur (20), un quart de tour ».
\end{reponse}
\q{4.b}{Quel programme trace la vue du dessus de la table ?}
\begin{reponse}
Après le bloc Rectangle, le lutin est revenu à son point de départ, dans la même direction. Pour tracer le rectangle suivant, il doit aller au coin suivant de la table, situé à 80 pas (le côté de la table), puis tourner d'un quart de tour.\\
C'est le \textbf{programme C}. (Le programme A trace les quatre rectangles à partir du même coin ; le programme B n'avance que de 60 pas.)
\end{reponse}
'''),
]
