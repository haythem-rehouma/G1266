
## **Leçon 3 – Créer un environnement**



### Pourquoi un environnement est-il nécessaire ?

L’agent **n’apprend pas tout seul dans le vide**.
Il a besoin d’un **monde autour de lui** pour :

* voir ce qu’il se passe,
* faire des actions,
* recevoir des résultats.

> Ce monde, on l’appelle **l’environnement**.



### 1. Qu’est-ce que l’environnement dans un projet RL ?

C’est **l’espace dans lequel l’agent agit**. Il contient :

* les règles du jeu,
* les limites (ex. : murs, bords),
* les obstacles (ou pas),
* le **résultat de chaque action**.

**Dans DeepRacer**, l’environnement est :

* une piste virtuelle en 3D,
* avec des virages, des bords, et une ligne centrale,
* dans laquelle une voiture apprend à rouler seule.



### 2. Ce que l’environnement fait exactement

| Ce que l’agent fait | Ce que l’environnement répond |
| ------------------- | ----------------------------- |
| Avance ou tourne    | Change la position de l’agent |
| Sort de la piste    | Signale un échec              |
| Reste bien centré   | Donne une récompense          |


### 3. Virtuel ou réel ?

| Type d’environnement     | Exemple                               | Avantages                                      |
| ------------------------ | ------------------------------------- | ---------------------------------------------- |
| **Virtuel** (simulation) | Une piste DeepRacer dans l'ordi       | Rapide, sans risque, facile à redémarrer       |
| **Réel** (physique)      | Une vraie voiture sur un tracé au sol | Plus proche du monde réel, mais plus compliqué |

> En DeepRacer, **on commence toujours en simulation**, car c’est plus sûr et plus facile à modifier.



### 4. Pourquoi bien définir l’environnement est essentiel

* Si l’environnement est **trop facile**, l’agent n’apprend rien.
* S’il est **trop dur**, il échoue tout le temps.
* Il faut qu’il soit **assez riche pour apprendre**, mais **pas trop compliqué** au début.



### 5. Résumé visuel

```
Environnement = le monde de l’agent

→ Il agit dedans
→ Il reçoit des infos
→ Il reçoit des récompenses
→ Il peut progresser
```

# Annexe 1 - **Complément à la Leçon 3 – Mieux comprendre les environnements en RL**



#### 1. Qu’est-ce qu’un environnement, en détail ?

Un **environnement**, c’est **tout ce qui entoure l’agent** et **réagit à ses actions**.

Il contient :

* Un **état** : ce que voit ou connaît l’agent à un moment donné (image, position, vitesse, etc.)
* Une **dynamique** : comment l’environnement change quand l’agent agit
* Une **récompense** : un score donné après chaque action
* Une **condition de fin** : quand l’épisode s’arrête (par exemple : la voiture sort de la piste)



#### 2. Types d’environnements (avec exemples simples)

| Type d’environnement               | Description                                                   | Exemple en DeepRacer                                                     |
| ---------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Statique**                       | L’environnement **ne change pas** pendant l’épisode           | Toujours la même piste, sans obstacle                                    |
| **Dynamique**                      | Des éléments **bougent** ou **apparaissent** au fil du temps  | D’autres voitures apparaissent (Head-to-Bot)                             |
| **Déterministe**                   | Une même action donne **toujours le même résultat**           | Tourner à droite donne toujours le même virage                           |
| **Stochastique** (ou probabiliste) | Une même action peut donner **plusieurs résultats possibles** | La voiture tourne plus ou moins selon les conditions (bruit, glissement) |



#### 3. DeepRacer : un environnement **stochastique et dynamique**

Même si la piste semble fixe, l’environnement DeepRacer :

* **Ajoute du bruit** dans la vitesse ou la position (stochastique)
* Peut contenir des **éléments mobiles** si on active les bots (dynamique)
* Peut donner des résultats légèrement différents pour **la même action**

> L’agent doit apprendre à **s’adapter** malgré les **petites incertitudes**.



#### 4. Éléments techniques d’un environnement

Voici ce que contient typiquement un environnement :

| Élément               | Description                                     | Exemple                                            |
| --------------------- | ----------------------------------------------- | -------------------------------------------------- |
| **États**             | Ce que perçoit l’agent                          | Image de la caméra, vitesse, position sur la piste |
| **Actions**           | Ce que peut faire l’agent                       | Tourner, accélérer, freiner                        |
| **Transitions**       | Comment l’environnement change après une action | "Si tu tournes, ta position change"                |
| **Récompenses**       | Score donné selon l’action et l’état            | +1 si bien centré, -1 si sorti                     |
| **Conditions de fin** | Quand l’épisode s’arrête                        | Sortie de piste, temps écoulé, fin de tour         |
| **Stochasticité**     | Incertitude dans le résultat d’une action       | Glissement, retard moteur, variation légère        |



#### 5. En résumé

> Un bon environnement doit :

* **fournir les bonnes informations**,
* **réagir logiquement**,
* être **assez stable pour apprendre**,
* mais **pas trop parfait**, sinon l’agent n’apprendra pas à gérer l’imprévu.





