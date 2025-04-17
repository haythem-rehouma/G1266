
# Plan de la séance


<br/>




**Dans les parties 1 et 2, nous allons réviser l’ensemble des concepts fondamentaux abordés en classe, notamment :**  
- les **états** et **états de départ** ;  
- les **états absorbants** ;  
- les **actions** et les **transitions** ;  
- les **récompenses** (rewards) et le **discount factor** (facteur d’actualisation) ;  
- la notion d’**utilité** ;  
- la **fonction de valeur d’un état** (*value function*) ;  
- la **fonction de valeur d’une politique** ;  
- le concept de **politique** (*policy*) lui-même.
- etc ...


Pour plus d'informations, cliquez ici : [Révision des Concepts Fondamentaux](../../concepts/recap-concepts-rl.md)



# Partie 1 - rappel du processus de Décision de Markov (MDP)


# Composantes des MDP :
- **États (S)** : Représentent les différentes situations possibles dans lesquelles un agent peut se trouver.
- **Actions (A)** : Les différentes actions que l'agent peut entreprendre dans un état donné.
- **Transitions (P(s'|s,a) ou T(s,a,s'))** : La probabilité de passer d'un état à un autre, en fonction de l'action entreprise.
- **Récompenses (R(s,a,s') et facteur de réduction γ)** : Les récompenses obtenues par l'agent lorsqu'il effectue une transition entre états après avoir pris une action.
- **État de départ (s₀)** : L'état initial à partir duquel le processus commence.

# Quantités importantes :
- **Politique** : Une stratégie ou une fonction qui associe à chaque état une action à entreprendre.
- **Utilité** : La somme des récompenses actualisées, où les récompenses futures sont pondérées par le facteur de réduction (γ).


<br/>


# Partie 2 - offline vs online learning

Nous verrons la différence entre les approches d’apprentissage avec ou sans interaction directe avec l’environnement.
Cette distinction est essentielle pour bien comprendre les méthodes utilisées en pratique.


<br/>



# Partie 3 - Équation de Bellman 

Nous introduirons l’équation de Bellman, pierre angulaire des MDP et de l’apprentissage par renforcement.
Elle permet d’exprimer la valeur d’un état en fonction des récompenses et des transitions futures.

*Dans cette partie, vous devez consulter les diapositives de la partie 3 (dossier pptx) afin de bien comprendre les notions suivantes : la fonction de valeur d’un état, la fonction Q (valeur d’un couple état-action), ainsi que l’équation de Bellman.*

<br/>



# Partie 4 - Calcul Mathématique 1  + Démonstration 1

*Dans cette partie, vous devez consulter les diapositives de la partie 4 (dossier pptx) afin de bien comprendre en détail comment on fait les calculs + la démonstration avec Python*

Nous allons justifier les étapes de la démonstration et proposer deux exercices guidés.
L’objectif est de renforcer la compréhension en appliquant l’équation de Bellman à un mini-problème.


- Démo 1 via un calcul mathématique (Partie_04.pptx)
- Démo 2 via l'éxcution d'un programme informatique (Dossier P10)

Nous allons illustrer l’utilisation concrète de l’équation de Bellman à travers un exemple simple.
Cette démonstration vise à montrer comment l’agent estime les valeurs d’état et la convergence de l'algorithme.



<br/>





# Partie 6 - Q-Learning

Nous verrons une méthode d’apprentissage très populaire : le Q-Learning.
C’est une technique modèle-free qui permet à un agent d’apprendre une politique optimale à partir de ses interactions.

- Démo 3 via un calcul mathématique (Partie_05.pptx) dans le dossier pptx.

<br/>




# Partie 7 - Examen formatif


- Nous mettrons en pratique le Q-Learning avec un exemple pas-à-pas et un examen formatif (dossier P12 - 12.5 - Examen-1-style-2.md).
- L’objectif est de montrer comment se construit la table des Q-values au fil des épisodes.


<br/>


# Partie 8 - Mini-projet 1


- Nous mettrons en pratique le Q-Learning avec des exemples pratqiue en python pas-à-pas et un examen formatif (dossier P12 - 12.5 - Examen-1-style-1.md), au même style que le gridworld (suite de la Démo 2 de la Partie 4).

<br/>




# Partie 9 - Démo AWS

Prochaines séances





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





# Références : 

- https://www.javatpoint.com/reinforcement-learning#google_vignette
- https://www.youtube.com/watch?v=9JZID-h6ZJ0&ab_channel=CodeEmporium
- https://www.youtube.com/watch?app=desktop&v=3Rx2x2traxw&ab_channel=MaheshHuddar
