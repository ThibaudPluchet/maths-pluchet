# DNB Polynésie, juin 2025
QCM = (3, 136, 235)
PARTS = [
dict(id='2025-polj-1a', s='polj', ex=1, titre="Exercice 1 -- L'escalade, questions 1 à 5", theme='Statistiques, tableur, moyenne',
     consigne='Traite les questions 1 à 5.', regions=[(1, 195, 506)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{1}{Nombre d'élèves de 12 ans.}
\begin{reponse}
On lit dans la colonne D : \textbf{8} élèves ont 12 ans.
\end{reponse}
\q{2}{Nombre total d'élèves inscrits.}
\begin{reponse}
$1 + 3 + 8 + 12 + 4 + 2 = 30$ élèves.
\end{reponse}
\q{3}{Formule à saisir dans la cellule H2.}
\begin{reponse}
\texttt{=SOMME(B2:G2)}\quad (ou \texttt{=B2+C2+D2+E2+F2+G2}).
\end{reponse}
\q{4}{« $\frac15$ des élèves ont 14 ans ou plus » : a-t-il raison ?}
\begin{reponse}
Élèves de 14 ans ou plus : $4 + 2 = 6$. \quad $\dfrac{6}{30} = \dfrac{1}{5}$ : le professeur a raison.
\end{reponse}
\q{5}{La moyenne des âges a-t-elle augmenté (elle était de 13 ans) ?}
\begin{reponse}
\[ \bar{x} = \frac{10 \times 1 + 11 \times 3 + 12 \times 8 + 13 \times 12 + 14 \times 4 + 15 \times 2}{30} = \frac{10 + 33 + 96 + 156 + 56 + 30}{30} = \frac{381}{30} = 12{,}7. \]
$12{,}7 < 13$ : la moyenne des âges a diminué, elle n'a pas augmenté.
\end{reponse}
'''),
dict(id='2025-polj-1b', s='polj', ex=1, titre="Exercice 1 -- L'escalade, question 6", theme='Pourcentages',
     consigne="Traite la question 6 (il y a 30 inscrits cette année).", regions=[(1, 195, 326), (1, 506, 542)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{6}{Nombre d'inscrits l'an prochain avec une hausse de 10 \%.}
\begin{reponse}
Augmenter de 10 \%, c'est multiplier par 1,1 : $30 \times 1{,}1 = 33$.\\
(Ou : 10 \% de 30, c'est 3 ; $30 + 3 = 33$.) Il y aura 33 élèves inscrits.
\end{reponse}
'''),
dict(id='2025-polj-2a', s='polj', ex=2, titre='Exercice 2 -- Le jardin botanique, questions 1 et 2', theme='Théorème de Pythagore',
     consigne='Traite les questions 1 et 2.', regions=[(2, 136, 396)], s3=2, n3=[], s4=4, n4=[10],
     corr=r'''
\q{1}{Longueur du segment [DB].}
\begin{reponse}
$E$ est sur le segment $[BD]$, donc $DB = DE + EB = 750 + 250 = 1\,000$ m.
\end{reponse}
\q{2}{Montrer que AD $\approx$ 866 m.}
\begin{reponse}
Le triangle $ABD$ est rectangle en $A$ ; son hypoténuse est $[BD]$. D'après le théorème de Pythagore :
\begin{align*}
BD^2 &= AB^2 + AD^2\\
AD^2 &= BD^2 - AB^2 = 1\,000^2 - 500^2 = 1\,000\,000 - 250\,000 = 750\,000\\
AD &= \sqrt{750\,000} \approx 866{,}03 \text{ m, soit environ } 866 \text{ m au mètre près.}
\end{align*}
\end{reponse}
'''),
dict(id='2025-polj-2b', s='polj', ex=2, titre='Exercice 2 -- Le jardin botanique, question 3', theme='Trigonométrie (sinus)',
     consigne='Traite la question 3 (le triangle AEB est rectangle en E).', regions=[(2, 136, 340), (2, 394, 440)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{3.a}{Calculer le sinus de l'angle $\widehat{EAB}$.}
\begin{reponse}
Dans le triangle $AEB$ rectangle en $E$, l'hypoténuse est $[AB]$ et $[EB]$ est le côté opposé à $\widehat{EAB}$ :
\[ \sin\widehat{EAB} = \frac{EB}{AB} = \frac{250}{500} = 0{,}5. \]
\end{reponse}
\q{3.b}{En déduire la mesure de l'angle $\widehat{EAB}$.}
\begin{reponse}
$\widehat{EAB} = \arcsin(0{,}5) = 30^\circ$.
\end{reponse}
'''),
dict(id='2025-polj-2c', s='polj', ex=2, titre='Exercice 2 -- Le jardin botanique, question 4', theme='Parallélisme, théorème de Thalès',
     consigne='Traite la question 4.', regions=[(2, 136, 340), (2, 440, 480)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{4.a}{Montrer que les droites (AB) et (DC) sont parallèles.}
\begin{reponse}
D'après le codage de la figure, les droites $(AB)$ et $(DC)$ sont toutes les deux perpendiculaires à la droite $(AD)$.
Or, si deux droites sont perpendiculaires à une même droite, alors elles sont parallèles : $(AB) \parallel (DC)$.
\end{reponse}
\q{4.b}{Montrer que CD = 1 500 m.}
\begin{reponse}
Les points $B$, $E$, $D$ et $A$, $E$, $C$ sont alignés, et $(AB) \parallel (DC)$. D'après le théorème de Thalès :
\[ \frac{EB}{ED} = \frac{EA}{EC} = \frac{AB}{DC} \qquad\text{donc}\qquad \frac{250}{750} = \frac{500}{DC} \qquad\text{et}\qquad DC = \frac{500 \times 750}{250} = 1\,500 \text{ m}. \]
\end{reponse}
'''),
dict(id='2025-polj-2d', s='polj', ex=2, titre='Exercice 2 -- Le jardin botanique, question 5', theme='Vitesse, durée',
     consigne='Traite la question 5 (AD ≈ 866 m et CD = 1 500 m).', regions=[(2, 136, 340), (2, 480, 540)], s3=14, n3=[], s4=15, n4=[35],
     corr=r'''
\q{5}{Le piéton fait-il le tour du jardin en moins d'une heure ?}
\begin{reponse}
Longueur du tour : $AB + BC + CD + DA \approx 500 + 1\,323 + 1\,500 + 866 = 4\,189$ m.\\
Durée : $t = \dfrac{d}{v} \approx \dfrac{4\,189}{1{,}1} \approx 3\,808$ s.\\
Or 1 h $= 3\,600$ s et $3\,808 > 3\,600$ : le piéton met \textbf{plus d'une heure} (environ 1 h 3 min).
\end{reponse}
'''),
dict(id='2025-polj-3q1', s='polj', ex=3, titre='Exercice 3 -- QCM, question 1', theme='Carré d’un nombre relatif',
     regions=[QCM, (3, 235, 250)], s3=25, n3=[], s4=1, n4=[2],
     corr=r'''
\q{1}{$(-3)^2$ est égal à\ldots}
\begin{reponse}
$(-3)^2 = (-3) \times (-3) = 9$ (produit de deux nombres négatifs : il est positif). \textbf{Réponse D.}
\end{reponse}
'''),
dict(id='2025-polj-3q2', s='polj', ex=3, titre='Exercice 3 -- QCM, question 2', theme='Décomposition en facteurs premiers',
     regions=[QCM, (3, 250, 289)], s3=24, n3=[], s4=6, n4=[14],
     corr=r'''
\q{2}{Décomposition en produit de facteurs premiers de 360.}
\begin{reponse}
$360 = 2 \times 180 = 2 \times 2 \times 90 = 2 \times 2 \times 2 \times 45 = 2^3 \times 3^2 \times 5$. \textbf{Réponse D.}\\
(9 et 8 ne sont pas premiers, et $2^3 \times 3^2 \times 7 = 504$.)
\end{reponse}
'''),
dict(id='2025-polj-3q3', s='polj', ex=3, titre='Exercice 3 -- QCM, questions 3 et 4', theme='Aire, expression littérale',
     regions=[QCM, (3, 289, 415)], s3=1, n3=[], s4=8, n4=[20],
     corr=r'''
\q{3}{Longueur d'un rectangle d'aire 135 cm² et de largeur 3 cm.}
\begin{reponse}
$\text{longueur} = 135 \div 3 = 45$ cm. \textbf{Réponse B.}
\end{reponse}
\q{4}{Expression de la longueur du segment [BG].}
\begin{reponse}
$BG = BD + DE + EG = x + x + 3 = 2x + 3$ (les segments $[BD]$ et $[DE]$ ont la même longueur $x$). \textbf{Réponse D.}
\end{reponse}
'''),
dict(id='2025-polj-3q5', s='polj', ex=3, titre='Exercice 3 -- QCM, question 5', theme='Translation',
     regions=[QCM, (3, 415, 590)], s3=11, n3=[], s4=7, n4=[17],
     corr=r'''
\q{5}{Image du rectangle GFHI par la translation qui transforme D en M.}
\begin{reponse}
Cette translation fait « glisser » chaque point du même déplacement que de $D$ vers $M$ : elle transforme $G$ en $K$, $F$ en $B$, $H$ en $O$ et $I$ en $L$.
L'image est le rectangle $KBOL$. \textbf{Réponse C.}
\end{reponse}
'''),
dict(id='2025-polj-4a', s='polj', ex=4, titre='Exercice 4 -- Programme de calcul, questions 1 et 2', theme='Programme de calcul, double distributivité',
     consigne='Traite les questions 1 et 2.', regions=[(4, 136, 509)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{1}{Avec 5 comme nombre de départ.}
\begin{reponse}
$5 + 4 = 9$ et $5 - 2 = 3$ ; $9 \times 3 = 27$ ; $27 - 5^2 = 27 - 25 = 2$. Le résultat est bien 2.
\end{reponse}
\q{2.a}{Expression du résultat en fonction de $x$.}
\begin{reponse}
$(x + 4) \times (x - 2) - x^2$ : \textbf{expression C} (les parenthèses sont indispensables).
\end{reponse}
\q{2.b}{Montrer que le résultat s'écrit $2x - 8$.}
\begin{reponse}
\[ (x+4)(x-2) - x^2 = x^2 - 2x + 4x - 8 - x^2 = 2x - 8. \]
\end{reponse}
'''),
dict(id='2025-polj-4b', s='polj', ex=4, titre='Exercice 4 -- La fonction f, question 3', theme='Fonction affine : représentation, image',
     consigne='Traite la question 3.', regions=[(4, 509, 792)], s3=17, n3=[26, 28], s4=None, n4=None,
     corr=r'''
\q{3.a}{Pourquoi les représentations n\textsuperscript{o}~1 et n\textsuperscript{o}~2 ne conviennent-elles pas ?}
\begin{reponse}
$f(x) = 2x - 8$ est une fonction affine : sa représentation graphique est une droite. La représentation n\textsuperscript{o}~1 n'est pas une droite.\\
Le coefficient directeur de $f$ est $2$, positif : la droite « monte ». La représentation n\textsuperscript{o}~2 est une droite qui « descend », elle ne convient pas.
\end{reponse}
\q{3.b}{Image de 4 par la fonction $f$.}
\begin{reponse}
$f(4) = 2 \times 4 - 8 = 8 - 8 = 0$ : l'image de 4 est \textbf{0}.
\end{reponse}
'''),
dict(id='2025-polj-4c', s='polj', ex=4, titre='Exercice 4 -- Programme de calcul, question 4', theme='Équation',
     consigne='Traite la question 4 (le résultat du programme peut s’écrire 2x − 8).', regions=[(4, 136, 367), (5, 128, 186)], s3=7, n3=[], s4=16, n4=[38],
     corr=r'''
\q{4}{Quel nombre de départ choisir pour obtenir 100 ?}
\begin{reponse}
Je résous $2x - 8 = 100$ : \quad $2x = 108$ \quad donc \quad $x = 54$.\\
Il faut choisir \textbf{54}. (Vérification : $58 \times 52 - 54^2 = 3\,016 - 2\,916 = 100$.)
\end{reponse}
'''),
dict(id='2025-polj-4img', s='polj', ex=4, extra=True, titre='Exercice 4 -- La fonction f, image de 4', theme='Fonction : calculer une image',
     consigne="Traite seulement la question 3.b.", regions=[(4, 509, 529), (4, 772, 792)], s3=3, n3=[5], s4=None, n4=None,
     corr=r'''
\q{3.b}{Image de 4 par la fonction $f$.}
\begin{reponse}
Je remplace $x$ par 4 dans $f(x) = 2x - 8$ :\\
$f(4) = 2 \times 4 - 8 = 8 - 8 = 0$. L'image de 4 par la fonction $f$ est \textbf{0}.
\end{reponse}
'''),
dict(id='2025-polj-5a', s='polj', ex=5, titre='Exercice 5 -- Le dé à 12 faces, partie A', theme='Probabilités',
     consigne='Traite la partie A.', regions=[(5, 185, 362)], s3=22, n3=[], s4=20, n4=[13, 47],
     corr=r'''
\q{1}{Pourquoi la probabilité d'obtenir 4 est-elle $\frac{1}{12}$ ?}
\begin{reponse}
Le dé est équilibré : les 12 faces ont la même probabilité d'apparaître, et une seule porte le nombre 4. Donc $p = \dfrac{1}{12}$.
\end{reponse}
\q{2}{Probabilité d'obtenir un nombre pair.}
\begin{reponse}
Les nombres pairs de 1 à 12 sont 2, 4, 6, 8, 10, 12 : $p = \dfrac{6}{12} = \dfrac12$.
\end{reponse}
\q{3}{La probabilité d'obtenir un multiple de 3 est-elle supérieure à 0,3 ?}
\begin{reponse}
Les multiples de 3 sont 3, 6, 9, 12 : $p = \dfrac{4}{12} = \dfrac13 \approx 0{,}333$. Comme $0{,}333 > 0{,}3$, Tom a raison.
\end{reponse}
'''),
dict(id='2025-polj-5b', s='polj', ex=5, titre='Exercice 5 -- Le dé à 12 faces, partie B (Scratch)', theme='Algorithmique (Scratch)',
     consigne='Traite la partie B.', regions=[(5, 185, 207), (5, 362, 792)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Compléter les lignes 2, 3 et 4 du bloc « Lancer ».}
\begin{reponse}
\texttt{2\quad mettre Dé 1 à nombre aléatoire entre 1 et \fbox{12}}\\
\texttt{3\quad mettre Dé 2 à nombre aléatoire entre \fbox{1} et 12}\\
\texttt{4\quad mettre Résultat à \fbox{Dé 1} + \fbox{Dé 2}}
\end{reponse}
\q{2}{Dé n\textsuperscript{o}~1 : 8 et dé n\textsuperscript{o}~2 : 3. Qu'affiche le programme ?}
\begin{reponse}
Résultat $= 8 + 3 = 11$. Comme $11 > 6$, la condition est vraie : le programme affiche \textbf{« Gagné ! »} pendant 2 secondes.
\end{reponse}
'''),
]
