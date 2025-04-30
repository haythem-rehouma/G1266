# Introduction

Avant de plonger dans les équations, il est essentiel de comprendre **pourquoi** nous avons besoin des méthodes TD(0), TD(1), TD(2) et Q-Learning.

Imaginez un agent (comme un robot, un joueur, ou un programme) qui doit apprendre à prendre de bonnes décisions dans un environnement où il ne connaît pas les règles. Il doit apprendre **à partir de ses propres expériences**.  
C’est là que les méthodes dites **TD(n)** (pour "Temporal Difference Learning") entrent en jeu.

---

## Comprendre les méthodes TD(n)

Les méthodes TD sont des techniques d’apprentissage qui permettent à un agent de **mettre à jour ce qu’il pense d’un état**, en utilisant les récompenses qu’il reçoit après avoir pris une action.

Le chiffre dans TD(0), TD(1), TD(2) correspond au nombre d’étapes dans le futur que l’agent regarde pour corriger sa prédiction.

---

## Tableau comparatif simplifié

| **Méthode**      | **Type**     | **Mise à jour**                                   | **Description simplifiée**                                        | **Avantages**                        | **Inconvénients**                          |
|------------------|--------------|----------------------------------------------------|-------------------------------------------------------------------|--------------------------------------|--------------------------------------------|
| **TD(0)**        | On-policy    | Basée sur l’état suivant immédiat                 | Je regarde la prochaine récompense et j’ajuste                    | Très rapide, facile                   | Vision très courte                         |
| **TD(1)**        | N-step       | Inclut une récompense future                      | Je regarde un peu plus loin pour mieux juger                      | Plus précis que TD(0)                | Plus lent, plus de mémoire                 |
| **TD(2)**        | N-step       | Plusieurs récompenses successives                 | J’attends deux étapes avant d’apprendre                           | Bon compromis                        | Demande plus d’espace mémoire              |
| **Q-Learning**   | Off-policy   | Basée sur état-action et meilleure action future  | J’apprends ce que j’aurais dû faire pour mieux réussir            | Optimise à long terme                | Complexité et coût mémoire plus élevés     |

---

## Explication des colonnes

1. **Méthode** : Le nom de la méthode.
2. **Type** :
   - On-policy : l’agent apprend en suivant ce qu’il fait.
   - Off-policy : il apprend à partir d’autres stratégies (meilleures) qu’il pourrait suivre.
3. **Mise à jour** : Ce que l’agent utilise comme information pour ajuster ce qu’il croit.
4. **Description simplifiée** : Une façon intuitive de comprendre la logique.
5. **Avantages** : Pourquoi cette méthode est utile.
6. **Inconvénients** : Limites ou difficultés à utiliser cette méthode.

---

## Conclusion rapide

Les méthodes TD sont utiles pour apprendre **au fil du temps**, sans avoir besoin d’attendre la fin d’un épisode.  
Q-Learning est particulièrement puissant car il apprend à **trouver la meilleure stratégie possible**, même si l’agent ne l’utilise pas encore.  
Ces approches sont essentielles pour tout système qui doit apprendre seul à long terme, dans un environnement complexe ou inconnu.
