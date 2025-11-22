# **Tableau Récapitulatif — Choix par Élimination pour les 6 Études de Cas**


| **Étude de Cas**                                  | **Méthodes Éliminées Radicalement (avec justification)**                                                                       | **Méthodes Encore Possibles** | **Méthode Recommandée** | **Justification Finale**                                                                                  |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------- |
| **1. Gestion de l’énergie (maison intelligente)** | Monte Carlo (retard immense), Q-Learning (type contrôle inutile), SARSA (prudence non pertinente)                              | TD(0), TD(λ)                  | **TD(λ)**               | Capture les tendances temporelles tout en restant réactif aux variations du coût et de la météo.          |
| **2. Drone en environnement changeant**           | Monte Carlo (mise à jour trop tardive), TD(0) (vision trop courte), Q-Learning (instable en environnement non stationnaire)    | SARSA, TD(λ)                  | **TD(λ)**               | Mise à jour incrémentale adaptée aux conditions dynamiques et obstacles mouvants.                         |
| **3. Prévision de demande en supermarché**        | TD(0) (trop court terme), Monte Carlo (épisodes trop longs), SARSA (non pertinent), Q-Learning (problème non décisionnel)      | TD(λ)                         | **TD(λ)**               | Suivi continu des tendances saisonnières avec mémoire pondérée du passé récent.                           |
| **4. Jeu vidéo de combat (agent vs adversaire)**  | Monte Carlo (retard trop long), TD(0) (incapacité à capturer séquences adverses)                                               | Q-Learning, SARSA             | **SARSA**               | S’adapte aux adversaires non déterministes en apprenant une politique alignée avec ses actions réelles.   |
| **5. Répartition de charge (serveurs)**           | Monte Carlo (trop lent), Q-Learning (risque agressif), SARSA (prudence mais pas optimal), TD(0) (trop limité)                  | TD(λ)                         | **TD(λ)**               | Combine réactivité en temps réel et prise en compte des variations structurelles de la charge.            |
| **6. Marchés financiers (prédiction)**            | Monte Carlo (retard immense), SARSA (non pertinent), Q-Learning (pas un problème d’actions optimales), TD(0) (pas assez riche) | TD(λ)                         | **TD(λ)**               | Gère mieux la volatilité grâce à une trace d'historique pondérée, essentielle dans les marchés instables. |

---

# **Résumé global en une phrase**

Dans les six cas industriels proposés, **TD(λ)** domine la majorité des scénarios grâce à sa capacité d’intégrer simultanément la réactivité de TD(0) et la mémoire des tendances récentes, tandis que Monte Carlo, Q-Learning et SARSA ne répondent pas aux contraintes temporelles ou structurelles des systèmes réels sauf dans le cas du jeu vidéo où SARSA est préféré.


