# **Découvrir le Cycle de Vie d’un Projet en Apprentissage par Renforcement (RL)**



## Introduction

Quand on parle d’apprentissage par renforcement (RL), on parle d’un **agent intelligent** qui apprend à **prendre des décisions** pour **atteindre un objectif**, en **testant des actions** et en **recevant des récompenses**.



## Objectif général

L’objectif d’un projet en RL est de permettre à un agent (par exemple, un robot, une voiture virtuelle ou un logiciel) d’**apprendre par essais et erreurs** comment bien se comporter dans un environnement.



## Le cycle de vie en 6 étapes

### **1. Comprendre le problème**

On commence par se poser la question :

> **Qu’est-ce que l’agent doit réussir à faire ?**

Exemple :
Faire rouler une voiture sans sortir de la route.



### **2. Créer un environnement**

On construit un **monde simulé** ou réel où l’agent va s’entraîner.
Ce monde doit :

* Réagir à ce que fait l’agent,
* Lui donner des informations (par exemple, une image ou une position),
* Lui dire s’il a bien ou mal agi (récompense).



### **3. Choisir les actions possibles**

L’agent ne peut pas faire tout ce qu’il veut.
On lui donne une **liste d’actions autorisées** (par exemple : avancer, tourner à gauche, ralentir).



### **4. Définir la récompense**

C’est l’étape **la plus importante**.
On doit dire à l’agent :

> “Cette action est bonne → tu gagnes +1”
> “Cette action est mauvaise → tu perds -1”

Exemple :
+1 s’il reste sur la route,
-1 s’il sort ou va trop vite dans un virage.

### **5. Entraîner l’agent**

L’agent commence à **tester des actions** au hasard.
Petit à petit, il **apprend quelles actions donnent des récompenses**.

C’est comme un jeu vidéo où il recommence jusqu’à trouver le bon chemin.



### **6. Tester ce qu’il a appris**

À la fin, on arrête l’apprentissage et on teste l’agent :

* Est-ce qu’il réussit à faire la tâche ?
* Est-ce qu’il fait mieux qu’avant ?
* Peut-on utiliser ce qu’il a appris dans un vrai environnement ?



## Résumé visuel (à afficher ou dessiner au tableau)

```
[ Problème à résoudre ]
         ↓
[ Environnement ]
         ↓
[ Actions possibles ]
         ↓
[ Récompense = règles ]
         ↓
[ Entraînement = apprentissage ]
         ↓
[ Test final = a-t-il appris ? ]
```

---

## Exemples concrets simples

| Exemple           | Agent          | Environnement  | Objectif            |
| ----------------- | -------------- | -------------- | ------------------- |
| Voiture virtuelle | DeepRacer      | Circuit        | Rester sur la piste |
| Chat robot        | Jouet éducatif | Salon          | Trouver la balle    |
| Jeu vidéo         | Personnage IA  | Plateau de jeu | Gagner une partie   |

