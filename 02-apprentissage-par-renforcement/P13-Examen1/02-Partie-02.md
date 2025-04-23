# **Partie 2 : Questions à réponse courte (30 points)**

> **Instructions** : Répondez de façon claire et structurée. Utilisez des schémas ou équations si cela vous aide à mieux justifier vos réponses.


### **1. Décrivez la stratégie $\epsilon$-greedy.**

.....................................................................................................

### **2. Décrivez un exemple dans lequel un agent utilisant une stratégie purement exploitative pourrait échouer à apprendre une politique optimale. Quelle solution proposez-vous pour corriger ce comportement ?**

> *Conseil et Astuce pour la réflexion :  Expliquez, par exemple, à l’aide d’un exemple, un scénario dans lequel un agent appliquant une stratégie strictement exploitative (greedy) échoue à découvrir une politique optimale. Pourquoi ce comportement est-il problématique ? Quelle solution proposez-vous pour encourager une meilleure exploration de l’environnement ?*


.....................................................................................................

### **3. Un MDP contient deux états absorbants : un état terminal avec récompense - 100 et un autre avec +100. Expliquez comment un faible facteur de discount (γ proche de 0) influence le comportement de l’agent face à ces deux états.**

.....................................................................................................



### 4. Apprentissage **en ligne** vs **hors ligne** :

**Expliquez la différence entre une politique apprise en ligne et une politique apprise hors ligne. Donnez un exemple dans lequel une politique hors ligne pourrait échouer lorsqu’elle est appliquée à un environnement réel.**

**Pourquoi ce type d’échec survient-il ? Quelle approche recommandez-vous pour réduire cet écart entre entraînement hors ligne et déploiement réel ?**

> *Conseil et Astuce pour la réflexion : Vous pouvez vous appuyer sur des notions comme la non-stationnarité des données, ou le manque d’exploration active.*

.....................................................................................................

### 5. Environnement **statique vs dynamique** et **déterministe vs stochastique** :
**Comparez un environnement statique déterministe et un environnement dynamique stochastique. Décrivez un cas où une politique apprise dans un environnement statique échouerait lorsqu’elle est utilisée dans un environnement dynamique ou stochastique.**

**Quelle adaptation de la stratégie d’apprentissage recommandez-vous dans ce cas ? Justifiez votre réponse.**

> *Conseil et Astuce pour la réflexion : Pensez à des environnements où les probabilités de transition changent au fil du temps ou où certaines actions ont des effets aléatoires (ex. : météo, comportements humains, etc.).*

.....................................................................................................

# Optionnel:

### **1. Donnez un exemple d’environnement où l’équation de Bellman ne suffit pas pour résoudre le problème. Quelle approche alternative recommanderiez-vous ? Justifiez.**

.....................................................................................................

### **2. Supposons que vous entraîniez un agent avec Q-learning, mais que la Q-table converge vers des valeurs incohérentes. Listez trois causes probables de cette instabilité et proposez une solution concrète pour chacune.**

.....................................................................................................
