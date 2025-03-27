-------------------------------------------------------
# Quiz sur l'actualisation (discounting)
-------------------------------------------------------

1. **Qu'est-ce que l'actualisation (discounting) dans le RL ?**
   - a) Ignorer les récompenses futures
   - b) Réduire l'impact des récompenses futures en utilisant un facteur $$\gamma$$ (0 < $$\gamma$$ < 1)
   - c) Augmenter la probabilité de succès des actions

2. **Quel est l'effet d'un facteur d'actualisation ($$\gamma$$) proche de 0 ?**
   - a) Mettre plus d'accent sur les récompenses futures
   - b) Mettre plus d'accent sur les récompenses immédiates
   - c) Ne pas affecter la stratégie de l'agent

3. **Comment calcule-t-on l'utilité cumulative avec l'actualisation ?**
   - a) En additionnant simplement toutes les récompenses
   - b) En utilisant la formule : $$U([r_0, \ldots, r_\infty]) = \sum_{t=0}^{\infty} \gamma^t r_t$$
   - c) En multipliant toutes les récompenses par un facteur constant

4. **Mise en situation :**
   - Un agent reçoit une séquence de récompenses [2, 3, 5] avec un facteur d'actualisation $$\gamma = 0.8$$. Calculez l'utilité cumulative.

5. **Pourquoi utilise-t-on l'actualisation dans le RL ?**
   - a) Pour simplifier les calculs
   - b) Pour éviter des utilités infinies et favoriser un équilibre entre récompenses immédiates et futures
   - c) Pour augmenter la difficulté des problèmes

### Réponses

1. b) Réduire l'impact des récompenses futures en utilisant un facteur $$\gamma$$ (0 < $$\gamma$$ < 1)
2. b) Mettre plus d'accent sur les récompenses immédiates
3. b) En utilisant la formule : $$U([r_0, \ldots, r_\infty]) = \sum_{t=0}^{\infty} \gamma^t r_t$$
4. Utilité cumulative : $$2 + 0.8 \times 3 + 0.8^2 \times 5 = 2 + 2.4 + 3.2 = 7.6$$
5. b) Pour éviter des utilités infinies et favoriser un équilibre entre récompenses immédiates et futures


