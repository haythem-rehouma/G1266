

```bash
# Diagnostic complet de l'installation MLflow
mlflow doctor

# Diagnostic MLflow avec masquage des variables d'environnement
mlflow doctor --mask-envs

# Liste des artefacts pour un ID de run spécifique
mlflow artifacts list --run-id b18697e8c62945e6adbdef5cb1af6c21

# Téléchargement des artefacts pour un ID de run spécifique vers un dossier local
mlflow artifacts download --run-id b18697e8c62945e6adbdef5cb1af6c21 --dst-path cli_artifact

# Enregistrement des artefacts depuis un dossier local vers un run MLflow
mlflow artifacts log-artifacts --local-dir cli_artifact --run-id b18697e8c62945e6adbdef5cb1af6c21 --artifact-path cli_artifact

# Mise à jour de la base de données MLflow pour une version supérieure
mlflow db upgrade sqlite:///mlflow.db

# Création d'une nouvelle expérience MLflow avec un nom spécifique
mlflow experiments create --experiment-name cli_experiment

# Renommage d'une expérience existante en utilisant son ID
mlflow experiments rename --experiment-id 26 --new-name test1

# Suppression d'une expérience MLflow par son ID
mlflow experiments delete --experiment-id 26

# Restauration d'une expérience MLflow supprimée par son ID
mlflow experiments restore --experiment-id 26

# Recherche et affichage de toutes les expériences MLflow, y compris les supprimées
mlflow experiments search --view "all"

# Exportation des résultats d'une expérience MLflow dans un fichier CSV
mlflow experiments csv --experiment-id 6 --filename test.csv

# Liste des runs associés à une expérience donnée, en affichant toutes les vues (actives, supprimées)
mlflow runs list --experiment-id 6 --view "all"

# Description détaillée d'un run spécifique par son ID
mlflow runs describe --run-id 97e72d1a3a074e97a4a59b95625cca64

# Suppression d'un run spécifique par son ID
mlflow runs delete --run-id [ID_DU_RUN]

# Restauration d'un run supprimé par son ID
mlflow runs restore --run-id [ID_DU_RUN]
```

### Explications 📄

- **mlflow doctor** : Diagnostique de l’installation et des dépendances MLflow.
- **mlflow artifacts** : Gestion des artefacts dans MLflow, avec des options pour lister, télécharger et enregistrer des fichiers.
- **mlflow db upgrade** : Met à jour la base de données vers une nouvelle version de MLflow.
- **mlflow experiments** : Gestion des expériences MLflow (création, renommage, suppression, restauration).
- **mlflow runs** : Gestion des runs MLflow, y compris la description, suppression et restauration.

Ces commandes permettent une gestion complète des expériences et runs, ainsi que des artefacts MLflow.
