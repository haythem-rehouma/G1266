
```python
!pip install gym gymnasium stable-baselines3

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import matplotlib.pyplot as plt
from IPython import display as ipythondisplay
import time

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

# Training the PPO agent
env = DummyVecEnv([lambda: gym.make(env_name)])
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=20000)
model.save('/content/ppo_model')

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

