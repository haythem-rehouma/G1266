# **Quiz à choix multiples : Méthodes de Monte Carlo**

1. **Qu'est-ce que la méthode de Monte Carlo dans le contexte de l'apprentissage par renforcement ?**
   - A. Une technique utilisant un modèle prédictif de l'environnement
   - B. Une méthode basée sur l'échantillonnage aléatoire répété pour estimer des valeurs
   - C. Une méthode qui calcule les valeurs d’état en temps réel
   - D. Une approche déterministe pour calculer des politiques optimales

2. **Quel est l'objectif principal de la prédiction Monte Carlo ?**
   - A. Déterminer la meilleure action pour chaque état
   - B. Calculer le rendement attendu pour une politique donnée
   - C. Évaluer la politique optimale
   - D. Calculer les transitions d'état

3. **Dans la méthode Every-Visit, la valeur d'un état est mise à jour :**
   - A. Uniquement la première fois que l'état est visité
   - B. À chaque fois que l'état est visité dans chaque épisode
   - C. Seulement si l'épisode se termine dans cet état
   - D. Après plusieurs épisodes

4. **Dans la méthode First-Visit, la valeur d'un état est mise à jour :**
   - A. À chaque visite de cet état dans chaque épisode
   - B. Seulement la première fois qu'il est visité dans chaque épisode
   - C. Après avoir visité tous les états
   - D. À chaque fois que l'épisode se termine dans cet état

5. Quelle équation représente la mise à jour de la fonction de valeur dans la méthode Every-Visit ?

A. 

$$ V(s) = V(s) + \alpha G $$

B.

$$ V(s) \approx \frac{1}{N(s)} \sum_{i=1}^{N(s)} G_i(s) $$

C.

$$ V(s) = \alpha [G - V(s)] $$

D.

$$ V(s) = \max G(s) $$

7. **Dans les méthodes Monte Carlo, qu'est-ce que le rendement \( G \) ?**
   - A. La valeur instantanée de l'état
   - B. La récompense cumulée observée pour un état jusqu'à la fin de l'épisode
   - C. La moyenne de toutes les valeurs d'état précédentes
   - D. La récompense immédiate de l'action

8. **Pourquoi les méthodes Monte Carlo nécessitent-elles des épisodes entiers ?**
   - A. Pour garantir que tous les états sont explorés
   - B. Parce qu'elles mettent à jour les valeurs à la fin de chaque épisode
   - C. Pour échantillonner toutes les transitions possibles
   - D. Pour maximiser la récompense immédiate

9. **Qu'est-ce que la politique epsilon-greedy ?**
   - A. Une politique qui sélectionne uniquement les actions optimales
   - B. Une politique où une action aléatoire est choisie avec probabilité \( \epsilon \)
   - C. Une politique qui ne choisit jamais d'actions aléatoires
   - D. Une politique qui maximise uniquement les récompenses futures

10. **Dans une politique epsilon-greedy, que se passe-t-il si $$\epsilon$$ est proche de 0 ?**
   - A. L'agent explore souvent de nouvelles actions
   - B. L'agent exploite principalement les actions optimales
   - C. L'agent choisit toujours des actions aléatoires
   - D. L'agent ignore les valeurs de récompense

11. **Que signifie "apprentissage sur politique" dans le contexte de Monte Carlo ?**
    - A. L'agent apprend en suivant la même politique pour le comportement et la mise à jour
    - B. L'agent utilise des politiques différentes pour le comportement et la mise à jour
    - C. L'agent apprend sans aucune politique
    - D. L'agent modifie sa politique de manière aléatoire

12. **Que signifie "apprentissage hors politique" dans les méthodes Monte Carlo ?**
    - A. L'agent utilise une politique unique pour le comportement et la mise à jour
    - B. L'agent suit une politique différente de la politique de comportement pour la mise à jour
    - C. L'agent maximise la récompense immédiate uniquement
    - D. L'agent se base uniquement sur des épisodes complets

13. **Dans l'apprentissage hors politique, pourquoi utilise-t-on l'échantillonnage d'importance ?**
    - A. Pour maximiser la récompense immédiate
    - B. Pour corriger la différence entre la politique de comportement et la politique cible
    - C. Pour diminuer la complexité de calcul
    - D. Pour éviter d'explorer de nouvelles actions

14. Quelle est l'équation de mise à jour pour l'échantillonnage d'importance ?

A. 

$$ Q(s, a) \leftarrow Q(s, a) + \alpha \cdot (G - Q(s, a)) $$

B. 

$$ Q(s, a) \leftarrow Q(s, a) + \alpha \cdot \frac{\pi(a|s)}{\mu(a|s)} \cdot (G - Q(s, a)) $$

C. 

$$ Q(s, a) \leftarrow Q(s, a) + \alpha \cdot \max(G) $$

D.

$$ Q(s, a) = G(s) $$

15. **Pourquoi les méthodes de Monte Carlo sont-elles dites "sans modèle" ?**
    - A. Elles nécessitent un modèle d'état-action
    - B. Elles estiment les valeurs sans connaissance préalable de la dynamique de l'environnement
    - C. Elles utilisent un modèle complexe de prédiction
    - D. Elles dépendent d'un modèle probabiliste

16. **Quelle est l'étape initiale dans l'algorithme de Monte Carlo ?**
    - A. Déterminer l'action optimale pour chaque état
    - B. Générer des épisodes en suivant la politique actuelle
    - C. Mettre à jour toutes les valeurs d'état
    - D. Calculer la récompense cumulée pour chaque action

17. **Quel est le rôle du facteur de réduction (ou d'actualisation) $$\gamma$$ dans les méthodes Monte Carlo ?**
    - A. Il réduit le taux d'apprentissage
    - B. Il diminue l'importance des récompenses futures
    - C. Il ajuste la politique pour chaque état
    - D. Il augmente la probabilité d'exploration

18. **Que fait un agent Monte Carlo dans une situation de contrôle sur politique ?**
    - A. Il utilise une politique optimale pour chaque état
    - B. Il suit la politique actuelle pour explorer et améliorer ses actions
    - C. Il explore aléatoirement toutes les actions possibles
    - D. Il applique uniquement la récompense immédiate

19. **Quel est le but du contrôle Monte Carlo ?**
    - A. Maximiser les récompenses futures dans un modèle de dynamique connu
    - B. Trouver la politique optimale en apprenant à partir des épisodes
    - C. Diminuer le nombre d'épisodes nécessaires pour l'apprentissage
    - D. Éviter de visiter les états non optimaux

20. **Dans les méthodes de contrôle Monte Carlo, que représente la fonction $$Q(s, a)$$ ?**
    - A. Le nombre total d'actions dans l'état \( s \)
    - B. La valeur d'action estimée pour l'état \( s \) et l'action \( a \)
    - C. La somme des récompenses futures possibles
    - D. La probabilité de choisir l'action \( a \) dans l'état \( s \)

21. **Quelle est la principale différence entre les méthodes Monte Carlo et les méthodes TD ?**
    - A. Les méthodes Monte Carlo mettent à jour après chaque action, contrairement aux méthodes TD
    - B. Les méthodes Monte Carlo nécessitent des épisodes entiers pour la mise à jour
    - C. Les méthodes Monte Carlo utilisent un modèle de prédiction
    - D. Les méthodes Monte Carlo sont basées sur des estimations temporelles

