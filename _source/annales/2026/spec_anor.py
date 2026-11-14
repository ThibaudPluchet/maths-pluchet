# DNB Amérique du Nord, 3 juin 2026
SOURCE = ('dnb_ameri_nord_juin_2026.pdf', 'Amérique du Nord, 3 juin 2026')
QA = (1, 393, 496)
def q(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2026-anor-a{n}', s='anor', ex=0, titre=f'Automatismes, question {n}', theme=theme,
                regions=[QA] + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
q(1, [(1, 496, 544)], 5, [], 12, [28], 'Addition de fractions', r'''
\q{1}{Calculer $A = \frac23 + \frac34$.}
\begin{reponse}
$A = \dfrac{8}{12} + \dfrac{9}{12} = \mathbf{\dfrac{17}{12}}$.
\end{reponse}
'''),
q(2, [(1, 544, 580)], 14, [], 15, [34], 'Pourcentage de réduction', r'''
\q{2}{Prix de 45 € après une réduction de 10 \%.}
\begin{reponse}
10 \% de 45 €, c'est 4,50 € : $45 - 4{,}50 = \mathbf{40{,}50}$ € \quad (ou $45 \times 0{,}9$).
\end{reponse}
'''),
q(3, [(1, 580, 768)], 2, [], 4, [], 'Nature d’un quadrilatère', r'''
\q{3}{Nature du quadrilatère.}
\begin{reponse}
Le codage indique seulement que les côtés opposés sont de même longueur : c'est un parallélogramme, mais rien ne dit que deux côtés consécutifs sont égaux ni qu'il a un angle droit. \textbf{Réponse D}.
\end{reponse}
'''),
q(4, [(2, 135, 173)], 7, [], 16, [38], 'Équation du premier degré', r'''
\q{4}{Résoudre $5x - 15 = 20$.}
\begin{reponse}
$5x = 20 + 15 = 35$, donc $x = 35 \div 5 = \mathbf{7}$.
\end{reponse}
'''),
q(5, [(2, 173, 326)], 8, [], 9, [], 'Repérage dans le plan', r'''
\q{5}{Abscisse de A et coordonnées de B.}
\begin{reponse}
a. L'abscisse de $A$ est $\mathbf{-2}$. \quad b. $B\,(\mathbf{-2\,;\,-1})$.
\end{reponse}
'''),
q(6, [(2, 326, 376)], 23, [], 11, [24], 'Médiane', r'''
\q{6}{Médiane de la série.}
\begin{reponse}
Dans l'ordre : 1 ; 3 ; 3 ; 8 ; \textbf{11} ; 12 ; 12 ; 19 ; 25. Il y a 9 valeurs : la médiane est la $5^{\text{e}}$, \textbf{11}.
\end{reponse}
'''),
q(7, [(2, 376, 576)], 15, [24], None, None, 'Trigonométrie (longueur)', r'''
\q{7}{Formule qui donne AB.}
\begin{reponse}
Dans le triangle rectangle en $A$, $[AB]$ est le côté adjacent à l'angle de $60^\circ$ et $[BC]$ l'hypoténuse : $\cos 60^\circ = \dfrac{AB}{5}$, donc $AB = \mathbf{5 \times \cos(60)}$.
\end{reponse}
'''),
q(8, [(2, 576, 604)], 24, [], 6, [13], 'Diviseurs', r'''
\q{8}{Un diviseur de 387 autre que 1 et 387.}
\begin{reponse}
$3 + 8 + 7 = 18$ est divisible par 3 (et par 9) : $387 = 3 \times 129 = 9 \times 43$. Par exemple \textbf{3} (ou 9, 43, 129).
\end{reponse}
'''),
dict(id='2026-anor-1', s='anor', ex=1, titre='Exercice 1 -- Deux triangles', theme='Réciproque de Pythagore, aire, parallélisme, Thalès, angles',
     regions=[(3, 280, 554)], s3=13, n3=[], s4=19, n4=[22, 32],
     corr=r'''
\q{1}{Montrer que AED est rectangle en E.}
\begin{reponse}
Le plus grand côté est $[AD]$. \quad $AD^2 = 7{,}3^2 = 53{,}29$ \quad et \quad $AE^2 + ED^2 = 5{,}5^2 + 4{,}8^2 = 30{,}25 + 23{,}04 = 53{,}29$.\\
$AD^2 = AE^2 + ED^2$ : d'après la réciproque du théorème de Pythagore, $AED$ est rectangle en $E$.
\end{reponse}
\q{2}{Aire du triangle AED.}
\begin{reponse}
$\dfrac{AE \times ED}{2} = \dfrac{5{,}5 \times 4{,}8}{2} = \mathbf{13{,}2}$ cm².
\end{reponse}
\q{3}{Pourquoi (BC) et (ED) sont-elles parallèles ?}
\begin{reponse}
$(BC) \perp (BE)$ (triangle $ABC$ rectangle en $B$) et $(ED) \perp (BE)$ (question 1) : deux droites perpendiculaires à une même droite sont parallèles.
\end{reponse}
\q{4}{Valeur exacte de AB.}
\begin{reponse}
Les droites $(BE)$ et $(CD)$ sont sécantes en $A$ et $(BC) \parallel (ED)$. D'après le théorème de Thalès :
\[ \frac{AB}{AE} = \frac{BC}{ED} \qquad\text{soit}\qquad \frac{AB}{5{,}5} = \frac{7{,}2}{4{,}8} \qquad\text{donc}\qquad AB = \frac{5{,}5 \times 7{,}2}{4{,}8} = \mathbf{8{,}25} \text{ cm}. \]
\end{reponse}
\q{5}{Mesure de l'angle $\widehat{ADE}$.}
\begin{reponse}
$(BC) \parallel (ED)$ coupées par la sécante $(CD)$ : $\widehat{ACB}$ et $\widehat{ADE}$ sont alternes-internes, donc égaux. $\widehat{ADE} \approx \mathbf{49^\circ}$.
\end{reponse}
'''),
dict(id='2026-anor-2a', s='anor', ex=2, titre='Exercice 2 -- Les fonctions f et g, questions 1 à 4', theme='Image, antécédent, tableur, lecture graphique',
     consigne='Traite les questions 1 à 4.', regions=[(4, 136, 737)], s3=17, n3=[5, 13, 14, 26], s4=None, n4=None,
     corr=r'''
\q{1}{Calculer $f(-4)$.}
\begin{reponse}
$f(-4) = (-4 - 1)(-4 + 3) = (-5) \times (-1) = \mathbf{5}$.
\end{reponse}
\q{2}{Antécédent de 2 par $g$.}
\begin{reponse}
$2x + 1 = 2 \iff 2x = 1 \iff x = \mathbf{0{,}5}$.
\end{reponse}
\q{3.a}{Formule en B3.}
\begin{reponse}
\texttt{=2*B1+1}.
\end{reponse}
\q{3.b}{Une solution de $f(x) = g(x)$ (tableau).}
\begin{reponse}
Colonne D : $f(2) = g(2) = 5$, donc \textbf{2} est une solution.
\end{reponse}
\q{4.a}{Associer chaque fonction à sa courbe.}
\begin{reponse}
$g$ est affine : sa représentation est une droite, $\mathcal{C}_2$. La courbe $\mathcal{C}_1$ (qui n'est pas une droite) représente $f$.
\end{reponse}
\q{4.b}{Solutions de $f(x) = g(x)$ (lecture).}
\begin{reponse}
Les courbes se coupent aux points d'abscisses \textbf{$-2$ et 2}.
\end{reponse}
'''),
dict(id='2026-anor-2b', s='anor', ex=2, titre='Exercice 2 -- Les fonctions f et g, question 5', theme='Double distributivité, équation x² = a',
     consigne='Traite la question 5.', regions=[(4, 136, 178), (4, 737, 766)], s3=19, n3=[18, 32], s4=None, n4=None,
     corr=r'''
\q{5}{Lola a-t-elle raison ?}
\begin{reponse}
$(x - 1)(x + 3) = x^2 + 3x - x - 3 = x^2 + 2x - 3$.
\[ x^2 + 2x - 3 = 2x + 1 \iff x^2 - 3 - 1 = 0 \iff x^2 - 4 = 0. \]
Les deux équations sont équivalentes : \textbf{oui}, elle a raison (solutions $-2$ et 2).
\end{reponse}
'''),
dict(id='2026-anor-3a', s='anor', ex=3, titre='Exercice 3 -- L’intelligence artificielle, partie A', theme='Pourcentages, probabilités',
     consigne='Traite la partie A.', regions=[(5, 136, 536)], s3=22, n3=[], s4=20, n4=[34, 47],
     corr=r'''
\q{1}{Images de la catégorie « Autres ».}
\begin{reponse}
$50\,000 - 28\,000 - 12\,000 - 8\,000 = \mathbf{2\,000}$ images.
\end{reponse}
\q{2}{Objets du quotidien reconnus.}
\begin{reponse}
$28\,000 \times 0{,}9 = \mathbf{25\,200}$ images.
\end{reponse}
\q{3}{Pourcentage de réussite pour les véhicules.}
\begin{reponse}
$\dfrac{5\,600}{8\,000} = 0{,}7$, soit \textbf{70 \%}.
\end{reponse}
\q{4}{Probabilité d'un « Objet du quotidien ».}
\begin{reponse}
$\dfrac{28\,000}{50\,000} = \mathbf{0{,}56}$.
\end{reponse}
'''),
dict(id='2026-anor-3b', s='anor', ex=3, titre='Exercice 3 -- L’intelligence artificielle, partie B', theme='Puissances de 10, écriture scientifique',
     consigne='Traite la partie B.', regions=[(5, 136, 210), (5, 536, 790)], s3=25, n3=[], s4=13, n4=[30, 31],
     corr=r'''
\q{5}{Consommations en Wh.}
\begin{reponse}
IA : $82\,000 \times 10^9 = 8{,}2 \times 10^4 \times 10^9 = \mathbf{8{,}2 \times 10^{13}}$ Wh.\\
Collège : $200\,000 \times 10^3 = 2 \times 10^5 \times 10^3 = \mathbf{2 \times 10^{8}}$ Wh.
\end{reponse}
\q{6}{Nombre de collèges alimentés pendant un an.}
\begin{reponse}
$\dfrac{8{,}2 \times 10^{13}}{2 \times 10^{8}} = 4{,}1 \times 10^5 = \mathbf{410\,000}$ collèges.
\end{reponse}
\q{7}{Nombre d'années pour les 7 100 collèges.}
\begin{reponse}
$410\,000 \div 7\,100 \approx 57{,}7$ : environ \textbf{58 ans}.
\end{reponse}
'''),
dict(id='2026-anor-4', s='anor', ex=4, titre='Exercice 4 -- Carrés et triangles (Scratch), questions 1 et 2', theme='Algorithmique (Scratch)',
     consigne='Traite les questions 1 et 2.', regions=[(6, 136, 482)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Coordonnées du lutin après le bloc 1.}
\begin{reponse}
$(0\,;\,0)$.
\end{reponse}
\q{2}{Valeurs de A, B, C et D.}
\begin{reponse}
Carré : A $= \mathbf{4}$ côtés, B $= \mathbf{90}$ degrés. Triangle équilatéral : C $= \mathbf{3}$ côtés, D $= \mathbf{120}$ degrés (angle extérieur $180^\circ - 60^\circ$).
\end{reponse}
'''),
]
