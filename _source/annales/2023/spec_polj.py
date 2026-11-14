# DNB Polynésie, 23 juin 2023
SOURCE = ('dnb_polynesie_juin_2023.pdf', 'Polynésie, 23 juin 2023')
QCM = (1, 184, 265)
E4 = (3, 677, 790)
E5 = (4, 743, 790)
PARTS = [
dict(id='2023-polj-1q1', s='polj', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Représentation d’une fonction affine',
     regions=[QCM, (1, 265, 428)], s3=17, n3=[28], s4=None, n4=None,
     corr=r'''
\q{1}{Représentation de $f(x) = -2x + 3$.}
\begin{reponse}
C'est une droite qui descend (coefficient directeur $-2$) et qui coupe l'axe des ordonnées en 3 : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2023-polj-1q2', s='polj', ex=1, titre='Exercice 1 -- QCM, question 2', theme='Lecture graphique d’une image',
     regions=[QCM, (1, 428, 573)], s3=8, n3=[13], s4=None, n4=None,
     corr=r'''
\q{2}{Image de 1.}
\begin{reponse}
Le point de la courbe d'abscisse 1 est le point $C$, d'ordonnée 2 : l'image de 1 est 2, \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2023-polj-1q3', s='polj', ex=1, titre='Exercice 1 -- QCM, question 3', theme='Fonction, tableur',
     regions=[QCM, (1, 573, 754)], s3=3, n3=[5], s4=None, n4=None,
     corr=r'''
\q{3}{Formule saisie en B2.}
\begin{reponse}
La formule doit utiliser la cellule B1 pour pouvoir être étirée : \texttt{= - B1 + 1}, \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2023-polj-1q4', s='polj', ex=1, titre='Exercice 1 -- QCM, question 4', theme='Développer (double distributivité)',
     regions=[QCM, (1, 754, 788), (2, 128, 190)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{4}{Forme développée de $(3x - 7)^2$.}
\begin{reponse}
$(3x - 7)^2 = (3x - 7)(3x - 7) = 9x^2 - 21x - 21x + 49 = \mathbf{9x^2 - 42x + 49}$ : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2023-polj-2a', s='polj', ex=2, titre='Exercice 2 -- Les panneaux solaires, questions 1 et 4', theme='Théorème de Pythagore, pourcentage, longueurs',
     consigne='Traite les questions 1 et 4.', regions=[(2, 190, 790)], s3=2, n3=[], s4=4, n4=[10, 34],
     corr=r'''
\q{1.a}{Vérifier que HS $\approx$ 166,4 cm.}
\begin{reponse}
Le triangle $PHS$ est rectangle en $P$, d'hypoténuse $[HS]$. D'après le théorème de Pythagore :
\[ HS^2 = PH^2 + PS^2 = 90^2 + 140^2 = 8\,100 + 19\,600 = 27\,700 \qquad\text{donc}\qquad HS = \sqrt{27\,700} \approx 166{,}4 \text{ cm}. \]
\end{reponse}
\q{1.b}{HS mesure-t-il au moins 95 \% de la longueur du panneau ?}
\begin{reponse}
1\,700 mm $= 170$ cm. \quad $170 \times 0{,}95 = 161{,}5$ cm. $166{,}4 > 161{,}5$ : le support est \textbf{conforme}.
\end{reponse}
\q{4}{Budget minimum pour les tubes.}
\begin{reponse}
Une équerre : $90 + 140 + 166{,}4 + 50 = 446{,}4$ cm, soit 4,464 m : un tube de 4,5 m par équerre.\\
Une barre latérale de 4 m : un tube par barre (il ne reste que 0,5 m).\\
$3 + 3 = 6$ tubes : $6 \times 37 = \mathbf{222}$ €.
\end{reponse}
'''),
dict(id='2023-polj-2b', s='polj', ex=2, titre='Exercice 2 -- Les panneaux solaires, questions 2 et 3', theme='Trigonométrie, théorème de Thalès',
     consigne='Traite les questions 2 et 3.', regions=[(2, 190, 790)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{2}{L'angle $\widehat{HSP}$ permet-il un fonctionnement optimal ?}
\begin{reponse}
Dans le triangle $PHS$ rectangle en $P$, $[PH]$ est le côté opposé à $\widehat{HSP}$ et $[PS]$ le côté adjacent :
\[ \tan\widehat{HSP} = \frac{PH}{PS} = \frac{90}{140} \qquad\text{donc}\qquad \widehat{HSP} \approx 32{,}7^\circ. \]
$32{,}7^\circ$ est entre $30^\circ$ et $35^\circ$ : \textbf{oui}.
\end{reponse}
\q{3}{Longueur ST.}
\begin{reponse}
$(UT) \perp (PS)$ et $(HP) \perp (PS)$ : $(UT) \parallel (HP)$. Les points $S$, $T$, $P$ et $S$, $U$, $H$ sont alignés. D'après le théorème de Thalès :
\[ \frac{ST}{SP} = \frac{TU}{PH} \qquad\text{soit}\qquad \frac{ST}{140} = \frac{50}{90} \qquad\text{donc}\qquad ST = \frac{140 \times 50}{90} \approx \mathbf{77{,}8} \text{ cm}. \]
\end{reponse}
'''),
dict(id='2023-polj-3a', s='polj', ex=3, titre='Exercice 3 -- Les deux jeux, partie A', theme='Probabilités, nombres premiers',
     consigne='Traite la partie A.', regions=[(3, 146, 552)], s3=22, n3=[], s4=20, n4=[14, 47],
     corr=r'''
\q{1}{Probabilité de gagner au jeu 1.}
\begin{reponse}
2 boules G sur 5 boules : $p = \dfrac25$.
\end{reponse}
\q{2}{Probabilité de gagner au jeu 2.}
\begin{reponse}
Les nombres premiers de 1 à 6 sont 2, 3 et 5 (1 n'est pas premier) : $p = \dfrac36 = \dfrac12$.
\end{reponse}
\q{3.a}{Jeu le moins favorable.}
\begin{reponse}
$\dfrac25 = 0{,}4 < \dfrac12 = 0{,}5$ : le \textbf{jeu 1}.
\end{reponse}
\q{3.b}{Boules à ajouter pour une probabilité de $\frac14$.}
\begin{reponse}
Avec 2 boules G, il faut 8 boules en tout ($\dfrac28 = \dfrac14$) : on ajoute \textbf{3 boules sans la lettre G}, par exemple 3 boules P.
\end{reponse}
'''),
dict(id='2023-polj-3b', s='polj', ex=3, titre='Exercice 3 -- Les deux jeux, partie B', theme='Probabilités (deux épreuves)',
     consigne='Traite la partie B.', regions=[(3, 146, 368), (3, 552, 677)], s3=22, n3=[39], s4=None, n4=None,
     corr=r'''
\q{B}{Probabilité de gagner en combinant les deux jeux.}
\begin{reponse}
Il y a $5 \times 6 = 30$ issues équiprobables (une boule, puis un secteur). Issues gagnantes : 2 boules G $\times$ 3 nombres premiers $= 6$.
\[ p = \frac{6}{30} = \frac15 = 0{,}2. \]
\small (Ou : $\dfrac25 \times \dfrac12 = \dfrac15$.)
\end{reponse}
'''),
dict(id='2023-polj-4a', s='polj', ex=4, titre='Exercice 4 -- Le programme de calcul, questions 1 et 2', theme='Programme de calcul, Scratch',
     consigne='Traite les questions 1 et 2.', regions=[E4, (4, 128, 663)], s3=1, n3=[], s4=8, n4=[2, 18],
     corr=r'''
\q{1.a}{Avec 4 au départ.}
\begin{reponse}
$4^2 = 16$ ; $16 \times 2 = 32$ ; $32 + 4 = 36$ ; $36 - 66 = -30$.
\end{reponse}
\q{1.b}{Avec $-3$ au départ.}
\begin{reponse}
$(-3)^2 = 9$ ; $9 \times 2 = 18$ ; $18 + (-3) = 15$ ; $15 - 66 = \mathbf{-51}$.
\end{reponse}
\q{2.a}{Contenu des emplacements A et B.}
\begin{reponse}
A : \textbf{Nombre choisi} (pour obtenir le carré) ; B : \textbf{2}.
\end{reponse}
\q{2.b}{Que représente 5,5 ?}
\begin{reponse}
Le script teste 0 ; 0,5 ; 1 ; \ldots\ et ne parle que si le résultat vaut 0 : 5,5 est un nombre de départ pour lequel le programme donne \textbf{0}.\\
Vérification : $2 \times 5{,}5^2 + 5{,}5 - 66 = 60{,}5 + 5{,}5 - 66 = 0$.
\end{reponse}
'''),
dict(id='2023-polj-4b', s='polj', ex=4, titre='Exercice 4 -- Le programme de calcul, question 3', theme='Expression littérale, équation produit',
     consigne='Traite la question 3.', regions=[E4, (4, 663, 745)], s3=19, n3=[32], s4=None, n4=None,
     corr=r'''
\q{3.a}{Expression en fonction de $x$.}
\begin{reponse}
$x \longrightarrow x^2 \longrightarrow 2x^2 \longrightarrow 2x^2 + x \longrightarrow \mathbf{2x^2 + x - 66}$.
\end{reponse}
\q{3.b}{Valeurs de $x$ qui donnent 0.}
\begin{reponse}
$(2x - 11)(x + 6) = 0 \iff 2x - 11 = 0$ ou $x + 6 = 0 \iff x = 5{,}5$ ou $x = -6$.\\
Le résultat est nul pour \textbf{5,5 et $-6$} (le script de Lucie ne teste que des nombres positifs).
\end{reponse}
'''),
dict(id='2023-polj-5a', s='polj', ex=5, titre='Exercice 5 -- Le karting, questions 1 à 3', theme='Longueurs, périmètre du cercle, vitesses',
     consigne='Traite les questions 1 à 3.', regions=[E5, (5, 128, 558)], s3=14, n3=[], s4=15, n4=[35, 36],
     corr=r'''
\q{1}{Longueur de la piste.}
\begin{reponse}
Segments (d'après le codage) : $90 + 60 + 90 + 60 + 60 + 120 = 480$ m.\\
Les quatre quarts de cercle de rayon 30 m forment un cercle : $2 \times \pi \times 30 = 60\pi$ m.\\
Les deux demi-cercles de diamètre $60 + 60 = 120$ m (rayon 60 m) forment un cercle : $2 \times \pi \times 60 = 120\pi$ m.\\
Total : $480 + 60\pi + 120\pi = 480 + 180\pi \approx \mathbf{1\,045}$ m.
\end{reponse}
\q{2}{Vitesse moyenne du professionnel.}
\begin{reponse}
$v = \dfrac{1\,045}{60} \approx \mathbf{17{,}42}$ m/s.
\end{reponse}
\q{3}{L'amateur dépasse-t-il 60 km/h ?}
\begin{reponse}
$v = \dfrac{1\,045}{72} \approx 14{,}51$ m/s, soit $14{,}51 \times 3{,}6 \approx 52{,}2$ km/h. $52{,}2 < 60$ : il \textbf{respecte} les règles.
\end{reponse}
'''),
dict(id='2023-polj-5b', s='polj', ex=5, titre='Exercice 5 -- Le karting, question 4', theme='Décomposition, multiples communs',
     consigne='Traite la question 4.', regions=[E5, (5, 558, 660)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{4.a}{Décomposer 60 et 72.}
\begin{reponse}
$60 = 2^2 \times 3 \times 5$ \qquad et \qquad $72 = 2^3 \times 3^2$.
\end{reponse}
\q{4.b}{Quand se retrouvent-ils sur la ligne de départ ?}
\begin{reponse}
Il faut le plus petit multiple commun de 60 et 72 : $2^3 \times 3^2 \times 5 = 360$ s, soit \textbf{6 minutes}.
\end{reponse}
\q{4.c}{Nombre de tours de chacun.}
\begin{reponse}
Professionnel : $360 \div 60 = \mathbf{6}$ tours ; amateur : $360 \div 72 = \mathbf{5}$ tours.
\end{reponse}
'''),
]
