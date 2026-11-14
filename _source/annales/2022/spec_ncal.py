# DNB Nouvelle-Calédonie, décembre 2022
SOURCE = ('dnb_caledonie_dec_2022.pdf', 'Nouvelle-Calédonie, décembre 2022')
AH = [(1, 194, 246)]
QH = [(1, 319, 436)]
def aff(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2022-ncal-1q{n}', s='ncal', ex=1, titre=f'Exercice 1 -- Vrai ou faux, affirmation {n}', theme=theme,
                consigne=f'Traite seulement l’affirmation {n}.', regions=AH + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
def qcm(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2022-ncal-2q{n}', s='ncal', ex=2, titre=f'Exercice 2 -- QCM, question {n}', theme=theme,
                consigne=f'Traite seulement la question {n}.', regions=QH + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
aff(1, [(1, 246, 278)], 14, [], 15, [35, 36], 'Vitesse, conversion', r'''
\q{1}{Affirmation 1 : 1\,200 km/h est plus rapide que 340,29 m/s.}
\begin{reponse}
1\,200 km/h $= 1\,200\,000$ m en 3\,600 s, soit $1\,200\,000 \div 3\,600 \approx 333{,}3$ m/s. $333{,}3 < 340{,}29$ : l'affirmation est \textbf{fausse}.
\end{reponse}
'''),
aff(2, [(1, 276, 294)], 1, [], 3, [6, 8], 'Développer et réduire', r'''
\q{2}{Affirmation 2 : $4(4x-4) + 16 = 16x^2$.}
\begin{reponse}
$4(4x - 4) + 16 = 16x - 16 + 16 = 16x$, et non $16x^2$ (pour $x = 2$ : 32 et 64). L'affirmation est \textbf{fausse}.
\end{reponse}
'''),
aff(3, [(1, 293, 312)], 24, [], 6, [14], 'Décomposition en facteurs premiers', r'''
\q{3}{Affirmation 3 : $33 \times 13$ est la décomposition de 429.}
\begin{reponse}
$33 = 3 \times 11$ n'est pas premier : $429 = 3 \times 11 \times 13$. L'affirmation est \textbf{fausse}.
\end{reponse}
'''),
qcm(1, [(1, 435, 532)], 1, [], 1, [], 'Tableur', r'''
\q{1}{Formule pour la somme de A1, B1 et C1.}
\begin{reponse}
\texttt{=somme(A1:C1)}, \textbf{réponse A}.
\end{reponse}
'''),
qcm(2, [(1, 531, 602)], 23, [], 11, [24], 'Moyenne', r'''
\q{2}{Valeur de $x$ pour une moyenne de 11.}
\begin{reponse}
La somme doit valoir $6 \times 11 = 66$. Or $15 + 10 + 13 + 9 + 10 = 57$, donc $x = 66 - 57 = \mathbf{9}$, \textbf{réponse A}.
\end{reponse}
'''),
qcm(3, [(1, 601, 613)], 6, [9], None, None, 'Repérage sur la sphère', r'''
\q{3}{L'équateur est…}
\begin{reponse}
\textbf{un parallèle}, \textbf{réponse C}.
\end{reponse}
'''),
qcm(4, [(1, 613, 695)], 21, [36], None, None, 'Volume de la boule', r'''
\q{4}{Volume exact d'une boule de 6 cm de diamètre.}
\begin{reponse}
Le rayon vaut 3 cm : $V = \dfrac{4 \times \pi \times 3^3}{3} = 4 \times 9 \times \pi = \mathbf{36\pi}$ cm$^3$, \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2022-ncal-3', s='ncal', ex=3, titre='Exercice 3 -- Le vent', theme='Effectifs, fréquences, pourcentage, médiane',
     consigne='Recopie et complète le tableau de la question 1 sur ta copie.', regions=[(1, 713, 765), (2, 120, 270), (5, 167, 240)], s3=23, n3=[], s4=11, n4=[23, 24],
     corr=r'''
\q{1}{Tableau des effectifs et fréquences.}
\begin{reponse}
10 nœuds : 3 jours, 20 \% ; 15 nœuds : 5 jours, 33 \% ; 20 nœuds : 4 jours, 27 \% ; 25 nœuds : 3 jours, 20 \%.
\end{reponse}
\q{2}{Pourcentage de jours à 15 nœuds ou plus.}
\begin{reponse}
$15 - 3 = 12$ jours sur 15 : $\dfrac{12}{15} = 0{,}8$, soit \textbf{80 \%}.
\end{reponse}
\q{3}{Vitesse médiane.}
\begin{reponse}
Il y a 15 valeurs : la médiane est la 8\ieme{} dans l'ordre croissant. Les 3 premières valent 10, les 5 suivantes (de la 4\ieme{} à la 8\ieme{}) valent 15 : la médiane est \textbf{15 nœuds}.
\end{reponse}
'''),
dict(id='2022-ncal-4a', s='ncal', ex=4, titre='Exercice 4 -- Construction, questions 1 et 2', theme='Construction, réciproque de Pythagore',
     consigne='Traite les questions 1 et 2.', regions=[(2, 280, 374)], s3=13, n3=[], s4=14, n4=[32],
     corr=r'''
\q{1}{Construire le triangle MWB.}
\begin{reponse}
Je trace $[MB]$ de 7,5 cm, puis deux arcs de cercle : de centre $M$ et de rayon 6 cm, de centre $B$ et de rayon 4,5 cm. Ils se coupent en $W$.
\end{reponse}
\q{2}{Montrer que MWB est rectangle en W.}
\begin{reponse}
Le plus grand côté est $[MB]$. $MB^2 = 7{,}5^2 = 56{,}25$ et $MW^2 + WB^2 = 6^2 + 4{,}5^2 = 36 + 20{,}25 = 56{,}25$.
D'après la réciproque du théorème de Pythagore, $MWB$ est \textbf{rectangle en $W$}.
\end{reponse}
'''),
dict(id='2022-ncal-4b', s='ncal', ex=4, titre='Exercice 4 -- Construction, question 3', theme='Trigonométrie',
     consigne='Traite seulement la question 3 (MWB est rectangle en W).', regions=[(2, 280, 327), (2, 374, 394)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{3}{Mesure de l'angle $\widehat{BMW}$.}
\begin{reponse}
$\cos\widehat{BMW} = \dfrac{MW}{MB} = \dfrac{6}{7{,}5} = 0{,}8$, donc $\widehat{BMW} \approx \mathbf{37^\circ}$.
\end{reponse}
'''),
dict(id='2022-ncal-4c', s='ncal', ex=4, titre='Exercice 4 -- Construction, questions 4 à 6', theme='Théorème de Thalès, longueurs',
     consigne='Traite les questions 4 à 6 (MWB est rectangle en W).', regions=[(2, 280, 327), (2, 394, 507)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{4.c}{Calculer WE.}
\begin{reponse}
Les points $W$, $F$, $B$ et $W$, $E$, $M$ sont alignés et $(EF) \parallel (MB)$. D'après le théorème de Thalès :
\[ \frac{WE}{WM} = \frac{WF}{WB} \qquad\text{donc}\qquad \frac{WE}{6} = \frac{3}{4{,}5} \qquad\text{et}\qquad WE = \frac{6 \times 3}{4{,}5} = \mathbf{4} \text{ cm}. \]
\end{reponse}
\q{6}{Calculer TE.}
\begin{reponse}
$T$ est sur la demi-droite $[MW)$ avec $MT = 10$ cm, donc $WT = 10 - 6 = 4$ cm. $E$ est sur $[MW]$, donc $TE = TW + WE = 4 + 4 = \mathbf{8}$ cm.
\end{reponse}
'''),
dict(id='2022-ncal-5a', s='ncal', ex=5, titre='Exercice 5 -- Le club de planche à voile, questions 1 et 2', theme='Calculs de prix, expression littérale',
     consigne='Traite les questions 1 et 2.', regions=[(2, 533, 760)], s3=14, n3=[], s4=8, n4=[11, 20],
     corr=r'''
\q{1}{Prix de 4 heures au tarif découverte.}
\begin{reponse}
$4 \times 1\,600 = \mathbf{6\,400}$ F.
\end{reponse}
\q{2.a}{4 heures au tarif personnalisé.}
\begin{reponse}
$4\,800 + 4 \times 600 = 4\,800 + 2\,400 = 7\,200$ F.
\end{reponse}
\q{2.b}{10 heures au tarif personnalisé.}
\begin{reponse}
$4\,800 + 10 \times 600 = \mathbf{10\,800}$ F.
\end{reponse}
\q{2.c}{Expression de $P(x)$.}
\begin{reponse}
$\mathbf{P(x) = 600x + 4\,800}$.
\end{reponse}
'''),
dict(id='2022-ncal-5b', s='ncal', ex=5, titre='Exercice 5 -- Le club de planche à voile, questions 3 et 4', theme='Fonctions affines, lecture graphique, équation',
     consigne='Traite les questions 3 et 4 (P(x) = 600x + 4 800 ; trace sur une copie du graphique).', regions=[(2, 533, 664), (2, 758, 790), (3, 120, 245), (5, 257, 535)], s3=17, n3=[28, 29], s4=None, n4=None,
     corr=r'''
\q{3.a}{Égalité des tarifs découverte et renforcé.}
\begin{reponse}
Les droites se coupent pour $x = 6$ : $1\,600 \times 6 = 9\,600$. Les deux tarifs sont égaux pour \textbf{6 heures}.
\end{reponse}
\q{3.b}{Tracer la représentation de $P$.}
\begin{reponse}
C'est la droite qui passe par les points $(4\,;7\,200)$ et $(10\,;10\,800)$.
\end{reponse}
\q{3.c}{Tarif le plus économique pour 7 heures.}
\begin{reponse}
Découverte : $7 \times 1\,600 = 11\,200$ F ; personnalisé : $P(7) = 4\,200 + 4\,800 = 9\,000$ F ; renforcé : 9\,600 F. Le \textbf{tarif personnalisé} est le plus économique.
\end{reponse}
\q{4}{Égalité des tarifs personnalisé et renforcé.}
\begin{reponse}
$600x + 4\,800 = 9\,600 \iff 600x = 4\,800 \iff x = 8$ : pour \textbf{8 heures}.
\end{reponse}
'''),
dict(id='2022-ncal-6', s='ncal', ex=6, titre='Exercice 6 -- Les dés', theme='Probabilités (deux épreuves)',
     regions=[(3, 255, 560)], s3=22, n3=[39], s4=None, n4=None,
     corr=r'''
\q{1}{Lecture de (3 ; 2).}
\begin{reponse}
a. \textbf{3} au premier lancer ; b. \textbf{2} au second.
\end{reponse}
\q{2}{Les 16 issues.}
\begin{reponse}
(1 ; 1), (1 ; 2), (1 ; 3), (1 ; 4), (2 ; 1), (2 ; 2), (2 ; 3), (2 ; 4), (3 ; 1), (3 ; 2), (3 ; 3), (3 ; 4), (4 ; 1), (4 ; 2), (4 ; 3), (4 ; 4).
\end{reponse}
\q{3}{L'évènement A.}
\begin{reponse}
La plus petite somme possible est $1 + 1 = 2$ : A est un évènement \textbf{impossible}.
\end{reponse}
\q{4}{Issues de l'évènement C.}
\begin{reponse}
(1 ; 4), (2 ; 3), (3 ; 2), (4 ; 1).
\end{reponse}
\q{5}{Probabilité de C.}
\begin{reponse}
4 issues favorables sur 16 équiprobables : $p = \dfrac{4}{16} = \mathbf{\dfrac{1}{4}}$.
\end{reponse}
'''),
dict(id='2022-ncal-7', s='ncal', ex=7, titre='Exercice 7 -- Le drapeau', theme='Algorithmique (Scratch)',
     consigne='Recopie et complète le script n° 2 sur ta copie.', regions=[(3, 566, 790), (4, 120, 312), (5, 552, 602), (6, 120, 420)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Motif de base.}
\begin{reponse}
Un segment de 6 cm (la hampe), puis un carré de 4 cm de côté au bout de ce segment : un petit drapeau.
\end{reponse}
\q{2}{Script n° 2 complété.}
\begin{reponse}
répéter \textbf{8} fois ; motif de base ; aller à x: \textbf{0} y: \textbf{0} ; tourner de \textbf{45} degrés ($360 \div 8 = 45$).
\end{reponse}
'''),
]
