### **Étude de Cas 1 : Prévision des Températures pour les Cultures Agricoles**

Un groupe de chercheurs souhaite optimiser la production agricole en prévoyant les températures sur plusieurs mois. L'objectif est de fournir une estimation de température pour chaque jour à partir de données historiques afin de planifier les périodes de plantation et de récolte en fonction des prévisions climatiques.

**Question :** 
1. *Étant donné la nature de la prévision sur une série temporelle (chaque jour dépendant des précédents), recommanderiez-vous d'utiliser le TD-Learning ou la méthode Monte Carlo ? Justifiez votre choix.*
2. *Quelles seraient les limitations de la méthode que vous avez choisie pour ce type de prédiction climatique ?*

---

### **Étude de Cas 2 : Simulation de Ventes en Ligne avec Remises**

Un site e-commerce cherche à simuler les ventes pour différents scénarios de remises (réduction de prix). L'objectif est de prédire l'impact des remises sur les ventes en observant les comportements des clients lors de précédentes périodes de promotions.

**Question :**
1. *Si le site souhaite estimer la valeur moyenne des ventes au cours d'une promotion, quel algorithme recommanderiez-vous entre Monte Carlo et TD-Learning ?*
2. *Quelles seraient les raisons d’éviter l’autre méthode dans ce cas précis ?*

---

### **Étude de Cas 3 : Prévision des Événements Météorologiques Extrêmes**

Une organisation météorologique souhaite créer un modèle pour estimer la probabilité d’événements extrêmes (ex. tempêtes ou vagues de chaleur) en fonction des données des dernières années. Avec l’intensification des phénomènes météorologiques due au changement climatique, ils veulent un modèle adaptable qui prend en compte les extrêmes croissants.

**Question :**
1. *Entre Monte Carlo et TD-Learning, lequel recommanderiez-vous pour prévoir des événements extrêmes en fonction de tendances annuelles ? Expliquez comment la méthode choisie pourrait s’adapter aux changements dans les tendances climatiques.*
2. *Quel pourrait être un inconvénient de la méthode choisie dans ce cas ?*

---

### **Étude de Cas 4 : Navigation d'un Robot dans un Entrepôt**

Un robot est programmé pour déplacer des marchandises dans un entrepôt. Il reçoit des récompenses en fonction de la distance parcourue et des obstacles évités, et doit optimiser son trajet. Les environnements peuvent être différents d’un trajet à l’autre, car les obstacles changent de position.

**Question :**
1. *Pour un environnement où chaque trajet est unique, est-il plus judicieux d’utiliser le TD-Learning ou Monte Carlo ? Justifiez votre choix en expliquant la manière dont le modèle utiliserait les informations des épisodes passés.*
2. *Quelles seraient les conditions dans lesquelles l’autre méthode serait plus efficace ?*

---

### **Étude de Cas 5 : Prévision des Comportements d'Achat des Consommateurs**

Une entreprise souhaite modéliser les comportements d’achat des consommateurs au fil du temps pour maximiser les profits en s’adaptant aux changements dans les habitudes de consommation. Elle dispose de données sur les achats historiques, et chaque nouvel achat est influencé par les actions précédentes de la campagne marketing.

**Question :**
1. *Dans ce contexte, recommanderiez-vous d’utiliser TD-Learning ou Monte Carlo pour modéliser les comportements d’achat au fil du temps ? Expliquez votre choix.*
2. *Quel avantage aurait votre méthode pour s’adapter à des habitudes de consommation évoluant constamment ?*

---

### **Évaluation**

Pour chaque étude de cas :
1. **Justifier votre choix** entre Monte Carlo et TD-Learning, en mentionnant les caractéristiques spécifiques de chaque méthode qui les rendent plus adaptées.
2. **Identifier les limitations de la méthode choisie**, en expliquant dans quels contextes elle pourrait être moins efficace.
3. **Proposer des améliorations** ou des adaptations à la méthode choisie, si nécessaire, pour améliorer les performances dans chaque cas.

Ces questions vous permettront de vérifier si vous avez bien compris que :
- **Monte Carlo** est plus adapté quand des épisodes complets sont disponibles et peuvent être analysés en moyenne (meilleur pour des événements indépendants, sans dépendance temporelle immédiate).
- **TD-Learning** convient mieux dans les environnements où une mise à jour progressive est utile pour s’adapter aux changements continus dans les séquences de données, surtout quand les informations de chaque étape sont précieuses pour ajuster l’apprentissage de manière incrémentale.
