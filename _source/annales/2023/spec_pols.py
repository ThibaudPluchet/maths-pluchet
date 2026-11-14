# DNB Polynésie, 11 septembre 2023
SOURCE = ('dnb_polynesie_sept_2023.pdf', 'Polynésie, 11 septembre 2023')
QCM = (1, 183, 284)
E2 = (1, 750, 790)
E4 = (3, 781, 842)
PARTS = [
dict(id='2023-pols-1q1', s='pols', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Pourcentages',
     regions=[QCM, (1, 284, 315)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{1}{Une augmentation de 9 \% correspond à une multiplication par\ldots}
\begin{reponse}
$1 + \dfrac{9}{100} = \mathbf{1{,}09}$ : réponse C.
\end{reponse}
'''),
dict(id='2023-pols-1q2', s='pols', ex=1, titre='Exercice 1 -- QCM, question 2', theme='Théorème de Thalès',
     regions=[QCM, (1, 315, 492)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{2}{Longueur BC.}
\begin{reponse}
Les points $A$, $E$, $C$ et $A$, $D$, $B$ sont alignés, et $(DE) \parallel (BC)$. $AC = 2 + 5 = 7$ cm. D'après le théorème de Thalès :
\[ \frac{AE}{AC} = \frac{ED}{CB} \qquad\text{soit}\qquad \frac27 = \frac{3}{BC} \qquad\text{donc}\qquad BC = \frac{3 \times 7}{2} = \mathbf{10{,}5} \text{ cm} : \text{réponse C}. \]
\end{reponse}
'''),
dict(id='2023-pols-1q3', s='pols', ex=1, titre='Exercice 1 -- QCM, questions 3 et 4', theme='Probabilités, tableau à double entrée',
     regions=[QCM, (1, 492, 752)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{3}{Probabilité qu'un élève ait choisi l'italien.}
\begin{reponse}
Il y a $10 + 43 + 26 + 7 + 42 + 32 = 160$ élèves, dont $26 + 32 = 58$ font italien : $p = \dfrac{58}{160}$, réponse B.
\end{reponse}
\q{4}{Probabilité d'une fille qui ne fait pas d'allemand.}
\begin{reponse}
Filles qui font espagnol ou italien : $43 + 26 = 69$, parmi les 160 élèves : $p = \dfrac{69}{160}$, réponse C.
\end{reponse}
'''),
dict(id='2023-pols-2a', s='pols', ex=2, titre='Exercice 2 -- Programme de calcul, question 1', theme='Programme de calcul, équation produit',
     consigne='Traite la question 1.', regions=[E2, (2, 128, 322)], s3=19, n3=[32], s4=None, n4=None,
     corr=r'''
\q{1.a}{Avec $-8$ au départ.}
\begin{reponse}
$-8 + 3 = -5$ et $-8 - 4 = -12$ ; $(-5) \times (-12) = 60$.
\end{reponse}
\q{1.b}{Résoudre $(x + 3)(x - 4) = 0$.}
\begin{reponse}
$x + 3 = 0$ ou $x - 4 = 0$, soit $x = -3$ ou $x = 4$. Il faut choisir \textbf{$-3$ ou 4}.
\end{reponse}
'''),
dict(id='2023-pols-2b', s='pols', ex=2, titre='Exercice 2 -- Les fonctions f et g, questions 2 et 3', theme='Double distributivité, image, lecture graphique, tableur',
     consigne='Traite les questions 2 et 3 (le repère est en annexe).', regions=[(2, 322, 697), (6, 200, 532)], s3=17, n3=[5, 13, 18, 28], s4=None, n4=None,
     corr=r'''
\q{2.a}{Montrer que $f(x) = x^2 - x - 12$.}
\begin{reponse}
$(x + 3)(x - 4) = x^2 - 4x + 3x - 12 = x^2 - x - 12$.
\end{reponse}
\q{2.b}{Calculer $f\left(\frac12\right)$.}
\begin{reponse}
$f(0{,}5) = 0{,}5^2 - 0{,}5 - 12 = 0{,}25 - 0{,}5 - 12 = \mathbf{-12{,}25}$.
\end{reponse}
\q{2.c}{Antécédents de $-6$ (lecture graphique).}
\begin{reponse}
La droite horizontale d'ordonnée $-6$ coupe la courbe en $x = \mathbf{-2}$ et $x = \mathbf{3}$ (en effet $f(-2) = f(3) = -6$).
\end{reponse}
\q{3.a}{Formule en B2.}
\begin{reponse}
\texttt{=3*A2-7}.
\end{reponse}
\q{3.b}{Tracer la représentation de $g$.}
\begin{reponse}
C'est une droite : elle passe par exemple par $(0\,;\,-7)$ et $(3\,;\,2)$.
\end{reponse}
\q{3.c}{Nombres qui ont la même image par $f$ et $g$.}
\begin{reponse}
Les deux courbes se coupent pour $x = \mathbf{-1}$ et $x = \mathbf{5}$ ($f(-1) = g(-1) = -10$ ; $f(5) = g(5) = 8$).
\end{reponse}
'''),
dict(id='2023-pols-3', s='pols', ex=3, titre='Exercice 3 -- Les dix carrés (Scratch)', theme='Algorithmique (Scratch), pourcentages',
     consigne='Le bloc « Carré » est en annexe.', regions=[(2, 694, 844), (3, 128, 781), (6, 530, 660)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Côté du 2\textsuperscript{e} carré.}
\begin{reponse}
Diminuer de 20 \%, c'est multiplier par 0,8 : $300 \times 0{,}8 = 240$ pixels.
\end{reponse}
\q{2}{Lignes 2 et 4 du bloc « Carré ».}
\begin{reponse}
Ligne 2 : répéter \textbf{4} fois ; ligne 4 : tourner de \textbf{90} degrés.
\end{reponse}
\q{3.a}{Coordonnées du stylo au début du premier carré.}
\begin{reponse}
Côté vaut 300 : $\left(\dfrac{300}{2}\,;\,\dfrac{300}{2}\right) = \mathbf{(150\,;\,150)}$.
\end{reponse}
\q{3.b}{Proposition qui correspond aux deux premiers carrés.}
\begin{reponse}
Le premier carré part de $(150\,;\,150)$ et a pour côté 300 : il est centré sur l'origine. Le deuxième part de $(120\,;\,120)$ avec un côté de 240 : lui aussi est centré sur l'origine. Deux carrés de même centre $O$ : \textbf{proposition 3}.
\end{reponse}
\q{3.c}{Côté du dernier carré.}
\begin{reponse}
Le dixième carré a subi 9 réductions : $300 \times 0{,}8^9 \approx 40{,}3$, soit \textbf{40 pixels}.
\end{reponse}
\q{4}{Où placer les instructions A et B ?}
\begin{reponse}
B (mettre la taille à 11) une seule fois, avant la boucle : entre les lignes \textbf{4 et 5}.\\
A (ajouter $-1$) dans la boucle, une fois par carré : par exemple entre les lignes \textbf{9 et 10}.
\end{reponse}
'''),
dict(id='2023-pols-4a', s='pols', ex=4, titre='Exercice 4 -- La rampe d’accès, questions 1 et 2', theme='Trigonométrie, théorème de Pythagore',
     consigne='Traite les questions 1 et 2.', regions=[E4, (4, 128, 453)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{1}{Mesure de l'angle $\widehat{ABC}$.}
\begin{reponse}
Dans le triangle $ABC$ rectangle en $C$, $[AC]$ est le côté opposé à $\widehat{ABC}$ et $[AB]$ l'hypoténuse :
\[ \sin\widehat{ABC} = \frac{AC}{AB} = \frac{30}{124} \qquad\text{donc}\qquad \widehat{ABC} \approx \mathbf{14^\circ}. \]
\end{reponse}
\q{2}{Montrer que BC $\approx$ 120 cm.}
\begin{reponse}
D'après le théorème de Pythagore : $BC^2 = AB^2 - AC^2 = 124^2 - 30^2 = 15\,376 - 900 = 14\,476$, donc $BC = \sqrt{14\,476} \approx 120$ cm.
\end{reponse}
'''),
dict(id='2023-pols-4b', s='pols', ex=4, titre='Exercice 4 -- La rampe d’accès, questions 3 et 4', theme='Volume d’un prisme, équation',
     consigne='Traite les questions 3 et 4 (BC ≈ 120 cm).', regions=[E4, (4, 128, 404), (4, 452, 546)], s3=21, n3=[], s4=16, n4=[38],
     corr=r'''
\q{3}{2 m³ de béton suffisent-ils ?}
\begin{reponse}
En mètres : aire de la base $ABC$ : $\dfrac{0{,}3 \times 1{,}2}{2} = 0{,}18$ m². Volume du prisme : $0{,}18 \times 9 = 1{,}62$ m³.\\
$1{,}62 < 2$ : \textbf{oui}, c'est suffisant.
\end{reponse}
\q{4}{Valeur de BC pour un volume de 2 m³.}
\begin{reponse}
\[ \frac{0{,}3 \times BC}{2} \times 9 = 2 \iff 1{,}35 \times BC = 2 \iff BC = \frac{2}{1{,}35} \approx 1{,}48 \text{ m}, \text{ soit } \mathbf{148} \text{ cm}. \]
\end{reponse}
'''),
dict(id='2023-pols-5a', s='pols', ex=5, titre='Exercice 5 -- La transat Jacques Vabre, question 1', theme='Latitude et longitude',
     consigne='Traite la question 1.', regions=[(4, 545, 800)], s3=6, n3=[9], s4=None, n4=None,
     corr=r'''
\q{1}{Latitude et longitude de Fort-de-France.}
\begin{reponse}
La croix est au nord de l'équateur et à l'ouest du méridien de Greenwich : environ \textbf{15° Nord et 60° Ouest} (en réalité 14,6° N et 61,1° O).
\end{reponse}
'''),
dict(id='2023-pols-5b', s='pols', ex=5, titre='Exercice 5 -- La transat Jacques Vabre, question 2', theme='Durées, moyenne, vitesse, périmètre',
     consigne='Traite la question 2.', regions=[(4, 545, 598), (5, 128, 578)], s3=14, n3=[], s4=15, n4=[24, 35],
     corr=r'''
\q{2.a}{Écart entre LinkedOut et Primonial.}
\begin{reponse}
$18$ j $1$ h $21$ min $= 17$ j $24$ h $81$ min. \quad $17$ j $24$ h $81$ min $- 15$ j $13$ h $27$ min $= \mathbf{2}$ \textbf{j 11 h 54 min}.
\end{reponse}
\q{2.b}{Distance moyenne des 75 bateaux.}
\begin{reponse}
\[ \frac{43 \times 4\,600 + 7 \times 5\,800 + 20 \times 5\,800 + 5 \times 7\,500}{75} = \frac{391\,900}{75} \approx \mathbf{5\,225} \text{ milles}. \]
\end{reponse}
\q{2.c}{Vitesse du Maxi Edmond de Rothschild.}
\begin{reponse}
16 j 1 h 48 min $= 16 \times 24 + 1 + 0{,}8 = 385{,}8$ h. \quad $v = \dfrac{7\,500}{385{,}8} \approx 19{,}4$ milles/h.\\
$\dfrac{19{,}4}{8{,}7} \approx 2{,}2$ : sa vitesse est bien environ 2,2 fois plus grande.
\end{reponse}
\q{2.d}{Un quart de l'équateur ?}
\begin{reponse}
Équateur : $2 \times \pi \times 6\,370 \approx 40\,024$ km ; un quart : $\approx 10\,006$ km.\\
Ocean Fifty : $5\,800 \times 1{,}852 \approx 10\,742$ km. C'est un peu plus (environ 7 \% de plus) : le journaliste a \textbf{à peu près} raison, l'ordre de grandeur est le même.
\end{reponse}
'''),
]
