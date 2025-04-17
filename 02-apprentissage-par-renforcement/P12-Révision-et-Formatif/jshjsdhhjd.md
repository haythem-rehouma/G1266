

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

#### ✗ Mauvaises réponses :
- **b)** Faux : aucune règle n’affirme que V(s) > Q(s,a).
- **c)** Faux : les deux valeurs sont utilisées dans **tous types d’environnements**, déterministes ou stochastiques.
- **d)** Ce ne sont **pas des synonymes**.

