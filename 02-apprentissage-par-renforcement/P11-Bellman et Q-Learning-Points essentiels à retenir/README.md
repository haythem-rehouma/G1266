
# Plan de la séance



<br/>
<br/>
<br/>
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


Pour plus d'informations , cliquez ici : 




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
<br/>
<br/>
<br/>

# Partie 2 - offline vs online learning

Nous verrons la différence entre les approches d’apprentissage avec ou sans interaction directe avec l’environnement.
Cette distinction est essentielle pour bien comprendre les méthodes utilisées en pratique.


<br/>
<br/>
<br/>
<br/>


# Partie 3 - Équation de Bellman 

Nous introduirons l’équation de Bellman, pierre angulaire des MDP et de l’apprentissage par renforcement.
Elle permet d’exprimer la valeur d’un état en fonction des récompenses et des transitions futures.



<br/>
<br/>
<br/>
<br/>


# Partie 4 - Démonstration 1

Nous allons illustrer l’utilisation concrète de l’équation de Bellman à travers un exemple simple.
Cette démonstration vise à montrer comment l’agent estime les valeurs d’état.



<br/>
<br/>
<br/>
<br/>



# Partie 5 - (Justification de la démo 1 et exercice): Comment utiliser l'équation de Bellman dans l'Apprentissage par Renforcement

Nous allons justifier les étapes de la démonstration et proposer un exercice guidé.
L’objectif est de renforcer la compréhension en appliquant l’équation de Bellman à un mini-problème.



<br/>
<br/>
<br/>
<br/>


# Partie 6 - Q-Learning

Nous verrons une méthode d’apprentissage très populaire : le Q-Learning.
C’est une technique modèle-free qui permet à un agent d’apprendre une politique optimale à partir de ses interactions.



<br/>
<br/>
<br/>
<br/>



# Partie 7 - Démonstration 2


Nous mettrons en pratique le Q-Learning avec un exemple pas-à-pas.
L’objectif est de montrer comment se construit la table des Q-values au fil des épisodes.


<br/>
<br/>
<br/>
<br/>


# Partie 8 - Démo AWS

Prochaines séances



<br/>
<br/>
<br/>
<br/>


# Partie 9 - Exercices

Nous conclurons la séance par une série d’exercices pour consolider les acquis.
Ces exercices couvrent les concepts vus dans la séance, de l’équation de Bellman jusqu’au Q-Learning.





# Références : 

- https://www.javatpoint.com/reinforcement-learning#google_vignette
- https://www.youtube.com/watch?v=9JZID-h6ZJ0&ab_channel=CodeEmporium
- https://www.youtube.com/watch?app=desktop&v=3Rx2x2traxw&ab_channel=MaheshHuddar
