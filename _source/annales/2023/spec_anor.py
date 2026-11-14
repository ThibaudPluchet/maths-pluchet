# DNB Amérique du Nord, 31 mai 2023
SOURCE = ('dnb_ameri_nord_mai_2023.pdf', 'Amérique du Nord, 31 mai 2023')
E1 = (1, 172, 214)
E2 = (1, 772, 790)
PARTS = [
dict(id='2023-anor-1s1', s='anor', ex=1, titre='Exercice 1 -- Situation 1', theme='Décomposition en facteurs premiers',
     regions=[E1, (1, 214, 266)], s3=24, n3=[], s4=6, n4=[14],
     corr=r'''
\q{1}{Décomposer 780.}
\begin{reponse}
$780 = 2 \times 390 = 2 \times 2 \times 195 = 2 \times 2 \times 3 \times 65 = \mathbf{2^2 \times 3 \times 5 \times 13}$.
\end{reponse}
'''),
dict(id='2023-anor-1s2', s='anor', ex=1, titre='Exercice 1 -- Situation 2', theme='Probabilités',
     regions=[E1, (1, 266, 391)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{2.a}{Probabilité d'obtenir le 8 de pique.}
\begin{reponse}
Une seule carte sur 32 : $p = \dfrac{1}{32}$.
\end{reponse}
\q{2.b}{Probabilité d'obtenir un roi ou un cœur.}
\begin{reponse}
4 rois et 8 cœurs, mais le roi de cœur est compté deux fois : $4 + 8 - 1 = 11$ cartes. $p = \dfrac{11}{32}$.
\end{reponse}
'''),
dict(id='2023-anor-1s3', s='anor', ex=1, titre='Exercice 1 -- Situation 3', theme='Double distributivité',
     regions=[E1, (1, 391, 429)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{3}{Développer et réduire $A = (2x + 5)(3x - 4)$.}
\begin{reponse}
$A = 6x^2 - 8x + 15x - 20 = \mathbf{6x^2 + 7x - 20}$.
\end{reponse}
'''),
dict(id='2023-anor-1s4', s='anor', ex=1, titre='Exercice 1 -- Situation 4', theme='Volume d’un prisme, conversion',
     regions=[E1, (1, 429, 626)], s3=21, n3=[], s4=17, n4=[],
     corr=r'''
\q{4.a}{Volume du prisme droit.}
\begin{reponse}
La base est un triangle rectangle de côtés de l'angle droit 60 cm et 80 cm : $\mathcal{A} = \dfrac{60 \times 80}{2} = 2\,400$ cm². La hauteur du prisme est 120 cm.\\
$V = 2\,400 \times 120 = \mathbf{288\,000}$ cm³.
\end{reponse}
\q{4.b}{Conversion en litres.}
\begin{reponse}
$1$ dm³ $= 1\,000$ cm³ : $288\,000$ cm³ $= 288$ dm³ $= \mathbf{288}$ L.
\end{reponse}
'''),
dict(id='2023-anor-1s5', s='anor', ex=1, titre='Exercice 1 -- Situation 5', theme='Agrandissement et aires',
     regions=[E1, (1, 626, 772)], s3=21, n3=[], s4=17, n4=[41],
     corr=r'''
\q{5}{Aire du polygone 2.}
\begin{reponse}
Un agrandissement de coefficient 3 multiplie les aires par $3^2 = 9$ : $11 \times 9 = \mathbf{99}$ cm².
\end{reponse}
'''),
dict(id='2023-anor-2a', s='anor', ex=2, titre='Exercice 2 -- La figure, questions 1 et 2', theme='Réciproque de Pythagore, théorème de Thalès',
     consigne='Traite les questions 1 et 2.', regions=[E2, (2, 128, 428)], s3=9, n3=[], s4=19, n4=[22, 32],
     corr=r'''
\q{1}{Montrer que LNA est rectangle en L.}
\begin{reponse}
Le plus grand côté est $[AN]$. \quad $AN^2 = 13^2 = 169$ \quad et \quad $LN^2 + AL^2 = 25 + 144 = 169$.\\
$AN^2 = LN^2 + AL^2$ : d'après la réciproque du théorème de Pythagore, $LNA$ est rectangle en $L$.
\end{reponse}
\q{2}{Montrer que OH = 7,2 cm.}
\begin{reponse}
$(AL) \perp (LN)$ et, d'après le codage, $(OH) \perp (LN)$ : les droites $(AL)$ et $(OH)$ sont parallèles.\\
Les points $N$, $O$, $L$ et $N$, $H$, $A$ sont alignés. D'après le théorème de Thalès :
\[ \frac{NO}{NL} = \frac{OH}{LA} \qquad\text{soit}\qquad \frac35 = \frac{OH}{12} \qquad\text{donc}\qquad OH = \frac{3 \times 12}{5} = 7{,}2 \text{ cm}. \]
\end{reponse}
'''),
dict(id='2023-anor-2b', s='anor', ex=2, titre='Exercice 2 -- La figure, questions 3 à 5', theme='Trigonométrie, triangles semblables, aires',
     consigne='Traite les questions 3 à 5 (LNA est rectangle en L et OH = 7,2 cm).', regions=[E2, (2, 128, 396), (2, 426, 496)], s3=10, n3=[6, 16], s4=None, n4=None,
     corr=r'''
\q{3}{Mesure de l'angle $\widehat{LNA}$.}
\begin{reponse}
Dans le triangle $LNA$ rectangle en $L$, $[LN]$ est le côté adjacent à $\widehat{LNA}$ et $[AN]$ l'hypoténuse :
\[ \cos\widehat{LNA} = \frac{LN}{AN} = \frac{5}{13} \qquad\text{donc}\qquad \widehat{LNA} \approx \mathbf{67^\circ}. \]
\end{reponse}
\q{4}{Pourquoi LNA et ONH sont-ils semblables ?}
\begin{reponse}
Ils ont l'angle $\widehat{LNA}$ en commun et chacun un angle droit ($\widehat{NLA}$ et $\widehat{NOH}$). Deux triangles qui ont deux angles de même mesure sont semblables.
\end{reponse}
\q{5.a}{Aire du quadrilatère LOHA.}
\begin{reponse}
$\mathcal{A}_{LNA} = \dfrac{5 \times 12}{2} = 30$ cm² \quad et \quad $\mathcal{A}_{ONH} = \dfrac{3 \times 7{,}2}{2} = 10{,}8$ cm².\\
$\mathcal{A}_{LOHA} = 30 - 10{,}8 = \mathbf{19{,}2}$ cm².
\end{reponse}
\q{5.b}{Proportion de l'aire de LNA.}
\begin{reponse}
$\dfrac{19{,}2}{30} = 0{,}64$ : le quadrilatère représente \textbf{64 \%} de l'aire du triangle.
\end{reponse}
'''),
dict(id='2023-anor-3a', s='anor', ex=3, titre='Exercice 3 -- Les visiteurs, partie A', theme='Lecture de diagramme, pourcentage',
     consigne='Traite la partie A.', regions=[(3, 146, 704)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{1.a}{Nombre de visiteurs en 2010.}
\begin{reponse}
\textbf{300 000} visiteurs.
\end{reponse}
\q{1.b}{Année du plus grand nombre de visiteurs.}
\begin{reponse}
\textbf{2019} (400\,000 visiteurs).
\end{reponse}
\q{2}{L'objectif d'au moins +15 \% a-t-il été atteint ?}
\begin{reponse}
Augmenter de 15 \%, c'est multiplier par 1,15 : $187\,216 \times 1{,}15 = 215\,298{,}4$.\\
$219\,042 > 215\,298{,}4$ : l'objectif est \textbf{atteint} (hausse d'environ 17 \%).
\end{reponse}
'''),
dict(id='2023-anor-3b', s='anor', ex=3, titre='Exercice 3 -- Les prix des hôtels, partie B', theme='Étendue, moyenne, médiane',
     consigne='Traite la partie B.', regions=[(3, 704, 790), (4, 128, 226)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{3}{Étendue des prix.}
\begin{reponse}
$500 - 60 = \mathbf{440}$ €.
\end{reponse}
\q{4}{Prix moyen d'une nuit.}
\begin{reponse}
Effectif total : $1\,200 + 1\,350 + 1\,000 + 1\,100 + 1\,200 + 1\,300 + 900 + 300 = 8\,350$ nuits.
\[ \bar{x} = \frac{60 \times 1\,200 + 80 \times 1\,350 + 85 \times 1\,000 + 90 \times 1\,100 + 110 \times 1\,200 + 120 \times 1\,300 + 350 \times 900 + 500 \times 300}{8\,350} = \frac{1\,117\,000}{8\,350} \approx \mathbf{134} \text{ €}. \]
\end{reponse}
\q{5}{« Au moins la moitié des nuits à moins de 100 € » ?}
\begin{reponse}
La moitié de 8\,350 est 4\,175. Nuits à moins de 100 € : $1\,200 + 1\,350 + 1\,000 + 1\,100 = 4\,650$, et $4\,650 > 4\,175$.\\
C'est \textbf{vrai} (la médiane est 90 €).
\end{reponse}
'''),
dict(id='2023-anor-4', s='anor', ex=4, titre='Exercice 4 -- Le motif « Fleur » (Scratch)', theme='Algorithmique (Scratch)',
     regions=[(4, 226, 616), (5, 128, 800), (6, 128, 192)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1.a}{Construire le parallélogramme KLMN (1 cm pour 5 pas).}
\begin{reponse}
$KL = 35 \div 5 = 7$ cm et $LM = 20 \div 5 = 4$ cm, avec $\widehat{KLM} = 120^\circ$ ; on termine en traçant les parallèles.
\end{reponse}
\q{1.b}{Lignes 4 à 7 du bloc « Pétale ».}
\begin{reponse}
Ligne 4 : avancer de \textbf{35} pas ; ligne 5 : tourner de \textbf{60} degrés ; ligne 6 : avancer de \textbf{20} pas ; ligne 7 : tourner de \textbf{120} degrés.\\
\small (Au sommet d'angle $120^\circ$, le lutin tourne de $180^\circ - 120^\circ = 60^\circ$ ; au sommet d'angle $60^\circ$, de $120^\circ$.)
\end{reponse}
\q{2.a}{Valeur de la ligne 2 du bloc « Fleur ».}
\begin{reponse}
\textbf{5} (la fleur a 5 pétales).
\end{reponse}
\q{2.b}{Pourquoi 72 ?}
\begin{reponse}
Les 5 pétales se répartissent sur un tour complet : $360^\circ \div 5 = 72^\circ$.
\end{reponse}
\q{2.c}{Modifications pour le nouveau motif.}
\begin{reponse}
Le motif a 12 pétales : ligne 2, \texttt{répéter 12 fois} ; ligne 4, \texttt{tourner de 30 degrés} ($360 \div 12 = 30$).
\end{reponse}
'''),
dict(id='2023-anor-5', s='anor', ex=5, titre='Exercice 5 -- L’hippodrome', theme='Périmètre, vitesse, coût minimum',
     regions=[(6, 190, 682)], s3=14, n3=[], s4=15, n4=[35, 36],
     corr=r'''
\q{1}{Longueur d'un tour de piste.}
\begin{reponse}
Les deux demi-cercles forment un cercle de rayon 40 m : $2 \times \pi \times 40 = 80\pi \approx 251$ m.\\
Tour : $2 \times 850 + 80\pi \approx 1\,700 + 251 = 1\,951$ m.
\end{reponse}
\q{2.a}{Vitesse moyenne en m/s.}
\begin{reponse}
2 min 9 s $= 129$ s. \quad $v = \dfrac{1\,951}{129} \approx \mathbf{15}$ m/s.
\end{reponse}
\q{2.b}{Vitesse en km/h.}
\begin{reponse}
15 m en 1 s, c'est $15 \times 3\,600 = 54\,000$ m en 1 h : \textbf{54 km/h}.
\end{reponse}
\q{3}{Marque la moins chère pour 73 027 m².}
\begin{reponse}
\begin{itemize}
\item A : $73\,027 \div 500 \approx 146{,}1$, il faut 147 sacs : $147 \times 141{,}95 = 20\,866{,}65$ € ;
\item B : $73\,027 \div 400 \approx 182{,}6$, il faut 183 sacs : $183 \times 87{,}90 = 16\,085{,}70$ € ;
\item C : $73\,027 \div 300 \approx 243{,}4$, il faut 244 sacs : $244 \times 66{,}50 = 16\,226$ €.
\end{itemize}
La marque \textbf{B} est la moins chère.
\end{reponse}
'''),
]
