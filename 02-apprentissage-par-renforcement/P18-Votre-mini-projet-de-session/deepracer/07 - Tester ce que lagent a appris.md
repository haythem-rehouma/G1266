
## **Leçon 7 – Tester ce qu’il a appris**

### Pourquoi faut-il tester l’agent ?

Quand l’agent a terminé son entraînement, on veut **vérifier** s’il a **vraiment compris ce qu’on attendait de lui**.

> Le test permet de **voir ce qu’il a retenu** et **comment il se comporte**.


### 1. Tester, ce n’est plus apprendre

Pendant l’apprentissage, l’agent reçoit des récompenses et continue à s’améliorer.
Mais **pendant le test**, il n’apprend plus.
Il **fait ce qu’il a appris**, sans ajustement.

C’est comme :

* passer un examen à la fin d’un cours,
* jouer une partie avec les règles bien connues.



### 2. Ce qu’on regarde pendant le test

* Est-ce qu’il **reste sur la piste** ?
* Est-ce qu’il **va jusqu’au bout** ?
* Est-ce qu’il est **rapide et fluide** ?
* Est-ce qu’il **fait moins d’erreurs qu’avant** ?



### 3. Exemple de test (voiture)

* La voiture fait un tour complet sans toucher les murs.
* Elle ne s’arrête pas sans raison.
* Elle ne sort pas de la route.
* Elle prend bien les virages.

> Si tout cela fonctionne bien, on peut dire : **"l’agent a appris."**


### 4. Et si le test se passe mal ?

Pas grave. Cela arrive souvent.

On peut alors :

* **corriger la fonction de récompense**,
* **changer les actions autorisées**,
* **lancer un nouvel entraînement**,
* ou **tester sur une piste plus simple**.


### 5. Résumé visuel

```
Entraînement terminé
→ On teste l’agent sans l’aider
→ S’il réussit → il a appris
→ Sinon → on peut améliorer et recommencer
```


