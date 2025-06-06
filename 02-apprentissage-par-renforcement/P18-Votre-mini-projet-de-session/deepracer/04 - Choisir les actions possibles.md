
## **Leçon 4 – Choisir les actions possibles**

### Pourquoi l’agent a besoin d’actions ?

Un agent intelligent **ne peut pas rester immobile**.
Pour apprendre, il doit **essayer des choses** : avancer, tourner, freiner, etc.

> Ces choses qu’il peut faire s’appellent des **actions**.



### 1. Qu’est-ce qu’une action ?

Une **action**, c’est **une décision que l’agent peut prendre à un moment donné**.

Exemple avec une voiture :

* Aller tout droit
* Tourner à gauche
* Tourner à droite
* Ralentir
* S’arrêter

L’agent **choisit une action**, puis l’environnement **réagit**.



### 2. On ne lui donne pas toutes les actions possibles

L’agent **ne peut pas tout faire**.
C’est nous qui décidons **quelles actions sont autorisées**.

Pourquoi ?

* Pour que l’apprentissage soit plus simple,
* Pour éviter qu’il fasse des choses inutiles ou dangereuses.



### 3. Deux façons de choisir les actions

| Type        | Explication simple                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------- |
| **Discret** | L’agent a une **liste limitée** d’actions. Par exemple : avancer vite, avancer lentement, tourner à gauche. |
| **Continu** | L’agent peut **choisir une valeur précise**. Par exemple : tourner à 12° ou 33°, aller à 1.6 m/s.           |

**Pour débuter**, on utilise presque toujours des **actions discrètes**, car c’est plus facile à gérer.



### 4. Pourquoi c’est important ?

Si tu donnes trop peu d’actions, l’agent ne pourra pas faire des choses utiles.
Si tu en donnes trop, il mettra **plus de temps à apprendre**.

> Il faut **trouver un bon équilibre** : assez pour agir, pas trop pour se perdre.



### 5. Résumé visuel

```
L’agent doit faire des choix
→ Ces choix = actions possibles
→ On lui donne une liste simple pour commencer
→ Il apprend en les testant dans son environnement
```

