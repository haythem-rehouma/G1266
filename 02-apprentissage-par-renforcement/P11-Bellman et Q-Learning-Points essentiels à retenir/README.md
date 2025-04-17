
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


Pour plus d'informations, cliquez ici : [Révision des Concepts Fondamentaux](./concepts/recap-concepts-rl.md)



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









# Références : 

- https://www.javatpoint.com/reinforcement-learning#google_vignette
- https://www.youtube.com/watch?v=9JZID-h6ZJ0&ab_channel=CodeEmporium
- https://www.youtube.com/watch?app=desktop&v=3Rx2x2traxw&ab_channel=MaheshHuddar
