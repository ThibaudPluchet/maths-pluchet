# DNB Amérique du Nord, 4 juin 2025
H1 = (1, 212, 277)
PARTS = [
dict(id='2025-anor-1s1', s='anor', ex=1, titre='Exercice 1 -- Situation 1', theme='Probabilités',
     regions=[H1, (1, 277, 343)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{1}{Probabilité d'obtenir une boule verte.}
\begin{reponse}
20 boules vertes sur 40, tirées au hasard : $p = \dfrac{20}{40} = \dfrac12 = 0{,}5$.
\end{reponse}
'''),
dict(id='2025-anor-1s2', s='anor', ex=1, titre='Exercice 1 -- Situation 2', theme='Décomposition en facteurs premiers',
     regions=[H1, (1, 343, 390)], s3=24, n3=[], s4=6, n4=[14],
     corr=r'''
\q{2}{Décomposer 1 050 en produit de facteurs premiers.}
\begin{reponse}
$1\,050 = 2 \times 525 = 2 \times 3 \times 175 = 2 \times 3 \times 5 \times 35 = 2 \times 3 \times 5^2 \times 7$.
\end{reponse}
'''),
dict(id='2025-anor-1s3', s='anor', ex=1, titre='Exercice 1 -- Situation 3', theme='Pourcentages',
     regions=[H1, (1, 390, 422)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{3}{Prix d'un article de 25 € après une augmentation de 14 \%.}
\begin{reponse}
Augmenter de 14 \%, c'est multiplier par $1{,}14$ : $25 \times 1{,}14 = 28{,}50$ €.
\end{reponse}
'''),
dict(id='2025-anor-1s4', s='anor', ex=1, titre='Exercice 1 -- Situation 4', theme='Agrandissement et aires',
     regions=[H1, (1, 422, 567)], s3=21, n3=[], s4=17, n4=[41],
     corr=r'''
\q{4}{Aire du polygone 2 (agrandissement de coefficient 2,5 d'un polygone de 7,5 cm²).}
\begin{reponse}
Dans un agrandissement de coefficient $k$, les aires sont multipliées par $k^2$. Ici $k^2 = 2{,}5^2 = 6{,}25$.
\[ \mathcal{A}_2 = 7{,}5 \times 6{,}25 = 46{,}875 \text{ cm}^2. \]
\end{reponse}
'''),
dict(id='2025-anor-1s5', s='anor', ex=1, titre='Exercice 1 -- Situation 5', theme='Moyenne, médiane',
     regions=[H1, (1, 567, 715)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{1}{Moyenne des tailles.}
\begin{reponse}
Effectif total : $2 + 4 + 2 + 5 + 2 + 4 + 6 + 5 = 30$ élèves.
\[ \bar{x} = \frac{2 \times 152 + 4 \times 157 + 2 \times 160 + 5 \times 162 + 2 \times 165 + 4 \times 170 + 6 \times 174 + 5 \times 180}{30} = \frac{5\,016}{30} = 167{,}2 \text{ cm}. \]
\end{reponse}
\q{2}{Médiane des tailles.}
\begin{reponse}
L'effectif est pair (30) : la médiane est la moyenne des $15^{\text{e}}$ et $16^{\text{e}}$ valeurs.\\
Effectifs cumulés : 2 ; 6 ; 8 ; 13 ; \textbf{15} ; 19 ; \ldots\ La $15^{\text{e}}$ valeur est 165 cm et la $16^{\text{e}}$ est 170 cm.
\[ \text{médiane} = \frac{165 + 170}{2} = 167{,}5 \text{ cm}. \]
\end{reponse}
'''),
dict(id='2025-anor-2a', s='anor', ex=2, titre='Exercice 2 -- Géométrie, questions 1 à 3', theme='Pythagore, parallélisme, Thalès',
     consigne='Traite les questions 1 à 3.', regions=[(2, 134, 610)], s3=9, n3=[], s4=19, n4=[10, 22],
     corr=r'''
\q{1}{Calculer la longueur AB.}
\begin{reponse}
Le triangle $ABC$ est rectangle en $B$, d'hypoténuse $[AC]$. D'après le théorème de Pythagore :
\[ AB^2 = AC^2 - BC^2 = 50^2 - 30^2 = 2\,500 - 900 = 1\,600 \qquad\text{donc}\qquad AB = \sqrt{1\,600} = 40 \text{ m}. \]
\end{reponse}
\q{2}{Montrer que les droites (DE) et (BC) sont parallèles.}
\begin{reponse}
$(DE) \perp (AE)$ (triangle $ADE$ rectangle en $E$) et $(BC) \perp (AB)$ (triangle $ABC$ rectangle en $B$). Les points $A$, $B$, $E$ sont alignés : $(DE)$ et $(BC)$ sont perpendiculaires à la même droite, elles sont donc parallèles.
\end{reponse}
\q{3}{Montrer que DE = 42 m.}
\begin{reponse}
Les points $A$, $B$, $E$ et $A$, $C$, $D$ sont alignés, et $(BC) \parallel (DE)$. D'après le théorème de Thalès :
\[ \frac{AB}{AE} = \frac{AC}{AD} = \frac{BC}{DE} \qquad\text{soit}\qquad \frac{50}{70} = \frac{30}{DE} \qquad\text{donc}\qquad DE = \frac{30 \times 70}{50} = 42 \text{ m}. \]
\end{reponse}
'''),
dict(id='2025-anor-2b', s='anor', ex=2, titre='Exercice 2 -- Géométrie, questions 4 et 5', theme='Trigonométrie, aire',
     consigne='Traite les questions 4 et 5 (on sait que AB = 40 m et DE = 42 m).', regions=[(2, 134, 559), (2, 610, 645)], s3=15, n3=[24], s4=None, n4=None,
     corr=r'''
\q{4}{Montrer que EM $\approx$ 24,2 m.}
\begin{reponse}
Dans le triangle $DME$ rectangle en $E$, $[DE]$ est le côté opposé à l'angle $\widehat{DME}$ et $[EM]$ le côté adjacent :
\[ \tan\widehat{DME} = \frac{DE}{EM} \qquad\text{donc}\qquad EM = \frac{DE}{\tan 60^\circ} = \frac{42}{\tan 60^\circ} \approx 24{,}2 \text{ m}. \]
\end{reponse}
\q{5}{En déduire l'aire du triangle AMD.}
\begin{reponse}
D'après Thalès, $\dfrac{AE}{AB} = \dfrac{AD}{AC}$, donc $AE = \dfrac{40 \times 70}{50} = 56$ m. Le point $M$ est entre $A$ et $E$ :
$AM = AE - EM \approx 56 - 24{,}25 = 31{,}75$ m.\\
$[DE]$ est la hauteur du triangle $AMD$ issue de $D$ (perpendiculaire à $(AM)$) :
\[ \mathcal{A}_{AMD} = \frac{AM \times DE}{2} \approx \frac{31{,}75 \times 42}{2} \approx 666{,}8 \text{ m}^2. \]
\end{reponse}
'''),
dict(id='2025-anor-3a', s='anor', ex=3, titre='Exercice 3 -- Le programme A, questions 1 à 3', theme='Programme de calcul, calcul littéral',
     consigne='Traite les questions 1 à 3.', regions=[(3, 134, 438)], s3=1, n3=[], s4=8, n4=[6, 19],
     corr=r'''
\q{1}{Avec 4 comme nombre de départ (programme A).}
\begin{reponse}
$4 \times 3 = 12$ ; $12 + 15 = 27$ ; $27 \div 3 = 9$ ; $9 - 4 = 5$. On obtient bien 5.
\end{reponse}
\q{2}{Avec $-2$ comme nombre de départ (programme A).}
\begin{reponse}
$-2 \times 3 = -6$ ; $-6 + 15 = 9$ ; $9 \div 3 = 3$ ; $3 - (-2) = 5$. On obtient bien 5.
\end{reponse}
\q{3}{« Le programme A donne toujours le même résultat. »}
\begin{reponse}
Avec le nombre de départ $x$ :
\[ \frac{3x + 15}{3} - x = \frac{3x}{3} + \frac{15}{3} - x = x + 5 - x = 5. \]
Le résultat est toujours 5, quel que soit le nombre choisi : l'affirmation est vraie.
\end{reponse}
'''),
dict(id='2025-anor-3b', s='anor', ex=3, titre='Exercice 3 -- Le programme B, questions 4 et 5', theme='Équation produit',
     consigne='Traite les questions 4 et 5 (le programme A donne toujours 5).', regions=[(3, 134, 351), (3, 438, 500)], s3=19, n3=[32], s4=None, n4=None,
     corr=r'''
\q{4}{Résultat du programme B avec 10.}
\begin{reponse}
$10 - 1 = 9$ et $10 - 6 = 4$ ; $9 \times 4 = 36$ ; $36 + 5 = 41$.
\end{reponse}
\q{5}{Les deux nombres pour lesquels les programmes A et B donnent le même résultat.}
\begin{reponse}
Le programme A donne toujours 5 ; le programme B donne $(x - 1)(x - 6) + 5$. Je résous :
\[ (x - 1)(x - 6) + 5 = 5 \iff (x - 1)(x - 6) = 0. \]
Un produit est nul si l'un de ses facteurs est nul : $x - 1 = 0$ ou $x - 6 = 0$, soit $x = 1$ ou $x = 6$.\\
Les deux nombres sont \textbf{1 et 6}.
\end{reponse}
'''),
dict(id='2025-anor-4', s='anor', ex=4, titre="Exercice 4 -- L'entraînement de Malo", theme='Lecture graphique, vitesses',
     regions=[(4, 134, 725)], s3=14, n3=[], s4=15, n4=[12, 35],
     corr=r'''
\q{1}{Le temps et la distance sont-ils proportionnels ?}
\begin{reponse}
Non : la courbe n'est pas une droite passant par l'origine (il y a notamment un palier où la distance ne change pas).
\end{reponse}
\q{2}{Distance parcourue au bout de 20 minutes.}
\begin{reponse}
On lit environ \textbf{4,5 km}.
\end{reponse}
\q{3}{Temps mis pour les 9 premiers kilomètres.}
\begin{reponse}
On lit environ \textbf{50 minutes}.
\end{reponse}
\q{4}{Vitesse moyenne de Malo, au dixième de km/h.}
\begin{reponse}
Malo parcourt 13,5 km en 80 min (lecture graphique), soit $\dfrac{80}{60} = \dfrac43$ h.
\[ v = \frac{13{,}5}{\frac43} = 13{,}5 \times \frac34 = 10{,}125 \approx 10{,}1 \text{ km/h}. \]
\end{reponse}
\q{5.a}{Qui de Louise (12 km/h) ou Hillal (10 km/h) arrive le premier ?}
\begin{reponse}
Sur la même distance, partis en même temps, c'est le plus rapide qui arrive le premier : \textbf{Louise}.
\end{reponse}
\q{5.b}{Distance entre Louise et Hillal quand Louise arrive.}
\begin{reponse}
Durée de course de Louise : $t = \dfrac{13{,}5}{12} = 1{,}125$ h. Pendant ce temps, Hillal parcourt $10 \times 1{,}125 = 11{,}25$ km.\\
Il est encore à $13{,}5 - 11{,}25 = 2{,}25$ km de l'arrivée : \textbf{2,25 km} les séparent.
\end{reponse}
'''),
dict(id='2025-anor-5a', s='anor', ex=5, titre='Exercice 5 -- Les motifs, partie 1 (Scratch)', theme='Algorithmique (Scratch)',
     consigne='Traite la partie 1.', regions=[(5, 134, 790), (6, 128, 190)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Associer les scripts 1 et 2 à leur dessin.}
\begin{reponse}
Script 1 (3 côtés, $120^\circ$) : un triangle équilatéral, c'est le \textbf{dessin 2}.\\
Script 2 (6 côtés, $60^\circ$) : un hexagone régulier, c'est le \textbf{dessin 1}.
\end{reponse}
\q{2}{Instructions cachées du script 3, dans le bon ordre.}
\begin{reponse}
\texttt{tourner de 120 degrés} (instruction B), puis \texttt{avancer de 30 pas} (instruction C), puis \texttt{tourner de 60 degrés} (instruction A).\\
Répété 2 fois, cela trace les 4 côtés de 30 pas du losange, avec des angles de $60^\circ$ et $120^\circ$.
\end{reponse}
'''),
dict(id='2025-anor-5b', s='anor', ex=5, titre='Exercice 5 -- Le script principal, partie 2', theme='Scratch, probabilités, fréquences',
     consigne='Traite la partie 2.', regions=[(5, 134, 183), (7, 128, 730), (8, 128, 345), (9, 128, 280)], s3=22, n3=[], s4=20, n4=[47, 48],
     corr=r'''
\q{3}{Coordonnées du point de départ du lutin.}
\begin{reponse}
$(-200\,;\,0)$ : c'est l'instruction « aller à x : $-200$ y : 0 ».
\end{reponse}
\q{4}{Quelles sont les deux captures d'écran possibles ?}
\begin{reponse}
Si le nombre aléatoire est 3, le lutin trace 6 losanges espacés de 60 pas et dit « Voici le dessin ! » : \textbf{capture n\textsuperscript{o}~2}.\\
Si c'est 1 ou 2, il ne dessine rien et dit « Perdu ! » : \textbf{capture n\textsuperscript{o}~3}.
\end{reponse}
\q{5}{Probabilité que le message soit « Voici le dessin ! ».}
\begin{reponse}
Le message s'affiche seulement si le nombre aléatoire est 3 : 1 cas sur 3 équiprobables. $p = \dfrac13$.
\end{reponse}
\q{6.a}{Fréquence de l'affichage « Voici le dessin ! » sur 100 lancers.}
\begin{reponse}
$\dfrac{40}{100} = 0{,}4$, soit 40 \%.
\end{reponse}
\q{6.b}{Pourquoi ce résultat est-il différent de celui de la question 5 ?}
\begin{reponse}
La fréquence observée varie d'une série d'expériences à l'autre. Elle se rapproche de la probabilité $\frac13 \approx 0{,}33$ quand le nombre d'essais devient très grand ; 100 lancers ne suffisent pas pour qu'elle soit égale à la probabilité.
\end{reponse}
'''),
]
