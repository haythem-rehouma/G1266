
# Étude de Cas 1 : Gestion de l’Énergie dans une Maison Intelligente

### Explication détaillée et justification de la méthode recommandée

## 1. Contexte opérationnel du système

Une maison intelligente doit, chaque heure, choisir parmi trois sources d’énergie :

1. l’énergie renouvelable disponible (solaire, éolien),
2. l’énergie provenant du réseau principal, dont le prix varie au cours de la journée,
3. les batteries domestiques, dont la capacité et la vitesse de chargement sont limitées.

Le prix de l’électricité dépend de facteurs externes comme :

* la période de la journée (heures pleines, heures creuses),
* la demande locale ou régionale,
* les prévisions météorologiques influençant la production renouvelable,
* les variations imprévisibles du marché de l’énergie.

Le problème est dynamique, non stationnaire, et dépend fortement d’un horizon temporel glissant (tendance du prix, état des batteries, prévisions de soleil).

---

## 2. Choix de la méthode : TD(λ)

La méthode la mieux adaptée pour ce scénario est **TD(λ)**.
Cette approche fournit le meilleur compromis entre réactivité immédiate, stabilité temporelle, adaptation progressive, et exploitation d’un horizon d’apprentissage plus long que TD(0), sans les contraintes lourdes de Monte Carlo.

### Pourquoi TD(λ) est la méthode la plus appropriée

TD(λ) permet de combiner plusieurs niveaux d’information temporelle :

* le présent immédiat (comme TD(0)),
* les signaux des heures précédentes (comme TD(1), TD(2), etc.),
* un horizon complet pondéré par le paramètre λ.

Cela offre un comportement très performant dans des environnements où :

1. les conditions changent continuellement,
2. les décisions doivent être prises en ligne, sans attendre la fin d’un épisode (ici, une journée entière),
3. les séquences d’états contiennent des dépendances temporelles significatives (niveau de batterie, production solaire, tendances du prix).

---

## 3. Pourquoi les autres méthodes sont moins adaptées

### a. TD(0)

TD(0) réagit uniquement à la transition actuelle.
Il est trop court terme pour ce problème car il ignore l’évolution progressive des conditions.

Exemple :
Une baisse temporaire du soleil pourrait conduire TD(0) à vider la batterie immédiatement, alors qu’une amélioration est attendue une heure plus tard. Cela produit une politique instable.

### b. Monte Carlo

Monte Carlo exige l’observation de l’épisode complet avant de mettre à jour la valeur.
Dans ce contexte, un épisode représenterait une journée entière ou une semaine. Cela rend la méthode inutilisable pour des décisions à l’heure où les conditions changent constamment.

### c. Q-Learning

Q-Learning cherche une politique optimale théorique.
Dans un environnement non stationnaire, cette politique n’existe pas de manière stable. Le système risquerait d’apprendre un comportement optimal pour une configuration ancienne qui ne correspond plus aux conditions actuelles.

### d. SARSA

SARSA est plus prudent que Q-Learning puisque les mises à jour dépendent des actions réellement choisies.
Cependant, la prudence n’est pas le principal objectif ici. L’objectif est de maximiser l’efficacité énergétique, pas de réduire les risques. SARSA aurait tendance à produire des décisions trop conservatrices et moins efficaces que TD(λ).

---

## 4. Capacité d’adaptation de TD(λ) aux changements imprévus

TD(λ) réagit efficacement aux variations soudaines parce qu’il prend en compte :

### 1. Une pondération décroissante des événements passés

Le paramètre λ permet de donner plus d’importance aux observations récentes, tout en conservant une mémoire des tendances qui se sont développées sur plusieurs heures.

Si une hausse de prix apparaît soudainement, les transitions récentes auront un poids plus important dans la mise à jour, ce qui accélère l’ajustement de la politique.

### 2. Une mise à jour incrémentale après chaque heure

La mise à jour de la valeur est réalisée immédiatement après chaque observation, selon :

[
V_{\text{nouveau}} = V_{\text{ancien}} + \alpha , \delta_t , e_t
]

où :

* (\delta_t) est l’erreur de prédiction (TD error),
* (e_t) est la trace d’éligibilité, qui représente la mémoire pondérée des états passés.

Ainsi, le système peut réagir en temps réel à des changements inattendus.

### 3. Une analyse multi-horizon

La gestion de l’énergie dépend à la fois :

* des conditions observées maintenant,
* mais aussi de la tendance observée durant les heures précédentes,
* et enfin du comportement anticipé dans les heures suivantes.

TD(λ) est capable de capturer cette relation temporelle complexe.

---

## 5. Exemple illustratif de réaction à un événement imprévu

Situation :
Il est 15 h.
Le soleil disparaît subitement en raison d’un nuage dense, le prix du réseau augmente brusquement, et une consommation élevée commence à 16 h (chauffage, électroménagers).

### Réaction avec TD(λ)

* L’information récente (baisse du solaire + hausse du prix) influence fortement la mise à jour.
* Le système anticipe les conséquences sur les heures suivantes grâce à la mémoire pondérée des états récents.
* La politique s’ajuste immédiatement pour privilégier la batterie sans la vider brusquement, car TD(λ) prend en compte la tendance future.

La décision devient plus rationnelle :

* utiliser la batterie maintenant,
* tout en conservant une réserve suffisante pour les heures suivantes,
* et en évitant d’acheter de l’électricité à prix élevé.

---

# Conclusion

TD(λ) est la méthode la plus efficace pour la gestion énergétique dans une maison intelligente, car elle concilie :

* réactivité,
* continuité,
* stabilité,
* adaptation à des environnements non stationnaires,
* exploitation d’un horizon temporel étendu sans attendre la fin d’un épisode.

Elle permet d’ajuster en temps réel les stratégies énergétiques en fonction des variations de prix, des changements météorologiques, et des besoins de consommation, tout en conservant une vision globale de l’évolution du système.


