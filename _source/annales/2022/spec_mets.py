# DNB Métropole (sujet de secours), juin 2022
SOURCE = ('dnb_metropole_secours_juin_2022.pdf', 'Métropole (secours), juin 2022')
QH = [(1, 194, 241)]
def aff(n, rows, s3, n3, s4, n4, theme, corr):
    return dict(id=f'2022-mets-1q{n}', s='mets', ex=1, titre=f'Exercice 1 -- Vrai ou faux, affirmation {n}', theme=theme,
                consigne=f'Traite seulement l’affirmation {n}.', regions=QH + rows, s3=s3, n3=n3, s4=s4, n4=n4, corr=corr)
PARTS = [
aff(1, [(1, 241, 412)], 22, [], 20, [47], 'Probabilités', r'''
\q{1}{Affirmation 1 : la probabilité de gagner une peluche est $\frac{1}{2}$.}
\begin{reponse}
Les 8 secteurs sont de même mesure et 4 portent « peluche » : $p = \dfrac{4}{8} = \dfrac{1}{2}$. L'affirmation est \textbf{vraie}.
\end{reponse}
'''),
aff(2, [(1, 410, 566)], 13, [], 14, [32], 'Réciproque du théorème de Pythagore', r'''
\q{2}{Affirmation 2 : le triangle ABC est rectangle.}
\begin{reponse}
Le plus grand côté est $[BC]$. $BC^2 = 7{,}5^2 = 56{,}25$ et $AB^2 + AC^2 = 4{,}5^2 + 6^2 = 20{,}25 + 36 = 56{,}25$.
D'après la réciproque du théorème de Pythagore, $ABC$ est rectangle en $A$ : l'affirmation est \textbf{vraie}.
\end{reponse}
'''),
aff(3, [(1, 565, 681)], 5, [], 12, [28], 'Addition de fractions', r'''
\q{3}{Affirmation 3 : les trois amis ont mangé tout le gâteau.}
\begin{reponse}
\[ \frac{3}{7} + \frac{2}{5} + \frac{1}{7} = \frac{15}{35} + \frac{14}{35} + \frac{5}{35} = \frac{34}{35} \neq 1. \]
Il reste $\frac{1}{35}$ du gâteau : l'affirmation est \textbf{fausse}.
\end{reponse}
'''),
aff(4, [(1, 680, 729)], 12, [18], None, None, 'Double distributivité', r'''
\q{4}{Affirmation 4 : $(2x+3)(5x-4) - 5(3x-2) = 10x^2 - 8x - 2$.}
\begin{reponse}
\[ (2x + 3)(5x - 4) - 5(3x - 2) = 10x^2 - 8x + 15x - 12 - 15x + 10 = 10x^2 - 8x - 2. \]
L'affirmation est \textbf{vraie}.
\end{reponse}
'''),
aff(5, [(1, 728, 791)], 2, [], 4, [], 'Angles d’un triangle', r'''
\q{5}{Affirmation 5 : le triangle DEF est isocèle.}
\begin{reponse}
$\widehat{DEF} + \widehat{FDE} = 180^\circ - 30^\circ = 150^\circ$ et $\widehat{DEF} = 4\,\widehat{FDE}$, donc $5\,\widehat{FDE} = 150^\circ$ et $\widehat{FDE} = 30^\circ$.
Le triangle a deux angles de $30^\circ$ : il est isocèle. L'affirmation est \textbf{vraie}.
\end{reponse}
'''),
dict(id='2022-mets-2', s='mets', ex=2, titre='Exercice 2 -- Les tapisseries', theme='Médiane, moyenne, tableur, pourcentage',
     regions=[(2, 136, 547)], s3=23, n3=[], s4=15, n4=[24, 34],
     corr=r'''
\q{1}{Tapisserie de surface maximale.}
\begin{reponse}
\textbf{L'Homme en gloire dans la paix} (57,5 m$^2$).
\end{reponse}
\q{2}{Surface médiane.}
\begin{reponse}
Rangées : 10,2 ; 12,8 ; 27,2 ; 30,9 ; \textbf{32,4} ; \textbf{39,2} ; 45,4 ; 45,4 ; 45,9 ; 57,5.
Il y a 10 valeurs : la médiane est la moyenne des 5\ieme{} et 6\ieme{}, $\dfrac{32{,}4 + 39{,}2}{2} = \mathbf{35{,}8}$ m$^2$.
\end{reponse}
\q{3}{Formule en B12.}
\begin{reponse}
\texttt{=SOMME(B2:B11)}.
\end{reponse}
\q{4}{Surface moyenne.}
\begin{reponse}
Total : 346,9 m$^2$. Moyenne : $346{,}9 \div 10 = \mathbf{34{,}69}$ m$^2$.
\end{reponse}
\q{5}{Sara a-t-elle raison ?}
\begin{reponse}
4 tapisseries sur 10 dépassent 45 m$^2$ (45,4 ; 45,4 ; 45,9 ; 57,5) : $\dfrac{4}{10} = 40$ \%. \textbf{Sara a raison}.
\end{reponse}
'''),
dict(id='2022-mets-3a', s='mets', ex=3, titre='Exercice 3 -- La salle de sport, questions 1 et 2', theme='Calculs de prix',
     consigne='Traite les questions 1 et 2.', regions=[(2, 545, 656)], s3=14, n3=[], s4=5, n4=[11],
     corr=r'''
\q{1}{Coût de dix séances.}
\begin{reponse}
$32 + 10 \times 4{,}50 = 32 + 45 = \mathbf{77}$ €.
\end{reponse}
\q{2}{Nombre de séances avec 95 €.}
\begin{reponse}
Après la carte, il reste $95 - 32 = 63$ € et $63 \div 4{,}50 = 14$ : \textbf{14 séances}.
\end{reponse}
'''),
dict(id='2022-mets-3b', s='mets', ex=3, titre='Exercice 3 -- La salle de sport, question 3', theme='Fonction affine, image',
     consigne='Traite seulement la question 3.', regions=[(2, 545, 604), (2, 655, 736)], s3=17, n3=[27, 28], s4=None, n4=None,
     corr=r'''
\q{3.a}{Expression de $p(x)$.}
\begin{reponse}
$\mathbf{p(x) = 4{,}5x + 32}$.
\end{reponse}
\q{3.b}{Vérifier que $p(27) = 153{,}5$.}
\begin{reponse}
$p(27) = 4{,}5 \times 27 + 32 = 121{,}5 + 32 = 153{,}5$.
\end{reponse}
\q{3.c}{Interprétation.}
\begin{reponse}
\textbf{27 séances dans l'année coûtent 153,50 €.}
\end{reponse}
'''),
dict(id='2022-mets-3c', s='mets', ex=3, titre='Exercice 3 -- La salle de sport, question 4', theme='Algorithmique (Scratch)',
     consigne='Traite seulement la question 4 (complète les lignes 4 et 5 sur ta copie).', regions=[(2, 545, 604), (2, 735, 790), (3, 120, 352)], s3=0, n3=[], s4=0, n4=[],
     corr=r'''
\q{4}{Compléter les lignes 4 et 5.}
\begin{reponse}
Ligne 4 : mettre résultat à nombre de séances * \textbf{4.5}.
Ligne 5 : mettre résultat à \textbf{32} + résultat.
\end{reponse}
'''),
dict(id='2022-mets-4a', s='mets', ex=4, titre='Exercice 4 -- Le contre-la-montre, questions 1, 2 et 4', theme='Lecture graphique, vitesse moyenne',
     consigne='Traite les questions 1, 2 et 4.', regions=[(3, 352, 746), (4, 203, 236)], s3=14, n3=[], s4=15, n4=[21, 35],
     corr=r'''
\q{1}{Distance parcourue en 20 minutes.}
\begin{reponse}
Je lis l'abscisse du point de la courbe d'ordonnée 20 : environ \textbf{17 km}.
\end{reponse}
\q{2}{Durée des 27,2 km.}
\begin{reponse}
Je lis l'ordonnée du point d'abscisse 27,2 : environ \textbf{32 min}.
\end{reponse}
\q{4}{La vitesse moyenne dépasse-t-elle 50 km/h ?}
\begin{reponse}
27,2 km en 32 min : en 60 min, $27{,}2 \times \dfrac{60}{32} = 51$ km. Sa vitesse moyenne est d'environ 51 km/h : \textbf{oui}, elle dépasse 50 km/h.
\end{reponse}
'''),
dict(id='2022-mets-4lec', s='mets', ex=4, titre='Exercice 4 -- Le contre-la-montre, questions 1 et 2', theme='Lecture graphique', extra=True,
     consigne='Traite seulement les questions 1 et 2.', regions=[(3, 352, 746)], s3=8, n3=[], s4=9, n4=[21],
     corr=r'''
\q{1}{Distance parcourue en 20 minutes.}
\begin{reponse}
Je lis l'abscisse du point de la courbe d'ordonnée 20 : environ \textbf{17 km}.
\end{reponse}
\q{2}{Durée des 27,2 km.}
\begin{reponse}
Je lis l'ordonnée du point d'abscisse 27,2 : environ \textbf{32 min}.
\end{reponse}
'''),
dict(id='2022-mets-4b', s='mets', ex=4, titre='Exercice 4 -- Le contre-la-montre, question 3', theme='Fonction linéaire : représentation graphique',
     consigne='Traite seulement la question 3 (trace la droite sur une copie du graphique).', regions=[(3, 352, 712), (3, 746, 790), (4, 120, 204)], s3=17, n3=[26, 28], s4=None, n4=None,
     corr=r'''
\q{3.a}{Représenter $f(x) = 1{,}4x$.}
\begin{reponse}
$f$ est linéaire : sa représentation est une droite qui passe par l'origine. Avec $f(20) = 28$, elle passe aussi par le point $(20\,;28)$.
\end{reponse}
\q{3.b}{Quel coureur est classé avant l'autre ?}
\begin{reponse}
Bryan Coquard met $f(27{,}2) = 1{,}4 \times 27{,}2 \approx 38$ min, contre environ 32 min pour Tadej Pogacar : \textbf{Pogacar} est classé avant.
\end{reponse}
'''),
dict(id='2022-mets-5a', s='mets', ex=5, titre='Exercice 5 -- La tour de la Vade, question 1', theme='Droites parallèles, théorème de Thalès',
     consigne='Traite seulement la question 1.', regions=[(4, 244, 632)], s3=9, n3=[], s4=10, n4=[22],
     corr=r'''
\q{1.a}{Montrer que (FG) et (AB) sont parallèles.}
\begin{reponse}
$(FG)$ et $(AB)$ sont toutes les deux perpendiculaires au sol, la droite $(MB)$ : elles sont parallèles.
\end{reponse}
\q{1.b}{Hauteur AB de la tour.}
\begin{reponse}
$MB = 3 + 51 = 54$ m. Les points $M$, $F$, $A$ et $M$, $G$, $B$ sont alignés et $(FG) \parallel (AB)$. D'après le théorème de Thalès :
\[ \frac{MG}{MB} = \frac{FG}{AB} \qquad\text{donc}\qquad \frac{3}{54} = \frac{1{,}4}{AB} \qquad\text{et}\qquad AB = \frac{54 \times 1{,}4}{3} = \mathbf{25{,}2} \text{ m}. \]
\end{reponse}
'''),
dict(id='2022-mets-5b', s='mets', ex=5, titre='Exercice 5 -- La tour de la Vade, questions 2 à 4', theme='Volume du cylindre, réduction, aire latérale',
     consigne='Traite les questions 2 à 4 (la tour mesure 25,2 m de haut).', regions=[(4, 244, 356), (4, 630, 790)], s3=21, n3=[34, 37], s4=None, n4=None,
     corr=r'''
\q{2}{Volume de la tour.}
\begin{reponse}
Le rayon vaut 7 m : $V = \pi \times 7^2 \times 25{,}2 \approx 3\,879$ m$^3$, soit environ \textbf{3\,880 m$^3$}.
\end{reponse}
\q{3}{Volume de la maquette.}
\begin{reponse}
Les longueurs sont divisées par 20, donc le volume par $20^3 = 8\,000$ : $3\,880 \div 8\,000 = \mathbf{0{,}485}$ m$^3$ (485 L).
\end{reponse}
\q{4}{Coût du traitement.}
\begin{reponse}
Aire latérale : $2 \times \pi \times 7 \times 25{,}2 \approx 1\,108{,}4$ m$^2$. Coût : $1\,108{,}4 \times 39 \approx \mathbf{43\,226}$ €.
(Si l'on traite aussi le dessus de la tour, on ajoute $\pi \times 7^2 \approx 154$ m$^2$, soit environ 49\,230 € en tout.)
\end{reponse}
'''),
]
