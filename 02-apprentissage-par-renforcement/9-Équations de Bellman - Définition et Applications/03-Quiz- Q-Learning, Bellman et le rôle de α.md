#  Quiz : Q-Learning, Bellman et le rôle de α

# Partie 1 

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


<br/>
<br/>

#  Partie 2 – Questions avec calculs (Q-Learning)



# Question 6 – Mise à jour simple de Q

On considère :

- $Q(s,a) = 4$  
- $r = 5$ (récompense immédiate)  
- $\gamma = 0.9$ (facteur d’actualisation)  
- $\max_{a'} Q(s', a') = 10$ (meilleure action future)  
- $\alpha = 0.2$

### Question :  

Calculez la nouvelle valeur de $Q(s,a)$ après la mise à jour.

> **Formule :**  

$$
Q(s,a) \leftarrow (1 - \alpha) \cdot Q(s,a) + \alpha \cdot \left[ r + \gamma \cdot \max Q(s',a') \right]
$$

> **Réponse attendue :**

$$
Q(s,a) = 0.8 \cdot 4 + 0.2 \cdot (5 + 0.9 \cdot 10) = 3.2 + 0.2 \cdot 14 = 3.2 + 2.8 = \boxed{6.0}
$$

# Question 7 – Impact du taux d’apprentissage

Même situation que la question précédente, mais avec $\alpha = 0.5$.

Calculez à nouveau $Q(s,a)$.

> Réponse attendue :

$$
Q(s,a) = 0.5 \cdot 4 + 0.5 \cdot (5 + 0.9 \cdot 10) = 2 + 0.5 \cdot 14 = 2 + 7 = \boxed{9.0}
$$

> **Remarque pédagogique :**  
Plus α est élevé, plus l’agent se fie à **l’expérience récente**.



# Question 8 – Impact du facteur de discount γ

Prenons maintenant :  
- $Q(s,a) = 2$  
- $r = 3$  
- $\max Q(s',a') = 8$  
- $\alpha = 0.3$  
- **$\gamma = 0$**

Calculez $Q(s,a)$.

> Réponse attendue :

$$
Q(s,a) = (1 - 0.3) \cdot 2 + 0.3 \cdot (3 + 0 \cdot 8) = 0.7 \cdot 2 + 0.3 \cdot 3 = 1.4 + 0.9 = \boxed{2.3}
$$

> **Interprétation :**  
Quand $\gamma = 0$, l’agent **ignore complètement le futur**.

<br/>
<br/>

# Question 9 – Cas inverse avec γ = 1

Même question que la précédente, mais maintenant avec $\gamma = 1$ :

> Réponse attendue :

$$
Q(s,a) = 0.7 \cdot 2 + 0.3 \cdot (3 + 1 \cdot 8) = 1.4 + 0.3 \cdot 11 = 1.4 + 3.3 = \boxed{4.7}
$$

> **Interprétation :**  
Avec $\gamma = 1$, l’agent **considère pleinement le futur** (pas de réduction des récompenses futures).


