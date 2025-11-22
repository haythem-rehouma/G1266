# **Exemple : Évaluer le rendement d’un employé avec TD(λ)**

Imagine que tu veux évaluer **la performance d’un employé** (appelons-le Samir) au fil du temps.

Chaque semaine, Samir produit un résultat :

* Semaine 1 : pas très bon
* Semaine 2 : moyen
* Semaine 3 : très bon
* Semaine 4 : très bon
* Semaine 5 : catastrophique (bug majeur)
* Semaine 6 : correct
* etc.

Ton objectif est de maintenir une **note de performance** qui évolue semaine par semaine.

La question :
**Comment mettre à jour la note de Samir à chaque nouvelle semaine ?**

---

# **1. Si tu utilises TD(0)**

Tu décides :
“Je note Samir **uniquement** sur la dernière semaine.”

Si semaine 5 est catastrophique, tu baisses la note **fortement et immédiatement**, même si Samir était excellent les semaines précédentes.

C’est très réactif, mais souvent injuste ou instable.

---

# **2. Si tu utilises TD(2) ou TD(3)**

Tu décides :
“Je note Samir en regardant **les deux ou trois dernières semaines**.”

Par exemple TD(3) :

* Semaine 3, 4, 5 influencent la note.
* Une seule mauvaise semaine (5) modifie la note, mais les bonnes semaines (3–4) amortissent le choc.

C’est mieux, mais **tu dois choisir à l’avance** si tu regardes 2 semaines, 3 semaines, 4 semaines…

Mauvais choix = mauvaise évaluation.

---

# **3. Avec TD(λ), tu ne fixes pas un nombre de semaines**

Tu fais quelque chose de plus intelligent :

> **Tu prends en compte toutes les semaines passées, mais avec une importance décroissante.**

* La semaine juste avant → très importante
* La semaine précédente → un peu moins
* Celle encore avant → encore moins
* Et ainsi de suite…

La décroissance est contrôlée par λ :

* si **λ = 0** → seule la semaine dernière compte (comme TD(0))
* si **λ = 0.5** → la semaine dernière compte beaucoup, celle d'avant un peu, la troisième beaucoup moins
* si **λ = 0.9** → tu prends en compte quasiment tout l’historique, avec une décroissance lente

---

# **Exemple numérique simple**

Supposons :

* Semaine 4 → Samir obtient 9/10
* Semaine 5 → Samir obtient 2/10
* Semaine 6 → Samir obtient 7/10

Tu veux mettre à jour sa note après la semaine 6.

Avec **TD(λ)** :

* la semaine 6 compte beaucoup (poids 1)
* la semaine 5 compte avec poids λ
* la semaine 4 compte avec poids λ²
* la semaine 3 compte avec poids λ³
* etc.

Imaginons λ = 0.5 :

* Semaine 6 : poids 1
* Semaine 5 : poids 0.5
* Semaine 4 : poids 0.25

Donc même si la semaine 5 était très mauvaise, elle ne ruine pas toute l'évaluation, car :

1. les bonnes semaines précédentes comptent encore un peu,
2. la nouvelle semaine 6 corrige immédiatement,
3. et la mauvaise semaine 5 est pondérée par λ.

C’est exactement l’intelligence de TD(λ).

---

# **4. Pourquoi c’est utile en gestion du rendement ?**

Parce que :

1. **On ne veut pas juger un employé uniquement sur sa dernière performance** (TD(0) est trop dur).
2. **On ne veut pas attendre un long cycle complet** (comme Monte Carlo, trop lent).
3. **On ne veut pas fixer arbitrairement un nombre de semaines** (TD(3) est trop rigide).

TD(λ) permet :

* une adaptation immédiate
* tout en gardant en mémoire les performances passées
* mais sans que le passé domine
* grâce à un poids qui s’atténue naturellement

---

# **Résumé**

> **TD(λ) évalue un employé en combinant intelligemment les performances récentes et les performances passées, avec un poids qui diminue progressivement, ce qui produit une évaluation stable, juste et réactive.**


<br/>

## Annexe 1 - Clarifier la différence entre TD(n) et TD(λ) avec l’exemple de l’employé

Imagine que tu évalues le rendement d’un employé semaine après semaine.

### 1. TD(n) : n est un **nombre de semaines**

Avec **TD(n)**, tu décides **à l’avance** sur combien de semaines tu juges l’employé.
Par exemple, **TD(3)** veut dire :

> « Pour mettre à jour la note d’aujourd’hui, je regarde **exactement 3 semaines** de rendement de l’employé (par exemple les 3 dernières semaines), puis j’ajuste la note avec ça. »

Ici, **n est clairement un nombre de pas / de semaines**.
On ne parle que de TD(1), TD(2), TD(3), TD(4), etc., avec **n entier**.

En résumé :

* TD(3) = « je regarde un **bloc fixe** de 3 semaines, les autres ne comptent pas du tout dans cette mise à jour ».

---

### 2. TD(λ) : λ est un **coefficient de décroissance**, pas un nombre de semaines

Avec **TD(λ)**, ce n’est plus la même logique :
tu **ne choisis pas** un nombre fixe de semaines, tu dis plutôt :

> « Je vais tenir compte de **toutes** les semaines passées, mais avec une importance qui diminue progressivement. »

Par exemple, **TD(λ = 0.3)** veut dire :

> « Je prends en compte toutes les semaines passées, mais avec des poids qui décroissent :
> 1 pour la dernière semaine, 0.3 pour l’avant-dernière, 0.3² pour la semaine d’avant, 0.3³ pour encore avant, etc. »

Ici, **0.3 n’est pas un nombre de semaines**, c’est un **coefficient de décroissance entre 0 et 1** qui contrôle à quelle vitesse le passé “s’efface”.

En général :

* Si **λ = 0**, seule la dernière semaine compte vraiment → on retombe sur le comportement de **TD(0)**, très focalisé sur la semaine la plus récente.
* Quand **λ se rapproche de 1**, on donne presque autant d’importance à des semaines très anciennes qu’aux plus récentes → on se rapproche d’un comportement **type Monte Carlo**, où l’on juge l’employé sur une longue histoire complète.

Donc **λ = 1 ne veut pas dire “1 semaine”** :
λ = 1 correspond à « je prends pratiquement tout l’historique en compte », pas à « je regarde 1 pas ».

---

### 3. À ne pas confondre

On ne doit donc **jamais** lire :

* **TD(0.3)** comme si c’était **TD(3)**.

Ce sont **deux familles de méthodes différentes**, avec deux paramètres de nature différente :

* **TD(n)** :
  n entier → **nombre de pas / de semaines**.
* **TD(λ)** :
  λ réel dans [0, 1] → **vitesse de décroissance de l’importance du passé**.



### 4. Résumé


| Méthode         | Paramètre      | Interprétation dans l’exemple de l’employé                          |
|-----------------|----------------|------------------------------------------------------------------------|
| TD(3)           | n = 3 (entier) | Je regarde **exactement les 3 dernières semaines**, le reste ignoré. |
| TD(λ = 0.3)     | λ = 0.3        | Je regarde **toutes** les semaines, mais avec des poids 1, 0.3, 0.3²… |
| TD(λ = 0)       | λ = 0          | Seule la dernière semaine compte → équivalent à **TD(0)**.            |
| TD(λ → 1)       | λ ~ 1          | Presque tout l’historique compte → comportement proche Monte Carlo.   |


