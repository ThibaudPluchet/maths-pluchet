# DNB Métropole – Antilles-Guyane, 18 septembre 2023
SOURCE = ('dnb_metropole_sept_2023.pdf', 'Métropole – Antilles-Guyane, 18 septembre 2023')
QCM = (1, 250, 358)
E5 = (6, 486, 790)
PARTS = [
dict(id='2023-mets-1q1', s='mets', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Diviseurs',
     regions=[QCM, (1, 358, 372)], s3=24, n3=[], s4=6, n4=[13],
     corr=r'''
\q{1}{Trois diviseurs de 84.}
\begin{reponse}
$84 = 2 \times 42 = 3 \times 28 = 4 \times 21$ : \textbf{2, 3 et 4}, réponse B (5 ne divise pas 84 ; 84, 168 et 252 sont des multiples).
\end{reponse}
'''),
dict(id='2023-mets-1q2', s='mets', ex=1, titre='Exercice 1 -- QCM, question 2', theme='Agrandissement et volumes',
     regions=[QCM, (1, 372, 578)], s3=21, n3=[], s4=17, n4=[41],
     corr=r'''
\q{2}{Coefficient pour le volume (agrandissement de coefficient 2).}
\begin{reponse}
Les volumes sont multipliés par $2^3 = \mathbf{8}$ : réponse B.
\end{reponse}
'''),
dict(id='2023-mets-1q3', s='mets', ex=1, titre='Exercice 1 -- QCM, question 3', theme='Calculer une expression littérale',
     regions=[QCM, (1, 578, 609)], s3=1, n3=[], s4=8, n4=[2, 18],
     corr=r'''
\q{3}{Valeur de $x^2 + 3x - 5$ pour $x = -2$.}
\begin{reponse}
$(-2)^2 + 3 \times (-2) - 5 = 4 - 6 - 5 = \mathbf{-7}$ : réponse C.
\end{reponse}
'''),
dict(id='2023-mets-1q4', s='mets', ex=1, titre='Exercice 1 -- QCM, question 4', theme='Probabilités',
     regions=[QCM, (1, 609, 664)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{4}{Probabilité d'obtenir un multiple de 2.}
\begin{reponse}
2, 4, 6 et 8 : 4 boules sur 8, $p = \dfrac48 = \dfrac12$, réponse A.
\end{reponse}
'''),
dict(id='2023-mets-1q5', s='mets', ex=1, titre='Exercice 1 -- QCM, question 5', theme='Homothétie',
     regions=[QCM, (1, 664, 780)], s3=18, n3=[30], s4=None, n4=None,
     corr=r'''
\q{5}{Rapport de l'homothétie de centre O.}
\begin{reponse}
Le triangle $DEF$ est de l'autre côté de $O$ et deux fois plus grand : le rapport est $\mathbf{-2}$, réponse A.
\end{reponse}
'''),
dict(id='2023-mets-2', s='mets', ex=2, titre='Exercice 2 -- Les losanges (Scratch)', theme='Algorithmique (Scratch), rotation',
     regions=[(2, 146, 615), (3, 128, 488), (4, 128, 438)], s3=0, n3=[17], s4=None, n4=None,
     corr=r'''
\q{1}{Compléter les lignes 3 et 6.}
\begin{reponse}
Ligne 3 : répéter \textbf{2} fois ; ligne 6 : avancer de \textbf{50} pas (les quatre côtés du losange mesurent 50 pas).
\end{reponse}
\q{2}{Associer chaque script à sa figure.}
\begin{reponse}
Script 1 (avancer de 50 pas) : losanges accolés, \textbf{figure C}.\\
Script 2 (avancer de 100 pas) : losanges séparés, \textbf{figure A}.\\
Script 3 (avancer de 50 pas et monter de 30) : losanges en escalier, \textbf{figure B}.
\end{reponse}
\q{3}{Transformation qui envoie EDCF sur ABCD.}
\begin{reponse}
Les six losanges ont le sommet $C$ en commun et le programme tourne de $60^\circ$ entre deux losanges : c'est la \textbf{rotation de centre $C$ et d'angle $60^\circ$} (dans le sens des aiguilles d'une montre), qui envoie $E$ sur $A$, $D$ sur $B$\ldots
\end{reponse}
'''),
dict(id='2023-mets-3a', s='mets', ex=3, titre='Exercice 3 -- La piscine, questions 1 à 3', theme='Fonctions linéaires et affines, équation',
     consigne='Traite les questions 1 à 3.', regions=[(5, 146, 333)], s3=17, n3=[26], s4=None, n4=None,
     corr=r'''
\q{1.a}{Prix de 10 entrées, tarif A.}
\begin{reponse}
$10 \times 5{,}90 = \mathbf{59}$ €.
\end{reponse}
\q{1.b}{Prix de 10 entrées, tarif B.}
\begin{reponse}
$30 + 10 \times 4{,}40 = 30 + 44 = \mathbf{74}$ €.
\end{reponse}
\q{2}{Expressions de $f(x)$ et $g(x)$.}
\begin{reponse}
$f(x) = 5{,}9x$ \qquad et \qquad $g(x) = 4{,}4x + 30$.
\end{reponse}
\q{3.a}{Résoudre $5{,}90x = 4{,}40x + 30$.}
\begin{reponse}
$5{,}9x - 4{,}4x = 30 \iff 1{,}5x = 30 \iff x = \dfrac{30}{1{,}5} = \mathbf{20}$.
\end{reponse}
\q{3.b}{Nombre d'entrées pour un même prix.}
\begin{reponse}
\textbf{20 entrées} (118 € avec les deux tarifs).
\end{reponse}
'''),
dict(id='2023-mets-3b', s='mets', ex=3, titre='Exercice 3 -- La piscine, questions 4 et 5', theme='Moyenne, étendue, volume',
     consigne='Traite les questions 4 et 5.', regions=[(5, 146, 215), (5, 333, 500)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{4.a}{Nombre moyen d'entrées par mois.}
\begin{reponse}
La somme des 12 mois vaut $144\,600$ : $144\,600 \div 12 = \mathbf{12\,050}$ entrées par mois.
\end{reponse}
\q{4.b}{Étendue.}
\begin{reponse}
$13\,800 - 10\,200 = \mathbf{3\,600}$ entrées.
\end{reponse}
\q{5}{Volume d'eau évacué.}
\begin{reponse}
$50 \times 25 \times 3 = \mathbf{3\,750}$ m³.
\end{reponse}
'''),
dict(id='2023-mets-4', s='mets', ex=4, titre='Exercice 4 -- Le funiculaire', theme='Pourcentage de réduction, vitesse, pente',
     regions=[(5, 498, 765), (6, 128, 488)], s3=14, n3=[], s4=15, n4=[34, 35],
     corr=r'''
\q{1.a}{Prix au tarif individuel (aller-retour).}
\begin{reponse}
$12 \times 10 + 8 \times 8 = 120 + 64 = \mathbf{184}$ €.
\end{reponse}
\q{1.b}{Prix au tarif de groupe (20 personnes).}
\begin{reponse}
$12 \times 8{,}50 + 8 \times 7 = 102 + 56 = \mathbf{158}$ €.
\end{reponse}
\q{1.c}{Pourcentage de réduction.}
\begin{reponse}
Réduction : $184 - 158 = 26$ €. \quad $\dfrac{26}{184} \approx 0{,}141$, soit environ \textbf{14 \%}.
\end{reponse}
\q{2}{Vitesse moyenne sur [DA].}
\begin{reponse}
8 min 45 s $= 8 \times 60 + 45 = 525$ s. \quad $v = \dfrac{448{,}5}{525} \approx \mathbf{0{,}85}$ m/s.
\end{reponse}
\q{3}{Longueur horizontale AC.}
\begin{reponse}
Pente de 25 \% : $\dfrac{BC}{AC} = 0{,}25$, donc $AC = \dfrac{50}{0{,}25} = \mathbf{200}$ m.
\end{reponse}
'''),
dict(id='2023-mets-5a', s='mets', ex=5, titre='Exercice 5 -- Le triangle ABC, questions 1 à 4', theme='Théorème de Pythagore, trigonométrie',
     consigne='Traite les questions 1 à 4.', regions=[E5, (7, 128, 312)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{1}{Calculer AB.}
\begin{reponse}
$M$ est sur $[AB]$ : $AB = AM + MB = 2{,}7 + 2{,}5 = \mathbf{5{,}2}$ cm.
\end{reponse}
\q{2}{Montrer que AH = 4,8 cm.}
\begin{reponse}
Le triangle $ABH$ est rectangle en $H$ (codage), d'hypoténuse $[AB]$. D'après le théorème de Pythagore :
\[ AH^2 = AB^2 - BH^2 = 5{,}2^2 - 2^2 = 27{,}04 - 4 = 23{,}04 \qquad\text{donc}\qquad AH = \sqrt{23{,}04} = 4{,}8 \text{ cm}. \]
\end{reponse}
\q{3}{Mesure de l'angle $\widehat{ACH}$.}
\begin{reponse}
Dans le triangle $AHC$ rectangle en $H$, $[AH]$ est le côté opposé à $\widehat{ACH}$ et $[AC]$ l'hypoténuse :
\[ \sin\widehat{ACH} = \frac{AH}{AC} = \frac{4{,}8}{8{,}5} \qquad\text{donc}\qquad \widehat{ACH} \approx \mathbf{34^\circ}. \]
\end{reponse}
\q{4}{Longueur HC.}
\begin{reponse}
D'après le théorème de Pythagore dans le triangle $AHC$ rectangle en $H$ :
\[ HC^2 = AC^2 - AH^2 = 8{,}5^2 - 4{,}8^2 = 72{,}25 - 23{,}04 = 49{,}21 \qquad\text{donc}\qquad HC = \sqrt{49{,}21} \approx \mathbf{7} \text{ cm}. \]
\end{reponse}
'''),
dict(id='2023-mets-5b', s='mets', ex=5, titre='Exercice 5 -- Le triangle ABC, questions 5 et 6', theme='Théorème de Thalès, aire',
     consigne='Traite les questions 5 et 6 (AB = 5,2 cm ; AH = 4,8 cm ; HC ≈ 7 cm).', regions=[E5, (7, 128, 243), (7, 312, 345)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{5}{« AN est inférieure à 4 cm » ?}
\begin{reponse}
Les points $A$, $M$, $B$ et $A$, $N$, $C$ sont alignés, et $(MN) \parallel (BC)$. D'après le théorème de Thalès :
\[ \frac{AN}{AC} = \frac{AM}{AB} \qquad\text{soit}\qquad \frac{AN}{8{,}5} = \frac{2{,}7}{5{,}2} \qquad\text{donc}\qquad AN = \frac{8{,}5 \times 2{,}7}{5{,}2} \approx 4{,}4 \text{ cm}. \]
$4{,}4 > 4$ : l'élève \textbf{a tort}.
\end{reponse}
\q{6}{Aire du triangle AHC.}
\begin{reponse}
Le triangle est rectangle en $H$ : $\mathcal{A} = \dfrac{HC \times AH}{2} \approx \dfrac{7 \times 4{,}8}{2} \approx \mathbf{16{,}8}$ cm².
\end{reponse}
'''),
dict(id='2023-mets-3equ', s='mets', ex=3, extra=True, titre='Exercice 3 -- La piscine, une équation', theme='Résoudre une équation du premier degré',
     consigne='Traite seulement la question 3.a.', regions=[(5, 296, 314)], s3=7, n3=[], s4=16, n4=[38],
     corr=r'''
\q{3.a}{Résoudre $5{,}90x = 4{,}40x + 30$.}
\begin{reponse}
\[ 5{,}9x = 4{,}4x + 30 \iff 5{,}9x - 4{,}4x = 30 \iff 1{,}5x = 30 \iff x = \frac{30}{1{,}5} = \mathbf{20}. \]
\end{reponse}
'''),
]
