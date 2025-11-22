
# Étude de Cas 4 : Apprentissage d’un Jeu Vidéo de Combat

### Analyse détaillée et justification de la méthode la plus adaptée

## 1. Contexte opérationnel du jeu

L’agent IA doit évoluer dans un jeu de combat où chaque action (attaque, garde, esquive, contre, déplacement) produit un effet dont la probabilité de succès dépend :

* des actions précédentes de l’IA,
* des actions précédentes de l’adversaire,
* de l’état courant du jeu (positions, points de vie, distance),
* de la stratégie adoptée par l’adversaire, qui peut être stable ou changeante.

Le jeu comporte donc :

1. une dynamique **hautement séquentielle**,
2. une interaction **adversariale**,
3. des probabilités de transition **conditionnées par l’historique**.

Le problème est un cas typique de décision séquentielle dans un environnement potentiellement non stationnaire, surtout si l’adversaire change de stratégie ou s’adapte lui-même.

---

# 2. Méthode recommandée : Q-Learning (si adversaire stable) ou SARSA (si adversaire non déterministe)

La réponse dépend du type d’adversaire.
Pour un adversaire stable, la méthode la plus appropriée est **Q-Learning**.
Pour un adversaire imprévisible, probabiliste ou adaptatif, la méthode la mieux adaptée est **SARSA**.

---

## 2.1 Pourquoi Q-Learning est recommandé dans un environnement avec adversaire stable

Q-Learning est une méthode **off-policy**, ce qui signifie que :

* elle apprend la politique optimale théorique,
* indépendamment de la politique d’exploration employée par l’agent.

Pour un adversaire qui suit une stratégie constante, répétitive ou prévisible, Q-Learning permet à l’agent IA :

* d’extraire la politique optimale contre cet adversaire,
* d’exploiter les faiblesses de l’adversaire,
* d’apprendre des actions agressives qui maximisent la récompense à long terme.

### Avantages de Q-Learning dans ce cas :

1. **Optimisation du comportement offensif ou stratégique**
   Le but est de trouver la meilleure action indépendamment de l’action réellement exécutée pendant l’apprentissage.

2. **Convergence vers une politique optimale lorsque l’environnement est stationnaire**
   Si l’adversaire joue toujours de la même manière, la dynamique devient relativement stable.

3. **Exploration agressive utile pour l’exploitation d’un adversaire fixe**
   Q-Learning n'est pas limité par la prudence et peut découvrir des coups ou enchaînements risqués mais très efficaces.

---

## 2.2 Pourquoi SARSA devient supérieur si l’adversaire est non déterministe

SARSA, à l’inverse, est **on-policy**. Il met à jour les valeurs selon :

* l’état réellement observé,
* l’action réellement choisie,
* l’action réelle suivante.

Cela implique que SARSA apprend une politique cohérente avec ce que l’agent fait réellement, ce qui est crucial quand l’environnement est :

* imprévisible,
* changeant,
* soumis à des comportements adversariaux stochastiques.

### Avantages de SARSA dans un environnement non déterministe :

1. **Politique plus prudente**
   SARSA prend en compte le risque réel associé aux actions exécutées.
   Dans un jeu, certaines actions qui semblent optimales selon Q-Learning peuvent être trop dangereuses si l’adversaire varie de manière imprévisible.

2. **Adaptation stable face à un adversaire changeant**
   Si l’adversaire modifie parfois son comportement :

   * agressif à un moment,
   * défensif à un autre,
   * aléatoire par intermittence,
     alors une politique prudente est préférable.

SARSA évite des stratégies risquées qui dépendent trop de la stabilité de l’adversaire.

3. **Résilience face aux transitions stochastiques**
   Dans les jeux de combat, les probabilités de réussite peuvent changer selon le timing, la distance ou la stratégie adverse.
   SARSA s’adapte mieux à ce type de variance.

4. **Prévention des comportements sur-optimistes**
   Q-Learning peut pousser l’agent à sélectionner des actions dangereuses parce qu’elles offrent un gain élevé dans des situations idéales, même si ces situations n’arrivent presque jamais lorsque l’adversaire joue de manière imprévisible.

SARSA corrige cet excès d’optimisme.

---

## 3. Pourquoi TD(0) et Monte Carlo ne sont pas adaptés

### a) TD(0)

TD(0) met à jour les valeurs à partir d’un horizon d’un seul pas.
Cela pose deux limites majeures :

* il ne capture pas correctement les longues séquences d’actions courtes qui composent un combat ;
* il ignore la dépendance temporelle, pourtant essentielle pour comprendre les enchaînements adverses.

TD(0) est trop court terme pour un jeu de combat.

### b) Monte Carlo

Monte Carlo nécessite d’attendre la fin d’un épisode (le combat complet).
Ce procédé pose plusieurs problèmes :

* les combats sont parfois longs, ce qui rend les mises à jour tardives ;
* la variance est très élevée dans les jeux adversariaux ;
* un seul épisode peut être fortement influencé par des événements ponctuels non représentatifs.

Monte Carlo est utile pour analyser des stratégies globales, mais trop inefficace pour un apprentissage en ligne réactif.

---

# 4. Conclusion de l’Étude de Cas 4

### Synthèse :

* Si l’adversaire est **stable, prévisible ou stationnaire**, la meilleure méthode est **Q-Learning**, car elle maximise l’optimisation à long terme et peut exploiter des patterns figés.
* Si l’adversaire est **non déterministe, imprévisible ou adaptatif**, la meilleure méthode est **SARSA**, parce qu’elle produit une politique prudente et stable, cohérente avec les actions réellement exécutées par l’agent.

### Réponse directe aux questions :

1. La méthode recommandée dépend du comportement de l’adversaire.

   * Adversaire stable → Q-Learning.
   * Adversaire non déterministe → SARSA.

2. SARSA peut être plus efficace que Q-Learning lorsque l’adversaire a un comportement non déterministe, car SARSA apprend une politique alignée sur les actions réellement effectuées. Cette approche tient compte du risque réel associé aux mouvements exécutés face à un adversaire irrégulier, ce qui évite d’adopter des stratégies optimistes mais dangereuses, souvent induites par les maximisations de Q-Learning dans les environnements adversariaux instables.
