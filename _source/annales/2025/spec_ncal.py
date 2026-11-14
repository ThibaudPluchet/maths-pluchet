# DNB Nouvelle-Calédonie, décembre 2025
QCM = (1, 194, 310)
PARTS = [
dict(id='2025-ncal-1q1', s='ncal', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Nombres premiers',
     regions=[QCM, (1, 310, 337)], s3=24, n3=[], s4=6, n4=[14],
     corr=r'''
\q{1}{Lequel de ces nombres est premier : 719, 935 ou 687 ?}
\begin{reponse}
935 se termine par 5 : il est divisible par 5. \quad $6 + 8 + 7 = 21$ : 687 est divisible par 3.\\
719 n'est divisible par aucun des nombres premiers 2, 3, 5, 7, 11, 13, 17, 19, 23 (et $29^2 = 841 > 719$) : il est premier. \textbf{Réponse A.}
\end{reponse}
'''),
dict(id='2025-ncal-1q2', s='ncal', ex=1, titre='Exercice 1 -- QCM, question 2', theme='Aire d’une figure',
     regions=[QCM, (1, 336, 506)], s3=21, n3=[], s4=17, n4=[],
     corr=r'''
\q{2}{Aire de la figure.}
\begin{reponse}
On complète la figure en un rectangle de $7 \times 5 = 35 \text{ cm}^2$, auquel on retire le rectangle manquant de $5 \times 2 = 10 \text{ cm}^2$ :
$35 - 10 = 25 \text{ cm}^2$. \textbf{Réponse C.}
\end{reponse}
'''),
dict(id='2025-ncal-1q3', s='ncal', ex=1, titre='Exercice 1 -- QCM, question 3', theme='Fonction affine',
     regions=[QCM, (1, 506, 545)], s3=17, n3=[26], s4=None, n4=None,
     corr=r'''
\q{3}{Laquelle de ces fonctions est affine ?}
\begin{reponse}
$f(x) = 3(x + 1) = 3x + 3$ est de la forme $ax + b$ : elle est affine. ($g$ contient $\frac{5}{x}$ et $h$ contient $x^2$.) \textbf{Réponse A.}
\end{reponse}
'''),
dict(id='2025-ncal-1q4', s='ncal', ex=1, titre='Exercice 1 -- QCM, question 4', theme='Vitesse moyenne',
     regions=[QCM, (1, 545, 637)], s3=14, n3=[], s4=15, n4=[35],
     corr=r'''
\q{4}{Vitesse moyenne de l'avion (6 980 km en 9 h), à la centaine de km/h.}
\begin{reponse}
$v = \dfrac{6\,980}{9} \approx 776$ km/h, soit environ \textbf{800 km/h} à la centaine près. \textbf{Réponse B.}
\end{reponse}
'''),
dict(id='2025-ncal-1q5', s='ncal', ex=1, titre='Exercice 1 -- QCM, question 5', theme='Pourcentages',
     regions=[QCM, (1, 637, 700)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{5}{Nombre de filles : 60 \% de 730 élèves.}
\begin{reponse}
$730 \times \dfrac{60}{100} = 730 \times 0{,}6 = 438$. \textbf{Réponse A.}
\end{reponse}
'''),
dict(id='2025-ncal-2a', s='ncal', ex=2, titre='Exercice 2 -- Le cerf-volant, question 1', theme='Trigonométrie (calcul de longueur)',
     consigne='Traite la question 1.', regions=[(2, 135, 410)], s3=15, n3=[24], s4=None, n4=None,
     corr=r'''
\q{1}{Calculer BE, arrondie au millimètre.}
\begin{reponse}
$E$ est le milieu de $[CD]$ ($ED = EC$), donc $ED = 40 \div 2 = 20$ cm.\\
Dans le triangle $BED$ rectangle en $E$, $[ED]$ est le côté opposé à l'angle $\widehat{EBD}$ et $[BE]$ le côté adjacent :
\[ \tan\widehat{EBD} = \frac{ED}{BE} \qquad\text{donc}\qquad BE = \frac{ED}{\tan 30^\circ} = \frac{20}{\tan 30^\circ} \approx 34{,}64 \text{ cm}. \]
$BE \approx 34{,}6$ cm, soit 346 mm au millimètre près.
\end{reponse}
'''),
dict(id='2025-ncal-2b', s='ncal', ex=2, titre='Exercice 2 -- Le cerf-volant, question 2', theme='Théorème de Pythagore',
     consigne='Traite la question 2.', regions=[(2, 135, 173), (2, 411, 642)], s3=2, n3=[], s4=4, n4=[10],
     corr=r'''
\q{2}{Altitude HT du cerf-volant, arrondie au mètre.}
\begin{reponse}
Le triangle $SHT$ est rectangle en $T$ ($H$ est à la verticale de $T$), d'hypoténuse $[SH]$ (la corde, 20,50 m). D'après le théorème de Pythagore :
\begin{align*}
SH^2 &= ST^2 + HT^2\\
HT^2 &= 20{,}5^2 - 7{,}6^2 = 420{,}25 - 57{,}76 = 362{,}49\\
HT &= \sqrt{362{,}49} \approx 19{,}04 \text{ m}
\end{align*}
Le cerf-volant vole à environ \textbf{19 m} d'altitude.
\end{reponse}
'''),
dict(id='2025-ncal-2c', s='ncal', ex=2, titre='Exercice 2 -- Le cerf-volant, question 3', theme='Conversions de vitesse',
     consigne='Traite la question 3.', regions=[(2, 135, 173), (2, 642, 730)], s3=14, n3=[23], s4=15, n4=[36],
     corr=r'''
\q{3}{Avec un vent de 15 nœuds au plus, le cerf-volant peut-il voler sans risque (limite : 20 km/h) ?}
\begin{reponse}
$15 \text{ nœuds} = 15 \times 0{,}514 = 7{,}71$ m/s.\\
En 1 h $= 3\,600$ s : $7{,}71 \times 3\,600 = 27\,756$ m $\approx 27{,}8$ km, soit environ 27,8 km/h.\\
$27{,}8 > 20$ : le vent peut dépasser 20 km/h, Thomas \textbf{ne peut pas} faire voler son cerf-volant sans risque.
\end{reponse}
'''),
dict(id='2025-ncal-3a', s='ncal', ex=3, titre='Exercice 3 -- Programmes de calcul, question 1', theme='Programmes de calcul',
     consigne='Traite la question 1.', regions=[(2, 728, 790), (3, 128, 289)], s3=1, n3=[], s4=8, n4=[19],
     corr=r'''
\q{1.a}{Avec 2, on obtient 18 avec le programme A.}
\begin{reponse}
$2 + 4 = 6$ puis $6 \times 3 = 18$.
\end{reponse}
\q{1.b}{Avec 2, on obtient 5 avec le programme B.}
\begin{reponse}
$2 \times 5 = 10$ ; $10 - 3 = 7$ ; $7 - 2 = 5$.
\end{reponse}
'''),
dict(id='2025-ncal-3b', s='ncal', ex=3, titre='Exercice 3 -- Programmes de calcul, questions 2 à 4', theme='Fonctions, antécédent, équations',
     consigne='Traite les questions 2 à 4.', regions=[(2, 728, 790), (3, 128, 240), (3, 289, 482)], s3=8, n3=[5, 14], s4=None, n4=None,
     corr=r'''
\q{2.a}{Justifier que $f(x) = 3x + 12$.}
\begin{reponse}
$x \longrightarrow x + 4 \longrightarrow (x + 4) \times 3 = 3x + 12$.
\end{reponse}
\q{2.b}{Antécédent de 27 par la fonction $f$.}
\begin{reponse}
Je résous $3x + 12 = 27$ : $3x = 15$, donc $x = 5$. L'antécédent de 27 est \textbf{5}.
\end{reponse}
\q{3.a}{Expression de $g(x)$.}
\begin{reponse}
$x \longrightarrow 5x \longrightarrow 5x - 3 \longrightarrow 5x - 3 - x = 4x - 3$. Donc $g(x) = 4x - 3$.
\end{reponse}
\q{3.b}{Nombre à choisir pour obtenir 2 avec le programme B.}
\begin{reponse}
$4x - 3 = 2 \iff 4x = 5 \iff x = \dfrac54 = 1{,}25$.
\end{reponse}
\q{4}{Quel nombre Hugo a-t-il choisi ?}
\begin{reponse}
Je cherche $x$ tel que $f(x) = g(x)$ : $3x + 12 = 4x - 3 \iff 12 + 3 = 4x - 3x \iff x = 15$.\\
Hugo a choisi \textbf{15} (les deux programmes donnent 57).
\end{reponse}
'''),
dict(id='2025-ncal-4', s='ncal', ex=4, titre='Exercice 4 -- Jeu de hasard', theme='Probabilités',
     regions=[(3, 480, 748)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{1}{Probabilité de tirer une bille bleue.}
\begin{reponse}
La boîte contient $15 + 10 + 5 = 30$ billes, dont 5 bleues : $p = \dfrac{5}{30} = \dfrac16$.
\end{reponse}
\q{2}{Amandine (bille verte) ou Alexis (bille rouge) : qui a le plus de chances de gagner ?}
\begin{reponse}
Amandine lance le dé vert (6 faces, de 1 à 6) : $p = \dfrac16$.\quad Alexis lance le dé rouge (10 faces, de 0 à 9) : $p = \dfrac{1}{10}$.\\
$\dfrac16 > \dfrac{1}{10}$ : c'est \textbf{Amandine} qui a le plus de chances de gagner.
\end{reponse}
\q{3}{Ensemble des issues possibles.}
\begin{reponse}
(R ; 0), (R ; 1), (R ; 2), (R ; 3), (R ; 4), (R ; 5), (R ; 6), (R ; 7), (R ; 8), (R ; 9),\\
(V ; 1), (V ; 2), (V ; 3), (V ; 4), (V ; 5), (V ; 6),\\
(B ; 1), (B ; 2), (B ; 3), (B ; 4) : soit 20 issues.
\end{reponse}
'''),
dict(id='2025-ncal-5', s='ncal', ex=5, titre='Exercice 5 -- Géométrie', theme='Parallélisme, Thalès, agrandissement',
     regions=[(4, 135, 436), (6, 170, 420)], s3=9, n3=[], s4=10, n4=[22, 41],
     corr=r'''
\q{1}{Prouver que les droites (BE) et (CD) sont parallèles.}
\begin{reponse}
Les angles $\widehat{BEA}$ et $\widehat{CDA}$ mesurent tous les deux $110^\circ$. Ils sont correspondants (formés par les droites $(BE)$ et $(CD)$ avec la sécante $(AD)$) et de même mesure : les droites $(BE)$ et $(CD)$ sont parallèles.
\end{reponse}
\q{2}{Calculer CD.}
\begin{reponse}
Les points $A$, $E$, $D$ et $A$, $B$, $C$ sont alignés, et $(BE) \parallel (CD)$. D'après le théorème de Thalès :
\[ \frac{AE}{AD} = \frac{AB}{AC} = \frac{BE}{CD} \qquad\text{soit}\qquad \frac{6}{15} = \frac{4}{CD} \qquad\text{donc}\qquad CD = \frac{4 \times 15}{6} = 10 \text{ cm}. \]
\end{reponse}
\q{3}{Aire du triangle ACD, sachant que l'aire de ABE est environ 11,3 cm².}
\begin{reponse}
Le triangle $ACD$ est un agrandissement du triangle $ABE$ de rapport $k = \dfrac{AD}{AE} = \dfrac{15}{6} = 2{,}5$.\\
Les aires sont multipliées par $k^2 = 2{,}5^2 = 6{,}25$ : $\mathcal{A}_{ACD} \approx 11{,}3 \times 6{,}25 \approx 70{,}6 \text{ cm}^2$.
\end{reponse}
\q{4}{Construire la figure en vraie grandeur.}
\begin{reponse}
Tracer $[AD]$ de 15 cm et placer $E$ à 6 cm de $A$. En $E$ puis en $D$, construire au rapporteur un angle de $110^\circ$ (du même côté) ; placer $B$ sur la demi-droite issue de $E$ à 4 cm de $E$. La droite $(AB)$ coupe la demi-droite issue de $D$ en $C$ (on doit trouver $CD = 10$ cm).
\end{reponse}
'''),
dict(id='2025-ncal-6', s='ncal', ex=6, titre='Exercice 6 -- Scratch', theme='Algorithmique (Scratch)',
     regions=[(4, 434, 790), (5, 128, 392), (6, 418, 640)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Associer chaque script à sa figure.}
\begin{reponse}
Le lutin trace 3 segments de 100 pas en tournant de 60°, 90° ou 120°.\\
\textbf{Script 1 $\to$ figure C}\qquad \textbf{Script 2 $\to$ figure A}\qquad \textbf{Script 3 $\to$ figure B} (avec 120°, il trace un triangle équilatéral fermé).
\end{reponse}
\q{2}{Compléter le script qui trace la figure E.}
\begin{reponse}
\texttt{mettre \fbox{longueur} à \fbox{20}}\\
\texttt{stylo en position d'écriture}\\
\texttt{répéter \fbox{12} fois}\\
\texttt{\quad avancer de \fbox{longueur} pas}\\
\texttt{\quad tourner de 90 degrés}\\
\texttt{\quad ajouter \fbox{20} à \fbox{longueur}}\\
La longueur de chaque segment augmente de 20 pas à chaque tour (20, 40, 60, \ldots) : la spirale de la figure E compte 12 segments.
\end{reponse}
'''),
]
