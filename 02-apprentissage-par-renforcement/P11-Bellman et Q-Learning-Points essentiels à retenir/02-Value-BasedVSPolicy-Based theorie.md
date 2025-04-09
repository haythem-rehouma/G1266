

# **Value-Based** ou **Policy-Based**



La différence entre **Value-Based** et **Policy-Based** en **apprentissage par renforcement** (Reinforcement Learning) peut sembler complexe, mais nous allons l’expliquer de manière claire à l’aide d’analogies et d’exemples concrets.

<br/>

### 1. **Value-Based Methods (Méthodes Basées sur les Valeurs)**

#### Concept

Dans les méthodes basées sur les valeurs, l'agent cherche à **évaluer les états** (ou les paires état-action) afin de déterminer quelle action est la meilleure à long terme. L'idée est de calculer une fonction de valeur qui donne une estimation de la récompense future attendue en étant dans un certain état et en suivant une stratégie donnée.

**Objectif** : Trouver la valeur optimale pour chaque état (ou chaque paire état-action), puis choisir les actions en conséquence.

<br/>

#### Exemple : **Q-Learning** et **Value Iteration**

- Dans **Q-Learning**, l'agent apprend une **fonction de valeur d'état-action** appelée la **fonction Q** qui estime les récompenses attendues en fonction de l'état et de l'action choisis.

- L'agent ne suit pas une stratégie explicite dès le départ. Il décide de ses actions en regardant les valeurs qu'il a apprises pour chaque action dans un état donné.

<br/>

#### Analogie

Imagine que tu es dans un labyrinthe. À chaque position, tu veux savoir à quel point c’est un bon endroit (en fonction de la distance de la sortie et des obstacles) et quelles actions t’amèneront plus probablement à la sortie. Tu évalues les positions et tu agis selon les estimations que tu as construites, sans stratégie préétablie.

<br/>

#### Résumé

- **Focus** sur la **valeur des états ou des actions**.

- L'agent **n'apprend pas une stratégie directement**, mais utilise les valeurs apprises pour guider ses décisions.

<br/>

---

### 2. **Policy-Based Methods (Méthodes Basées sur les Politiques)**

#### Concept

Dans les méthodes basées sur les politiques, l'agent apprend directement une **politique** ou **stratégie**. Une politique est une fonction qui détermine quelle action l’agent doit entreprendre dans chaque état.

Contrairement aux méthodes basées sur les valeurs, ici l'agent cherche à **optimiser directement la politique**, sans évaluer chaque état.

**Objectif** : Trouver la politique optimale, c’est-à-dire la meilleure stratégie qui indique directement l’action à prendre dans chaque état.

<br/>

#### Exemple : **REINFORCE** et **Policy Gradient**

- Dans **Policy Gradient**, l’agent ajuste directement sa stratégie en maximisant la récompense totale à travers les épisodes.

- Il apprend une fonction qui, pour chaque état, donne une distribution de probabilités sur les actions possibles.

<br/>

#### Analogie

Reprenant l’exemple du labyrinthe : cette fois, tu disposes d’un ensemble de règles (stratégie) te disant quoi faire à chaque endroit (tourner à gauche, continuer, etc.). Tu optimises ces règles au fur et à mesure pour atteindre la sortie, sans évaluer individuellement chaque position.

<br/>

#### Résumé

- **Focus** sur l’apprentissage d’une **politique** directement.

- L’agent **n’évalue pas les états**, il apprend **comment agir** dans chacun pour maximiser la récompense.

<br/>

---

### **Comparaison Résumée**

| **Caractéristique**            | **Value-Based**                                 | **Policy-Based**                                |
|-------------------------------|--------------------------------------------------|-------------------------------------------------|
| Qu’est-ce qui est appris ?    | Fonction de valeur (états ou actions)            | Politique (stratégie)                           |
| Exemple d’algorithme          | Q-Learning, Value Iteration                      | Policy Gradient, REINFORCE                      |
| Approche                      | Évaluer les actions pour choisir la meilleure    | Apprendre directement quelle action entreprendre|
| Stratégie ?                   | Déduite des valeurs                              | Apprise directement                             |

<br/>

---

### **Quand utiliser chaque méthode ?**

- **Value-Based** : Idéal pour des environnements **à espace d’actions discret**, comme des jeux à choix limités. Exemples : Q-Learning, Value Iteration.

- **Policy-Based** : Recommandé lorsque l’espace d’actions est **continu** (ex. : contrôle de robot, accélération, rotation), ou lorsqu’une stratégie fluide et flexible est nécessaire. Exemples : Policy Gradient, REINFORCE.

<br/>

---

### **Conclusion avec un Exemple Pratique**

Imagine que tu joues à un jeu vidéo :

- En **Value-Based**, tu tentes d’évaluer chaque situation pour choisir l’action qui t’apportera le plus de points à long terme.

- En **Policy-Based**, tu développes directement une règle comme : « si je suis dans cette situation, je saute immédiatement », sans calculer toutes les récompenses futures.

Les deux approches sont puissantes, mais chacune a son domaine d’application privilégié. Dans des environnements complexes ou continus, une approche basée sur les politiques peut s’avérer plus efficace.

