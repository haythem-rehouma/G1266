# Introduction
--------------------------------

```bash
C:\Python27\python gridworld.py -a value -i 100 -k 10
```

**Cette commande exécute :**

- **Algorithme :** Itération de Valeur (`-a value`)
- **Itérations :** 100 itérations pour évaluer les valeurs des états (`-i 100`)
- **Épisodes :** 10 épisodes seront lancés (`-k 10`)

---------------------------------------------------------

```bash
C:\Python27\python gridworld.py -a value -i 100 -k 10 --livingReward -2
```

**Détails de cette commande :**

- **Algorithme :** Itération de Valeur (`-a value`)
- **Itérations :** 100 itérations pour évaluer les valeurs des états (`-i 100`)
- **Épisodes :** 10 épisodes
- **Récompense de Survie :** -2 (`--livingReward -2`)

---------------------------------------------------------

```bash
C:\Python27\python gridworld.py -a value -i 10 -k 2 --livingReward -2
```

**Explication :**

- **Algorithme :** Itération de Valeur (`-a value`)
- **Itérations :** 10 mises à jour des états
- **Épisodes :** 2 épisodes
- **Récompense de Survie :** -2

---------------------------------------------------------

# Différence entre Itérations et Épisodes

| Critère                 | Itérations                                  | Épisodes                                           |
|-------------------------|----------------------------------------------|----------------------------------------------------|
| **Définition**           | Nombre de fois que les valeurs des états sont mises à jour | Nombre de fois que l'agent interagit avec l'environnement |
| **Algorithme affecté**   | Itération de Valeur, Q-learning              | Interactions directes dans l'environnement         |
| **Objectif**             | Améliorer les estimations des états          | Tester la politique sur plusieurs épisodes         |
| **Convergence**          | Plus d'itérations = meilleures estimations   | Plus d'épisodes = meilleure évaluation de la politique |

---------------------------------------------------------

# Exercice 
--------------------------------

```bash
C:\Python27\python gridworld.py -a value -i 1
C:\Python27\python gridworld.py -a value -i 2
C:\Python27\python gridworld.py -a value -i 3
C:\Python27\python gridworld.py -a value -i 5
C:\Python27\python gridworld.py -a value -i 7
C:\Python27\python gridworld.py -a value -i 12
C:\Python27\python gridworld.py -a value -i 100
```

**Ces commandes exécutent :**

- **Algorithme :** Itération de Valeur (`-a value`)
- **Itérations :** Effectue 1, 2, 3, 5, 7, 12, ou 100 itérations selon la commande pour évaluer les valeurs des états.

---------------------------------------------------------

```bash
C:\Python27\python gridworld.py -a value -i 100 -k 10
C:\Python27\python gridworld.py -a value -i 1 -k 2 --livingReward -2
C:\Python27\python gridworld.py -a value -i 2 -k 2 --livingReward -2
C:\Python27\python gridworld.py -a value -i 10 -k 2 --livingReward -2
C:\Python27\python gridworld.py -a value -i 10 -k 2 --livingReward 2
```

**Ces commandes exécutent :**

- **Algorithme :** Itération de Valeur (`-a value`)
- **Itérations et Épisodes :**
  - 100 itérations, 10 épisodes (`-i 100 -k 10`)
  - 1 ou 2 ou 10 itérations avec 2 épisodes et différentes récompenses de survie (`--livingReward -2` ou `2`)

---------------------------------------------------------

```bash
C:\Python27\python gridworld.py -a value -i 12 -k 2 --livingReward -0.01
C:\Python27\python gridworld.py -a value -i 12 -k 2 --livingReward -0.03
C:\Python27\python gridworld.py -a value -i 12 -k 2 --livingReward -0.4
C:\Python27\python gridworld.py -a value -i 12 -k 2 --livingReward -2.0
C:\Python27\python gridworld.py -a value -i 12 -k 2 --livingReward 2.0
```

**Ces commandes exécutent :**

- **Algorithme :** Itération de Valeur (`-a value`)
- **Itérations :** 12 itérations avec 2 épisodes.
- **Récompenses de Survie :** Valeurs variant de -0.01 à 2.0 (`--livingReward`)

---------------------------------------------------------

### Explication des commandes supplémentaires :

1. **Nombre d'itérations** :
   - Les itérations définissent combien de fois l'algorithme actualise les valeurs des états pour mieux estimer les futurs gains.

2. **Nombre d'épisodes** :
   - Les épisodes représentent le nombre d'interactions de l'agent avec l'environnement pour appliquer les décisions basées sur les valeurs d'états calculées.
