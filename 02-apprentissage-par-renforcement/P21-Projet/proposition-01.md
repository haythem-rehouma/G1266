# **Projet 1 – Apprentissage par renforcement avec un agent DQN**

## **Objectif du projet**

Ce projet a pour but de vous familiariser avec les principes de l’apprentissage par renforcement, à travers l’implémentation d’un agent basé sur l’algorithme DQN (Deep Q-Network). L’agent devra apprendre à interagir avec un environnement de type jeu Atari — tel que **Pong** — en optimisant ses décisions grâce à un réseau neuronal profond.

---

## **Description générale**

### 1. Principes fondamentaux

L’apprentissage par renforcement repose sur l’interaction entre un agent et un environnement. À chaque étape, une action est entreprise, une récompense est reçue, et une nouvelle observation est produite. L’objectif est d’apprendre une stratégie optimale maximisant les récompenses cumulées. Le jeu Atari fournira ici un environnement interactif propice à l’expérimentation.

### 2. Composantes essentielles

* **Prétraitement des observations** : Les images issues du jeu doivent être converties en niveaux de gris, redimensionnées, puis empilées afin de modéliser la dynamique temporelle.
* **Réseau neuronal convolutif (CNN)** : Un modèle convolutif est utilisé pour interpréter visuellement l’état de l’environnement et déterminer l’action optimale.
* **Mémoire de relecture (Replay Buffer)** : Une mémoire est utilisée pour stocker des transitions \$(s, a, r, s')\$ et entraîner le réseau sur des échantillons aléatoires, réduisant ainsi la corrélation entre les données.
* **Exploration vs exploitation** : Une stratégie d’exploration contrôlée (ex. \$\epsilon\$-greedy) permet d’équilibrer la découverte de nouvelles actions et l’exploitation des connaissances acquises.

### 3. Environnement d’apprentissage

La bibliothèque **OpenAI Gym** est utilisée pour simuler l’environnement. Des wrappers spécifiques permettent d’améliorer la qualité des données en simplifiant les observations ou en ajustant la fréquence des frames.

---

## **Méthodologie proposée**

### Étape 1 – Configuration de l’environnement

* Charger un jeu Atari (ex. : Pong) à l’aide de `gym.make()`.
* Appliquer une série de wrappers pour :

  * convertir les images en niveaux de gris,
  * les redimensionner à une taille standard (ex. : 84×84),
  * empiler plusieurs images successives pour capturer le mouvement.

### Étape 2 – Conception de l’agent DQN

* Implémenter un réseau convolutif prenant en entrée une pile d’images.
* Approcher la fonction \$Q(s, a)\$ à l’aide de ce réseau.
* Définir les fonctions de perte, de mise à jour, et d’optimisation des poids.

### Étape 3 – Entraînement de l’agent

* Simuler de multiples épisodes de jeu.
* Enregistrer les transitions dans la mémoire de relecture.
* Tirer des mini-batchs pour entraîner le réseau à partir d’expériences passées.
* Ajuster les hyperparamètres (taux d’apprentissage, facteur \$\gamma\$, valeur de \$\epsilon\$, taille de la mémoire, etc.).

### Étape 4 – Évaluation des performances

* Évaluer les performances de l’agent sur des épisodes de test.
* Mesurer la récompense moyenne, la stabilité des comportements, et la capacité d’apprentissage.

---

## **Livrables attendus**

1. **Code source complet**
   Le code doit inclure :

   * la configuration de l’environnement,
   * l’implémentation du modèle DQN,
   * la procédure d’entraînement et d’évaluation.

2. **Rapport technique**
   Le rapport doit présenter :

   * les choix méthodologiques (modèle, hyperparamètres, stratégie d’exploration),
   * une analyse critique des résultats obtenus,
   * des propositions d’amélioration.

3. **Démonstration obligatoire**
   Une **vidéo ou une démonstration fonctionnelle** doit être fournie pour illustrer le comportement de l’agent après entraînement. Cette démonstration constitue une partie essentielle de l’évaluation du projet.

---

## **Intérêt pédagogique**

Ce projet permet de mettre en œuvre un algorithme d’apprentissage par renforcement profond appliqué à une tâche concrète. La méthode DQN, au croisement du deep learning et de la prise de décision séquentielle, est utilisée dans des secteurs aussi divers que la robotique, la conduite autonome ou les systèmes de recommandation. Les compétences développées sont transférables à de nombreux contextes professionnels.

---

## **Ressources recommandées**

* [OpenAI Gym](https://www.gymlibrary.dev)
* [Article fondateur – Playing Atari with Deep Reinforcement Learning (DeepMind)](https://arxiv.org/abs/1312.5602)
* [Documentation Keras](https://keras.io)


