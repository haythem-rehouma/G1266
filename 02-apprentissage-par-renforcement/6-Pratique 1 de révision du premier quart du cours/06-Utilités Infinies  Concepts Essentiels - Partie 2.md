------------------------------------------------------------------
# Exercices sur les utilités infinies
------------------------------------------------------------------

1. **Exercice de réflexion :**
   - Imaginez un jeu où un agent reçoit une récompense de +1 à chaque étape sans fin. Pourquoi est-il problématique de calculer l'utilité totale sans ajustement ? Proposez une solution.

2. **Calcul avec actualisation :**
   - Considérez un facteur d'actualisation $$\gamma = 0.9$$. Si un agent reçoit une séquence de récompenses de [1, 1, 1, ...], calculez l'utilité cumulée pour les 5 premières étapes.

3. **Mise en situation :**
   - Un robot doit nettoyer une pièce et reçoit +10 pour chaque zone nettoyée et -5 pour chaque collision. Utilisez un horizon fini de 10 étapes pour déterminer la stratégie optimale.

4. **État absorbant :**
   - Décrivez un scénario où l'utilisation d'un état absorbant serait bénéfique. Expliquez comment cela empêche les utilités infinies.

5. **Comparaison des solutions :**
   - Comparez les avantages et inconvénients de l'horizon fini et de l'actualisation comme solutions aux utilités infinies.

### Réponses suggérées

1. Sans ajustement, l'utilité devient infinie car le jeu ne se termine jamais. Utiliser un facteur d'actualisation ou un horizon fini peut résoudre ce problème.
2. Utilité cumulée avec $$\gamma = 0.9$$ est $$1 + 0.9 + 0.81 + 0.729 + 0.6561 = 4.0951$$.
3. Avec un horizon fini, le robot peut maximiser les zones nettoyées tout en minimisant les collisions sur 10 étapes.
4. Un état absorbant garantit que le jeu se termine, évitant ainsi des cycles infinis et des utilités infinies.
5. L'horizon fini simplifie le calcul mais peut mener à des politiques non stationnaires, tandis que l'actualisation offre une approche plus continue mais nécessite le choix d'un $$\gamma$$ approprié.
