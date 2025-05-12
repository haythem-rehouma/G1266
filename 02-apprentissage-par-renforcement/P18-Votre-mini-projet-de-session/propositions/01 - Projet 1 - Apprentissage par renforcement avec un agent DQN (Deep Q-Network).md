# **Projet 1 : Apprentissage par renforcement avec un agent DQN (Deep Q-Network)**

# **Objectif :**

Dans ce projet, vous allez explorer l'apprentissage par renforcement en développant un agent capable de jouer à un jeu Atari, comme **Pong**, en apprenant de ses propres actions. Votre mission sera d'implémenter et de former un modèle de Deep Q-Network (DQN), un algorithme qui utilise un réseau neuronal profond pour prendre des décisions optimales dans un environnement dynamique.

---

# **Description détaillée :**

1. **Concept de base :**  
   L’apprentissage par renforcement repose sur l’idée d’un agent qui interagit avec un environnement, prend des actions et reçoit des récompenses. L’objectif de l’agent est de maximiser les récompenses cumulées en apprenant une stratégie optimale. Ici, le jeu Atari servira d’environnement interactif.

2. **Composantes principales :**  
   - **Prétraitement des observations** : Les images du jeu seront converties en niveaux de gris, redimensionnées et empilées pour capturer les dynamiques temporelles.  
   - **Réseau neuronal convolutif (CNN)** : Ce réseau analysera les observations visuelles pour prédire les actions les plus avantageuses.  
   - **Mémoire de relecture (Replay Memory)** : Une technique clé qui permet à l’agent d’apprendre à partir d’expériences passées en stockant des transitions (états, actions, récompenses, états suivants).  
   - **Exploration et exploitation** : Votre agent devra équilibrer ces deux aspects pour explorer l’environnement tout en exploitant ce qu’il a déjà appris.

3. **Environnement :**  
   Vous utiliserez **OpenAI Gym** pour interagir avec le jeu. L’environnement sera modifié avec des wrappers pour améliorer l’efficacité de l’apprentissage (par exemple, réduction de la complexité des observations).

---

# **Étapes à suivre :**

1. **Créer et configurer l'environnement :**  
   - Charger un jeu Atari à l’aide de Gym.
   - Implémenter des wrappers pour prétraiter les observations (conversion en niveaux de gris, redimensionnement, empilement des états).

2. **Implémenter l'agent DQN :**  
   - Construire un réseau neuronal convolutif qui prend en entrée les images de l’environnement.
   - Utiliser l’algorithme DQN pour approximer la fonction Q et optimiser les décisions de l’agent.

3. **Former l'agent :**  
   - Lancer des simulations où l’agent joue au jeu.
   - Stocker les expériences dans la mémoire de relecture et les utiliser pour l’entraînement.
   - Ajuster les hyperparamètres pour améliorer les performances (taux d’apprentissage, epsilon, etc.).

4. **Évaluer les performances :**  
   - Tester l’agent après l’entraînement pour voir sa progression.
   - Mesurer des métriques telles que les récompenses cumulées ou le taux de réussite.

---

# **Résultats attendus :**

1. **Code complet et fonctionnel** :  
   Votre implémentation doit inclure un environnement correctement configuré, un agent DQN entraîné, et une évaluation des performances.

2. **Rapport d'analyse :**  
   - Expliquez vos choix techniques (réseaux, hyperparamètres, méthode d’entraînement).  
   - Analysez les résultats : où l’agent a-t-il réussi ? Où a-t-il échoué ? Comment pourrait-il être amélioré ?

3. **Démo (optionnel)** :  
   Une vidéo ou une démonstration en direct montrant l’agent jouant au jeu.

---

# **Pourquoi ce projet est important :**

Ce projet est une introduction concrète à l’un des concepts les plus influents de l’intelligence artificielle moderne. L’apprentissage par renforcement est utilisé dans des domaines variés, des véhicules autonomes à la robotique en passant par la finance. Ce que vous apprendrez ici peut être appliqué bien au-delà du jeu.

---

# **Ressources utiles :**
- OpenAI Gym : [https://www.gymlibrary.dev](https://www.gymlibrary.dev)  
- Tutoriel DQN de DeepMind : ["Playing Atari with Deep Reinforcement Learning"](https://arxiv.org/abs/1312.5602)  
- Documentation Keras : [https://keras.io](https://keras.io)  
