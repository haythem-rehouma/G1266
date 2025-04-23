# **EXAMEN MI-SESSION : APPRENTISSAGE PAR RENFORCEMENT**

---

### **Barème global :**

L'examen est noté sur **100 points** répartis comme suit :

- **Partie 1 : Questions à choix multiples** (20 points)
  - 5 questions à 4 points chacune.
  
- **Partie 2 : Questions à réponse courte** (30 points)
  - 5 questions à 6 points chacune.
  
- **Partie 3 : Problème pratique 1** (20 points)
  - Sous-questions avec des points attribués en fonction des calculs et explications.
  
- **Partie 4 : Problème pratique 2** (30 points)
  - Mises à jour de Q-table et raisonnement détaillé.








<br/>
<br/>

# **Partie 1 : Questions à choix multiples (20 points)**



### 1. Qu'est-ce qu'un Processus de Décision Markovien (MDP) ?
   
   a) Un algorithme d'apprentissage supervisé
   
   b) Un modèle mathématique pour la prise de décision séquentielle
   
   c) Une technique de clustering
   
   d) Un type de réseau neuronal

### 2. La propriété de Markov stipule que :
   
   a) L'état futur dépend uniquement de l'état présent
   
   b) L'état futur dépend de tous les états passés
   
   c) L'état futur est complètement aléatoire
   
   d) L'état futur dépend uniquement de l'action présente
   

### 3. Quelle est la différence entre l'exploration et l'exploitation en apprentissage par renforcement ?
   
   a) L'exploration cherche de nouvelles actions, l'exploitation utilise les meilleures actions connues
   
   b) L'exploration est utilisée en apprentissage supervisé, l'exploitation en apprentissage non supervisé
   
   c) L'exploration est déterministe, l'exploitation est stochastique
   
   d) Il n'y a pas de différence, ce sont des synonymes
   

### 4. Qu'est-ce que le "discounting" en apprentissage par renforcement ?
   
   a) Une technique pour réduire la taille du modèle
   
   b) Un moyen de donner moins d'importance aux récompenses futures
   
   c) Une méthode pour accélérer l'apprentissage
   
   d) Un type de fonction d'activation

### 5. Quelle est la différence entre la valeur d'état et la valeur Q-state ?
    
   a) La valeur d'état considère toutes les actions possibles, la valeur Q-state une action spécifique
   
   b) La valeur d'état est toujours plus grande que la valeur Q-state
   
   c) La valeur d'état est utilisée pour les environnements déterministes, la valeur Q-state pour les stochastiques
   
   d) Il n'y a pas de différence, ce sont des synonymes



<br/>
<br/>

# **Partie 2 : Questions à réponse courte (30 points)**



#### 6. Expliquez la différence entre un environnement dynamique et un environnement statique en apprentissage par renforcement.
   

#### 7. Décrivez l'approche ε-greedy en apprentissage par renforcement. Pourquoi est-elle utilisée ?
   

#### 8. Qu'est-ce qu'un état absorbant dans un MDP ? Donnez un exemple.
    

#### 9. Expliquez la différence entre une stratégie (policy) et une stratégie optimale en apprentissage par renforcement.
    

#### 10. Décrivez brièvement l'algorithme d'itération de valeur (value iteration). Quel est son objectif principal ?
    


<br/>
<br/>

# **Partie 3 : Problème pratique 1 (20 points)**




###  11. Considérez le MDP suivant représentant un petit labyrinthe :

```
   +---+---+---+
   | S | 0 | 0 |
   +---+---+---+
   |-1 |-1 | 0 |
   +---+---+---+
   |-1 |-1 | G |
   +---+---+---+
```

S est l'état initial, G est l'état but (récompense +10), les cases marquées -1 sont des pièges (récompense -1), et les 0 sont des cases neutres. L'agent peut se déplacer dans les 4 directions (haut, bas, gauche, droite) et reste sur place s'il tente de sortir de la grille. Le facteur de discount γ est de 0.9.

###   a) Écrivez la fonction de récompense r(s,a,s') pour ce MDP. 

###   b) Calculez la valeur optimale V*(s) pour l'état initial S en utilisant l'équation de Bellman. Montrez vos calculs. 

###   c) Quelle est la stratégie optimale pour ce MDP ? Justifiez votre réponse. 

###   d) Comment ce problème changerait-il si l'environnement était stochastique, avec une probabilité de 0.2 que l'agent glisse et se déplace dans une direction aléatoire différente de celle choisie ? 




<br/>
<br/>

# **Partie 4 : Problème pratique 2 (30 points)**



## Contexte
Dans cet exercice, vous allez utiliser les concepts de **Q-learning** pour mettre à jour une Q-table en fonction des décisions prises par un agent évoluant dans un environnement de grille (Grid World). L'agent devra apprendre une **politique cible** en explorant cet environnement.

## Objectifs
1. Analyser une **Q-table**.
2. Comprendre l'environnement **Grid World** et les déplacements possibles.
3. Mettre à jour une valeur de la Q-table.


<br/>


## Partie 4-1 : Mise à jour de la Q-table après un déplacement initial

### Étape 1 : Q-table initiale

Voici la **Q-table** initiale, qui contient les valeurs des actions possibles dans différents états. Chaque ligne représente un état, et chaque colonne représente une action (gauche, droite, haut, bas).

```
+----+--------+--------+------+-------+
| Q  | gauche | droite |  haut | bas  |
+----+--------+--------+------+-------+
| S1 |  -0.5  |   1    |  2.1 |  1.3  |
+----+--------+--------+------+-------+
| S2 |   0.5  |  0.75  | -0.5 |  1.5  |
+----+--------+--------+------+-------+
| S3 |  -1.2  |   1.2  |  0.7 |  1.7  |
+----+--------+--------+------+-------+
```


<br/>


### Étape 2 : Environnement Grid World

L'environnement dans lequel l'agent évolue est une grille (Grid World). Chaque cellule de la grille contient une récompense. Les états terminaux ont des récompenses spéciales, comme indiqué ci-dessous :

```
+----+----+----+
| -1 | -1 | -1 |
+----+----+----+
| -1 | -1 | -1 |
+----+----+----+
| -1 | -10| +10|
+----+----+----+
```

- **Récompenses** : Toutes les actions entraînent une récompense de **-1**, sauf lorsqu'un état terminal est atteint. Les récompenses dans les états terminaux sont **-10** et **+10** respectivement.


<br/>

### Étape 3 : Déplacement de l'agent

L'agent, représenté par un robot **(🤖)**, commence dans l'état **S1**, en haut à gauche de la grille :

```
+------+----+----+
| 🤖 S1 | -1 | -1 |
+------+----+----+
| -1   | -1 | -1 |
+------+----+----+
| -1   | -10| +10|
+------+----+----+
```


<br/>


### Étape 4 : Prise de décision

L'agent prend une décision basée sur une **politique de comportement**. Depuis l'état **S1**, l'agent peut se déplacer **vers la droite** ou **vers le bas** :

```
+---------+----+----+----+
| 🤖 S1 → | -1 | -1 | -1 |
+---↓-----+----+----+----+
|   -1    | -1 | -1 | -1 |
+---------+----+----+----+
|   -1    | -10| +10| -1 |
+---------+----+----+----+
```


<br/>


### Étape 5 : Action choisie

L'agent choisit de se déplacer **vers la droite**, atteignant ainsi l'état **S2** :

```
+------+----+----+
| 🤖 S1|→ -1 (S2) | -1 | 
+------+----+----+
| -1   | -1 | -1 | 
+------+----+----+
| -1   | -10| +10| 
+------+----+----+
```


<br/>


### Étape 6 : Mise à jour de la Q-table

**Question :** En utilisant vos connaissances du Q-learning (référez-vous à vos notes de cours), mettez à jour la valeur de **Q(S1, droite)**, initialement à **1**, dans la Q-table ci-dessous.

- **Alpha** (taux d'apprentissage) : 0.1
- **discount γ** : 0.1
- **Récompenses** : Toutes les récompenses sont de **-1**, sauf pour les états terminaux où les récompenses sont **-10** et **+10**.
- **Bruit** : Aucun bruit.

```
+----+--------+--------+------+-------+
| Q  | gauche | droite |  haut | bas  |
+----+--------+--------+------+-------+
| S1 |  -0.5  |   ?    |  2.1 |  1.3  |
+----+--------+--------+------+-------+
| S2 |   0.5  |  0.75  | -0.5 |  1.5  |
+----+--------+--------+------+-------+
| S3 |  -1.2  |   1.2  |  0.7 |  1.7  |
+----+--------+--------+------+-------+
```


<br/>


### Instructions :
- Calculez la nouvelle valeur de **Q(S1, droite)** en appliquant la mise à jour de la Q-table.
- Indiquez les étapes de votre raisonnement, et montrez comment vous avez utilisé les récompenses et le taux d'apprentissage pour ajuster cette valeur.


<br/>

## Partie 4-2 : Déplacement supplémentaire et mise à jour de la Q-table

### Étape 1 : Déplacement supplémentaire de l'agent

Après avoir mis à jour la valeur de **Q(S1, droite)**, l'agent continue à se déplacer. Cette fois-ci, depuis l'état **S2**, l'agent choisit de se déplacer **vers la droite**, atteignant ainsi l'état **S3**.

```
+----+----+----+----+
| -1 | 🤖 S2 → | S3 -1 |
+----+----+----+----+
| -1 | -1 | -1 | -1 |
+----+----+----+----+
| -1 | -10 | +10| -1 |
+----+----+----+----+
```

### Étape 2 : Mise à jour de la Q-table pour S2

**Question :** Mettez à jour la valeur de **Q(S2, droite)** en appliquant à nouveau vos connaissances du Q-learning. Référez-vous à vos notes de cours pour effectuer cette mise à jour.

- **Alpha** (taux d'apprentissage) : 0.1
- **discount γ** : 0.1
- **Récompenses** : Toutes les récompenses sont de **-1**, sauf pour les états terminaux où les récompenses sont **-10** et **+10**.
- **Bruit** : Aucun bruit.

Voici la Q-table à compléter :

```
+----+--------+--------+------+-------+
| Q  | gauche | droite |  haut | bas  |
+----+--------+--------+------+-------+
| S1 |  -0.5  |   ?    |  2.1 |  1.3  |
+----+--------+--------+------+-------+
| S2 |   0.5  |   ?    | -0.5 |  1.5  |
+----+--------+--------+------+-------+
| S3 |  -1.2  |   1.2  |  0.7 |  1.7  |
+----+--------+--------+------+-------+
```

---

### Instructions :
- Calculez la nouvelle valeur de **Q(S2, droite)** en appliquant la mise à jour de la Q-table.
- Expliquez les étapes de votre raisonnement et montrez comment vous avez utilisé les récompenses et le taux d'apprentissage pour ajuster cette valeur.



<br/>


## Partie 4-3 : Réévaluer dans un environnement stochastique

Dans cette partie, vous allez réévaluer les résultats des **Parties 1 et 2**, mais cette fois-ci dans un **environnement stochastique**.

### Question

Comment ce problème changerait-il si l'environnement était **stochastique**, avec une probabilité de **0.2** que l'agent glisse et se déplace dans une direction aléatoire différente de celle choisie ?



### Instructions :
- Reprenez les **Parties 1 et 2** en tenant compte du fait que l'agent peut glisser dans une direction aléatoire avec une probabilité de 0.2.
- Calculez à nouveau les mises à jour des valeurs de **Q(S1, droite)** et **Q(S2, droite)** en prenant en compte cet environnement stochastique.
- Expliquez comment cela affecte votre raisonnement et les valeurs mises à jour dans la Q-table.





