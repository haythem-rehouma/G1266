
## 1. Rappel : TD-Learning (Temporal Difference Learning)

Le **TD-Learning** est une famille de méthodes d’apprentissage par renforcement qui met à jour les valeurs **en ligne**, c’est-à-dire **au fil de l’expérience**, sans attendre la fin de l’épisode.

Il s’inspire :
- de **Monte Carlo** (échantillonnage basé sur l’expérience),
- et de **la Programmation Dynamique** (mise à jour via estimations).

### Formule TD(0) — version explicite :

$$
V(s) \leftarrow (1 - \alpha)V(s) + \alpha \big[ r + \gamma V(s') \big]
$$

On met à jour **la valeur estimée de l’état courant** à chaque pas, de manière incrémentale.

---

## 2. SARSA : définition pédagogique

**SARSA** signifie :

- **S** : État actuel $$s$$  
- **A** : Action exécutée $$a$$  
- **R** : Récompense reçue $$r$$  
- **S** : État suivant $$s'$$  
- **A** : Action suivante choisie $$a'$$  

C’est une méthode TD appliquée à la fonction d’action-valeur $$Q(s, a)$$.  
Elle met à jour **en fonction de l’action réellement effectuée dans l’état suivant**.

### Formule SARSA — version explicite :

$$
Q(s, a) \leftarrow (1 - \alpha)Q(s, a) + \alpha \big[ r + \gamma Q(s', a') \big]
$$

Ici, $$Q(s', a')$$ correspond à **l’action réellement suivie** selon la politique d’exploration.

---

## 3. Intuition de SARSA : apprentissage "réaliste"

Imagine un enfant qui apprend à marcher dans une pièce inconnue :

- Il agit en suivant **sa stratégie actuelle**, parfois aléatoire.
- À chaque pas, il reçoit un retour (récompense).
- Il apprend **en fonction des actions qu’il effectue vraiment**, même si elles ne sont pas parfaites.

**SARSA est donc on-policy** :  
> Il apprend **ce que la politique en cours produit comme comportement**, en intégrant exploration et hésitations.

---

## 4. Différence avec Q-Learning (autre TD-learning)

**Q-Learning** est aussi une méthode de TD-Learning, mais elle est **off-policy**.

- Il apprend **comme s’il choisissait toujours la meilleure action possible**, même si ce n’est pas le cas dans la pratique.
- Il met donc à jour en fonction de **la valeur maximale estimée** dans l’état suivant.

### Formule Q-Learning — version explicite :

$$
Q(s, a) \leftarrow (1 - \alpha)Q(s, a) + \alpha \big[ r + \gamma \max_{a'} Q(s', a') \big]
$$

Contrairement à SARSA, l’action suivante $$a'$$ n’est pas celle suivie, mais **celle qui aurait donné la meilleure récompense espérée**.

---

## 5. SARSA vs TD(0)

- **TD(0)** met à jour des **valeurs d’état** $$V(s)$$
- **SARSA** applique le même principe mais aux **valeurs d’action** $$Q(s, a)$$

On peut voir **SARSA comme une version TD(0)** qui apprend à la granularité des couples (état, action), avec une politique suivie.

---

## 6. Tableau récapitulatif

| Méthode       | Type de politique | Ce qu’on met à jour         | Action réellement suivie ? | Formule de mise à jour |
|---------------|-------------------|------------------------------|-----------------------------|-------------------------|
| TD(0)         | On-policy          | $$V(s)$$                    | Pas d’action                | $$V(s) \leftarrow (1 - \alpha)V(s) + \alpha [r + \gamma V(s')]$$ |
| SARSA         | On-policy          | $$Q(s, a)$$                 | Oui                         | $$Q(s, a) \leftarrow (1 - \alpha)Q(s, a) + \alpha [r + \gamma Q(s', a')]$$ |
| Q-Learning    | Off-policy         | $$Q(s, a)$$                 | Non                         | $$Q(s, a) \leftarrow (1 - \alpha)Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a')]$$ |
