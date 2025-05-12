
#  Scénario d’apprentissage :

> **Je veux que ma voiture reste bien au centre de la piste, roule assez vite, et évite de tourner trop fort dans les lignes droites.**

On va construire la fonction **étape par étape**, en expliquant **chaque ajout**.



## Étape 1 – Créer la base de la fonction

Tout commence par cette structure :

```python
def reward_function(params):
    reward = 0.0
    return reward
```

👉 Ici, on initialise la variable `reward` à zéro, et on la retournera à la fin.


## Étape 2 – Récompenser si la voiture reste sur la piste

On ajoute un test simple :

> “Si les 4 roues sont sur la piste, on donne 1 point.”

```python
def reward_function(params):
    reward = 0.0

    if params['all_wheels_on_track']:
        reward += 1.0

    return reward
```

 **Pourquoi c’est utile ?**
L’agent apprend que sortir de la piste = pas de récompense.



## Étape 3 – Récompenser s’il est bien centré

On veut maintenant encourager la voiture à **rouler près du centre de la piste**.

```python
def reward_function(params):
    reward = 0.0

    if params['all_wheels_on_track']:
        reward += 1.0

        # Récupérer les données
        distance_from_center = params['distance_from_center']
        track_width = params['track_width']

        # Calculer la distance relative au centre
        if distance_from_center < 0.1 * track_width:
            reward += 1.0  # très bien centré
        elif distance_from_center < 0.25 * track_width:
            reward += 0.5  # correct
        else:
            reward += 0.1  # proche du bord, mais encore sur la piste

    return reward
```

 **Pourquoi c’est important ?**
Le centre = trajectoire plus rapide, plus stable.



## Étape 4 – Bonus si la voiture roule vite

Ajoutons maintenant un **bonus pour la vitesse**.

```python
def reward_function(params):
    reward = 0.0

    if params['all_wheels_on_track']:
        reward += 1.0

        distance_from_center = params['distance_from_center']
        track_width = params['track_width']

        if distance_from_center < 0.1 * track_width:
            reward += 1.0
        elif distance_from_center < 0.25 * track_width:
            reward += 0.5
        else:
            reward += 0.1

        # Bonus pour la vitesse
        speed = params['speed']
        if speed > 2.0:
            reward += 0.5
```

 On encourage l’agent à **rouler vite… mais bien centré !**



## Étape 5 – Pénaliser les virages trop serrés

On évite que la voiture **zigzague** ou fasse des mouvements brusques :

```python
        # Pénalité si l'angle de braquage est trop fort
        steering_angle = abs(params['steering_angle'])
        if steering_angle > 15:
            reward *= 0.8  # on réduit un peu la récompense
```



## Fonction finale complète

```python
def reward_function(params):
    reward = 0.0

    if params['all_wheels_on_track']:
        reward += 1.0

        distance_from_center = params['distance_from_center']
        track_width = params['track_width']

        if distance_from_center < 0.1 * track_width:
            reward += 1.0
        elif distance_from_center < 0.25 * track_width:
            reward += 0.5
        else:
            reward += 0.1

        speed = params['speed']
        if speed > 2.0:
            reward += 0.5

        steering_angle = abs(params['steering_angle'])
        if steering_angle > 15:
            reward *= 0.8  # on pénalise les virages trop serrés

    return float(reward)
```



# Vous allez:

1. **Copier chaque étape au tableau ou dans un notebook.**
2. **Expliquer en commentaire ce que chaque ligne contrôle.**
3. **Modifier un paramètre et voir le résultat.**
4. **Tester plusieurs variantes de fonctions.**
