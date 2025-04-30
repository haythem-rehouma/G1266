# Variantes des équations Bellman , TD-Learning et Q-Learning

## Introduction

Le TD-Learning (Temporal Difference Learning) et le Q-Learning sont des méthodes d'apprentissage par renforcement utilisées pour apprendre à partir d'expériences sans avoir besoin d'un modèle complet de l'environnement.

## Équation de Bellman

L'équation de Bellman exprime la valeur d’un état comme la récompense immédiate attendue plus la valeur actualisée des futurs états, selon une politique $\pi$. Elle constitue la base théorique du TD-Learning et du Q-Learning.

**Équation de Bellman (valeur d’un état sous politique $\pi$) :**

$$
V^\pi(s) = \mathbb{E}_\pi \left[ R_{t+1} + \gamma \cdot V^\pi(S_{t+1}) \mid S_t = s \right]
$$

**Équation de Bellman (valeur d'une paire état-action sous politique $\pi$) :**

$$
Q^\pi(s, a) = \mathbb{E}_\pi \left[ R_{t+1} + \gamma \cdot Q^\pi(S_{t+1}, A_{t+1}) \mid S_t = s, A_t = a \right]
$$

**Équation de Bellman optimale (état) :**

$$
V^*(s) = \max_a \mathbb{E} \left[ R_{t+1} + \gamma \cdot V^*(S_{t+1}) \mid S_t = s, A_t = a \right]
$$

**Équation de Bellman optimale (état-action) :**

$$
Q^*(s, a) = \mathbb{E} \left[ R_{t+1} + \gamma \cdot \max_{a'} Q^*(S_{t+1}, a') \mid S_t = s, A_t = a \right]
$$

## TD(0)

TD(0) est la forme la plus simple de TD-Learning. Il met à jour la valeur d'un état immédiatement après chaque action.

**Équation de mise à jour TD(0) :**

$$
V(S_t) \leftarrow (1 - \alpha) V(S_t) + \alpha \left[ R_{t+1} + \gamma V(S_{t+1}) \right]
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
V(S_t) \leftarrow (1 - \alpha) V(S_t) + \alpha \left[ \sum_{k=1}^{n} \gamma^{k-1} R_{t+k} + \gamma^n V(S_{t+n}) \right]
$$

## Q-Learning

Q-Learning est une méthode off-policy qui apprend les valeurs des paires état-action.

**Équation de mise à jour Q-Learning :**

$$
Q(S_t, A_t) \leftarrow (1 - \alpha) Q(S_t, A_t) + \alpha \left[ R_{t+1} + \gamma \max_{a} Q(S_{t+1}, a) \right]
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

# Conclusion

Le TD-Learning et le Q-Learning sont des méthodes puissantes pour l'apprentissage par renforcement, permettant aux agents d'apprendre de manière efficace dans des environnements complexes sans modèle complet.
