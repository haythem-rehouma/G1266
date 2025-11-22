# **RAPPEL- Comprendre TD(0), TD(n) et TD(λ)**



# **Table des matières**

1. Introduction : pourquoi ces méthodes existent
2. Rappel : Qu’est-ce qu’une valeur V(S) en RL ?
3. Pourquoi faut-il mettre à jour V(S) ?
4. Les trois philosophies de mise à jour
5. TD(0) : mise à jour immédiate
6. TD(n) : mise à jour après n pas
7. TD(λ) : combinaison intelligente de tous les horizons
8. Traces d’éligibilité : intuition visuelle
9. Comparaisons complètes entre TD(0), TD(n), TD(λ)
10. Quand utiliser chaque méthode ?
11. Exemples réels concrets
12. Exercices pour vérifier la compréhension

---

# **1. Introduction : pourquoi ces méthodes existent**

En apprentissage par renforcement (RL), le but est d’apprendre une fonction :

$$
V(S) = \text{qualité future attendue si je suis dans l’état } S
$$

Pour apprendre cette valeur, on estime comment les récompenses futures se comportent.
Mais un agent ne reçoit pas toutes les récompenses en une seule fois.
Elles arrivent progressivement dans le temps.

Les méthodes TD (Temporal Difference) servent à **mettre à jour V(S) avant d’avoir tout vu**, en utilisant ce qu’on connaît du futur immédiat.

Il en existe plusieurs versions selon le niveau de patience et de précision souhaité.



# **2. Rappel : Qu’est-ce qu’une valeur V(S) ?**

Pour un état S :

* si V(S) est grande → cet état est prometteur
* si V(S) est faible → cet état mène à de mauvaises récompenses

Dans un jeu cela peut être :

* V(«position») = chance de gagner
  Dans la robotique :
* V(«position/énergie») = performance attendue
  Dans un marché financier :
* V(«prix+contexte») = gain attendu

L’objectif est d’améliorer V(S) avec le temps.

---

# **3. Pourquoi mettre à jour V(S) ?**

Parce que :

1. Le futur change
2. Le monde n’est jamais parfaitement connu
3. L’agent apprend en marchant

On doit donc mettre à jour V(S) après chaque événement, chaque récompense, ou chaque observation.

---

# **4. Les trois philosophies de mise à jour**

Il existe trois grandes manières :

### **1) Très rapide → TD(0)**

On met à jour immédiatement avec ce qu’on connaît maintenant.

### **2) Moyennement patient → TD(n)**

On attend d’avoir n récompenses avant de mettre à jour.

### **3) Très intelligent → TD(λ)**

On mélange toutes les mises à jour possibles, court terme + moyen terme, avec une pondération λ.

---

# **5. TD(0) : mise à jour immédiate**

## **Définition**

TD(0) utilise la récompense immédiate plus l’estimation du prochain état.

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \right]
$$

### **Intuition**

Je suis dans S.
Je reçois une récompense.
Je regarde seulement l’étape suivante S'.
Je mets à jour immédiatement.

### **Avantages**

* très rapide
* peu coûteux
* parfait pour les environnements rapides

### **Limites**

* ne voit pas plus loin que 1 pas
* sous-utilise les informations futures

---

# **6. TD(n) : mise à jour après n pas**

## **Définition**

On utilise les n prochaines récompenses :

$$
G_t^{(n)} = \sum_{k=1}^{n} \gamma^{k-1} R_{t+k} + \gamma^n V(S_{t+n})
$$

Mise à jour 

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ G_t^{(n)} - V(S_t) \right]
$$

### **Intuition**

Au lieu de regarder un seul pas, TD(n) regarde plusieurs pas.
Il attend d’avoir n récompenses pour corriger V(S_t).

### **Avantages**

* meilleure précision si n augmente
* combine réel + bootstrap

### **Limites**

* si n grand, l’agent doit attendre
* variance plus élevée
* mémoire plus grande

---

# **7. TD(λ) : combinaison intelligente de tous les horizons**

## **Idée principale**

TD(λ) combine **tous** les TD(n), du court terme au long terme, avec un poids décroissant :

$$
G_t^{(\lambda)} = (1-\lambda) \sum_{n=1}^{\infty} \lambda^{n-1} G_t^{(n)}
$$

### **Interprétation**

* λ = 0 → TD(0)
* λ proche de 1 → un mélange proche de Monte Carlo
* entre les deux → on prend un peu de TD(1), TD(2), TD(3), etc.

C’est comme si TD(0), TD(1), TD(2), TD(3)… travaillaient ensemble.

---

# **8. Traces d’éligibilité : intuition visuelle**

TD(λ) est implémenté avec les **traces d’éligibilité**, qui donnent de l’importance aux états visités récemment.

Pour chaque état s 

$$
e_t(s) = \gamma \lambda e_{t-1}(s) + \mathbf{1}{s = S_t}
$$

Plus un état a été visité récemment, plus il reçoit une mise à jour lorsque l’erreur TD apparaît.

C’est ce qui permet à TD(λ) d’apprendre sur plusieurs horizons en même temps.

---

# **9. Comparaison complète**

| Méthode   | Horizon | Mise à jour  | Biais        | Variance    | Rapidité    | Utilité                                     |
| --------- | ------- | ------------ | ------------ | ----------- | ----------- | ------------------------------------------- |
| **TD(0)** | 1 pas   | immédiate    | biaisé       | faible      | très rapide | environnements rapides                      |
| **TD(n)** | n pas   | retardée     | moins biaisé | plus élevée | moyenne     | prédictions à horizon court/moyen           |
| **TD(λ)** | tous n  | incrémentale | compromis    | compromis   | très bonne  | environnements complexes, non stationnaires |

---

# **10. Quand utiliser chaque méthode ?**

### **TD(0)** → si le système doit apprendre très rapidement

Exemples : robotique instantanée, détection immédiate, autoscaling.

### **TD(n)** → si on sait que les futures récompenses jusqu’à n pas sont importantes

Exemples : prévision météo 3 jours, tendance court terme.

### **TD(λ)** → si l’environnement est complexe ou non stationnaire

Exemples : marché financier, drones, optimisation d’énergie, systèmes cyber.

---

# **11. Exemples industriels**

### **Gestion d’énergie**

Les coûts changent continuellement → TD(λ).

### **Drone**

Obstacles dynamiques → TD(λ).

### **Supermarché**

Tendances saisonnières → TD(λ).

### **Jeu vidéo**

Environnement adversarial → SARSA ou TD(λ).

### **Serveurs**

Charge variable → TD(λ).

### **Marché financier**

Volatilité → TD(λ).

---

# **12. Exercices (avec réponses sur demande)**

1. Explique la différence entre TD(0) et TD(n).
2. Pourquoi TD(λ) peut-il être vu comme une moyenne de TD(n) ?
3. Donne un cas réel où TD(0) échoue mais TD(λ) réussit.
4. Donne un cas réel où TD(n) est préférable à TD(0).
5. Trouve un environnement où λ doit être proche de 1.


