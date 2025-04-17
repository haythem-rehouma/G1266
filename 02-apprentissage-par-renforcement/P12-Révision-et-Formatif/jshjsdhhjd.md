

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



# **5. Quelle est la différence entre la valeur d'état et la valeur Q-state ?**

**Bonne réponse : a) La valeur d'état considère toutes les actions possibles, la valeur Q-state une action spécifique**

#### ❖ Justification :
- La **valeur d’un état** (V(s)) est la **valeur attendue** de l'état si l’agent suit une certaine politique.
- La **valeur Q (Q(s, a))** est la **valeur attendue d’un couple (état, action)**.

On a généralement :
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















