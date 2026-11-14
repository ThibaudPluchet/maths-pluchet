# DNB Asie, juin 2022
SOURCE = ('dnb_asie_juin_2022.pdf', 'Asie, juin 2022')
PARTS = [
dict(id='2022-asie-1a', s='asie', ex=1, titre='Exercice 1 -- Trois situations, situation 1', theme='Programme de calcul, expression littérale',
     consigne='Traite la situation 1.', regions=[(1, 249, 533)], s3=1, n3=[], s4=8, n4=[2, 19, 20],
     corr=r'''
\q{1}{Avec 10 au départ.}
\begin{reponse}
$10 - 7 = 3$ ; $3 \times 5 = 15$ ; $15 - 2 \times 10 = 15 - 20 = \mathbf{-5}$.
\end{reponse}
\q{2}{Expression du résultat.}
\begin{reponse}
On soustrait 7, puis on multiplie le tout par 5, puis on enlève $2x$ : \textbf{expression C}, $5(x - 7) - 2x$.
\end{reponse}
'''),
dict(id='2022-asie-1b', s='asie', ex=1, titre='Exercice 1 -- Trois situations, situation 2', theme='Fonction linéaire, lecture graphique',
     consigne='Traite la situation 2.', regions=[(1, 249, 290), (1, 533, 756)], s3=17, n3=[26, 28], s4=None, n4=None,
     corr=r'''
\q{1}{Image de $-2$ par $f$.}
\begin{reponse}
Je lis l'ordonnée du point de la droite d'abscisse $-2$ : $f(-2) = \mathbf{-4}$.
\end{reponse}
\q{2}{Expression de $f(x)$.}
\begin{reponse}
$f$ est linéaire : $f(x) = ax$. Comme $A(3\,;6)$ est sur la droite, $3a = 6$, donc $a = 2$ : $\mathbf{f(x) = 2x}$.
\end{reponse}
'''),
dict(id='2022-asie-1c', s='asie', ex=1, titre='Exercice 1 -- Trois situations, situation 3', theme='Volume d’une pyramide, conversion',
     consigne='Traite la situation 3.', regions=[(1, 249, 290), (1, 756, 772), (2, 125, 268)], s3=21, n3=[35], s4=17, n4=[36, 40],
     corr=r'''
\q{3}{Le volume de la pyramide dépasse-t-il 20 L ?}
\begin{reponse}
La base est un rectangle de $30 \times 40 = 1\,200$ cm$^2$ et la hauteur est $GH = 55$ cm :
\[ V = \frac{1\,200 \times 55}{3} = 22\,000 \text{ cm}^3 = 22 \text{ dm}^3 = 22 \text{ L}. \]
$22 > 20$ : \textbf{oui}, le volume dépasse 20 L.
\end{reponse}
'''),
dict(id='2022-asie-2a', s='asie', ex=2, titre='Exercice 2 -- Le papillon, questions 1 et 2', theme='Théorème de Thalès, réciproque de Pythagore',
     consigne='Traite les questions 1 et 2.', regions=[(2, 268, 484)], s3=13, n3=[], s4=14, n4=[22, 32],
     corr=r'''
\q{1}{Démontrer que EC = 4,8 cm.}
\begin{reponse}
$(AB) \parallel (CD)$ et les droites $(AD)$ et $(BC)$ se coupent en $E$. D'après le théorème de Thalès :
\[ \frac{EB}{EC} = \frac{EA}{ED} = \frac{AB}{DC} \qquad\text{donc}\qquad \frac{7{,}2}{EC} = \frac{9}{6} \qquad\text{et}\qquad EC = \frac{7{,}2 \times 6}{9} = 4{,}8 \text{ cm}. \]
\end{reponse}
\q{2}{Le triangle ECD est-il rectangle ?}
\begin{reponse}
Le plus grand côté est $[CD]$. $CD^2 = 6^2 = 36$ et $ED^2 + EC^2 = 3{,}6^2 + 4{,}8^2 = 12{,}96 + 23{,}04 = 36$.
D'après la réciproque du théorème de Pythagore, $ECD$ est \textbf{rectangle en $E$}.
\end{reponse}
'''),
dict(id='2022-asie-2b', s='asie', ex=2, titre='Exercice 2 -- Le papillon, questions 3 et 4', theme='Homothétie, agrandissement et aires',
     consigne='Traite les questions 3 et 4.', regions=[(2, 268, 612)], s3=21, n3=[30, 37], s4=None, n4=None,
     corr=r'''
\q{3}{Transformation qui transforme ECD en ABE.}
\begin{reponse}
\textbf{Une homothétie} (de centre $E$, de rapport $-1{,}5$).
\end{reponse}
\q{4}{L'aire de ABE est-elle 1,5 fois plus grande ?}
\begin{reponse}
Les longueurs sont multipliées par 1,5, donc les aires par $1{,}5^2 = 2{,}25$. L'affirmation est \textbf{fausse}.
\end{reponse}
'''),
dict(id='2022-asie-3a', s='asie', ex=3, titre='Exercice 3 -- Les Jeux paralympiques, questions 1 à 3', theme='Lecture d’un tableau, tableur',
     consigne='Traite les questions 1 à 3.', regions=[(3, 136, 532)], s3=1, n3=[], s4=1, n4=[1],
     corr=r'''
\q{1}{Médailles d'argent de l'Australie.}
\begin{reponse}
\textbf{29} médailles d'argent.
\end{reponse}
\q{2}{Médailles de bronze de l'Italie.}
\begin{reponse}
$69 - 14 - 29 = \mathbf{26}$ médailles de bronze.
\end{reponse}
\q{3}{Formule saisie en F2.}
\begin{reponse}
\texttt{=C2+D2+E2} ou \texttt{=SOMME(C2:E2)}.
\end{reponse}
'''),
dict(id='2022-asie-3b', s='asie', ex=3, titre='Exercice 3 -- Les Jeux paralympiques, questions 4 et 5', theme='Pourcentages, médiane',
     consigne='Traite les questions 4 et 5.', regions=[(3, 136, 478), (3, 530, 674)], s3=23, n3=[], s4=15, n4=[24, 34],
     corr=r'''
\q{4}{Affirmation 1 : 20 \% des médailles françaises sont en or.}
\begin{reponse}
$\dfrac{11}{54} \approx 0{,}204$, soit environ 20 \% : l'affirmation est \textbf{vraie} (à l'arrondi près).
\end{reponse}
\q{4}{Affirmation 2 : la médiane des médailles d'argent est 29.}
\begin{reponse}
Rangées : 1 ; 11 ; 12 ; 15 ; 15 ; 15 ; 17 ; \textbf{20} ; 29 ; 29 ; 33 ; 36 ; 38 ; 47 ; 60.
Il y a 15 valeurs : la médiane est la 8\ieme{}, 20. L'affirmation est \textbf{fausse}.
\end{reponse}
\q{5}{Pourcentage d'augmentation de la prime.}
\begin{reponse}
L'augmentation est de $65\,000 - 50\,000 = 15\,000$ € et $\dfrac{15\,000}{50\,000} = 0{,}3$ : la prime a augmenté de \textbf{30 \%}.
\end{reponse}
'''),
dict(id='2022-asie-4a', s='asie', ex=4, titre='Exercice 4 -- Les photos, question 1', theme='Calculs de prix',
     consigne='Traite seulement la question 1.', regions=[(4, 136, 274)], s3=14, n3=[], s4=5, n4=[11],
     corr=r'''
\q{1.a}{Prix pour 35 photos.}
\begin{reponse}
$35 \times 0{,}17 = \mathbf{5{,}95}$ €.
\end{reponse}
\q{1.b}{Prix pour 150 photos.}
\begin{reponse}
$17 + 50 \times 0{,}13 = 17 + 6{,}50 = \mathbf{23{,}50}$ €.
\end{reponse}
\q{1.c}{Nombre maximum de photos pour 10 €.}
\begin{reponse}
$10 \div 0{,}17 \approx 58{,}8$ : on peut commander au maximum \textbf{58 photos} ($58 \times 0{,}17 = 9{,}86$ €).
\end{reponse}
'''),
dict(id='2022-asie-4b', s='asie', ex=4, titre='Exercice 4 -- Les photos, question 2', theme='Algorithmique (Scratch)',
     consigne='Traite seulement la question 2.', regions=[(4, 136, 226), (4, 274, 616)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{2}{Valeurs des lignes 4, 5 et 8.}
\begin{reponse}
Ligne 4 : Nb photos < \textbf{101} ; ligne 5 : Nb photos * \textbf{0.17} ; ligne 8 : \textbf{17} + Nb photos supplémentaires * 0.13.
\end{reponse}
'''),
dict(id='2022-asie-4c', s='asie', ex=4, titre='Exercice 4 -- Les photos, question 3', theme='Pourcentage de réduction',
     consigne='Traite seulement la question 3 (150 photos coûtent 23,50 €).', regions=[(4, 136, 226), (4, 274, 554), (4, 616, 792)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{3.a}{Prix de 150 photos en période de soldes.}
\begin{reponse}
$23{,}50 > 20$ : la réduction s'applique. $23{,}50 \times 0{,}7 = \mathbf{16{,}45}$ €.
\end{reponse}
\q{3.b}{Proposition qui convient.}
\begin{reponse}
Baisser de 30 \%, c'est enlever $0{,}3 \times$ Prix, ou multiplier par 0,7 : la \textbf{proposition 2} ou la \textbf{proposition 4}.
\end{reponse}
'''),
dict(id='2022-asie-5a', s='asie', ex=5, titre='Exercice 5 -- L’ISS, question 1', theme='Latitude et longitude',
     consigne='Traite seulement la question 1.', regions=[(5, 136, 546)], s3=6, n3=[9], s4=None, n4=None,
     corr=r'''
\q{1}{Coordonnées de Canberra et de Miami.}
\begin{reponse}
Miami : environ \textbf{(80°O ; 25°N)}. Canberra : environ \textbf{(150°E ; 35°S)}.
\end{reponse}
'''),
dict(id='2022-asie-5b', s='asie', ex=5, titre='Exercice 5 -- L’ISS, questions 2 et 3', theme='Périmètre du cercle, vitesse, durées',
     consigne='Traite les questions 2 et 3.', regions=[(5, 136, 188), (5, 546, 792), (6, 125, 183)], s3=14, n3=[], s4=15, n4=[35, 36],
     corr=r'''
\q{2}{Longueur d'un tour.}
\begin{reponse}
Le rayon de l'orbite est $6\,371 + 380 = 6\,751$ km : $2 \times \pi \times 6\,751 \approx 42\,418$ km, soit environ \textbf{42\,400 km}.
\end{reponse}
\q{3.a}{Durée d'un tour.}
\begin{reponse}
$t = \dfrac{42\,400}{27\,600} \approx 1{,}536$ h ; $0{,}536 \times 60 \approx 32$ min : environ \textbf{1 h 32 min}.
\end{reponse}
\q{3.b}{Nombre de tours complets pendant la sortie.}
\begin{reponse}
La sortie dure de 14 h 30 à 21 h 45, soit 7 h 15 min $= 435$ min. Un tour dure 92 min et $435 = 4 \times 92 + 67$ : \textbf{4 tours complets}.
\end{reponse}
'''),
]
