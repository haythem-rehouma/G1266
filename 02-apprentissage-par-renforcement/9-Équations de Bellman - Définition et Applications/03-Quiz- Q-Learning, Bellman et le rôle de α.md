#  Quiz : Q-Learning, Bellman et le rôle de α

# Question 1  
Que représente la lettre **α (alpha)** dans l’équation du Q-Learning ?  
**a.** Le taux d'exploration  
**b.** Le facteur de réduction du futur  
**c.** Le taux d’apprentissage  
**d.** La probabilité de récompense immédiate

> **Réponse attendue :** c

<br/>
<br/>

# Question 2  
Dans cette équation :

$$
Q(s,a) \leftarrow (1 - \alpha) \cdot Q(s,a) + \alpha \cdot \left[ r + \gamma \cdot \max_{a'} Q(s', a') \right]
$$

Que représente le terme **$(1 - \alpha) \cdot Q(s,a)$** ?

**a.** Le poids de l’expérience récente  
**b.** Le poids de ce qu’on savait déjà  
**c.** La récompense immédiate  
**d.** L’action choisie aléatoirement

> **Réponse attendue :** b


<br/>
<br/>

# Question 3  
Si **α = 1**, que se passe-t-il lors de la mise à jour ?

**a.** On garde uniquement l’ancienne valeur  
**b.** On prend en compte uniquement la nouvelle estimation  
**c.** On mélange à 50/50  
**d.** Il n’y a aucune mise à jour

> **Réponse attendue :** b


<br/>
<br/>

# Question 4  

Complétez :  
Dans le Q-learning, le **choix de l’action** est souvent contrôlé par une stratégie appelée ___________.

**a.** `alpha-greedy`  
**b.** `greedy-only`  
**c.** `epsilon-greedy`  
**d.** `bellman-greedy`

> **Réponse attendue :** c


<br/>
<br/>

# Question 5  
Quelle phrase est correcte à propos de l’équation de Bellman ?  
**a.** Elle permet d’ajouter des récompenses négatives uniquement  
**b.** Elle ignore les états futurs  
**c.** Elle permet de relier la valeur actuelle à des états futurs possibles  
**d.** Elle est utilisée uniquement pour les jeux vidéo

> **Réponse attendue :** c
