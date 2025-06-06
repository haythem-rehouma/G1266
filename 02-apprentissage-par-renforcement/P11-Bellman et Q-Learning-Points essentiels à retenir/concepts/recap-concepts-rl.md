## **Révision Complète : Concepts Fondamentaux en Apprentissage par Renforcement**



# **1. Processus de Décision Markovien (MDP)**

Un **MDP (Markov Decision Process)** est un cadre mathématique formel pour la prise de décision dans des environnements où les résultats sont partiellement aléatoires et partiellement sous le contrôle de l’agent.

#### Composants d’un MDP :
- **S** : Ensemble des **états** possibles.
- **A** : Ensemble des **actions** disponibles.
- **R(s, a)** : **Récompense** reçue après avoir effectué l’action `a` dans l’état `s`.
- **P(s’ | s, a)** : **Probabilité de transition** vers l’état `s’` après avoir exécuté l’action `a` depuis `s`.
- **γ (gamma)** : **Facteur d’actualisation** (*discount*) ∈ [0,1], qui pondère l’importance des récompenses futures.

#### Propriété de Markov :
L’évolution du système ne dépend **que** de l’état courant, **et non de l’historique complet**.



# **2. État, Action, Récompense, Utilité**

- **État (State)** : Description complète d'une situation.
- **Action** : Décision ou mouvement possible depuis un état.
- **Récompense (Reward)** : Valeur numérique indiquant la qualité d'une action.
- **Utilité (U)** : Somme actualisée des récompenses futures
  
  $$ U = r_0 + \gamma r_1 + \gamma^2 r_2 + \dots + \gamma^n r_n $$
  
- **Utilité optimale (U*)** : Meilleure utilité possible qu’un agent peut atteindre à partir d’un état donné.



# **3. Politique et stratégie**

- **Policy π(s)** : Fonction qui assigne une action à chaque état.
- **Policy optimale π*** : Politique qui maximise la somme des récompenses attendues à long terme.
- **Behaviour policy** : Politique utilisée **pendant l’apprentissage**, souvent exploratoire.
- **Target policy** : Politique **visée** ou à apprendre, souvent optimale.



# **4. Q-State et fonctions de valeur**

- **Q(s, a)** : Valeur estimée de l’action `a` dans l’état `s`.  
- **V(s)** : Valeur de l’état `s` sous une politique donnée V(s)
  
$$ V(s) = \max_a Q(s,a) $$

- **Différence** :
  - V(s) : évalue un **état**.
  - Q(s, a) : évalue un **état-action**.



# **5. États absorbants, Épisodes**

- **État absorbant** : État terminal, sans actions possibles (ex. : état de victoire ou défaite).
- **Épisode** : Séquence complète allant d’un état initial à un état terminal.


### **6. Types d’environnement**

- **Déterministe** : Une action entraîne toujours le même état suivant.
- **Stochastique** : Les transitions dépendent de probabilités.
- **Statique** : L’environnement ne change pas pendant que l’agent agit.
- **Dynamique** : L’environnement peut évoluer indépendamment de l’agent.



# **7. Exploration vs Exploitation**

- **Exploitation** : Suivre la meilleure action connue à ce jour.
- **Exploration** : Essayer de nouvelles actions pour découvrir de meilleures options.
- **ε-greedy** : Stratégie où, avec une probabilité ε, l’agent explore ; sinon, il exploite la meilleure action.



# **8. Méthodes d’apprentissage**

- **Apprentissage en ligne (Online)** : L’agent apprend en interagissant directement avec l’environnement.
- **Apprentissage hors-ligne (Offline)** : L’apprentissage se fait à partir de données historiques.



# **9. Algorithmes**

- **Value-based** : Approchent la politique optimale via une fonction de valeur (ex. : Q-learning).
- **Policy-based** : Apprennent directement la politique sans passer par la fonction de valeur.

#### Algorithmes classiques :
- **Itération de la valeur** : Mise à jour successive de `V(s)` jusqu’à convergence.
- **Q-learning** : Apprentissage hors-modèle de la Q-table, mise à jour selon  l'équation suivante
  
  
$$ Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)] $$



Voici la **variante de la mise à jour de Q-learning** utilisant le facteur \( (1 - \alpha) \), très utile pour les explications pédagogiques :



### **Forme équivalente avec $$1 - \alpha$$** 

$$
Q(s,a) \leftarrow (1 - \alpha) \cdot Q(s,a) + \alpha \cdot \left[ r + \gamma \cdot \max_{a'} Q(s', a') \right]
$$




  
- **Équation de Bellman** : Formule de base pour la mise à jour des valeurs dans un MDP.



# **10. Exemples explicatifs**

#### Exemple 1 : Interprétation intuitive
```text
État : j’ai mal à la tête
Actions :
- a1 : aller dormir → Q(s,a1) = 0.89
- a2 : prendre Advil → Q(s,a2) = 0.7
- a3 : faire du yoga → Q(s,a3) = 0.4
- a4 : continuer à travailler → Q(s,a4) = -0.5

Valeur de l’état s : V(s) = max Q(s,a) = 0.89
Politique optimale : π(s) = a1
```

#### Exemple 2 : Grille (état = (3,1))
```text
Actions possibles : haut, bas, gauche, droite
Q((3,1), haut) = 0.59  
Q((3,1), bas) = 0.53  
Q((3,1), droite) = 0.64  
Q((3,1), gauche) = 0.57

→ Valeur de l’état (3,1) = 0.64 (meilleure action = droite)
```



# **Allez plus loin**

Voici quelques points qu'on peut également inclure selon le niveau visé :
- **SARSA** (on-policy learning)
- **Modèle de l’environnement vs approche sans modèle (model-free)**
- **Tableau vs Réseaux de neurones (Q-table vs Deep Q-learning)**
- **Critique d’une politique (Policy Evaluation)**
- **Amélioration de politique (Policy Improvement)**

<br/>

# Tableau des concepts pour l’examen de mi-session**

| **Catégorie**                        | **Concept / Élément à revoir**                             | **Définition ou exemple** |
|-------------------------------------|------------------------------------------------------------|---------------------------|
| **Fondamentaux MDP**               | MDP (Markov Decision Process)                              | Modèle mathématique pour décrire la prise de décision séquentielle dans un environnement incertain. |
|                                     | Propriété de Markov                                        | L'état futur dépend uniquement de l'état actuel, pas de l’historique complet. |
|                                     | Environnement                                              | Le monde dans lequel évolue l’agent, avec ses règles, états et récompenses. |
|                                     | État                                                       | Une situation ou configuration à un moment donné (ex: position d’un robot). |
|                                     | Action                                                     | Une décision ou un mouvement effectué par l’agent à partir d’un état. |
|                                     | Reward (Récompense)                                        | Retour numérique obtenu après une action (ex: +10 pour un bon choix). |
|                                     | Utilité                                                    | Valeur totale attendue qu’un agent peut accumuler à partir d’un état. |
|                                     | Utilité optimale                                           | Utilité maximale possible, en suivant la meilleure stratégie. |
|                                     | Stratégie                                                  | Plan qui indique quelle action prendre dans chaque état. |
|                                     | Stratégie optimale                                         | Stratégie qui maximise les récompenses à long terme. |
|                                     | Discounting                                                | Réduction de l’importance des récompenses futures, avec un facteur γ. |
|                                     | État absorbant                                             | État final duquel on ne sort plus (ex: sortie du labyrinthe). |
|                                     | Épisode                                                    | Suite d'étapes (état → action → état...) qui se termine dans un état absorbant. |
| **Comparaisons**                    | Processus déterministe vs stochastique                     | Déterministe : même action → même résultat. Stochastique : action → résultats variables. |
|                                     | Environnement dynamique vs statique                        | Dynamique : change pendant l’apprentissage. Statique : ne change pas. |
| **Apprentissage par Renforcement** | Exploration vs exploitation                                | Explorer : essayer de nouvelles actions. Exploiter : choisir la meilleure connue. |
|                                     | Stratégie ε-greedy                                         | Avec probabilité ε, on explore ; sinon on exploite la meilleure action. |
|                                     | Valeur d'état vs valeur Q-state                            | Valeur d’état : utilité d’un état. Q-state : utilité d’une paire (état, action). |
|                                     | Calcul de la valeur d’un état                              | Moyenne pondérée des valeurs futures attendues. |
|                                     | Calcul de la valeur Q-state                                | Basée sur la récompense immédiate + valeur future estimée via Bellman. |
|                                     | Itération                                                  | Répétition du calcul des valeurs jusqu’à convergence. |
|                                     | Algorithme d’itération de valeur                           | Méthode pour calculer la meilleure stratégie en mettant à jour les valeurs d’état. |
| **Application / Exercices vus**     | Mise à jour de la Q-table avec équations de Bellman        | On actualise les Q-valeurs à chaque expérience : Q ← Q + α (TD). |
|                                     | Quiz sur la Q-table (correction envoyée précédemment)      | Vérification de la compréhension de la mise à jour de Q-table. |

