# **Étude de Cas 6 : Prédiction des Mouvements de Marché Financier**

Un trader algorithmique souhaite prédire les variations futures du marché boursier à partir :

* de données historiques de prix,
* de signaux récents (trend, momentum, volatilité),
* d’événements soudains (news, annonces économiques),
* de microstructures de marché (ticks, spreads, volume).

Le modèle doit être **extrêmement réactif**, tout en exploitant les corrélations temporelles des dernières secondes ou minutes. Le marché est un environnement classique de non-stationnarité : les distributions changent, les tendances s’inversent, et les signaux peuvent perdre leur pertinence du jour au lendemain.

---

# **1. Quel algorithme recommander ?**

Dans ce contexte, l’algorithme le plus adapté est **TD(λ)**.

## **Pourquoi TD(λ) ?**

### **a) Le marché exige une mise à jour en temps réel**

TD(λ) permet des mises à jour incrémentales :

* à chaque nouvelle observation,
* sans attendre un épisode complet (comme Monte Carlo),
* avec un coût computationnel faible,
* avec la possibilité d’intégrer plusieurs pas temporels.

Dans un système de trading algorithmique, l’apprentissage doit être **online**, **continu** et **instantané**. TD(λ) correspond exactement à ce besoin.

---

### **b) Le marché dépend fortement de l’historique récent**

TD(0) ne regarde qu’un seul pas (t → t+1). C’est trop court.

Dans la vraie vie, les mouvements de prix dépendent de plusieurs signaux récents :

* momentum à 3–5 pas,
* micro-tendances,
* séquences de ticks,
* réactions graduelles à des news,
* volatilité qui se propage sur plusieurs minutes.

TD(λ) prend en compte **une trace déclinante du passé**, ce qui est parfaitement aligné avec les dynamiques financières.

---

### **c) Q-Learning et SARSA ne sont pas adaptés à ce problème**

Ici, l’objectif n’est pas d’apprendre une **politique optimale d’action**, mais d’apprendre une **fonction de valeur ou de prédiction**.

Le trader cherche à prédire un signal (hausse, baisse, probabilité de mouvement) — pas à choisir une action directement dans un environnement interactif.

Donc :

* Q-Learning est inutile (il optimise actions vs récompenses).
* SARSA aussi (politique prudente dans un environnement interactif).
* Le trading n’est pas un problème d’environnement "agent → action → récompense".
  Il s'agit plutôt d’un **problème de prédiction continue**.

---

### **d) Monte Carlo est inutilisable en trading réel**

MC attend la fin de l’épisode.
Or un épisode en trading représente :

* une journée,
* une session complète,
* voire un mois.

Attendre la fin de la journée pour mettre à jour le modèle est **impossible** :

* le prix change chaque seconde,
* les opportunités disparaissent immédiatement,
* les régimes de marché changent dans la journée.

TD(λ) est la seule méthode adaptée à cette fréquence.

---

# **2. Pourquoi TD(λ) est particulièrement utile dans un marché volatil ?**

### **a) TD(λ) équilibre instantané + mémoire courte**

En marché volatil, certaines informations doivent être oubliées très rapidement (vieille tendance), et d'autres doivent rester quelques instants (volatilité locale, momentum).

TD(λ) permet :

* λ faible → modèle très réactif, oubli rapide
* λ moyen → capture de micro-tendances
* λ élevé → suit une tendance plus longue

Ce degré de liberté est essentiel dans la finance, où les régimes fluctuent.

---

### **b) TD(λ) réduit la variance sans sacrifier la réactivité**

Les prix en finance sont extrêmement bruités.
Utiliser seulement TD(0) crée un signal :

* trop instable,
* trop sensible au bruit,
* sujet à des inversions fréquentes.

TD(λ) stabilise les prédictions tout en restant suffisamment rapide pour suivre le marché.

---

### **c) TD(λ) capture des dépendances temporelles multi-échelles**

En finance, certains signaux se propagent :

* en quelques millisecondes (microstructure),
* en quelques secondes (tape reading),
* en quelques minutes (order flow trends).

Avec les traces d’éligibilité, TD(λ) :

* attribue plus de poids aux signaux récents,
* donne une importance décroissante au passé,
* le fait de manière adaptative,
* sans coût computationnel excessif.

---

### **d) TD(λ) gère bien les régimes non-stationnaires**

Un marché volatil peut changer de comportement sans prévenir.
TD(λ) permet :

* de s’adapter rapidement à un nouveau régime,
* tout en ne réagissant pas de façon excessive aux fluctuations isolées,
* ce qui réduit les faux signaux.

Il offre un compromis optimal entre stabilité et adaptabilité.

---

# **Conclusion de l’Étude de Cas 6**

1. **TD(λ)** est l’algorithme recommandé car il combine mise à jour immédiate, capture des dépendances temporelles, robustesse au bruit et adaptabilité à la non-stationnarité.

2. **TD(λ)** est particulièrement avantageux dans un marché volatil car :

   * il réagit rapidement aux changements,
   * il stabilise la prédiction malgré le bruit,
   * il pondère intelligemment l’historique récent,
   * il s’ajuste aux régimes de marché en temps réel.

