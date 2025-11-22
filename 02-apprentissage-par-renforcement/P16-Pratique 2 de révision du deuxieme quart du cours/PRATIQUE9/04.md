

# **ÉTUDE DE CAS 1 — Gestion de l’Énergie dans une Maison Intelligente**

## **1. Élimination radicale**

* **Monte Carlo : Éliminé radicalement.** Impossible d’attendre la fin d’une journée ou d’une semaine pour mettre à jour le modèle. Le système doit ajuster sa stratégie heure par heure.
* **Q-Learning : Éliminé radicalement.** Le problème n’est pas centré sur des actions optimales dans un environnement interactif complexe, mais plutôt sur une prédiction et un ajustement continu.
* **SARSA : Éliminé radicalement.** La prudence liée à SARSA n’a pas d’intérêt ici. Le risque n’est pas lié à un agent qui fait face à des états dangereux, mais à de la prédiction énergétique.

## **2. Méthodes encore possibles**

* **TD(0) : Possible, mais trop court terme.** Il réagit rapidement, mais ne capture pas les variations lentes du coût ou de la météo.
* **TD(λ) : Très bon candidat.** Capture à la fois les variations instantanées et les tendances récentes.

## **3. Méthode recommandée**

**TD(λ)** est la méthode la plus adaptée, car elle met à jour à chaque pas de temps, avec une trace déclinante de l’historique, ce qui est essentiel pour suivre les changements de coût, météo, et consommation.

---

# **ÉTUDE DE CAS 2 — Navigation d’un Drone en Environnement Changeant**

## **1. Élimination radicale**

* **Monte Carlo : Éliminé radicalement.** Un drone ne peut pas attendre la fin d’un vol pour mettre à jour son modèle.
* **TD(0) : Éliminé radicalement.** Une seule observation n’est pas suffisante pour prendre de bonnes décisions dans un environnement physique dynamique.
* **Q-Learning : Éliminé radicalement.** Hors politique agressif, instable en environnement non stationnaire. Un drone ne peut pas se permettre d’apprendre une politique trop risquée.

## **2. Méthodes encore possibles**

* **SARSA : Possible.** S’adapte à un environnement stochastique avec prudence.
* **TD(λ) : Excellent candidat.** Approche incrémentale adaptée à un environnement où les signaux se propagent sur plusieurs pas.

## **3. Méthode recommandée**

**TD(λ)** est recommandé, car il permet des mises à jour incrémentales tout en tenant compte des dernières séquences de mouvements, ce qui est crucial pour les vents, obstacles en mouvement et réactivité du drone.

---

# **ÉTUDE DE CAS 3 — Anticipation des Demandes dans un Supermarché**

## **1. Élimination radicale**

* **TD(0) : Éliminé radicalement.** Le comportement de consommation ne se décide pas sur un seul pas temporel.
* **Monte Carlo : Éliminé radicalement.** Les épisodes saisonniers durent des semaines ou des mois. Attendre la fin de la saison pour mettre à jour le modèle est inutilisable opérationnellement.
* **SARSA : Éliminé radicalement.** La prudence et les interactions agent-environnement n’ont aucun rôle ici.
* **Q-Learning : Éliminé radicalement.** Le problème n’est pas un problème d’action optimale, mais d’anticipation continue.

## **2. Méthodes encore possibles**

* **TD(λ) : Très bon candidat.** Permet de capturer des tendances glissantes et de s’adapter aux évolutions graduelles des ventes.

## **3. Méthode recommandée**

**TD(λ)** est la meilleure méthode, car elle actualise les prédictions continuellement tout en tenant compte de plusieurs pas temporels, ce qui est essentiel pour suivre les comportements d’achat saisonniers et les micro-tendances.

---

# **ÉTUDE DE CAS 4 — Jeu Vidéo de Combat (Agent VS Adversaire)**

## **1. Élimination radicale**

* **Monte Carlo : Éliminé radicalement.** Le jeu nécessite une adaptation instantanée, pas un apprentissage après un match complet.
* **TD(0) : Éliminé radicalement.** Trop court terme pour capturer les séquences d’actions adverses.

## **2. Méthodes encore possibles**

* **Q-Learning : Possible.** Très performant si l’adversaire est déterministe et stable. Peut trouver des stratégies agressives.
* **SARSA : Excellent candidat.** Approprié si l’adversaire adopte des stratégies mouvantes, stochastiques ou adaptatives.

## **3. Méthode recommandée**

**SARSA** est recommandé lorsque l’adversaire n’est pas déterministe, car elle apprend une politique prudente basée sur ses propres actions réelles.
**Q-Learning** peut être retenu seulement si l’environnement est stable.

---

# **ÉTUDE DE CAS 5 — Répartition de Charge dans un Réseau de Serveurs**

## **1. Élimination radicale**

* **Monte Carlo : Éliminé radicalement.** Impossible d’attendre la fin de la journée pour adapter la répartition de charge.
* **Q-Learning : Éliminé radicalement.** Les politiques agressives sont instables dans un centre de données. Le risque de surcharge instantanée est trop grand.
* **SARSA : Non éliminé, mais moins optimal.** Possible dans des cas où il faut éviter les surcharges extrêmes, mais insuffisant pour capturer les tendances temporelles.

## **2. Méthodes encore possibles**

* **TD(0) : Possible, mais trop limité.** Réagit très vite, mais ne capture pas les tendances de charge.
* **TD(λ) : Excellent candidat.** Combine réactivité et capture de tendances (pics, creux, patterns journaliers).

## **3. Méthode recommandée**

**TD(λ)** est le meilleur choix, car la charge des serveurs dépend d’une séquence de variations et non d’un seul instant, et il permet des ajustements rapides en plus d’une sensibilité aux patterns récents.

---

# **ÉTUDE DE CAS 6 — Prédiction des Mouvements de Marché Financier**

## **1. Élimination radicale**

* **Monte Carlo : Éliminé radicalement.** Un modèle financier doit réagir immédiatement et non à la fin d’un épisode.
* **Q-Learning : Éliminé radicalement.** Le marché n’est pas un environnement interactif approprié au contrôle d’actions optimales, mais à la prédiction continue.
* **SARSA : Éliminé radicalement.** Le marché ne requiert pas une politique prudente d’actions, mais une mise à jour de prédiction.
* **TD(0) : Non éliminé mais insuffisant.** Réagit vite, mais ne capture pas les dépendances multi-temps.

## **2. Méthodes encore possibles**

* **TD(λ) : Très bon candidat.** Capture les dépendances temporelles, tendance, momentum, volatilité, propagation des micro-mouvements.

## **3. Méthode recommandée**

**TD(λ)** est la meilleure approche, car elle met à jour les prédictions à chaque nouvelle donnée tout en intégrant un historique pondéré des variations précédentes, indispensable dans un marché volatile.


