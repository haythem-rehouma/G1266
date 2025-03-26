
![image](https://github.com/user-attachments/assets/8508a1d2-71b5-46f3-8608-b4f9fa7b452a)




L'image ci-haut du problème des **récompenses infinies** dans un environnement où une tâche ou un jeu pourrait durer indéfiniment. 

# **Problème**

- **Jeu infini** : Si le jeu ou la tâche ne se termine jamais, comment éviter que les récompenses cumulatives deviennent infinies ?

# **Solutions**

1. **Horizon fini** :
   - Terminer les épisodes après un nombre fixe de pas (T).
   - Cela peut entraîner des politiques non stationnaires (voir Annexe01), car la stratégie dépend du temps restant.

2. **Actualisation (Discounting)** :
   - Utiliser un facteur d'actualisation $$\gamma$$ (0 < $$\gamma$$ < 1) pour réduire l'impact des récompenses futures.
   - Formule : $$U([r_0, \ldots, r_\infty]) = \sum_{t=0}^{\infty} \gamma^t r_t$$
   - Un $$\gamma$$ plus petit signifie un "horizon" plus court, favorisant les récompenses à court terme.

3. **État absorbant** :
   - Assurer qu'un état terminal soit éventuellement atteint pour chaque politique, garantissant ainsi une fin à la tâche.



------------------------------------------------
# Annexe 01
------------------------------------------------

Dans le cadre de l'apprentissage par renforcement (Reinforcement Learning, RL), un "jeu infini" signifie que la tâche ou l'environnement n'a pas de fin, c'est-à-dire qu'il n'y a pas de moment où l'agent sort ou termine l'épisode. Cela pose un problème car, si le but est de maximiser les **récompenses cumulatives** (les récompenses obtenues au fil du temps), elles pourraient devenir infinies si l'agent agit indéfiniment.

### Problème

Si l'environnement ne se termine jamais, l'agent pourrait accumuler des récompenses sans fin, ce qui compliquerait l'évaluation d'une politique (stratégie). Par exemple, si un agent continue à recevoir des récompenses positives indéfiniment, comment savoir s'il agit de manière optimale ou simplement profite d'une situation sans limite ? Cela mène à la question de savoir comment l'agent peut planifier ses actions de manière à ne pas accumuler des récompenses infinies, ce qui rendrait le problème difficile à résoudre.

### Solutions

1. **Horizon fini** :  
   Une solution courante consiste à définir un nombre fixe de pas après lequel l'épisode se termine, même si le jeu ou la tâche pourrait théoriquement durer pour toujours. Par exemple, on pourrait limiter un épisode à \( T \) pas (actions prises par l'agent).

   **Conséquence** :  
   Cela peut entraîner ce que l'on appelle des **politiques non stationnaires**. Une politique non stationnaire signifie que la stratégie de l'agent dépend du temps restant dans l'épisode. Au début, l'agent pourrait agir de manière différente que vers la fin, car il sait que l'épisode va bientôt se terminer. Par exemple, l'agent pourrait prendre plus de risques vers la fin s'il sait qu'il ne reste plus beaucoup de temps, ce qui fait varier la politique en fonction du temps.

En résumé, dans un problème de RL avec un **jeu infini**, on veut éviter que les récompenses cumulatives deviennent infinies. Une solution est d'introduire un **horizon fini**, mais cela peut rendre la politique de l'agent dépendante du temps, créant ainsi une politique non stationnaire.
