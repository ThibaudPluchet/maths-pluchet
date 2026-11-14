# DNB Antilles-Guyane, 30 juin 2026
SOURCE = ('dnb_antilles_juin_2026.pdf', 'Antilles-Guyane, 30 juin 2026')
QA = (1, 205, 288)
def q(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2026-antj-a{n}', s='antj', ex=0, titre=f'Automatismes, question {n}', theme=theme,
                regions=[QA] + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
q(1, [(1, 288, 456)], 8, [], 9, [], 'Repérage dans le plan', r'''
\q{1}{Coordonnées du point A.}
\begin{reponse}
$A\,(\mathbf{-2\,;\,2})$.
\end{reponse}
'''),
q(2, [(1, 456, 624)], 11, [], 7, [], 'Symétrie centrale', r'''
\q{2}{Symétrique de K par la symétrie de centre O.}
\begin{reponse}
$O$ doit être le milieu du segment qui joint $K$ à son image : c'est le point \textbf{M}.
\end{reponse}
'''),
q(3, [(1, 624, 772)], 2, [], 4, [], 'Aire d’un triangle', r'''
\q{3}{Calcul de l'aire du triangle ABC.}
\begin{reponse}
$[BD]$ est la hauteur relative à la base $[AC]$ : $\mathcal{A} = \dfrac{AC \times BD}{2}$, \textbf{réponse B}.
\end{reponse}
'''),
q(4, [(2, 128, 237)], 22, [], 20, [48], 'Fréquence', r'''
\q{4}{Fréquence de « pile ».}
\begin{reponse}
« Pile » sort 4 fois sur 10 : $\dfrac{4}{10}$, \textbf{réponse C}.
\end{reponse}
'''),
q(5, [(2, 237, 323)], 1, [], 8, [20], 'Expression littérale', r'''
\q{5}{La moitié de $n$.}
\begin{reponse}
$\dfrac{n}{2}$, \textbf{réponse D}.
\end{reponse}
'''),
q(6, [(2, 323, 398)], 14, [], 15, [36], 'Durées', r'''
\q{6}{$\frac{1}{10}$ d'heure en minutes.}
\begin{reponse}
$60 \div 10 = \mathbf{6}$ min, \textbf{réponse C}.
\end{reponse}
'''),
q(7, [(2, 398, 456)], 23, [], 11, [24], 'Moyenne', r'''
\q{7}{Moyenne de 10 ; 10 ; 12 ; 16.}
\begin{reponse}
$\dfrac{10 + 10 + 12 + 16}{4} = \dfrac{48}{4} = \mathbf{12}$.
\end{reponse}
'''),
q(8, [(2, 456, 579)], 2, [], 4, [], 'Angles d’un triangle isocèle', r'''
\q{8}{Valeur de $x$.}
\begin{reponse}
Le triangle est isocèle (codage) : ses deux angles à la base sont égaux et valent ensemble $180^\circ - 120^\circ = 60^\circ$. Donc $x = \mathbf{30^\circ}$.
\end{reponse}
'''),
q(9, [(2, 579, 632)], 14, [], 15, [35], 'Vitesse, durée', r'''
\q{9}{Durée d'un trajet de 15 km à 20 km/h.}
\begin{reponse}
20 km en 60 min, donc 5 km en 15 min et 15 km en \textbf{45 min}.
\end{reponse}
'''),
dict(id='2026-antj-1a', s='antj', ex=1, titre='Exercice 1 -- Les triangles, questions 1 et 2', theme='Longueurs, théorème de Pythagore',
     consigne='Traite les questions 1 et 2.', regions=[(3, 160, 466)], s3=2, n3=[], s4=4, n4=[10],
     corr=r'''
\q{1}{Justifier que AM = 5,5 m.}
\begin{reponse}
$A$ est sur le segment $[TM]$ : $AM = TM - AT = 7{,}7 - 2{,}2 = 5{,}5$ m.
\end{reponse}
\q{2}{Montrer que AB = 4,8 m.}
\begin{reponse}
Le triangle $ABM$ est rectangle en $A$, d'hypoténuse $[MB]$. D'après le théorème de Pythagore :
\[ AB^2 = MB^2 - AM^2 = 7{,}3^2 - 5{,}5^2 = 53{,}29 - 30{,}25 = 23{,}04 \qquad\text{donc}\qquad AB = \sqrt{23{,}04} = 4{,}8 \text{ m}. \]
\end{reponse}
'''),
dict(id='2026-antj-1b', s='antj', ex=1, titre='Exercice 1 -- Les triangles, questions 3 à 5', theme='Trigonométrie, réciproque de Thalès, homothétie',
     consigne='Traite les questions 3 à 5 (AM = 5,5 m et AB = 4,8 m).', regions=[(3, 160, 433), (3, 466, 602)], s3=18, n3=[6, 30], s4=None, n4=None,
     corr=r'''
\q{3}{Mesure de l'angle $\widehat{ABM}$.}
\begin{reponse}
Dans le triangle $ABM$ rectangle en $A$, $[AM]$ est le côté opposé à $\widehat{ABM}$ et $[AB]$ le côté adjacent :
\[ \tan\widehat{ABM} = \frac{AM}{AB} = \frac{5{,}5}{4{,}8} \qquad\text{donc}\qquad \widehat{ABM} \approx \mathbf{49^\circ}. \]
\end{reponse}
\q{4}{Montrer que (TE) et (BM) sont parallèles.}
\begin{reponse}
Les points $T$, $A$, $M$ et $E$, $A$, $B$ sont alignés dans le même ordre.
\[ \frac{AT}{AM} = \frac{2{,}2}{5{,}5} = 0{,}4 \qquad\text{et}\qquad \frac{AE}{AB} = \frac{1{,}92}{4{,}8} = 0{,}4. \]
Les rapports sont égaux : d'après la réciproque du théorème de Thalès, $(TE) \parallel (BM)$.
\end{reponse}
\q{5}{Rapport de l'homothétie de centre A qui transforme AET en ABM.}
\begin{reponse}
$\dfrac{AB}{AE} = \dfrac{4{,}8}{1{,}92} = 2{,}5$, et $B$ est de l'autre côté de $A$ par rapport à $E$ : le rapport est $\mathbf{-2{,}5}$ (proposition 3).
\end{reponse}
'''),
dict(id='2026-antj-1rec', s='antj', ex=1, titre='Exercice 1 -- Les triangles, question 4', theme='Réciproque du théorème de Thalès', extra=True,
     consigne='Traite seulement la question 4 (AM = 5,5 m et AB = 4,8 m).', regions=[(3, 160, 433), (3, 485, 518)], s3=20, n3=[], s4=19, n4=[45],
     corr=r'''
\q{4}{Montrer que (TE) et (BM) sont parallèles.}
\begin{reponse}
Les points $T$, $A$, $M$ et $E$, $A$, $B$ sont alignés dans le même ordre.
\[ \frac{AT}{AM} = \frac{2{,}2}{5{,}5} = 0{,}4 \qquad\text{et}\qquad \frac{AE}{AB} = \frac{1{,}92}{4{,}8} = 0{,}4. \]
Les rapports sont égaux : d'après la réciproque du théorème de Thalès, $(TE) \parallel (BM)$.
\end{reponse}
'''),
dict(id='2026-antj-2', s='antj', ex=2, titre='Exercice 2 -- Deux programmes de calcul', theme='Programme de calcul, expression littérale, équation, Scratch',
     regions=[(4, 130, 668)], s3=7, n3=[], s4=16, n4=[6, 19, 38],
     corr=r'''
\q{1}{Avec 1 au départ.}
\begin{reponse}
$1 - 2 = -1$ ; $-1 \times 5 = -5$ ; $-5 + 3 \times 1 = -2$.
\end{reponse}
\q{2.a}{Résultat en fonction de $x$.}
\begin{reponse}
$(x - 2) \times 5 + 3x = 5x - 10 + 3x = 8x - 10$.
\end{reponse}
\q{2.b}{Nombre de départ pour obtenir 0.}
\begin{reponse}
$8x - 10 = 0 \iff 8x = 10 \iff x = \mathbf{1{,}25}$.
\end{reponse}
\q{3.a}{Programme B avec 1.}
\begin{reponse}
$4 \times 1 = 4$ ; $4 - 5 = -1$ ; $2 \times (-1) = \mathbf{-2}$.
\end{reponse}
\q{3.b}{Les programmes A et B donnent toujours le même résultat.}
\begin{reponse}
Programme B : $x \longrightarrow 4x \longrightarrow 4x - 5 \longrightarrow 2(4x - 5) = 8x - 10$. C'est le résultat du programme A, quel que soit $x$.
\end{reponse}
'''),
dict(id='2026-antj-3', s='antj', ex=3, titre='Exercice 3 -- Le centre de loisirs', theme='Fonctions linéaires et affines, tableur',
     regions=[(5, 130, 770), (6, 128, 346)], s3=17, n3=[26], s4=None, n4=None,
     corr=r'''
\q{1}{Prix de 12 demi-journées au tarif B.}
\begin{reponse}
$15 + 12 \times 3{,}50 = 15 + 42 = \mathbf{57}$ €.
\end{reponse}
\q{2}{Associer fonctions et tarifs.}
\begin{reponse}
$f$ : tarif \textbf{B} ; $g$ : tarif \textbf{C} ; $h$ : tarif \textbf{A}.
\end{reponse}
\q{3}{Associer les droites aux fonctions.}
\begin{reponse}
$(d_2)$ est horizontale : $g$. $(d_3)$ passe par l'origine : $h$. $(d_1)$ coupe l'axe des ordonnées en 15 : $f$.
\end{reponse}
\q{4}{$(d_1)$ représente-t-elle une situation de proportionnalité ?}
\begin{reponse}
\textbf{Non} : c'est une droite qui ne passe pas par l'origine (pour 0 demi-journée, on paie 15 €).
\end{reponse}
\q{5}{À partir de combien de demi-journées B est-il plus avantageux que A ?}
\begin{reponse}
Les droites $(d_1)$ et $(d_3)$ se coupent pour 7,5 demi-journées : à partir de \textbf{8 demi-journées}.
\end{reponse}
\q{6.a}{Formule saisie en B2.}
\begin{reponse}
\texttt{=15+3,5*B1}.
\end{reponse}
\q{6.b}{À partir de combien de demi-journées C est-il plus avantageux que B ?}
\begin{reponse}
Le tarif B vaut 64 € pour 14 demi-journées, puis dépasse 64 € : le tarif C devient plus avantageux à partir de \textbf{15 demi-journées}.
\end{reponse}
'''),
]
