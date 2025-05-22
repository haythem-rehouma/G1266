
### Installation des librairies nécessaires

```python
!pip install gym gymnasium stable-baselines3


```

### import des librairies

```python

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import matplotlib.pyplot as plt
from IPython import display as ipythondisplay
import time

```



### Essai aléatoire

```python
env_name = 'CartPole-v1'
env = gym.make(env_name, render_mode='rgb_array')

def show_frame(frame):
    plt.figure(figsize=(8,6))
    plt.imshow(frame)
    plt.axis('off')
    ipythondisplay.clear_output(wait=True)
    ipythondisplay.display(plt.gcf())
    plt.close()

# Random Agent Visualization
for episode in range(1, 10):
    score = 0
    state, _ = env.reset()
    done = False
    truncated = False

    while not (done or truncated):
        frame = env.render()
        show_frame(frame)
        action = env.action_space.sample()
        n_state, reward, done, truncated, info = env.step(action)
        score += reward

    print(f'Episode: {episode}, Score: {score}')
    time.sleep(2)

env.close()

```


### entraînement du modèle

```python
# Training the PPO agent
env = DummyVecEnv([lambda: gym.make(env_name)])
model = PPO('MlpPolicy', env, verbose=1) <== Changez cette ligne pour l'exercice
model.learn(total_timesteps=20000)  <== Changez cette ligne pour l'exercice
model.save('/content/ppo_model') <== Changez cette ligne pour l'exercice

```


### Visiualisation du résultat final

```python
# Evaluate PPO Agent
env = gym.make(env_name, render_mode='rgb_array')
obs, _ = env.reset()

for episode in range(1, 2):
    score = 0
    done = False
    truncated = False
    start_time = time.time()

    while not (done or truncated):
        frame = env.render()
        show_frame(frame)
        action, _ = model.predict(obs)
        obs, reward, done, truncated, info = env.step(action)
        score += reward

        if time.time() - start_time >= 20:
            print(f'Episode: {episode}, Score: {score} (Timed out after 20 seconds)')
            break

    if not (done or truncated):
        print(f'Episode: {episode}, Score: {score} (Completed)')

env.close()

```

### Calculer le score et évaluation finale

```python
import time

env_eval = gym.make(env_name, render_mode='rgb_array')
obs, _ = env_eval.reset()
score = 0
done, truncated = False, False
start_time = time.time()

while not (done or truncated):
    action, _ = model.predict(obs)
    obs, reward, done, truncated, _ = env_eval.step(action)
    score += reward
    if time.time() - start_time >= 20:
        break

print(f"Score obtenu après entraînement court (20000 étapes) : {score}")
env_eval.close()

```





### *Objectif général :*

Entraîner une intelligence artificielle (IA) à **équilibrer un bâton sur un chariot** dans un environnement appelé **CartPole-v1**, à l’aide de l’algorithme **PPO (Proximal Policy Optimization)**.



###  *Étapes principales du programme :*

1. **Installation des bibliothèques nécessaires**

   * `gym`, `gymnasium` : pour créer l’environnement de simulation (le jeu).
   * `stable-baselines3` : pour utiliser l’algorithme PPO.

2. **Création de l’environnement**

   * On initialise `CartPole-v1`, un jeu classique où un bâton doit rester en équilibre sur un chariot mobile.

3. **Visualisation d’un agent aléatoire**

   * On fait jouer un agent qui prend des décisions au hasard (sans intelligence).
   * Résultat : il échoue souvent.

4. **Entraînement de l’agent avec PPO**

   * On crée un modèle PPO et on l’entraîne pendant 20 000 itérations.
   * L’agent apprend progressivement comment garder le bâton droit.

5. **Évaluation de l’agent entraîné**

   * On teste l’agent après l’entraînement.
   * Cette fois, il réussit bien à garder le bâton en équilibre, car il a "appris" à jouer.


###  **Résumé :**

* **Avant l’entraînement** : l’agent agit au hasard → échec.
* **Après l’entraînement** : l’agent prend des décisions optimisées → succès.


<br/>

# Plus de détails :



###  **Objectif général :**

Entraîner une intelligence artificielle (IA) à **équilibrer un bâton sur un chariot** dans un environnement appelé **CartPole-v1**, à l’aide de l’algorithme **PPO (Proximal Policy Optimization)**.



###  **Étapes principales du programme :**



### 1.  **Installation des bibliothèques nécessaires**

```python
!pip install gym gymnasium stable-baselines3
```

* `gym`, `gymnasium` : bibliothèques qui fournissent l’environnement de simulation (ici, CartPole).
* `stable-baselines3` : permet d’utiliser des algorithmes d’apprentissage par renforcement comme PPO.



### 2.  **Création de l’environnement**

```python
import gymnasium as gym
env_name = 'CartPole-v1'
env = gym.make(env_name, render_mode='rgb_array')
```

* On initialise l’environnement `CartPole-v1` avec un mode de rendu visuel (`rgb_array`) pour observer les actions de l’agent.



### 3.  **Visualisation d’un agent aléatoire**

```python
import matplotlib.pyplot as plt
from IPython import display as ipythondisplay
import time

def show_frame(frame):
    plt.figure(figsize=(8,6))
    plt.imshow(frame)
    plt.axis('off')
    ipythondisplay.clear_output(wait=True)
    ipythondisplay.display(plt.gcf())
    plt.close()

for episode in range(1, 4):  # réduit à 3 pour aller plus vite
    score = 0
    state, _ = env.reset()
    done = False
    truncated = False

    while not (done or truncated):
        frame = env.render()
        show_frame(frame)
        action = env.action_space.sample()  # action aléatoire
        state, reward, done, truncated, _ = env.step(action)
        score += reward

    print(f"Épisode: {episode}, Score: {score}")
    time.sleep(1)

env.close()
```

* L’agent prend des décisions aléatoires → il ne garde pas le bâton en équilibre longtemps.


### 4.  **Entraînement de l’agent avec PPO**

```python
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

env = DummyVecEnv([lambda: gym.make(env_name)])
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=20000)
model.save("/content/ppo_model")
```

* On utilise PPO (Proximal Policy Optimization), un algorithme puissant d’apprentissage par renforcement.
* L’agent apprend à jouer intelligemment pendant 20 000 itérations.



### 5.  **Évaluation de l’agent entraîné**

```python
env = gym.make(env_name, render_mode='rgb_array')
obs, _ = env.reset()

for episode in range(1, 2):
    score = 0
    done = False
    truncated = False
    start_time = time.time()

    while not (done or truncated):
        frame = env.render()
        show_frame(frame)
        action, _ = model.predict(obs)  # prédiction intelligente
        obs, reward, done, truncated, _ = env.step(action)
        score += reward

        if time.time() - start_time >= 20:
            print(f'Épisode: {episode}, Score: {score} (Limite de temps atteinte)')
            break

    if not (done or truncated):
        print(f'Épisode: {episode}, Score: {score} (Terminé avec succès)')

env.close()
```

* Cette fois, l’agent utilise ce qu’il a appris pour jouer efficacement et garder le bâton en équilibre.



###  **Résumé final**

* **Avant l’entraînement** → Agent agit au hasard → chute rapide.
* **Après l’entraînement** → Agent agit de façon optimisée → stabilité prolongée.

<br/>

# Annexe 2



```python
!pip install gym gymnasium stable-baselines3      # Installe les bibliothèques Gym / Gymnasium et Stable-Baselines3
```

```python
import gymnasium as gym                            # Importe Gymnasium (création d’environnements RL)
from stable_baselines3 import PPO                 # Importe l’algorithme PPO (Proximal Policy Optimization)
from stable_baselines3.common.vec_env import DummyVecEnv  # Wrapper pour vectoriser l’environnement
import matplotlib.pyplot as plt                   # Bibliothèque d’affichage pour les images
from IPython import display as ipythondisplay     # Permet d’afficher/effacer des figures dans un notebook
import time                                       # Mesure du temps et pauses
```

```python
env_name = 'CartPole-v1'                          # Nom de l’environnement choisi : CartPole-v1
env = gym.make(env_name, render_mode='rgb_array') # Création de l’environnement, rendu sous forme d’images RGB
```

```python
def show_frame(frame):                            # Déclaration d’une fonction utilitaire pour afficher une image
    plt.figure(figsize=(8, 6))                    # 1) Définit la taille de la figure
    plt.imshow(frame)                             # 2) Affiche l’image passée en paramètre
    plt.axis('off')                               # 3) Supprime les axes pour un rendu propre
    ipythondisplay.clear_output(wait=True)        # 4) Efface la figure précédente (effet vidéo fluide)
    ipythondisplay.display(plt.gcf())             # 5) Affiche la figure courante
    plt.close()                                   # 6) Ferme la figure pour libérer la mémoire
```

```python
# ---- 1re phase : agent aléatoire ------------------------------------------
for episode in range(1, 4):                       # Boucle sur 3 épisodes d’observation
    score = 0                                     # Initialise le score (somme des récompenses)
    state, _ = env.reset()                        # Réinitialise l’environnement et récupère l’état initial
    done, truncated = False, False                # Flags de fin d’épisode

    while not (done or truncated):                # Boucle jusqu’à la fin de l’épisode
        frame = env.render()                      # Rendu visuel de l’environnement (image RGB)
        show_frame(frame)                         # Affiche l’image
        action = env.action_space.sample()        # Sélectionne une action au hasard
        state, reward, done, truncated, _ = env.step(action)  # Applique l’action et récupère la transition
        score += reward                           # Cumule la récompense
    print(f"Épisode {episode} : score {score}")   # Affiche le score obtenu
    time.sleep(1)                                 # Petite pause avant l’épisode suivant
env.close()                                       # Ferme l’environnement (libère les ressources)
```

```python
# ---- 2e phase : entraînement PPO ------------------------------------------
env = DummyVecEnv([lambda: gym.make(env_name)])   # Vectorise l’environnement (même s’il n’y en a qu’un)
model = PPO('MlpPolicy', env, verbose=1)          # Crée un agent PPO avec une politique réseau MLP
model.learn(total_timesteps=20_000)               # Entraîne l’agent pendant 20 000 étapes
model.save("/content/ppo_model")                  # Sauvegarde du modèle entraîné
```

```python
# ---- 3e phase : évaluation du modèle entraîné -----------------------------
env = gym.make(env_name, render_mode='rgb_array') # Nouveau CartPole pour l’évaluation
obs, _ = env.reset()                              # État initial
for episode in range(1, 2):                       # Un seul épisode d’évaluation
    score, done, truncated = 0, False, False
    start_time = time.time()                      # Point de départ du chronomètre
    while not (done or truncated):
        frame = env.render()                      # Rendu image
        show_frame(frame)                         # Affiche l’image
        action, _ = model.predict(obs)            # Action décidée par la politique PPO
        obs, reward, done, truncated, _ = env.step(action)  # Transition environnementale
        score += reward                           # Mise à jour du score
        if time.time() - start_time >= 20:        # Coupe l’épisode après 20 s pour ne pas boucler trop longtemps
            print(f"Épisode 1 : score {score} (limite de temps atteinte)")
            break
    if not (done or truncated):                   # Si l’épisode s’est terminé avant le timeout
        print(f"Épisode 1 : score {score} (terminé normalement)")
env.close()                                       # Ferme l’environnement
```

---

### Lecture guidée

1. **Installation** : première ligne, exécutable dans Colab ou Jupyter, installe trois dépendances essentielles.
2. **Imports** : chargent les bibliothèques nécessaires (environnements, algorithmes RL, affichage, etc.).
3. **Création de l’environnement** : `CartPole-v1` est démarré en mode visuel.
4. **Fonction `show_frame`** : gère l’affichage fluide d’une image (frame).
5. **Agent aléatoire** : démontre l’environnement avant apprentissage ; l’agent choisit ses actions au hasard.
6. **Entraînement PPO** : le modèle apprend pendant 20 000 pas à garder le bâton en équilibre.
7. **Évaluation** : on recharge l’environnement, on laisse l’agent entraîné jouer et on observe qu’il réussit mieux.


