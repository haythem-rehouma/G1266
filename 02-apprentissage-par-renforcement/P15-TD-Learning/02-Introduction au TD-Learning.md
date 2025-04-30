# Introduction au TD-Learning

- Le **TD-Learning** est une méthode d'apprentissage par renforcement qui combine des aspects des méthodes de Monte Carlo et de la programmation dynamique. Il permet à un agent d'apprendre en mettant à jour les estimations de la valeur des états ou des paires état-action à chaque étape, sans attendre la fin d'un épisode.

- Le **TD-Learning** (Temporal Difference Learning) est une technique d'apprentissage par renforcement qui aide un agent à prendre de meilleures décisions en apprenant progressivement de ses expériences.

## Simplification

1. *Valeur de l'État* **$$V(S_t)$$** : C'est une estimation de la qualité d'un état donné. Plus la valeur est élevée, plus l'état est considéré comme bon.
2. *Récompense Immédiate* **($R_{t+1}$)** : C'est le retour immédiat reçu après une action. Cela peut être positif (récompense) ou négatif (punition).
3. *Taux d'Apprentissage* **($\alpha$)** : Un nombre entre 0 et 1 qui détermine à quelle vitesse l'agent apprend. Un taux élevé signifie que l'agent s'adapte rapidement aux nouvelles informations.
4. *Facteur de Discount* **($\gamma$)** : Un nombre entre 0 et 1 qui réduit l'importance des récompenses futures. Plus il est proche de 1, plus l'agent valorise les récompenses futures.

## Fonctionnement

- **Mise à Jour Progressive** : Contrairement aux méthodes qui attendent la fin d'un épisode pour apprendre, le TD-Learning met à jour les valeurs après chaque étape.
- **Combinaison d'Approches** : Il utilise des idées des méthodes Monte Carlo (qui apprennent à partir d'expériences complètes) et de la programmation dynamique (qui utilise des estimations actuelles pour améliorer les décisions futures).
  
## Pourquoi Utiliser TD-Learning ?

- **Efficacité** : L'apprentissage se fait en temps réel, ce qui est utile dans des environnements où les épisodes sont longs ou continus.
- **Flexibilité** : Il s'adapte bien aux environnements changeants, permettant à l'agent d'améliorer ses décisions au fur et à mesure qu'il acquiert de nouvelles informations.

En résumé, le TD-Learning est une méthode efficace pour enseigner à un agent comment naviguer dans un environnement complexe en apprenant progressivement de ses propres actions et résultats.





# 2 - Concepts Clés

### 1. Équation de Mise à Jour TD(0)

L'algorithme TD(0) met à jour la valeur d'un état en utilisant l'équation suivante :

$$
V(S_t) \leftarrow V(S_t) + \alpha [R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]
$$

**Termes :**
- **$$V(S_t)$$** : Valeur de l'état actuel.
- **$$R_{t+1}$$** : Récompense immédiate après l'action.
- **$$\alpha$$** : Taux d'apprentissage.
- **$$\gamma$$** : Facteur de discount.

### 2. Q-Learning

Le **Q-Learning** est une extension du TD-Learning qui apprend les valeurs des paires état-action :

$$
Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma \max_{a} Q(S_{t+1}, a) - Q(S_t, A_t)]
$$

## Comparaison avec Monte Carlo

- **Monte Carlo** : Nécessite la fin d'un épisode pour mettre à jour les valeurs.
- **TD-Learning** : Met à jour après chaque étape, permettant un apprentissage plus rapide dans des environnements longs ou infinis.

## Applications et Exemples

### Exemple Pratique : Lancer de Dé

Pour estimer la valeur attendue d'un lancer de dé :

$$
E(X) = \frac{1 + 2 + 3 + 4 + 5 + 6}{6} = 3.5
$$

### Code Python pour Estimation Empirique

```python
import numpy as np
import matplotlib.pyplot as plt

def estimate_expected_value(num_throws):
    sum_of_dice_values = 0
    running_average = []
    
    for i in range(num_throws):
        dice_value = np.random.randint(1, 7)
        sum_of_dice_values += dice_value
        running_average.append(sum_of_dice_values / (i + 1.0))
    
    average = sum_of_dice_values / num_throws
    print(f"Valeur moyenne après {num_throws} lancers: {average}")
    
    plt.plot(running_average, label="Moyenne empirique")
    plt.axhline(y=3.5, color='k', linestyle='-', label="Valeur attendue théorique (3.5)")
    plt.legend()
    plt.show()

estimate_expected_value(10000)
```

## Conclusion

Le TD-Learning est une méthode puissante pour l'apprentissage en temps réel dans des environnements dynamiques. Le Q-Learning, une version avancée, permet d'apprendre directement les actions optimales.

Pour plus de détails sur les algorithmes et leurs applications, vous pouvez consulter des ressources comme "Reinforcement Learning: An Introduction" par Sutton et Barto.

