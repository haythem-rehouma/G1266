------------------------------------------------------------------
# Quiz sur les utilités infinies
------------------------------------------------------------------

1. **Qu'est-ce qu'une utilité infinie dans le contexte du RL ?**
   - a) Une récompense qui ne peut jamais être atteinte
   - b) Une situation où les récompenses cumulées peuvent devenir infinies si le jeu ne se termine jamais
   - c) Une stratégie optimale pour maximiser les gains

2. **Quelle est une solution pour gérer les utilités infinies ?**
   - a) Ignorer les récompenses futures
   - b) Utiliser un horizon fini pour terminer les épisodes après un nombre fixe de pas
   - c) Réduire la taille de l'environnement

3. **Qu'est-ce que l'actualisation (discounting) ?**
   - a) Ignorer les récompenses immédiates
   - b) Utiliser un facteur $$\gamma$$ (0 < $$\gamma$$ < 1) pour donner plus d'importance aux récompenses immédiates et réduire l'impact des récompenses futures
   - c) Augmenter la probabilité de succès des actions

4. **Mise en situation :**
   - Imaginez un jeu vidéo où le joueur peut continuer indéfiniment :
     - **Horizon fini** : Le jeu se termine automatiquement après 1000 étapes.
     - **Actualisation** : Les récompenses futures sont réduites par un facteur de 0,9 à chaque étape.
     - **État absorbant** : Le jeu garantit qu'un état final est atteint après un certain temps.

5. **Pourquoi utiliser un état absorbant ?**
   - a) Pour éviter que le joueur ne gagne trop de points
   - b) Pour garantir que chaque politique atteindra éventuellement un état terminal, évitant ainsi des cycles infinis
   - c) Pour augmenter la difficulté du jeu

### Réponses

1. b) Une situation où les récompenses cumulées peuvent devenir infinies si le jeu ne se termine jamais
2. b) Utiliser un horizon fini pour terminer les épisodes après un nombre fixe de pas
3. b) Utiliser un facteur $$\gamma$$ (0 < $$\gamma$$ < 1) pour donner plus d'importance aux récompenses immédiates et réduire l'impact des récompenses futures
4. Mise en situation : Compréhension des concepts appliqués.
5. b) Pour garantir que chaque politique atteindra éventuellement un état terminal, évitant ainsi des cycles infinis

