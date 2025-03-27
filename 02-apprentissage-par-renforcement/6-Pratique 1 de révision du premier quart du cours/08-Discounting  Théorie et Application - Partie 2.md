----------------------------------------------------------
# Exercices sur l'actualisation (discounting)
----------------------------------------------------------

1. **Exercice de calcul :**
   - Un agent reçoit une séquence de récompenses [4, 3, 2, 1] avec un facteur d'actualisation $$\gamma = 0.9$$. Calculez l'utilité cumulative.

2. **Exercice de réflexion :**
   - Expliquez pourquoi un facteur d'actualisation proche de 0 favorise les récompenses immédiates par rapport aux récompenses futures.

3. **Mise en situation :**
   - Imaginez un jeu où chaque action réussie rapporte +5 points, mais chaque échec coûte -2 points. Comment le choix du facteur $$\gamma$$ influence-t-il la stratégie de l'agent ?

4. **Comparaison des scénarios :**
   - Comparez les utilités cumulatives pour deux séquences de récompenses [5, 5, 5] et [10, 0, 0] avec $$\gamma = 0.8$$. Quelle séquence est préférée et pourquoi ?

5. **Exercice d'application :**
   - Décrivez un scénario dans lequel un état absorbant serait nécessaire pour éviter des utilités infinies et expliquez comment l'actualisation pourrait également aider.

### Réponses suggérées

1. Utilité cumulative : $$4 + 0.9 \times 3 + 0.9^2 \times 2 + 0.9^3 \times 1 = 4 + 2.7 + 1.62 + 0.729 = 9.049$$.
2. Un $$\gamma$$ proche de 0 signifie que les récompenses futures sont fortement réduites, donc les décisions sont basées principalement sur les récompenses immédiates.
3. Un facteur $$\gamma$$ élevé incite l'agent à prendre des risques pour des gains futurs, tandis qu'un $$\gamma$$ bas favorise la sécurité et les gains immédiats.
4. Calcul des utilités cumulatives :
   - [5, 5, 5]: $$5 + 0.8 \times 5 + 0.8^2 \times 5 = 5 + 4 + 3.2 = 12.2$$
   - [10, 0, 0]: $$10 + 0 + 0 = 10$$
   - La première séquence est préférée car elle offre une utilité cumulative plus élevée.
5. Un état absorbant garantit une fin à la tâche pour éviter des cycles infinis, tandis que l'actualisation réduit l'impact des récompenses futures, aidant à gérer les utilités infinies.


