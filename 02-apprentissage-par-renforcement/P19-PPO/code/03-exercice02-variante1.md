## Solution – Variante 1 : Moins d’entraînement (`total_timesteps=5000`)

### Code modifié

```python
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import gymnasium as gym

env_name = 'CartPole-v1'
env = DummyVecEnv([lambda: gym.make(env_name)])

# Création du modèle avec configuration par défaut
model = PPO('MlpPolicy', env, verbose=1)

# Apprentissage avec seulement 5000 itérations
model.learn(total_timesteps=5000)

# Sauvegarde du modèle (facultatif)
model.save('/content/ppo_model_variante1')
```



### Code d’évaluation (à faire après entraînement)

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

print(f"Score obtenu après entraînement court (5000 étapes) : {score}")
env_eval.close()
```

---

### Exemple de résultat observé

```text
Score obtenu après entraînement court (5000 étapes) : 28.0
```

> (Ce score peut varier légèrement à chaque exécution, mais restera généralement faible : entre 20 et 40.)



### Observation 

| Variante             | total\_timesteps | Architecture réseau | Autres paramètres | Score moyen | Observation                                                                                           |
| -------------------- | ---------------- | ------------------- | ----------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| Moins d’entraînement | 5000             | Par défaut (`Mlp`)  | Aucun             | \~28        | L’agent commence à apprendre mais reste très limité. Trop peu d’entraînement pour maîtriser la tâche. |



### Analyse

* **Conclusion** : Avec seulement 5000 étapes, l’agent **n’a pas assez exploré** l’environnement pour comprendre comment garder le bâton droit.
* Cela montre que **le temps d’entraînement est un facteur critique** dans l’apprentissage par renforcement.
* On peut supposer que les performances s’amélioreront significativement en passant à 20 000 ou 50 000 étapes.

