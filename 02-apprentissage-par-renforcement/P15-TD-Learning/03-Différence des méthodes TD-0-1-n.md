

-------------
# Annexe 1 - Pourquoi l'appelle-t-on TD(0) ?
-------------


Le **TD(0)** est appelé ainsi parce qu'il utilise une estimation à un seul pas pour mettre à jour la valeur d'un état. Le "0" indique qu'il ne regarde qu'un seul pas dans le futur (c'est-à-dire, la prochaine récompense et l'état suivant immédiat).

### Différence avec le Q-Learning

- **TD(0)** : Met à jour uniquement la valeur des états.
- **Q-Learning** : Met à jour la valeur des paires état-action, ce qui permet de déterminer directement quelle action est optimale dans chaque état.

-------------
# Annexe 2 - Différence avec l'Équation de Bellman
-------------

- **Équation de Bellman** : Utilisée dans la programmation dynamique, elle calcule les valeurs optimales en utilisant des connaissances complètes de l'environnement (modèle).
- **TD(0)** et **Q-Learning** : N'ont pas besoin de modèle complet. Ils apprennent à partir d'expériences directes et ajustent les valeurs au fur et à mesure.

En résumé, TD(0) et Q-Learning sont des méthodes d'apprentissage par renforcement qui permettent d'apprendre sans connaître entièrement l'environnement, contrairement à l'équation de Bellman utilisée dans des contextes où le modèle est connu.

-------------
# Annexe 3 - Différence des méthodes TD(0), TD(1), TD(2), et Q-Learning :
-------------


```
| Méthode      | Type       | Mise à jour de la valeur                   | Équation                                                                 | Avantages                                           | Inconvénients                         |
|--------------|------------|--------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------|
| TD(0)        | On-policy  | État uniquement                            | V(S_t) ← V(S_t) + α [R_{t+1} + γ V(S_{t+1}) - V(S_t)]                    | Simple, rapide                                      | Ne considère qu’un seul pas           |
| TD(1)        | N-step     | État et prochaines récompenses             | V(S_t) ← V(S_t) + α [Σ R_{t+i} + γ^i V(S_{t+i})]                         | Mieux pour de courtes époques                      | Complexité plus élevée                |
| TD(2)        | N-step     | État et plusieurs récompenses              | V(S_t) ← V(S_t) + α [Σ R_{t+i} + γ^i V(S_{t+i})]                         | Équilibre entre exploration et exploitation         | Peut être lent                        |
| Q-Learning   | Off-policy | Paire état-action                          | Q(S_t, A_t) ← Q(S_t, A_t) + α [R_{t+1} + γ max Q(S_{t+1}, a) - Q(S_t, A_t)] | Efficace pour trouver une politique optimale       | Nécessite un plus grand espace de stockage |
```



## Anenxe 4 - Résumé **TD(0)**  vs **TD(1)** vs **TD(2)** 

- **TD(0)** : Met à jour la valeur d'un état immédiatement après chaque action, en utilisant la récompense immédiate et la valeur de l'état suivant.

- **TD(1)** et **TD(2)** : Utilisent plusieurs étapes futures pour mettre à jour les valeurs, ce qui peut améliorer la précision mais augmente la complexité.

- **Q-Learning** : Apprend les valeurs des paires état-action, permettant de déterminer directement l'action optimale à partir de n'importe quel état. C'est une méthode off-policy, ce qui signifie qu'elle apprend indépendamment de la politique suivie par l'agent.

Chaque méthode a ses propres avantages et inconvénients en fonction du contexte d'application et des besoins spécifiques de l'environnement d'apprentissage.




# Équations pour **TD(0)**, **TD(1)**, **TD(2)**, et ainsi de suite, ainsi que pour **Q-Learning**.

### TD(0) — Mise à jour immédiate après chaque étape

L'algorithme **TD(0)** met à jour la valeur de l'état après chaque transition, en tenant compte de la récompense immédiate et de la valeur estimée de l'état suivant :

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \right]
$$

### TD(1) — Utilisation d'une récompense complète après un épisode

Dans **TD(1)**, on attend une étape supplémentaire, en tenant compte non seulement de la récompense immédiate mais aussi de la récompense après deux étapes :

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma R_{t+2} + \gamma^2 V(S_{t+2}) - V(S_t) \right]
$$

### TD(2) — Deux étapes de transition

Pour **TD(2)**, la mise à jour prend en compte deux étapes supplémentaires, ce qui donne :

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \gamma^3 V(S_{t+3}) - V(S_t) \right]
$$

### TD(n) — Généralisation pour \(n\) étapes

De manière générale, pour **TD(n)**, où nous utilisons \(n\) étapes futures pour la mise à jour, l'équation devient :

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ \sum_{k=1}^{n} \gamma^{k-1} R_{t+k} + \gamma^n V(S_{t+n}) - V(S_t) \right]
$$

Ici, **$$\sum_{k=1}^{n} \gamma^{k-1} R_{t+k}$$** représente la somme pondérée des récompenses jusqu'à **$$n$$** étapes.

### Q-Learning — Apprentissage des paires état-action

Le **Q-Learning** est une extension du TD-Learning qui apprend des paires état-action \( (S, A) \) au lieu de simplement les valeurs d'états. L'équation de mise à jour pour **Q-Learning** est :

$$
Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha \left[ R_{t+1} + \gamma \max_{a} Q(S_{t+1}, a) - Q(S_t, A_t) \right]
$$

- **$$Q(S_t, A_t)$$** : la valeur de la paire état-action **$$(S_t, A_t)$$**.
- **$$\max_{a} Q(S_{t+1}, a)$$** : la meilleure valeur de l'action possible à partir de l'état suivant **$$S_{t+1}$$**.

### Résumé

- **TD(0)** se met à jour immédiatement après une étape.
- **TD(1)** se met à jour en prenant en compte une étape supplémentaire.
- **TD(2)** prend en compte deux étapes.
- **TD(n)** généralise à \(n\) étapes avant de faire une mise à jour.
- **Q-Learning** optimise l'apprentissage pour des paires état-action, cherchant à maximiser la récompense en choisissant l'action optimale à chaque étape.






### TD(0) — Mise à jour immédiate après chaque étape

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \right]
$$

### TD(1) — Utilisation d'une récompense après une étape supplémentaire

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma R_{t+2} + \gamma^2 V(S_{t+2}) - V(S_t) \right]
$$

### TD(2) — Utilisation de deux étapes supplémentaires

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \gamma^3 V(S_{t+3}) - V(S_t) \right]
$$

### TD(n) — Généralisation pour \(n\) étapes

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ \sum_{k=1}^{n} \gamma^{k-1} R_{t+k} + \gamma^n V(S_{t+n}) - V(S_t) \right]
$$






------------------------------
# Annexe 5 - Résumé
------------------------------


### TD(0) — Mise à jour immédiate après chaque étape

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \right]
$$

### TD(1) — Utilisation d'une récompense complète après un épisode

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma R_{t+2} + \gamma^2 V(S_{t+2}) - V(S_t) \right]
$$

### TD(2) — Deux étapes de transition

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \gamma^3 V(S_{t+3}) - V(S_t) \right]
$$

### TD(n) — Généralisation pour $$n$$ étapes

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ \sum_{k=1}^{n} \gamma^{k-1} R_{t+k} + \gamma^n V(S_{t+n}) - V(S_t) \right]
$$

------------------------







# Citations:

[1] https://mpatacchiola.github.io/blog/2017/01/29/dissecting-reinforcement-learning-3.html

[2] https://fr.wikipedia.org/wiki/Temporal_difference_learning

[3] https://www.td.com/ca/fr/investir/placement-en-direct/education

[4] https://www.lancaster.ac.uk/stor-i-student-sites/jordan-j-hood/2021/04/12/reinforcement-learning-temporal-difference-td-learning/

[5] https://towardsdatascience.com/temporal-difference-learning-and-the-importance-of-exploration-an-illustrated-guide-5f9c3371413a?gi=de80dad61959

[6] https://www.csd.uwo.ca/~xling/cs346a/extra/tdgammon.pdf
