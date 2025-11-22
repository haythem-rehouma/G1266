## 1. L’idée générale

TD(λ), c’est une manière **d’apprendre à partir de l’expérience en ligne** en mélangeant :

* ce que je vois **tout de suite** (court terme),
* ce que je vois **un peu plus tard** (moyen terme),
* ce qui se passe **encore plus loin** (plus long terme),

avec un **bouton de réglage** qui s’appelle λ (lambda).

---

## 2. Imagine que tu évalues une série

Tu regardes une série Netflix et tu veux donner une note à l’épisode 1.

Trois stratégies extrêmes :

1. **TD(0)** :
   Tu notes l’épisode 1 **après seulement les 5 premières minutes**.
   Très rapide, mais tu risques de te tromper.

2. **Monte Carlo** :
   Tu attends d’avoir vu **toute la saison** avant de noter l’épisode 1.
   Très précis, mais beaucoup trop lent.

3. **TD(n)** :
   Tu décides :
   “Je regarde **exactement 3 épisodes** (1, 2, 3),
   puis je donne une note à l’épisode 1.”
   C’est mieux, mais tu dois choisir ce “3” à l’avance.

TD(λ) fait quelque chose de plus intelligent :

> “Je vais tenir compte de l’épisode 2, un peu de l’épisode 3, un peu moins de l’épisode 4, encore moins du 5, etc., en diminuant progressivement leur importance.”

C’est un **mélange pondéré** de “regarder un peu”, “regarder moyen” et “regarder plus loin”.

---

## 3. Le rôle de λ (lambda)

λ est un nombre entre 0 et 1.

* **λ = 0**
  → tu n’utilises que ce qui se passe immédiatement après
  → tu retombes sur **TD(0)**.

* **λ proche de 1**
  → tu donnes de l’importance à des événements plus lointains dans le temps
  → tu te rapproches de **Monte Carlo** (tu tiens compte de toute la suite).

* **0 < λ < 1**
  → tu fais un compromis :
  court terme + moyen terme + un peu de long terme.

Tu peux voir λ comme un **curseur de patience** :

* petit λ → “je suis impatient, je veux apprendre très vite, même si c’est un peu approximatif” ;
* grand λ → “je suis plus patient, je veux tenir compte d’une histoire plus longue avant de juger”.

---

## 4. Comment ça fonctionne dans la tête (intuitivement)

Tu peux imaginer que l’algorithme garde une **trace** des états récemment visités.

* Plus un état est récent, plus il a une **trace forte**.
* Plus il est ancien, plus sa trace **s’efface**.

Quand une nouvelle récompense arrive (bonne ou mauvaise nouvelle), l’algorithme :

1. calcule une “erreur” entre ce qu’il attendait et ce qui s’est passé,
2. propage cette erreur vers les états passés,
   mais **avec une intensité décroissante** (ce qui est plus récent reçoit une plus grande correction).

Cette “intensité décroissante” est contrôlée par λ.

---

## 5. Pourquoi TD(λ) est plus malin que TD(0) ou TD(n)

* **Par rapport à TD(0)** :
  TD(0) regarde seulement “un pas” devant lui.
  Il ne voit pas les effets un peu plus tard.
  TD(λ) corrige en utilisant plusieurs pas, donc il apprend des tendances plus riches.

* **Par rapport à TD(n)** :
  TD(n) fixe un nombre de pas n, ce qui est rigide :
  si n est mal choisi, l’algorithme est soit trop myope, soit trop lent.
  TD(λ), lui, ne se fixe pas un seul n :
  il mélange **tous** les n (1, 2, 3, 4, …) avec des poids qui décroissent ((\lambda^{n-1})).

En pratique, TD(λ) est souvent :

* plus **stable** que TD(n) (tu n’es pas coincé avec un n mal choisi),
* plus **performant** que TD(0) dans des environnements un peu complexes,
* plus **rapide** que Monte Carlo, car il n’attend pas la fin de l’épisode.

---

## 6. Résumé en une seule phrase

> **TD(λ)**, c’est une méthode qui apprend en ligne en mélangeant toutes les mises à jour possibles à différents horizons temporels, avec un curseur λ qui contrôle combien tu fais confiance au court terme versus au long terme.


