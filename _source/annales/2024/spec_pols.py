# DNB Polynésie, septembre 2024
SOURCE = ('dnb_polynesie_sept_2024.pdf', 'Polynésie, septembre 2024')
E1 = (1, 285, 330)
PARTS = [
dict(id='2024-pols-1q1', s='pols', ex=1, titre='Exercice 1 -- Questions indépendantes, question 1', theme='Divisibilité, facteurs premiers',
     regions=[E1, (1, 330, 429)], s3=24, n3=[], s4=6, n4=[13, 14],
     corr=r'''
\q{1}{Nombres divisibles par 21.}
\begin{reponse}
$21 = 3 \times 7$ : la décomposition doit contenir le facteur 3 et le facteur 7.\\
Seuls le \textbf{nombre 4} ($2 \times 3 \times 5 \times 7$) et le \textbf{nombre 5} ($2^3 \times 3^2 \times 7$) conviennent (le nombre 2 n'a pas de facteur 7, le nombre 3 pas de facteur 3).
\end{reponse}
'''),
dict(id='2024-pols-1q2', s='pols', ex=1, titre='Exercice 1 -- Questions indépendantes, question 2', theme='Écriture scientifique',
     regions=[E1, (1, 429, 446)], s3=25, n3=[], s4=13, n4=[31],
     corr=r'''
\q{2}{Écriture scientifique de 0,000 002 76.}
\begin{reponse}
$\mathbf{2{,}76 \times 10^{-6}}$.
\end{reponse}
'''),
dict(id='2024-pols-1q3', s='pols', ex=1, titre='Exercice 1 -- Questions indépendantes, question 3', theme='Conversion de vitesse',
     regions=[E1, (1, 446, 463)], s3=14, n3=[], s4=15, n4=[36],
     corr=r'''
\q{3}{2 640 km/min en m/s.}
\begin{reponse}
2\,640 km $= 2\,640\,000$ m, parcourus en 1 min $= 60$ s : $2\,640\,000 \div 60 = \mathbf{44\,000}$ m/s.
\end{reponse}
'''),
dict(id='2024-pols-1q4', s='pols', ex=1, titre='Exercice 1 -- Questions indépendantes, question 4', theme='Équation produit',
     regions=[E1, (1, 463, 510)], s3=19, n3=[32], s4=None, n4=None,
     corr=r'''
\q{4}{Solutions de $(2x - 7)(3x + 1) = 0$.}
\begin{reponse}
Un produit est nul si l'un de ses facteurs est nul : $2x - 7 = 0 \iff x = \dfrac72$ \quad ou \quad $3x + 1 = 0 \iff x = -\dfrac13$.\\
Les solutions sont $\mathbf{\dfrac72}$ et $\mathbf{-\dfrac13}$.
\end{reponse}
'''),
dict(id='2024-pols-1q5', s='pols', ex=1, titre='Exercice 1 -- Questions indépendantes, question 5', theme='Fonction : calculer une image',
     regions=[E1, (1, 510, 546)], s3=3, n3=[5], s4=None, n4=None,
     corr=r'''
\q{5}{Image de $-3$ par $f(x) = 5x^2 + 2$.}
\begin{reponse}
$f(-3) = 5 \times (-3)^2 + 2 = 5 \times 9 + 2 = \mathbf{47}$.
\end{reponse}
'''),
dict(id='2024-pols-1q6', s='pols', ex=1, titre='Exercice 1 -- Questions indépendantes, question 6', theme='Théorème de Thalès',
     regions=[E1, (1, 546, 786)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{6}{Calculer DE.}
\begin{reponse}
Les points $C$, $E$, $A$ et $C$, $D$, $B$ sont alignés, et $(ED) \parallel (AB)$. $CB = CD + DB = 3 + 1 = 4$ cm. D'après le théorème de Thalès :
\[ \frac{CD}{CB} = \frac{DE}{BA} \qquad\text{soit}\qquad \frac34 = \frac{DE}{5} \qquad\text{donc}\qquad DE = \frac{3 \times 5}{4} = \mathbf{3{,}75} \text{ cm}. \]
\end{reponse}
'''),
dict(id='2024-pols-2a', s='pols', ex=2, titre='Exercice 2 -- Les températures, questions 1 à 4', theme='Tableur, moyenne, médiane, étendue',
     consigne='Traite les questions 1 à 4.', regions=[(2, 137, 466)], s3=23, n3=[], s4=11, n4=[24],
     corr=r'''
\q{1}{Formule pour la moyenne en B4.}
\begin{reponse}
\texttt{=MOYENNE(B2:J2)} \quad (ou \texttt{=SOMME(B2:J2)/9}).
\end{reponse}
\q{2}{Valeur approchée de la moyenne.}
\begin{reponse}
$\dfrac{216{,}4}{9} \approx 24{,}04$ : environ \textbf{24 °C}.
\end{reponse}
\q{3}{Interpréter la médiane.}
\begin{reponse}
La médiane est 24 °C : sur ces 9 années, au moins la moitié des 25 juin ont eu une température maximale inférieure ou égale à 24 °C, et au moins la moitié supérieure ou égale à 24 °C.
\end{reponse}
\q{4}{Température du 25 juin 2019.}
\begin{reponse}
De 2010 à 2018, la plus basse est 17,4 °C et la plus haute 29 °C (étendue 11,6). Avec 2019, l'étendue passe à 18,5 : la nouvelle valeur est une nouvelle extrémité.
\begin{itemize}
\item si c'est la plus haute : $17{,}4 + 18{,}5 = \mathbf{35{,}9}$ °C ;
\item si c'est la plus basse : $29 - 18{,}5 = 10{,}5$ °C (peu vraisemblable un 25 juin).
\end{itemize}
Le 25 juin 2019 (canicule), il a fait 35,9 °C.
\end{reponse}
'''),
dict(id='2024-pols-2b', s='pols', ex=2, titre='Exercice 2 -- Les températures, question 5', theme='Probabilités, pourcentage',
     consigne='Traite la question 5.', regions=[(2, 137, 318), (2, 466, 612)], s3=22, n3=[], s4=20, n4=[34, 47],
     corr=r'''
\q{5.a}{Probabilité d'une fiche à 26 °C.}
\begin{reponse}
Une fiche sur 9 : $p = \dfrac19$.
\end{reponse}
\q{5.b}{Probabilité d'une température inférieure ou égale à 24 °C.}
\begin{reponse}
23,1 ; 22,6 ; 17,4 ; 23,4 ; 24 : 5 fiches sur 9, $p = \dfrac59$.
\end{reponse}
\q{5.c}{Plus de 40 \% de chance d'avoir plus de 25 °C ?}
\begin{reponse}
29 ; 25,7 ; 25,2 ; 26 : 4 fiches sur 9, $p = \dfrac49 \approx 0{,}444$, soit environ 44 \%. $44 > 40$ : \textbf{oui}.
\end{reponse}
'''),
dict(id='2024-pols-3a', s='pols', ex=3, titre='Exercice 3 -- Les triangles, question 1', theme='Trigonométrie (tangente)',
     consigne='Traite la question 1.', regions=[(3, 137, 425)], s3=15, n3=[24], s4=None, n4=None,
     corr=r'''
\q{1}{Calculer MN, au millimètre.}
\begin{reponse}
Dans le triangle $ONM$ rectangle en $N$, $[MN]$ est le côté opposé à l'angle $\widehat{MON}$ et $[ON]$ le côté adjacent :
\[ \tan\widehat{MON} = \frac{MN}{ON} \qquad\text{donc}\qquad MN = 6 \times \tan 32^\circ \approx \mathbf{3{,}7} \text{ cm}. \]
\end{reponse}
'''),
dict(id='2024-pols-3b', s='pols', ex=3, titre='Exercice 3 -- Les triangles, questions 2 à 4', theme='Théorème de Pythagore, agrandissement et aires',
     consigne='Traite les questions 2 à 4 (MN ≈ 3,7 cm).', regions=[(3, 137, 408), (3, 424, 503)], s3=21, n3=[], s4=17, n4=[10, 41],
     corr=r'''
\q{2}{Montrer que OP = 6 cm.}
\begin{reponse}
Le triangle $OPQ$ est rectangle en $P$, d'hypoténuse $[OQ]$. D'après le théorème de Pythagore :
\[ OP^2 = OQ^2 - PQ^2 = 6{,}5^2 - 2{,}5^2 = 42{,}25 - 6{,}25 = 36 \qquad\text{donc}\qquad OP = 6 \text{ cm}. \]
\end{reponse}
\q{3}{Les triangles ONM et OPQ ne sont pas égaux.}
\begin{reponse}
Ils ont un côté de 6 cm et un angle droit, mais $MN \approx 3{,}7$ cm alors que $PQ = 2{,}5$ cm : leurs côtés ne sont pas tous égaux, ils ne sont pas égaux.
\end{reponse}
\q{4}{Aire du triangle ORS.}
\begin{reponse}
Rapport d'agrandissement : $\dfrac{OQ}{OS} = \dfrac{6{,}5}{3{,}25} = 2$. Les aires sont multipliées par $2^2 = 4$.\\
$\mathcal{A}_{OPQ} = \dfrac{OP \times PQ}{2} = \dfrac{6 \times 2{,}5}{2} = 7{,}5$ cm², donc $\mathcal{A}_{ORS} = 7{,}5 \div 4 = \mathbf{1{,}875}$ cm².
\end{reponse}
'''),
dict(id='2024-pols-4', s='pols', ex=4, titre='Exercice 4 -- Les pentagones (Scratch)', theme='Algorithmique (Scratch), transformations',
     consigne='L’annexe est à la fin de l’énoncé.', regions=[(3, 503, 790), (4, 128, 658), (6, 168, 765)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{1}{Justifier que $\widehat{FEy}$ mesure 72°.}
\begin{reponse}
Les points $D$, $E$, $y$ sont alignés : $\widehat{DEF} + \widehat{FEy} = 180^\circ$, donc $\widehat{FEy} = 180^\circ - 108^\circ = 72^\circ$.
\end{reponse}
\q{2.a}{Compléter le bloc « pentagone ».}
\begin{reponse}
\texttt{répéter 5 fois} ; \texttt{avancer de longueur pas} ; \texttt{tourner de 72 degrés} (le lutin tourne de l'angle extérieur, $72^\circ$, à chaque sommet).
\end{reponse}
\q{2.b}{Associer élève, copie d'écran et transformation.}
\begin{reponse}
\begin{tabular}{|l|c|l|}\hline
\entete Élève & Copie d'écran & Transformation \\\hline
Camille & 3 & translation (avancer de 120 pas) \\\hline
Lou & 1 & rotation (tourner de $60^\circ$) \\\hline
Zoé & 2 & symétrie centrale (tourner de $180^\circ$) \\\hline
\end{tabular}
\end{reponse}
\q{2.c}{Ordre des instructions du programme de Sofia.}
\begin{reponse}
1 : Quand drapeau cliqué ; 2 : effacer tout ; 3 : aller à x : 0 y : 0 ; 4 : s'orienter à 90 ; 5 : mettre longueur à 60 ; 6 : pentagone ; 7 : mettre longueur à longueur * 1.5 ; 8 : pentagone.\\
\small (Les instructions 2, 3 et 4 peuvent être placées dans un autre ordre.)
\end{reponse}
'''),
dict(id='2024-pols-5a', s='pols', ex=5, titre='Exercice 5 -- La piscine du camping, questions 1 et 2', theme='Volume du cylindre, débit',
     consigne='Traite les questions 1 et 2.', regions=[(5, 137, 256)], s3=21, n3=[34], s4=None, n4=None,
     corr=r'''
\q{1}{Volume du bassin.}
\begin{reponse}
$V = \pi \times 3{,}6^2 \times 1{,}5 = 19{,}44\pi \approx \mathbf{61{,}1}$ m³.
\end{reponse}
\q{2}{Volume restant à vider au bout de 2 heures.}
\begin{reponse}
En 2 h, la pompe vide $2 \times 14{,}1 = 28{,}2$ m³. Il reste $61{,}1 - 28{,}2 = \mathbf{32{,}9}$ m³.
\end{reponse}
'''),
dict(id='2024-pols-5b', s='pols', ex=5, titre='Exercice 5 -- La piscine du camping, questions 3 et 4', theme='Fonction affine, équation, lecture graphique',
     consigne='Traite les questions 3 et 4 (le bassin plein contient 61,1 m³).', regions=[(5, 137, 210), (5, 256, 590)], s3=17, n3=[13, 26], s4=None, n4=None,
     corr=r'''
\q{3.a}{Justifier l'expression $V(t) = 61{,}1 - 0{,}235t$.}
\begin{reponse}
La pompe vide $14{,}1$ m³ en 60 min, soit $14{,}1 \div 60 = 0{,}235$ m³ par minute. En $t$ minutes elle vide $0{,}235t$ m³ : il reste $61{,}1 - 0{,}235t$ m³.
\end{reponse}
\q{3.b}{Temps pour qu'il reste 30 m³.}
\begin{reponse}
\[ 61{,}1 - 0{,}235t = 30 \iff 0{,}235t = 31{,}1 \iff t = \frac{31{,}1}{0{,}235} \approx \mathbf{132} \text{ min}. \]
\end{reponse}
\q{4.a}{Antécédent de 40 par $V$.}
\begin{reponse}
On lit environ \textbf{90} : au bout d'environ 90 minutes, il reste 40 m³ d'eau dans le bassin.
\end{reponse}
\q{4.b}{Temps pour vider complètement le bassin.}
\begin{reponse}
La droite coupe l'axe des abscisses vers \textbf{260 minutes} (en effet $61{,}1 \div 0{,}235 = 260$), soit 4 h 20 min.
\end{reponse}
'''),
]
