# DNB Métropole – Antilles-Guyane, 26 juin 2025
# s3/s4 : séquence de rangement (3e / 4e) ; n3 : notions de 3e nécessaires (hors programme de 4e) ;
# n4 : notions de 4e nécessaires (None = pas proposé en 4e)
QCM = (2, 397, 493)   # consigne du QCM (page, y0, y1)
PARTS = [
dict(id='2025-metj-1', s='metj', ex=1, titre='Exercice 1 -- Deux urnes', theme='Probabilités, multiples, nombres premiers',
     regions=[(1, 205, 462)], s3=22, n3=[], s4=20, n4=[13, 14, 47],
     corr=r'''
\q{1}{Probabilité d'obtenir un nombre pair dans l'urne A.}
\begin{reponse}
L'urne A contient 6 boules, dont 4 portent un nombre pair : 10, 12, 24 et 30. Les tirages sont équiprobables, donc
\[ p = \frac{4}{6} = \frac{2}{3}. \]
\end{reponse}
\q{2}{Justifier que la probabilité d'obtenir un nombre premier dans l'urne B est $\frac13$.}
\begin{reponse}
Dans l'urne B (9 boules), les nombres premiers sont 2, 5 et 17 (6, 8, 18, 22 sont pairs, 21 $=3\times7$, 25 $=5\times5$).
\[ p = \frac{3}{9} = \frac{1}{3}. \]
\end{reponse}
\q{3}{Quelle urne contient le plus de multiples de 6 ?}
\begin{reponse}
Urne A : 12, 24 et 30, soit 3 boules. Urne B : 6 et 18, soit 2 boules.\\
C'est l'urne A qui contient le plus de boules portant un multiple de 6.
\end{reponse}
\q{4}{Probabilité d'obtenir un nombre supérieur ou égal à 20.}
\begin{reponse}
Urne A : 24 et 30, donc $p_A = \dfrac{2}{6} = \dfrac{1}{3}$.\qquad Urne B : 21, 22 et 25, donc $p_B = \dfrac{3}{9} = \dfrac{1}{3}$.\\
La probabilité est la même, $\dfrac13$, quelle que soit l'urne choisie.
\end{reponse}
\q{5}{On ajoute une boule numérotée 50 dans chaque urne.}
\begin{reponse}
Urne A : 7 boules dont 3 supérieures ou égales à 20, donc $p_A = \dfrac{3}{7} \approx 0{,}43$.\\
Urne B : 10 boules dont 4 supérieures ou égales à 20, donc $p_B = \dfrac{4}{10} = 0{,}4$.\\
$\dfrac37 = \dfrac{30}{70}$ et $\dfrac{4}{10} = \dfrac{28}{70}$ : les probabilités ne sont plus égales (l'urne A est plus favorable).
\end{reponse}
'''),
dict(id='2025-metj-2a', s='metj', ex=2, titre='Exercice 2 -- Aquathlon, questions 1 à 3.a',
     theme='Pythagore, réciproque de Thalès', consigne='Traite les questions 1, 2 et 3.a.',
     regions=[(1, 464, 790), (2, 128, 218)], s3=20, n3=[], s4=19, n4=[10, 45],
     corr=r'''
\q{1}{Justifier que AD = 200 m.}
\begin{reponse}
Les points $A$, $D$, $E$ sont alignés dans cet ordre, donc $AD = AE - DE = 250 - 50 = 200$ m.
\end{reponse}
\q{2}{Calculer la longueur CD.}
\begin{reponse}
Le triangle $ADC$ est rectangle en $A$, j'utilise le théorème de Pythagore :
\begin{align*}
CD^2 &= AC^2 + AD^2\\
CD^2 &= 480^2 + 200^2 = 230\,400 + 40\,000 = 270\,400\\
CD &= \sqrt{270\,400} = 520 \text{ m}
\end{align*}
\end{reponse}
\q{3.a}{Les droites (CD) et (BE) sont-elles parallèles ?}
\begin{reponse}
$AB = AC + CB = 480 + 120 = 600$ m.
\[ \frac{AC}{AB} = \frac{480}{600} = 0{,}8 \qquad\text{et}\qquad \frac{AD}{AE} = \frac{200}{250} = 0{,}8. \]
Les points $A$, $C$, $B$ et $A$, $D$, $E$ sont alignés dans le même ordre et $\dfrac{AC}{AB} = \dfrac{AD}{AE}$.\\
D'après la réciproque du théorème de Thalès, les droites $(CD)$ et $(BE)$ sont parallèles.
\end{reponse}
'''),
dict(id='2025-metj-2b', s='metj', ex=2, titre='Exercice 2 -- Aquathlon, questions 3.b et 3.c',
     theme='Trigonométrie', consigne='Traite les questions 3.b et 3.c (on sait que AD = 200 m et que (CD) et (BE) sont parallèles).',
     regions=[(1, 464, 790), (2, 128, 262)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{3.b}{La mesure de l'angle $\widehat{ACD}$ est-elle supérieure à 20° ?}
\begin{reponse}
Dans le triangle $ADC$ rectangle en $A$, je connais le côté opposé à $\widehat{ACD}$ ($AD = 200$ m) et le côté adjacent ($AC = 480$ m) :
\[ \tan\widehat{ACD} = \frac{AD}{AC} = \frac{200}{480} \qquad\text{donc}\qquad \widehat{ACD} = \arctan\left(\frac{200}{480}\right) \approx 22{,}6^\circ. \]
L'angle $\widehat{ACD}$ mesure environ $22{,}6^\circ$ : il est bien supérieur à $20^\circ$.
\end{reponse}
\q{3.c}{Le parcours est-il validé ?}
\begin{reponse}
Les droites $(CD)$ et $(BE)$ sont parallèles (question 3.a) et $\widehat{ACD} > 20^\circ$ : les deux conditions sont remplies, le parcours est validé.
\end{reponse}
'''),
dict(id='2025-metj-2c', s='metj', ex=2, titre='Exercice 2 -- Natation, question 4', theme='Médiane',
     consigne='Traite la question 4.', regions=[(2, 265, 350)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{4}{Quel est le temps médian de cette série ?}
\begin{reponse}
Les 9 temps sont déjà rangés dans l'ordre croissant. L'effectif est impair : la médiane est la $5^{\text{e}}$ valeur ($\frac{9+1}{2} = 5$).\\
Le temps médian est \textbf{6 min} : au moins la moitié des élèves a nagé en 6 min ou moins.
\end{reponse}
'''),
dict(id='2025-metj-2d', s='metj', ex=2, titre='Exercice 2 -- Natation, question 5', theme='Vitesse',
     consigne='Traite la question 5.', regions=[(2, 265, 334), (2, 350, 396)], s3=14, n3=[], s4=15, n4=[35],
     corr=r'''
\q{5}{Le poisson rouge (5 km/h) nage-t-il plus vite que l'élève le plus rapide ?}
\begin{reponse}
L'élève le plus rapide nage 200 m en 5 min 30 s, soit $5 \times 60 + 30 = 330$ s.
\[ v = \frac{d}{t} = \frac{200 \text{ m}}{330 \text{ s}} \approx 0{,}606 \text{ m/s} \qquad\text{et}\qquad 0{,}606 \times 3{,}6 \approx 2{,}2 \text{ km/h}. \]
(Autre méthode : en 1 h $= 3\,600$ s, il parcourt $200 \times \frac{3\,600}{330} \approx 2\,182$ m, soit environ 2,2 km.)\\
$2{,}2 < 5$ : le poisson rouge nage plus vite que l'élève le plus rapide.
\end{reponse}
'''),
dict(id='2025-metj-3q1', s='metj', ex=3, titre='Exercice 3 -- QCM, question 1', theme='Proportionnalité',
     regions=[QCM, (2, 493, 573)], s3=14, n3=[], s4=5, n4=[11],
     corr=r'''
\q{1}{Prix de 5 melons si 3 melons coûtent 8,40 €.}
\begin{reponse}
Un melon coûte $8{,}40 \div 3 = 2{,}80$ €, donc 5 melons coûtent $5 \times 2{,}80 = 14$ €. \textbf{Réponse C.}
\end{reponse}
'''),
dict(id='2025-metj-3q2', s='metj', ex=3, titre='Exercice 3 -- QCM, question 2', theme='Transformations',
     regions=[QCM, (2, 573, 790)], s3=11, n3=[], s4=7, n4=[16],
     corr=r'''
\q{2}{Transformation qui passe de la figure 1 à la figure 2.}
\begin{reponse}
La figure 2 est « retournée » par rapport à la figure 1 : on passe de l'une à l'autre en pliant le long d'une droite (la médiatrice du segment qui relie deux points correspondants). C'est une \textbf{symétrie axiale} : \textbf{réponse D}.\\
Une translation, une rotation ou une symétrie centrale ne retournent pas la figure.
\end{reponse}
'''),
dict(id='2025-metj-3q3', s='metj', ex=3, titre='Exercice 3 -- QCM, question 3', theme='Pourcentages',
     regions=[QCM, (3, 128, 222)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{3}{Un article de 350 € augmente de 20 \%.}
\begin{reponse}
Augmenter de 20 \%, c'est multiplier par $1 + \frac{20}{100} = 1{,}2$ : $350 \times 1{,}2 = 420$ €. \textbf{Réponse A.}
\end{reponse}
'''),
dict(id='2025-metj-3q4', s='metj', ex=3, titre='Exercice 3 -- QCM, question 4', theme='Aire, Pythagore',
     regions=[QCM, (3, 222, 366)], s3=2, n3=[], s4=4, n4=[10],
     corr=r'''
\q{4}{Aire du triangle rectangle ABC.}
\begin{reponse}
Le plus grand côté (7,5 cm) est l'hypoténuse ; les côtés de l'angle droit mesurent 4,5 cm et 6 cm
(on peut vérifier : $4{,}5^2 + 6^2 = 20{,}25 + 36 = 56{,}25 = 7{,}5^2$).
\[ \mathcal{A} = \frac{4{,}5 \times 6}{2} = 13{,}5 \text{ cm}^2. \qquad\textbf{Réponse B.} \]
\end{reponse}
'''),
dict(id='2025-metj-3q5', s='metj', ex=3, titre='Exercice 3 -- QCM, question 5', theme='Double distributivité',
     regions=[QCM, (3, 366, 446)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{5}{Forme développée et réduite de $(2x+3)(x-4)$.}
\begin{reponse}
\[ (2x+3)(x-4) = 2x \times x + 2x \times (-4) + 3 \times x + 3 \times (-4) = 2x^2 - 8x + 3x - 12 = 2x^2 - 5x - 12. \]
\textbf{Réponse A.}
\end{reponse}
'''),
dict(id='2025-metj-3q6', s='metj', ex=3, titre='Exercice 3 -- QCM, question 6', theme='Volume de la pyramide',
     regions=[QCM, (3, 446, 674)], s3=21, n3=[], s4=17, n4=[40],
     corr=r'''
\q{6}{Volume de la pyramide à base rectangulaire.}
\begin{reponse}
\[ V = \frac{\text{aire de la base} \times \text{hauteur}}{3} = \frac{4 \times 7 \times 12}{3} = \frac{336}{3} = 112 \text{ cm}^3. \qquad\textbf{Réponse B.} \]
\end{reponse}
'''),
dict(id='2025-metj-4a', s='metj', ex=4, titre='Exercice 4 -- Le programme de Zoé', theme='Programme de calcul, calcul littéral',
     consigne='Traite les questions 1 à 3 (partie A).', regions=[(3, 674, 790), (4, 128, 212)], s3=1, n3=[], s4=8, n4=[6, 19],
     corr=r'''
\q{1}{Avec 10 comme nombre de départ.}
\begin{reponse}
$10 - 4 = 6$ ;\quad $6 \times 2 = 12$ ;\quad $12 + 8 = 20$. On obtient bien 20.
\end{reponse}
\q{2}{Avec $-7$ comme nombre de départ.}
\begin{reponse}
$-7 - 4 = -11$ ;\quad $-11 \times 2 = -22$ ;\quad $-22 + 8 = -14$. On obtient $-14$.
\end{reponse}
\q{3}{Le résultat est-il toujours le double du nombre de départ ?}
\begin{reponse}
Je note $x$ le nombre de départ. Le programme donne :
\[ (x - 4) \times 2 + 8 = 2x - 8 + 8 = 2x. \]
Le résultat est toujours $2x$, le double du nombre de départ : Zoé a raison.
\end{reponse}
'''),
dict(id='2025-metj-4b', s='metj', ex=4, titre='Exercice 4 -- Le programme de Fred (Scratch)', theme='Expression littérale, équation, Scratch',
     consigne='Traite les questions 4 à 6 (partie B).', regions=[(4, 212, 596)], s3=7, n3=[], s4=16, n4=[6, 20, 38],
     corr=r'''
\q{4}{Démontrer que le programme de Fred donne $20x + 50$.}
\begin{reponse}
Avec le nombre de départ $x$ : résultat $= x \times 4 = 4x$, puis $4x + 10$, puis $(4x + 10) \times 5 = 20x + 50$.
\end{reponse}
\q{5}{Quel nombre choisir pour obtenir 75 ?}
\begin{reponse}
Je résous l'équation $20x + 50 = 75$ :
\[ 20x = 75 - 50 = 25 \qquad\text{donc}\qquad x = \frac{25}{20} = 1{,}25. \]
Il faut choisir \textbf{1,25}. (Vérification : $20 \times 1{,}25 + 50 = 25 + 50 = 75$.)
\end{reponse}
\q{6}{Compléter la sixième ligne pour obtenir toujours 20 fois le nombre de départ.}
\begin{reponse}
Le programme donne $20x + 50$ ; pour obtenir $20x$, il faut retirer 50 :\\
\texttt{mettre résultat à \fbox{résultat} - \fbox{50}}
\end{reponse}
'''),
dict(id='2025-metj-5a', s='metj', ex=5, titre='Exercice 5 -- Achat ou location ? (partie A)', theme='Calculs, tableur',
     consigne='Traite les questions 1 à 3 (partie A).', regions=[(4, 596, 790), (5, 128, 240)], s3=17, n3=[], s4=9, n4=[21],
     corr=r'''
\q{1}{Dépense avec l'option Achat à la fin de la première année.}
\begin{reponse}
$22\,400 + 12 \times 75 = 22\,400 + 900 = 23\,300$ €.
\end{reponse}
\q{2}{Économie réalisée après 36 mois avec l'option Location.}
\begin{reponse}
Option Achat : $22\,400 + 36 \times 75 = 22\,400 + 2\,700 = 25\,100$ €.\qquad Option Location : $36 \times 425 = 15\,300$ €.\\
Économie : $25\,100 - 15\,300 = 9\,800$ €.
\end{reponse}
\q{3}{Formule à saisir en B3.}
\begin{reponse}
\texttt{=425*B1}\qquad (la dépense de location est 425 € multiplié par le nombre de mois, écrit en ligne 1).
\end{reponse}
'''),
dict(id='2025-metj-5b', s='metj', ex=5, titre='Exercice 5 -- Achat ou location ? (partie B)', theme='Fonctions affines, lecture graphique',
     consigne='Traite les questions 4 et 5 (partie B).', regions=[(4, 596, 704), (5, 246, 404), (6, 128, 545)], s3=17, n3=[26, 13], s4=None, n4=None,
     corr=r'''
\q{4}{Expression de $f(x)$ (option Achat).}
\begin{reponse}
Achat : 22\,400 € une fois, puis 75 € par mois. Donc $f(x) = 75x + 22\,400$.
\end{reponse}
\q{5}{À partir de combien de mois l'option Achat est-elle la plus avantageuse ?}
\begin{reponse}
Les droites $\mathcal{C}_f$ et $\mathcal{C}_g$ se coupent au point d'abscisse 64. Après ce point, $\mathcal{C}_f$ est en dessous de $\mathcal{C}_g$ : l'achat coûte moins cher que la location.\\
L'option Achat est la plus avantageuse \textbf{à partir de 65 mois} (à 64 mois, les deux options coûtent la même chose).\\[2pt]
\small Vérification par le calcul : $425x = 75x + 22\,400 \iff 350x = 22\,400 \iff x = 64$.
\end{reponse}
'''),
]
