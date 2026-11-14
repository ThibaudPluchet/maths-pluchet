# DNB Centres étrangers, juin 2022
SOURCE = ('dnb_centres_etrangers_juin_2022.pdf', 'Centres étrangers, juin 2022')
PARTS = [
dict(id='2022-cetr-1a', s='cetr', ex=1, titre='Exercice 1 -- Fonction et calcul, partie A', theme='Fonction affine : image, représentation, tableur',
     consigne='Traite la partie A.', regions=[(1, 246, 604)], s3=17, n3=[27, 28], s4=None, n4=None,
     corr=r'''
\q{1}{Représentation graphique de $f(x) = 2x + 3$.}
\begin{reponse}
La droite passe par le point $(0\,;3)$ car $f(0) = 3$ et monte (coefficient 2 positif) : \textbf{réponse A}.
\end{reponse}
\q{2}{Image de $-2$.}
\begin{reponse}
$f(-2) = 2 \times (-2) + 3 = -4 + 3 = \mathbf{-1}$, \textbf{réponse B}.
\end{reponse}
\q{3}{Formule à saisir en B2.}
\begin{reponse}
B2 doit contenir l'image du nombre écrit en B1 : \texttt{=2*B1+3}, \textbf{réponse B}.
\end{reponse}
'''),
dict(id='2022-cetr-1b', s='cetr', ex=1, titre='Exercice 1 -- Fonction et calcul, partie B, question 1', theme='Double distributivité',
     consigne='Traite seulement la question 1 de la partie B.', regions=[(1, 246, 286), (1, 604, 657)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{1}{Montrer que $(2x-1)(3x+4) - 2x = 6x^2 + 3x - 4$.}
\begin{reponse}
\[ (2x - 1)(3x + 4) - 2x = 6x^2 + 8x - 3x - 4 - 2x = 6x^2 + 3x - 4. \]
\end{reponse}
'''),
dict(id='2022-cetr-1c', s='cetr', ex=1, titre='Exercice 1 -- Fonction et calcul, partie B, question 2', theme='Réciproque du théorème de Pythagore',
     consigne='Traite seulement la question 2 de la partie B.', regions=[(1, 246, 286), (1, 604, 622), (1, 655, 700)], s3=13, n3=[], s4=14, n4=[32],
     corr=r'''
\q{2}{Le triangle CDE est-il rectangle ?}
\begin{reponse}
Le plus grand côté est $[DE]$. $DE^2 = 5{,}5^2 = 30{,}25$ et $CD^2 + CE^2 = 3{,}6^2 + 4{,}2^2 = 12{,}96 + 17{,}64 = 30{,}6$.
$30{,}25 \neq 30{,}6$ : d'après le théorème de Pythagore, le triangle $CDE$ \textbf{n'est pas rectangle}.
\end{reponse}
'''),
dict(id='2022-cetr-2a', s='cetr', ex=2, titre='Exercice 2 -- Paris–Nice, question 1', theme='Moyenne, médiane, étendue',
     consigne='Traite seulement la question 1.', regions=[(1, 702, 760), (2, 120, 336)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{1.a}{Distance moyenne par étape.}
\begin{reponse}
$\dfrac{166 + 188 + 187{,}5 + 200 + 202{,}5 + 119{,}5 + 93}{7} = \dfrac{1\,156{,}5}{7} \approx \mathbf{165{,}2}$ km.
\end{reponse}
\q{1.b}{Médiane.}
\begin{reponse}
Rangées : 93 ; 119,5 ; 166 ; \textbf{187,5} ; 188 ; 200 ; 202,5. Il y a 7 valeurs : la médiane est la 4\ieme{}, \textbf{187,5 km}.
\end{reponse}
\q{1.c}{Étendue.}
\begin{reponse}
$202{,}5 - 93 = \mathbf{109{,}5}$ km.
\end{reponse}
'''),
dict(id='2022-cetr-2b', s='cetr', ex=2, titre='Exercice 2 -- Paris–Nice, questions 2 à 4', theme='Pourcentage, durées, vitesse',
     consigne='Traite les questions 2 à 4.', regions=[(1, 702, 760), (2, 120, 246), (2, 334, 468)], s3=14, n3=[], s4=15, n4=[34, 35, 36],
     corr=r'''
\q{2}{Le journaliste a-t-il raison ?}
\begin{reponse}
4 étapes sur 7 sont accidentées : $\dfrac{4}{7} \approx 0{,}571$, soit environ 57 \%. \textbf{Il a raison}.
\end{reponse}
\q{3}{Retard du dernier.}
\begin{reponse}
De 28 h 50 min à 29 h : 10 min ; de 29 h à 30 h 12 min : 1 h 12 min. Retard : \textbf{1 h 22 min}.
\end{reponse}
\q{4}{Vitesse moyenne de Sam Bennett.}
\begin{reponse}
3 h 51 min $= 231$ min. Il parcourt 166 km en 231 min : $v = \dfrac{166}{231} \times 60 \approx \mathbf{43}$ km/h.
\end{reponse}
'''),
dict(id='2022-cetr-3a', s='cetr', ex=3, titre='Exercice 3 -- Deux triangles, question 1', theme='Trigonométrie (cosinus)',
     consigne='Traite seulement la question 1.', regions=[(2, 466, 782)], s3=4, n3=[6], s4=None, n4=None,
     corr=r'''
\q{1}{Prouver que AB = 4 cm.}
\begin{reponse}
Le triangle $ABC$ est rectangle en $B$ : $\cos\widehat{BAC} = \dfrac{AB}{AC}$, donc $AB = 8 \times \cos 60^\circ = 8 \times 0{,}5 = \mathbf{4}$ cm.
\end{reponse}
'''),
dict(id='2022-cetr-3b', s='cetr', ex=3, titre='Exercice 3 -- Deux triangles, questions 2 à 4', theme='Réciproque de Thalès, théorème de Pythagore, aire',
     consigne='Traite les questions 2 à 4 (AB = 4 cm).', regions=[(2, 466, 764), (3, 120, 210)], s3=20, n3=[], s4=19, n4=[10, 45],
     corr=r'''
\q{2}{Démontrer que (BC) et (DE) sont parallèles.}
\begin{reponse}
Les points $B$, $A$, $D$ et $C$, $A$, $E$ sont alignés dans le même ordre.
\[ \frac{AC}{AE} = \frac{8}{19{,}2} = \frac{5}{12} \qquad\text{et}\qquad \frac{AB}{AD} = \frac{4}{9{,}6} = \frac{5}{12}. \]
Les rapports sont égaux : d'après la réciproque du théorème de Thalès, $(BC) \parallel (DE)$.
\end{reponse}
\q{3}{Démontrer que (DB) est perpendiculaire à (DE).}
\begin{reponse}
$(DB) \perp (BC)$ et $(BC) \parallel (DE)$. Si deux droites sont parallèles, toute perpendiculaire à l'une est perpendiculaire à l'autre : $(DB) \perp (DE)$.
\end{reponse}
\q{4}{Aire du triangle ADE.}
\begin{reponse}
$ADE$ est rectangle en $D$. D'après le théorème de Pythagore : $DE^2 = AE^2 - AD^2 = 19{,}2^2 - 9{,}6^2 = 276{,}48$, donc $DE \approx 16{,}63$ cm.
$\mathcal{A} = \dfrac{AD \times DE}{2} \approx \dfrac{9{,}6 \times 16{,}63}{2} \approx \mathbf{80}$ cm$^2$.
\end{reponse}
'''),
dict(id='2022-cetr-4a', s='cetr', ex=4, titre='Exercice 4 -- Les motifs, partie A', theme='Algorithmique (Scratch)',
     consigne='Traite la partie A.', regions=[(3, 215, 523)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{A}{Instructions à insérer dans le script.}
\begin{reponse}
Après « avancer de 40 » : \textbf{tourner à gauche de 40 degrés}, \textbf{avancer de 30}, \textbf{tourner à gauche de 140 degrés}.
\end{reponse}
'''),
dict(id='2022-cetr-4b', s='cetr', ex=4, titre='Exercice 4 -- Les motifs, partie B', theme='Algorithmique (Scratch)',
     consigne='Traite la partie B.', regions=[(3, 215, 256), (3, 521, 792), (4, 120, 382)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Lancer le programme de l'élève B.}
\begin{reponse}
On appuie sur la \textbf{barre d'espace}.
\end{reponse}
\q{2.a}{Figure du programme A.}
\begin{reponse}
Le lutin trace 9 motifs côte à côte en avançant vers la droite : \textbf{figure 1}.
\end{reponse}
\q{2.b}{Figure du programme B.}
\begin{reponse}
Le lutin tourne de $40^\circ$ après chaque motif et $9 \times 40^\circ = 360^\circ$ : les motifs forment une rosace, \textbf{figure 4}.
\end{reponse}
'''),
dict(id='2022-cetr-5a', s='cetr', ex=5, titre='Exercice 5 -- Les truffes, question 1', theme='Décomposition, diviseurs communs, répartition',
     consigne='Traite seulement la question 1.', regions=[(4, 382, 586)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{1.a}{Décompositions.}
\begin{reponse}
$125 = 5 \times 5 \times 5 = \mathbf{5^3}$ et $175 = 5 \times 5 \times 7 = \mathbf{5^2 \times 7}$.
\end{reponse}
\q{1.b}{Diviseurs communs.}
\begin{reponse}
Les diviseurs communs sont ceux de $5^2 = 25$ : \textbf{1, 5 et 25}.
\end{reponse}
\q{1.c}{Nombre maximal de boîtes.}
\begin{reponse}
\textbf{25 boîtes}.
\end{reponse}
\q{1.d}{Contenu de chaque boîte.}
\begin{reponse}
$125 \div 25 = 5$ et $175 \div 25 = 7$ : \textbf{5 truffes au café et 7 à la noix de coco}.
\end{reponse}
'''),
dict(id='2022-cetr-5b', s='cetr', ex=5, titre='Exercice 5 -- Les truffes, question 2', theme='Volumes de la boule, de la pyramide et du pavé',
     consigne='Traite seulement la question 2.', regions=[(4, 382, 434), (4, 584, 780), (5, 120, 292)], s3=21, n3=[35, 36], s4=None, n4=None,
     corr=r'''
\q{2}{Quel type de boîte choisir ?}
\begin{reponse}
Une truffe a pour rayon 0,75 cm. Les 12 truffes occupent $12 \times \dfrac{4}{3} \times \pi \times 0{,}75^3 = 6{,}75\pi \approx 21{,}2$ cm$^3$.

Type A : $V = \dfrac{4{,}8 \times 4{,}8 \times 5}{3} = 38{,}4$ cm$^3$. Volume libre : $38{,}4 - 21{,}2 = 17{,}2$ cm$^3$, inférieur à 21,2 cm$^3$ : la boîte convient.

Type B : $V = 5 \times 3{,}5 \times 3{,}5 = 61{,}25$ cm$^3$. Volume libre : $61{,}25 - 21{,}2 \approx 40$ cm$^3$, supérieur à 21,2 cm$^3$ : elle ne convient pas.

Il doit choisir le \textbf{type A}.
\end{reponse}
'''),
]
