
# Examen : Concepts en Apprentissage par Renforcement



###  **Instructions générales :**

* Cet examen comporte **25 questions** réparties entre **questions à choix multiples, questions ouvertes et questions d’analyse de code**.
* Chaque question vaut **4 points**.
* Le total de l’examen est de **100 points**.
* Justifiez vos réponses lorsque cela est demandé.
* Toute réponse non motivée dans les questions ouvertes ou d’analyse de code peut entraîner une perte partielle ou totale des points attribués.





# **Question 1.** 

- En apprentissage par renforcement, la **fonction de récompense** :

* a) indique la probabilité d’aller d’un état à un autre.
* b) définit immédiatement les récompenses après avoir exécuté une action dans un état donné.
* c) détermine les actions à choisir selon l'état.
* d) est utilisée uniquement pour l’exploration.

# **Question 2.** 

- La notion d’état de Markov implique :

* a) une dépendance explicite au futur.
* b) que l'état actuel contient toute l'information pertinente nécessaire pour prédire l'avenir.
* c) qu'il faut nécessairement mémoriser tous les états passés.
* d) une absence totale de récompenses immédiates.

# **Question 3.** 

- Un algorithme basé sur la méthode de Monte-Carlo :

* a) apprend toujours par épisodes complets.
* b) apprend uniquement avec une transition à la fois.
* c) utilise toujours une politique déterministe.
* d) ne permet pas d'actualiser progressivement les valeurs estimées.

# **Question 4.** 

- La différence principale entre Monte-Carlo et Temporal Difference (TD) est :

* a) Monte-Carlo apprend après chaque transition, TD uniquement à la fin d’un épisode.
* b) Monte-Carlo nécessite des épisodes complets, TD peut apprendre à chaque transition.
* c) Monte-Carlo utilise toujours une politique stochastique, TD toujours une politique déterministe.
* d) TD ne nécessite pas de politique initiale, contrairement à Monte-Carlo.

# **Question 5.** 

- Le paramètre d’actualisation (discount factor) $\gamma$, lorsqu'il est proche de 0 :

* a) encourage la planification à long terme.
* b) favorise les récompenses immédiates.
* c) n'a aucun impact sur l'apprentissage.
* d) augmente systématiquement les récompenses futures.

# **Question 6.** 

- Le problème de l’exploration-exploitation concerne :

* a) comment maximiser immédiatement les récompenses sans explorer.
* b) comment équilibrer la sélection d'actions connues et la découverte de nouvelles actions potentiellement meilleures.
* c) uniquement l'exploration d'états jamais visités.
* d) uniquement l’exploitation des meilleures actions déjà connues.

# **Question 7.** 

- Une politique stochastique est une politique :

* a) qui associe plusieurs états à une seule action.
* b) qui associe chaque état à une distribution de probabilités sur les actions possibles.
* c) qui donne toujours une unique action optimale.
* d) qui ignore totalement les récompenses futures.

# **Question 8.** 

- L'équation de Bellman décrit :

* a) comment les récompenses immédiates sont calculées.
* b) comment la fonction de valeur d'un état dépend récursivement de la valeur des états suivants.
* c) comment sélectionner des états au hasard.
* d) uniquement la fonction de récompense immédiate.


# **Question 9.** 

- Le phénomène connu sous le nom de « malédiction de la dimensionnalité » signifie :

* a) que les récompenses deviennent trop grandes.
* b) que l’espace d’états devient exponentiellement complexe à gérer.
* c) qu’il n’y a plus de récompense immédiate.
* d) que l'apprentissage est uniquement possible sur de petits espaces d’états.


# **Question 10.** 

- Expliquez la différence entre une politique déterministe et une politique stochastique.

# **Question 11.** 

- Quel est le rôle du paramètre d’apprentissage (learning rate) $\alpha$ dans les méthodes TD ?

# **Question 12.** 

- Définissez précisément l’équilibre exploration-exploitation et expliquez une méthode pratique pour gérer ce compromis.

# **Question 13.** 

- Expliquez en détail la méthode de Monte-Carlo pour l’évaluation de politique. Présentez ses avantages et limites majeures comparativement aux méthodes par différence temporelle (TD).

# **Question 14.** 

- Présentez l’équation de Bellman pour la fonction de valeur d’état $V(s)$. Expliquez chaque terme de cette équation, et montrez clairement son utilité dans l’apprentissage par renforcement.



<br/>




## **Question 15**

- Maison intelligente et stratégie énergétique

> **Contexte :** Un agent intelligent doit décider, heure par heure, s’il est préférable d’utiliser de l’énergie provenant de sources renouvelables, du réseau principal ou de batteries domestiques. Ces décisions doivent tenir compte des coûts variables de l’électricité, des prévisions météorologiques et des besoins en consommation.

**Question :**

Pensez-vous que des méthodes d’apprentissage par renforcement comme **TD(0)**, **TD(λ)**, **SARSA**, **Q-Learning** ou **Monte Carlo** pourraient être adaptées pour optimiser ce système en temps réel ? Ou, au contraire, estimez-vous que aucune de ces approches ne sont pas pertinentes dans un tel contexte ?

Pensez-vous que la pertinence de ces méthodes peut varier selon d'autres caractéristiques spécifiques de l’environnement? Dans ce cas, donnez un exemple illustratif incluant les contraintes à prendre en compte. Justifiez votre réponse en vous appuyant sur les caractéristiques de l’environnement, les objectifs d’apprentissage, la disponibilité des données et la capacité d’adaptation aux changements imprévus.



<br/>

## **Question 16** 

- Drone en environnement dynamique

> **Contexte :** Un drone autonome évolue dans un environnement partiellement imprévisible, comprenant des vents changeants, des obstacles mobiles (comme des oiseaux ou d'autres drones) et des conditions météo variables.

**Question :**
Pensez-vous que des approches comme **SARSA**, **Q-Learning**, ou d'autres variantes de l’apprentissage par renforcement sont adaptées à ce type d’environnement dynamique ?
Selon vous, en quoi le caractère **on-policy** ou **off-policy** de l’algorithme peut-il influencer sa stabilité ou sa capacité d’adaptation dans un environnement instable ?
Donnez un exemple ou une situation illustrant comment certaines méthodes pourraient mieux réagir que d'autres aux incertitudes et aux changements fréquents.
Justifiez votre analyse à partir des caractéristiques du problème, de la nature des récompenses, et de la fréquence des mises à jour nécessaires.

<br/>

## **Question 17**

- Anticipation des demandes en supermarché

> **Contexte :** Un supermarché souhaite ajuster dynamiquement ses commandes de stocks en fonction de la demande des clients, influencée par des tendances saisonnières, des promotions, ou des événements externes.

**Question :**
Est-ce que des méthodes comme **TD(0)**, **TD(λ)**, **Monte Carlo**, ou toute autre approche de renforcement vous paraissent pertinentes pour ce problème d’anticipation et d’adaptation aux tendances ?
En quoi la capacité d’une méthode à **intégrer l’influence du passé avec un certain recul temporel** (comme le permet TD(λ)) pourrait-elle représenter un avantage ici ?
Proposez un exemple d’utilisation dans un cas concret (ex. : pic de demande pour des glaces en été) et justifiez votre réponse selon la disponibilité des données, la fréquence d’apprentissage et la stabilité de l’environnement.

<br/>

## **Question 18 – IA pour jeu vidéo de combat**

> **Contexte :** Un agent IA est entraîné pour affronter un adversaire virtuel dans un jeu de combat. Les stratégies de l’adversaire évoluent au cours du temps de façon partiellement prévisible.

**Question :**
Pensez-vous qu’un agent basé sur **SARSA**, **Q-Learning**, ou un autre algorithme de renforcement pourrait apprendre à s’adapter efficacement dans ce contexte ?
Dans quelle mesure le caractère **stochastique** ou **adversarial** du comportement de l’ennemi peut-il influencer la pertinence d’une méthode ?
Donnez un exemple de situation où une méthode serait préférable à une autre, et justifiez votre analyse en lien avec la prise de décision, la sensibilité au risque, et l’apprentissage à long terme.

<br/>

## **Question 19 - Répartition de charge dans un réseau de serveurs**

> **Contexte :** Un système distribué doit répartir la charge de travail entre différents serveurs, en tenant compte de leur disponibilité, de la consommation énergétique, et du trafic réseau, qui varient dans le temps.

**Question :**
Pensez-vous qu’un algorithme comme **TD(λ)**, **Q-Learning**, ou une autre approche par renforcement pourrait être utilisé efficacement dans ce type de système ?
Selon vous, quels seraient les avantages ou inconvénients d’utiliser une méthode capable de **réagir rapidement tout en conservant une mémoire partielle du passé** ?
Proposez un exemple illustrant un scénario réaliste (ex. : surcharge le matin, faible charge la nuit) et justifiez votre raisonnement en fonction des contraintes de réactivité, de mémoire et d’optimisation énergétique.

<br/>

## **Question 20 – Prédiction des tendances boursières**

> **Contexte :** Un algorithme de trading en ligne doit s’ajuster aux variations rapides des marchés boursiers en se basant sur des données historiques bruitées et parfois contradictoires.

**Question :**
Pensez-vous qu’un algorithme basé sur **TD(λ)**, **Monte Carlo**, **Q-Learning**, ou un autre paradigme d’apprentissage par renforcement serait pertinent dans ce type de contexte volatil ?
Quel rôle des mécanismes comme les **traces d’éligibilité** (dans TD(λ)) pourraient jouer dans la réactivité de l’agent face aux retournements rapides ?
Donnez un exemple d’une situation de marché où la mémoire pondérée du passé améliorerait (ou non) les décisions de l’algorithme. Justifiez votre réponse en prenant en compte le bruit, la fréquence des observations, et le délai entre action et résultat.

<br/>

## **Question 21 – Comparaison globale des méthodes**

> **Contexte :** Vous êtes consultant en IA et devez recommander une méthode d’apprentissage par renforcement à une entreprise évoluant dans un environnement partiellement observable et sujet à des changements fréquents.

**Question :**
Rédigez une **analyse comparative argumentée** des approches suivantes : **TD(0)**, **TD(λ)**, **SARSA**, **Q-Learning**, et **Monte Carlo**.
Selon vous, quels sont les points forts et limites de chaque méthode dans un environnement :

* non stationnaire,
* à données partielles ou bruitées,
* avec interactions continues (temps réel) ou structurées par épisodes (jeux, simulations) ?

Vous pouvez proposer des cas d’usage concrets pour chaque méthode, en expliquant leur pertinence ou leur inadaptation. Structurez votre réponse de façon claire en distinguant les critères de : stabilité, rapidité, exploration, adaptation, mémoire et complexité computationnelle.









<br/>

## <h1 id="q-22"> Question 22 

Identifier le type d’algorithme utilisé à partir de son code, et expliquer les caractéristiques clés qui permettent cette identification en répondant aux questions.


### <h2 id="ex1"> Extrait #1</h2>

```python
Q[s, a] = Q[s, a] + alpha * (r + gamma * np.max(Q[s_next]) - Q[s, a])
```

**Questions :**

1. Quel est le nom de cet algorithme ?
2. Est-ce un algorithme :

   * par différence temporelle ?
   * on-policy ou off-policy ?
3. Pourquoi utilise-t-on `np.max(Q[s_next])` ici ?
4. Est-ce que cet algorithme s'intitule SARSA ? Sinon expliquez brièvement la différence avec SARSA.




<br/>

## <h1 id="q-23"> Question 23


Identifier le type d’algorithme utilisé à partir de son code, et expliquer les caractéristiques clés qui permettent cette identification en répondant aux questions.


### <h2 id="ex2"> Extrait #2</h2>

```python
Q[s, a] = Q[s, a] + alpha * (r + gamma * Q[s_next, a_next] - Q[s, a])
```

**Questions :**

1. Quel est le nom de cet algorithme ?
2. Quelle est la différence entre `a` et `a_next` ?
3. Est-ce un algorithme **on-policy** ou **off-policy** ? Pourquoi ?
4. À quel moment `a_next` est-il sélectionné ?
5. Quel lien avec la méthode de Bellman ?


<br/>

## <h1 id="q-24"> Question 24

Identifier le type d’algorithme utilisé à partir de son code, et expliquer les caractéristiques clés qui permettent cette identification en répondant aux questions.


### <h2 id="ex3"> Extrait #3</h2>

```python
for visit in episode:
    if first_visit_to(visit):
        G = compute_return_from(visit)
        Q[s, a] += G
```

**Questions :**

1. De quel algorithme s’agit-il ?
2. Pourquoi le retour (`G`) est-il calculé à partir de l’épisode entier ?
3. Est-ce une méthode **à pas de temps unique** ou **basée sur des épisodes complets** ?
4. Quelle est la différence entre **First-Visit** et **Every-Visit** ?
5. Cette méthode a-t-elle besoin d’un modèle de l’environnement (modèle dynamique de `P(s’|s,a)`) ?







<br/>

## <h1 id="q-25"> Question 25

Identifier le type d’algorithme utilisé à partir de son code, et expliquer les caractéristiques clés qui permettent cette identification en répondant aux questions.


```python
V[s] = sum([P(s, a, s_next) * (R(s, a, s_next) + gamma * V[s_next]) for s_next in S])
```

**Questions :**

1. Cet algorithme est-il une **méthode par valeur** ou par **action-valeur (Q)** ?
2. De quel **type de mise à jour** s'agit-il ? (Bellman ? MC ? TD ?)
3. Est-ce une méthode **modèle-based** ou **modèle-free** ? Justifiez.
4. Dans quel contexte cette méthode est-elle utilisée :

   * **Policy Evaluation**,
   * **Value Iteration** ou
   * **Policy Iteration** ?
5. Est-ce que l'algorithme est intitulé Q-learning. Sinon, quelle est la différence avec Q-learning ?




> **Barème :**
> Chaque question vaut **4 points**. La note finale est calculée sur 100.
> Les réponses justifiées seront valorisées, en particulier pour les questions ouvertes et analytiques.
> Aucune documentation ni calculatrice autorisée.
> **Durée : 4 heures.**
