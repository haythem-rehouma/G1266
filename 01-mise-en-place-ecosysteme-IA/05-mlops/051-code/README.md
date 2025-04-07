
# Étapes
------------------------



# 01 - Code de Base de Machine Learning
- Code de base pour un modèle d'apprentissage machine simple
- Mise en place initiale sans intégration avec MLflow

# 02 - Premier Code Machine Learning avec MLflow
- Entraînement d'un modèle avec MLflow
- Enregistrement de paramètres et de métriques dans MLflow

# 03 - Configuration de l'URI de Suivi MLflow
- Utilisation de `mlflow.set_tracking_uri` pour configurer l'URI de suivi
- Vérification de l'URI de suivi actuel avec `mlflow.get_tracking_uri`

# 04 - Création d'une Expérience MLflow
- Création d'une expérience avec `mlflow.create_experiment`
- Définition des métadonnées et emplacement d'artefact

# 05 - Gestion des Exécutions Actives
- Utilisation de `mlflow.start_run` et `mlflow.end_run` pour démarrer et terminer des exécutions
- Récupération de la dernière exécution active avec `mlflow.last_active_run`

# 06 - Enregistrement des Artefacts
- Enregistrement des artefacts avec `mlflow.log_artifacts`
- Organisation des fichiers de données associés à l'expérience

# 07 - Ajout de Tags aux Exécutions
- Utilisation de `mlflow.set_tags` pour ajouter des tags
- Organisation et gestion des métadonnées supplémentaires

# 08 - Lancement de Plusieurs Exécutions
- Exécution de plusieurs runs dans un même script
- Comparaison des résultats de différents paramètres

# 09 - Lancement de Plusieurs Expériences
- Lancement de diverses expériences (ElasticNet, Ridge, Lasso)
- Comparaison des performances des algorithmes de régression

# 10 - Automatisation avec `mlflow.autolog`
- Utilisation de `mlflow.autolog` pour enregistrer automatiquement les paramètres, métriques et modèles
- Simplification du suivi des expériences de machine learning

# 11 - Commande Serveur MLflow
- Commande pour lancer un serveur MLflow pour centraliser les enregistrements
- Configuration d'un serveur de suivi MLflow

# 12 - Signature de Modèle et Exemples d'Entrée
- Définition de la signature des modèles et des exemples d'entrées
- Documentation complète pour le suivi des modèles

# 13 - Inférence de la Signature de Modèle
- Utilisation de `mlflow.models.infer_signature` pour inférer la signature des modèles
- Simplification de la gestion des inputs

# 14 - Extension de la Signature et Exemples
- Amélioration de la gestion des signatures et des exemples d'entrée
- Adaptation pour des cas d'utilisation avancés

# 15 - Personnalisation de Modèle
- Personnalisation des paramètres d'entraînement pour un modèle spécifique
- Ajustements pour des besoins particuliers

# 16 - Amélioration de la Personnalisation de Modèle
- Options avancées pour la personnalisation des modèles
- Adaptation des modèles pour des configurations uniques

# 17 - Chargement de Modèle Enregistré
- Chargement d'un modèle préalablement enregistré pour évaluation ou prédiction
- Utilisation de `mlflow.pyfunc.load_model`

# 18 - Évaluation de Modèle
- Utilisation de métriques pour évaluer les performances d'un modèle
- Vérification de la précision et autres métriques

# 19 - Métrique Personnalisée et Artefact
- Création de métriques et artefacts personnalisés
- Extension des capacités d'évaluation

# 20 - Définition de Seuil de Validation
- Paramétrage de seuils pour la validation des modèles
- Affinement des résultats selon des critères spécifiques

# 21 - Chargement de Modèle depuis le Registre
- Récupération de modèles depuis le registre MLflow pour utilisation
- Gestion centralisée des modèles disponibles

# 22 - Régression ElasticNet Sans MLflow
- Entraînement d'un modèle ElasticNet pour comparaison
- Test de modèle sans la gestion de suivi de MLflow

# 23 - Enregistrement de Modèle dans le Registre
- Processus pour enregistrer un modèle dans le registre MLflow
- Partage et gestion de modèles enregistrés

# 24 - Enregistrement du Modèle ElasticNet
- Exemple d'enregistrement du modèle ElasticNet dans le registre
- Documentation des étapes d'enregistrement

# 25 - Code Simplifié pour MLflow
- Version simplifiée du code d'entraînement et d'enregistrement
- Facilitation de l'intégration pour des utilisateurs novices

# 26 - Définition de Projet MLflow (MLproject)
- Création d'un fichier MLproject pour organiser les configurations
- Standardisation des configurations de projet avec MLflow

# 27 - Script d'Exécution de Projet
- Script de lancement du projet MLflow pour automatisation des exécutions
- Standardisation des étapes d'exécution de projet

# 28 - Commandes CLI pour MLflow
- Ensemble de commandes CLI pour interagir avec MLflow
- Utilisation avancée de MLflow en ligne de commande

# 29 - Commandes CLI Avancées
- Extension des commandes CLI pour de nouvelles options
- Support de fonctionnalités avancées via la CLI
```



---------------------

```plaintext
| Numéro | Nom du Fichier                 | Objectif                                                                                          |
|--------|---------------------------------|---------------------------------------------------------------------------------------------------|
| 01     | Basic ML Code                   | Code de base pour l'entraînement d'un modèle de régression sans utilisation de MLflow.             |
| 02     | First ML Code with MLflow       | Introduction de MLflow pour enregistrer les expériences de base, incluant les paramètres et métriques. |
| 03     | Set and Get Tracking URI        | Configuration de l'URI de suivi avec MLflow pour centraliser les enregistrements.                  |
| 04     | Create Experiment               | Création d'expériences spécifiques dans MLflow pour structurer les tests.                          |
| 05     | Active and Last Active Run      | Gestion des exécutions actives et récupération de la dernière exécution active.                    |
| 06     | Log Artifacts                   | Enregistrement des artefacts dans MLflow pour conserver les fichiers associés à chaque expérience. |
| 07     | Set Tags                        | Utilisation de tags pour organiser les métadonnées des exécutions.                                 |
| 08     | Launching Multiple Runs         | Exécution de plusieurs configurations dans un même script pour comparaison de résultats.           |
| 09     | Launching Multiple Experiments  | Lancement de différentes expériences pour comparer des modèles (ElasticNet, Ridge, Lasso).         |
| 10     | Autolog                         | Utilisation de `mlflow.autolog` pour simplifier l'enregistrement automatique des paramètres.       |
| 11     | MLflow Server Command           | Commande de lancement d’un serveur MLflow pour centraliser les enregistrements de projets.        |
| 12     | Model Signature and Input Examples | Définition de signatures de modèles et d'exemples d'entrée pour une documentation complète.       |
| 13     | Infer Signature                 | Inférence automatique des signatures de modèles pour une meilleure gestion des inputs.             |
| 14     | Model Signature and Input Examples (1) | Extension des signatures et des exemples pour les cas de modèles avancés.                    |
| 15     | Model Customization             | Personnalisation des modèles pour adapter les paramètres d'entraînement.                          |
| 16     | Model Customization (1)         | Amélioration des options de personnalisation des modèles pour des configurations spécifiques.      |
| 17     | Load Model                      | Chargement des modèles enregistrés pour évaluation ou prédiction.                                 |
| 18     | Evaluate                        | Évaluation des modèles en utilisant les métriques définies pour vérifier les performances.         |
| 19     | Custom Metric and Artifact      | Création de métriques et d'artefacts personnalisés pour des analyses spécifiques.                 |
| 20     | Validation Threshold            | Définition de seuils de validation pour affiner les performances des modèles.                      |
| 21     | Registry - Load Model           | Chargement de modèles depuis le registre pour des réutilisations facilitées.                       |
| 22     | Pure ElasticNet Regression      | Modèle de régression ElasticNet sans MLflow pour comparaison des résultats.                        |
| 23     | Registry - Register Model       | Enregistrement de modèles dans le registre pour les rendre disponibles pour des prédictions.      |
| 24     | Register Elastic Model          | Procédure détaillée pour enregistrer un modèle ElasticNet dans le registre.                        |
| 25     | Simplified Code                 | Version simplifiée du code d’entraînement et d’enregistrement.                                     |
| 26     | MLproject                       | Définition d’un fichier MLproject pour gérer les configurations de projet avec MLflow.            |
| 27     | Run Script                      | Script de lancement du projet MLflow pour standardiser les exécutions.                             |
| 28     | CLI Commands                    | Commandes CLI pour interagir avec MLflow pour les utilisateurs avancés.                           |
| 29     | CLI Commands (1)                | Suite des commandes CLI, ajout de nouvelles fonctionnalités et options.                            |
```


---------------------
# ANNEXE:
---------------------



```plaintext
+----------------------------------------+
|        01 - Code de Base ML            |
| - Modèle simple sans MLflow            |
+----------------------------------------+
                |
                v
+----------------------------------------+
|  02 - Premier Code ML avec MLflow      |
| - Entraînement de modèle               |
| - Enregistrement de paramètres         |
| - Enregistrement de métriques          |
+----------------------------------------+
                |
                v
+----------------------------------------+
|     03 - Configuration URI Suivi       |
| - mlflow.set_tracking_uri              |
| - mlflow.get_tracking_uri              |
+----------------------------------------+
                |
                v
+----------------------------------------+
|    04 - Création d'Expérience          |
| - mlflow.create_experiment             |
| - Définition des métadonnées           |
+----------------------------------------+
                |
                v
+----------------------------------------+
|    05 - Gestion des Exécutions Actives |
| - mlflow.start_run                     |
| - mlflow.end_run                       |
| - mlflow.last_active_run               |
+----------------------------------------+
                |
                v
+----------------------------------------+
|       06 - Enregistrement Artefacts    |
| - mlflow.log_artifacts                 |
+----------------------------------------+
                |
                v
+----------------------------------------+
|       07 - Ajout de Tags               |
| - mlflow.set_tags                      |
+----------------------------------------+
                |
                v
+----------------------------------------+
|       08 - Lancement Exécutions        |
| - Multiple runs dans un script         |
+----------------------------------------+
                |
                v
+----------------------------------------+
|       09 - Lancement Expériences       |
| - Différents algorithmes (ElasticNet,  |
|   Ridge, Lasso)                        |
+----------------------------------------+
                |
                v
+----------------------------------------+
|   10 - Automatisation avec Autolog     |
| - mlflow.autolog                       |
+----------------------------------------+
                |
                v
+----------------------------------------+
|  11 - Commande Serveur MLflow          |
| - Lancement d'un serveur de suivi      |
+----------------------------------------+
                |
                v
+----------------------------------------+
|    12 - Signature de Modèle et Entrée  |
| - Signature et exemples d'entrée       |
+----------------------------------------+
                |
                v
+----------------------------------------+
|  13 - Inférence de la Signature        |
| - mlflow.models.infer_signature        |
+----------------------------------------+
                |
                v
+----------------------------------------+
|      14 - Extension de la Signature    |
+----------------------------------------+
                |
                v
+----------------------------------------+
|   15 - Personnalisation du Modèle      |
+----------------------------------------+
                |
                v
+----------------------------------------+
|  16 - Amélioration Personnalisation    |
+----------------------------------------+
                |
                v
+----------------------------------------+
|    17 - Chargement Modèle Enregistré   |
| - mlflow.pyfunc.load_model             |
+----------------------------------------+
                |
                v
+----------------------------------------+
|         18 - Évaluation Modèle         |
| - Évaluation des performances          |
+----------------------------------------+
                |
                v
+----------------------------------------+
| 19 - Métrique Personnalisée & Artefact |
| - Création de métriques personnalisées |
+----------------------------------------+
                |
                v
+----------------------------------------+
|   20 - Seuil de Validation             |
+----------------------------------------+
                |
                v
+----------------------------------------+
| 21 - Chargement Modèle du Registre     |
| - Récupération de modèles enregistrés  |
+----------------------------------------+
                |
                v
+----------------------------------------+
| 22 - Régression ElasticNet Sans MLflow |
+----------------------------------------+
                |
                v
+----------------------------------------+
| 23 - Enregistrement Modèle dans Reg.   |
+----------------------------------------+
                |
                v
+----------------------------------------+
| 24 - Enregistrement Modèle ElasticNet  |
+----------------------------------------+
                |
                v
+----------------------------------------+
| 25 - Code Simplifié pour MLflow        |
+----------------------------------------+
                |
                v
+----------------------------------------+
| 26 - Définition de Projet MLflow       |
+----------------------------------------+
                |
                v
+----------------------------------------+
| 27 - Script d'Exécution de Projet      |
+----------------------------------------+
                |
                v
+----------------------------------------+
| 28 - Commandes CLI pour MLflow         |
+----------------------------------------+
                |
                v
+----------------------------------------+
| 29 - Commandes CLI Avancées            |
+----------------------------------------+
```




