# 1 - Commandes

```bash
# Diagnostic complet de l'installation MLflow
mlflow doctor

# Diagnostic MLflow avec masquage des variables d'environnement pour plus de sécurité
mlflow doctor --mask-envs

# Liste tous les artefacts associés à un run spécifique
mlflow artifacts list --run-id b18697e8c62945e6adbdef5cb1af6c21

# Télécharge les artefacts pour un run spécifique vers un répertoire local
mlflow artifacts download --run-id b18697e8c62945e6adbdef5cb1af6c21 --dst-path cli_artifact

# Enregistre des artefacts depuis un répertoire local vers un run dans MLflow
mlflow artifacts log-artifacts --local-dir cli_artifact --run-id b18697e8c62945e6adbdef5cb1af6c21 --artifact-path cli_artifact

# Mise à jour de la base de données MLflow vers une version supérieure
mlflow db upgrade sqlite:///mlflow.db

# Crée une nouvelle expérience MLflow avec un nom défini
mlflow experiments create --experiment-name cli_experiment

# Renomme une expérience existante via son ID
mlflow experiments rename --experiment-id 26 --new-name test1

# Supprime une expérience MLflow via son ID
mlflow experiments delete --experiment-id 26

# Restaure une expérience MLflow supprimée via son ID
mlflow experiments restore --experiment-id 26

# Recherche et affiche toutes les expériences, y compris celles supprimées
mlflow experiments search --view "all"

# Exporte les résultats d'une expérience en CSV
mlflow experiments csv --experiment-id 6 --filename test.csv

# Liste tous les runs d'une expérience spécifique, incluant les supprimés
mlflow runs list --experiment-id 6 --view "all"

# Donne une description détaillée d'un run par son ID
mlflow runs describe --run-id 97e72d1a3a074e97a4a59b95625cca64

# Supprime un run spécifique par son ID
mlflow runs delete --run-id [ID_DU_RUN]

# Restaure un run supprimé via son ID
mlflow runs restore --run-id [ID_DU_RUN]
```

# 2 - Explications 

- **mlflow doctor** : Permet de vérifier l'installation MLflow et d'identifier les éventuels problèmes.
- **mlflow artifacts** : Commandes pour gérer les artefacts associés aux runs, notamment pour la consultation, le téléchargement et l'enregistrement depuis ou vers MLflow.
- **mlflow db upgrade** : Met à jour la base de données associée à MLflow.
- **mlflow experiments** : Gère les expériences MLflow, permettant de les créer, renommer, supprimer, restaurer, et exporter.
- **mlflow runs** : Gère les runs dans MLflow, incluant la consultation de listes de runs, la description, suppression, et restauration.

Ces commandes vous aident à administrer les éléments principaux de MLflow, tels que les artefacts, expériences et runs, avec des options supplémentaires pour une gestion fine de la base de données et des diagnostics.
