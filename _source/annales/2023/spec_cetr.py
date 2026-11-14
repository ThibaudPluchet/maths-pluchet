# DNB Centres étrangers (groupe I), 14 juin 2023
SOURCE = ('dnb_centres_etrangers_juin_2023.pdf', 'Centres étrangers, 14 juin 2023')
QB = [(1, 135, 222), (2, 432, 462)]
E2 = [(2, 653, 726), (3, 128, 325)]
PARTS = [
dict(id='2023-cetr-1a', s='cetr', ex=1, titre='Exercice 1 -- QCM, partie A (Scratch)', theme='Algorithmique (Scratch)',
     consigne='Traite la partie A.', regions=[(1, 135, 645), (2, 128, 418)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Valeur à compléter dans le bloc « triangle équilatéral ».}
\begin{reponse}
Les angles d'un triangle équilatéral mesurent $60^\circ$ : le lutin tourne de l'angle extérieur, $180^\circ - 60^\circ = 120^\circ$ : \textbf{réponse C}.
\end{reponse}
\q{2}{Figure obtenue avec le script principal.}
\begin{reponse}
Le premier triangle est tracé vers la droite. Le lutin tourne ensuite de $60^\circ$ vers la gauche : le second triangle part dans la direction du côté gauche du premier, avec lequel il partage ce côté. On obtient un triangle et un triangle « à l'envers » accolés : \textbf{réponse C}.
\end{reponse}
\q{3}{Avec « répéter 6 fois ».}
\begin{reponse}
Six triangles équilatéraux tournés de $60^\circ$ autour du point de départ ($6 \times 60^\circ = 360^\circ$) forment \textbf{un hexagone} : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2023-cetr-1b1', s='cetr', ex=1, titre='Exercice 1 -- QCM, partie B, question 1', theme='Calculs avec des fractions',
     regions=QB + [(2, 462, 491)], s3=5, n3=[], s4=18, n4=[42, 43],
     corr=r'''
\q{1}{$\left(\frac23 - \frac13 \times \frac75\right) \div \frac43$.}
\begin{reponse}
La multiplication d'abord : $\dfrac13 \times \dfrac75 = \dfrac{7}{15}$, puis $\dfrac23 - \dfrac{7}{15} = \dfrac{10}{15} - \dfrac{7}{15} = \dfrac{3}{15}$.\\
Diviser par $\dfrac43$, c'est multiplier par $\dfrac34$ : on obtient $\dfrac{3}{15} \times \dfrac34$, \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2023-cetr-1b2', s='cetr', ex=1, titre='Exercice 1 -- QCM, partie B, question 2', theme='Écriture scientifique',
     regions=QB + [(2, 491, 518)], s3=25, n3=[], s4=13, n4=[30, 31],
     corr=r'''
\q{2}{Écriture scientifique de $302{,}4 \times 10^{18}$.}
\begin{reponse}
$302{,}4 = 3{,}024 \times 10^2$, donc $302{,}4 \times 10^{18} = \mathbf{3{,}024 \times 10^{20}}$ : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2023-cetr-1b3', s='cetr', ex=1, titre='Exercice 1 -- QCM, partie B, question 3', theme='Médiane',
     regions=QB + [(2, 518, 628)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{3}{Effet de la correction 18 g $\to$ 16 g sur la médiane.}
\begin{reponse}
Dans l'ordre : 8 ; 10 ; 11 ; \textbf{12} ; \textbf{12} ; 13 ; 15 ; 18. Avec 8 valeurs, la médiane est la moyenne des $4^{\text{e}}$ et $5^{\text{e}}$ : 12 g.\\
Remplacer 18 par 16 ne change pas l'ordre ni les deux valeurs du milieu : la médiane reste \textbf{la même} (réponse B).
\end{reponse}
'''),
dict(id='2023-cetr-2a', s='cetr', ex=2, titre='Exercice 2 -- La cabane, partie A (toboggan)', theme='Trigonométrie, théorème de Pythagore',
     consigne='Traite la partie A.', regions=E2 + [(3, 325, 402)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{1}{L'angle $\widehat{DEF}$ mesure-t-il 30° au degré près ?}
\begin{reponse}
Dans le triangle $DEF$ rectangle en $D$, $[DF]$ est le côté opposé à l'angle $\widehat{DEF}$ et $[DE]$ le côté adjacent :
\[ \tan\widehat{DEF} = \frac{DF}{DE} = \frac{1{,}2}{2{,}04} \qquad\text{donc}\qquad \widehat{DEF} \approx 30^\circ. \]
Le toboggan est \textbf{sécurisé}.
\end{reponse}
\q{2}{Montrer que EF $\approx$ 2,37 m.}
\begin{reponse}
D'après le théorème de Pythagore dans le triangle $DEF$ rectangle en $D$ :
\[ EF^2 = DF^2 + DE^2 = 1{,}2^2 + 2{,}04^2 = 1{,}44 + 4{,}1616 = 5{,}6016 \qquad\text{donc}\qquad EF = \sqrt{5{,}6016} \approx 2{,}37 \text{ m}. \]
\end{reponse}
'''),
dict(id='2023-cetr-2b', s='cetr', ex=2, titre='Exercice 2 -- La cabane, partie B (échelle)', theme='Parallélisme, théorème de Thalès',
     consigne='Traite la partie B.', regions=E2 + [(3, 402, 494)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{1}{Démontrer que (AC) et (MN) sont parallèles.}
\begin{reponse}
Le triangle $BMN$ est rectangle en $N$ : $(MN) \perp (BC)$. Le triangle $ABC$ est rectangle en $C$ : $(AC) \perp (BC)$.\\
Deux droites perpendiculaires à une même droite sont parallèles : $(AC) \parallel (MN)$.
\end{reponse}
\q{2}{Longueur MN avec BN = 0,84 m.}
\begin{reponse}
Les points $B$, $N$, $C$ et $B$, $M$, $A$ sont alignés, et $(MN) \parallel (AC)$. D'après le théorème de Thalès :
\[ \frac{BN}{BC} = \frac{MN}{CA} \qquad\text{soit}\qquad \frac{0{,}84}{1{,}2} = \frac{MN}{0{,}5} \qquad\text{donc}\qquad MN = \frac{0{,}84 \times 0{,}5}{1{,}2} = \mathbf{0{,}35} \text{ m}. \]
\end{reponse}
'''),
dict(id='2023-cetr-2c', s='cetr', ex=2, titre='Exercice 2 -- La cabane, partie C (bac à sable)', theme='Volume, ratio, coût',
     consigne='Traite la partie C.', regions=[(2, 653, 681), (3, 494, 768)], s3=14, n3=[22], s4=None, n4=None,
     corr=r'''
\q{1}{Volume du bac à sable en cm³.}
\begin{reponse}
$V = 200 \times 180 \times 20 = \mathbf{720\,000}$ cm³.
\end{reponse}
\q{2}{Volumes de sable (ratio 3 : 2).}
\begin{reponse}
$3 + 2 = 5$ parts : une part vaut $0{,}72 \div 5 = 0{,}144$ m³.\\
Sable à maçonner : $3 \times 0{,}144 = 0{,}432$ m³ ; sable fin : $2 \times 0{,}144 = 0{,}288$ m³.
\end{reponse}
\q{3}{Coût total du sable.}
\begin{reponse}
Sable à maçonner : $0{,}432 \div 0{,}022 \approx 19{,}6$, il faut 20 sacs : $20 \times 2{,}95 = 59$ €.\\
Sable fin : $0{,}288 \div 0{,}016 = 18$ sacs : $18 \times 5{,}95 = 107{,}10$ €.\\
Total : $59 + 107{,}10 = \mathbf{166{,}10}$ €.
\end{reponse}
'''),
dict(id='2023-cetr-3a', s='cetr', ex=3, titre='Exercice 3 -- Les programmes de calcul, questions 1 et 2', theme='Programmes de calcul, tableur',
     consigne='Traite les questions 1 et 2.', regions=[(4, 135, 535)], s3=1, n3=[], s4=8, n4=[2, 19],
     corr=r'''
\q{1}{Avec 6 au départ.}
\begin{reponse}
Amir : $6 - 5 = 1$ ; $2 \times 1 = 2$. \quad Sonia : $6 + 3 = 9$ ; $9 \times 6 = 54$ ; $54 - 16 = 38$.
\end{reponse}
\q{2.a}{Formule saisie en B2.}
\begin{reponse}
\texttt{=(B1-5)*2}.
\end{reponse}
\q{2.b}{Nombre qui donne le même résultat.}
\begin{reponse}
Dans la colonne F, les deux programmes donnent $-6$ : il faut choisir \textbf{2}.
\end{reponse}
'''),
dict(id='2023-cetr-3b', s='cetr', ex=3, titre='Exercice 3 -- Les programmes de calcul, question 3', theme='Expression littérale, équation produit',
     consigne='Traite la question 3.', regions=[(4, 135, 265), (4, 534, 690)], s3=19, n3=[32], s4=None, n4=None,
     corr=r'''
\q{3.a}{Résultat du programme de Sonia.}
\begin{reponse}
$x \longrightarrow x + 3 \longrightarrow (x + 3) \times x = x^2 + 3x \longrightarrow \mathbf{x^2 + 3x - 16}$.
\end{reponse}
\q{3.b}{Résoudre $(x - 2)(x + 3) = 0$.}
\begin{reponse}
$x - 2 = 0$ ou $x + 3 = 0$, soit $x = 2$ ou $x = -3$. Les programmes donnent le même résultat pour \textbf{2 et $-3$}.
\end{reponse}
'''),
dict(id='2023-cetr-4a', s='cetr', ex=4, titre='Exercice 4 -- Le jeu, partie A', theme='Probabilités (une et deux épreuves)',
     consigne='Traite la partie A.', regions=[(4, 688, 790), (5, 128, 272)], s3=22, n3=[39], s4=None, n4=None,
     corr=r'''
\q{1.a}{Probabilité de tirer une boule rouge.}
\begin{reponse}
4 boules rouges sur 7 : $p = \dfrac47$.
\end{reponse}
\q{1.b}{Probabilité d'un numéro pair.}
\begin{reponse}
Noire 2, rouge 2 et rouge 4 : 3 boules sur 7, $p = \dfrac37$.
\end{reponse}
\q{2}{Probabilité de gagner.}
\begin{reponse}
Avec remise, il y a $7 \times 7 = 49$ tirages possibles, équiprobables. Tirages gagnants : la rouge 1 puis une des 3 noires, ou une des 3 noires puis la rouge 1, soit $3 + 3 = 6$ tirages.\\
$p = \dfrac{6}{49}$.
\end{reponse}
'''),
dict(id='2023-cetr-4b', s='cetr', ex=4, titre='Exercice 4 -- Les lots, partie B', theme='Diviseurs, décomposition, répartition',
     consigne='Traite la partie B.', regions=[(4, 688, 768), (5, 272, 462)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{1}{Peut-on faire 3 lots ?}
\begin{reponse}
$195 = 3 \times 65$ et $234 = 3 \times 78$ : \textbf{oui}, 3 lots de 65 figurines et 78 autocollants.
\end{reponse}
\q{2}{Décomposer 195.}
\begin{reponse}
$195 = 3 \times 65 = \mathbf{3 \times 5 \times 13}$.
\end{reponse}
\q{3.a}{Nombre maximal de lots.}
\begin{reponse}
Facteurs communs à $3 \times 5 \times 13$ et $2 \times 3^2 \times 13$ : $3 \times 13 = \mathbf{39}$ lots.
\end{reponse}
\q{3.b}{Composition d'un lot.}
\begin{reponse}
$195 \div 39 = 5$ figurines et $234 \div 39 = 6$ autocollants.
\end{reponse}
'''),
dict(id='2023-cetr-5', s='cetr', ex=5, titre='Exercice 5 -- La location de bateaux', theme='Proportionnalité, fonctions linéaires et affines',
     consigne='Le graphique est en annexe.', regions=[(5, 462, 790), (6, 128, 235), (7, 190, 530)], s3=17, n3=[26, 28], s4=None, n4=None,
     corr=r'''
\q{1.a}{Prix pour 2 heures (société A).}
\begin{reponse}
On lit \textbf{60 €}.
\end{reponse}
\q{1.b}{Nombre d'heures avec 100 €.}
\begin{reponse}
3 h coûtent 90 € et 4 h coûtent 120 € : \textbf{3 heures}.
\end{reponse}
\q{1.c}{Pourquoi le prix est-il proportionnel à la durée ?}
\begin{reponse}
La représentation graphique est une droite qui passe par l'origine du repère.
\end{reponse}
\q{1.d}{Prix pour 10 heures.}
\begin{reponse}
Une heure coûte $60 \div 2 = 30$ € : $10 \times 30 = \mathbf{300}$ €.
\end{reponse}
\q{2.a}{Prix pour 2 heures (société B).}
\begin{reponse}
$60 + 2 \times 15 = 60 + 30 = 90$ €.
\end{reponse}
\q{2.b}{Tracer la représentation de $f(x) = 15x + 60$.}
\begin{reponse}
C'est une droite : elle passe par $(0\,;\,60)$ et $(4\,;\,120)$ (car $f(4) = 120$).
\end{reponse}
\q{2.c}{Le prix B est-il proportionnel à la durée ?}
\begin{reponse}
\textbf{Non} : la droite ne passe pas par l'origine ($f(0) = 60$, les frais de dossier).
\end{reponse}
\q{3.a}{Société la moins chère pour 3 heures.}
\begin{reponse}
A : $3 \times 30 = 90$ € ; B : $60 + 3 \times 15 = 105$ €. La société \textbf{A}, pour 90 €.
\end{reponse}
\q{3.b}{Durée pour laquelle les prix sont égaux.}
\begin{reponse}
$30x = 15x + 60 \iff 15x = 60 \iff x = 4$ : pour \textbf{4 heures} (120 € chez les deux).
\end{reponse}
'''),
]
