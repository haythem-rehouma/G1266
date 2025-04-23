# **EXAMEN 1 – APPRENTISSAGE PAR RENFORCEMENT**

## **Partie 1 : Questions à choix multiples (20 points)**  
> **Instructions** : Choisissez **la meilleure réponse** + Justifiez votre réponse brièvement. Chaque question vaut **2 points**.



### **1. Parmi les éléments suivants, lequel est indispensable pour définir formellement un MDP ?**

a) Une fonction de coût  
b) Une politique aléatoire  
c) Un ensemble d’états, d’actions, de récompenses et de transitions  
d) Une stratégie de récompense optimale



### **2. Quelle affirmation est correcte à propos d’un MDP stationnaire ?**

a) Les probabilités de transition changent avec le temps  
b) Les récompenses dépendent de la trajectoire complète  
c) Les politiques optimales n’existent pas  
d) Les dynamiques de transition ne changent pas dans le temps



### **3. Dans un environnement stochastique, quelle conséquence principale la stochasticité introduit-elle sur l’agent ?**

a) L’agent peut utiliser l’algorithme KNN pour la prédiction  
b) Les actions ne garantissent pas d’atteindre l’état cible  
c) Les politiques deviennent uniquement exploitatives  
d) L’environnement est désormais totalement déterministe



### **4. Quelle stratégie décrit le mieux un comportement greedy pur ?**

a) L’agent choisit parfois des actions aléatoires  
b) L’agent maximise toujours la récompense immédiate  
c) L’agent utilise la fonction de valeur pour prédire des trajectoires  
d) L’agent n’explore jamais et suit la probabilité la plus basse



### **5. Quel rôle joue le taux de discount (γ) dans les décisions à long terme ?**

a) Il ignore totalement les récompenses futures si γ = 1  
b) Il inverse l’ordre des récompenses passées et futures  
c) Il permet de pondérer l’importance des récompenses futures  
d) Il accélère la convergence de l’apprentissage Q uniquement



### **6. Quelle est une condition **nécessaire** pour garantir la convergence de l’algorithme de Q-learning ?**

a) Le taux d'apprentissage doit être constant  
b) Toutes les paires (état, action) doivent être explorées infiniment souvent  
c) Les actions doivent être tirées aléatoirement sans stratégie  
d) La politique doit être purement déterministe dès le départ



### **7. En quoi la fonction de valeur V(s) diffère-t-elle de l’estimation Q(s, a) dans l’apprentissage par renforcement ?**

a) V(s) suppose toujours un environnement stochastique, Q(s, a) non  
b) V(s) est toujours plus précise que Q(s, a)  
c) V(s) estime la valeur d’un état sous une politique, Q(s, a) la valeur d’une action dans un état  
d) Il n’y a pas de différence fondamentale entre les deux



### **8. Quelle est la meilleure description d’un état absorbant ?**

a) Un état à partir duquel toutes les récompenses futures sont nulles  
b) Un état qui maximise toujours les récompenses  
c) Un état à partir duquel toutes les politiques deviennent invalides  
d) Un état qui doit toujours être évité dans un MDP



### **9. Dans un processus de prise de décision, que signifie qu’une politique est $\epsilon$-greedy ?**

a) Elle suit uniquement les transitions aléatoires  
b) Elle ne choisit jamais l’action optimale  
c) Elle choisit l’action optimale avec une probabilité de $1 - \epsilon$, et une action aléatoire avec $\epsilon$  
d) Elle choisit l’action la plus risquée si $\epsilon$ est élevé




### **10. Quelle est la principale différence entre l’équation de Bellman et l’algorithme de Q-learning ?**

a) L'équation de Bellman nécessite l'exécution complète d'un épisode, Q-learning non  
b) Q-learning estime les valeurs en ligne sans connaître le modèle de transition, contrairement à l’équation de Bellman  
c) L’équation de Bellman est utilisée uniquement pour des environnements stochastiques, Q-learning pour des environnements déterministes  
d) Q-learning suppose une connaissance parfaite de la fonction de récompense, contrairement à l’équation de Bellman




# Question Bonus non obligatoire ( de recherche)

### **11. Quelle est la différence fondamentale entre la méthode Monte Carlo et l’algorithme de Q-learning ?**

a) Monte Carlo utilise l’actualisation temporelle, Q-learning non  
b) Q-learning est une méthode non-off-policy  
c) Monte Carlo nécessite d’attendre la fin d’un épisode pour mettre à jour les valeurs  
d) Q-learning ne peut pas être utilisé dans des environnements stochastiques


