# DNB Métropole, septembre 2022
SOURCE = ('dnb_metropole_sept_2022.pdf', 'Métropole, septembre 2022')
QH = [(1, 236, 366)]
def qcm(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2022-msep-1q{n}', s='msep', ex=1, titre=f'Exercice 1 -- QCM, question {n}', theme=theme,
                consigne=f'Traite seulement la question {n}.', regions=QH + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
qcm(1, [(1, 365, 394)], 25, [46], 13, [29], 'Puissances', r'''
\q{1}{$\dfrac{5^7 \times 5^3}{5^2}$.}
\begin{reponse}
$\dfrac{5^7 \times 5^3}{5^2} = \dfrac{5^{10}}{5^2} = \mathbf{5^8}$, \textbf{réponse C}.
\end{reponse}
'''),
qcm(2, [(1, 393, 436)], 24, [44], 12, [25], 'Fraction irréductible', r'''
\q{2}{Fraction irréductible égale à $\frac{630}{882}$.}
\begin{reponse}
$630 = 2 \times 3^2 \times 5 \times 7$ et $882 = 2 \times 3^2 \times 7^2$. Je simplifie par $2 \times 3^2 \times 7 = 126$ : $\dfrac{630}{882} = \mathbf{\dfrac{5}{7}}$, \textbf{réponse A}.
\end{reponse}
'''),
qcm(3, [(1, 435, 477)], 12, [18], None, None, 'Double distributivité', r'''
\q{3}{Développer $A = (x-2)(3x+7)$.}
\begin{reponse}
$A = 3x^2 + 7x - 6x - 14 = \mathbf{3x^2 + x - 14}$, \textbf{réponse C}.
\end{reponse}
'''),
qcm(4, [(1, 476, 518)], 19, [32], None, None, 'Équation produit', r'''
\q{4}{Solutions de $(2x+1)(-x+3) = 0$.}
\begin{reponse}
Un produit est nul si l'un de ses facteurs est nul : $2x + 1 = 0 \iff x = -\dfrac{1}{2}$ ou $-x + 3 = 0 \iff x = 3$. \textbf{Réponse B}.
\end{reponse}
'''),
qcm(5, [(1, 517, 642)], 22, [], 20, [47], 'Probabilités', r'''
\q{5}{Probabilité de ne pas tirer de boule noire.}
\begin{reponse}
$4 + 2 = 6$ boules ne sont pas noires sur 9 : $p = \mathbf{\dfrac{6}{9}}$, \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2022-msep-2a', s='msep', ex=2, titre='Exercice 2 -- La location de voiture, questions 1 et 2', theme='Calculs de prix',
     consigne='Traite les questions 1 et 2.', regions=[(1, 662, 782), (2, 120, 218)], s3=14, n3=[], s4=5, n4=[11],
     corr=r'''
\q{1}{Prix pour 280 km au tarif « Affaire ».}
\begin{reponse}
$280 \times 0{,}50 = \mathbf{140}$ €.
\end{reponse}
\q{2}{Offre la plus avantageuse pour 450 km.}
\begin{reponse}
« Affaire » : $450 \times 0{,}5 = 225$ € ; « Voyage court » : $120 + 450 \times 0{,}2 = 210$ € ; « Voyage long » : 230 €.
Le tarif \textbf{« Voyage court »} est le plus avantageux.
\end{reponse}
'''),
dict(id='2022-msep-2b', s='msep', ex=2, titre='Exercice 2 -- La location de voiture, questions 3 et 4', theme='Fonctions linéaires et affines, équation, lecture graphique',
     consigne='Traite les questions 3 et 4 (trace les droites dans un repère : 1 cm pour 40 km en abscisse et pour 40 € en ordonnée).', regions=[(1, 662, 782), (2, 120, 160), (2, 216, 410)], s3=17, n3=[26, 28, 29], s4=None, n4=None,
     corr=r'''
\q{3.a}{Associer chaque fonction à son tarif.}
\begin{reponse}
$l$ : « Voyage long » ; $m$ : « Affaire » ; $n$ : « Voyage court ».
\end{reponse}
\q{3.b}{Distance pour laquelle « Voyage court » et « Affaire » coûtent autant.}
\begin{reponse}
Je résous $0{,}5x = 0{,}2x + 120 \iff 0{,}3x = 120 \iff x = 400$ : pour \textbf{400 km}.
\end{reponse}
\q{4.a}{Tracer les représentations graphiques.}
\begin{reponse}
$l$ : droite horizontale d'ordonnée 230. $m$ : droite passant par $(0\,;0)$ et $(400\,;200)$. $n$ : droite passant par $(0\,;120)$ et $(400\,;200)$.
\end{reponse}
\q{4.b}{Distance à partir de laquelle « Voyage long » est le plus avantageux.}
\begin{reponse}
La droite de $l$ est en dessous des deux autres à partir de son intersection avec celle de $n$ : $0{,}2x + 120 = 230$ pour $x = 550$. Il faut dépasser \textbf{550 km}.
\end{reponse}
'''),
dict(id='2022-msep-3a', s='msep', ex=3, titre='Exercice 3 -- Les cerfs-volants, partie A', theme='Angles, symétries',
     consigne='Traite la partie A.', regions=[(2, 418, 742)], s3=11, n3=[], s4=7, n4=[],
     corr=r'''
\q{1}{Mesure de l'angle $\widehat{PSL}$.}
\begin{reponse}
$SLP$ est équilatéral : ses angles mesurent $180^\circ \div 3 = \mathbf{60^\circ}$.
\end{reponse}
\q{2}{Image du cerf-volant 2 par la symétrie d'axe (PL).}
\begin{reponse}
Le \textbf{cerf-volant 5}.
\end{reponse}
\q{3}{Transformation qui transforme le cerf-volant 1 en cerf-volant 6.}
\begin{reponse}
La \textbf{symétrie de centre $J$}.
\end{reponse}
'''),
dict(id='2022-msep-3b', s='msep', ex=3, titre='Exercice 3 -- Les cerfs-volants, partie B', theme='Algorithmique (Scratch)',
     consigne='Traite la partie B.', regions=[(2, 418, 440), (2, 740, 790), (3, 120, 582)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Tracer le programme de Nicolas.}
\begin{reponse}
Il trace trois côtés de 3 cm en tournant de $120^\circ$ : un \textbf{triangle équilatéral} de côté 3 cm.
\end{reponse}
\q{2}{Élève dont le script est correct.}
\begin{reponse}
Le cerf-volant a deux côtés de 300 pas et deux de 173 pas, les côtés égaux étant consécutifs. Le programme de Nicolas trace un triangle ; celui de Tyago alterne 173 et 300 pas. C'est le programme d'\textbf{Essya} : 300, puis 173, 173, puis 300, avec des angles de $90^\circ$ entre les côtés longs et courts.
\end{reponse}
'''),
dict(id='2022-msep-4a', s='msep', ex=4, titre='Exercice 4 -- Le pont de l’île de Ré, questions 1 à 3', theme='Tableur, moyenne, étendue',
     consigne='Traite les questions 1 à 3.', regions=[(3, 580, 640), (4, 120, 408)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{1}{Formule en B14.}
\begin{reponse}
\texttt{=SOMME(B2:B13)}.
\end{reponse}
\q{2}{Nombre moyen de passages par mois.}
\begin{reponse}
$2\,801\,172 \div 12 = \mathbf{233\,431}$ passages par mois.
\end{reponse}
\q{3}{Étendue.}
\begin{reponse}
$389\,250 - 62\,930 = \mathbf{326\,320}$ passages.
\end{reponse}
'''),
dict(id='2022-msep-4b', s='msep', ex=4, titre='Exercice 4 -- Le pont de l’île de Ré, questions 4 et 5', theme='Pourcentage d’évolution, vitesse',
     consigne='Traite les questions 4 et 5.', regions=[(3, 580, 640), (4, 120, 357), (4, 408, 515)], s3=14, n3=[], s4=15, n4=[34, 35],
     corr=r'''
\q{4}{Pourcentage d'augmentation entre mai 2020 et mai 2021.}
\begin{reponse}
$\dfrac{305\,214 - 179\,699}{179\,699} = \dfrac{125\,515}{179\,699} \approx 0{,}698$ : une hausse d'environ \textbf{70 \%}.
\end{reponse}
\q{5}{Vitesse du cycliste.}
\begin{reponse}
3 km en 10 min, donc $6 \times 3 = 18$ km en 60 min : \textbf{18 km/h}.
\end{reponse}
'''),
dict(id='2022-msep-5a', s='msep', ex=5, titre='Exercice 5 -- La tyrolienne, questions 1 à 3', theme='Trigonométrie, théorème de Pythagore',
     consigne='Traite les questions 1 à 3.', regions=[(4, 527, 790), (5, 120, 282)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{1}{Vérifier que BC = 20 m.}
\begin{reponse}
$BC = 12{,}20 + 6 + 1{,}80 = 20$ m.
\end{reponse}
\q{2}{La tyrolienne est-elle conforme ?}
\begin{reponse}
Le triangle $ABC$ est rectangle en $B$ : $\tan\widehat{BCA} = \dfrac{AB}{BC} = \dfrac{5{,}5}{20} = 0{,}275$, donc $\widehat{BCA} \approx 15^\circ$.
$15^\circ < 30^\circ$ : \textbf{elle est conforme}.
\end{reponse}
\q{3}{Longueur AC du câble.}
\begin{reponse}
D'après le théorème de Pythagore : $AC^2 = 5{,}5^2 + 20^2 = 30{,}25 + 400 = 430{,}25$, donc $AC \approx 20{,}7$, soit \textbf{21 m}.
\end{reponse}
'''),
dict(id='2022-msep-5b', s='msep', ex=5, titre='Exercice 5 -- La tyrolienne, question 4', theme='Théorème de Thalès',
     consigne='Traite seulement la question 4 (BC = 20 m).', regions=[(4, 527, 790), (5, 120, 230), (5, 282, 310)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{4}{Distance DC.}
\begin{reponse}
$(ED)$ et $(AB)$ sont perpendiculaires à $(BC)$ : elles sont parallèles. Les points $C$, $E$, $A$ et $C$, $D$, $B$ sont alignés. D'après le théorème de Thalès :
\[ \frac{CD}{CB} = \frac{ED}{AB} \qquad\text{donc}\qquad CD = \frac{1{,}5 \times 20}{5{,}5} \approx \mathbf{5{,}45} \text{ m}. \]
\end{reponse}
'''),
dict(id='2022-msep-5c', s='msep', ex=5, titre='Exercice 5 -- La tyrolienne, question 5', theme='Volume du pavé droit',
     consigne='Traite seulement la question 5.', regions=[(4, 527, 790), (5, 120, 230), (5, 310, 346)], s3=21, n3=[], s4=2, n4=[],
     corr=r'''
\q{5}{Volume de la piscine.}
\begin{reponse}
$V = 6 \times 6 \times 1{,}6 = \mathbf{57{,}6}$ m$^3$.
\end{reponse}
'''),
]
