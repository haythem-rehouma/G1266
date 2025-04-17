
--------------------
# Partie 1
--------------------

<br/>

# **1. Qu'est-ce qu'un Processus de Décision Markovien (MDP) ?**

**Bonne réponse : b) Un modèle mathématique pour la prise de décision séquentielle**

#### ❖ Justification :
Un **MDP (Markov Decision Process)** est un **cadre mathématique** utilisé pour modéliser les situations où un **agent** prend des décisions dans un environnement avec incertitude. Il comprend :
- un **ensemble d'états**,
- un **ensemble d'actions** disponibles à chaque état,
- une **fonction de transition** (décrit les probabilités de passer d’un état à un autre),
- une **fonction de récompense** (récompense reçue après avoir effectué une action),
- et parfois un **facteur de discount**.

L’objectif est de **maximiser la récompense cumulée à long terme**, ce qui en fait un outil **central en apprentissage par renforcement**.

#### ❖ Vulgarisation + exemple :
Un MDP est une façon de **modéliser un problème où un agent prend des décisions pas à pas**.  
Chaque fois qu’il prend une décision (**action**), il passe d’un **état** à un autre et reçoit une **récompense**.

**Exemple :**  
- État 1 : je suis au carrefour.  
- Action : je tourne à gauche.  
- État 2 : j'arrive à la boulangerie.  
- Récompense : +5 (car j’ai trouvé du pain !)

Un MDP nous aide à **calculer quelles actions maximisent les récompenses à long terme**.




#### ✗ Mauvaises réponses :
- **a)** L’apprentissage supervisé nécessite des paires (entrée, sortie) — un MDP ne suit pas ce principe.
- **c)** Le clustering est une tâche d’apprentissage non supervisé.
- **d)** Un réseau neuronal est une structure d’apprentissage, **pas un modèle de décision séquentielle**.


<br/>

# **2. La propriété de Markov stipule que :**

**Bonne réponse : a) L'état futur dépend uniquement de l'état présent**

#### ❖ Justification :
La **propriété de Markov** (ou hypothèse de Markov) dit que le **futur est indépendant du passé**, à condition que l’on connaisse le **présent**.  
Formellement, dans un MDP :
$${\Pr}(S_{t+1} \mid S_t, S_{t-1}, ..., S_0) = {\Pr}(S_{t+1} \mid S_t)$$  
Cette propriété permet d’appliquer efficacement les équations de Bellman, qui supposent que **toutes les informations pertinentes pour l’avenir sont contenues dans l’état actuel**.



#### ❖ Vulgarisation + exemple :
Cela veut dire que **pour prédire ce qui va se passer ensuite, on a juste besoin de savoir où on est maintenant**, pas toute l’histoire du passé.

**Exemple :**  
- Si je suis dans l’état 1 (carrefour), peu importe comment je suis arrivé là.  
- L’action que je fais **depuis cet état** détermine ce qui va arriver ensuite.  
- Je n’ai pas besoin de savoir si j’ai pris le métro ou le vélo avant.

C’est très pratique car ça simplifie les calculs !


#### ✗ Mauvaises réponses :
- **b)** Faux : ce serait un processus non markovien.
- **c)** Faux : l’évolution n’est **pas purement aléatoire**, elle dépend de l’état courant.
- **d)** Faux : la transition dépend de l’état **et** de l’action, pas juste de l’action.


<br/>

# **3. Quelle est la différence entre l'exploration et l'exploitation en apprentissage par renforcement ?**

**Bonne réponse : a) L'exploration cherche de nouvelles actions, l'exploitation utilise les meilleures actions connues**

#### ❖ Justification :
C’est l’un des **grands dilemmes** de l’apprentissage par renforcement :
- **Exploitation** : utiliser les connaissances actuelles pour choisir la meilleure action connue.
- **Exploration** : essayer des actions nouvelles ou moins fréquentes, dans l’espoir de trouver une meilleure stratégie à long terme.

Par exemple, un agent peut **exploiter** une stratégie efficace, mais il peut manquer des actions encore **plus rentables** s’il **n’explore pas**.

L’approche **ε-greedy** est un moyen courant de gérer ce compromis.


#### ❖ Vulgarisation + exemple :
- **Exploitation** : l’agent fait ce qu’il **connaît déjà comme efficace**.  
- **Exploration** : il essaie des choses **nouvelles, même risquées**, pour apprendre plus.

**Exemple :**  
- Je connais une pizzeria qui me donne +7 points de bonheur.  
- Mais je vois un nouveau restaurant. Si je vais le tester, c’est **exploration** (peut-être +10 ? ou -5...).  
- Si je retourne à la pizzeria, c’est **exploitation**.




#### ✗ Mauvaises réponses :
- **b)** Confusion entre types d’apprentissage — exploration et exploitation sont des concepts **propres au RL**.
- **c)** Le caractère stochastique ou déterministe n’a pas de lien direct avec ce dilemme.
- **d)** Ce ne sont **pas des synonymes**, au contraire !


<br/>

# **4. Qu'est-ce que le "discounting" en apprentissage par renforcement ?**

**Bonne réponse : b) Un moyen de donner moins d'importance aux récompenses futures**

#### ❖ Justification :
Le **discounting** consiste à appliquer un **facteur de réduction (γ ∈ [0,1])** aux récompenses futures :
$${\text{Return}} = r_0 + \gamma r_1 + \gamma^2 r_2 + \dots$$  
- Si **γ est proche de 1**, l’agent **valorise** les récompenses futures.
- Si **γ est petit**, il **privilégie le court terme**.

Cela reflète des situations réelles où une récompense immédiate est préférée à une récompense incertaine ou lointaine.



#### ❖ Vulgarisation + exemple :
En apprentissage par renforcement, **on préfère souvent une récompense immédiate** à une récompense plus tard.

On utilise un **facteur gamma (γ)** entre 0 et 1 :  
- Si γ = 1 → on valorise autant le futur que le présent  
- Si γ = 0.5 → chaque pas dans le futur compte moitié moins  
- Si γ = 0 → on ignore totalement le futur

**Exemple :**  
- Si je reçois 10 aujourd’hui, c’est mieux que 10 dans 3 jours.  
- Donc on applique un coefficient **pour réduire la valeur des récompenses futures**.


#### ✗ Mauvaises réponses :
- **a)** Rien à voir avec la taille du modèle.
- **c)** Cela **n’accélère pas** directement l’apprentissage, mais change la priorité temporelle.
- **d)** Ce n’est pas une fonction d’activation.

<br/>


# **5. Quelle est la différence entre la valeur d'état et la valeur Q-state ?**

**Bonne réponse : a) La valeur d'état considère toutes les actions possibles, la valeur Q-state une action spécifique**

#### ❖ Justification :
- La **valeur d’un état** (V(s)) est la **valeur attendue** de l'état si l’agent suit une certaine politique.
- La **valeur Q (Q(s, a))** est la **valeur attendue d’un couple (état, action)**.

On a généralement 

$$ V(s) = \max_a Q(s, a) $$  

C’est-à-dire que la valeur d’un état est liée à la **meilleure action possible** depuis cet état.


#### ❖ Vulgarisation + exemple :
- **V(s)** = valeur globale d’un **état** = meilleure récompense possible à partir de là  
- **Q(s, a)** = valeur de **faire une action a à partir de l’état s**

**Exemple :**  
- État 1 : je suis devant un croisement  
- Action 1 : aller à gauche → Q(s, a1) = +5  
- Action 2 : aller à droite → Q(s, a2) = +3  
- Donc V(s) = max(Q(s, a)) = +5

La **valeur d’état** est donc **calculée à partir des Q-valeurs**.


#### ✗ Mauvaises réponses :
- **b)** Faux : aucune règle n’affirme que V(s) > Q(s,a).
- **c)** Faux : les deux valeurs sont utilisées dans **tous types d’environnements**, déterministes ou stochastiques.
- **d)** Ce ne sont **pas des synonymes**.






<br/>
<br/>
<br/>

--------------------  
# Partie 2 – Réponses courtes (30 points)  
--------------------

<br/>

# **6. Quelle est la différence entre un environnement dynamique et un environnement statique ?**

**Bonne réponse :**  
Un **environnement statique** ne change **que si l’agent agit**.  
Un **environnement dynamique** peut évoluer **indépendamment des actions de l’agent**.



### ❖ Justification :
- Dans un environnement **statique**, si l’agent ne fait rien, rien ne change.  
- Dans un environnement **dynamique**, **des événements externes peuvent modifier l’état du monde**, même si l’agent reste inactif.

### ❖ Vulgarisation + exemple :

**Exemple d’environnement statique :**  
- Un robot dans un labyrinthe où les murs ne bougent pas.  
  - État 1 : robot au point (0,0)  
  - Action : aller à droite  
  - État 2 : robot au point (1,0)  
  - Si le robot ne bouge pas, le labyrinthe reste identique.

**Exemple d’environnement dynamique :**  
- Un robot dans un entrepôt où **des humains déplacent des objets**.  
  - Même sans action du robot, l’état change : un obstacle peut apparaître.  
  - L’agent doit s’adapter en temps réel.



<br/>

# **7. Décrivez l’approche ε-greedy et pourquoi elle est utilisée.**

**Bonne réponse :**  
L’approche **ε-greedy** permet de mélanger **exploration** (tester de nouvelles actions) et **exploitation** (choisir les meilleures actions connues).



### ❖ Justification :
- À chaque décision :
  - Avec probabilité **ε** (par exemple 10%), l’agent **choisit une action aléatoire** → exploration.
  - Avec probabilité **1−ε**, il **prend la meilleure action actuelle** → exploitation.

Cela permet d’**éviter de rester bloqué dans une stratégie sous-optimale**, et d’apprendre de nouvelles informations sur l’environnement.



### ❖ Vulgarisation + exemple :

**Exemple :**  
- L’agent est dans l’état A.  
- Il a déjà appris que **aller à gauche** donne une récompense de +6.  
- Il pourrait toujours exploiter cela… mais peut-être que **aller à droite** donne +10 !

Avec ε = 0.1, il explore 1 fois sur 10 pour ne pas rater une meilleure solution.



<br/>

# **8. Qu’est-ce qu’un état absorbant dans un MDP ?**

**Bonne réponse :**  
Un **état absorbant** est un état **terminal**, où l’agent **reste bloqué pour toujours** une fois qu’il y entre.  



### ❖ Justification :
- Dans un état absorbant, **peu importe l’action choisie**, l’agent **reste dans cet état**.  
- Ce sont généralement des états **de fin d’épisode** (victoire, échec, arrêt…).



### ❖ Vulgarisation + exemple :

**Exemple :**  
- État G = état "arrivée" dans un labyrinthe → Récompense : +10  
- Une fois que le robot atteint G, il **ne peut plus sortir**.  
  - Actions possibles : gauche, droite, bas, haut  
  - Résultat : G à chaque fois → **l’agent y est absorbé**.

**Autres exemples :**  
- État "Game Over" dans un jeu  
- État "Succès de mission" dans un drone autonome



<br/>

# **9. Quelle est la différence entre une stratégie (policy) et une stratégie optimale ?**

**Bonne réponse :**  
- Une **stratégie (ou policy)** est une règle qui **dit à l’agent quelle action prendre dans chaque état**.  
- Une **stratégie optimale** est celle qui **maximise la récompense cumulée attendue**.



### ❖ Justification :
- Toutes les stratégies ne se valent pas : certaines mènent à de meilleurs résultats.  
- La stratégie optimale **π\*** est celle qui **donne les meilleures décisions dans chaque état**, pour maximiser les gains à long terme.



### ❖ Vulgarisation + exemple :

**Exemple :**  
- État A : l’agent peut aller à gauche (+2) ou à droite (+5)

**Stratégie A :** toujours aller à gauche → gain = +2  
**Stratégie B :** aller à droite → gain = +5

→ La **stratégie B est optimale** pour cet état.

Mais attention : sur le long terme, ce n’est pas juste la récompense immédiate qui compte, c’est **la récompense cumulée avec les transitions futures**.



<br/>

# **10. Décrivez brièvement l’algorithme d’itération de valeur (value iteration).**

**Bonne réponse :**  
L’algorithme d’**itération de valeur** calcule la **valeur de chaque état V(s)** en utilisant l’**équation de Bellman**, pour en déduire une **stratégie optimale**.



### ❖ Justification :
- À chaque itération, on met à jour V(s) selon :
  $${V(s) = \max_a \sum_{s'} P(s'|s,a) \left[r(s,a,s') + \gamma V(s')\right]}$$  
- Cela permet d’évaluer **la meilleure action dans chaque état**, en tenant compte des **récompenses et transitions futures**.



### ❖ Vulgarisation + exemple :

**Étapes :**
1. On donne une valeur initiale à chaque état (ex : 0)
2. À chaque étape, on regarde **les actions possibles** depuis chaque état
3. On choisit **celle qui maximise** la somme : récompense immédiate + valeur des états suivants (avec discount)
4. On **répète jusqu’à convergence** (les valeurs ne changent plus)

**Exemple :**
- État A → 2 choix :  
  - Action gauche → état B avec +2  
  - Action droite → état C avec +5 mais plus risqué

L’algorithme évalue **quelle suite d’actions donnera le meilleur total de récompenses**.








