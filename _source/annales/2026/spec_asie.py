# DNB Asie, 15 juin 2026
SOURCE = ('dnb_asie_juin_2026.pdf', 'Asie, 15 juin 2026')
QA = (1, 205, 288)
def q(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2026-asie-a{n}', s='asie', ex=0, titre=f'Automatismes, question {n}', theme=theme,
                regions=[QA] + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
q(1, [(1, 288, 355)], 25, [], 13, [31], 'Écriture scientifique', r'''
\q{1}{Écriture scientifique de 45\,310.}
\begin{reponse}
$45\,310 = 4{,}531 \times 10\,000 = \mathbf{4{,}531 \times 10^4}$, \textbf{réponse B}.
\end{reponse}
'''),
q(2, [(1, 355, 440)], 12, [19], None, None, 'Identité remarquable', r'''
\q{2}{Développer $(4x-3)(4x+3)$.}
\begin{reponse}
J'utilise $(a-b)(a+b) = a^2 - b^2$ avec $a = 4x$ et $b = 3$ : $(4x)^2 - 3^2 = \mathbf{16x^2 - 9}$, \textbf{réponse C}.
\end{reponse}
'''),
q(3, [(1, 440, 536)], 21, [], 2, [], 'Volume du pavé droit', r'''
\q{3}{Volume du pavé droit.}
\begin{reponse}
$V = 4{,}5 \times 4 \times 10 = \mathbf{180}$ cm$^3$, \textbf{réponse A}.
\end{reponse}
'''),
q(4, [(1, 536, 665)], 24, [], 6, [13], 'Divisibilité par 9', r'''
\q{4}{Divisibilité de 2\,025 et 2\,026 par 9.}
\begin{reponse}
$2 + 0 + 2 + 5 = 9$ : 2\,025 est divisible par 9. $2 + 0 + 2 + 6 = 10$ : 2\,026 ne l'est pas. \textbf{Réponse B}.
\end{reponse}
'''),
q(5, [(1, 665, 718)], 14, [], 15, [35], 'Vitesse moyenne', r'''
\q{5}{Vitesse moyenne pour 9 km en 45 min.}
\begin{reponse}
9 km en 45 min, donc 3 km en 15 min et $3 \times 4 = 12$ km en 60 min : \textbf{12 km/h}.
\end{reponse}
'''),
q(6, [(2, 128, 271)], 22, [], 20, [47], 'Probabilités', r'''
\q{6}{Probabilité de gagner un casque audio.}
\begin{reponse}
Les 10 secteurs sont de même taille et 2 portent « casque » : $p = \dfrac{2}{10} = \mathbf{\dfrac{1}{5}}$.
\end{reponse}
'''),
q(7, [(2, 271, 321)], 14, [], 15, [34], 'Pourcentage de baisse', r'''
\q{7}{Prix de 60 € après une baisse de 10 \%.}
\begin{reponse}
$60 \times 0{,}9 = \mathbf{54}$ €.
\end{reponse}
'''),
q(8, [(2, 321, 462)], 2, [], 4, [], 'Angles d’un triangle', r'''
\q{8}{Mesure de l'angle $\widehat{BAC}$.}
\begin{reponse}
Le triangle $ABC$ est rectangle en $C$ et la somme de ses angles vaut $180^\circ$ : $\widehat{BAC} = 180^\circ - 90^\circ - 40^\circ = \mathbf{50^\circ}$.
\end{reponse}
'''),
q(9, [(2, 462, 758)], 23, [], 11, [24], 'Effectif, médiane', r'''
\q{9.a}{Nombre d'élèves.}
\begin{reponse}
$3 + 4 + 4 + 5 + 5 + 3 + 2 + 1 = \mathbf{27}$ élèves.
\end{reponse}
\q{9.b}{Note médiane.}
\begin{reponse}
L'effectif 27 est impair : la médiane est la 14\ieme{} note rangée dans l'ordre croissant ($27 = 13 + 1 + 13$).
Les notes 7 et 8 regroupent $3 + 4 = 7$ élèves, la note 10 mène à 11 élèves et la note 11 à 16 élèves. La 14\ieme{} note vaut 11 : la médiane est \textbf{11}.
\end{reponse}
'''),
dict(id='2026-asie-1a', s='asie', ex=1, titre='Exercice 1 -- Les forfaits, question 1', theme='Calculs de prix',
     consigne='Traite seulement la question 1.', regions=[(3, 236, 386)], s3=14, n3=[], s4=9, n4=[21],
     corr=r'''
\q{1}{Offre la plus intéressante au bout de 24 mois.}
\begin{reponse}
Offre A : $175 + 16 \times 24 = 175 + 384 = 559$ €. Offre B : $23 \times 24 = 552$ €.
$552 < 559$ : l'\textbf{offre B} est la plus intéressante.
\end{reponse}
'''),
dict(id='2026-asie-1b', s='asie', ex=1, titre='Exercice 1 -- Les forfaits, question 2', theme='Fonctions affines, équation',
     consigne='Traite la question 2.', regions=[(3, 236, 368), (3, 384, 516)], s3=17, n3=[26], s4=None, n4=None,
     corr=r'''
\q{2.a}{Associer chaque fonction à son offre.}
\begin{reponse}
$f$ correspond à l'offre \textbf{A} (175 € puis 16 € par mois) et $g$ à l'offre \textbf{B}.
\end{reponse}
\q{2.b}{Nombre de mois pour payer le même prix.}
\begin{reponse}
Je résous $f(x) = g(x)$ :
\[ 175 + 16x = 23x \iff 175 = 7x \iff x = 25. \]
Au bout de \textbf{25 mois}, les deux offres coûtent le même prix ($23 \times 25 = 575$ €).
\end{reponse}
\q{2.c}{Est-on encore dans la période d'engagement ?}
\begin{reponse}
\textbf{Non} : $25 > 24$, la période d'engagement de 24 mois est terminée.
\end{reponse}
'''),
dict(id='2026-asie-2a', s='asie', ex=2, titre='Exercice 2 -- Le gobelet, questions 1 à 3', theme='Théorème de Pythagore, théorème de Thalès',
     consigne='Traite les questions 1 à 3.', regions=[(4, 130, 398)], s3=9, n3=[], s4=10, n4=[10, 22],
     corr=r'''
\q{1}{Montrer que OA = 8 cm.}
\begin{reponse}
Le triangle $OAD$ est rectangle en $A$, d'hypoténuse $[OD]$. D'après le théorème de Pythagore :
\[ OA^2 = OD^2 - AD^2 = 8{,}2^2 - 1{,}8^2 = 67{,}24 - 3{,}24 = 64 \qquad\text{donc}\qquad OA = \sqrt{64} = 8 \text{ cm}. \]
\end{reponse}
\q{2}{Justifier que (BC) et (AD) sont parallèles.}
\begin{reponse}
Les droites $(BC)$ et $(AD)$ sont toutes les deux perpendiculaires à la droite $(OB)$ : elles sont donc parallèles.
\end{reponse}
\q{3}{Calculer OB.}
\begin{reponse}
Les points $O$, $A$, $B$ et $O$, $D$, $C$ sont alignés et $(AD) \parallel (BC)$. D'après le théorème de Thalès :
\[ \frac{OA}{OB} = \frac{OD}{OC} = \frac{AD}{BC} \qquad\text{donc}\qquad \frac{8}{OB} = \frac{1{,}8}{4{,}5} \qquad\text{et}\qquad OB = \frac{8 \times 4{,}5}{1{,}8} = \mathbf{20} \text{ cm}. \]
\end{reponse}
'''),
dict(id='2026-asie-2b', s='asie', ex=2, titre='Exercice 2 -- Le gobelet, question 4', theme='Volume du cône',
     consigne='Traite la question 4 (OA = 8 cm et OB = 20 cm).', regions=[(4, 398, 708)], s3=21, n3=[35], s4=17, n4=[40],
     corr=r'''
\q{4.a}{Volume du grand cône.}
\begin{reponse}
Le rayon de sa base est $BC = 4{,}5$ cm et sa hauteur $OB = 20$ cm :
\[ V = \frac{\pi \times 4{,}5^2 \times 20}{3} = 135\pi \approx \mathbf{424} \text{ cm}^3. \]
\end{reponse}
\q{4.b}{Volume du gobelet.}
\begin{reponse}
Le petit cône a pour rayon $AD = 1{,}8$ cm et pour hauteur $OA = 8$ cm :
\[ V' = \frac{\pi \times 1{,}8^2 \times 8}{3} = 8{,}64\pi \approx 27 \text{ cm}^3. \]
Le gobelet est le grand cône privé du petit : $135\pi - 8{,}64\pi = 126{,}36\pi \approx \mathbf{397}$ cm$^3$.
\end{reponse}
'''),
dict(id='2026-asie-3a', s='asie', ex=3, titre='Exercice 3 -- Deux programmes, questions 1 à 4', theme='Programme de calcul, tableur, expression littérale',
     consigne='Traite les questions 1 à 4.', regions=[(5, 130, 716)], s3=1, n3=[], s4=8, n4=[18, 19, 20],
     corr=r'''
\q{1}{Programme A avec 5.}
\begin{reponse}
$5^2 = 25$ puis $3 \times 25 = 75$ ; $7 \times 5 = 35$ ; $75 + 35 = 110$ ; $110 - 6 = \mathbf{104}$.
\end{reponse}
\q{2}{Formule saisie en B2.}
\begin{reponse}
\texttt{= 3 * A2 * A2 + 7 * A2 - 6} (le carré de A2 s'écrit A2*A2).
\end{reponse}
\q{3}{Valeur de départ qui donne 0.}
\begin{reponse}
D'après le tableur, $\mathbf{-3}$ donne 0.
\end{reponse}
\q{4}{Expression du programme A.}
\begin{reponse}
$\mathbf{3x^2 + 7x - 6}$.
\end{reponse}
'''),
dict(id='2026-asie-3b', s='asie', ex=3, titre='Exercice 3 -- Deux programmes, questions 5 à 8', theme='Double distributivité, équation produit',
     consigne='Traite les questions 5 à 8 (le programme A donne 3x² + 7x − 6).', regions=[(5, 130, 400), (6, 125, 472)], s3=19, n3=[18, 32], s4=None, n4=None,
     corr=r'''
\q{5}{Programme B avec 5.}
\begin{reponse}
$3 \times 5 - 2 = 13$ ; $5 + 3 = 8$ ; $13 \times 8 = \mathbf{104}$.
\end{reponse}
\q{6}{Expression du programme B.}
\begin{reponse}
$\mathbf{(3x - 2)(x + 3)}$.
\end{reponse}
\q{7}{Mathis a-t-il raison ?}
\begin{reponse}
Je développe avec la double distributivité :
\[ (3x - 2)(x + 3) = 3x^2 + 9x - 2x - 6 = 3x^2 + 7x - 6. \]
C'est l'expression du programme A : \textbf{Mathis a raison}.
\end{reponse}
\q{8}{Résoudre $(3x-2)(x+3) = 0$.}
\begin{reponse}
Un produit est nul si et seulement si l'un de ses facteurs est nul :
\[ 3x - 2 = 0 \iff x = \frac{2}{3} \qquad\text{ou}\qquad x + 3 = 0 \iff x = -3. \]
Les programmes A et B donnent 0 pour $\mathbf{x = -3}$ et $\mathbf{x = \dfrac{2}{3}}$.
\end{reponse}
'''),
dict(id='2026-asie-4a', s='asie', ex=4, titre='Exercice 4 -- Triangle et carré, question 1', theme='Angles (triangle équilatéral, carré)',
     consigne='Traite seulement la question 1.', regions=[(6, 478, 684)], s3=2, n3=[], s4=4, n4=[],
     corr=r'''
\q{1}{Justifier que $\widehat{EAD} = 30^\circ$.}
\begin{reponse}
$ABF$ est équilatéral : $\widehat{FAB} = 60^\circ$. $ABCD$ est un carré : $\widehat{BAD} = 90^\circ$.
$F$, $A$ et $E$ sont alignés, donc $\widehat{FAE} = 180^\circ$ et
\[ \widehat{EAD} = 180^\circ - 60^\circ - 90^\circ = \mathbf{30^\circ}. \]
\end{reponse}
'''),
dict(id='2026-asie-4b', s='asie', ex=4, titre='Exercice 4 -- Triangle et carré, questions 2 et 3', theme='Algorithmique (Scratch)',
     consigne='Traite les questions 2 et 3.', regions=[(6, 478, 665), (6, 684, 742), (7, 125, 795)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{2}{Valeurs de J, K, M et N.}
\begin{reponse}
4 cm correspondent à 40 pas : $J = \mathbf{40}$ et $M = \mathbf{40}$.
Pour tracer un angle de $60^\circ$, le lutin tourne de $180^\circ - 60^\circ$ : $K = \mathbf{120}$. Pour un angle droit : $N = \mathbf{90}$.
\end{reponse}
\q{3}{Figure obtenue.}
\begin{reponse}
Chaque bloc ramène le lutin à son point de départ dans la même direction. Il avance ensuite de 50 pas, plus que le côté (40 pas) : il reste un espace de 10 pas entre deux motifs. Après chaque motif il tourne de $30^\circ$ : 6 fois 2 rotations de $30^\circ$ font 360°, la figure se referme en cercle. C'est la \textbf{figure 3}.
\end{reponse}
'''),
]
