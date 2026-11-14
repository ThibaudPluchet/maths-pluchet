# DNB Asie, 18 juin 2024
SOURCE = ('dnb_asie_juin_2024.pdf', 'Asie, 18 juin 2024')
QCM = (1, 168, 238)
E2 = (1, 627, 665)
PARTS = [
dict(id='2024-asie-1q1', s='asie', ex=1, titre='Exercice 1 -- QCM, question 1', theme='Nombres premiers',
     regions=[QCM, (1, 238, 308)], s3=24, n3=[], s4=6, n4=[14],
     corr=r'''
\q{1}{Lequel de ces nombres est premier ?}
\begin{reponse}
1 n'est pas premier (il n'a qu'un diviseur), $21 = 3 \times 7$ et $54 = 2 \times 27$ ne sont pas premiers.\\
37 n'a que deux diviseurs, 1 et 37 : \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2024-asie-1q2', s='asie', ex=1, titre='Exercice 1 -- QCM, question 2', theme='Patron d’un cube, aire',
     regions=[QCM, (1, 308, 379)], s3=21, n3=[], s4=2, n4=[5],
     corr=r'''
\q{2}{Aire totale du patron d'un cube d'arête 5 cm.}
\begin{reponse}
Le patron est formé de 6 carrés de côté 5 cm : $6 \times 5 \times 5 = 150$ cm² : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2024-asie-1q3', s='asie', ex=1, titre='Exercice 1 -- QCM, question 3', theme='Factorisation (identité remarquable)',
     regions=[QCM, (1, 379, 449)], s3=12, n3=[19], s4=None, n4=None,
     corr=r'''
\q{3}{Forme factorisée de $4x^2 - 9$.}
\begin{reponse}
$4x^2 - 9 = (2x)^2 - 3^2 = (2x - 3)(2x + 3)$ (troisième identité remarquable) : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2024-asie-1q4', s='asie', ex=1, titre='Exercice 1 -- QCM, question 4', theme='Ratio',
     regions=[QCM, (1, 449, 533)], s3=14, n3=[22], s4=None, n4=None,
     corr=r'''
\q{4}{Largeur d'un écran 16 : 9 de longueur 110 cm.}
\begin{reponse}
Longueur et largeur sont dans le ratio $16 : 9$ : $\ell = \dfrac{110 \times 9}{16} = 61{,}875 \approx 62$ cm : \textbf{réponse A}.
\end{reponse}
'''),
dict(id='2024-asie-1q5', s='asie', ex=1, titre='Exercice 1 -- QCM, question 5', theme='Médiane',
     regions=[QCM, (1, 533, 620)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{5}{Médiane de la série 4,1 ; 3,67 ; 4,23 ; 4,5 ; 3,4.}
\begin{reponse}
Dans l'ordre croissant : 3,4 ; 3,67 ; \textbf{4,1} ; 4,23 ; 4,5. Il y a 5 valeurs : la médiane est la $3^{\text{e}}$, soit 4,1 : \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2024-asie-2a', s='asie', ex=2, titre='Exercice 2 -- Vrai ou faux, affirmation 1', theme='Vues d’un assemblage de cubes',
     regions=[E2, (1, 665, 790), (2, 128, 200)], s3=21, n3=[], s4=2, n4=[5],
     corr=r'''
\q{1}{La vue de droite est-elle le dessin proposé ?}
\begin{reponse}
L'assemblage compte 4 cubes : trois cubes posés sur la table et un quatrième posé au-dessus de l'un d'eux, à l'avant.\\
Vu de droite, on voit deux carrés côte à côte en bas et, au-dessus de l'un d'eux, le carré du cube posé en hauteur. Le dessin proposé ne montre que les deux carrés du bas : l'affirmation 1 est \textbf{fausse}.
\end{reponse}
'''),
dict(id='2024-asie-2b', s='asie', ex=2, titre='Exercice 2 -- Vrai ou faux, affirmation 2', theme='Réciproque du théorème de Thalès',
     regions=[E2, (2, 200, 428)], s3=20, n3=[], s4=19, n4=[45],
     corr=r'''
\q{2}{Les droites (NU) et (OD) sont-elles parallèles ?}
\begin{reponse}
D'après le codage, $N$ est le milieu de $[SO]$ : $SN = ON = 6$ cm et $SO = 12$ cm. Les points $S$, $U$, $D$ sont alignés : $SD = 5 + 6 = 11$ cm.
\[ \frac{SN}{SO} = \frac{6}{12} = \frac12 = 0{,}5 \qquad\text{et}\qquad \frac{SU}{SD} = \frac{5}{11} \approx 0{,}45. \]
Les rapports ne sont pas égaux : d'après la contraposée du théorème de Thalès, $(NU)$ et $(OD)$ ne sont pas parallèles.\\
L'affirmation 2 est \textbf{fausse}.
\end{reponse}
'''),
dict(id='2024-asie-2c', s='asie', ex=2, titre='Exercice 2 -- Vrai ou faux, affirmation 3', theme='Probabilités',
     regions=[E2, (2, 428, 530)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{3}{Boule bleue plus probable qu'un nombre pair ?}
\begin{reponse}
Boule bleue : $p = \dfrac{6}{4 + 6} = \dfrac{6}{10} = 0{,}6$. \quad Nombre pair (2, 4 ou 6) : $p = \dfrac{3}{6} = 0{,}5$.\\
$0{,}6 > 0{,}5$ : l'affirmation 3 est \textbf{vraie}.
\end{reponse}
'''),
dict(id='2024-asie-3a', s='asie', ex=3, titre='Exercice 3 -- Les trois pièces, questions 1 et 2', theme='Théorème de Pythagore, aire d’un triangle',
     consigne='Traite les questions 1 et 2.', regions=[(3, 140, 619)], s3=2, n3=[], s4=4, n4=[9, 10],
     corr=r'''
\q{1}{Montrer que BC $\approx$ 17,3 cm.}
\begin{reponse}
$(CG) \perp (AB)$ : le triangle $BCG$ est rectangle en $C$, d'hypoténuse $[BG]$. D'après le théorème de Pythagore :
\[ BC^2 = BG^2 - CG^2 = 20^2 - 10^2 = 400 - 100 = 300 \qquad\text{donc}\qquad BC = \sqrt{300} \approx 17{,}3 \text{ cm}. \]
\end{reponse}
\q{2}{Aire du triangle BAG.}
\begin{reponse}
$AC = CB$, donc $AB = 2 \times \sqrt{300} \approx 34{,}64$ cm. La hauteur issue de $G$ est $[GC]$, de longueur 10 cm :
\[ \mathcal{A} = \frac{AB \times CG}{2} = \frac{2\sqrt{300} \times 10}{2} = 10\sqrt{300} \approx 173 \text{ cm}^2. \]
\end{reponse}
'''),
dict(id='2024-asie-3b', s='asie', ex=3, titre='Exercice 3 -- Les trois pièces, questions 3 à 5', theme='Trigonométrie, angles, aire d’un disque',
     consigne='Traite les questions 3 à 5.', regions=[(3, 140, 588), (3, 619, 728)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{3.a}{Montrer que l'angle $\widehat{CGB}$ mesure 60°.}
\begin{reponse}
Dans le triangle $BCG$ rectangle en $C$, $[CG]$ est le côté adjacent à l'angle $\widehat{CGB}$ et $[BG]$ l'hypoténuse :
\[ \cos\widehat{CGB} = \frac{CG}{BG} = \frac{10}{20} = 0{,}5 \qquad\text{donc}\qquad \widehat{CGB} = 60^\circ. \]
\end{reponse}
\q{3.b}{Mesure de l'angle $\widehat{AGB}$.}
\begin{reponse}
$GA = GB$ (rayons de l'arc de centre $G$) : le triangle $AGB$ est isocèle en $G$, et la hauteur $(GC)$ est aussi sa bissectrice. Donc $\widehat{AGC} = \widehat{CGB} = 60^\circ$ et $\widehat{AGB} = 2 \times 60^\circ = \mathbf{120^\circ}$.
\end{reponse}
\q{4}{Pourquoi les trois pièces forment-elles un disque ?}
\begin{reponse}
Chaque pièce est une portion de disque de rayon 20 cm et d'angle $120^\circ$. Placées autour du même centre : $3 \times 120^\circ = 360^\circ$, un tour complet. Elles forment un disque complet.
\end{reponse}
\q{5}{Aire d'une pièce.}
\begin{reponse}
Chaque pièce est le tiers d'un disque de rayon 20 cm :
\[ \mathcal{A} = \frac{\pi \times 20^2}{3} = \frac{400\pi}{3} \approx \mathbf{419} \text{ cm}^2. \]
\end{reponse}
'''),
dict(id='2024-asie-4a', s='asie', ex=4, titre='Exercice 4 -- Les vacances, partie A', theme='Proportionnalité, consommation, budget',
     consigne='Traite la partie A.', regions=[(3, 726, 790), (4, 128, 620)], s3=14, n3=[], s4=5, n4=[11],
     corr=r'''
\q{1}{Distance de l'aller-retour Strasbourg -- Marseille.}
\begin{reponse}
Le tableau donne 803 km entre Strasbourg et Marseille : $2 \times 803 = \mathbf{1\,606}$ km.
\end{reponse}
\q{2}{Coût de la location avec la formule B.}
\begin{reponse}
$300 + 0{,}25 \times 1\,606 = 300 + 401{,}50 = 701{,}50$ €.
\end{reponse}
\q{3}{Formule la plus avantageuse.}
\begin{reponse}
Formule A : $0{,}50 \times 1\,606 = 803$ €. Formule B : 701,50 €. Formule C : 900 €.\\
La formule \textbf{B} est la plus avantageuse.
\end{reponse}
\q{4}{Le budget de 1 000 € est-il suffisant ?}
\begin{reponse}
Gazole : la voiture consomme 5,6 L pour 100 km, donc $\dfrac{1\,606 \times 5{,}6}{100} = 89{,}936$ L, qui coûtent $89{,}936 \times 1{,}87 \approx 168{,}18$ €.\\
Total : $701{,}50 + 168{,}18 + 115{,}80 = 985{,}48$ €. $985{,}48 < 1\,000$ : le budget est \textbf{suffisant}.
\end{reponse}
'''),
dict(id='2024-asie-4b', s='asie', ex=4, titre='Exercice 4 -- Les vacances, partie B', theme='Fonctions linéaires et affines, équation',
     consigne='Traite la partie B.', regions=[(4, 618, 782), (5, 128, 606)], s3=17, n3=[13, 26, 28], s4=None, n4=None,
     corr=r'''
\q{5}{Prix payé en fonction de $x$.}
\begin{reponse}
Formule A : $0{,}5x$. \quad Formule B : $0{,}25x + 300$. \quad Formule C : $900$.
\end{reponse}
\q{6}{Associer chaque courbe à une formule.}
\begin{reponse}
Courbe 1 (droite horizontale) : formule \textbf{C}. Courbe 2 (droite qui coupe l'axe des ordonnées en 300) : formule \textbf{B}. Courbe 3 (droite qui passe par l'origine) : formule \textbf{A}.
\end{reponse}
\q{7}{Résoudre $0{,}25x + 300 = 0{,}5x$ et interpréter.}
\begin{reponse}
\[ 0{,}25x + 300 = 0{,}5x \iff 300 = 0{,}5x - 0{,}25x \iff 300 = 0{,}25x \iff x = \frac{300}{0{,}25} = 1\,200. \]
Pour \textbf{1 200 km}, les formules A et B coûtent le même prix (600 €).
\end{reponse}
\q{8.a}{Formule la moins chère pour 2 500 km.}
\begin{reponse}
La formule \textbf{C} (la courbe 1 est la plus basse).
\end{reponse}
\q{8.b}{Une distance pour laquelle la formule A est la plus intéressante.}
\begin{reponse}
Par exemple \textbf{500 km} (toute distance inférieure à 1 200 km convient).
\end{reponse}
\q{8.c}{Formule la moins chère selon la distance (moins de 2 600 km).}
\begin{reponse}
Les courbes 2 et 1 se coupent pour 2\,400 km ($0{,}25 \times 2\,400 + 300 = 900$).
\begin{itemize}
\item de 0 à 1\,200 km : formule \textbf{A} ;
\item de 1\,200 à 2\,400 km : formule \textbf{B} ;
\item de 2\,400 à 2\,600 km : formule \textbf{C}.
\end{itemize}
\end{reponse}
'''),
dict(id='2024-asie-5', s='asie', ex=5, titre='Exercice 5 -- Le motif (Scratch)', theme='Algorithmique (Scratch)',
     regions=[(6, 140, 750), (7, 128, 560)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Coordonnées du lutin après le clic sur le drapeau.}
\begin{reponse}
$(-100\,;\,0)$.
\end{reponse}
\q{2}{Figure obtenue (1 cm pour 20 pas).}
\begin{reponse}
80 pas représentent 4 cm. Le motif trace un triangle équilatéral de côté 4 cm au-dessus du segment de départ (tours à gauche), puis un deuxième en dessous (tours à droite) : on obtient un \textbf{losange} de côté 4 cm, d'angles $60^\circ$ et $120^\circ$.
\begin{center}
\begin{tikzpicture}[scale=0.6]
\draw[thick] (0,0) -- (4,0) -- (2,3.464) -- cycle;
\draw[thick] (0,0) -- (4,0) -- (2,-3.464) -- cycle;
\fill (0,0) circle (2pt) node[left] {départ};
\end{tikzpicture}
\end{center}
\end{reponse}
\q{3}{Associer chaque script à sa figure.}
\begin{reponse}
Script 1 (avancer de 100 pas entre deux motifs) : trois losanges séparés, \textbf{figure B}.\\
Script 2 (côté multiplié par 1,2) : trois losanges de plus en plus grands, avec le même point de départ, \textbf{figure A}.\\
Script 3 (tourner de $120^\circ$) : trois losanges qui tournent autour du point de départ, \textbf{figure C}.
\end{reponse}
\q{4.a}{Nombre d'exécutions du bloc « motif » (script 2).}
\begin{reponse}
\textbf{3 fois} (il est dans une boucle « répéter 3 fois »).
\end{reponse}
\q{4.b}{Valeur de « côté » à la fin du script 2.}
\begin{reponse}
Le côté est multiplié 3 fois par 1,2 : $80 \times 1{,}2^3 = 80 \times 1{,}728 = \mathbf{138{,}24}$.
\end{reponse}
'''),
]
