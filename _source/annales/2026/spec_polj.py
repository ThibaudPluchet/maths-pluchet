# DNB Polynésie, 26 juin 2026
SOURCE = ('dnb_polynesie_juin_2026.pdf', 'Polynésie, 26 juin 2026')
QA = (1, 208, 290)
def q(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2026-polj-a{n}', s='polj', ex=0, titre=f'Automatismes, question {n}', theme=theme,
                regions=[QA] + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
q(1, [(1, 290, 341)], 23, [], 11, [24], 'Médiane', r'''
\q{1}{Médiane de la série.}
\begin{reponse}
Dans l'ordre croissant : 7 ; 7 ; 9 ; 9 ; 12 ; 23 ; 25. Il y a 7 valeurs : la médiane est la 4\ieme{}, \textbf{9}.
\end{reponse}
'''),
q(2, [(1, 341, 384)], 25, [], 13, [31], 'Écriture scientifique', r'''
\q{2}{Notation scientifique de 0,000\,457.}
\begin{reponse}
$0{,}000\,457 = \mathbf{4{,}57 \times 10^{-4}}$.
\end{reponse}
'''),
q(3, [(1, 381, 494)], 2, [], 4, [], 'Aire d’un triangle rectangle', r'''
\q{3}{Aire du triangle.}
\begin{reponse}
Le triangle est rectangle en $B$ : $\mathcal{A} = \dfrac{AB \times BC}{2} = \dfrac{8 \times 6}{2} = \mathbf{24}$ cm$^2$.
\end{reponse}
'''),
q(4, [(1, 494, 619)], 22, [], 20, [47], 'Probabilités', r'''
\q{4}{Probabilité de piocher un beignet à la framboise.}
\begin{reponse}
$6 + 5 + 4 = 15$ beignets dont 4 à la framboise : $p = \mathbf{\dfrac{4}{15}}$.
\end{reponse}
'''),
q(5, [(1, 619, 688)], 14, [], 15, [34], 'Pourcentage de baisse', r'''
\q{5}{Prix de 800 € après une baisse de 10 \%.}
\begin{reponse}
$800 \times 0{,}9 = \mathbf{720}$ €.
\end{reponse}
'''),
q(6, [(1, 688, 744)], 1, [], 3, [6, 8], 'Développer et réduire', r'''
\q{6}{Développer et réduire $B = 4y(3y - 1)$.}
\begin{reponse}
$B = 4y \times 3y - 4y \times 1 = \mathbf{12y^2 - 4y}$.
\end{reponse}
'''),
q(7, [(1, 744, 790)], 21, [], 15, [36], 'Conversion de volumes', r'''
\q{7}{$3{,}57$ L $= \ldots$ cm$^3$.}
\begin{reponse}
1 L $=$ 1 dm$^3$ $=$ 1\,000 cm$^3$, donc $3{,}57$ L $= \mathbf{3\,570}$ cm$^3$.
\end{reponse}
'''),
q(8, [(2, 128, 200)], 3, [5], None, None, 'Fonction : calculer une image', r'''
\q{8}{Image de 4 par $f(x) = 3x - 5$.}
\begin{reponse}
Je remplace $x$ par 4 : $f(4) = 3 \times 4 - 5 = 12 - 5 = \mathbf{7}$, \textbf{réponse B}.
\end{reponse}
'''),
q(9, [(2, 199, 354)], 11, [], 7, [], 'Quadrilatères', r'''
\q{9}{Nature du quadrilatère ABCD.}
\begin{reponse}
D'après les codages, les diagonales se coupent en leur milieu ; rien n'indique qu'elles sont perpendiculaires ou de même longueur. C'est \textbf{un parallélogramme}, \textbf{réponse D}.
\end{reponse}
'''),
dict(id='2026-polj-1a', s='polj', ex=1, titre='Exercice 1 -- Périmètres, partie A', theme='Expression littérale, périmètre',
     consigne='Traite la partie A.', regions=[(3, 165, 450)], s3=1, n3=[], s4=8, n4=[18, 20],
     corr=r'''
\q{1}{Longueur AB et périmètre pour $x = 10$.}
\begin{reponse}
$AB = 3 \times 10 + 1 = \mathbf{31}$ et $AD = 10 - 2 = 8$.
Périmètre : $2 \times (31 + 8) = 2 \times 39 = \mathbf{78}$.
\end{reponse}
\q{2}{Périmètre en fonction de $x$.}
\begin{reponse}
$P = 2 \times (3x + 1) + 2 \times (x - 2) = 6x + 2 + 2x - 4 = \mathbf{8x - 2}$.
\end{reponse}
'''),
dict(id='2026-polj-1b', s='polj', ex=1, titre='Exercice 1 -- Périmètres, partie B, question 1', theme='Algorithmique (Scratch)',
     consigne='Traite seulement la question 1 de la partie B.', regions=[(3, 165, 365), (3, 448, 762), (4, 125, 170)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Que renvoie le programme pour 7 ?}
\begin{reponse}
Périmètre ABCD : $8 \times 7 - 2 = 54$ ; périmètre IJK : $6 \times 7 + 9 = 51$. Comme $54 \neq 51$, le lutin dit \textbf{« Les deux périmètres ne sont pas égaux »}.
\end{reponse}
'''),
dict(id='2026-polj-1c', s='polj', ex=1, titre='Exercice 1 -- Périmètres, partie B, questions 2 et 3', theme='Tableur, équation',
     consigne='Traite les questions 2 et 3 de la partie B.', regions=[(3, 448, 518), (4, 170, 697)], s3=7, n3=[], s4=16, n4=[19, 38],
     corr=r'''
\q{2.a}{Formule saisie en B2.}
\begin{reponse}
\texttt{= 8 * A2 - 2}.
\end{reponse}
\q{2.b}{Expliquer le raisonnement de Nour.}
\begin{reponse}
Pour $x = 5$, le périmètre du rectangle (38) est plus petit que celui du triangle (39). Pour $x = 6$, il est plus grand (46 contre 45). Le rectangle « dépasse » le triangle entre 5 et 6 : s'il y a égalité, c'est pour une valeur comprise \textbf{entre 5 et 6}.
\end{reponse}
\q{3}{Résoudre $8x - 2 = 6x + 9$.}
\begin{reponse}
\[ 8x - 2 = 6x + 9 \iff 8x - 6x = 9 + 2 \iff 2x = 11 \iff x = 5{,}5. \]
Les périmètres sont égaux pour $\mathbf{x = 5{,}5}$.
\end{reponse}
'''),
dict(id='2026-polj-2a', s='polj', ex=2, titre='Exercice 2 -- Points alignés ?, questions 1 et 2', theme='Angles d’un triangle isocèle, réciproque de Pythagore',
     consigne='Traite les questions 1 et 2.', regions=[(5, 134, 405)], s3=13, n3=[], s4=14, n4=[32],
     corr=r'''
\q{1.a}{Justifier que $\widehat{CFB} = 74^\circ$.}
\begin{reponse}
D'après les codages, $BC = BF = 4$ cm : le triangle $BCF$ est isocèle en $B$. Ses angles à la base sont égaux : $\widehat{CFB} = \widehat{BCF} = 74^\circ$.
\end{reponse}
\q{1.b}{Mesure de l'angle $\widehat{CBF}$.}
\begin{reponse}
$\widehat{CBF} = 180^\circ - 74^\circ - 74^\circ = \mathbf{32^\circ}$.
\end{reponse}
\q{2}{Le triangle ABC est-il rectangle ?}
\begin{reponse}
Le plus grand côté est $[AC]$. D'une part $AC^2 = 5^2 = 25$ ; d'autre part $AB^2 + BC^2 = 3^2 + 4^2 = 9 + 16 = 25$.
$AC^2 = AB^2 + BC^2$ : d'après la réciproque du théorème de Pythagore, $ABC$ est \textbf{rectangle en $B$}.
\end{reponse}
'''),
dict(id='2026-polj-2b', s='polj', ex=2, titre='Exercice 2 -- Points alignés ?, questions 3 et 4', theme='Trigonométrie (cosinus), angles',
     consigne='Traite les questions 3 et 4 (on sait que CBF = 32° et ABC = 90°).', regions=[(5, 134, 338), (5, 403, 455)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{3}{Mesure de l'angle $\widehat{FBG}$.}
\begin{reponse}
Dans le triangle $BGF$ rectangle en $G$, $[BF]$ est l'hypoténuse et $[BG]$ le côté adjacent à $\widehat{FBG}$ :
\[ \cos\widehat{FBG} = \frac{BG}{BF} = \frac{2}{4} = 0{,}5 \qquad\text{donc}\qquad \widehat{FBG} = \mathbf{60^\circ}. \]
\end{reponse}
\q{4}{Les points A, B et G sont-ils alignés ?}
\begin{reponse}
$\widehat{ABC} + \widehat{CBF} + \widehat{FBG} = 90^\circ + 32^\circ + 60^\circ = 182^\circ$.
Pour que $A$, $B$, $G$ soient alignés, il faudrait obtenir $180^\circ$ : les points \textbf{ne sont pas alignés}.
\end{reponse}
'''),
dict(id='2026-polj-3a', s='polj', ex=3, titre='Exercice 3 -- Les Jeux olympiques à Tahiti, question 1', theme='Latitude et longitude',
     consigne='Traite seulement la question 1.', regions=[(6, 134, 525)], s3=6, n3=[9], s4=None, n4=None,
     corr=r'''
\q{1}{Coordonnées géographiques de Tahiti.}
\begin{reponse}
Tahiti est à l'ouest du méridien de Greenwich et au sud de l'équateur : environ \textbf{(150°O ; 17°S)} (une latitude entre 15°S et 20°S est acceptable avec la précision de la carte).
\end{reponse}
'''),
dict(id='2026-polj-3b', s='polj', ex=3, titre='Exercice 3 -- Les Jeux olympiques à Tahiti, question 2', theme='Durées',
     consigne='Traite seulement la question 2.', regions=[(6, 134, 222), (6, 523, 648)], s3=14, n3=[], s4=15, n4=[36],
     corr=r'''
\q{2}{Durée des deux vols.}
\begin{reponse}
$22$ h $10$ min $- 2$ h $20$ min $= 21$ h $70$ min $- 2$ h $20$ min $= \mathbf{19}$ \textbf{h} $\mathbf{50}$ \textbf{min}.
\end{reponse}
'''),
dict(id='2026-polj-3c', s='polj', ex=3, titre='Exercice 3 -- Les Jeux olympiques à Tahiti, question 3', theme='Volume du cylindre, masse volumique',
     consigne='Traite seulement la question 3.', regions=[(6, 134, 222), (7, 125, 400)], s3=21, n3=[34], s4=None, n4=None,
     corr=r'''
\q{3.a}{Volume de la médaille.}
\begin{reponse}
Le rayon vaut $8{,}5 \div 2 = 4{,}25$ cm : $V = \pi \times 4{,}25^2 \times 0{,}92 \approx \mathbf{52{,}2}$ cm$^3$.
\end{reponse}
\q{3.b}{Masse d'argent de la médaille.}
\begin{reponse}
1 cm$^3$ d'argent pèse 10,5 g : $m \approx 52{,}2 \times 10{,}5 \approx \mathbf{548}$ g.
\end{reponse}
'''),
]
