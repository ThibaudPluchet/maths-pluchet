# DNB Métropole Antilles-Guyane, 30 juin 2022
SOURCE = ('dnb_metropole_juin_2022.pdf', 'Métropole Antilles-Guyane, 30 juin 2022')
QH = [(1, 694, 758), (2, 154, 178)]
def qcm(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2022-metj-2q{n}', s='metj', ex=2, titre=f'Exercice 2 -- QCM, question {n}', theme=theme,
                consigne=f'Traite seulement la question {n}.', regions=QH + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
dict(id='2022-metj-1a', s='metj', ex=1, titre='Exercice 1 -- La rivière, questions 1 et 2', theme='Droites parallèles, théorème de Thalès',
     consigne='Traite les questions 1 et 2.', regions=[(1, 320, 586)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{1}{Démontrer que (AC) et (BD) sont parallèles.}
\begin{reponse}
D'après le schéma, $(AC)$ et $(BD)$ sont toutes les deux perpendiculaires à la droite $(AB)$ : elles sont donc parallèles.
\end{reponse}
\q{2}{Largeur AC de la rivière, en pas.}
\begin{reponse}
Les points $C$, $E$, $D$ et $A$, $E$, $B$ sont alignés et $(AC) \parallel (BD)$. D'après le théorème de Thalès :
\[ \frac{EA}{EB} = \frac{EC}{ED} = \frac{AC}{BD} \qquad\text{donc}\qquad \frac{20}{5} = \frac{AC}{1} \qquad\text{et}\qquad AC = \mathbf{4} \text{ pas}. \]
\end{reponse}
'''),
dict(id='2022-metj-1b', s='metj', ex=1, titre='Exercice 1 -- La rivière, questions 3 et 4', theme='Théorème de Pythagore, vitesse',
     consigne='Traite les questions 3 et 4 (la rivière mesure AC = 4 pas).', regions=[(1, 320, 550), (1, 586, 697)], s3=14, n3=[], s4=15, n4=[10, 35],
     corr=r'''
\q{3}{Montrer que CE vaut 13,3 m.}
\begin{reponse}
Le triangle $AEC$ est rectangle en $A$. D'après le théorème de Pythagore :
\[ CE^2 = AE^2 + AC^2 = 20^2 + 4^2 = 416 \qquad\text{donc}\qquad CE = \sqrt{416} \approx 20{,}4 \text{ pas}. \]
En mètres : $\sqrt{416} \times 0{,}65 \approx 13{,}26$ m, soit \textbf{13,3 m} au décimètre près.
\end{reponse}
\q{4.a}{Vitesse du bâton en m/s.}
\begin{reponse}
$v = \dfrac{13{,}3}{5} = \mathbf{2{,}66}$ m/s.
\end{reponse}
\q{4.b}{Le bâton va-t-il à moins de 10 km/h ?}
\begin{reponse}
En 1 h $= 3\,600$ s, il parcourt $2{,}66 \times 3\,600 = 9\,576$ m, soit environ 9,6 km : $9{,}6 < 10$, \textbf{c'est vrai}.
\end{reponse}
'''),
qcm(1, [(2, 176, 308)], 11, [], 7, [16], 'Translation', r'''
\q{1}{Transformation qui transforme la figure 1 en figure 2.}
\begin{reponse}
La figure garde sa forme, sa taille et son sens ; tous les points glissent de la même façon : c'est une \textbf{translation}, \textbf{réponse A}.
\end{reponse}
'''),
qcm(2, [(2, 305, 461)], 8, [12], None, None, 'Antécédent, lecture graphique', r'''
\q{2}{Antécédent de 2 par $g$.}
\begin{reponse}
Je cherche l'abscisse du point de la courbe d'ordonnée 2 : c'est \textbf{1}, \textbf{réponse B}.
\end{reponse}
'''),
qcm(3, [(2, 458, 528)], 3, [5], None, None, 'Fonction : calculer une image', r'''
\q{3}{Affirmation correcte pour $f(x) = 3x^2 - 7$.}
\begin{reponse}
Je remplace $x$ par 3 : $f(3) = 3 \times 3^2 - 7 = 27 - 7 = 20$, \textbf{réponse B}.
($f(2) = 5$, et $f$ n'est pas affine à cause du $x^2$.)
\end{reponse}
'''),
qcm(4, [(2, 525, 627)], 23, [], 11, [24], 'Médiane', r'''
\q{4}{Médiane des 13 performances.}
\begin{reponse}
Rangées : 3,41 ; 3,7 ; 4,01 ; 4,28 ; 4,3 ; 4,62 ; \textbf{4,91} ; 5,15 ; … Il y a 13 valeurs : la médiane est la 7\ieme{}, \textbf{4,91 m}, \textbf{réponse B}.
\end{reponse}
'''),
qcm(5, [(3, 156, 369)], 21, [16, 37], None, None, 'Triangles semblables, aires', r'''
\q{5}{Coefficient pour passer de l'aire de LAC à celle de BUT.}
\begin{reponse}
$\dfrac{6{,}3}{2{,}1} = \dfrac{7{,}2}{2{,}4} = \dfrac{7{,}5}{2{,}5} = 3$ : les longueurs sont multipliées par 3, donc les aires par $3^2 = \mathbf{9}$, \textbf{réponse C}.
\end{reponse}
'''),
dict(id='2022-metj-3a', s='metj', ex=3, titre='Exercice 3 -- Les cartes Pokémon, questions 1 et 2', theme='Décomposition en facteurs premiers, répartition',
     consigne='Traite les questions 1 et 2.', regions=[(3, 389, 616)], s3=24, n3=[], s4=6, n4=[14, 15],
     corr=r'''
\q{1.a}{Décomposition de 252.}
\begin{reponse}
9 et 21 ne sont pas premiers : c'est la \textbf{proposition 3}, $252 = 2^2 \times 3^2 \times 7$.
\end{reponse}
\q{1.b}{Décomposition de 156.}
\begin{reponse}
$156 = 2 \times 78 = 2 \times 2 \times 39 = 2 \times 2 \times 3 \times 13$, soit $\mathbf{156 = 2^2 \times 3 \times 13}$.
\end{reponse}
\q{2.a}{Peut-elle faire 36 paquets ?}
\begin{reponse}
$156 \div 36 \approx 4{,}33$ n'est pas entier : \textbf{non}.
\end{reponse}
\q{2.b}{Nombre maximum de paquets.}
\begin{reponse}
Le nombre de paquets doit diviser 252 et 156. Le plus grand diviseur commun est $2^2 \times 3 = \mathbf{12}$ paquets.
\end{reponse}
\q{2.c}{Contenu de chaque paquet.}
\begin{reponse}
$252 \div 12 = 21$ et $156 \div 12 = 13$ : \textbf{21 cartes « feu » et 13 cartes « terre »}.
\end{reponse}
'''),
dict(id='2022-metj-3b', s='metj', ex=3, titre='Exercice 3 -- Les cartes Pokémon, question 3', theme='Probabilités',
     consigne='Traite seulement la question 3.', regions=[(3, 389, 440), (3, 616, 660)], s3=22, n3=[], s4=20, n4=[47],
     corr=r'''
\q{3}{Probabilité de tirer une carte « terre ».}
\begin{reponse}
Elle a $252 + 156 = 408$ cartes, dont 156 « terre » : $p = \dfrac{156}{408} = \mathbf{\dfrac{13}{34}} \approx 0{,}38$.
\end{reponse}
'''),
dict(id='2022-metj-4a', s='metj', ex=4, titre='Exercice 4 -- Rectangle et carré, questions 1 et 2', theme='Aire, double distributivité',
     consigne='Traite les questions 1 et 2.', regions=[(3, 672, 750), (4, 120, 336)], s3=12, n3=[18], s4=None, n4=None,
     corr=r'''
\q{1}{Aire du carré.}
\begin{reponse}
$x \times x = \mathbf{x^2}$.
\end{reponse}
\q{2}{Montrer que l'aire du rectangle est $x^2 + 4x - 21$.}
\begin{reponse}
Je développe avec la double distributivité :
\[ (x - 3)(x + 7) = x^2 + 7x - 3x - 21 = x^2 + 4x - 21. \]
\end{reponse}
'''),
dict(id='2022-metj-4b', s='metj', ex=4, titre='Exercice 4 -- Rectangle et carré, questions 3 et 4', theme='Algorithmique (Scratch)',
     consigne='Traite les questions 3 et 4.', regions=[(3, 672, 750), (4, 120, 240), (4, 316, 617)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{3}{Contenu des cases des lignes 5, 6 et 7.}
\begin{reponse}
La ligne 4 met $x^2$ dans R ; il faut ajouter $4x$ puis $-21$.
Ligne 5 : \textbf{4} ; ligne 6 : \textbf{-21} ; ligne 7 : \textbf{R}.
\end{reponse}
\q{4}{Résultat pour 8.}
\begin{reponse}
$8^2 + 4 \times 8 - 21 = 64 + 32 - 21 = 75$ : le programme dit \textbf{« L'aire du rectangle est 75 »}.
\end{reponse}
'''),
dict(id='2022-metj-4c', s='metj', ex=4, titre='Exercice 4 -- Rectangle et carré, question 5', theme='Équation',
     consigne='Traite seulement la question 5 (l’aire du rectangle est x² + 4x − 21).', regions=[(3, 672, 750), (4, 120, 240), (4, 617, 648)], s3=7, n3=[], s4=16, n4=[38],
     corr=r'''
\q{5}{Valeur de $x$ pour laquelle les aires sont égales.}
\begin{reponse}
Je résous $x^2 + 4x - 21 = x^2$. J'enlève $x^2$ à chaque membre :
\[ 4x - 21 = 0 \iff 4x = 21 \iff x = 5{,}25. \]
Il faut choisir $\mathbf{x = 5{,}25}$ (qui est bien supérieur à 3).
\end{reponse}
'''),
dict(id='2022-metj-5a', s='metj', ex=5, titre='Exercice 5 -- La fuite d’eau, questions 1 à 4', theme='Durées, conversions, volume du cylindre',
     consigne='Traite les questions 1 à 4.', regions=[(4, 660, 778), (5, 120, 416)], s3=21, n3=[34], s4=None, n4=None,
     corr=r'''
\q{1}{Nombre de gouttes en une journée.}
\begin{reponse}
Une journée dure $24 \times 60 \times 60 = 86\,400$ s ; à une goutte par seconde, il tombe \textbf{86\,400 gouttes}.
\end{reponse}
\q{2}{Volume tombé en une semaine.}
\begin{reponse}
$86\,400 \times 7 = 604\,800$ gouttes ; $604\,800 \div 20 = 30\,240$ mL, soit \textbf{30,24 L}.
\end{reponse}
\q{3}{Volume de la vasque.}
\begin{reponse}
Le rayon vaut $40 \div 2 = 20$ cm : $V = \pi \times 20^2 \times 15 = 6\,000\pi \approx 18\,849{,}6$ cm$^3$.
Or 1 L $=$ 1 dm$^3$ $=$ 1\,000 cm$^3$ : $V \approx \mathbf{18{,}85}$ L.
\end{reponse}
\q{4}{L'eau va-t-elle déborder ?}
\begin{reponse}
$30{,}24 > 18{,}85$ : \textbf{oui}, l'eau va déborder.
\end{reponse}
'''),
dict(id='2022-metj-5b', s='metj', ex=5, titre='Exercice 5 -- La fuite d’eau, question 5', theme='Pourcentage d’évolution',
     consigne='Traite seulement la question 5.', regions=[(4, 660, 676), (5, 414, 516)], s3=14, n3=[], s4=15, n4=[34],
     corr=r'''
\q{5}{Pourcentage de diminution entre 2004 et 2018.}
\begin{reponse}
La baisse est de $165 - 148 = 17$ L. $\dfrac{17}{165} \approx 0{,}103$ : la consommation a baissé d'environ \textbf{10 \%}.
\end{reponse}
'''),
]
