# Exercice : Expérimenter avec PPO et comparer les résultats



- Notre objectif est de vomprendre l’impact des paramètres de configuration du modèle PPO (`Proximal Policy Optimization`) sur la qualité de l’apprentissage. 
- À travers plusieurs variantes, vous êtes amenés à observer comment les performances de l’agent évoluent selon la durée d’entraînement, la taille du réseau de neurones, ou encore les paramètres d’exploration.



# Consigne générale

Partir du code suivant :

```python
env = DummyVecEnv([lambda: gym.make(env_name)])
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=20000)
model.save('/content/ppo_model')
```

À chaque nouvelle tentative :

1. Modifier **un seul paramètre ou une seule ligne**.
2. Réentraîner le modèle.
3. Évaluer les performances en exécutant 1 ou 2 épisodes.
4. Noter le score final et formuler une observation comparative.



# Ensemble du code



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



# Variantes à tester

### Variante 1 – Moins d’entraînement

```python
model.learn(total_timesteps=5000)
```

Objectif : observer si le modèle apprend quelque chose en très peu de temps.



### Variante 2 – Entraînement plus long

```python
model.learn(total_timesteps=50000)
```

Objectif : comparer les performances avec un apprentissage plus long.



### Variante 3 – Réseau de neurones plus grand

```python
policy_kwargs = dict(net_arch=[128, 128])
model = PPO('MlpPolicy', env, verbose=1, policy_kwargs=policy_kwargs)
```

Objectif : tester si un réseau plus profond permet d’obtenir de meilleures décisions.


### Variante 4 – Réseau de neurones plus petit

```python
policy_kwargs = dict(net_arch=[32])
model = PPO('MlpPolicy', env, verbose=1, policy_kwargs=policy_kwargs)
```

Objectif : vérifier si une architecture minimale peut tout de même apprendre.



### Variante 5 – Renforcer l’exploration

```python
model = PPO('MlpPolicy', env, verbose=1, ent_coef=0.05)
```

Objectif : analyser si une exploration plus importante favorise l’apprentissage.



### Variante 6 – Changer la taille des mini-lots

```python
model = PPO('MlpPolicy', env, verbose=1, n_steps=128, batch_size=64)
```

Objectif : comprendre l’effet du batch size sur la stabilité de l’apprentissage.



## Tableau comparatif à compléter

| Variante               | total\_timesteps | Architecture réseau | Autres paramètres            | Score moyen | Observation |
| ---------------------- | ---------------- | ------------------- | ---------------------------- | ----------- | ----------- |
| Version de base        | 20000            | Par défaut          | Aucun                        |             |             |
| Moins d’entraînement   | 5000             | Par défaut          | Aucun                        |             |             |
| Entraînement plus long | 50000            | Par défaut          | Aucun                        |             |             |
| Réseau plus grand      | 20000            | \[128, 128]         | Aucun                        |             |             |
| Réseau plus petit      | 20000            | \[32]               | Aucun                        |             |             |
| Exploration renforcée  | 20000            | Par défaut          | `ent_coef=0.05`              |             |             |
| Taille de lot modifiée | 20000            | Par défaut          | `n_steps=128, batch_size=64` |             |             |



## Travail à remettre

1. Le code modifié pour chaque variante.
2. Le tableau rempli avec vos scores et observations.
3. Une conclusion synthétique (5 lignes maximum) :

   * Quel changement a eu l’effet le plus visible ?
   * Quelles hypothèses pouvez-vous formuler ?


<br/>

# Annexe 1 : Peut-on changer `MlpPolicy` dans PPO ?



**Oui**, mais seulement par d’autres **politiques compatibles** avec le type d’environnement (ici, `CartPole-v1`, qui est **discret et basé sur des vecteurs**, pas sur des images).



## Explication simple de `MlpPolicy`

* `MlpPolicy` signifie **Multi-Layer Perceptron Policy**.
* C’est un **réseau de neurones classique (dense)** adapté aux **observations sous forme de vecteurs numériques** (par exemple : `[position, vitesse, angle, vitesse angulaire]`).



## Quelles sont les autres politiques possibles dans `stable-baselines3` ?

| Politique          | Utilisation                            | Compatible avec CartPole ? |
| ------------------ | -------------------------------------- | -------------------------- |
| `MlpPolicy`        | Pour les vecteurs (comme CartPole)     | ✅ Oui                      |
| `CnnPolicy`        | Pour les images (vision, jeux vidéo)   | ❌ Non                      |
| `MultiInputPolicy` | Pour les observations complexes (dict) | ❌ Non                      |

> Pour CartPole, **vous devez utiliser `MlpPolicy`**.
> Changer par `CnnPolicy` ou `MultiInputPolicy` **plantera le code**, car l’observation n’est **pas une image**.



## Comment modifier **l’intérieur** de `MlpPolicy` sans la changer complètement ?

Vous pouvez personnaliser **la taille ou la forme du réseau** via `policy_kwargs`, sans changer de politique :

```python
policy_kwargs = dict(net_arch=[64, 64])
model = PPO('MlpPolicy', env, verbose=1, policy_kwargs=policy_kwargs)
```

> Cela **modifie la structure interne** du réseau, tout en gardant une politique compatible.



## À retenir

* Oui, vous pouvez **modifier** les paramètres internes de `MlpPolicy`.
* ❌ Non, vous **ne pouvez pas la remplacer** par `CnnPolicy` dans CartPole, car ce n’est **pas un environnement d’images**.
*  Si vous utilisez un autre environnement **basé sur des images**, alors `CnnPolicy` devient possible.


