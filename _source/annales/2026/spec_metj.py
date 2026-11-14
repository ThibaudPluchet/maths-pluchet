# DNB Métropole, 30 juin 2026
SOURCE = ('dnb_metropole_juin_2026.pdf', 'Métropole, 30 juin 2026')
QA = (1, 205, 280)
def q(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2026-metj-a{n}', s='metj', ex=0, titre=f'Automatismes, question {n}', theme=theme,
                regions=[QA] + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
q(1, [(1, 288, 341)], 5, [], 12, [], 'Écriture fractionnaire', r'''
\q{1}{Écrire 0,75 sous la forme d'une fraction.}
\begin{reponse}
$0{,}75 = \dfrac{75}{100} = \mathbf{\dfrac34}$.
\end{reponse}
'''),
q(2, [(1, 341, 391)], 1, [], 1, [1], 'Nombres relatifs', r'''
\q{2}{Calculer $-4{,}7 + 3{,}5$.}
\begin{reponse}
Les deux nombres sont de signes contraires : on soustrait les distances à zéro, $4{,}7 - 3{,}5 = 1{,}2$, et on garde le signe de $-4{,}7$. Résultat : $\mathbf{-1{,}2}$.
\end{reponse}
'''),
q(3, [(1, 391, 462)], 14, [], 5, [11], 'Quatrième proportionnelle', r'''
\q{3}{Valeur de $a$ dans le tableau de proportionnalité.}
\begin{reponse}
12 est le double de 6, donc $a$ est le double de 18 : $a = \mathbf{36}$ \quad (ou $a = \dfrac{12 \times 18}{6} = 36$).
\end{reponse}
'''),
q(4, [(1, 462, 581)], 22, [], 20, [47], 'Probabilités', r'''
\q{4}{Probabilité d'obtenir une boule bleue.}
\begin{reponse}
$10 + 4 + 6 = 20$ boules dont 4 bleues : $p = \dfrac{4}{20}$, \textbf{réponse B}.
\end{reponse}
'''),
q(5, [(1, 581, 653)], 7, [], 16, [38], 'Équation du premier degré', r'''
\q{5}{Solution de $10x + 16 = -64$.}
\begin{reponse}
$10x = -64 - 16 = -80$, donc $x = -80 \div 10 = \mathbf{-8}$ : \textbf{réponse C}.
\end{reponse}
'''),
q(6, [(1, 653, 712)], 25, [], 13, [31], 'Notation scientifique', r'''
\q{6}{Notation scientifique de 0,004 58.}
\begin{reponse}
$\mathbf{4{,}58 \times 10^{-3}}$ (un seul chiffre non nul avant la virgule) : \textbf{réponse C}.
\end{reponse}
'''),
q(7, [(2, 128, 314)], 23, [], 11, [23], 'Diagramme circulaire', r'''
\q{7}{Nombre d'élèves ayant choisi la réponse B.}
\begin{reponse}
Le secteur B est un angle droit, soit un quart du disque : $24 \div 4 = \mathbf{6}$ élèves.
\end{reponse}
'''),
q(8, [(2, 314, 435)], 21, [], 17, [], 'Périmètre', r'''
\q{8}{Périmètre du rectangle.}
\begin{reponse}
$2 \times 10 + 2 \times 5 = \mathbf{30}$ mm (un périmètre est une longueur) : \textbf{réponse A}.
\end{reponse}
'''),
q(9, [(2, 435, 632)], 4, [6], None, None, 'Cosinus', r'''
\q{9}{Cosinus de l'angle $\widehat{EDF}$.}
\begin{reponse}
Le triangle est rectangle en $E$ : pour l'angle en $D$, le côté adjacent est $[DE]$ (6 cm) et l'hypoténuse $[DF]$ (10 cm). $\cos\widehat{EDF} = \dfrac{6}{10} = \dfrac35$ : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2026-metj-1', s='metj', ex=1, titre='Exercice 1 -- Les Jeux paralympiques', theme='Tableau, pourcentages, médiane',
     regions=[(3, 132, 608)], s3=23, n3=[], s4=15, n4=[24, 34],
     corr=r'''
\q{1}{Médailles d'or des Pays-Bas.}
\begin{reponse}
\textbf{27}.
\end{reponse}
\q{2}{Médailles d'or de l'Australie.}
\begin{reponse}
$63 - 17 - 28 = \mathbf{18}$.
\end{reponse}
\q{3}{Plus de 20 \% des médailles britanniques en bronze ?}
\begin{reponse}
$\dfrac{31}{124} = 0{,}25 = 25$ \%, et $25 > 20$ : l'affirmation est vraie.
\end{reponse}
\q{4.a}{Médiane des totaux.}
\begin{reponse}
Dans l'ordre : 56 ; 63 ; 71 ; 75 ; \textbf{82} ; 89 ; 105 ; 124 ; 220. Il y a 9 valeurs : la médiane est la $5^{\text{e}}$, \textbf{82}.
\end{reponse}
\q{4.b}{Interprétation.}
\begin{reponse}
Au moins la moitié de ces pays ont obtenu 82 médailles ou moins, et au moins la moitié 82 médailles ou plus.
\end{reponse}
\q{5}{Pourcentage d'augmentation des médailles d'argent du Brésil.}
\begin{reponse}
Hausse : $26 - 20 = 6$. \quad $\dfrac{6}{20} = 0{,}3$ : une augmentation de \textbf{30 \%}.
\end{reponse}
'''),
dict(id='2026-metj-2a', s='metj', ex=2, titre='Exercice 2 -- Les deux triangles, questions 1 et 2', theme='Réciproque de Pythagore, théorème de Thalès',
     consigne='Traite les questions 1 et 2.', regions=[(4, 130, 552)], s3=13, n3=[], s4=19, n4=[22, 32],
     corr=r'''
\q{1}{Montrer que ABC est rectangle en A.}
\begin{reponse}
Le plus grand côté est $[BC]$. \quad $BC^2 = 8^2 = 64$ \quad et \quad $AB^2 + AC^2 = 6{,}4^2 + 4{,}8^2 = 40{,}96 + 23{,}04 = 64$.\\
$BC^2 = AB^2 + AC^2$ : d'après la réciproque du théorème de Pythagore, $ABC$ est rectangle en $A$.
\end{reponse}
\q{2}{Montrer que DE = 6 cm et AE = 3,6 cm.}
\begin{reponse}
Les droites $(BD)$ et $(CE)$ sont sécantes en $A$ et $(BC) \parallel (DE)$. D'après le théorème de Thalès :
\[ \frac{AD}{AB} = \frac{AE}{AC} = \frac{DE}{BC} \qquad\text{soit}\qquad \frac{4{,}8}{6{,}4} = \frac{AE}{4{,}8} = \frac{DE}{8}. \]
$DE = \dfrac{4{,}8 \times 8}{6{,}4} = 6$ cm \quad et \quad $AE = \dfrac{4{,}8 \times 4{,}8}{6{,}4} = 3{,}6$ cm.
\end{reponse}
'''),
dict(id='2026-metj-2b', s='metj', ex=2, titre='Exercice 2 -- Les deux triangles, questions 3 à 5', theme='Angles alternes-internes, triangles semblables, aire',
     consigne='Traite les questions 3 à 5 (ABC est rectangle en A ; DE = 6 cm ; AE = 3,6 cm).', regions=[(4, 130, 520), (4, 552, 622)], s3=10, n3=[16], s4=None, n4=None,
     corr=r'''
\q{3}{Montrer que $\widehat{ABC} = \widehat{ADE}$.}
\begin{reponse}
Les droites $(BC)$ et $(DE)$ sont parallèles et coupées par la sécante $(BD)$ : les angles $\widehat{ABC}$ et $\widehat{ADE}$ sont alternes-internes, donc égaux.
\end{reponse}
\q{4}{Montrer que ABC et ADE sont semblables.}
\begin{reponse}
$\widehat{ABC} = \widehat{ADE}$ et $\widehat{BAC} = \widehat{DAE}$ (angles opposés par le sommet, droits). Deux triangles qui ont deux angles égaux deux à deux sont semblables.
\end{reponse}
\q{5}{Aire du quadrilatère BCDE.}
\begin{reponse}
Ses diagonales $[BD]$ et $[CE]$ sont perpendiculaires en $A$ : le quadrilatère est formé de quatre triangles rectangles en $A$.
\[ \frac{6{,}4 \times 4{,}8}{2} + \frac{4{,}8 \times 4{,}8}{2} + \frac{4{,}8 \times 3{,}6}{2} + \frac{6{,}4 \times 3{,}6}{2} = 15{,}36 + 11{,}52 + 8{,}64 + 11{,}52 = \mathbf{47{,}04} \text{ cm}^2. \]
\end{reponse}
'''),
dict(id='2026-metj-3a', s='metj', ex=3, titre='Exercice 3 -- Le volume d’une boule, partie A', theme='Lecture graphique (image, antécédent)',
     consigne='Traite la partie A.', regions=[(5, 130, 423)], s3=8, n3=[13], s4=None, n4=None,
     corr=r'''
\q{1}{Image de 3,6.}
\begin{reponse}
On lit environ \textbf{200} cm³.
\end{reponse}
\q{2}{Rayon d'une boule de 660 cm³.}
\begin{reponse}
On lit environ \textbf{5,4} cm.
\end{reponse}
'''),
dict(id='2026-metj-3b', s='metj', ex=3, titre='Exercice 3 -- Le volume d’une boule, partie B', theme='Volume de la boule, masse volumique',
     consigne='Traite la partie B.', regions=[(5, 130, 183), (5, 423, 597)], s3=21, n3=[36], s4=None, n4=None,
     corr=r'''
\q{1}{Volume d'une boule de rayon 2,5 cm.}
\begin{reponse}
$V = \dfrac43 \times \pi \times 2{,}5^3 \approx 65{,}4$ cm³, soit \textbf{65} cm³ à l'unité.
\end{reponse}
\q{2}{Nombre de boules avec 1 000 cm³.}
\begin{reponse}
$1\,000 \div 65{,}4 \approx 15{,}3$ : au maximum \textbf{15 boules}.
\end{reponse}
\q{3}{Masse d'une boule.}
\begin{reponse}
$65{,}4 \times 0{,}9 \approx \mathbf{59}$ g (avec 65 cm³ : 58,5 g).
\end{reponse}
'''),
dict(id='2026-metj-4', s='metj', ex=4, titre='Exercice 4 -- Les sachets de bonbons', theme='Diviseurs, décomposition, répartition',
     regions=[(5, 595, 786)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{1}{Peut-on faire 16 sachets ?}
\begin{reponse}
$112 = 16 \times 7$, mais $140 \div 16 = 8{,}75$ n'est pas entier : \textbf{non}.
\end{reponse}
\q{2}{Décomposition de 140.}
\begin{reponse}
$140 = 2 \times 70 = 2 \times 2 \times 35 = \mathbf{2^2 \times 5 \times 7}$.
\end{reponse}
\q{3}{Nombre maximal de sachets et composition.}
\begin{reponse}
$112 = 2^4 \times 7$ et $140 = 2^2 \times 5 \times 7$ : facteurs communs $2^2 \times 7 = \mathbf{28}$ sachets.\\
Chacun contient $112 \div 28 = 4$ bonbons à la fraise et $140 \div 28 = 5$ au caramel.
\end{reponse}
'''),
]
