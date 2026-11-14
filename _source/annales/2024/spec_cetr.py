# DNB Centres étrangers, juin 2024
SOURCE = ('dnb_centres_etrangers_juin_2024.pdf', 'Centres étrangers, juin 2024')
QCM = (1, 132, 208)
PARTS = [
dict(id='2024-cetr-1q1', s='cetr', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Écriture scientifique',
     regions=[QCM, (1, 208, 242)], s3=25, n3=[], s4=13, n4=[31],
     corr=r'''
\q{1}{Écriture scientifique de $0{,}193 \times 10^{-100}$.}
\begin{reponse}
$0{,}193 = 1{,}93 \times 10^{-1}$, donc $0{,}193 \times 10^{-100} = 1{,}93 \times 10^{-1} \times 10^{-100} = \mathbf{1{,}93 \times 10^{-101}}$.
\end{reponse}
'''),
dict(id='2024-cetr-1q2', s='cetr', ex=1, titre='Exercice 1 -- QCM, question 2', theme='Vitesse moyenne',
     regions=[QCM, (1, 242, 298)], s3=14, n3=[], s4=15, n4=[35],
     corr=r'''
\q{2}{Vitesse moyenne pour 480 km en 5 h 42 min.}
\begin{reponse}
42 min $= \dfrac{42}{60}$ h $= 0{,}7$ h, donc la durée est 5,7 h. \quad $v = \dfrac{480}{5{,}7} \approx \mathbf{84{,}2}$ km/h.
\end{reponse}
'''),
dict(id='2024-cetr-1q3', s='cetr', ex=1, titre='Exercice 1 -- QCM, question 3', theme='Probabilités',
     regions=[QCM, (1, 298, 489)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{3}{Peut-on obtenir une probabilité de $\frac35$ pour le nombre 2 ?}
\begin{reponse}
La roue a 15 secteurs : 8 portent le nombre 2, 6 le nombre 1, et un est effacé.\\
$\dfrac35 = \dfrac{9}{15}$ : il faut 9 secteurs « 2 ». \textbf{Oui, en écrivant le nombre 2} dans le secteur effacé.
\end{reponse}
'''),
dict(id='2024-cetr-1q4', s='cetr', ex=1, titre='Exercice 1 -- QCM, question 4', theme='Médiane, étendue, moyenne',
     regions=[QCM, (1, 489, 536)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{4}{Que représente le nombre 5 pour la liste 5 ; 1 ; 3 ; 10 ; 17 ; 11 ; 10 ?}
\begin{reponse}
Dans l'ordre : 1 ; 3 ; 5 ; \textbf{10} ; 10 ; 11 ; 17. La médiane est 10, l'étendue $17 - 1 = 16$, la moyenne $\dfrac{57}{7} \approx 8{,}1$.\\
Le nombre 5 ne représente \textbf{rien de particulier}.
\end{reponse}
'''),
dict(id='2024-cetr-1q5', s='cetr', ex=1, titre='Exercice 1 -- QCM, question 5', theme='Fractions',
     regions=[QCM, (1, 536, 620)], s3=5, n3=[], s4=18, n4=[42, 44],
     corr=r'''
\q{5}{Fraction du prix que représente un des trois paiements.}
\begin{reponse}
Il reste $1 - \dfrac15 = \dfrac45$ du prix, partagés en 3 paiements égaux : $\dfrac45 \times \dfrac13 = \mathbf{\dfrac{4}{15}}$.
\end{reponse}
'''),
dict(id='2024-cetr-2', s='cetr', ex=2, titre='Exercice 2 -- Les circuits d’entraînement', theme='Décomposition en facteurs premiers, multiples communs',
     regions=[(2, 132, 662)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{1}{Durées des circuits 1 et 2.}
\begin{reponse}
Circuit 1 : $5 \times (40 + 16) = 5 \times 56 = 280$ s. \quad Circuit 2 : $10 \times (30 + 5) = 10 \times 35 = 350$ s.
\end{reponse}
\q{2}{Décompositions de 280 et de 350.}
\begin{reponse}
$280 = 2 \times 140 = 2 \times 2 \times 70 = 2 \times 2 \times 2 \times 35 = \mathbf{2^3 \times 5 \times 7}$.\\
$350 = 2 \times 175 = 2 \times 5 \times 35 = \mathbf{2 \times 5^2 \times 7}$.
\end{reponse}
\q{3.a}{Où sont Camille et Dominique au bout de 2 800 s ?}
\begin{reponse}
$2\,800 = 10 \times 280$ : Camille a fait exactement 10 tours, elle est de nouveau au départ du circuit 1.\\
$2\,800 = 8 \times 350$ : Dominique a fait exactement 8 tours, elle est aussi \textbf{au départ} du circuit 2.
\end{reponse}
\q{3.b}{Première fois où elles se retrouvent ensemble au départ.}
\begin{reponse}
Il faut le plus petit nombre non nul multiple à la fois de 280 et de 350. Il doit contenir $2^3$, $5^2$ et $7$ :
\[ 2^3 \times 5^2 \times 7 = 8 \times 25 \times 7 = 1\,400 \text{ s} \qquad (1\,400 = 5 \times 280 = 4 \times 350). \]
$1\,400 = 23 \times 60 + 20$ : elles se retrouvent au bout de \textbf{23 min 20 s}.
\end{reponse}
'''),
dict(id='2024-cetr-3a', s='cetr', ex=3, titre='Exercice 3 -- Programme de calcul, partie A', theme='Programme de calcul, fractions, Scratch',
     consigne='Traite la partie A (le script est en annexe).', regions=[(3, 132, 596), (7, 195, 460)], s3=1, n3=[], s4=18, n4=[2, 19, 42],
     corr=r'''
\q{1}{Avec 5 comme nombre de départ.}
\begin{reponse}
$5 - 2 = 3$ et $5 + 1 = 6$ ; $3 \times 6 = 18$.
\end{reponse}
\q{2}{Avec $-\frac32$ comme nombre de départ.}
\begin{reponse}
$-\dfrac32 - 2 = -\dfrac32 - \dfrac42 = -\dfrac72$ \quad et \quad $-\dfrac32 + 1 = -\dfrac32 + \dfrac22 = -\dfrac12$.\\
Résultat : $\left(-\dfrac72\right) \times \left(-\dfrac12\right) = \mathbf{\dfrac74}$.
\end{reponse}
\q{3}{Compléter les lignes 3, 4 et 5 du script.}
\begin{reponse}
Ligne 3 : \texttt{mettre a à réponse - 2} ; ligne 4 : \texttt{mettre b à réponse + 1} ; ligne 5 : \texttt{dire a * b pendant 2 secondes} (déjà écrite).
\end{reponse}
'''),
dict(id='2024-cetr-3b', s='cetr', ex=3, titre='Exercice 3 -- La fonction g, partie B', theme='Double distributivité, équation produit, antécédents',
     consigne='Traite la partie B.', regions=[(3, 132, 465), (3, 596, 710), (4, 128, 414)], s3=19, n3=[13, 14, 18, 32], s4=None, n4=None,
     corr=r'''
\q{1}{Prouver que $(x - 2)(x + 1) = x^2 - x - 2$.}
\begin{reponse}
$(x - 2)(x + 1) = x^2 + x - 2x - 2 = x^2 - x - 2$.
\end{reponse}
\q{2.a}{Résoudre $(x - 2)(x + 1) = 0$.}
\begin{reponse}
Un produit est nul si l'un de ses facteurs est nul : $x - 2 = 0$ ou $x + 1 = 0$, soit $x = 2$ ou $x = -1$.
\end{reponse}
\q{2.b}{Antécédents de 0 par $g$.}
\begin{reponse}
$g(x) = (x - 2)(x + 1)$ : les antécédents de 0 sont \textbf{2 et $-1$}.
\end{reponse}
\q{3}{Graphique qui représente $g$.}
\begin{reponse}
La courbe doit couper l'axe des abscisses en $-1$ et en 2 : c'est le \textbf{graphique 3} (les graphiques 1 et 2 sont des droites qui ne passent pas par ces deux points).
\end{reponse}
\q{4}{Nombres de départ qui donnent 0.}
\begin{reponse}
Le programme donne $(x - 2)(x + 1) = g(x)$. Il faut choisir \textbf{2 ou $-1$}.
\end{reponse}
'''),
dict(id='2024-cetr-4a', s='cetr', ex=4, titre='Exercice 4 -- Triangles, questions 1 et 3', theme='Réciproque de Pythagore, théorème de Thalès',
     consigne='Traite les questions 1 et 3.', regions=[(4, 413, 668)], s3=13, n3=[], s4=19, n4=[22, 32],
     corr=r'''
\q{1}{Démontrer que le triangle ABE est rectangle.}
\begin{reponse}
Le plus grand côté est $[AB]$. \quad $AB^2 = 5{,}5^2 = 30{,}25$ \quad et \quad $AE^2 + EB^2 = 4{,}4^2 + 3{,}3^2 = 19{,}36 + 10{,}89 = 30{,}25$.\\
$AB^2 = AE^2 + EB^2$ : d'après la réciproque du théorème de Pythagore, le triangle $ABE$ est rectangle en $E$.
\end{reponse}
\q{3}{Calculer FD.}
\begin{reponse}
Les points $E$, $A$, $F$ et $E$, $B$, $D$ sont alignés, et $(AB) \parallel (FD)$. $ED = EB + BD = 3{,}3 + 6{,}6 = 9{,}9$ cm. D'après le théorème de Thalès :
\[ \frac{EB}{ED} = \frac{AB}{FD} \qquad\text{soit}\qquad \frac{3{,}3}{9{,}9} = \frac{5{,}5}{FD} \qquad\text{donc}\qquad FD = \frac{5{,}5 \times 9{,}9}{3{,}3} = \mathbf{16{,}5} \text{ cm}. \]
\end{reponse}
'''),
dict(id='2024-cetr-4b', s='cetr', ex=4, titre='Exercice 4 -- Triangles, questions 2 et 4', theme='Trigonométrie, homothétie',
     consigne='Traite les questions 2 et 4 (le triangle ABE est rectangle en E).', regions=[(4, 413, 668)], s3=18, n3=[6, 30], s4=None, n4=None,
     corr=r'''
\q{2}{Mesure de l'angle $\widehat{ABE}$, au degré.}
\begin{reponse}
Dans le triangle $ABE$ rectangle en $E$, $[EB]$ est le côté adjacent à $\widehat{ABE}$ et $[AB]$ l'hypoténuse :
\[ \cos\widehat{ABE} = \frac{EB}{AB} = \frac{3{,}3}{5{,}5} = 0{,}6 \qquad\text{donc}\qquad \widehat{ABE} \approx \mathbf{53^\circ}. \]
\end{reponse}
\q{4}{Rapport de l'homothétie de centre E qui transforme EAB en EFD.}
\begin{reponse}
$\dfrac{ED}{EB} = \dfrac{9{,}9}{3{,}3} = 3$, et $D$ est du même côté que $B$ par rapport à $E$ : le rapport est \textbf{3}.
\end{reponse}
'''),
dict(id='2024-cetr-5a', s='cetr', ex=5, titre='Exercice 5 -- Le chapeau de sorcier, partie A', theme='Théorème de Pythagore, périmètre du cercle, proportionnalité',
     consigne='Traite la partie A (le tableau est en annexe).', regions=[(5, 132, 703), (7, 460, 582)], s3=2, n3=[], s4=5, n4=[10, 11],
     corr=r'''
\q{1}{Montrer que MS $\approx$ 31,3 cm.}
\begin{reponse}
Le triangle $SOM$ est rectangle en $O$, d'hypoténuse $[SM]$. D'après le théorème de Pythagore :
\[ SM^2 = OS^2 + OM^2 = 30^2 + 9^2 = 900 + 81 = 981 \qquad\text{donc}\qquad SM = \sqrt{981} \approx 31{,}3 \text{ cm}. \]
\end{reponse}
\q{2}{Le chapeau est-il adapté à un tour de tête de 56 cm ?}
\begin{reponse}
Le tour du chapeau est le périmètre de la base : $2 \times \pi \times 9 = 18\pi \approx 56{,}5$ cm. C'est un peu plus que 56 cm : le chapeau est \textbf{adapté}.
\end{reponse}
\q{3.a}{Longueur du cercle de centre S et de rayon SM.}
\begin{reponse}
$2 \times \pi \times 31{,}3 \approx 196{,}7$ cm.
\end{reponse}
\q{3.b}{Compléter le tableau.}
\begin{reponse}
360° correspondent à la longueur 196,7 cm (le cercle entier) : je place 196,7 sous 360.
\end{reponse}
\q{3.c}{Mesure de l'angle $\widehat{M'SM}$.}
\begin{reponse}
L'angle est proportionnel à la longueur de l'arc :
\[ \widehat{M'SM} = \frac{360 \times 56{,}5}{196{,}7} \approx \mathbf{103^\circ}. \]
\end{reponse}
'''),
dict(id='2024-cetr-5b', s='cetr', ex=5, titre='Exercice 5 -- Le chapeau de sorcier, partie B', theme='Volume du cône, réduction, pourcentages',
     consigne='Traite la partie B.', regions=[(5, 132, 183), (5, 702, 738), (6, 128, 400)], s3=21, n3=[], s4=17, n4=[34, 40, 41],
     corr=r'''
\q{1}{Volume total du chapeau.}
\begin{reponse}
\[ V = \frac13 \times \pi \times 9^2 \times 30 = 810\pi \approx \mathbf{2\,545} \text{ cm}^3. \]
\end{reponse}
\q{2}{Les bonbons occupent-ils moins de 15 \% du volume ?}
\begin{reponse}
Les bonbons forment un petit cône de hauteur 15 cm, réduction du chapeau de rapport $\dfrac{15}{30} = \dfrac12$. Les volumes sont multipliés par $\left(\dfrac12\right)^3 = \dfrac18 = 0{,}125$.\\
Les bonbons occupent 12,5 \% du volume du chapeau ($2\,545 \times 0{,}125 \approx 318$ cm³) : c'est bien moins de 15 \%, son estimation est \textbf{correcte}.
\end{reponse}
'''),
]
