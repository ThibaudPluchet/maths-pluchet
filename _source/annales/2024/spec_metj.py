# DNB Métropole – Antilles-Guyane, 1er juillet 2024
SOURCE = ('dnb_metropole_juil_2024.pdf', 'Métropole – Antilles-Guyane, 1er juillet 2024')
QCM = (3, 136, 249)
E2 = (1, 608, 775)
PARTS = [
dict(id='2024-metj-1', s='metj', ex=1, titre='Exercice 1 -- La roulette, questions 1 et 3', theme='Probabilités',
     consigne='Traite les questions 1 et 3.', regions=[(1, 170, 521), (1, 536, 600)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{1}{Pourquoi la probabilité d'obtenir le 7 est-elle $\frac{1}{37}$ ?}
\begin{reponse}
De 0 à 36, il y a 37 numéros, qui ont tous la même probabilité. Le 7 est un seul de ces 37 numéros : $p = \dfrac{1}{37}$.
\end{reponse}
\q{3.a}{Probabilité d'un numéro inférieur ou égal à 6.}
\begin{reponse}
Les numéros 0, 1, 2, 3, 4, 5, 6 : 7 numéros sur 37. \quad $p = \dfrac{7}{37}$.
\end{reponse}
\q{3.b}{Probabilité d'un numéro supérieur ou égal à 7.}
\begin{reponse}
C'est l'événement contraire du précédent : $p = 1 - \dfrac{7}{37} = \dfrac{30}{37}$.
\end{reponse}
\q{3.c}{A-t-on plus de 3 chances sur 4 d'obtenir un numéro supérieur ou égal à 7 ?}
\begin{reponse}
$\dfrac{30}{37} \approx 0{,}81$ et $\dfrac34 = 0{,}75$. Comme $0{,}81 > 0{,}75$, le joueur \textbf{a raison}.
\end{reponse}
'''),
dict(id='2024-metj-2a', s='metj', ex=2, titre='Exercice 2 -- Deux programmes, questions 1 et 2', theme='Programme de calcul, Scratch, expression littérale',
     consigne='Traite les questions 1 et 2.', regions=[E2, (2, 128, 270)], s3=1, n3=[], s4=8, n4=[2, 19, 20],
     corr=r'''
\q{1.a}{Programme A avec 5.}
\begin{reponse}
$5^2 = 25$ ; $25 \times 2 = 50$ ; $50 + 2 \times 5 = 60$ ; $60 - 4 = 56$.
\end{reponse}
\q{1.b}{Programme B avec $-9$.}
\begin{reponse}
Résultat 1 : $-9 + 2 = -7$ ; Résultat 2 : $-9 - 1 = -10$. Le programme dit $(-7) \times (-10) = \mathbf{70}$.
\end{reponse}
\q{2.a}{Expression du programme B.}
\begin{reponse}
Le programme multiplie $x + 2$ par $x - 1$ : $\mathbf{E_2 = (x + 2) \times (x - 1)}$.
\end{reponse}
\q{2.b}{Résultat du programme A en fonction de $x$.}
\begin{reponse}
$x \longrightarrow x^2 \longrightarrow 2x^2 \longrightarrow 2x^2 + 2x \longrightarrow \mathbf{2x^2 + 2x - 4}$.
\end{reponse}
'''),
dict(id='2024-metj-2b', s='metj', ex=2, titre='Exercice 2 -- Deux programmes, question 3', theme='Double distributivité, preuve',
     consigne='Traite la question 3 (programme A : 2x² + 2x − 4 ; programme B : (x + 2)(x − 1)).', regions=[E2, (2, 270, 312)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{3}{Le résultat de A est toujours le double de celui de B.}
\begin{reponse}
Je développe le résultat du programme B : $(x + 2)(x - 1) = x^2 - x + 2x - 2 = x^2 + x - 2$.\\
Son double : $2(x^2 + x - 2) = 2x^2 + 2x - 4$, c'est exactement le résultat du programme A. Quel que soit $x$, A donne le double de B.
\end{reponse}
'''),
dict(id='2024-metj-3a', s='metj', ex=3, titre='Exercice 3 -- Le cercle, questions 1 à 3', theme='Réciproque de Pythagore, théorème de Thalès',
     consigne='Traite les questions 1 à 3.', regions=[(2, 314, 716)], s3=13, n3=[], s4=19, n4=[22, 32],
     corr=r'''
\q{1}{Justifier que AB = 9 cm.}
\begin{reponse}
$[AB]$ est un diamètre du cercle de rayon 4,5 cm : $AB = 2 \times 4{,}5 = 9$ cm.
\end{reponse}
\q{2}{Démontrer que ABD est rectangle en D.}
\begin{reponse}
Le plus grand côté est $[AB]$. \quad $AB^2 = 9^2 = 81$ \quad et \quad $AD^2 + DB^2 = 7{,}2^2 + 5{,}4^2 = 51{,}84 + 29{,}16 = 81$.\\
$AB^2 = AD^2 + DB^2$ : d'après la réciproque du théorème de Pythagore, $ABD$ est rectangle en $D$.
\end{reponse}
\q{3}{Calculer AF.}
\begin{reponse}
Les points $A$, $E$, $B$ et $A$, $F$, $D$ sont alignés, et $(EF) \parallel (BD)$. D'après le théorème de Thalès :
\[ \frac{AE}{AB} = \frac{AF}{AD} \qquad\text{soit}\qquad \frac{2{,}7}{9} = \frac{AF}{7{,}2} \qquad\text{donc}\qquad AF = \frac{2{,}7 \times 7{,}2}{9} = \mathbf{2{,}16} \text{ cm}. \]
\end{reponse}
'''),
dict(id='2024-metj-3b', s='metj', ex=3, titre='Exercice 3 -- Le cercle, questions 4 et 5', theme='Aires, pourcentage',
     consigne='Traite les questions 4 et 5 (le triangle ABD est rectangle en D).', regions=[(2, 314, 666), (2, 715, 790)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{4.a}{Aire du triangle ABD.}
\begin{reponse}
Le triangle est rectangle en $D$ : $\mathcal{A} = \dfrac{DB \times DA}{2} = \dfrac{5{,}4 \times 7{,}2}{2} = 19{,}44$ cm².
\end{reponse}
\q{4.b}{Aire du disque.}
\begin{reponse}
$\pi \times 4{,}5^2 = 20{,}25\pi \approx \mathbf{63{,}62}$ cm².
\end{reponse}
\q{5}{Pourcentage de l'aire du disque occupé par le triangle.}
\begin{reponse}
$\dfrac{19{,}44}{63{,}62} \approx 0{,}306$ : le triangle représente environ \textbf{30,6 \%} de l'aire du disque.
\end{reponse}
'''),
dict(id='2024-metj-4q1', s='metj', ex=4, titre='Exercice 4 -- QCM, question 1', theme='Fonction : calculer une image',
     regions=[QCM, (3, 248, 289)], s3=3, n3=[5], s4=None, n4=None,
     corr=r'''
\q{1}{Image de $-4$ par $f(x) = 3x - 2$.}
\begin{reponse}
$f(-4) = 3 \times (-4) - 2 = -12 - 2 = -14$ : \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2024-metj-4q2', s='metj', ex=4, titre='Exercice 4 -- QCM, question 2', theme='Puissances, nombres relatifs',
     regions=[QCM, (3, 289, 303)], s3=25, n3=[], s4=13, n4=[2, 29],
     corr=r'''
\q{2}{Combien vaut $(-5)^3$ ?}
\begin{reponse}
$(-5)^3 = (-5) \times (-5) \times (-5) = 25 \times (-5) = -125$ : \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2024-metj-4q3', s='metj', ex=4, titre='Exercice 4 -- QCM, question 3', theme='Translation',
     regions=[QCM, (3, 303, 415)], s3=11, n3=[], s4=7, n4=[17],
     corr=r'''
\q{3}{Image de J par la translation qui transforme C en A.}
\begin{reponse}
Pour aller de $C$ à $A$, on se déplace d'une colonne vers la gauche et d'une ligne vers le bas. En faisant le même déplacement à partir de $J$, on arrive en $E$ : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2024-metj-4q4', s='metj', ex=4, titre='Exercice 4 -- QCM, question 4', theme='Antécédent, lecture graphique',
     regions=[QCM, (3, 415, 566)], s3=8, n3=[13], s4=None, n4=None,
     corr=r'''
\q{4}{Antécédent de 3 par la fonction $f$.}
\begin{reponse}
Le point de la courbe d'ordonnée 3 a pour abscisse 0 : l'antécédent de 3 est \textbf{0}, \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2024-metj-4q5', s='metj', ex=4, titre='Exercice 4 -- QCM, question 5', theme='Médiane',
     regions=[QCM, (3, 566, 630)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{5}{Médiane des sept tailles.}
\begin{reponse}
Dans l'ordre : 1,46 ; 1,6 ; 1,65 ; \textbf{1,67} ; 1,7 ; 1,72 ; 1,75. La médiane est la $4^{\text{e}}$ valeur, 1,67 m : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2024-metj-4q6', s='metj', ex=4, titre='Exercice 4 -- QCM, question 6', theme='Trigonométrie (cosinus)',
     regions=[QCM, (3, 628, 760)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{6}{Valeur de $\cos\alpha$.}
\begin{reponse}
Dans le triangle $ABC$ rectangle en $A$, l'hypoténuse est $[BC]$ (5) et le côté adjacent à l'angle $\alpha$ (en $B$) est $[AB]$ (4) :
$\cos\alpha = \dfrac{4}{5} = 0{,}8$ : \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2024-metj-5a', s='metj', ex=5, titre='Exercice 5 -- Le club de natation, partie A', theme='Diviseurs, décomposition, répartition',
     consigne='Traite la partie A.', regions=[(3, 772, 792), (4, 128, 315)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{1}{Pourquoi pas 15 sachets ?}
\begin{reponse}
$330 = 15 \times 22$, mais $132 \div 15 = 8{,}8$ n'est pas entier : 15 ne divise pas 132.
\end{reponse}
\q{2.a}{Décomposer 330 et 132.}
\begin{reponse}
$330 = 2 \times 3 \times 5 \times 11$ \qquad et \qquad $132 = 2^2 \times 3 \times 11$.
\end{reponse}
\q{2.b}{Plus grand nombre de sachets.}
\begin{reponse}
Le nombre de sachets doit diviser 330 et 132. Le plus grand diviseur commun reprend les facteurs communs : $2 \times 3 \times 11 = \mathbf{66}$ sachets.
\end{reponse}
\q{2.c}{Contenu de chaque sachet.}
\begin{reponse}
$330 \div 66 = 5$ autocollants et $132 \div 66 = 2$ drapeaux par sachet.
\end{reponse}
'''),
dict(id='2024-metj-5b', s='metj', ex=5, titre='Exercice 5 -- La piscine, partie B', theme='Volume du pavé, fraction, prix',
     consigne='Traite la partie B.', regions=[(3, 772, 792), (4, 312, 526)], s3=21, n3=[], s4=18, n4=[42],
     corr=r'''
\q{B}{Coût du remplissage de la piscine.}
\begin{reponse}
Volume du pavé : $25 \times 15 \times 2 = 750$ m³. La piscine est remplie aux $\dfrac{9}{10}$ : $750 \times \dfrac{9}{10} = 675$ m³ d'eau.\\
Coût : $675 \times 4{,}14 = \mathbf{2\,794{,}50}$ €.
\end{reponse}
'''),
]
