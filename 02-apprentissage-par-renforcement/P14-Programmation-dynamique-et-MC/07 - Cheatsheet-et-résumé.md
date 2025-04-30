# Introduction à l'évaluation des politiques avec la méthode Monte Carlo

Dans cette section, nous allons explorer l'évaluation des politiques en utilisant la méthode Monte Carlo, une approche sans modèle qui ne nécessite pas de connaître à l'avance les détails de l'environnement.

## Limitations de la programmation dynamique

La programmation dynamique (DP) présente certaines limitations :
- Elle nécessite une **connaissance complète** de l'environnement, y compris la matrice de transitions et la matrice de récompenses.

## Méthodes sans modèle

Les méthodes sans modèle, comme Monte Carlo, n'ont pas besoin de connaître ces informations à l'avance pour fonctionner.

## Objectif

Nous allons utiliser la méthode Monte Carlo pour **évaluer une politique** dans l'environnement **FrozenLake**, en supposant que nous n'avons pas accès à sa matrice de transition ni à sa matrice de récompenses.

## Fonctionnement de l'évaluation Monte Carlo

Nous utilisons le **retour empirique** au lieu du retour attendu pour estimer la fonction de valeur.

### Le retour d'un processus

Le **retour** est calculé par la formule :

$$
G_t = \sum_k \gamma^k R_{t+k+1}
$$

### Deux approches d'évaluation

1. **Prédiction Monte Carlo de première visite** (First-visit MC)
2. **Prédiction Monte Carlo de toutes les visites** (Every-visit MC)

Nous utiliserons la méthode **First-visit MC** pour sa simplicité.

## Exemple avec l'environnement FrozenLake

Voici les étapes pour appliquer la méthode First-visit Monte Carlo :

1. Importer les bibliothèques nécessaires (PyTorch et Gym)
2. Définir la fonction qui simule un épisode
3. Définir la fonction qui évalue la politique
4. Simuler 10 000 épisodes avec un taux de discount γ = 1
5. Utiliser la politique optimale obtenue précédemment comme entrée

## Conclusion

L'évaluation des politiques avec Monte Carlo est une méthode **sans modèle**, utile lorsque nous n'avons pas accès aux informations complètes sur l'environnement. Elle est flexible et adaptée aux situations réelles où les informations sur les transitions et les récompenses ne sont pas disponibles à l'avance.

<br/>

# Annexe 1 - FrozenLake


**FrozenLake** est un environnement d’apprentissage par renforcement représentant une grille de glace où un agent doit atteindre un but (`G`) en partant d’un point de départ (`S`), tout en évitant de tomber dans des trous (`H`). Le sol est glissant, ce qui rend les déplacements incertains : même si l’agent choisit une direction, il peut glisser ailleurs, introduisant de la stochastique (`is_slippery=True`). Cet environnement est souvent utilisé pour expérimenter des algorithmes comme le **Q-Learning**, **SARSA**, ou encore les **méthodes Monte Carlo**, qui sont bien adaptées ici car l’environnement est discret (nombre fini d’états et d’actions). Avec Monte Carlo, on attend la fin de chaque épisode (trajectoire complète) pour mettre à jour les estimations de valeur, ce qui permet d’analyser l’effet des décisions sur le long terme. Enfin, FrozenLake peut aussi être configuré sans aléa (`is_slippery=False`), pour un apprentissage plus simple et déterministe.



