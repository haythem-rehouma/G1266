

## **Leçon 6 – Laisser l’agent apprendre**

### Que veut dire "apprendre" pour un agent ?

L’agent commence **sans rien savoir**.
Il va **essayer plein d’actions** dans son environnement.
Et à chaque fois, il reçoit une **récompense**.

> Petit à petit, il **comprend ce qui marche bien**… et **évite ce qui marche mal**.



### 1. Il apprend par essais et erreurs

L’agent ne lit pas un manuel.
Il **essaie une action**, regarde le **résultat**, et **réessaie autrement**.

C’est comme :

* un bébé qui apprend à marcher,
* ou quelqu’un qui apprend un jeu vidéo en jouant plusieurs fois.



### 2. Exemple très simple

Imaginons que l’agent tourne trop à droite → il sort de la piste → il perd des points.
La fois suivante, il tourne un peu moins → il reste sur la route → il gagne des points.

> L’agent **mémorise cette expérience** : "tourner un peu moins est mieux".



### 3. L’agent ne réussit pas tout de suite

* Au début, il fait n’importe quoi.
* Ensuite, il **fait mieux de temps en temps**.
* Enfin, il **trouve ce qui fonctionne le plus souvent**.

Ce processus prend :

* du **temps**,
* beaucoup de **répétitions**,
* et **beaucoup d’épisodes d’apprentissage** (des essais complets).



### 4. Comment on sait qu’il apprend ?

On regarde si :

* La **récompense moyenne** augmente.
* Le **comportement devient plus stable**.
* Il **réussit de plus en plus souvent**.



### 5. Résumé visuel

```
L’agent fait une action → reçoit un score
→ Il garde les bonnes actions
→ Il oublie les mauvaises
→ Il répète ce qui marche
```

