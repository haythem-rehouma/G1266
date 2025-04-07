# Table des Matières


```plaintext
+----+------------------------------+-------------------------------------------------------------+
| No | Fichier                      | Ajout par rapport à la version précédente                   |
+----+------------------------------+-------------------------------------------------------------+
| 0  | Installation.md              | Installation de base de MLflow sur une VM Ubuntu 22.04      |
+----+------------------------------+-------------------------------------------------------------+
| 1  | Config_MLflow_Simple.md      | Configuration de MLflow pour une première expérience simple |
+----+------------------------------+-------------------------------------------------------------+
| 2  | Init_Run_MLflow.md           | Utilisation de `mlflow.start_run()` pour initialiser        |
|    |                              | une exécution MLflow                                        |
+----+------------------------------+-------------------------------------------------------------+
| 3  | Log_Params_Metrics.md        | Ajout de l’enregistrement de paramètres et métriques avec   |
|    |                              | `log_param()` et `log_metric()`                             |
+----+------------------------------+-------------------------------------------------------------+
| 4  | Log_Model.md                 | Ajout de l’enregistrement d’un modèle dans MLflow           |
|    |                              | avec `log_model()`                                          |
+----+------------------------------+-------------------------------------------------------------+
| 5  | Log_Artifact.md              | Enregistrement d’une sortie en tant qu’artefact avec        |
|    |                              | `log_artifact()`                                            |
+----+------------------------------+-------------------------------------------------------------+
| 6  | Manage_Tags.md               | Ajout d’une gestion avancée des tags avec                   |
|    |                              | `mlflow.set_tags()` pour ajouter des métadonnées            |
+----+------------------------------+-------------------------------------------------------------+
| 7  | Multi_Experiments.md         | Exécution de multiples expériences avec différents          |
|    |                              | paramètres dans le même script                              |
+----+------------------------------+-------------------------------------------------------------+
| 8  | Compare_Models.md            | Comparaison de différents modèles de régression en          |
|    |                              | lançant plusieurs expériences                               |
+----+------------------------------+-------------------------------------------------------------+
| 9  | Autologging.md               | Automatisation de l’enregistrement avec `mlflow.autolog()`  |
|    |                              | pour simplifier le suivi                                    |
+----+------------------------------+-------------------------------------------------------------+
| 10 | Access_Last_Run.md           | Accès aux données de la dernière expérience active via      |
|    |                              | `active_run` et `last_active_run`                           |
+----+------------------------------+-------------------------------------------------------------+
| 11 | Log_Multiple_Artifacts.md    | Enregistrement de fichiers associés à une expérience        |
|    |                              | (artefacts) avec `log_artifacts()`                          |
+----+------------------------------+-------------------------------------------------------------+
```


---

## 01. Installation et Configuration de MLflow
- Guide pour installer MLflow sur une VM Ubuntu 22.04
- Configuration initiale de l’environnement pour l’utilisation de MLflow
- Téléchargement et préparation des jeux de données pour les expériences

## 02. Entraînement de Modèle de Base ElasticNet
- Code pour entraîner un modèle de régression ElasticNet simple
- Enregistrement des hyperparamètres et des métriques de performance
- Sauvegarde du modèle dans le système de suivi MLflow

## 03. Suivi des Expériences avec MLflow
- Utilisation de MLflow pour configurer et enregistrer les expériences
- Enregistrement des paramètres et métriques pour évaluer les performances du modèle
- Introduction au suivi d’expériences pour optimiser les itérations

## 04. Configuration de l'URI de Suivi
- Configuration de l'URI de suivi centralisé avec `mlflow.set_tracking_uri`
- Vérification de l’URI de suivi avec `mlflow.get_tracking_uri`
- Importance de l’URI pour la gestion multi-utilisateurs dans MLflow

## 05. Création d'Expériences dans MLflow
- Création de nouvelles expériences avec `mlflow.create_experiment`
- Définition des métadonnées et configuration de l'emplacement des artefacts
- Utilisation des expériences pour organiser différents essais de modèles

## 06. Gestion des Exécutions Actives
- Démarrage et fin d'exécutions avec `mlflow.start_run` et `mlflow.end_run`
- Accès aux informations de la dernière exécution active via `mlflow.last_active_run`
- Structuration des exécutions pour optimiser la traçabilité des essais

## 07. Enregistrement des Artefacts
- Enregistrement des artefacts d’une expérience avec `mlflow.log_artifacts`
- Organisation et sauvegarde des fichiers de sortie et résultats intermédiaires
- Gestion des versions des fichiers de données pour chaque exécution

## 08. Utilisation des Tags pour les Exécutions
- Ajout de tags aux exécutions pour une meilleure organisation avec `mlflow.set_tags`
- Classement des expériences par mots-clés et gestion des métadonnées
- Utilité des tags pour naviguer facilement dans des ensembles d'expériences

## 09. Lancement de Plusieurs Exécutions
- Exécution de tests multiples avec différents paramètres dans un seul script
- Comparaison automatique des performances pour ajuster les hyperparamètres
- Gestion des multiples exécutions pour optimiser le modèle

## 10. Comparaison de Différentes Expériences
- Tests avec divers algorithmes de régression (ElasticNet, Ridge, Lasso)
- Comparaison des performances de chaque modèle sur les mêmes données
- Avantages de comparer les algorithmes dans MLflow pour choisir le meilleur

## 11. Automatisation avec `mlflow.autolog`
- Automatisation de l’enregistrement des paramètres, métriques et modèles via `mlflow.autolog`
- Simplification du suivi des expériences sans code manuel supplémentaire
- Introduction à `autolog` pour rendre le code plus concis et clair
