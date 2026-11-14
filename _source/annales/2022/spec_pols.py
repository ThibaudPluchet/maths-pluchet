# DNB Polynésie, septembre 2022
SOURCE = ('dnb_polynesie_sept_2022.pdf', 'Polynésie, septembre 2022')
QH = [(1, 222, 262)]
def qu(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2022-pols-1q{n}', s='pols', ex=1, titre=f'Exercice 1 -- Six questions, question {n}', theme=theme,
                consigne=f'Traite seulement la question {n}.', regions=QH + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
qu(1, [(1, 262, 306)], 5, [], 12, [26, 28], 'Addition de fractions', r'''
\q{1}{Calculer $\frac{5}{6} + \frac{7}{8}$.}
\begin{reponse}
\[ \frac{5}{6} + \frac{7}{8} = \frac{20}{24} + \frac{21}{24} = \mathbf{\frac{41}{24}}. \]
\end{reponse}
'''),
qu(2, [(1, 306, 349)], 24, [43, 44], 12, [14, 25], 'Décomposition, fraction irréductible', r'''
\q{2.a}{Décompositions de 198 et de 84.}
\begin{reponse}
$198 = \mathbf{2 \times 3^2 \times 11}$ et $84 = \mathbf{2^2 \times 3 \times 7}$.
\end{reponse}
\q{2.b}{Forme irréductible de $\frac{198}{84}$.}
\begin{reponse}
Je simplifie par $2 \times 3 = 6$ : $\dfrac{198}{84} = \dfrac{3 \times 11}{2 \times 7} = \mathbf{\dfrac{33}{14}}$.
\end{reponse}
'''),
qu(3, [(1, 347, 380)], 1, [], 3, [6, 8], 'Développer et réduire', r'''
\q{3}{Développer et réduire $E = 5(3x-4) - (2x-7)$.}
\begin{reponse}
$E = 15x - 20 - 2x + 7 = \mathbf{13x - 13}$.
\end{reponse}
'''),
qu(4, [(1, 380, 497)], 7, [], 16, [38, 39], 'Périmètre, équation', r'''
\q{4}{Valeur de $b$ pour un périmètre de 25.}
\begin{reponse}
Le rectangle mesure 4,5 de large et $3b + 2{,}9$ de long. Son périmètre vaut $2(4{,}5 + 3b + 2{,}9) = 14{,}8 + 6b$.
\[ 14{,}8 + 6b = 25 \iff 6b = 10{,}2 \iff b = \mathbf{1{,}7}. \]
\end{reponse}
'''),
qu(5, [(1, 497, 671)], 21, [35], 17, [40], 'Volume d’une pyramide', r'''
\q{5}{Volume de la pyramide.}
\begin{reponse}
La base est un rectangle de $4 \times 3 = 12$ : $V = \dfrac{12 \times 6}{3} = \mathbf{24}$.
\end{reponse}
'''),
qu(6, [(1, 670, 720)], 14, [21], 15, [34], 'Pourcentage d’augmentation', r'''
\q{6}{Nombre d'habitants en 2019.}
\begin{reponse}
Augmenter de 12 \%, c'est multiplier par 1,12. Donc $x \times 1{,}12 = 20\,692$ et $x = 20\,692 \div 1{,}12 = \mathbf{18\,475}$ habitants.
\end{reponse}
'''),
dict(id='2022-pols-2a', s='pols', ex=2, titre='Exercice 2 -- Les araignées, questions 1 et 2', theme='Théorème de Pythagore, trigonométrie',
     consigne='Traite les questions 1 et 2.', regions=[(1, 731, 750), (2, 120, 324)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{1}{Montrer que AC = 6,5 m.}
\begin{reponse}
Le triangle $ABC$ est rectangle en $B$. D'après le théorème de Pythagore :
\[ AC^2 = AB^2 + BC^2 = 3{,}9^2 + 5{,}2^2 = 15{,}21 + 27{,}04 = 42{,}25 \qquad\text{donc}\qquad AC = \sqrt{42{,}25} = 6{,}5 \text{ m}. \]
\end{reponse}
\q{2}{Mesure de l'angle $\widehat{ACB}$.}
\begin{reponse}
$\cos\widehat{ACB} = \dfrac{BC}{AC} = \dfrac{5{,}2}{6{,}5} = 0{,}8$, donc $\widehat{ACB} \approx \mathbf{37^\circ}$.
\end{reponse}
'''),
dict(id='2022-pols-2b', s='pols', ex=2, titre='Exercice 2 -- Les araignées, questions 3 à 5', theme='Théorème de Thalès, vitesse, durée',
     consigne='Traite les questions 3 à 5 (AC = 6,5 m).', regions=[(1, 731, 750), (2, 120, 290), (2, 326, 712)], s3=14, n3=[], s4=15, n4=[22, 35],
     corr=r'''
\q{3}{Durée pour la première araignée.}
\begin{reponse}
$t = \dfrac{d}{v} = \dfrac{6{,}5}{0{,}2} = 32{,}5$ s.
\end{reponse}
\q{4}{Longueurs FH et HA.}
\begin{reponse}
$(FH)$ et $(CB)$ sont perpendiculaires à $(AB)$ : elles sont parallèles. Les points $A$, $F$, $C$ et $A$, $H$, $B$ sont alignés. D'après le théorème de Thalès :
\[ \frac{AF}{AC} = \frac{AH}{AB} = \frac{FH}{CB} \qquad\text{donc}\qquad \frac{4}{6{,}5} = \frac{AH}{3{,}9} = \frac{FH}{5{,}2}. \]
$FH = \dfrac{4 \times 5{,}2}{6{,}5} = \mathbf{3{,}2}$ m et $HA = \dfrac{4 \times 3{,}9}{6{,}5} = \mathbf{2{,}4}$ m.
\end{reponse}
\q{5}{Quelle araignée arrive la première ?}
\begin{reponse}
$CF = 6{,}5 - 4 = 2{,}5$ m. La deuxième marche $2{,}5 + 2{,}4 = 4{,}9$ m en $4{,}9 \div 0{,}2 = 24{,}5$ s et descend 3,2 m en $3{,}2 \div 0{,}8 = 4$ s : $28{,}5$ s en tout.
$28{,}5 < 32{,}5$ : c'est la \textbf{deuxième araignée} qui arrive la première.
\end{reponse}
'''),
dict(id='2022-pols-3a', s='pols', ex=3, titre='Exercice 3 -- Les motifs, questions 1 à 3', theme='Algorithmique (Scratch)',
     consigne='Traite les questions 1 à 3 (reproduis le quadrillage et le script 3 sur ta copie).', regions=[(2, 725, 790), (3, 120, 790), (4, 120, 350), (7, 172, 328), (7, 374, 826)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Chemin du script 1.}
\begin{reponse}
Le stylo trace un rectangle : 1 carreau vers le haut, 2 carreaux vers la droite, 1 carreau vers le bas, 2 carreaux vers la gauche (il revient au départ).
\end{reponse}
\q{2}{Dessin du script 2.}
\begin{reponse}
Le script 2 trace d'abord deux côtés de 20 pixels (vers le haut puis vers la droite), puis deux côtés de 40 pixels : c'est le \textbf{dessin 2}.
Le dessin 1 ne passe pas à 40 après deux côtés de 20 ; le dessin 3 ne commence pas vers le haut.
\end{reponse}
\q{3}{Cases du script 3.}
\begin{reponse}
Dans l'ordre : avancer de \textbf{40}, avancer de \textbf{20}, avancer de \textbf{120}.
\end{reponse}
'''),
dict(id='2022-pols-3b', s='pols', ex=3, titre='Exercice 3 -- Les motifs, question 4', theme='Translation, symétries',
     consigne='Traite seulement la question 4.', regions=[(2, 725, 746), (4, 348, 720)], s3=11, n3=[], s4=7, n4=[16],
     corr=r'''
\q{4.a}{Image du motif 1 par la translation qui transforme B en E.}
\begin{reponse}
Le \textbf{motif 5}.
\end{reponse}
\q{4.b}{Image du motif 1 par la symétrie de centre B.}
\begin{reponse}
Le \textbf{motif 9}.
\end{reponse}
\q{4.c}{Image du motif 16 par la symétrie de centre G.}
\begin{reponse}
Le \textbf{motif 12}.
\end{reponse}
\q{4.d}{Image du motif 2 par la symétrie d'axe (CG).}
\begin{reponse}
Le \textbf{motif 5}.
\end{reponse}
'''),
dict(id='2022-pols-4a', s='pols', ex=4, titre='Exercice 4 -- Trois fonctions, questions 1 et 2', theme='Images, antécédents, programme de calcul',
     consigne='Traite les questions 1 et 2.', regions=[(4, 734, 790), (5, 120, 366)], s3=8, n3=[5, 12], s4=None, n4=None,
     corr=r'''
\q{1.a}{Image de 3 par $f$.}
\begin{reponse}
$f(3) = \mathbf{-5}$.
\end{reponse}
\q{1.b}{Un nombre qui a pour image 5.}
\begin{reponse}
$f(-2) = 5$ : \textbf{$-2$}.
\end{reponse}
\q{1.c}{Un antécédent de 1.}
\begin{reponse}
$f(0) = 1$ : \textbf{0}.
\end{reponse}
\q{2.a}{Résultats pour 1 et pour $-2$.}
\begin{reponse}
$1 + 1 = 2$ et $2^2 = \mathbf{4}$. $-2 + 1 = -1$ et $(-1)^2 = \mathbf{1}$.
\end{reponse}
\q{2.b}{Expression de $g(x)$.}
\begin{reponse}
$\mathbf{g(x) = (x + 1)^2}$.
\end{reponse}
'''),
dict(id='2022-pols-4b', s='pols', ex=4, titre='Exercice 4 -- Trois fonctions, questions 3 et 4', theme='Images, antécédents, équation x² = a, courbes',
     consigne='Traite les questions 3 et 4 (f est donnée par le tableau et g(x) = (x + 1)²).', regions=[(4, 734, 790), (5, 120, 168), (5, 366, 680)], s3=19, n3=[12, 32], s4=None, n4=None,
     corr=r'''
\q{3.a}{Image de 3 par $h$.}
\begin{reponse}
$h(3) = 2 \times 3^2 - 3 = 18 - 3 = \mathbf{15}$.
\end{reponse}
\q{3.b}{Image de $-4$ par $h$.}
\begin{reponse}
$h(-4) = 2 \times (-4)^2 - 3 = 32 - 3 = \mathbf{29}$.
\end{reponse}
\q{3.c}{Antécédents de 5 par $h$.}
\begin{reponse}
$2x^2 - 3 = 5 \iff 2x^2 = 8 \iff x^2 = 4$ : il y a deux antécédents, \textbf{2 et $-2$}.
\end{reponse}
\q{4}{Associer chaque courbe à sa fonction.}
\begin{reponse}
Représentation 1 : $f$ (c'est une droite et l'image de 0 est 1). Représentation 2 : $h$ (elle passe par $(0\,;-3)$). Représentation 3 : $g$ (elle passe par $(0\,;1)$ et $(-1\,;0)$).
\end{reponse}
'''),
dict(id='2022-pols-5a', s='pols', ex=5, titre='Exercice 5 -- L’urne, questions 1 et 3', theme='Probabilités, fréquence',
     consigne='Traite les questions 1 et 3.', regions=[(5, 677, 790), (6, 120, 205), (6, 442, 488)], s3=22, n3=[], s4=20, n4=[47, 48],
     corr=r'''
\q{1.a}{Probabilité de gagner 10 points.}
\begin{reponse}
L'urne contient $20 + 10 + 5 + 1 = 36$ boules, dont 1 noire : $p = \mathbf{\dfrac{1}{36}}$.
\end{reponse}
\q{1.b}{Probabilité de gagner plus de 3 points.}
\begin{reponse}
Il faut une boule noire ou bleue : $p = \dfrac{1 + 5}{36} = \mathbf{\dfrac{1}{6}}$.
\end{reponse}
\q{1.c}{2 points ou 5 points ?}
\begin{reponse}
Il y a 10 boules vertes et 5 bleues : il a \textbf{plus de chances de gagner 2 points}.
\end{reponse}
\q{3}{Nombre de joueurs ayant 10 points sur 1\,000.}
\begin{reponse}
Sur un grand nombre de tirages, la fréquence est proche de la probabilité : $1\,000 \times \dfrac{1}{36} \approx 28$. On peut estimer à \textbf{environ 28} le nombre de joueurs à 10 points.
\end{reponse}
'''),
dict(id='2022-pols-5b', s='pols', ex=5, titre='Exercice 5 -- L’urne, question 2', theme='Moyenne, médiane, fréquence',
     consigne='Traite seulement la question 2.', regions=[(5, 677, 790), (6, 203, 440)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{2.a}{Moyenne des scores.}
\begin{reponse}
Total : $5 \times 1 + 5 \times 2 + 3 \times 5 + 2 \times 10 = 50$ points. Moyenne : $50 \div 15 \approx \mathbf{3{,}3}$ points.
\end{reponse}
\q{2.b}{Médiane.}
\begin{reponse}
Rangés : 1 ; 1 ; 1 ; 1 ; 1 ; 2 ; 2 ; \textbf{2} ; 2 ; 2 ; 5 ; 5 ; 5 ; 10 ; 10. Il y a 15 scores : la médiane est le 8\ieme{}, \textbf{2 points}.
\end{reponse}
\q{2.c}{Fréquence du score 10.}
\begin{reponse}
2 joueurs sur 15 : $\mathbf{\dfrac{2}{15}} \approx 0{,}13$.
\end{reponse}
'''),
]
