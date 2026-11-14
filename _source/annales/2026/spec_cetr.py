# DNB Centres étrangers, 18 juin 2026
SOURCE = ('dnb_centres_etr_juin_2026.pdf', 'Centres étrangers, 18 juin 2026')
QA = (1, 398, 481)
def q(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2026-cetr-a{n}', s='cetr', ex=0, titre=f'Automatismes, question {n}', theme=theme,
                regions=[QA] + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
q(1, [(1, 481, 543)], 23, [], 11, [24], 'Médiane', r'''
\q{1}{Médiane des températures.}
\begin{reponse}
Dans l'ordre croissant : $-1$ ; 0 ; 1 ; 3 ; 7. La valeur du milieu (la 3\ieme{} sur 5) est la médiane : \textbf{1~°C}.
\end{reponse}
'''),
q(2, [(1, 543, 706)], 11, [], 7, [16], 'Translation', r'''
\q{2}{Image du motif n°4 par la translation qui transforme le n°2 en n°6.}
\begin{reponse}
Pour aller du motif n°2 au motif n°6, on se décale d'une case vers la droite et d'une case vers le bas. Le motif n°4 a pour image le motif \textbf{n°8}.
\end{reponse}
'''),
q(3, [(1, 706, 768)], 22, [], 20, [47], 'Probabilités', r'''
\q{3}{Probabilité de tirer une boule rouge.}
\begin{reponse}
3 boules rouges sur 8 boules : $p = \mathbf{\dfrac{3}{8}}$.
\end{reponse}
'''),
q(4, [(1, 768, 786), (2, 128, 288)], 4, [6], None, None, 'Cosinus', r'''
\q{4}{Compléter $\cos\widehat{LKJ}$.}
\begin{reponse}
Le triangle $JLK$ est rectangle en $L$. Pour l'angle $\widehat{LKJ}$, le côté adjacent est $[KL]$ et l'hypoténuse $[JK]$ :
$\cos\widehat{LKJ} = \mathbf{\dfrac{KL}{JK}}$.
\end{reponse}
'''),
q(5, [(2, 288, 350)], 25, [], 13, [31], 'Écriture scientifique', r'''
\q{5}{Notation scientifique de 311\,200\,000.}
\begin{reponse}
$311\,200\,000 = \mathbf{3{,}112 \times 10^8}$.
\end{reponse}
'''),
q(6, [(2, 350, 414)], 14, [], 15, [35], 'Vitesse, distance', r'''
\q{6}{Distance parcourue en 2 h 30 min à 40 km/h.}
\begin{reponse}
En 2 h : $2 \times 40 = 80$ km ; en 30 min : $40 \div 2 = 20$ km. Total : \textbf{100 km}.
\end{reponse}
'''),
q(7, [(2, 414, 492)], 16, [25], 3, [7], 'Factoriser', r'''
\q{7}{Forme factorisée de $5x + 5$.}
\begin{reponse}
$5x + 5 = 5 \times x + 5 \times 1 = \mathbf{5(x + 1)}$.
\end{reponse}
'''),
q(8, [(2, 492, 594)], 14, [], 15, [34], 'Pourcentage de baisse', r'''
\q{8}{Calcul du prix après une baisse de 10 \%.}
\begin{reponse}
La baisse vaut $\dfrac{10}{100} \times 80$ € ; le calcul est $\mathbf{80 - \dfrac{10}{100} \times 80}$ (le prix final est 72 €).
\end{reponse}
'''),
q(9, [(2, 594, 632), (3, 125, 455)], 8, [12], None, None, 'Lecture graphique', r'''
\q{9}{Durée pendant laquelle la hauteur d'eau dépasse 4 m.}
\begin{reponse}
La courbe est au-dessus de 4 m d'environ 14 h 30 à 19 h : \textbf{4 h 30 min}.
\end{reponse}
'''),
dict(id='2026-cetr-1a', s='cetr', ex=1, titre='Exercice 1 -- Deux triangles rectangles, questions 1 et 2', theme='Construction, théorème de Pythagore',
     consigne='Traite les questions 1 et 2.', regions=[(4, 278, 556)], s3=2, n3=[], s4=4, n4=[10],
     corr=r'''
\q{1}{Tracer ABC en vraie grandeur.}
\begin{reponse}
Je trace $[AB]$ de 6,4 cm et la perpendiculaire à $(AB)$ passant par $B$. Avec le compas, je trace un arc de cercle de centre $A$ et de rayon 8 cm : il coupe la perpendiculaire en $C$.
\end{reponse}
\q{2}{Démontrer que BC = 4,8 cm.}
\begin{reponse}
Le triangle $ABC$ est rectangle en $B$, d'hypoténuse $[AC]$. D'après le théorème de Pythagore :
\[ BC^2 = AC^2 - AB^2 = 8^2 - 6{,}4^2 = 64 - 40{,}96 = 23{,}04 \qquad\text{donc}\qquad BC = \sqrt{23{,}04} = 4{,}8 \text{ cm}. \]
\end{reponse}
'''),
dict(id='2026-cetr-1b', s='cetr', ex=1, titre='Exercice 1 -- Deux triangles rectangles, questions 3 à 5', theme='Théorème de Thalès, périmètres',
     consigne='Traite les questions 3 à 5 (BC = 4,8 cm).', regions=[(4, 278, 522), (4, 555, 620)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{3}{Justifier que (BC) et (MN) sont parallèles.}
\begin{reponse}
$(BC)$ et $(MN)$ sont toutes les deux perpendiculaires à la droite $(AM)$ : elles sont parallèles.
\end{reponse}
\q{4}{Démontrer que MN = 7,2 cm et AN = 12 cm.}
\begin{reponse}
Les points $A$, $B$, $M$ et $A$, $C$, $N$ sont alignés et $(BC) \parallel (MN)$, avec $AM = 6{,}4 + 3{,}2 = 9{,}6$ cm. D'après le théorème de Thalès :
\[ \frac{AB}{AM} = \frac{AC}{AN} = \frac{BC}{MN} \qquad\text{donc}\qquad \frac{6{,}4}{9{,}6} = \frac{8}{AN} = \frac{4{,}8}{MN}. \]
$MN = \dfrac{4{,}8 \times 9{,}6}{6{,}4} = \mathbf{7{,}2}$ cm et $AN = \dfrac{8 \times 9{,}6}{6{,}4} = \mathbf{12}$ cm.
\end{reponse}
\q{5}{Les périmètres de ABC et de BMNC sont-ils égaux ?}
\begin{reponse}
Périmètre de $ABC$ : $6{,}4 + 4{,}8 + 8 = 19{,}2$ cm.
$CN = AN - AC = 12 - 8 = 4$ cm, donc le périmètre de $BMNC$ vaut $3{,}2 + 7{,}2 + 4 + 4{,}8 = 19{,}2$ cm.
\textbf{Oui}, les deux périmètres sont égaux.
\end{reponse}
'''),
dict(id='2026-cetr-2a', s='cetr', ex=2, titre='Exercice 2 -- Les bonbons, partie A', theme='Volumes du cylindre et de la boule, conversion',
     consigne='Traite la partie A.', regions=[(5, 134, 537)], s3=21, n3=[34, 36], s4=None, n4=None,
     corr=r'''
\q{1}{Hauteur du cylindre.}
\begin{reponse}
Chaque demi-boule mesure 2,5 mm de long : $h = 15 - 2 \times 2{,}5 = \mathbf{10}$ mm.
\end{reponse}
\q{2.a}{Volume de la partie cylindrique.}
\begin{reponse}
$V = \pi \times 2{,}5^2 \times 10 = 62{,}5\pi \approx \mathbf{196}$ mm$^3$.
\end{reponse}
\q{2.b}{Le volume total est-il compris entre 260 et 262 mm$^3$ ?}
\begin{reponse}
Les deux demi-boules forment une boule de rayon 2,5 mm : $\dfrac{4}{3} \times \pi \times 2{,}5^3 \approx 65{,}4$ mm$^3$.
Volume total : $62{,}5\pi + 65{,}4 \approx 196{,}3 + 65{,}4 = 261{,}7$ mm$^3$. \textbf{Léa a raison}.
\end{reponse}
\q{3}{Peut-on produire plus de 300\,000 bonbons avec 83 L ?}
\begin{reponse}
1 L $=$ 1 dm$^3$ $=$ 1\,000\,000 mm$^3$, donc 83 L $=$ 83\,000\,000 mm$^3$.
$83\,000\,000 \div 261{,}7 \approx 317\,000$ bonbons : \textbf{oui}, plus de 300\,000 bonbons.
\end{reponse}
'''),
dict(id='2026-cetr-2b', s='cetr', ex=2, titre='Exercice 2 -- Les bonbons, partie B', theme='Comparaison de prix',
     consigne='Traite la partie B.', regions=[(5, 134, 192), (5, 535, 705)], s3=14, n3=[], s4=5, n4=[11],
     corr=r'''
\q{B}{Quel format choisir pour 1 kg ?}
\begin{reponse}
Format A : 2 sachets de 500 g, soit $2 \times 7{,}90 = 15{,}80$ €.
Format B : 4 sachets de 250 g, le quatrième à moitié prix : $3 \times 4{,}30 + 4{,}30 \div 2 = 12{,}90 + 2{,}15 = 15{,}05$ €.
Léa doit choisir le \textbf{format B}.
\end{reponse}
'''),
dict(id='2026-cetr-3a', s='cetr', ex=3, titre='Exercice 3 -- Deux programmes, questions 1 et 2', theme='Programmes de calcul',
     consigne='Traite les questions 1 et 2.', regions=[(6, 134, 365)], s3=1, n3=[], s4=8, n4=[2, 18],
     corr=r'''
\q{1}{Programme A avec 1.}
\begin{reponse}
$1 + 6 = 7$ et $1 - 4 = -3$ ; $7 \times (-3) = \mathbf{-21}$.
\end{reponse}
\q{2}{Programme B avec 10.}
\begin{reponse}
$10^2 = 100$ ; $100 - 9 = \mathbf{91}$.
\end{reponse}
'''),
dict(id='2026-cetr-3b', s='cetr', ex=3, titre='Exercice 3 -- Deux programmes, question 3', theme='Équation x² = a',
     consigne='Traite seulement la question 3.', regions=[(6, 134, 316), (6, 363, 383)], s3=19, n3=[32], s4=None, n4=None,
     corr=r'''
\q{3}{Nombres de départ qui donnent 16 avec le programme B.}
\begin{reponse}
Je résous $x^2 - 9 = 16$, soit $x^2 = 25$. Cette équation a deux solutions : $\mathbf{x = 5}$ et $\mathbf{x = -5}$.
\end{reponse}
'''),
dict(id='2026-cetr-3c', s='cetr', ex=3, titre='Exercice 3 -- Deux programmes, question 4', theme='Algorithmique (Scratch)',
     consigne='Traite seulement la question 4.', regions=[(6, 134, 316), (6, 380, 553)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{4}{Compléter les lignes 3, 4 et 5.}
\begin{reponse}
Ligne 3 : mettre Valeur 1 à \textbf{réponse + 6}.
Ligne 4 : mettre Valeur 2 à \textbf{réponse - 4}.
Ligne 5 : mettre Résultat à \textbf{Valeur 1 * Valeur 2}.
\end{reponse}
'''),
dict(id='2026-cetr-3d', s='cetr', ex=3, titre='Exercice 3 -- Deux programmes, questions 5 et 6', theme='Double distributivité, équation',
     consigne='Traite les questions 5 et 6.', regions=[(6, 134, 316), (6, 554, 613)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{5}{Montrer que le programme A donne $x^2 + 2x - 24$.}
\begin{reponse}
Le programme A calcule $(x + 6)(x - 4)$. Je développe avec la double distributivité :
\[ (x + 6)(x - 4) = x^2 - 4x + 6x - 24 = x^2 + 2x - 24. \]
\end{reponse}
\q{6}{Nombre de départ pour lequel A et B donnent le même résultat.}
\begin{reponse}
Je résous $x^2 + 2x - 24 = x^2 - 9$. J'enlève $x^2$ à chaque membre :
\[ 2x - 24 = -9 \iff 2x = 15 \iff x = 7{,}5. \]
Il faut choisir \textbf{7,5} (les deux programmes donnent alors 47,25).
\end{reponse}
'''),
]
