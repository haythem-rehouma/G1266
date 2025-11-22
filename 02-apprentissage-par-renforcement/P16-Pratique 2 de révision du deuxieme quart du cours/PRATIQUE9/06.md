
## 1. TD(n) : horizon **fixe**

**Idée :**
On choisit un entier (n) et on met à jour avec un **retour à n-pas** (n-step return).

Pour un état (S_t) :

$$
G_t^{(n)} = R_{t+1} + \gamma R_{t+2} + \dots + \gamma^{n-1} R_{t+n} + \gamma^n V(S_{t+n})
$$

Mise à jour typique :

[
V(S_t) \leftarrow V(S_t) + \alpha\big( G_t^{(n)} - V(S_t) \big)
]

Caractéristiques :

* Tu fixes **un horizon** (n) à l’avance.
* (n = 1) donne TD(0), (n) grand se rapproche de Monte Carlo.
* Plus (n) est grand :
  – moins de biais,
  – mais plus de variance et plus de délai avant la mise à jour (il faut attendre d’avoir les (n) récompenses).
* C’est une méthode “**n-step** pure” : toujours exactement (n) pas de lookahead.

---

## 2. TD(λ) : **mélange de tous les TD(n)**

**Idée clé :**

TD(λ) ne se limite pas à un seul horizon (n).
Il combine **tous** les retours à (n) pas, avec une pondération géométrique par (\lambda).

Forme “forward view” (théorique) :

$$
G_t^{(\lambda)}
= (1-\lambda)\sum_{n=1}^{\infty} \lambda^{n-1} G_t^{(n)}
$$

Donc :

* Si (\lambda=0) → tu n’utilises que (G_t^{(1)}) ⇒ TD(0).
* Si (\lambda \to 1) → tu te rapproches de Monte Carlo.
* Pour (0 < \lambda < 1) → tu fais un **mélange pondéré** de TD(1), TD(2), TD(3), …

En pratique, on implémente TD(λ) avec des **traces d’éligibilité** (backward view) :

$$
e_t(s) = \gamma \lambda e_{t-1}(s) + \mathbf{1}{s = S_t}
$$

$$
V(s) \leftarrow V(s) + \alpha , \delta_t , e_t(s)
$$

où (\delta_t) est l’erreur TD au temps (t).

---

## 3. Différences conceptuelles majeures

### a) Horizon

* **TD(n)** : un seul horizon fixe (n).
  “Je regarde exactement (n) pas dans le futur.”
* **TD(λ)** : **tous** les horizons (1,2,3,\dots), avec poids décroissant (\lambda^{n-1}).
  “Je regarde court, moyen et un peu long terme en même temps, avec une décroissance contrôlée.”

---

### b) Paramétrage

* **TD(n)** : tu choisis **un entier** (n).
  Mauvais choix de (n) → méthode fragile.
* **TD(λ)** : tu choisis **un réel** (\lambda \in [0,1]).
  Cela te donne un contrôle continu entre TD(0) et Monte Carlo.

---

### c) Biais / variance

* **TD(n)** :
  – petit (n) → plus de biais, moins de variance
  – grand (n) → moins de biais, plus de variance
* **TD(λ)** :
  – en moyenne, fait un compromis “lissé” en combinant plusieurs (n),
  – il est souvent **plus stable** que de choisir un seul (n).

---

### d) Implémentation pratique

* **TD(n)** (forward) :
  tu dois stocker les (n) prochaines récompenses avant de mettre à jour → délai.
* **TD(λ)** (backward) :
  tu mets à jour **à chaque pas de temps** grâce aux traces d’éligibilité → algorithmique très adaptée à l’on-line.

---

## 4. Résumé ultra clair

* **TD(n)**

  * Un seul horizon de prédiction.
  * “Je regarde exactement (n) pas devant et j’utilise ça comme cible.”

* **TD(λ)**

  * C’est une **moyenne pondérée** de tous les TD(n).
  * “Je combine toutes les cibles à 1,2,3,… pas avec un poids (\lambda^{n-1}).”
  * Implémenté via les traces d’éligibilité, très naturel en on-line.

