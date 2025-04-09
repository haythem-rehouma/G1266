#  Quiz – Questions avec calculs (Q-Learning)



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

> **Réponse attendue :**  
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

> **Réponse attendue :**

$$
Q(s,a) = (1 - 0.3) \cdot 2 + 0.3 \cdot (3 + 0 \cdot 8) = 0.7 \cdot 2 + 0.3 \cdot 3 = 1.4 + 0.9 = \boxed{2.3}
$$

> **Interprétation :**  
Quand $\gamma = 0$, l’agent **ignore complètement le futur**.

<br/>
<br/>

## 🔢 Question 9 – Cas inverse avec γ = 1

Même question que la précédente, mais maintenant avec $\gamma = 1$ :

> **Réponse attendue :**

$$
Q(s,a) = 0.7 \cdot 2 + 0.3 \cdot (3 + 1 \cdot 8) = 1.4 + 0.3 \cdot 11 = 1.4 + 3.3 = \boxed{4.7}
$$

> **Interprétation :**  
Avec $\gamma = 1$, l’agent **considère pleinement le futur** (pas de réduction des récompenses futures).

