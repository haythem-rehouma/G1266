


# Cycle de vie en **apprentissage par renforcement (RL)**

# 1 - Cycle de vie d’un projet en apprentissage **supervisé** / **non supervisé**

### **Apprentissage supervisé**

1. **Collecte des données** (ex. : images de chats/chiens avec étiquettes)
2. **Prétraitement des données** (nettoyage, normalisation)
3. **Séparation en train/test**
4. **Choix du modèle** (régression, SVM, réseau de neurones…)
5. **Entraînement sur des données labellisées**
6. **Évaluation (accuracy, F1, etc.)**
7. **Déploiement du modèle**

### **Apprentissage non supervisé**

1. **Collecte des données** (sans étiquettes)
2. **Prétraitement**
3. **Choix du modèle (k-means, PCA...)**
4. **Entraînement basé sur des patterns**
5. **Évaluation via des métriques indirectes (silhouette, etc.)**
6. **Interprétation des clusters/composantes**
7. **Utilisation/déploiement**



# 2 - **Apprentissage par renforcement (RL)**

Là où ça change radicalement, c’est que **le modèle interagit avec un environnement**, il n’a **aucune donnée au début**, il **explore** par essais-erreurs.

Voici les **7 étapes du cycle RL** illustrées avec l'exemple **CartPole (DQN)** :



### **1. Formulate Problems**

> **Que cherche-t-on à faire ?**
> Ex : Garder un poteau en équilibre sur un chariot (CartPole).



### **2. Create Environment**

> **Où agit l’agent ?**
> Ex : On utilise un environnement comme `CartPole-v1` dans OpenAI Gym.
>
> * Observation : position, vitesse, angle
> * Actions possibles : gauche ou droite


### **3. Define Reward**

> **Qu’est-ce qui est considéré comme "bon" ?**
>
> * +1 à chaque timestep où le poteau est encore debout
> * 0 si le poteau tombe ou sort de l’écran



### **4. Create Agent**

> C’est **l’intelligence artificielle** qui va apprendre.
> Ex : un réseau de neurones (DQN) avec :
>
> * Des couches denses
> * Une fonction de prédiction des Q-valeurs : `Q(s, a)`
> * Un mécanisme d’exploration (`ε-greedy`)



### **5. Train Agent**

> L’agent agit dans l’environnement, reçoit des récompenses, apprend :
>
> * Il stocke ses expériences (états, actions, récompenses)
> * Il rejoue les expériences (experience replay)
> * Il ajuste ses poids avec l'équation de Bellman :
>
> > $Q(s,a) = r + \gamma \max_{a'} Q(s', a')$



### **6. Validate Agent**

> Évalue si l’agent **a vraiment appris** :
>
> * Combien de temps il garde le poteau droit ?
> * Courbes de récompense moyenne
> * Courbe de `ε` (exploration)



### **7. Deploy Policy**

> Si l’agent est performant :
>
> * On **déploie sa politique** dans un robot, un jeu, ou un simulateur.
> * Il n’a **plus besoin d’apprendre**, il **agit** directement.

##  Différences essentielles entre supervisé et RL

| Aspect        | Supervisé                      | Renforcement                         |
| ------------- | ------------------------------ | ------------------------------------ |
| Données       | Disponibles dès le début       | Générées par interaction             |
| Apprentissage | À partir d’exemples labellisés | Par essais-erreurs                   |
| Objectif      | Minimiser une erreur           | Maximiser une récompense             |
| Évaluation    | Sur un dataset de test         | Par performance dans l’environnement |
| Environnement | Aucun                          | Nécessaire (simulation ou réel)      |
| Exploration   | Inexistante                    | Cruciale (ε-greedy, etc.)            |






# 03 - **Table comparative : Supervisé / Non supervisé / Renforcement**

| **Étape**                     | **Apprentissage Supervisé**                        | **Apprentissage Non Supervisé**                        | **Apprentissage par Renforcement (RL)**                         |
| ----------------------------- | -------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------- |
| **1. Objectif**               | Prédire des étiquettes connues à partir d’exemples | Trouver des structures cachées dans les données        | Maximiser une récompense par interaction avec l’environnement   |
| **2. Données**                | Données labellisées                                | Données non labellisées                                | Aucune donnée initiale, explorées au fil du temps               |
| **3. Source de vérité**       | Étiquettes fournies (vérité terrain)               | Pas de vérité terrain explicite                        | Récompense reçue après action                                   |
| **4. Type d’apprentissage**   | Supervisé                                          | Non supervisé                                          | Par essais-erreurs (exploration vs exploitation)                |
| **5. Modèle utilisé**         | Régression, SVM, Réseaux de neurones, etc.         | K-means, PCA, clustering hiérarchique                  | DQN, PPO, A3C, SAC, etc.                                        |
| **6. Environnement**          | Aucun environnement                                | Aucun environnement                                    | Environnement dynamique (ex. CartPole, DeepRacer…)              |
| **7. Interaction**            | Pas d’interaction — modèle passif                  | Pas d’interaction — modèle passif                      | Agent actif : agit, observe, apprend                            |
| **8. Données de test**        | Test sur un jeu de données séparé                  | Validation difficile (métriques indirectes)            | Testé dans l’environnement avec métriques de performance        |
| **9. Boucle d’apprentissage** | Données → Modèle → Prédiction → Évaluation         | Données → Clustering → Évaluation visuelle ou métrique | Agent → Action → Récompense → Mise à jour de la politique       |
| **10. Validation**            | Accuracy, F1-score, etc.                           | Silhouette, Davies-Bouldin, etc.                       | Moyenne de récompense, durée de survie, taux de succès          |
| **11. Déploiement**           | Modèle prédictif prêt à l’emploi                   | Segments ou réductions dimensionnelles utilisées       | Politique entraînée (policy) déployée dans l’environnement réel |
| **12. Difficultés typiques**  | Overfitting, sous-apprentissage                    | Interprétation des résultats                           | Instabilité, exploration excessive, sparsité des récompenses    |
| **13. Besoin de labels**      | Oui                                                | Non                                                    | Non (récompense au lieu de label)                               |
| **14. Exemple concret**       | Prédire si un email est spam                       | Grouper des clients par profil d’achat                 | Apprendre à jouer à CartPole, DeepRacer, Pong, etc.             |



