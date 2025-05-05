# Architecture technique du DQN 
---

# **1. Introduction : Comment DQN est structuré ?**

Dans les documents précédents, nous avons vu pourquoi DQN est important et comment il apprend. Maintenant, il est temps d’explorer **les composants techniques** qui rendent DQN si puissant. Comprendre ces composants est essentiel pour maîtriser le fonctionnement interne de l’algorithme et son efficacité.

---

# **2. Les composants clés de DQN**

Pour que DQN fonctionne efficacement, il repose sur **trois innovations majeures** qui résolvent les défis des approches classiques d’apprentissage par renforcement. Voici ces innovations en détail :

---

### **2.1 Replay Memory (Mémoire de répétition)**

#### **Pourquoi est-elle nécessaire ?**
- Dans les approches classiques, l’agent apprend directement à partir des expériences qu’il vit à chaque étape.
- Cela pose un problème car **les expériences successives sont fortement corrélées** (elles dépendent de l’état précédent).
- Ces corrélations rendent l’apprentissage instable.

#### **Solution : Stocker et réutiliser les expériences**
- La mémoire de répétition est une **file de stockage** où l’agent enregistre ses expériences passées, sous la forme :  
  *(état, action, récompense, état suivant, fait)*.  
  Exemple :  
  > (Serpent à [3,3], va à gauche, +10, Serpent à [3,2], "fini=False")

#### **Comment ça marche ?**
1. **L’agent joue** et enregistre ses expériences dans cette mémoire.
2. Lors de l’entraînement, les expériences sont **prélevées aléatoirement** dans cette mémoire.
3. Cela permet de **casser les corrélations temporelles** et de stabiliser l’apprentissage.

#### **Avantage clé : Réutiliser les données**
- L’agent peut rejouer des expériences passées pour apprendre mieux et plus vite.
- Cela permet de maximiser l’efficacité des données collectées.

#### **Représentation graphique** :  
Imagine une mémoire circulaire avec une capacité fixe (exemple : 1 million d’expériences). Une fois pleine, les nouvelles expériences écrasent les plus anciennes.

---

### **2.2 Target Network (Réseau cible)**

#### **Pourquoi est-il nécessaire ?**
- Dans l’algorithme Q-Learning classique, l’estimation des valeurs Q dépend de l’état actuel et des poids du réseau.
- Si ces poids changent à chaque étape d’apprentissage, cela peut créer des **oscillations instables** et rendre l’apprentissage imprévisible.

#### **Solution : Introduire un réseau cible (Target Network)**
- Plutôt que de mettre à jour les valeurs Q directement avec le réseau principal, un **réseau secondaire** (cible) est utilisé pour calculer les cibles de mise à jour.
- Ce réseau cible est mis à jour **périodiquement** pour suivre lentement le réseau principal.

#### **Comment ça marche ?**
1. On utilise le réseau cible pour calculer la valeur Q future (la "cible").
2. Le réseau principal est entraîné en minimisant la différence entre sa prédiction et cette cible.
3. Toutes les *N* étapes, les poids du réseau principal sont copiés dans le réseau cible.

#### **Avantage clé : Stabilisation de l’apprentissage**
- En utilisant un réseau cible stable, l’agent évite les fluctuations trop brusques pendant l’entraînement.

#### **Représentation graphique** :  
1. Réseau principal (Main Network) : utilisé pour prendre des décisions.  
2. Réseau cible (Target Network) : utilisé uniquement pour calculer les cibles des valeurs Q.

---

### **2.3 Processus de prélevage aléatoire**

#### **Pourquoi est-il nécessaire ?**
- Sans prélèvement aléatoire, l’agent risque d’apprendre des biais basés sur l’ordre des données (par exemple, des actions répétées sur une série d’états similaires).

#### **Comment ça marche ?**
- Lors de chaque mise à jour, un mini-lot (*batch*) d’expériences est sélectionné **au hasard** depuis la mémoire de répétition.
- Cela crée une diversité dans les données utilisées pour entraîner le réseau.

#### **Avantage clé : Apprentissage plus robuste**
- En combinant des expériences variées, l’agent apprend à généraliser au lieu de se sur-adapter à des situations spécifiques.

---

# **3. Architecture réseau du DQN**

### **3.1 Structure d’un réseau DQN typique**
Dans un jeu Atari, chaque **image du jeu** est convertie en entrée pour un réseau de neurones. Voici les étapes principales :

1. **Entrée : Une image de l’état actuel**
   - Une capture d’écran (par exemple, 84x84 pixels en niveaux de gris).
   - Plusieurs images consécutives peuvent être empilées pour capturer le mouvement (4 frames, par exemple).

2. **Traitement : Réseau convolutionnel**
   - Une série de **couches convolutionnelles** pour extraire les caractéristiques importantes (comme la position des obstacles et des objets à éviter).

3. **Prédiction : Couche entièrement connectée**
   - Une ou plusieurs couches entièrement connectées prennent les caractéristiques extraites et produisent les **valeurs Q** pour chaque action possible.

#### **Représentation d’un réseau typique (pour un jeu Atari)**
- **Entrée** : Une image 84x84x4 (4 frames empilées).  
- **Couches convolutionnelles** :  
  - 32 filtres 8x8 avec un pas de 4.  
  - 64 filtres 4x4 avec un pas de 2.  
  - 64 filtres 3x3 avec un pas de 1.  
- **Couches entièrement connectées** :  
  - Une couche dense avec 512 unités.  
  - Une sortie avec autant de neurones que d’actions possibles dans le jeu (exemple : gauche, droite, sauter).  

---

### **3.2 Fonction de perte utilisée**
- La fonction de perte mesure la différence entre :  
  1. La prédiction actuelle des valeurs Q.  
  2. La valeur cible calculée grâce au réseau cible.  
- Perte utilisée : **Mean Squared Error (MSE)**  
  > ![image](https://github.com/user-attachments/assets/5a35dfd8-f510-44fd-b50d-bfc8752a5445)


---

# **4. Étapes complètes pour entraîner un DQN**

Voici le processus global d’entraînement d’un DQN :

1. **Initialiser le réseau principal et le réseau cible.**
2. **Initialiser la mémoire de répétition (Replay Memory).**
3. **Pour chaque épisode :**
   - Observer l’état actuel.
   - Choisir une action (**exploration vs exploitation**).
   - Exécuter l’action, observer la récompense et l’état suivant.
   - Stocker l’expérience dans la mémoire.
   - **Prélever un mini-lot** depuis la mémoire pour l’entraînement.
   - Calculer la cible avec le réseau cible.
   - Mettre à jour les poids du réseau principal en réduisant l’erreur.
   - Toutes les *N* étapes, mettre à jour le réseau cible.

---

# **5. Avantages combinés des innovations techniques**

1. **Replay Memory** : Brise les corrélations et améliore la stabilité.  
2. **Target Network** : Stabilise l’apprentissage en évitant des changements trop brusques.  
3. **Prélèvement aléatoire** : Permet un apprentissage diversifié et robuste.

Ces innovations sont ce qui rend DQN **scalable** et **efficace** dans des environnements complexes comme les jeux Atari.

---

# **6. Visualisation pour les étudiants**

Créer un schéma simple montrant :  
1. La boucle d’interaction (environnement, mémoire, réseaux).  
2. La différence entre réseau principal et réseau cible.  
3. L’utilisation de Replay Memory.

---

# **7. Conclusion**

Grâce à ces composants techniques, DQN a permis de révolutionner l’apprentissage par renforcement dans des environnements complexes. Dans le prochain document, nous passerons à **l’implémentation pratique** d’un DQN pour jouer à un jeu Atari. Restez prêts à coder !
