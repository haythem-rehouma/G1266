------------------------------------------------------------------
# **Quiz - Comprendre les États, Actions, et Récompenses dans l'Apprentissage par Renforcement**
------------------------------------------------------------------

- Théorie : Voir la partie 02-Notions-au-RL (FAQ)
  
#### **Question 1 : États**
**Mise en situation** : Un robot se trouve dans un entrepôt. Il peut se déplacer dans différentes zones de stockage pour chercher des boîtes. Chaque zone de l'entrepôt est définie par une position unique.

**Question :** Qu'est-ce qu'un **état** dans cette situation ?
- A) La décision de se déplacer vers une nouvelle zone.
- B) La position actuelle du robot dans l'entrepôt.
- C) Le nombre de boîtes que le robot a collectées.
- D) La direction vers laquelle le robot se dirige.

---

#### **Question 2 : Actions**
**Mise en situation** : Dans un jeu vidéo, un personnage doit ramasser des objets. À chaque instant, il peut choisir de se déplacer vers le haut, le bas, la gauche ou la droite.

**Question :** Quelle est l'**action** que le personnage peut effectuer dans cette situation ?
- A) Ramasser un objet.
- B) Se déplacer vers une direction (haut, bas, gauche ou droite).
- C) Gagner une vie supplémentaire.
- D) Sauvegarder sa progression dans le jeu.

---

#### **Question 3 : Récompenses**
**Mise en situation** : Un drone apprend à voler à travers des obstacles. Lorsqu'il évite un obstacle, il reçoit un point positif (+1). S'il entre en collision avec un obstacle, il perd un point (-1).

**Question :** Quelle est la **récompense** dans cette situation ?
- A) La vitesse à laquelle le drone se déplace.
- B) Le nombre d'obstacles que le drone a évités.
- C) Le point gagné (+1) ou perdu (-1) après avoir évité ou heurté un obstacle.
- D) La durée pendant laquelle le drone reste en vol.

---

#### **Question 4 : Transitions**
**Mise en situation** : Un joueur déplace son personnage dans un labyrinthe. Le personnage passe d'une case à une autre en fonction de la direction choisie (haut, bas, gauche ou droite).

**Question :** Qu'est-ce qu'une **transition** dans cette situation ?
- A) Le joueur choisit la direction dans laquelle se déplacer.
- B) Le passage d'une case à une autre après avoir pris une direction.
- C) La victoire du joueur à la fin du labyrinthe.
- D) Le temps que le joueur met pour terminer le labyrinthe.

---

#### **Question 5 : Politique**
**Mise en situation** : Dans un jeu, un robot doit collecter des diamants tout en évitant des zones dangereuses. Le robot peut choisir différentes stratégies pour se déplacer et maximiser le nombre de diamants collectés.

**Question :** Qu'est-ce que la **politique** du robot dans cette situation ?
- A) Le nombre de diamants que le robot a collectés.
- B) Les directions dans lesquelles le robot se déplace pour collecter les diamants.
- C) La stratégie que le robot suit pour maximiser ses récompenses en collectant des diamants et en évitant les zones dangereuses.
- D) La vitesse à laquelle le robot se déplace.

---

#### **Question 6 : Exemple d'un épisode**
**Mise en situation** : Un agent robot commence à un point de départ dans une pièce et doit naviguer pour atteindre une sortie. En chemin, il peut rencontrer des obstacles ou des objets à collecter.

**Question :** Qu'est-ce qu'un **épisode** dans cette situation ?
- A) Le parcours complet de l'agent depuis le point de départ jusqu'à la sortie.
- B) La direction prise par l'agent à un instant donné.
- C) Le nombre d'obstacles rencontrés par l'agent.
- D) La distance totale parcourue par l'agent.

---

#### **Question 7 : Exploration vs Exploitation**
**Mise en situation** : Un robot doit apprendre à choisir entre deux chemins pour aller à un objectif. Le premier chemin est plus court mais a une forte probabilité de rencontrer un obstacle. Le second chemin est plus long mais sans obstacle.

**Question :** Que signifie **explorer** dans cette situation ?
- A) Choisir le chemin déjà connu qui maximise les récompenses.
- B) Essayer différents chemins pour découvrir lequel est le meilleur.
- C) Éviter les obstacles à tout prix.
- D) Arrêter de chercher une solution.

---

### **Réponses**

1. **Question 1 :** B) La position actuelle du robot dans l'entrepôt.
   - **Explication** : Un état représente la situation actuelle du robot, ici sa position dans l'entrepôt.

2. **Question 2 :** B) Se déplacer vers une direction (haut, bas, gauche ou droite).
   - **Explication** : Une action représente une décision que l'agent (ici le personnage) prend pour interagir avec l'environnement, comme se déplacer dans une direction donnée.

3. **Question 3 :** C) Le point gagné (+1) ou perdu (-1) après avoir évité ou heurté un obstacle.
   - **Explication** : La récompense est le feedback que l'agent (le drone) reçoit après avoir pris une action, ici, éviter ou toucher un obstacle.

4. **Question 4 :** B) Le passage d'une case à une autre après avoir pris une direction.
   - **Explication** : Une transition représente le changement d'état (ici, la case) en fonction de l'action effectuée.

5. **Question 5 :** C) La stratégie que le robot suit pour maximiser ses récompenses en collectant des diamants et en évitant les zones dangereuses.
   - **Explication** : La politique est la stratégie globale que l'agent (le robot) suit pour choisir les actions qui lui rapporteront le plus de récompenses à long terme.

6. **Question 6 :** A) Le parcours complet de l'agent depuis le point de départ jusqu'à la sortie.
   - **Explication** : Un épisode correspond à un cycle complet d'interactions de l'agent avec l'environnement, de l'état initial jusqu'à un état terminal (ici, la sortie).

7. **Question 7 :** B) Essayer différents chemins pour découvrir lequel est le meilleur.
   - **Explication** : Explorer signifie essayer de nouvelles actions pour découvrir de nouvelles informations sur l'environnement, ici tester plusieurs chemins pour identifier celui qui rapporte le plus de récompenses.

