----------------------------------------------
# Exercices sur la Policy
----------------------------------------------

1. **Exercice de définition :**
   - Décrivez ce qu'est une policy dans le contexte du RL et donnez un exemple d'une policy déterministe et d'une policy stochastique.

2. **Exercice de calcul :**
   - Un agent dans un labyrinthe peut aller vers le haut, le bas, la gauche ou la droite. Proposez une policy déterministe pour atteindre la sortie en partant du coin inférieur gauche.

3. **Mise en situation :**
   - Imaginez un agent qui doit choisir entre deux actions : Action A (récompense immédiate de 5) et Action B (récompense de 10 après deux étapes). Quelle policy serait optimale si le facteur d'actualisation est élevé ? Et si le facteur est bas ?

4. **Exercice de comparaison :**
   - Comparez les avantages et inconvénients d'une policy déterministe par rapport à une policy stochastique dans un environnement incertain.

5. **Exercice de réflexion :**
   - Pourquoi est-il important pour un agent d'adapter sa policy en fonction des changements dans l'environnement ? Donnez un exemple pratique.

### Réponses suggérées

1. Une policy est une stratégie qui détermine quelle action prendre dans chaque état. 
   - *Déterministe* : Toujours aller à droite.
   - *Stochastique* : Choisir entre aller à droite ou en haut avec des probabilités égales.

2. Policy déterministe : Toujours aller vers le haut jusqu'à atteindre la ligne supérieure, puis aller à droite jusqu'à la sortie.

3. 
   - Facteur élevé : Choisir Action B pour maximiser les gains futurs.
   - Facteur bas: Choisir Action A pour maximiser les gains immédiats.

4. 
   - *Déterministe* : Simplicité et prévisibilité, mais manque de flexibilité.
   - *Stochastique* : Plus adapté aux environnements incertains, mais plus complexe à gérer.

5. L'adaptation est cruciale pour maximiser les récompenses dans des environnements dynamiques. Par exemple, un robot aspirateur doit ajuster sa stratégie si de nouveaux obstacles apparaissent.

