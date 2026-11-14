# DNB Centres étrangers, 17 juin 2025
QCM = (1, 195, 276)
PARTS = [
dict(id='2025-cetr-1q1', s='cetr', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Décomposition en facteurs premiers',
     regions=[QCM, (1, 274, 356)], s3=24, n3=[], s4=6, n4=[14],
     corr=r'''
\q{1}{Décomposition en produit de facteurs premiers de 120.}
\begin{reponse}
$120 = 2 \times 60 = 2 \times 2 \times 30 = 2 \times 2 \times 2 \times 15 = 2^3 \times 3 \times 5$. \textbf{Réponse C.}\\
(4 et 15 ne sont pas premiers ; $53 + 67$ est une somme.)
\end{reponse}
'''),
dict(id='2025-cetr-1q2', s='cetr', ex=1, titre='Exercice 1 -- QCM, question 2', theme='Tableur, calcul avec des relatifs',
     regions=[QCM, (1, 354, 472)], s3=1, n3=[], s4=1, n4=[2, 18],
     corr=r'''
\q{2}{Valeur obtenue en B2.}
\begin{reponse}
En étirant la formule, elle devient \texttt{=-4*B1-12} en B2, avec B1 $= 5$ :
$-4 \times 5 - 12 = -20 - 12 = -32$. \textbf{Réponse A.}
\end{reponse}
'''),
dict(id='2025-cetr-1q3', s='cetr', ex=1, titre='Exercice 1 -- QCM, question 3', theme='Homothétie',
     regions=[QCM, (1, 470, 596)], s3=18, n3=[30], s4=None, n4=None,
     corr=r'''
\q{3}{Rapport de l'homothétie de centre O qui transforme le carré A en le carré B.}
\begin{reponse}
Les dimensions du carré B sont le double de celles du carré A, et B est du même côté de $O$ que A : le rapport est \textbf{2}. \textbf{Réponse D.}
\end{reponse}
'''),
dict(id='2025-cetr-1q4', s='cetr', ex=1, titre='Exercice 1 -- QCM, question 4', theme='Identité remarquable',
     regions=[QCM, (1, 594, 675)], s3=12, n3=[19], s4=None, n4=None,
     corr=r'''
\q{4}{Écriture factorisée de $4x^2 - 1$.}
\begin{reponse}
$4x^2 - 1 = (2x)^2 - 1^2 = (2x - 1)(2x + 1)$, avec $a^2 - b^2 = (a - b)(a + b)$. \textbf{Réponse A.}
\end{reponse}
'''),
dict(id='2025-cetr-1q5', s='cetr', ex=1, titre='Exercice 1 -- QCM, question 5', theme='Trigonométrie (calcul de longueur)',
     regions=[QCM, (1, 673, 805), (2, 128, 172)], s3=15, n3=[24], s4=None, n4=None,
     corr=r'''
\q{5}{Longueur RE, au centième.}
\begin{reponse}
Le triangle $TER$ est rectangle en $R$ ; l'hypoténuse est $[TE]$ et $[ER]$ est le côté adjacent à l'angle $\widehat{TER}$ :
\[ \cos\widehat{TER} = \frac{ER}{ET} \qquad\text{donc}\qquad ER = 7{,}4 \times \cos 39^\circ \approx 5{,}75 \text{ cm}. \qquad\textbf{Réponse B.} \]
\end{reponse}
'''),
dict(id='2025-cetr-2a', s='cetr', ex=2, titre='Exercice 2 -- Les colis, questions 1 à 3', theme='Moyenne, médiane, probabilité',
     consigne='Traite les questions 1 à 3.', regions=[(2, 184, 352)], s3=23, n3=[], s4=11, n4=[24, 47],
     corr=r'''
\q{1}{Moyenne des masses.}
\begin{reponse}
$\dfrac{4 + 9 + 2 + 7 + 11}{5} = \dfrac{33}{5} = 6{,}6$ kg.
\end{reponse}
\q{2}{Médiane des masses, et interprétation.}
\begin{reponse}
Rangées dans l'ordre : 2 ; 4 ; \textbf{7} ; 9 ; 11. La médiane est la $3^{\text{e}}$ valeur : \textbf{7 kg}.\\
Au moins la moitié des colis pèse 7 kg ou moins, et au moins la moitié pèse 7 kg ou plus.
\end{reponse}
\q{3}{Probabilité de choisir un colis de moins de 8 kg.}
\begin{reponse}
Les colis A (4 kg), C (2 kg) et D (7 kg) pèsent moins de 8 kg : $p = \dfrac35 = 0{,}6$.
\end{reponse}
'''),
dict(id='2025-cetr-2b', s='cetr', ex=2, titre='Exercice 2 -- Les colis, question 4', theme='Volume, masse volumique',
     consigne='Traite la question 4.', regions=[(2, 184, 288), (2, 363, 800)], s3=14, n3=[23], s4=15, n4=[36],
     corr=r'''
\q{4.a}{Vérifier que le volume du colis E est 0,12 m³.}
\begin{reponse}
$V_E = 0{,}5 \times 0{,}4 \times 0{,}6 = 0{,}12 \text{ m}^3$.
\end{reponse}
\q{4.b}{Masse volumique du colis E, au dixième.}
\begin{reponse}
$\rho_E = \dfrac{11}{0{,}12} \approx 91{,}7 \text{ kg/m}^3$.
\end{reponse}
\q{4.c}{« E est plus lourd que C, donc sa masse volumique est plus grande. » A-t-il raison ?}
\begin{reponse}
$V_C = 0{,}3 \times 0{,}1 \times 0{,}5 = 0{,}015 \text{ m}^3$ et $\rho_C = \dfrac{2}{0{,}015} \approx 133{,}3 \text{ kg/m}^3$.\\
$133{,}3 > 91{,}7$ : le colis C a une masse volumique plus grande que E. Le transporteur \textbf{a tort} (la masse volumique dépend aussi du volume).
\end{reponse}
'''),
dict(id='2025-cetr-3a', s='cetr', ex=3, titre='Exercice 3 -- Programme de calcul, questions 1 à 4', theme='Programme de calcul, équation',
     consigne='Traite les questions 1 à 4.', regions=[(3, 137, 337)], s3=7, n3=[], s4=16, n4=[2, 6, 38],
     corr=r'''
\q{1}{Avec 1 comme nombre de départ.}
\begin{reponse}
$1 \times (-2) = -2$ ; $-2 + 4 = 2$ ; $2 \times 4 = 8$. On obtient bien 8.
\end{reponse}
\q{2}{Avec $-2$ comme nombre de départ.}
\begin{reponse}
$-2 \times (-2) = 4$ ; $4 + 4 = 8$ ; $8 \times 4 = 32$. On obtient 32.
\end{reponse}
\q{3}{Montrer que le résultat s'écrit $-8x + 16$.}
\begin{reponse}
$x \longrightarrow -2x \longrightarrow -2x + 4 \longrightarrow 4(-2x + 4) = -8x + 16$.
\end{reponse}
\q{4.a}{Résoudre $-8x + 16 = 4$.}
\begin{reponse}
$-8x + 16 = 4 \iff -8x = -12 \iff x = \dfrac{-12}{-8} = 1{,}5$.
\end{reponse}
\q{4.b}{Nombre de départ pour obtenir 4.}
\begin{reponse}
Il faut choisir \textbf{1,5}.
\end{reponse}
'''),
dict(id='2025-cetr-3b', s='cetr', ex=3, titre='Exercice 3 -- Programme de calcul, question 5', theme='Fonction affine : représentation graphique',
     consigne='Traite la question 5.', regions=[(3, 137, 245), (3, 335, 566)], s3=17, n3=[28], s4=None, n4=None,
     corr=r'''
\q{5}{Quelle représentation graphique correspond à $f(x) = -8x + 16$ ?}
\begin{reponse}
$f(0) = 16$ : la droite passe par le point $(0\,;\,16)$, ce qui élimine la représentation 2.\\
Le coefficient directeur est $-8$ : quand $x$ augmente de 1, $f(x)$ diminue de 8 (par exemple $f(2) = 0$). C'est la \textbf{représentation graphique 3}.
\end{reponse}
'''),
dict(id='2025-cetr-4a', s='cetr', ex=4, titre='Exercice 4 -- Le champ, partie A', theme='Pythagore, parallélisme, Thalès, aire',
     consigne='Traite la partie A.', regions=[(3, 564, 800), (4, 128, 212)], s3=9, n3=[], s4=19, n4=[10, 22],
     corr=r'''
\q{1}{Montrer que AC = 750 m.}
\begin{reponse}
Le triangle $ABC$ est rectangle en $B$, d'hypoténuse $[AC]$. D'après le théorème de Pythagore :
\[ AC^2 = AB^2 + BC^2 = 600^2 + 450^2 = 360\,000 + 202\,500 = 562\,500 \qquad\text{donc}\qquad AC = \sqrt{562\,500} = 750 \text{ m}. \]
\end{reponse}
\q{2.a}{Montrer que (ED) et (AB) sont parallèles.}
\begin{reponse}
D'après la figure, $(ED) \perp (BC)$, et $(AB) \perp (BC)$ car $ABC$ est rectangle en $B$. Deux droites perpendiculaires à une même droite sont parallèles : $(ED) \parallel (AB)$.
\end{reponse}
\q{2.b}{Montrer que DE = 360 m.}
\begin{reponse}
Les points $C$, $D$, $B$ et $C$, $E$, $A$ sont alignés, et $(ED) \parallel (AB)$. D'après le théorème de Thalès :
\[ \frac{CD}{CB} = \frac{CE}{CA} = \frac{DE}{BA} \qquad\text{soit}\qquad \frac{270}{450} = \frac{DE}{600} \qquad\text{donc}\qquad DE = \frac{270 \times 600}{450} = 360 \text{ m}. \]
\end{reponse}
\q{3}{Montrer que l'aire du triangle CDE est 48 600 m².}
\begin{reponse}
Le triangle $CDE$ est rectangle en $D$ : $\mathcal{A} = \dfrac{CD \times DE}{2} = \dfrac{270 \times 360}{2} = 48\,600 \text{ m}^2$.
\end{reponse}
'''),
dict(id='2025-cetr-4b', s='cetr', ex=4, titre='Exercice 4 -- Le champ, partie B', theme='Ratio, proportionnalité, prix',
     consigne="Traite la partie B (l'aire du triangle CDE est 48 600 m²).", regions=[(3, 564, 606), (4, 212, 517)], s3=14, n3=[22], s4=None, n4=None,
     corr=r'''
\q{1}{Le sac au ratio 16 : 12 : 8 respecte-t-il l'indication 2 ?}
\begin{reponse}
L'indication 2 donne 80 kg de blé, 60 kg de seigle et 50 kg de pois.
\[ \frac{80}{16} = 5 \qquad \frac{60}{12} = 5 \qquad \frac{50}{8} = 6{,}25. \]
Les quotients ne sont pas tous égaux : le ratio $16 : 12 : 8$ ne respecte pas la répartition (il faudrait 40 kg de pois pour 80 kg de blé).
\end{reponse}
\q{2}{Justifier les 388,80 kg de blé pour 48 600 m².}
\begin{reponse}
80 kg de blé pour $10\,000 \text{ m}^2$, donc pour $48\,600 \text{ m}^2$ (4,86 fois plus) : $80 \times 4{,}86 = 388{,}8$ kg.
\end{reponse}
\q{3}{Le budget de 1 500 € suffit-il ?}
\begin{reponse}
$388{,}8 \times 1{,}40 + 291{,}6 \times 1{,}30 + 243 \times 2{,}10 = 544{,}32 + 379{,}08 + 510{,}30 = 1\,433{,}70$ €.\\
$1\,433{,}70 < 1\,500$ : le budget est \textbf{suffisant}.
\end{reponse}
'''),
dict(id='2025-cetr-5', s='cetr', ex=5, titre='Exercice 5 -- Le digicode', theme='Probabilités, nombres premiers, Scratch',
     regions=[(4, 515, 800), (5, 128, 460)], s3=22, n3=[], s4=20, n4=[14, 47],
     corr=r'''
\q{1}{Deux codes possibles.}
\begin{reponse}
Par exemple \textbf{A3} et \textbf{C9}.
\end{reponse}
\q{2}{Probabilité que le code contienne la lettre C.}
\begin{reponse}
Il y a $3 \times 10 = 30$ codes possibles, dont 10 commencent par C : $p = \dfrac{10}{30} = \dfrac13$.
\end{reponse}
\q{3}{Montrer que la probabilité d'avoir le chiffre 7 est $\frac{1}{10}$.}
\begin{reponse}
Les codes A7, B7 et C7 conviennent : $p = \dfrac{3}{30} = \dfrac{1}{10}$.
\end{reponse}
\q{4}{Probabilité que le code comporte un nombre premier.}
\begin{reponse}
Entre 0 et 9, les nombres premiers sont 2, 3, 5 et 7. Il y a donc $3 \times 4 = 12$ codes favorables : $p = \dfrac{12}{30} = \dfrac25 = 0{,}4$.
\end{reponse}
\q{5.a}{Tous les codes en moins de 3 minutes ?}
\begin{reponse}
$30 \times 5 = 150$ s $= 2$ min 30 s : oui, elle aura essayé tous les codes en moins de 3 minutes.
\end{reponse}
\q{5.b}{Le code garantit-il la sécurité ? Comment l'améliorer ?}
\begin{reponse}
Non : n'importe qui peut trouver le code en moins de 3 minutes. On peut augmenter le nombre de codes possibles : par exemple utiliser les 26 lettres, ou des codes à plusieurs chiffres (avec 4 chiffres il y a $3 \times 10\,000 = 30\,000$ codes).
\end{reponse}
\q{6.a}{Léna saisit B5 : qu'affiche le programme ?}
\begin{reponse}
La condition « lettre $=$ B et chiffre $=$ 7 » est fausse (le chiffre est 5) : il affiche \textbf{« Code faux »}.
\end{reponse}
\q{6.b}{Quel est le code d'entrée ?}
\begin{reponse}
Le code correct est \textbf{B7}.
\end{reponse}
'''),
]
