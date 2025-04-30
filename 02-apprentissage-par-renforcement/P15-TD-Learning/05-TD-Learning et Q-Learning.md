# TD-Learning et Q-Learning

## Introduction

Le TD-Learning (Temporal Difference Learning) et le Q-Learning sont des méthodes d'apprentissage par renforcement utilisées pour apprendre à partir d'expériences sans avoir besoin d'un modèle complet de l'environnement.

## TD(0)

TD(0) est la forme la plus simple de TD-Learning. Il met à jour la valeur d'un état immédiatement après chaque action.

**Équation de mise à jour TD(0) :**

$$
V(S_t) \leftarrow (1 - \alpha) \cdot V(S_t) + \alpha \cdot \left[ R_{t+1} + \gamma \cdot V(S_{t+1}) \right]
$$

Où :
- $V(S_t)$ est la valeur de l'état actuel  
- $\alpha$ est le taux d'apprentissage  
- $R_{t+1}$ est la récompense immédiate  
- $\gamma$ est le facteur d'actualisation  
- $V(S_{t+1})$ est la valeur de l'état suivant

## TD(n)

TD(n) est une généralisation de TD(0) qui prend en compte *n* étapes futures pour la mise à jour.

**Équation de mise à jour TD(n) :**

$$
V(S_t) \leftarrow (1 - \alpha) \cdot V(S_t) + \alpha \cdot \left[ \sum_{k=1}^{n} \gamma^{k-1} \cdot R_{t+k} + \gamma^n \cdot V(S_{t+n}) \right]
$$

## Q-Learning

Q-Learning est une méthode *off-policy* qui apprend les valeurs des paires état-action.

**Équation de mise à jour Q-Learning :**

$$
Q(S_t, A_t) \leftarrow (1 - \alpha) \cdot Q(S_t, A_t) + \alpha \cdot \left[ R_{t+1} + \gamma \cdot \max_{a} Q(S_{t+1}, a) \right]
$$

Où :
- $Q(S_t, A_t)$ est la valeur de la paire état-action actuelle  
- $\max_{a} Q(S_{t+1}, a)$ est la valeur maximale de l'action dans l'état suivant

## Comparaison des méthodes

| Méthode    | Type       | Mise à jour                    | Avantages                               | Inconvénients                       |
|------------|------------|--------------------------------|-----------------------------------------|-------------------------------------|
| TD(0)      | On-policy  | État uniquement                | Simple, rapide                          | Ne considère qu'un seul pas         |
| TD(n)      | N-step     | État et n récompenses futures  | Équilibre entre exploration et précision| Complexité accrue avec n            |
| Q-Learning | Off-policy | Paire état-action              | Trouve une politique optimale           | Nécessite plus d'espace de stockage |

## Conclusion

Le TD-Learning et le Q-Learning sont des méthodes puissantes pour l'apprentissage par renforcement, permettant aux agents d'apprendre de manière efficace dans des environnements complexes sans modèle complet.
