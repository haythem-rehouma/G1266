
# Évaluation — Gridworld (Itérations vs Épisodes)

## Rappels (référence)

Formule de Bellman (itération de valeur) :

$$
V_k(s) = \max_{a} \sum_{s'} T(s,a,s')\Big[\,R(s,a,s') + \gamma\,V_{k-1}(s')\,\Big]
$$

Coût d’une issue particulière $s'$ :

$$
c_k(s,a\to s') = R(s,a,s') + \gamma\,V_{k-1}(s')
$$

Agrégation (pour une action $a$) :

$$
Q_k(s,a) = \sum_{s'} T(s,a,s')\Big[\,R(s,a,s') + \gamma\,V_{k-1}(s')\,\Big],
\qquad
V_k(s) = \max_a Q_k(s,a).
$$



## Partie 0 — Questions flash (20 pts)

**Q0.1 (4 pts)** Coche la bonne définition.  
- [ ] Itération = jouer un trajet dans l’environnement.  
- [ ] Itération = mettre à jour les valeurs $V(s)$ sans jouer. ✅  
- [ ] Épisode = mettre à jour $V(s)$ hors-ligne.  
- [ ] Épisode = jouer un trajet du départ jusqu’au terminal. ✅

**Q0.2 (4 pts)** Que fait `-i K` avec `-a value` ?  
- [ ] Lance $K$ épisodes d’apprentissage.  
- [x] Réalise $K$ mises à jour de Bellman (hors-ligne).  
- [ ] Change le bruit (noise).  
- [ ] Change la récompense de sortie.

**Q0.3 (4 pts)** Avec **noise = 0.2**, si l’on vise **Nord**, quelles sont les probabilités ?  
- [x] 0.8 vers Nord, 0.1 vers Ouest, 0.1 vers Est.  
- [ ] 0.8 vers Nord, 0.2 vers Sud.  
- [ ] 1.0 vers Nord.

**Q0.4 (4 pts)** Effet d’un **living reward négatif** (ex. $-0.2$) :  
- [x] Chemins plus courts (éviter de traîner).  
- [ ] Chemins plus longs.  
- [ ] Aucun effet.

**Q0.5 (4 pts)** $\gamma$ proche de 1 (ex. 0.99) rend l’agent…  
- [x] Plus sensible aux gains futurs.  
- [ ] Indifférent au futur.  
- [ ] Allergique aux récompenses positives.



## Partie A — Compréhension (20 pts)

**A1 (10 pts).** En 4–6 lignes, expliquer la différence entre **itération** (`-i K`) et **épisode** (`-k M`) pour `-a value` **et** `-a q`.

**A2 (5 pts).** Pourquoi les cases proches de $-1$ prennent souvent des valeurs plus faibles quand le bruit est non nul ?

**A3 (5 pts).** Donner un exemple concret où augmenter $\gamma$ change la politique.



## Partie B — Calculs légers (20 pts)

Contexte : **BookGrid**, living reward = 0, $\gamma=0.9$, noise = 0.2.

**B1 (10 pts).** Reproduire le calcul qui donne **0.72** pour la case **juste à gauche du +1** à $k=2$.  
(Indice : viser Est. Issues : Est 0.8 $\rightarrow V=1$, Nord 0.1 $\rightarrow V=0$, Sud 0.1 $\rightarrow V=0$.)

**B2 (10 pts).** Montrer pourquoi une case encore **une colonne plus à gauche** vaut environ **0.52** à $k=3$ (propagation depuis la case à 0.72, même schéma de bruit).



## Partie C — Mini-expériences (25 pts)

Fournir pour chaque commande : **commande exacte**, **capture**, **2–3 lignes** d’explication.

**C1 (10 pts).**
```bash
python gridworld.py -a value -i 1 --text
python gridworld.py -a value -i 2 --text
python gridworld.py -a value -i 3 --text
````

Expliquer la **propagation** des valeurs depuis $+1$ et $-1$.

**C2 (5 pts).**

```bash
python gridworld.py -a value -i 12 -k 2 --text
```

Décrire la **trajectoire** suivie et son lien avec les valeurs $V$.

**C3 (10 pts).**

```bash
python gridworld.py -a value -i 12 -k 2 --livingReward -0.2 --text
python gridworld.py -a value -i 12 -k 2 --noise 0.0 --text
python gridworld.py -a value -i 12 -k 2 --noise 0.4 --text
```

Comparer qualitativement les trajectoires (plus directes ? plus prudentes ? détours ?) et expliquer **pourquoi**.



## Partie D — Synthèse courte (15 pts)

**D1 (8 pts).** Proposer une **règle intuitive** de politique dans BookGrid quand **noise = 0.2** (4–6 lignes).

**D2 (7 pts).** Prédire l’effet de `--livingReward +0.1` sur la politique, en 3–5 lignes.



## Barème récapitulatif (100 pts)

* Partie 0 (flash) : 20 pts
* Partie A (compréhension) : 20 pts
* Partie B (calculs) : 20 pts
* Partie C (expériences) : 25 pts
* Partie D (synthèse) : 15 pts



## *Annexe — Exemples de commandes utiles*

```bash
# Valeurs uniquement (pas d’épisode)
python gridworld.py -a value -i 12 --text

# Visualiser la politique calculée par V (2 épisodes)
python gridworld.py -a value -i 12 -k 2 --text

# Q-learning : apprentissage par épisodes
python gridworld.py -a q -k 50 -d 0.9 -l 0.5 -e 0.3 --text
```




<br/>

# Partie E

## À exécuter

```bash
python gridworld.py -a value -i 12 -k 2 --text
C:\Python27\python gridworld.py -a value -i 100 -k 10 -d 0.9 -r 0.0 -n 0.2 -g BookGrid
# Voir l'évolution itération par itération :
python gridworld.py -a value -i 1 -v
python gridworld.py -a value -i 2 -v
python gridworld.py -a value -i 5 -v
python gridworld.py -a value -i 10 -v
python gridworld.py -a value -i 100 -v
````












Ce que vous devez écrire

1. **Formule générale** (obligatoire, sans commentaire)

   Mise à jour de Bellman 

$$
   V_k(s)=\max_{a}\sum_{s'} T(s,a,s')\big[\,R(s,a,s')+\gamma\,V_{k-1}(s')\,\big]
$$

   Définir aussi :

$$
   Q_k(s,a)=\sum_{s'} T(s,a,s')\big[\,R(s,a,s')+\gamma\,V_{k-1}(s')\,\big],
   \qquad
   V_k(s)=\max_{a} Q_k(s,a).
$$

2. **Pour `-i 1 -v`**

   Choisir **une** case non terminale et écrire les 4 sommes
   
$$
Q_1(s,\text{Nord})$, $Q_1(s,\text{Est})$, $Q_1(s,\text{Sud})$, $Q_1(s,\text{Ouest})$ en utilisant $V_0
$$

   Conclure par $V_1(s)=\max_{a} Q_1(s,a)$.

4. **Pour `-i 2 -v`**

   Pour la **même case**, réécrire $Q_2(s,a)$ avec $V_1$ (valeurs du tour précédent).

   Donner $V_2(s)$.

5. **Pour `-i 5 -v` et `-i 10 -v`**

   Écrire **seulement** l’action optimale $a^*$ (celle qui réalise le max) et
   l’expression **compacte** de $Q_k(s,a^*)$ (somme pondérée des trois issues avec probabilités 0.8 / 0.1 / 0.1).

   **Pas de prose** : juste l’expression mathématique.

6. **Pour `-i 100 -v`**

   Écrire l’égalité fixe attendue pour la même case

$$
   V_{100}(s)=\max_{a}\sum_{s'} T(s,a,s')\big[\,R(s,a,s')+\gamma\,V_{100}(s')\,\big]
$$

   (montrer que $V_{100}$ s’auto-référence à l’optimum — point fixe).

7. Pour la commande avec épisodes (`-i 12 -k 2 --text`)

   Écrire la **politique** pour 2–3 cases visitées :

$$
   \pi(s)=\arg\max_{a} Q_{12}(s,a)
$$

   Lister seulement $\pi(s)$ pour les cases traversées.

> Paramètres communs à prendre dans vos équations : $\gamma=0.9$, living reward $=0$, noise $=0.2$
> (donc issues 0.8 / 0.1 / 0.1 ; si un mur est rencontré, utiliser $s'=s$).







<br/>
<br/>
<br/>


# Partie F


**Règle d’or :**

* `-i N` = **N itérations** (mise à jour des valeurs, hors-ligne)
* `-k M` = **M épisodes** (exécutions dans l’environnement)

Écrivez **exactement** la commande demandée (une ligne par question).
Utilisez `python` (ou `python3` si besoin). Ajoutez `--text` si c’est spécifié.
Aucune explication : **juste la commande**.

1. Lancer **1 itération** de l’algorithme par valeur et **voir les étapes** de mise à jour.
   → Commande : `python gridworld.py …` (avec l’option pour voir les steps)

2. Lancer **2 itérations** et **voir les étapes**.

3. Lancer **5 itérations** et **voir les étapes**.

4. Lancer **10 itérations** et **voir les étapes**.

5. Lancer **100 itérations** et **voir les étapes**.

6. Lancer **12 itérations** et **2 épisodes** en **mode texte** (affichage console).

7. Lancer **100 itérations**, **10 épisodes**, avec **γ = 0.9**, **livingReward = 0.0**, **noise = 0.2**, **BookGrid**, en **mode texte**.

8. Lancer **50 épisodes** de **Q-learning** (pas d’itérations), avec `γ=0.9`, `α=0.5`, `ε=0.3`, en **mode texte**.

9. Lancer **30 itérations**, **1 épisode**, **sans bruit** (noise = 0.0), en **mode texte**.

10. Lancer **12 itérations**, **2 épisodes**, avec **livingReward = -0.2**, en **mode texte**.

> Indication : options possibles selon les besoins
> `-a value` | `-a q` · `-i` · `-k` · `--text` · `-d` (discount γ) · `-r` (livingReward) · `-n` (noise) · `-g` (grille) · `-v` (valueSteps)



<br/>

# Corrigé 

1. **1 itération + steps**
   `python gridworld.py -a value -i 1 -v`

2. **2 itérations + steps**
   `python gridworld.py -a value -i 2 -v`

3. **5 itérations + steps**
   `python gridworld.py -a value -i 5 -v`

4. **10 itérations + steps**
   `python gridworld.py -a value -i 10 -v`

5. **100 itérations + steps**
   `python gridworld.py -a value -i 100 -v`

6. **12 itérations + 2 épisodes + mode texte**
   `python gridworld.py -a value -i 12 -k 2 --text`

7. **100 itérations + 10 épisodes + params + BookGrid + mode texte**
   `python gridworld.py -a value -i 100 -k 10 -d 0.9 -r 0.0 -n 0.2 -g BookGrid --text`

8. **Q-learning : 50 épisodes (pas d’itérations) + params + mode texte**
   `python gridworld.py -a q -k 50 -d 0.9 -l 0.5 -e 0.3 --text`
   *(Remarque : `-i` est **inutile** pour `-a q`.)*

9. **30 itérations + 1 épisode + noise 0.0 + mode texte**
   `python gridworld.py -a value -i 30 -k 1 --noise 0.0 --text`
   (ou : `-n 0.0`)

10. **12 itérations + 2 épisodes + livingReward -0.2 + mode texte**
    `python gridworld.py -a value -i 12 -k 2 --livingReward -0.2 --text`
    (ou : `-r -0.2`)



# Barème rapide 

* Q1–Q5 (itérations + `-v`) : **1 pt** chacune = 5 pts
  (Doit avoir `-a value`, `-i N`, `-v`.)

* Q6 (mix itérations + épisodes + `--text`) : **2 pts**
  (`-a value`, `-i 12`, `-k 2`, `--text`)

* Q7 (config complète) : **4 pts**
  (Tous les flags présents et corrects : `-i 100`, `-k 10`, `-d 0.9`, `-r 0.0`, `-n 0.2`, `-g BookGrid`, `--text`, `-a value`)

* Q8 (Q-learning, **pas d’`-i`**) : **4 pts**
  (Doit avoir `-a q`, `-k 50`, `-d 0.9`, `-l 0.5`, `-e 0.3`, `--text`.
  **0 pt** si l’étudiant met `-i`.)

* Q9 (noise 0.0) : **2 pts**
  (`-a value`, `-i 30`, `-k 1`, `--noise 0.0`, `--text`)

* Q10 (livingReward négatif) : **3 pts**
  (`-a value`, `-i 12`, `-k 2`, `--livingReward -0.2`, `--text`)



# ❌ Erreurs fréquentes à pénaliser

* Confondre **`-i`** (itérations) et **`-k`** (épisodes).
* Oublier **`-v`** dans Q1–Q5.
* Mettre **`-i`** avec `-a q` (inutile/mauvaise compréhension).
* Oublier `--text` quand demandé.
* Mauvaise option courte/longue (ex. `-n` vs `--noise`) : tolérer si la valeur est correcte, sauf si la question **impose** l’une.


