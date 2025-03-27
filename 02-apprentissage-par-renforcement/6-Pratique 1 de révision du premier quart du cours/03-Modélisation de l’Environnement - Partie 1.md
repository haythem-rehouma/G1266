------------------------------------------------------------------
# **Quiz - Comprendre les Types d’Environnements dans l'Apprentissage par Renforcement**
------------------------------------------------------------------


- Théorie : Voir la partie 02-Notions-au-RL (FAQ)
  
#### **Question 1 : Environnement Déterministe**
**Mise en situation** : Dans un jeu vidéo, un personnage doit atteindre un trésor. À chaque fois que le joueur appuie sur la touche pour avancer, le personnage se déplace toujours d'une case vers l'avant.

**Question :** Comment qualifier cet environnement ?
- A) Stochastique
- B) Dynamique
- C) Déterministe
- D) Non déterministe

---

#### **Question 2 : Environnement Stochastique**
**Mise en situation** : Un robot apprend à naviguer dans une pièce où des obstacles apparaissent et disparaissent de manière aléatoire. Même si le robot choisit la même direction à plusieurs reprises, le chemin peut être bloqué ou dégagé en fonction de la position aléatoire des obstacles.

**Question :** Comment qualifier cet environnement ?
- A) Dynamique
- B) Déterministe
- C) Stochastique
- D) Non déterministe

---

#### **Question 3 : Environnement Dynamique**
**Mise en situation** : Une voiture autonome roule sur une autoroute. Les autres voitures se déplacent constamment, et la voiture autonome doit s'adapter à la vitesse des véhicules autour d’elle pour éviter les collisions.

**Question :** Comment qualifier cet environnement ?
- A) Stochastique
- B) Dynamique
- C) Déterministe
- D) Non déterministe

---

#### **Question 4 : Environnement Non Déterministe**
**Mise en situation** : Dans un jeu de société, un joueur lance un dé à six faces. En fonction du chiffre obtenu, le joueur doit avancer d'un nombre de cases correspondant. Le résultat est incertain, mais toujours entre 1 et 6.

**Question :** Comment qualifier cet environnement ?
- A) Dynamique
- B) Non déterministe
- C) Déterministe
- D) Stochastique

---

#### **Question 5 : Environnement Statique**
**Mise en situation** : Un agent dans un simulateur de labyrinthe doit trouver son chemin jusqu'à la sortie. Aucune modification n’est apportée au labyrinthe une fois qu’il a été créé ; les murs et les obstacles restent en place tout au long de l'épisode.

**Question :** Comment qualifier cet environnement ?
- A) Statique
- B) Dynamique
- C) Stochastique
- D) Non déterministe

---

#### **Question 6 : Environnement Déterministe Dynamique**
**Mise en situation** : Un agent est chargé de ramasser des objets dans une usine robotisée. À chaque fois que l'agent prend une action, les tapis roulants dans l'usine se déplacent d'une manière prévisible et les objets avancent selon un modèle fixe.

**Question :** Comment qualifier cet environnement ?
- A) Déterministe Dynamique
- B) Stochastique Statique
- C) Dynamique Non déterministe
- D) Déterministe Statique

---

#### **Question 7 : Environnement Non Déterministe Dynamique**
**Mise en situation** : Un drone apprend à voler dans un environnement où la météo change régulièrement. Parfois, lorsqu’il choisit de monter, le vent change soudainement et le fait dévier de sa trajectoire. Cependant, ces changements sont influencés par le climat général de la région et ne sont pas complètement aléatoires.

**Question :** Comment qualifier cet environnement ?
- A) Non déterministe Dynamique
- B) Stochastique Statique
- C) Déterministe Dynamique
- D) Non déterministe Statique

---

### **Réponses**

1. **Question 1 :** C) Déterministe
   - **Explication** : Dans un environnement déterministe, chaque action a un résultat prévisible. Ici, chaque mouvement de l’agent déplace toujours le personnage d’une case vers l'avant.

2. **Question 2 :** C) Stochastique
   - **Explication** : Dans un environnement stochastique, le résultat d'une action est influencé par des éléments aléatoires. Ici, la position des obstacles change aléatoirement.

3. **Question 3 :** B) Dynamique
   - **Explication** : Un environnement dynamique change au fil du temps, indépendamment des actions de l'agent. Ici, la voiture autonome doit s’adapter aux changements constants dans le trafic.

4. **Question 4 :** B) Non déterministe
   - **Explication** : Un environnement non déterministe a des résultats incertains, mais dans des limites définies. Ici, le dé donne un résultat compris entre 1 et 6, mais le résultat exact est imprévisible.

5. **Question 5 :** A) Statique
   - **Explication** : Un environnement statique ne change pas avec le temps. Ici, le labyrinthe reste identique pendant toute la durée de l'épisode.

6. **Question 6 :** A) Déterministe Dynamique
   - **Explication** : Un environnement déterministe dynamique change au fil du temps de manière prévisible. Ici, les tapis roulants se déplacent de manière déterministe et le système est en mouvement constant.

7. **Question 7 :** A) Non déterministe Dynamique
   - **Explication** : L'environnement dynamique non déterministe combine des éléments incertains et en évolution constante, comme le vent qui influence le vol du drone de manière partiellement imprévisible.
