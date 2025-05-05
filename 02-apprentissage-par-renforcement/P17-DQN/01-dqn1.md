# Introduction
----------------

# **1. C’est quoi DQN et pourquoi c’est important ?**

#### **Imagine un jeu vidéo**
Supposons que tu joues à un jeu où tu contrôles un personnage (par exemple, un serpent dans le jeu "Snake"). Ton objectif est de collecter des pommes tout en évitant de toucher les murs ou de te mordre la queue. Chaque fois que tu manges une pomme, tu gagnes des points. Chaque fois que tu fais une erreur (toucher un mur), c’est game over.

#### **L’apprentissage profond (Deep Learning) pour jouer**
Maintenant, imagine qu’on veut construire un programme qui joue à ce jeu tout seul, comme un pro. Le programme doit apprendre **tout seul** comment jouer, simplement en essayant encore et encore. C’est ici qu’intervient **DQN**, ou **Deep Q-Learning Network**.

#### **DQN, c’est quoi ?**
- C’est une méthode d’intelligence artificielle (IA) qui permet à un programme d’apprendre à prendre des décisions dans un environnement, comme jouer à un jeu vidéo.
- Il combine deux idées :
  1. **Q-Learning** : Une technique classique d’apprentissage par renforcement (on va l’expliquer dans une minute).
  2. **Réseaux de neurones profonds (Deep Neural Networks)** : Une technique utilisée pour traiter des données complexes, comme des images.

---

# **2. Avant DQN : L’idée de base du Q-Learning**

#### **C’est quoi le Q-Learning ?**
C’est une méthode d’apprentissage par renforcement où :
- **Un agent** (le joueur dans notre cas) explore un environnement (le jeu).
- **Il prend des décisions** (se déplacer à gauche, à droite, en haut ou en bas).
- **Il reçoit une récompense** pour ses actions (par exemple, +10 pour manger une pomme, -50 pour toucher un mur).
- **Son objectif ?** Maximiser le total des récompenses sur le long terme.

#### **Une table pour mémoriser les choix**
Dans le Q-Learning classique, l’agent utilise une **table** (appelée "table Q") pour se souvenir de la valeur de chaque action possible dans chaque situation. Voici à quoi cela ressemble :

| État actuel      | Action       | Valeur Q (Qualité) |
|------------------|--------------|--------------------|
| Serpent va en haut | Aller à gauche | +10               |
| Serpent va à droite | Aller à droite | -50               |

Le problème ? Quand le jeu devient complexe (par exemple, des centaines de milliers d’états possibles), cette table devient énorme. Impossible de tout mémoriser !

---

# **3. Pourquoi DQN est une amélioration ?**

#### **Remplacer la table Q par un réseau de neurones**
Plutôt que de mémoriser toutes les combinaisons possibles dans une table, on utilise un **réseau de neurones**. Ce réseau apprend à **prédire** la valeur Q des actions possibles à partir des informations qu’il reçoit.

Exemple : Si le serpent voit une pomme en haut, le réseau apprend à dire que "monter" est une bonne action.

#### **À quoi ça ressemble ?**
- L’entrée du réseau : une image ou une description de l’état actuel (par exemple, le jeu vu comme une grille).
- La sortie du réseau : les valeurs Q pour chaque action possible (gauche, droite, haut, bas).

---

# **4. Étape par étape : Comment DQN apprend ?**

#### **Étape 1 : Explorer et jouer**
L’agent commence par jouer au hasard. Il essaye différentes actions pour découvrir ce qui fonctionne ou non.

#### **Étape 2 : Obtenir des récompenses**
Chaque fois qu’il fait une action, il reçoit une récompense :
- Une récompense positive (par exemple, +10 pour manger une pomme).
- Une récompense négative (par exemple, -50 pour se heurter à un mur).

#### **Étape 3 : Mettre à jour les prédictions**
Le réseau de neurones apprend de ses erreurs :
- Si une action a donné une bonne récompense, le réseau apprendra à augmenter la valeur Q pour cette action.
- Si une action a conduit à un échec, le réseau diminue la valeur Q pour cette action.

#### **Étape 4 : Répéter**
L’agent joue des milliers, voire des millions de parties, et améliore peu à peu ses décisions grâce aux données accumulées.

---

# **5. Visualisation simple : Comment DQN apprend au fil du temps**

Imagine un enfant qui apprend à marcher :
1. **Au début**, il tombe souvent (comme l’agent qui prend de mauvaises décisions).
2. **Petit à petit**, il découvre que certains mouvements (par exemple, avancer une jambe à la fois) fonctionnent mieux.
3. **Avec de la pratique**, il devient plus habile et finit par marcher correctement. Pour DQN, c’est pareil !

---

# **6. Les défis de DQN**
Même si ça a l’air simple :
1. **L’exploration vs. l’exploitation** : L’agent doit décider s’il continue d’explorer de nouvelles stratégies ou s’il exploite celles qui fonctionnent déjà.
2. **Les réseaux de neurones** peuvent devenir instables ou apprendre lentement si les données ne sont pas bien gérées.

---

# **7. Applications de DQN**
- Jouer à des jeux comme Atari, où il a battu des humains sur des dizaines de jeux.
- Contrôler des robots pour qu’ils apprennent à marcher ou manipuler des objets.
- Résoudre des problèmes complexes comme la gestion d’énergie ou la navigation.
