

## Étude de Cas 3 : Anticipation des Demandes dans un Supermarché

### 1. Contexte opérationnel

Le supermarché doit décider régulièrement (par exemple chaque jour ou chaque semaine) des quantités à commander pour différents produits, en tenant compte :

* des variations saisonnières (produits estivaux en été, chocolat en hiver, etc.) ;
* des tendances de consommation (un produit devient progressivement populaire, un autre perd de l’intérêt) ;
* des événements particuliers (promotions, fêtes, météo, événements locaux) ;
* de l’incertitude sur la demande réelle (fluctuations imprévisibles).

L’objectif n’est pas seulement de prédire la demande à un instant donné, mais de :

* s’adapter progressivement aux changements de comportement des clients ;
* éviter les ruptures de stock ;
* éviter les surstocks coûteux.

L’environnement n’est pas stationnaire : les habitudes des consommateurs évoluent, la saison change, les promotions perturbent la demande.

---

## 2. Méthode la plus adaptée : TD(λ)

### 2.1 Choix de la méthode

Parmi Monte Carlo, TD(0), TD(λ), Q-Learning et SARSA, la méthode la plus adaptée à ce contexte est **TD(λ)**.

La raison principale est que le supermarché a besoin d’un mécanisme :

* capable de s’adapter progressivement aux tendances de consommation ;
* sensible aux dépendances temporelles (les ventes d’aujourd’hui dépendent de ce qui s’est passé les jours précédents, et annoncent ce qui va se passer dans les prochains jours) ;
* qui ne nécessite pas d’attendre la fin d’un “épisode complet” (par exemple une saison entière) pour mettre à jour les estimations.

TD(λ) est précisément conçu pour ce type de contexte, car il combine :

* la réactivité d’un apprentissage incrémental (comme TD(0)) ;
* une capacité à prendre en compte plusieurs pas de temps passés (comme TD(n)) grâce aux traces d’éligibilité ;
* une pondération contrôlée par λ, permettant de donner plus ou moins de poids à l’historique récent.

---

### 2.2 Pourquoi les autres méthodes sont moins adaptées

#### a) TD(0)

TD(0) mettrait à jour les estimations à partir de la transition immédiate seulement, par exemple en fonction de la demande de la journée actuelle.

Cela pose deux problèmes :

1. Il est trop sensible au bruit : une journée exceptionnelle (canicule, événement local) pourrait perturber fortement les estimations sans être suffisamment contextualisée.
2. Il exploite peu l’information de tendance : il ne capture pas naturellement l’idée qu’une augmentation régulière sur plusieurs jours signale un changement durable dans les préférences des clients.

TD(0) est donc trop myope pour un problème de tendance de consommation.

#### b) Monte Carlo

Monte Carlo met à jour les estimations à la fin d’un épisode complet, par exemple à la fin d’une saison, d’un mois, ou d’une campagne promotionnelle.

Cela implique :

* une mise à jour tardive ;
* une incapacité à corriger la politique en cours de saison ;
* une faible réactivité face aux évolutions rapides (par exemple, un produit qui devient viral en quelques jours).

Monte Carlo peut être utile en analyse a posteriori (évaluation des politiques passées), mais pas comme mécanisme principal d’adaptation en temps réel.

#### c) Q-Learning

Q-Learning cherche une politique optimale, généralement dans un environnement que l’on suppose relativement stable.

Dans ce contexte :

* la demande est influencée par des facteurs externes changeants (météo, tendances sociales, promotions concurrentes) ;
* l’environnement réel n’est pas fixe, la “politique optimale” change au fil du temps.

Q-Learning risque donc de s’ajuster à une politique qui n’est optimale que pour une période donnée, puis de devenir rapidement sous-optimale quand les habitudes évoluent. Par ailleurs, le problème de stock se prête davantage à une estimation de valeurs (prévision de demande, estimation de coût) qu’à de l’optimisation agressive de politique.

#### d) SARSA

SARSA est une méthode on-policy, adaptée aux environnements où la prudence ou la sécurité est un enjeu central (par exemple robotique, conduite autonome, cybersécurité).

Dans le cas du supermarché :

* l’enjeu n’est pas la sécurité, mais l’adaptation aux tendances ;
* le comportement souhaité est moins une “prudence en ligne” qu’une bonne exploitation des tendances de consommation.

SARSA pourrait être utilisé si l’on modélise la stratégie de commande comme une politique d’action explicite, mais, à lui seul, il ne répond pas aussi naturellement au besoin de capturer les dépendances temporelles longues. TD(λ) est plus directement adapté à la dimension “tendance”.

---

## 3. Avantages spécifiques de TD(λ) pour les tendances de consommation

La deuxième question porte spécifiquement sur l’intérêt de TD(λ) dans ce contexte.

### 3.1 Mises à jour continues et graduelles

TD(λ) met à jour les estimations de valeur de manière incrémentale, à chaque nouvelle observation (par exemple chaque jour de vente). Cela permet :

* de corriger en permanence les estimations de demande,
* d’éviter les ajustements brutaux fondés uniquement sur des épisodes complets (comme avec Monte Carlo).

Ainsi, si les ventes d’un produit augmentent régulièrement sur plusieurs jours, TD(λ) intègre progressivement cette information dans la politique de commande.

### 3.2 Pondération des observations passées par λ

Le paramètre λ contrôle l’importance de l’historique :

* si λ est proche de 1, les séquences longues (plusieurs jours ou semaines) influencent fortement les mises à jour ;
* si λ est plus faible, le système devient plus sensible aux changements récents.

Dans le contexte du supermarché :

* on peut choisir λ pour refléter le compromis désiré entre stabilité et réactivité ;
* par exemple, un λ élevé pour les produits à tendance saisonnière stable, et un λ plus faible pour des produits très sensibles aux effets de mode.

TD(λ) offre donc un réglage fin de la “mémoire” du système par produit ou par catégorie.

### 3.3 Sensibilité aux tendances et non aux seuls points isolés

L’un des points clés est que TD(λ) ne réagit pas uniquement à une journée particulière, mais à l’ensemble de la trajectoire récente des ventes. Cela permet de :

* distinguer une fluctuation ponctuelle (un seul jour anormal) d’un changement réel de tendance (hausse ou baisse sur plusieurs jours) ;
* mieux aligner les commandes sur les comportements réels des clients.

Par exemple, si un produit voit sa demande augmenter pendant dix jours consécutifs, la trace d’éligibilité associée à cet état (ou à cette configuration de demande) accumule de l’importance, et les mises à jour de valeur associées deviennent plus significatives.

### 3.4 Adaptation à un environnement non stationnaire

Les habitudes de consommation sont influencées par :

* les saisons ;
* la météo ;
* le contexte économique ;
* les promotions internes et externes ;
* les effets de mode, réseaux sociaux, etc.

Ces éléments rendent l’environnement non stationnaire.
TD(λ) permet de s’y adapter en permanence, sans nécessiter de réentraîner entièrement le modèle ou d’attendre la fin de cycles longs.

---

## 4. Conclusion de l’Étude de Cas 3

Dans le contexte de l’anticipation des demandes dans un supermarché, TD(λ) est la méthode la plus appropriée parmi Monte Carlo, TD(0), TD(λ), Q-Learning et SARSA, car elle :

* permet des mises à jour continues, en ligne, au fil des observations ;
* intègre la notion de tendance et de dépendance temporelle grâce à la pondération par λ ;
* offre un compromis contrôlable entre réactivité aux changements récents et stabilité vis-à-vis de l’historique ;
* évite les limitations de Monte Carlo (mise à jour seulement à la fin des épisodes) ;
* est mieux adaptée que Q-Learning et SARSA à un environnement non stationnaire où l’objectif principal est l’ajustement progressif aux habitudes des consommateurs plutôt que la recherche d’une politique unique optimale ou prudente.

