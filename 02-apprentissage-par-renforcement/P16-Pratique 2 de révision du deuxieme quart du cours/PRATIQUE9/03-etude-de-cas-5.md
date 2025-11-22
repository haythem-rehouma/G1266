

# **Étude de Cas 5 : Répartition de la Charge dans un Réseau de Serveurs**

### Analyse détaillée et réponse aux deux questions

## **1. Contexte technique et opérationnel**

Une entreprise exploite un ensemble de serveurs (ou conteneurs Kubernetes, ou machines virtuelles cloud) pour traiter du trafic :

* les charges fluctuent au fil de la journée ;
* certaines requêtes sont lourdes et d’autres légères ;
* les décisions de réallocation ont un impact immédiat sur la performance ;
* les coûts varient selon l’heure (tarifs cloud, énergie, surcharge) ;
* un mauvais équilibrage entraîne soit des latences, soit une surconsommation énergétique.

L’environnement est donc **hautement dynamique**, **non stationnaire**, et soumis à des signaux continus.

L’objectif est d’apprendre une politique qui répartit intelligemment la charge en temps réel.

---

# **2. Méthode recommandée : TD(λ) ou SARSA selon le degré d’incertitude**

Dans cet environnement, la meilleure approche est soit :

## **→ TD(λ)**

pour capturer les dépendances temporelles à court et moyen terme (ex : évolution de charge sur une fenêtre de quelques minutes).

## **→ SARSA**

si l’on veut une politique conservatrice et stable, qui évite des décisions trop risquées lorsque la charge est imprévisible.

Les deux méthodes sont préférables à TD(0), Monte Carlo et même Q-Learning dans ce type de contexte.

---

# **3. Pourquoi TD(0), Monte Carlo et Q-Learning sont moins adaptés**

## **3.1. TD(0) : horizon trop court**

TD(0) ne met à jour les valeurs qu’à partir du retour d’un seul pas de temps.
Ce modèle réagit trop rapidement aux variations instantanées et :

* risque de provoquer du thrashing (réallocation trop fréquente) ;
* manque la tendance réelle (pics réguliers, creux, charges saisonnières dans la journée) ;
* ne capture pas les corrélations sur plusieurs minutes.

Dans un système de serveurs, l’horizon d’action est rarement instantané, donc TD(0) est insuffisant.

---

## **3.2. Monte Carlo : mise à jour trop tardive**

Monte Carlo attend la fin d’un épisode complet pour mettre à jour les valeurs.
Or, un épisode peut correspondre à :

* une journée entière ;
* une fenêtre de trafic de plusieurs heures.

Cela rend Monte Carlo inutilisable dans un environnement où :

* il faut s’adapter continuellement,
* les décisions doivent être prises en ligne,
* les conditions changent plusieurs fois par minute.

---

## **3.3. Q-Learning : politique trop agressive**

Q-Learning est **off-policy** et apprend la politique optimale théorique, ce qui pose problème lorsque :

* les charges évoluent rapidement ;
* les décisions doivent être prudentes (éviter une surcharge) ;
* l’environnement est stochastique.

Q-Learning peut proposer des actions optimales dans un cas moyen, mais dangereuses en pratique lorsqu’une variation imprévisible survient (ex : un pic soudain venant d’un batch processing).

---

# **4. Pourquoi TD(λ) est particulièrement adapté**

TD(λ) pondère les récompenses futures selon un facteur λ, ce qui permet de :

1. **capturer l’effet de plusieurs décisions consécutives**
   Utile pour comprendre comment une réallocation de charge influence la performance un peu plus tard.

2. **réduire la variance par rapport à Monte Carlo**,
   tout en conservant une dépendance à plusieurs pas temporels.

3. **répondre aux variations lentes ou progressives de charge**
   comme les augmentations avant l’heure du dîner ou les diminutions la nuit.

4. **équilibrer réactivité et stabilité**,
   grâce à un paramètre λ pouvant être ajusté selon la dynamique réelle du trafic.

C’est idéal pour un système cloud où les tendances à court terme comptent autant que les valeurs instantanées.

---

# **5. Pourquoi SARSA apporte une stabilité cruciale**

SARSA est **on-policy**, ce qui signifie qu’il met à jour les valeurs selon la politique réellement suivie, et cela apporte deux avantages majeurs :

1. **Prudence dans l’exploration**
   SARSA n’apprend pas une politique agressive théorique mais celle réellement utilisée.
   Cela limite les fluctuations violentes dans la répartition de charge.

2. **Robustesse face à l’incertitude**
   Quand la charge varie soudainement ou devient imprévisible :

   * Q-Learning risque d’adopter des décisions trop optimistes,
   * SARSA reste cohérent avec les actions réellement effectuées.

3. **Stabilité opérationnelle**
   Dans un réseau de serveurs, il est préférable d’éviter des réaffectations massives et brutales, car cela génère des coûts supplémentaires.
   SARSA prévient ce type de comportement.

---

# **6. Réponses directes aux questions**

## **Question 1 — Quelle approche recommander ?**

Pour optimiser la répartition de charge dans un environnement dynamique :

### **→ TD(λ)**

si l’objectif est une adaptation progressive et stable prenant en compte les dépendances temporelles sur plusieurs pas.

### **→ SARSA**

si l’environnement est particulièrement imprévisible et qu’une politique prudente et stable est nécessaire pour éviter les surcharges ou les réallocations agressives.

TD(0), Monte Carlo et Q-Learning sont moins efficaces pour les raisons détaillées plus haut.

---

## **Question 2 — Comment TD(λ) ou SARSA aident à s’adapter aux changements imprévus ?**

### **a) TD(λ)**

TD(λ) s’adapte en intégrant graduellement les effets des fluctuations de charge sur plusieurs pas temporels :

* lorsque la charge augmente soudainement,
  TD(λ) réagit plus rapidement que Monte Carlo mais reste plus stable que TD(0) ;
* lorsque la charge diminue,
  TD(λ) ajuste la politique sans sur-réagir.

La pondération λ permet d’équilibrer réactivité et mémoire, ce qui est essentiel dans un trafic serveur réel.

---

### **b) SARSA**

SARSA apprend toujours en fonction des actions réellement exécutées, ce qui garantit :

* une politique cohérente avec les risques opérationnels,
* une réduction des comportements agressifs,
* une adaptation plus sûre aux anomalies ou pics soudains,
* une stabilité accrue dans les environnements stochastiques.

Par exemple, si un pic imprévu apparaît, SARSA évite de rediriger massivement la charge vers un serveur unique simplement parce qu’un état isolé semblait optimal.

---

# **Conclusion**

TD(λ) et SARSA sont les deux approches dominantes pour la répartition dynamique de la charge dans un réseau de serveurs.

* **TD(λ)** est préférable lorsque les tendances temporelles doivent être saisies et exploitées.
* **SARSA** est préférable lorsque l’environnement est très incertain et que la prudence opérationnelle est essentielle.


