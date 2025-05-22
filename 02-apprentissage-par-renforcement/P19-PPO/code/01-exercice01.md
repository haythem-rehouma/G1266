## Quiz : Compréhension du programme CartPole avec PPO

*(30 questions)*


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



### Instructions

Répondez aux questions suivantes sans consulter le corrigé. Certaines sont à choix multiple, d’autres à réponse courte ou vrai/faux.



### Questions

1. **Choix multiple**
   Quel est le but principal du programme ?
   
   a) Classifier des images de chiffres
   
   b) Équilibrer un bâton sur un chariot
   
   c) Jouer à Pac-Man
   
   d) Générer des textes

3. **Vrai/Faux**
   Le module `gymnasium` est utilisé pour créer l’environnement CartPole-v1.

4. **Réponse courte**
   Quelle commande unique installe toutes les bibliothèques nécessaires ?

5. **Choix multiple**
   Quel algorithme d’apprentissage par renforcement est employé ?
   
   a) DQN
   
   b) A2C
   
   c) PPO
   
   d) SAC

7. **Réponse courte**
   Que signifie l’argument `render_mode='rgb_array'` passé à `gym.make` ?

8. **Choix multiple**
   Dans la fonction `show_frame`, quel appel permet d’effacer la frame précédente ?
   
   a) `plt.close()`
   
   b) `ipythondisplay.clear_output(wait=True)`
   
   c) `plt.axis('off')`
   
   d) `plt.figure()`

10. **Vrai/Faux**
   La boucle d’entraînement s’exécute pendant exactement 2 000 pas.

11. **Réponse courte**
   Quel objet encapsule l’environnement pour le rendre compatible avec `stable-baselines3` ?

12. **Choix multiple**
   Quel paramètre de `PPO` définit le type de réseau de neurones utilisé pour la politique ?

   a) `policy_type`
   
   b) `MlpPolicy`
   
   c) `vec_env`
   
   d) `verbose`

14. **Réponse courte**
    Quelle variable contient la récompense reçue à chaque pas dans la phase “agent aléatoire” ?

15. **Vrai/Faux**
    `env.action_space.sample()` renvoie toujours la même action.

16. **Choix multiple**
    Quelle instruction sauvegarde le modèle entraîné ?
    
    a) `model.store()`
    
    b) `model.save('/content/ppo_model')`
    
    c) `torch.save(model)`
    
    d) `pickle.dump(model)`

18. **Réponse courte**
    Quel est l’objectif du test chronométré de 20 secondes lors de l’évaluation ?

19. **Vrai/Faux**
    `DummyVecEnv` est nécessaire même si l’on n’utilise qu’un seul environnement.

20. **Réponse courte**
    Combien d’épisodes aléatoires sont exécutés avant l’entraînement dans la version proposée ?

21. **Choix multiple**
    Quel module est utilisé pour afficher des images dans un notebook Jupyter ?
    
    a) `IPython.display`
    
    b) `cv2.imshow`
    
    c) `pygame.display`
    
    d) `tkinter`

23. **Réponse courte**
    Quel rôle joue la variable `score` dans chaque boucle d’épisode ?

24. **Vrai/Faux**
    Après l’entraînement, l’agent utilise la méthode `predict` du modèle pour choisir ses actions.

25. **Choix multiple**
    Pourquoi ferme-t-on l’environnement avec `env.close()` ?
    
    a) Pour libérer la mémoire et les ressources graphiques
    
    b) Pour sauvegarder les résultats
    
    c) Pour réinitialiser `gym`
    
    d) Ce n’est pas nécessaire, c’est décoratif

27. **Réponse courte**
    Quel paramètre de `PPO` active l’affichage détaillé de l’entraînement ?

28. **Vrai/Faux**
    Si la variable `done` devient `True`, l’épisode se termine immédiatement.

29. **Choix multiple**
    La récompense dans CartPole augmente principalement lorsque :
    
    a) Le bâton tombe vite
    
    b) Le bâton reste en équilibre plus longtemps
    
    c) Le chariot quitte l’écran
    
    d) L’agent n’agit pas

31. **Réponse courte**
    Quelle structure de contrôle assure la répétition d’actions jusqu’à la fin de l’épisode ?

32. **Vrai/Faux**
    `time.sleep(1)` ajoute une pause d’une seconde entre deux épisodes aléatoires.

33. **Choix multiple**
    Sous quelle forme stocke-t-on l’environnement dans `DummyVecEnv` ?
    
    a) Liste de fonctions lambdas
    
    b) Dictionnaire de paramètres
    
    c) Objet `GymWrapper`
    
    d) Tensor PyTorch

35. **Réponse courte**
    Quelle différence conceptuelle existe-t-il entre un agent “aléatoire” et un agent “entraîné” ?

36. **Vrai/Faux**
    La variable `truncated` peut devenir vraie même si `done` est fausse.

37. **Choix multiple**
    Quel import est indispensable pour afficher des figures ?
    
    a) `import seaborn`
    
    b) `import matplotlib.pyplot as plt`
    
    c) `import pandas as pd`
    
    d) `import numpy as np`

39. **Réponse courte**
    Que se passe-t-il si l’on supprime l’appel `plt.close()` dans `show_frame` ? Donnez une conséquence possible.

40. **Vrai/Faux**
    Le nom `CartPole-v1` indique le premier environnement officiel de type CartPole dans la suite Gym.



## Corrigé 

- 1 b,
- 2 V,
- 3 `!pip install gym gymnasium stable-baselines3`,
- 4 c,
- 5 Permet de renvoyer des images RGB pour l’affichage,
- 6 b,
- 7 F,
- 8 `DummyVecEnv`,
- 9 b,
- 10 `reward`,
- 11 F,
- 12 b,
- 13 Limiter la durée d’un épisode d’évaluation pour ne pas boucler indéfiniment,
- 14 V,
- 15 3,
- 16 a,
- 17 Compter la somme des récompenses de l’épisode,
- 18 V,
- 19 a,
- 20 `verbose=1`,
- 21 V,
- 22 b,
- 23 Boucle `while not (done or truncated):`,
- 24 V,
- 25 a,
- 26 L’agent aléatoire agit sans apprentissage ; l’agent entraîné a optimisé ses actions pour maximiser la récompense,
- 27 V,
- 28 b,
- 29 Accumulation de figures en mémoire → fuite mémoire/ralentissement,
- 30 V.


