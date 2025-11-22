
# Étude de Cas 2 : Navigation d’un Drone en Environnement Changeant

### Analyse détaillée et justification de la méthode optimale

## 1. Contexte opérationnel du drone

Le drone doit naviguer dans un environnement dynamique comportant :

* des obstacles statiques (bâtiments, arbres),
* des obstacles mobiles (oiseaux, autres drones),
* des rafales de vent changeant en intensité et en direction,
* un espace semi-structuré (zones prédéfinies et zones ouvertes),
* des contraintes de sécurité (éviter collisions),
* des objectifs de performance (livrer un colis rapidement).

Le drone reçoit :

* une récompense positive lorsqu’il réussit une livraison,
* une pénalité en cas de collision ou de déviation excessive,
* potentiellement des petites récompenses intermédiaires pour progression correcte.

L’environnement n’est **pas stationnaire** : les conditions changent continuellement et ne suivent pas une règle stable ou prédictible.

---

## 2. Méthode recommandée : SARSA combiné avec TD(λ)

Pour ce type d’environnement, la combinaison **SARSA + TD(λ)** est la plus adaptée.

### Justification générale

1. **Le comportement de l’environnement est stochastique**
   Les obstacles en mouvement et les conditions de vent ne suivent pas une dynamique fixe.
   Q-Learning, qui cherche une politique optimale indépendante de la politique d’exploration, peut apprendre une stratégie trop agressive ou irréaliste dans un environnement imprévisible.

2. **La prudence et la sécurité du drone sont essentielles**
   SARSA, en tant que méthode on-policy, apprend la valeur des états selon les actions réellement prises, et non selon l’action optimale théorique.
   Cela conduit à une politique plus prudente, plus stable, et mieux adaptée aux environnements incertains.

3. **L’agent doit adapter sa politique en continu**
   TD(λ) permet des mises à jour incrémentales durant chaque vol. L’apprentissage ne dépend pas de la fin d’un épisode complet, ce qui est indispensable pour des trajets potentiellement longs ou continuellement réévalués.

En résumé :
La combinaison SARSA + TD(λ) fournit à la fois **la prudence**, **la réactivité**, **la prise en compte d’horizons multiples** et **l’adaptabilité aux environnements non stationnaires**.

---

## 3. Pourquoi les autres méthodes sont moins adaptées

### a. TD(0)

TD(0) exploite uniquement la transition immédiate.
Dans un environnement de navigation où l’état futur dépend de multiples facteurs (rafales de vent, trajectoires adverses, mouvement du drone), TD(0) est trop local pour capturer les dépendances temporelles pertinentes.

Par exemple, une rafale de vent peut entraîner une déviation progressive sur plusieurs secondes. TD(0) verrait uniquement l’effet immédiat, ce qui mène à une mauvaise anticipation.

### b. Q-Learning

Q-Learning converge vers une politique optimale théorique, ce qui est inadapté dans des environnements hautement incertains. L’algorithme suppose que l’environnement est suffisamment stable pour apprendre une politique fixe, ce qui n’est pas le cas ici.

De plus, Q-Learning tend à être trop agressif : il favorise l’action au plus grand “max Q” même si cette action est dangereuse dans un environnement imprévisible. Cela peut conduire à des collisions.

### c. Monte Carlo

Monte Carlo nécessite d’attendre la fin de l’épisode pour mettre à jour les valeurs.
Pour un drone, un épisode peut durer plusieurs minutes, voire des dizaines de minutes.
L’environnement pouvant changer radicalement au milieu de la trajectoire, attendre la fin d’un épisode complet rend Monte Carlo inutilisable pour une navigation sécurisée en temps réel.

### d. TD(n)

TD(n) est raisonnable pour un horizon court, mais reste moins flexible que TD(λ) car il impose un nombre fixe d’étapes avant mise à jour. TD(λ) permet de pondérer dynamiquement plusieurs horizons de décision.

---

## 4. Avantages d’une approche incrémentale basée sur TD(λ)

TD(λ) est particulièrement adapté à cet environnement grâce à trois propriétés principales.

### 1. Sensibilité aux dépendances temporelles

TD(λ) permet de prendre en compte plusieurs états passés avec une importance dégressive.
C’est crucial pour un drone, car les états successifs sont fortement corrélés :

* une rafale de vent influence plusieurs instants consécutifs,
* une trajectoire d’obstacle mobile doit être suivie sur plusieurs pas,
* des micro-ajustements doivent être intégrés instantanément.

TD(λ) modélise très précisément ces relations temporelles.

### 2. Mise à jour immédiate et continue

Le drone ne peut pas attendre la fin du vol pour ajuster sa politique.
Il doit modifier son comportement après chaque transition observée.
TD(λ) permet une mise à jour :

* instantanée,
* progressive,
* sensible aux dernières observations.

Cela donne une grande capacité d’adaptation.

### 3. Stabilité dans un environnement non stationnaire

Lorsque :

* un oiseau change de direction,
* une bourrasque apparaît soudainement,
* un autre drone entre dans le champ,
* une zone de turbulence apparaît,

TD(λ) permet d’ajuster la politique immédiatement, tout en conservant une mémoire pondérée des événements précédents.
Cette combinaison assure une adaptation constante sans perdre la cohérence globale de la navigation.

---

## 5. Exemple illustratif d’adaptation

Considérons un scénario concret :

Il est 10 h 02.
Le drone vole en ligne droite vers un point de livraison.
Soudain, une rafale latérale dévie légèrement sa trajectoire, tout en faisant apparaître un groupe d’oiseaux sur la droite.

### Réaction avec TD(0)

* Le drone corrige immédiatement sa trajectoire mais sans tenir compte des effets futurs du vent.
* Il risque d’osciller ou de surcompenser.

### Réaction avec Q-Learning

* Le drone applique la politique optimale précédente, ce qui peut ne pas tenir compte des nouvelles conditions.

### Réaction avec Monte Carlo

* Impossible de réagir avant la fin de l’épisode.

### Réaction avec SARSA + TD(λ)

* SARSA s’appuie sur les actions réellement prises en tenant compte de l’incertitude.
* TD(λ) pondère les effets cumulés de la rafale et de l’arrivée des obstacles.
* La politique s’ajuste immédiatement, en prenant en compte les dernières trajectoires et en anticipant les conséquences futures.

La décision sera plus stable, plus sécurisée et plus réaliste.

---

# Conclusion de l’Étude de Cas 2

L’environnement du drone est caractérisé par une forte incertitude, une variabilité rapide et un besoin essentiel de sécurité.
La combinaison **SARSA + TD(λ)** est la plus adaptée, car elle permet :

* une adaptation continue et incrémentale,
* une prise en compte des tendances temporelles sur plusieurs pas,
* une politique prudente dans un environnement dangereux,
* une mise à jour en temps réel.

TD(λ) apporte la capacité de modéliser des dépendances temporelles complexes et de réagir instantanément à des changements imprévisibles, ce qui est indispensable pour une navigation autonome fiable.



