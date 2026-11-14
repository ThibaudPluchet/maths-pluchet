# DNB Amérique du Sud, 16 novembre 2023
SOURCE = ('dnb_ameri_sud_nov_2023.pdf', 'Amérique du Sud, 16 novembre 2023')
E3 = (2, 596, 635)
PARTS = [
dict(id='2023-asud-1a', s='asud', ex=1, titre='Exercice 1 -- Les triangles, questions 1 et 2', theme='Réciproque de Pythagore, trigonométrie',
     consigne='Traite les questions 1 et 2.', regions=[(1, 184, 370)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{1}{Montrer que EFG est rectangle en F.}
\begin{reponse}
Le plus grand côté est $[EG]$. \quad $EG^2 = 30^2 = 900$ \quad et \quad $EF^2 + FG^2 = 18^2 + 24^2 = 324 + 576 = 900$.\\
$EG^2 = EF^2 + FG^2$ : d'après la réciproque du théorème de Pythagore, $EFG$ est rectangle en $F$.
\end{reponse}
\q{2}{Mesure de l'angle $\widehat{EGF}$.}
\begin{reponse}
Dans le triangle $EFG$ rectangle en $F$, $[EF]$ est le côté opposé à $\widehat{EGF}$ et $[FG]$ le côté adjacent :
\[ \tan\widehat{EGF} = \frac{EF}{FG} = \frac{18}{24} = 0{,}75 \qquad\text{donc}\qquad \widehat{EGF} \approx \mathbf{37^\circ}. \]
\end{reponse}
'''),
dict(id='2023-asud-1b', s='asud', ex=1, titre='Exercice 1 -- Les triangles, questions 3 à 5', theme='Triangles semblables, agrandissement',
     consigne='Traite les questions 3 à 5 (le triangle EFG est rectangle en F).', regions=[(1, 184, 320), (1, 369, 497)], s3=10, n3=[16], s4=None, n4=None,
     corr=r'''
\q{3}{Montrer que EGF et LGH sont semblables.}
\begin{reponse}
$\widehat{EGF} = \widehat{LGH}$ (donnée) et $\widehat{EFG} = \widehat{LHG} = 90^\circ$. Deux triangles qui ont deux angles égaux deux à deux sont semblables.
\end{reponse}
\q{4}{Coefficient d'agrandissement de EFG à LHG.}
\begin{reponse}
Les côtés $[GF]$ et $[GH]$ se correspondent (ils relient le sommet commun $G$ à l'angle droit) : $k = \dfrac{GH}{GF} = \dfrac{38{,}4}{24} = \mathbf{1{,}6}$.
\end{reponse}
\q{5}{Périmètre du triangle LGH.}
\begin{reponse}
Périmètre de $EFG$ : $18 + 24 + 30 = 72$ cm. Les longueurs sont multipliées par 1,6 : $72 \times 1{,}6 = \mathbf{115{,}2}$ cm.
\end{reponse}
'''),
dict(id='2023-asud-2a', s='asud', ex=2, titre='Exercice 2 -- La feuille découpée, questions 1 à 3', theme='Aires, expression littérale',
     consigne='Traite les questions 1 à 3.', regions=[(1, 497, 790), (2, 128, 192)], s3=1, n3=[], s4=8, n4=[20],
     corr=r'''
\q{1}{Aire du triangle AEF (AE = 3 cm).}
\begin{reponse}
Le triangle est rectangle isocèle en $A$ : $AF = AE = 3$ cm. \quad $\mathcal{A} = \dfrac{3 \times 3}{2} = \mathbf{4{,}5}$ cm².
\end{reponse}
\q{2}{Aire du polygone.}
\begin{reponse}
$10 \times 8 - 4 \times 4{,}5 = 80 - 18 = \mathbf{62}$ cm².
\end{reponse}
\q{3.a}{Aire de AEF en fonction de $x$.}
\begin{reponse}
$\dfrac{x \times x}{2} = \dfrac{x^2}{2}$.
\end{reponse}
\q{3.b}{Aire du polygone en fonction de $x$.}
\begin{reponse}
$80 - 4 \times \dfrac{x^2}{2} = 80 - 2x^2$.
\end{reponse}
'''),
dict(id='2023-asud-2b', s='asud', ex=2, titre='Exercice 2 -- La feuille découpée, questions 4 et 5', theme='Tableur, lecture graphique, équation x² = a',
     consigne='Traite les questions 4 et 5.', regions=[(1, 497, 648), (1, 727, 790), (2, 192, 596)], s3=19, n3=[13, 26, 32], s4=None, n4=None,
     corr=r'''
\q{4}{Formule en B2.}
\begin{reponse}
\texttt{=80-2*B1*B1} \quad (ou \texttt{=80-2*B1\^{}2}).
\end{reponse}
\q{5.a}{La fonction $f$ est-elle affine ?}
\begin{reponse}
\textbf{Non} : sa représentation n'est pas une droite (et $f(x)$ contient $x^2$).
\end{reponse}
\q{5.b}{Valeur approchée de AE pour une aire de 60 cm².}
\begin{reponse}
On lit environ \textbf{3,2} cm.
\end{reponse}
\q{5.c}{Valeur exacte.}
\begin{reponse}
$80 - 2x^2 = 60 \iff 2x^2 = 20 \iff x^2 = 10$. Une longueur est positive : $x = \mathbf{\sqrt{10}}$ cm ($\approx 3{,}16$).
\end{reponse}
'''),
dict(id='2023-asud-3a', s='asud', ex=3, titre='Exercice 3 -- Vrai ou faux, affirmation 1', theme='Proportionnalité',
     regions=[E3, (2, 635, 718)], s3=14, n3=[], s4=5, n4=[11],
     corr=r'''
\q{1}{« Le prix est proportionnel au nombre de baguettes. »}
\begin{reponse}
$\dfrac{1{,}10}{1} = \dfrac{2{,}20}{2} = \dfrac{3{,}30}{3} = 1{,}10$, mais $\dfrac{4}{4} = 1$. Les quotients ne sont pas tous égaux : \textbf{faux}.
\end{reponse}
'''),
dict(id='2023-asud-3b', s='asud', ex=3, titre='Exercice 3 -- Vrai ou faux, affirmation 2', theme='Droite graduée, nombres décimaux',
     regions=[E3, (2, 718, 790), (3, 128, 163)], s3=5, n3=[], s4=12, n4=[],
     corr=r'''
\q{2}{« L'abscisse de A est un nombre décimal. »}
\begin{reponse}
L'unité, de 1 à 2, est partagée en 8 : chaque graduation vaut $\dfrac18 = 0{,}125$. $A$ est 2 graduations après 2 : $2 + 2 \times 0{,}125 = 2{,}25$.\\
2,25 est un nombre décimal : \textbf{vrai}.
\end{reponse}
'''),
dict(id='2023-asud-3c', s='asud', ex=3, titre='Exercice 3 -- Vrai ou faux, affirmation 3', theme='Multiples (engrenage)',
     regions=[E3, (3, 163, 262)], s3=24, n3=[], s4=6, n4=[13],
     corr=r'''
\q{3}{« Même position au bout de 6 tours de A et 4 tours de B. »}
\begin{reponse}
Roue A : $6 \times 8 = 48$ dents ; roue B : $4 \times 12 = 48$ dents. Le même nombre de dents est passé et chaque roue a fait un nombre entier de tours : \textbf{vrai}.\\
\small (Cela arrive même dès 24 dents : 3 tours de A et 2 tours de B.)
\end{reponse}
'''),
dict(id='2023-asud-3d', s='asud', ex=3, titre='Exercice 3 -- Vrai ou faux, affirmation 4', theme='Double distributivité',
     regions=[E3, (3, 262, 325)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{4}{$(x + 8)(2x - 1) = 2x^2 - (8 - 15x)$ ?}
\begin{reponse}
$(x + 8)(2x - 1) = 2x^2 - x + 16x - 8 = 2x^2 + 15x - 8$ \quad et \quad $2x^2 - (8 - 15x) = 2x^2 - 8 + 15x$.\\
Les deux expressions sont égales : \textbf{vrai}.
\end{reponse}
'''),
dict(id='2023-asud-4a', s='asud', ex=4, titre='Exercice 4 -- Les bougies, question 1', theme='Volume du cylindre, masse',
     consigne='Traite la question 1.', regions=[(3, 324, 612)], s3=21, n3=[34], s4=None, n4=None,
     corr=r'''
\q{1.a}{Volume d'une bougie.}
\begin{reponse}
$V = \pi \times 3^2 \times 12 = 108\pi \approx 339$ cm³.
\end{reponse}
\q{1.b}{Masse de cire pour une bougie.}
\begin{reponse}
Volume de cire : $108\pi \times \dfrac{9}{10} \approx 305{,}4$ cm³. Masse : $305{,}4 \times 0{,}7 \approx \mathbf{214}$ g.
\end{reponse}
'''),
dict(id='2023-asud-4b', s='asud', ex=4, titre='Exercice 4 -- Les bougies, questions 2 et 3', theme='Diagramme circulaire, pourcentages, moyenne',
     consigne='Traite les questions 2 et 3.', regions=[(3, 324, 361), (3, 612, 790)], s3=23, n3=[], s4=11, n4=[23, 24],
     corr=r'''
\q{2}{Pourcentage de bougies à la lavande.}
\begin{reponse}
Le secteur « Vanille » est un angle droit : $\dfrac{90}{360} = 25$ \%. Les secteurs « Miel » et « Jasmin » ont le même codage : 22 \% chacun.\\
Lavande : $100 - 25 - 22 - 22 = \mathbf{31}$ \%.
\end{reponse}
\q{3}{Bougies à produire en mars.}
\begin{reponse}
Moyenne de 7\,900 sur 3 mois : $3 \times 7\,900 = 23\,700$ bougies. En mars : $23\,700 - 6\,500 - 8\,000 = \mathbf{9\,200}$ bougies.
\end{reponse}
'''),
dict(id='2023-asud-5a', s='asud', ex=5, titre='Exercice 5 -- La roue et l’urne, questions 1 à 4', theme='Probabilités, nombres premiers',
     consigne='Traite les questions 1 à 4.', regions=[(4, 146, 569)], s3=22, n3=[], s4=20, n4=[14, 47],
     corr=r'''
\q{1}{Les 12 issues.}
\begin{reponse}
12 ; 13 ; 14 ; 22 ; 23 ; 24 ; 32 ; 33 ; 34 ; 42 ; 43 ; 44 (elles sont équiprobables).
\end{reponse}
\q{2}{Probabilité d'un nombre impair.}
\begin{reponse}
13 ; 23 ; 33 ; 43 : $p = \dfrac{4}{12} = \dfrac13$.
\end{reponse}
\q{3.a}{Probabilité de A (premier et inférieur à 30).}
\begin{reponse}
Inférieurs à 30 : 12, 13, 14, 22, 23, 24 ; parmi eux, seuls 13 et 23 sont premiers. $p(A) = \dfrac{2}{12} = \dfrac16$.
\end{reponse}
\q{3.b}{Probabilité de l'évènement contraire.}
\begin{reponse}
$1 - \dfrac16 = \dfrac56$.
\end{reponse}
\q{4}{Probabilité d'un multiple de 11.}
\begin{reponse}
22 ; 33 ; 44 : $p = \dfrac{3}{12} = \dfrac14 = 0{,}25$.
\end{reponse}
'''),
dict(id='2023-asud-5b', s='asud', ex=5, titre='Exercice 5 -- La roue et l’urne, question 5 (Scratch)', theme='Algorithmique (Scratch), simulation',
     consigne='Traite la question 5.', regions=[(4, 146, 420), (4, 569, 790), (5, 128, 284)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{5.a}{Ligne 5.}
\begin{reponse}
Nombre aléatoire entre \textbf{2} et \textbf{4} (les boules de l'urne).
\end{reponse}
\q{5.b}{Ligne 6.}
\begin{reponse}
Si \textbf{Chiffre des dizaines} $=$ \textbf{Chiffre des unités} alors\ldots\ (un multiple de 11 a deux chiffres égaux).
\end{reponse}
\q{5.c}{Pourquoi 0,23 et non 0,25 ?}
\begin{reponse}
0,23 est une fréquence observée sur 100 parties simulées au hasard : elle fluctue autour de la probabilité 0,25 et n'est pas forcément égale à celle-ci.
\end{reponse}
'''),
dict(id='2023-asud-1rec', s='asud', ex=1, extra=True, titre='Exercice 1 -- Le triangle EFG est-il rectangle ?', theme='Réciproque du théorème de Pythagore',
     consigne='Traite seulement la question 1.', regions=[(1, 184, 336)], s3=13, n3=[], s4=14, n4=[32],
     corr=r'''
\q{1}{Montrer que EFG est rectangle en F.}
\begin{reponse}
Le plus grand côté est $[EG]$. \quad $EG^2 = 30^2 = 900$ \quad et \quad $EF^2 + FG^2 = 18^2 + 24^2 = 324 + 576 = 900$.\\
$EG^2 = EF^2 + FG^2$ : d'après la réciproque du théorème de Pythagore, le triangle $EFG$ est rectangle en $F$.
\end{reponse}
'''),
]
