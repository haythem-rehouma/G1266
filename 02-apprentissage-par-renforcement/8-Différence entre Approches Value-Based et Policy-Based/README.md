
<br/>

# Tableau des concepts pour l’examen de mi-session**

| **Catégorie**                        | **Concept / Élément à revoir**                             | **Définition ou exemple** |
|-------------------------------------|------------------------------------------------------------|---------------------------|
| **Fondamentaux MDP**               | MDP (Markov Decision Process)                              | Modèle mathématique pour décrire la prise de décision séquentielle dans un environnement incertain. |
|                                     | Propriété de Markov                                        | L'état futur dépend uniquement de l'état actuel, pas de l’historique complet. |
|                                     | Environnement                                              | Le monde dans lequel évolue l’agent, avec ses règles, états et récompenses. |
|                                     | État                                                       | Une situation ou configuration à un moment donné (ex: position d’un robot). |
|                                     | Action                                                     | Une décision ou un mouvement effectué par l’agent à partir d’un état. |
|                                     | Reward (Récompense)                                        | Retour numérique obtenu après une action (ex: +10 pour un bon choix). |
|                                     | Utilité                                                    | Valeur totale attendue qu’un agent peut accumuler à partir d’un état. |
|                                     | Utilité optimale                                           | Utilité maximale possible, en suivant la meilleure stratégie. |
|                                     | Stratégie                                                  | Plan qui indique quelle action prendre dans chaque état. |
|                                     | Stratégie optimale                                         | Stratégie qui maximise les récompenses à long terme. |
|                                     | Discounting                                                | Réduction de l’importance des récompenses futures, avec un facteur γ. |
|                                     | État absorbant                                             | État final duquel on ne sort plus (ex: sortie du labyrinthe). |
|                                     | Épisode                                                    | Suite d'étapes (état → action → état...) qui se termine dans un état absorbant. |
| **Comparaisons**                    | Processus déterministe vs stochastique                     | Déterministe : même action → même résultat. Stochastique : action → résultats variables. |
|                                     | Environnement dynamique vs statique                        | Dynamique : change pendant l’apprentissage. Statique : ne change pas. |
| **Apprentissage par Renforcement** | Exploration vs exploitation                                | Explorer : essayer de nouvelles actions. Exploiter : choisir la meilleure connue. |
|                                     | Stratégie ε-greedy                                         | Avec probabilité ε, on explore ; sinon on exploite la meilleure action. |
|                                     | Valeur d'état vs valeur Q-state                            | Valeur d’état : utilité d’un état. Q-state : utilité d’une paire (état, action). |
|                                     | Calcul de la valeur d’un état                              | Moyenne pondérée des valeurs futures attendues. |
|                                     | Calcul de la valeur Q-state                                | Basée sur la récompense immédiate + valeur future estimée via Bellman. |
|                                     | Itération                                                  | Répétition du calcul des valeurs jusqu’à convergence. |
|                                     | Algorithme d’itération de valeur                           | Méthode pour calculer la meilleure stratégie en mettant à jour les valeurs d’état. |
| **Application / Exercices vus**     | Mise à jour de la Q-table avec équations de Bellman        | On actualise les Q-valeurs à chaque expérience : Q ← Q + α (TD). |
|                                     | Quiz sur la Q-table (correction envoyée précédemment)      | Vérification de la compréhension de la mise à jour de Q-table. |

