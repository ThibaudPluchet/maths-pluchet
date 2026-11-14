# DNB Amérique du Sud, 2 décembre 2024
SOURCE = ('dnb_ameri_sud_dec_2024.pdf', 'Amérique du Sud, 2 décembre 2024')
QCM = (1, 175, 303)
E4 = (3, 741, 790)
PARTS = [
dict(id='2024-asud-1q1', s='asud', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Probabilités',
     regions=[QCM, (1, 303, 385)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{1}{Probabilité d'obtenir un jeton blanc.}
\begin{reponse}
2 jetons blancs sur $3 + 2 = 5$ jetons : $p = \dfrac25$, \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2024-asud-1q3', s='asud', ex=1, titre='Exercice 1 -- QCM, question 3', theme='Théorème de Thalès',
     regions=[QCM, (1, 524, 696)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{3}{Longueur DH.}
\begin{reponse}
Les points $B$, $H$, $A$ et $B$, $D$, $C$ sont alignés, et $(DH) \parallel (AC)$. D'après le théorème de Thalès :
\[ \frac{BD}{BC} = \frac{DH}{CA} \qquad\text{soit}\qquad \frac{2}{10} = \frac{DH}{16} \qquad\text{donc}\qquad DH = \frac{2 \times 16}{10} = 3{,}2 \text{ cm} : \textbf{réponse A}. \]
\end{reponse}
'''),
dict(id='2024-asud-1q4', s='asud', ex=1, titre='Exercice 1 -- QCM, question 4', theme='Multiples (engrenage)',
     regions=[QCM, (2, 156, 303)], s3=24, n3=[], s4=6, n4=[13],
     corr=r'''
\q{4}{Tours de la grande roue quand la petite fait 4 tours.}
\begin{reponse}
4 tours de la petite roue font passer $4 \times 9 = 36$ dents. La grande roue a 12 dents : $36 \div 12 = 3$. Elle fait \textbf{3 tours complets} : \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2024-asud-1q5', s='asud', ex=1, titre='Exercice 1 -- QCM, question 5', theme='Homothétie',
     regions=[QCM, (2, 303, 488)], s3=18, n3=[30], s4=None, n4=None,
     corr=r'''
\q{5}{Triangle dont EGF est l'image.}
\begin{reponse}
L'homothétie de centre $A$ transforme le carré $ADCB$ en $AGFE$, sommet par sommet : $D \to G$, $C \to F$, $B \to E$.\\
Le triangle $EGF$ est donc l'image du triangle $BDC$ : \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2024-asud-2a', s='asud', ex=2, titre='Exercice 2 -- Les fonctions f et g, question 1', theme='Image, antécédent, tableur',
     consigne='Traite la question 1.', regions=[(2, 508, 790), (3, 128, 168)], s3=8, n3=[5, 12, 14], s4=None, n4=None,
     corr=r'''
\q{1.a}{Image de 5 par $f$.}
\begin{reponse}
$f(5) = 5^2 - 5 - 6 = 25 - 5 - 6 = 14$.
\end{reponse}
\q{1.b}{Antécédent de 4 par $g$.}
\begin{reponse}
Je résous $-2x = 4$ : $x = \dfrac{4}{-2} = \mathbf{-2}$.
\end{reponse}
\q{1.c}{Deux antécédents de 14 par $f$.}
\begin{reponse}
$f(5) = 14$ (question a) et $f(-4) = 14$ (tableur) : \textbf{5 et $-4$}.
\end{reponse}
\q{1.d}{Formule saisie en B2.}
\begin{reponse}
\texttt{=B1*B1-B1-6} \quad (ou \texttt{=B1\^{}2-B1-6}).
\end{reponse}
\q{1.e}{Un nombre qui a la même image par $f$ et par $g$ ?}
\begin{reponse}
\textbf{Oui} : d'après le tableau, $f(-3) = g(-3) = 6$ (et aussi $f(2) = g(2) = -4$).
\end{reponse}
'''),
dict(id='2024-asud-2b', s='asud', ex=2, titre='Exercice 2 -- Les fonctions f et g, question 2', theme='Double distributivité, équation produit',
     consigne='Traite la question 2.', regions=[(2, 508, 585), (3, 168, 212)], s3=19, n3=[18, 32], s4=None, n4=None,
     corr=r'''
\q{2.a}{Montrer que $f(x) = (x + 2)(x - 3)$.}
\begin{reponse}
$(x + 2)(x - 3) = x^2 - 3x + 2x - 6 = x^2 - x - 6 = f(x)$.
\end{reponse}
\q{2.b}{Résoudre $f(x) = 0$.}
\begin{reponse}
$(x + 2)(x - 3) = 0 \iff x + 2 = 0$ ou $x - 3 = 0 \iff x = -2$ ou $x = 3$. Les solutions sont \textbf{$-2$ et 3}.
\end{reponse}
'''),
dict(id='2024-asud-3', s='asud', ex=3, titre='Exercice 3 -- Les félins, questions 1 et 2', theme='Probabilités, vitesse, pourcentage',
     consigne='Traite les questions 1 et 2.', regions=[(3, 212, 538)], s3=14, n3=[], s4=15, n4=[34, 35, 47],
     corr=r'''
\q{1}{Le chat à pieds noirs a-t-il la plus grande probabilité ?}
\begin{reponse}
Lion : $25\ \% = 0{,}25$ ; guépard : $\dfrac12 = 0{,}5$ ; tigre : $0{,}1$ ; chat à pieds noirs : $\dfrac{6}{10} = 0{,}6$.\\
0,6 est la plus grande valeur : c'est bien le chat à pieds noirs.
\end{reponse}
\q{2}{Temps pour 100 m à 115 km/h.}
\begin{reponse}
115 km/h, c'est $115\,000$ m en $3\,600$ s. Pour 100 m : $t = \dfrac{100 \times 3\,600}{115\,000} \approx \mathbf{3{,}13}$ s.
\end{reponse}
\q{2 (suite)}{Baisse d'environ 86 \% entre 1999 et 2016 ?}
\begin{reponse}
Baisse : $1\,200 - 170 = 1\,030$ guépards. \quad $\dfrac{1\,030}{1\,200} \approx 0{,}858$, soit environ 86 \% : \textbf{oui}.
\end{reponse}
'''),
dict(id='2024-asud-4a', s='asud', ex=4, titre='Exercice 4 -- Le terrain en pente, questions 1 et 3', theme='Théorème de Pythagore, volume d’un prisme',
     consigne='Traite les questions 1 et 3.', regions=[E4, (4, 128, 320), (4, 372, 604)], s3=2, n3=[], s4=4, n4=[10],
     corr=r'''
\q{1}{Justifier que CB = 16,8 m.}
\begin{reponse}
Le triangle $ABC$ est rectangle en $C$, d'hypoténuse $[AB]$. D'après le théorème de Pythagore :
\[ CB^2 = AB^2 - AC^2 = 17^2 - 2{,}6^2 = 289 - 6{,}76 = 282{,}24 \qquad\text{donc}\qquad CB = \sqrt{282{,}24} = 16{,}8 \text{ m}. \]
\end{reponse}
\q{3}{Volume de terre à enlever.}
\begin{reponse}
Aire de la base $ACB$ (triangle rectangle en $C$) : $\dfrac{2{,}6 \times 16{,}8}{2} = 21{,}84$ m². La hauteur du prisme est $CF = AD = 30$ m.\\
$V = 21{,}84 \times 30 = \mathbf{655{,}2}$ m³.
\end{reponse}
'''),
dict(id='2024-asud-4b', s='asud', ex=4, titre='Exercice 4 -- Le terrain en pente, question 2', theme='Trigonométrie',
     consigne='Traite la question 2.', regions=[E4, (4, 128, 372)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{2}{L'angle $\widehat{ABC}$ dépasse-t-il 8,5° ?}
\begin{reponse}
Dans le triangle $ABC$ rectangle en $C$, $[AC]$ est le côté opposé à l'angle $\widehat{ABC}$ et $[AB]$ l'hypoténuse :
\[ \sin\widehat{ABC} = \frac{AC}{AB} = \frac{2{,}6}{17} \qquad\text{donc}\qquad \widehat{ABC} \approx 8{,}8^\circ. \]
$8{,}8^\circ > 8{,}5^\circ$ : \textbf{oui}, il y aura un surcoût.
\end{reponse}
'''),
dict(id='2024-asud-5', s='asud', ex=5, titre='Exercice 5 -- Les losanges (Scratch)', theme='Algorithmique (Scratch)',
     regions=[(4, 603, 672), (5, 128, 735), (6, 128, 392)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Valeurs de $a$ et $b$.}
\begin{reponse}
Les quatre côtés d'un losange ont la même longueur : $a = \mathbf{20}$. Les angles du losange mesurent $120^\circ$ et $60^\circ$ : après avoir tourné de $60^\circ$, le lutin tourne de $180^\circ - 60^\circ = 120^\circ$, donc $b = \mathbf{120}$.
\end{reponse}
\q{2}{Figure obtenue avec « Motif A ».}
\begin{reponse}
Trois losanges qui ont le même point de départ, chacun tourné de $60^\circ$ par rapport au précédent : c'est la \textbf{figure 3}.
\end{reponse}
\q{3}{Script du bloc « Motif B ».}
\begin{reponse}
Trois losanges identiques, alignés et espacés :
\texttt{définir Motif B} ; \texttt{répéter 3 fois} : \texttt{Losange} puis \texttt{avancer de 40} (le stylo est relevé à la fin du bloc Losange, le déplacement ne laisse pas de trait).
\end{reponse}
'''),
]
