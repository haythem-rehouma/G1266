# **Partie-01 : Questions Directes**

1. **Définissez l'apprentissage par différence temporelle (TD) dans le contexte de l'apprentissage par renforcement.**
   - *Sous-question : Quels sont les principaux avantages des méthodes TD par rapport aux méthodes de Monte Carlo ?*

2. **Quelle est la règle de mise à jour TD(0) pour estimer la valeur d’un état ?**
   - *Sous-question : Quel est le rôle de chaque terme dans cette règle de mise à jour ?*

3. **Expliquez la différence entre SARSA et Q-Learning.**
   - *Sous-question : Pourquoi SARSA est-il considéré comme une méthode sur politique et Q-Learning comme une méthode hors politique ?*

4. **Qu’est-ce qu’une politique epsilon-greedy et comment est-elle utilisée dans les algorithmes de TD ?**
   - Sous-question : Que se passerait-il si $\\epsilon$ était très faible ou très élevé dans un algorithme SARSA ?

5. **Quelle est la règle de mise à jour dans l’algorithme SARSA ?**
   - Sous-question : Que signifie le terme $Q(S_{t+1}, A_{t+1})$ dans cette règle ?

---

# **Partie-02 : Questions de Réflexion**

1. **Pourquoi les méthodes de contrôle TD peuvent-elles être appliquées sans attendre la fin de l'épisode ?**
   - *Sous-question : Quels types de situations bénéficient particulièrement de cette caractéristique des méthodes TD ?*

2. **Expliquez le rôle du taux d'apprentissage (alpha) dans les algorithmes TD comme SARSA et Q-Learning.**
   - Sous-question : Comment un choix inapproprié de $\\alpha$ pourrait-il affecter la convergence de l'algorithme ?

3. **Dans l’algorithme Q-Learning, pourquoi utilise-t-on la valeur Q maximale de l’état suivant pour mettre à jour la valeur Q actuelle ?**
   - *Sous-question : Quels sont les effets d’utiliser la valeur maximale par rapport à une valeur moyenne ?*

4. **En quoi SARSA est-il plus sensible aux choix de la politique actuelle par rapport à Q-Learning ?**
   - *Sous-question : Donnez un exemple de situation où SARSA et Q-Learning produiraient des comportements différents pour un même environnement.*

5. **Comment l’utilisation d’une politique epsilon-greedy dans SARSA et Q-Learning aide-t-elle à résoudre le dilemme exploration/exploitation ?**
   - Sous-question : Pourquoi pourrait-il être nécessaire de réduire progressivement $\\epsilon$ dans un contexte d’apprentissage à long terme ?
