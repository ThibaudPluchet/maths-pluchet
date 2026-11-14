# DNB Amérique du Sud, novembre 2022
SOURCE = ('dnb_ameri_sud_nov_2022.pdf', 'Amérique du Sud, novembre 2022')
QH = [(1, 195, 250)]
def aff(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2022-asud-1q{n}', s='asud', ex=1, titre=f'Exercice 1 -- Vrai ou faux, affirmation {n}', theme=theme,
                consigne=f'Traite seulement l’affirmation {n}.', regions=QH + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
aff(1, [(1, 254, 356)], 22, [], 20, [47], 'Probabilités', r'''
\q{1}{Affirmation 1 : une boule bleue est plus probable dans l'urne B.}
\begin{reponse}
Urne A : $\dfrac{8}{20} = 0{,}4$. Urne B : $\dfrac{11}{11 + 14} = \dfrac{11}{25} = 0{,}44$. $0{,}44 > 0{,}4$ : l'affirmation est \textbf{vraie}.
\end{reponse}
'''),
aff(2, [(1, 355, 389)], 23, [], 11, [24], 'Médiane', r'''
\q{2}{Affirmation 2 : la médiane est 11.}
\begin{reponse}
Rangées : 3 ; 7 ; 7 ; 11 ; \textbf{12} ; 12 ; 14 ; 14 ; 14. Il y a 9 valeurs : la médiane est la 5\ieme{}, 12. L'affirmation est \textbf{fausse}.
\end{reponse}
'''),
aff(3, [(1, 388, 421)], 14, [], 15, [35, 36], 'Vitesse moyenne', r'''
\q{3}{Affirmation 3 : la vitesse moyenne est 11,25 km/h.}
\begin{reponse}
3 h 20 min $= 3 + \dfrac{20}{60} = \dfrac{10}{3}$ h. $v = 36 \div \dfrac{10}{3} = 36 \times \dfrac{3}{10} = 10{,}8$ km/h. L'affirmation est \textbf{fausse}.
\end{reponse}
'''),
aff(4, [(1, 420, 776)], 8, [5, 12], None, None, 'Images par deux fonctions', r'''
\q{4}{Affirmation 4 : $f(-1)$ est inférieure à $g(-1)$.}
\begin{reponse}
$f(-1) = -4 \times (-1) - 5 = 4 - 5 = -1$. Sur le graphique, $g(-1) = -1$. Les deux images sont égales : l'affirmation est \textbf{fausse}.
\end{reponse}
'''),
aff(5, [(1, 772, 798)], 12, [18], None, None, 'Double distributivité', r'''
\q{5}{Affirmation 5 : $(x+5)^2 - 4 = (x+1)(x+9)$.}
\begin{reponse}
$(x + 5)^2 - 4 = x^2 + 10x + 25 - 4 = x^2 + 10x + 21$ et $(x + 1)(x + 9) = x^2 + 9x + x + 9 = x^2 + 10x + 9$.
Les expressions sont différentes (par exemple pour $x = 0$ : 21 et 9). L'affirmation est \textbf{fausse}.
\end{reponse}
'''),
aff(6, [(2, 120, 172)], 2, [], 4, [9, 10], 'Théorème de Pythagore', r'''
\q{6}{Affirmation 6 : les diagonales mesurent $\sqrt{72}$ m.}
\begin{reponse}
Une diagonale est l'hypoténuse d'un triangle rectangle isocèle de côtés 6 m. D'après le théorème de Pythagore : $d^2 = 6^2 + 6^2 = 72$, donc $d = \sqrt{72}$ m. L'affirmation est \textbf{vraie}.
\end{reponse}
'''),
dict(id='2022-asud-2a', s='asud', ex=2, titre='Exercice 2 -- L’énergie solaire, questions 1 et 2', theme='Lecture graphique, pourcentages',
     consigne='Traite les questions 1 et 2.', regions=[(2, 176, 708)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{1}{Production du pays E.}
\begin{reponse}
Environ \textbf{10 TWh} (un peu moins : environ 9,8 TWh).
\end{reponse}
\q{2.a}{Part des pays A et B.}
\begin{reponse}
$47{,}5 + 23{,}7 = 71{,}2$ TWh et $\dfrac{71{,}2}{131{,}8} \approx 0{,}54$ : environ \textbf{54 \%}.
\end{reponse}
\q{2.b}{Pourcentage d'augmentation entre 2018 et 2019.}
\begin{reponse}
$\dfrac{131{,}8 - 122{,}3}{122{,}3} = \dfrac{9{,}5}{122{,}3} \approx 0{,}078$ : une hausse d'environ \textbf{7,8 \%}.
\end{reponse}
'''),
dict(id='2022-asud-2b', s='asud', ex=2, titre='Exercice 2 -- L’énergie solaire, question 3', theme='Tableur, comparaison de décimaux',
     consigne='Traite seulement la question 3.', regions=[(2, 176, 240), (2, 708, 790), (3, 120, 340)], s3=1, n3=[], s4=1, n4=[],
     corr=r'''
\q{3.a}{Énergies en hausse chaque année.}
\begin{reponse}
\textbf{L'éolien} ($24{,}1 < 27{,}8 < 34{,}1$), \textbf{le solaire} ($9{,}2 < 10{,}2 < 11{,}6$) et \textbf{les bioénergies} ($9{,}5 < 9{,}7 < 9{,}9$).
\end{reponse}
\q{3.b}{Formule en B9.}
\begin{reponse}
\texttt{=SOMME(B3:B8)}.
\end{reponse}
'''),
dict(id='2022-asud-3a', s='asud', ex=3, titre='Exercice 3 -- Le triangle rectangle, questions 1 et 4', theme='Angles, triangle isocèle, triangle équilatéral',
     consigne='Traite les questions 1 et 4.', regions=[(3, 343, 587), (3, 620, 640)], s3=2, n3=[], s4=4, n4=[],
     corr=r'''
\q{1}{Mesure de l'angle $\widehat{DBC}$.}
\begin{reponse}
$DB = CB$ : le triangle $DBC$ est isocèle en $B$, donc $\widehat{BDC} = \widehat{BCD} = 30^\circ$ et $\widehat{DBC} = 180^\circ - 30^\circ - 30^\circ = \mathbf{120^\circ}$.
\end{reponse}
\q{4}{Nature du triangle ABD.}
\begin{reponse}
$A$, $B$, $C$ sont alignés : $\widehat{DBA} = 180^\circ - 120^\circ = 60^\circ$. De plus $\widehat{ADB} = 90^\circ - \widehat{BDC} = 90^\circ - 30^\circ = 60^\circ$.
Le troisième angle vaut $180^\circ - 60^\circ - 60^\circ = 60^\circ$ : le triangle $ABD$ est \textbf{équilatéral}.
\end{reponse}
'''),
dict(id='2022-asud-3b', s='asud', ex=3, titre='Exercice 3 -- Le triangle rectangle, questions 2 et 3', theme='Trigonométrie (calcul de longueurs)',
     consigne='Traite les questions 2 et 3.', regions=[(3, 343, 566), (3, 586, 622)], s3=15, n3=[24], s4=None, n4=None,
     corr=r'''
\q{2}{Montrer que AD = 5 cm.}
\begin{reponse}
Dans le triangle $ADC$ rectangle en $D$ : $\sin\widehat{ACD} = \dfrac{AD}{AC}$, donc $AD = 10 \times \sin 30^\circ = 10 \times 0{,}5 = 5$ cm.
\end{reponse}
\q{3}{Longueur DC.}
\begin{reponse}
$\cos\widehat{ACD} = \dfrac{DC}{AC}$, donc $DC = 10 \times \cos 30^\circ \approx \mathbf{8{,}7}$ cm.
\end{reponse}
'''),
dict(id='2022-asud-4', s='asud', ex=4, titre='Exercice 4 -- Le logo', theme='Algorithmique (Scratch), rotation',
     regions=[(3, 645, 700), (4, 120, 582), (5, 120, 536)], s3=0, n3=[17], s4=None, n4=None,
     corr=r'''
\q{1}{Transformation qui fait passer d'un motif au suivant.}
\begin{reponse}
Une \textbf{rotation} (de centre le point de départ).
\end{reponse}
\q{2}{Proposition qui trace le motif.}
\begin{reponse}
La \textbf{proposition 2} : elle trace d'abord la hampe, puis le losange du bon côté.
\end{reponse}
\q{3}{Boucle « répéter » complétée.}
\begin{reponse}
répéter \textbf{5} fois ; Motif ; aller à x: \textbf{0} y: \textbf{0} ; tourner de \textbf{72} degrés ($360 \div 5 = 72$).
\end{reponse}
\q{4}{Où placer « ajouter 10 à la couleur du stylo » ?}
\begin{reponse}
Dans la boucle, par exemple après l'instruction \textbf{7}.
\end{reponse}
'''),
dict(id='2022-asud-5a', s='asud', ex=5, titre='Exercice 5 -- Le carré potager, question 1', theme='Calculs de prix',
     consigne='Traite seulement la question 1.', regions=[(5, 541, 620), (6, 120, 568)], s3=14, n3=[], s4=5, n4=[11],
     corr=r'''
\q{1.a}{Nombre de planches.}
\begin{reponse}
Chaque côté a 30 cm de haut, soit 2 planches de 15 cm de 1,20 m : il faut 8 morceaux de 1,20 m. Une planche de 2,50 m donne 2 morceaux ($2 \times 1{,}20 = 2{,}40$) : il faut \textbf{4 planches}.
\end{reponse}
\q{1.b}{Budget hors terre.}
\begin{reponse}
4 équerres : $4 \times 2{,}90 = 11{,}60$ € ; 4 planches : $4 \times 5{,}60 = 22{,}40$ € ; $4 \times 8 = 32$ vis, soit 1 lot : 5,70 €.
Total : $11{,}60 + 22{,}40 + 5{,}70 = \mathbf{39{,}70}$ €.
\end{reponse}
'''),
dict(id='2022-asud-5b', s='asud', ex=5, titre='Exercice 5 -- Le carré potager, question 2', theme='Volume du pavé droit, conversions',
     consigne='Traite seulement la question 2.', regions=[(5, 541, 620), (6, 120, 516), (6, 568, 648)], s3=21, n3=[], s4=15, n4=[36],
     corr=r'''
\q{2}{Sept sacs suffisent-ils ?}
\begin{reponse}
Hauteur de terre : $\dfrac{2}{3} \times 30 = 20$ cm $= 2$ dm. Volume : $11{,}8 \times 11{,}8 \times 2 = 278{,}48$ dm$^3$ $= 278{,}48$ L.
7 sacs contiennent $7 \times 40 = 280$ L et $280 > 278{,}48$ : \textbf{oui}, c'est suffisant.
\end{reponse}
'''),
]
