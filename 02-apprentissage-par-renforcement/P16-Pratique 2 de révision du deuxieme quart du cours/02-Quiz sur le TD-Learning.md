# Quiz sur le TD-Learning


#### 1. Introduction au TD-Learning

1. Qu’est-ce que le TD-Learning ?
   - A) Une méthode d'apprentissage par renforcement utilisant des modèles
   - B) Une méthode d'apprentissage par renforcement qui combine Monte Carlo et programmation dynamique
   - C) Une méthode d’apprentissage supervisé pour les données tabulaires
   - D) Un algorithme de régression linéaire

2. Comment le TD-Learning met-il à jour les valeurs ?
   - A) À chaque étape, sans attendre la fin d'un épisode
   - B) Après chaque épisode complet
   - C) En fonction d’une récompense fixe
   - D) Uniquement en cas d’échec de l’agent

3. Quelle est la principale différence entre le TD-Learning et Monte Carlo ?
   - A) Monte Carlo utilise des approximations, alors que TD-Learning utilise des modèles exacts
   - B) Monte Carlo nécessite la fin d'un épisode pour la mise à jour, alors que TD-Learning met à jour à chaque étape
   - C) TD-Learning est une méthode de classification
   - D) TD-Learning utilise uniquement des estimations passées pour la mise à jour

4. Quel est l’avantage principal de TD-Learning dans des environnements longs ou continus ?
   - A) Il permet un apprentissage en temps réel
   - B) Il fonctionne uniquement avec des données statiques
   - C) Il utilise des récompenses fixes
   - D) Il nécessite un modèle complet de l’environnement

---

#### 2. Concepts Clés du TD-Learning

5. Dans l’équation de mise à jour du TD(0), que représente **$$V(S_t)$$** ?
   - A) La récompense immédiate
   - B) La valeur de l'état actuel
   - C) Le taux d’apprentissage
   - D) Le facteur de discount

6. Que représente le taux d'apprentissage **($\alpha$)** dans TD-Learning ?
   - A) La vitesse à laquelle l'agent apprend des nouvelles informations
   - B) La fréquence des actions
   - C) La distance entre les états
   - D) La vitesse de déplacement de l'agent

7. À quoi sert le facteur de discount **($\gamma$)** dans le TD-Learning ?
   - A) À réduire l’importance des récompenses futures
   - B) À augmenter l’importance des récompenses passées
   - C) À diminuer le taux d'apprentissage
   - D) À maximiser les récompenses immédiates

8. Dans l'équation TD(0), que signifie un **$\gamma$** proche de 1 ?
   - A) Les récompenses futures sont négligées
   - B) Les récompenses futures sont très valorisées
   - C) La mise à jour se fait uniquement en fin d'épisode
   - D) L’apprentissage se concentre uniquement sur l'état actuel

9. Dans le TD-Learning, quel est l’effet d’un **$\alpha$** élevé ?
   - A) L’agent apprend lentement
   - B) L’agent s’adapte rapidement aux nouvelles informations
   - C) La mise à jour des valeurs est retardée
   - D) L’apprentissage est complètement arrêté

---

#### 3. Fonctionnement du TD(0) et du Q-Learning

10. Que met à jour l'algorithme TD(0) ?
    - A) La valeur d'une action spécifique
    - B) La valeur d'un état uniquement
    - C) La probabilité de transition
    - D) La récompense immédiate

11. Comment fonctionne l'équation de mise à jour de TD(0) ?
    - A) $$V(S_t) \leftarrow V(S_t) + \alpha [R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]$$
    - B) $$V(S_t) \leftarrow V(S_t) + \alpha \times R_{t+1}$$
    - C) $$V(S_t) \leftarrow \gamma [V(S_t) - V(S_{t-1})]$$
    - D) $$V(S_t) \leftarrow V(S_t) - \alpha [R_{t+1}]$$

12. Que met à jour le Q-Learning par rapport au TD(0) ?
    - A) Les paires état-action
    - B) Les probabilités de transition
    - C) Les valeurs d'état uniquement
    - D) Le facteur de discount

13. Quelle est l’équation de mise à jour du Q-Learning ?
    - A) $$Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma \max_{a} Q(S_{t+1}, a) - Q(S_t, A_t)]$$
    - B) $$Q(S_t, A_t) \leftarrow Q(S_t, A_t) \times R_{t+1}$$
    - C) $$Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \gamma R_{t+1}$$
    - D) $$Q(S_t, A_t) \leftarrow Q(S_t, A_t) - \alpha \max R_{t+1}$$

14. Quelle est la principale différence entre TD(0) et Q-Learning ?
    - A) TD(0) met à jour les valeurs d'état, tandis que Q-Learning met à jour les paires état-action
    - B) Q-Learning utilise un modèle de l’environnement
    - C) TD(0) est basé sur les méthodes de Monte Carlo
    - D) Q-Learning met à jour uniquement après un épisode

---

#### 4. Comparaison avec l’Équation de Bellman et les Méthodes Sans Modèle

15. Quelle méthode nécessite un modèle complet de l’environnement pour fonctionner ?
    - A) TD-Learning
    - B) Q-Learning
    - C) Équation de Bellman
    - D) Apprentissage supervisé

16. En quoi l'équation de Bellman diffère-t-elle du TD-Learning ?
    - A) L'équation de Bellman n'utilise pas de taux d'apprentissage
    - B) L'équation de Bellman nécessite des probabilités de transition pour calculer la valeur d'un état
    - C) Le TD-Learning utilise un modèle de transition complet
    - D) L’équation de Bellman met à jour uniquement les actions

17. Pourquoi Q-Learning est-il considéré comme une méthode sans modèle ?
    - A) Parce qu'il utilise uniquement des récompenses immédiates
    - B) Parce qu'il n'a pas besoin de connaître les transitions entre états pour apprendre
    - C) Parce qu'il apprend après chaque épisode
    - D) Parce qu'il utilise un facteur de discount constant

18. Quel est un avantage du TD-Learning par rapport aux méthodes basées sur modèle ?
    - A) Il peut apprendre sans connaître les transitions entre états
    - B) Il utilise des estimations exactes dès le départ
    - C) Il nécessite moins de temps d'apprentissage
    - D) Il est plus rapide que Monte Carlo

---

#### 5. Applications et Avantages

19. Pourquoi le TD-Learning est-il particulièrement utile dans des environnements en temps réel ?
    - A) Car il met à jour les valeurs immédiatement après chaque étape
    - B) Car il attend la fin de l’épisode pour apprendre
    - C) Car il nécessite un modèle complet de l’environnement
    - D) Car il maximise les récompenses immédiates

20. Dans quel cas le TD-Learning est-il plus efficace que Monte Carlo ?
    - A) Dans des environnements où les épisodes sont très longs ou continus
    - B) Lorsqu’un modèle de transition est connu
    - C) Lorsqu'il y a peu de récompenses dans l’environnement
    - D) Dans des environnements statiques avec peu de variations
