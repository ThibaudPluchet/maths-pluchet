# DNB Polynésie, juin 2022
SOURCE = ('dnb_polynesie_juin_2022.pdf', 'Polynésie, juin 2022')
QH = [(1, 194, 248)]
def aff(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2022-polj-1q{n}', s='polj', ex=1, titre=f'Exercice 1 -- Vrai ou faux, affirmation {n}', theme=theme,
                consigne=f'Traite seulement l’affirmation {n}.', regions=QH + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
aff(1, [(1, 248, 339)], 5, [], 18, [42, 43], 'Calculs avec des fractions', r'''
\q{1}{Affirmation 1 : $-\frac{7}{5} + \frac{6}{5} \times \frac{4}{7} = -\frac{4}{35}$.}
\begin{reponse}
La multiplication est prioritaire :
\[ -\frac{7}{5} + \frac{6}{5} \times \frac{4}{7} = -\frac{7}{5} + \frac{24}{35} = -\frac{49}{35} + \frac{24}{35} = -\frac{25}{35} = -\frac{5}{7}. \]
L'affirmation est \textbf{fausse}.
\end{reponse}
'''),
aff(2, [(1, 337, 548)], 20, [], 19, [45], 'Réciproque du théorème de Thalès', r'''
\q{2}{Affirmation 2 : (GE) et (MR) sont parallèles.}
\begin{reponse}
Les points $G$, $A$, $R$ et $E$, $A$, $M$ sont alignés dans le même ordre.
\[ \frac{AM}{AE} = \frac{3}{4{,}2} = \frac{5}{7} \qquad\text{et}\qquad \frac{AR}{AG} = \frac{7}{9{,}8} = \frac{5}{7}. \]
D'après la réciproque du théorème de Thalès, $(GE) \parallel (MR)$ : l'affirmation est \textbf{vraie}.
\end{reponse}
'''),
aff(3, [(1, 548, 568)], 24, [], 6, [14], 'Décomposition en facteurs premiers', r'''
\q{3}{Affirmation 3 : $126 = 2 \times 7 \times 9$ est la décomposition en facteurs premiers.}
\begin{reponse}
9 n'est pas premier : $126 = 2 \times 3^2 \times 7$. L'affirmation est \textbf{fausse}.
\end{reponse}
'''),
aff(4, [(1, 568, 620)], 14, [22], None, None, 'Ratio', r'''
\q{4}{Affirmation 4 : il faut 210 mL d'huile pour 330 mL de sauce.}
\begin{reponse}
$1 + 3 + 7 = 11$ parts ; une part vaut $330 \div 11 = 30$ mL ; l'huile représente $7 \times 30 = 210$ mL. L'affirmation est \textbf{vraie}.
\end{reponse}
'''),
dict(id='2022-polj-2a', s='polj', ex=2, titre='Exercice 2 -- La salle de sport, questions 1 et 2', theme='Proportionnalité, image et antécédent graphiques',
     consigne='Traite les questions 1 et 2.', regions=[(1, 629, 716), (2, 120, 535)], s3=8, n3=[12], s4=None, n4=None,
     corr=r'''
\q{1}{Le tarif « liberté » est-il proportionnel ?}
\begin{reponse}
\textbf{Oui} : sa représentation $(d_1)$ est une droite qui passe par l'origine.
\end{reponse}
\q{2.a}{Image de 5 par $f$.}
\begin{reponse}
Je lis l'ordonnée du point de $(d_1)$ d'abscisse 5 : $f(5) = \mathbf{25}$.
\end{reponse}
\q{2.b}{Antécédent de 10 par $g$.}
\begin{reponse}
Je lis l'abscisse du point de $(d_2)$ d'ordonnée 10 : \textbf{1}.
\end{reponse}
'''),
dict(id='2022-polj-2b', s='polj', ex=2, titre='Exercice 2 -- La salle de sport, questions 3 et 4', theme='Lecture graphique, fonction linéaire',
     consigne='Traite les questions 3 et 4.', regions=[(1, 629, 716), (2, 120, 372), (2, 534, 598)], s3=17, n3=[26], s4=None, n4=None,
     corr=r'''
\q{3}{Tarif le plus avantageux.}
\begin{reponse}
Les droites se coupent pour 3 heures. Pour \textbf{moins de 3 h}, le tarif « liberté » est le plus avantageux ; pour 3 h, les deux se valent ; pour \textbf{plus de 3 h}, c'est le tarif « abonné ».
\end{reponse}
\q{4}{Prix pour 15 heures au tarif « liberté ».}
\begin{reponse}
$f$ est linéaire et $f(3) = 15$, donc $f(x) = 5x$. $f(15) = 5 \times 15 = \mathbf{75}$ €.
\end{reponse}
'''),
dict(id='2022-polj-3a', s='polj', ex=3, titre='Exercice 3 -- Les briques de jus, partie A', theme='Médiane, étendue, probabilité, pourcentage',
     consigne='Traite la partie A.', regions=[(2, 608, 792), (3, 120, 248)], s3=23, n3=[], s4=20, n4=[24, 34, 47],
     corr=r'''
\q{1}{Médiane et interprétation.}
\begin{reponse}
Il y a 24 briques : la médiane est la moyenne des 12\ieme{} et 13\ieme{} volumes. Les effectifs cumulés sont 1 ; 3 ; 7 ; 11 ; 13 ; … : les 12\ieme{} et 13\ieme{} valent 350. La médiane est \textbf{350 mL} : au moins la moitié des briques contient 350 mL ou moins, au moins la moitié 350 mL ou plus.
\end{reponse}
\q{2}{Étendue.}
\begin{reponse}
$357 - 344 = \mathbf{13}$ mL.
\end{reponse}
\q{3}{Probabilité qu'une brique contienne exactement 350 mL.}
\begin{reponse}
$p = \dfrac{2}{24} = \mathbf{\dfrac{1}{12}}$.
\end{reponse}
\q{4}{Pourcentage de briques vendables.}
\begin{reponse}
Seules les briques de 344, 356 et 357 mL sont hors des limites : $24 - 3 = 21$ briques. $\dfrac{21}{24} = 0{,}875$, soit \textbf{87,5 \%}.
\end{reponse}
'''),
dict(id='2022-polj-3b', s='polj', ex=3, titre='Exercice 3 -- Les briques de jus, partie B', theme='Aire, volume du pavé droit',
     consigne='Traite la partie B.', regions=[(2, 608, 628), (3, 258, 416)], s3=21, n3=[], s4=2, n4=[],
     corr=r'''
\q{1}{Aire de la base.}
\begin{reponse}
$6{,}4 \times 5 = \mathbf{32}$ cm$^2$.
\end{reponse}
\q{2}{Hauteur pour un volume de 400 cm$^3$.}
\begin{reponse}
$V = 32 \times h = 400$, donc $h = 400 \div 32 = \mathbf{12{,}5}$ cm.
\end{reponse}
'''),
dict(id='2022-polj-4a', s='polj', ex=4, titre='Exercice 4 -- Le programme de calcul, question 1', theme='Programme de calcul, nombres relatifs',
     consigne='Traite seulement la question 1.', regions=[(3, 415, 742)], s3=1, n3=[], s4=1, n4=[1, 2],
     corr=r'''
\q{1.a}{Avec 7.}
\begin{reponse}
$7 + 5 = 12$ et $7 - 5 = 2$ ; $12 \times 2 = 24$ ; $24 + 25 = \mathbf{49}$.
\end{reponse}
\q{1.b}{Avec $-4$.}
\begin{reponse}
$-4 + 5 = 1$ et $-4 - 5 = -9$ ; $1 \times (-9) = -9$ ; $-9 + 25 = \mathbf{16}$.
\end{reponse}
'''),
dict(id='2022-polj-4b', s='polj', ex=4, titre='Exercice 4 -- Le programme de calcul, question 2', theme='Double distributivité, preuve',
     consigne='Traite seulement la question 2.', regions=[(3, 415, 708), (3, 740, 792), (4, 120, 184)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{2.a}{Résultat en fonction de $x$.}
\begin{reponse}
$\mathbf{(x + 5)(x - 5) + 25}$.
\end{reponse}
\q{2.b}{Développer et réduire $(x+5)(x-5)$.}
\begin{reponse}
$(x + 5)(x - 5) = x^2 - 5x + 5x - 25 = \mathbf{x^2 - 25}$.
\end{reponse}
\q{2.c}{Sarah a-t-elle raison ?}
\begin{reponse}
$(x + 5)(x - 5) + 25 = x^2 - 25 + 25 = x^2$ : le résultat est toujours le carré du nombre de départ. \textbf{Sarah a raison}.
\end{reponse}
'''),
dict(id='2022-polj-5a', s='polj', ex=5, titre='Exercice 5 -- La chenille du centre Pompidou, question 1', theme='Équations, longueurs',
     consigne='Traite seulement la question 1.', regions=[(4, 195, 556)], s3=7, n3=[], s4=16, n4=[38, 39],
     corr=r'''
\q{1.a}{Vérifier que $p = 12$ m.}
\begin{reponse}
La longueur totale compte 6 passerelles de 12,5 m et 5 profondeurs $p$ : $6 \times 12{,}5 + 5p = 135$, donc $75 + 5p = 135$, $5p = 60$ et $p = 12$ m.
\end{reponse}
\q{1.b}{Hauteur $h$.}
\begin{reponse}
Les 5 escalators montent de 32 m : $h = 32 \div 5 = \mathbf{6{,}4}$ m.
\end{reponse}
'''),
dict(id='2022-polj-5b', s='polj', ex=5, titre='Exercice 5 -- La chenille du centre Pompidou, question 2', theme='Théorème de Pythagore, trigonométrie',
     consigne='Traite seulement la question 2.', regions=[(4, 195, 505), (4, 555, 648)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{2.a}{Longueur ST.}
\begin{reponse}
Le triangle $RST$ est rectangle en $R$. D'après le théorème de Pythagore :
\[ ST^2 = SR^2 + RT^2 = 12^2 + 6{,}4^2 = 144 + 40{,}96 = 184{,}96 \qquad\text{donc}\qquad ST = \sqrt{184{,}96} = 13{,}6 \text{ m}. \]
\end{reponse}
\q{2.b}{Angle $\widehat{RST}$.}
\begin{reponse}
$\tan\widehat{RST} = \dfrac{RT}{SR} = \dfrac{6{,}4}{12}$, donc $\widehat{RST} \approx \mathbf{28^\circ}$.
\end{reponse}
'''),
dict(id='2022-polj-5c', s='polj', ex=5, titre='Exercice 5 -- La chenille du centre Pompidou, question 3', theme='Algorithmique (Scratch)',
     consigne='Traite seulement la question 3 (ST = 13,6 m ; complète les lignes sur ta copie).', regions=[(4, 195, 505), (4, 646, 722), (5, 120, 275), (7, 120, 770)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{3}{Lignes 6, 7, 9 et 10.}
\begin{reponse}
Ligne 6 : répéter \textbf{5} fois. Ligne 7 : avancer de \textbf{12,5}.
Ligne 9 : avancer de \textbf{13,6}. Ligne 10 : tourner \textbf{à droite} de \textbf{28} degrés (pour revenir à l'horizontale).
\end{reponse}
'''),
]
