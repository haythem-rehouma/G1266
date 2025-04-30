# Introduction aux méthodes de Monte Carlo pour faire des estimations numériques

Dans cette nouvelle section, nous allons explorer une approche différente et plus flexible appelée **méthode de Monte Carlo**. Contrairement à d'autres méthodes comme la **programmation dynamique** que nous avons étudiée auparavant, les méthodes Monte Carlo présentent plusieurs avantages intéressants.

### Pourquoi la méthode Monte Carlo ?
La programmation dynamique (DP) que nous avons vue dans les sections précédentes a certains **inconvénients** :
1. **Besoin d'un modèle complet de l'environnement** : Elle nécessite de connaître à l'avance comment l'environnement fonctionne (les transitions entre les états, et les récompenses associées).
2. **Difficulté avec les grands systèmes** : La programmation dynamique a du mal à gérer des environnements avec un grand nombre d'états, car cela devient trop complexe.

Les méthodes Monte Carlo, par contre, sont beaucoup plus flexibles car elles :
- **N'ont pas besoin de connaître l'environnement à l'avance** : Tu n'as pas besoin de connaître toutes les transitions et récompenses à l'avance.
- **S'adaptent mieux aux environnements de grande taille** : Elles sont plus efficaces même lorsque le système a beaucoup d'états possibles.

### Qu'allons-nous faire ?

Nous allons d'abord commencer par un exemple simple : **estimer la valeur de Pi** en utilisant une méthode Monte Carlo. Cela nous permettra de voir comment ces méthodes fonctionnent de manière intuitive.

Ensuite, nous allons utiliser la méthode Monte Carlo pour résoudre un problème plus complexe :
- **Prédire des valeurs d'états et d'actions** : Comment estimer la "valeur" d'un état ou d'une action dans un environnement donné.
  
Nous allons explorer deux manières d'appliquer ces prédictions :
1. **Première visite (First-visit)** : où nous utilisons les informations de la première fois qu'un état est visité.
2. **Chaque visite (Every-visit)** : où nous utilisons toutes les visites d'un état pour améliorer nos prédictions.

### Application pratique : Jouer au blackjack avec Monte Carlo
Ensuite, nous allons **entraîner un agent** à jouer au jeu de cartes **blackjack** en utilisant la méthode Monte Carlo. Cela signifie que l'agent va apprendre, au fur et à mesure qu'il joue, quelles actions lui rapportent le plus de gains dans ce jeu. 

Nous mettrons également en œuvre :
- **Le contrôle on-policy et off-policy** : Ce sont des techniques qui permettent de guider l'agent à trouver la meilleure stratégie (ou politique).
- **Le contrôle epsilon-greedy** : Une méthode qui permet à l'agent d'explorer de nouvelles actions, tout en exploitant ce qu'il a déjà appris.
- **L'échantillonnage par importance pondérée** : Une technique avancée qui nous aide à évaluer et améliorer les politiques de manière plus efficace.


