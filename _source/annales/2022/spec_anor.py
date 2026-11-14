# DNB Amérique du Nord, juin 2022
SOURCE = ('dnb_ameri_nord_juin_2022.pdf', 'Amérique du Nord, 3 juin 2022')
QH = [(2, 136, 247)]
def qcm(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2022-anor-2q{n}', s='anor', ex=2, titre=f'Exercice 2 -- QCM, question {n}', theme=theme,
                consigne=f'Traite seulement la question {n}.', regions=QH + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
dict(id='2022-anor-1a', s='anor', ex=1, titre='Exercice 1 -- Deux triangles, questions 1 et 2', theme='Théorème de Pythagore, théorème de Thalès',
     consigne='Traite les questions 1 et 2.', regions=[(1, 249, 604)], s3=9, n3=[], s4=10, n4=[10, 22],
     corr=r'''
\q{1}{Démontrer que HS = 12 cm.}
\begin{reponse}
Le triangle $HMS$ est rectangle en $H$, d'hypoténuse $[MS]$. D'après le théorème de Pythagore :
\[ HS^2 = MS^2 - MH^2 = 13^2 - 5^2 = 169 - 25 = 144 \qquad\text{donc}\qquad HS = \sqrt{144} = 12 \text{ cm}. \]
\end{reponse}
\q{2}{Calculer AT.}
\begin{reponse}
$(HS)$ et $(AT)$ sont perpendiculaires à la même droite $(HT)$ : elles sont parallèles. Les points $A$, $M$, $S$ et $T$, $M$, $H$ sont alignés. D'après le théorème de Thalès :
\[ \frac{MH}{MT} = \frac{MS}{MA} = \frac{HS}{AT} \qquad\text{donc}\qquad \frac{5}{7} = \frac{12}{AT} \qquad\text{et}\qquad AT = \frac{12 \times 7}{5} = \mathbf{16{,}8} \text{ cm}. \]
\end{reponse}
'''),
dict(id='2022-anor-1b', s='anor', ex=1, titre='Exercice 1 -- Deux triangles, question 3', theme='Trigonométrie',
     consigne='Traite seulement la question 3.', regions=[(1, 249, 571), (1, 603, 624)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{3}{Mesure de l'angle $\widehat{HMS}$.}
\begin{reponse}
Dans le triangle $HMS$ rectangle en $H$, $[MH]$ est le côté adjacent à $\widehat{HMS}$ et $[MS]$ l'hypoténuse :
\[ \cos\widehat{HMS} = \frac{MH}{MS} = \frac{5}{13} \qquad\text{donc}\qquad \widehat{HMS} \approx \mathbf{67^\circ}. \]
\end{reponse}
'''),
dict(id='2022-anor-1c', s='anor', ex=1, titre='Exercice 1 -- Deux triangles, questions 4 et 5', theme='Homothétie, agrandissement et aires',
     consigne='Traite les questions 4 et 5.', regions=[(1, 249, 571), (1, 623, 758)], s3=21, n3=[30, 37], s4=None, n4=None,
     corr=r'''
\q{4}{Transformation qui transforme MHS en MAT.}
\begin{reponse}
Les deux triangles ont la même forme mais pas la même taille : c'est \textbf{une homothétie} (de centre $M$, de rapport $-1{,}4$).
\end{reponse}
\q{5}{L'aire de MAT est-elle 1,4 fois plus grande ?}
\begin{reponse}
$MAT$ est un agrandissement de $MHS$ de rapport 1,4 : les aires sont multipliées par $1{,}4^2 = 1{,}96$. L'affirmation est \textbf{fausse}.
\end{reponse}
'''),
dict(id='2022-anor-1hom', s='anor', ex=1, titre='Exercice 1 -- Deux triangles, question 4', theme='Homothétie', extra=True,
     consigne='Traite seulement la question 4.', regions=[(1, 249, 571), (1, 623, 714)], s3=18, n3=[30], s4=None, n4=None,
     corr=r'''
\q{4}{Transformation qui transforme MHS en MAT.}
\begin{reponse}
Les deux triangles ont la même forme mais pas la même taille, et ils sont de part et d'autre de $M$ : c'est \textbf{une homothétie} de centre $M$ (de rapport $-1{,}4$).
\end{reponse}
'''),
qcm(1, [(2, 246, 315)], 22, [], 20, [47], 'Probabilités', r'''
\q{1}{Probabilité d'obtenir un numéro inférieur ou égal à 5.}
\begin{reponse}
5 issues favorables sur 20 : $\dfrac{5}{20} = \mathbf{\dfrac{1}{4}}$, \textbf{réponse B}.
\end{reponse}
'''),
qcm(2, [(2, 315, 438)], 14, [22], None, None, 'Ratio', r'''
\q{2}{Quantité d'eau pour 560 mL de boisson.}
\begin{reponse}
La boisson compte $1 + 7 = 8$ parts : une part vaut $560 \div 8 = 70$ mL. L'eau représente $7 \times 70 = \mathbf{490}$ mL, \textbf{réponse D}.
\end{reponse}
'''),
qcm(3, [(2, 437, 474)], 17, [26], None, None, 'Fonction linéaire', r'''
\q{3}{Fonction linéaire telle que $f\left(\frac{4}{5}\right) = 1$.}
\begin{reponse}
$f(x) = ax$ avec $a \times \dfrac{4}{5} = 1$, donc $a = \dfrac{5}{4}$ : $f(x) = \dfrac{5}{4}x$, \textbf{réponse C}.
\end{reponse}
'''),
qcm(4, [(2, 474, 516)], 24, [], 6, [14], 'Décomposition en facteurs premiers', r'''
\q{4}{Décomposition de 195.}
\begin{reponse}
$195 = 3 \times 5 \times 13$ et 3, 5, 13 sont premiers, \textbf{réponse B} (39 et 65 ne sont pas premiers).
\end{reponse}
'''),
qcm(5, [(2, 515, 633)], 21, [], 2, [], 'Volume d’un prisme', r'''
\q{5}{Volume du prisme droit.}
\begin{reponse}
La base est un triangle rectangle d'aire $\dfrac{5 \times 3}{2} = 7{,}5$ cm$^2$ ; la hauteur est 8 cm : $V = 7{,}5 \times 8 = \mathbf{60}$ cm$^3$, \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2022-anor-3a', s='anor', ex=3, titre='Exercice 3 -- La pratique physique, question 1', theme='Pourcentage',
     consigne='Traite seulement la question 1.', regions=[(2, 649, 790)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{1}{Nombre d'adolescents qui ne respectent pas la recommandation.}
\begin{reponse}
$0{,}81 \times 1\,600\,000 = \mathbf{1\,296\,000}$ adolescents.
\end{reponse}
'''),
dict(id='2022-anor-3b', s='anor', ex=3, titre='Exercice 3 -- La pratique physique, questions 2 et 3', theme='Étendue, médiane, moyenne, durées',
     consigne='Traite les questions 2 et 3.', regions=[(2, 649, 728), (3, 125, 401)], s3=23, n3=[], s4=11, n4=[24, 36],
     corr=r'''
\q{2.a}{Étendue des durées.}
\begin{reponse}
La plus grande durée est 1 h 40 min, la plus petite 0 min : l'étendue est \textbf{1 h 40 min}.
\end{reponse}
\q{2.b}{Une médiane.}
\begin{reponse}
Rangées : 0 ; 15 ; 15 ; 30 ; 30 ; 40 ; \textbf{50} ; \textbf{60} ; 60 ; 60 ; 60 ; 90 ; 90 ; 100 (en min).
Il y a 14 valeurs : une médiane est entre la 7\ieme{} et la 8\ieme{}, par exemple $\dfrac{50 + 60}{2} = \mathbf{55}$ \textbf{min}.
\end{reponse}
\q{3.a}{L'objectif n'est pas atteint.}
\begin{reponse}
Total : $0 + 2 \times 15 + 2 \times 30 + 40 + 50 + 4 \times 60 + 2 \times 90 + 100 = 700$ min.
Moyenne : $700 \div 14 = 50$ min, moins d'une heure : l'objectif \textbf{n'est pas atteint}.
\end{reponse}
\q{3.b}{Durée minimale sur les 7 jours suivants.}
\begin{reponse}
Sur 21 jours, il faut au moins $21 \times 60 = 1\,260$ min. Il en manque $1\,260 - 700 = \mathbf{560}$ \textbf{min}, soit 9 h 20 min.
\end{reponse}
'''),
dict(id='2022-anor-4a', s='anor', ex=4, titre='Exercice 4 -- Le jeu de hasard, questions 1 et 2', theme='Algorithmique (Scratch)',
     consigne='Traite les questions 1 et 2.', regions=[(3, 414, 522), (4, 125, 581)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Motif obtenu par le bloc « rectangle ».}
\begin{reponse}
Un rectangle de $60 \div 20 = 3$ cm de large (horizontalement) et $80 \div 20 = 4$ cm de haut.
\end{reponse}
\q{2}{Distance $d$ entre deux rectangles.}
\begin{reponse}
Le lutin revient au coin de départ du rectangle, puis avance de 100 pas ; le rectangle mesure 60 pas de large : $d = 100 - 60 = \mathbf{40}$ \textbf{pas}.
\end{reponse}
'''),
dict(id='2022-anor-4b', s='anor', ex=4, titre='Exercice 4 -- Le jeu de hasard, questions 3 à 6', theme='Probabilités (deux épreuves), Scratch',
     consigne='Traite les questions 3 à 6.', regions=[(3, 414, 522), (4, 125, 474), (4, 579, 736)], s3=22, n3=[39], s4=None, n4=None,
     corr=r'''
\q{3}{Probabilité que le premier motif soit une croix.}
\begin{reponse}
Le nombre aléatoire vaut 1 ou 2 avec la même chance : $p = \mathbf{\dfrac{1}{2}}$.
\end{reponse}
\q{4}{Les 8 affichages possibles.}
\begin{reponse}
En notant X une croix et R un rectangle : XXX, XXR, XRX, XRR, RXX, RXR, RRX, RRR.
\end{reponse}
\q{5}{Probabilité que le joueur gagne.}
\begin{reponse}
Deux affichages sur 8 sont gagnants (XXX et RRR) : $p = \dfrac{2}{8} = \mathbf{\dfrac{1}{4}}$.
\end{reponse}
\q{6}{Compléter l'instruction de la ligne 5.}
\begin{reponse}
\textbf{nombre aléatoire entre 1 et 3 = 1} : la croix a 1 chance sur 3 et le rectangle 2 chances sur 3.
\end{reponse}
'''),
dict(id='2022-anor-5a', s='anor', ex=5, titre='Exercice 5 -- Le programme de calcul, partie A', theme='Programme de calcul, tableur, expression littérale',
     consigne='Traite la partie A.', regions=[(4, 753, 772), (5, 125, 582)], s3=1, n3=[], s4=8, n4=[18, 19, 20],
     corr=r'''
\q{1}{Avec 15 au départ.}
\begin{reponse}
$15^2 = 225$ ; $225 + 15 = \mathbf{240}$.
\end{reponse}
\q{2}{Formule saisie en B2.}
\begin{reponse}
\texttt{=A2*A2+A2} (ou \texttt{=A2\^{}2+A2}).
\end{reponse}
\q{3}{Expression en fonction de $x$.}
\begin{reponse}
$\mathbf{x^2 + x}$.
\end{reponse}
'''),
dict(id='2022-anor-5b', s='anor', ex=5, titre='Exercice 5 -- Le programme de calcul, partie B', theme='Factorisation, preuve, nombres pairs',
     consigne='Traite la partie B (le programme donne x² + x).', regions=[(4, 753, 772), (5, 125, 340), (5, 588, 724)], s3=16, n3=[25], s4=8, n4=[7, 20],
     corr=r'''
\q{2}{Vérification avec 9.}
\begin{reponse}
$9^2 + 9 = 90$ et $9 \times 10 = 90$ : l'affirmation est vraie pour 9.
\end{reponse}
\q{3}{Démonstration dans le cas général.}
\begin{reponse}
Je factorise par $x$ : $x^2 + x = x \times x + x \times 1 = x(x + 1)$. C'est le produit du nombre de départ par l'entier qui le suit.
\end{reponse}
\q{4}{Le résultat est toujours pair.}
\begin{reponse}
Parmi deux entiers qui se suivent, $x$ et $x + 1$, l'un est pair. Leur produit est donc un multiple de 2 : le résultat est \textbf{toujours pair}.
\end{reponse}
'''),
]
