
# 1 - Liste de commandes 
```bash
mlflow doctor

mlflow doctor --mask-envs

mlflow artifacts list --run-id b18697e8c62945e6adbdef5cb1af6c21

mlflow artifacts download --run-id b18697e8c62945e6adbdef5cb1af6c21 --dst-path cli_artifact

mlflow artifacts log-artifacts --local-dir cli_artifact --run-id b18697e8c62945e6adbdef5cb1af6c21 --artifact-path cli_artifact

mlflow db upgrade sqlite:///mlflow.db

mlflow experiments create --experiment-name cli_experiment

mlflow experiments rename --experiment-id 26 --new-name test1

mlflow experiments delete --experiment-id 26

mlflow experiments restore --experiment-id 26

mlflow experiments search --view "all" 

mlflow experiments csv --experiment-id 6 --filename test.csv

mlflow runs list --experiment-id 6 --view "all"

mlflow runs describe --run-id 97e72d1a3a074e97a4a59b95625cca64

mlflow runs delete --run-id 

mlflow runs restore --run-id
```

# 2 - Explications 

### Liste des Commandes MLflow et Leurs Explications

#### `mlflow doctor`

```bash
mlflow doctor
```
Cette commande exécute des diagnostics pour vérifier la configuration de votre environnement MLflow. Elle génère un rapport contenant des informations utiles sur les versions de dépendances, les variables d'environnement et la configuration générale de MLflow.

#### `mlflow doctor --mask-envs`

```bash
mlflow doctor --mask-envs
```
Cette variante de la commande `mlflow doctor` masque les valeurs des variables d'environnement dans le rapport. Cela peut être utile pour protéger les informations sensibles tout en effectuant des diagnostics.

#### `mlflow artifacts list --run-id <run-id>`

```bash
mlflow artifacts list --run-id b18697e8c62945e6adbdef5cb1af6c21
```
Cette commande liste tous les artefacts associés à un ID de run spécifique. Elle est utile pour voir les fichiers et répertoires enregistrés lors de ce run.

- **`--run-id <run-id>`** : L'ID du run dont vous voulez lister les artefacts.

#### `mlflow artifacts download --run-id <run-id> --dst-path <path>`

```bash
mlflow artifacts download --run-id b18697e8c62945e6adbdef5cb1af6c21 --dst-path cli_artifact
```
Cette commande télécharge les artefacts d'un run spécifique vers un répertoire local.

- **`--run-id <run-id>`** : L'ID du run dont vous voulez télécharger les artefacts.
- **`--dst-path <path>`** : Le chemin local où les artefacts seront téléchargés.

#### `mlflow artifacts log-artifacts --local-dir <dir> --run-id <run-id> --artifact-path <path>`

```bash
mlflow artifacts log-artifacts --local-dir cli_artifact --run-id b18697e8c62945e6adbdef5cb1af6c21 --artifact-path cli_artifact
```
Cette commande enregistre les fichiers d'un répertoire local comme artefacts dans un run spécifique.

- **`--local-dir <dir>`** : Le répertoire local contenant les fichiers à enregistrer.
- **`--run-id <run-id>`** : L'ID du run où les artefacts seront enregistrés.
- **`--artifact-path <path>`** : Le chemin dans l'artefact où les fichiers seront enregistrés.

#### `mlflow db upgrade <uri>`

```bash
mlflow db upgrade sqlite:///mlflow.db
```
Cette commande met à jour la base de données MLflow vers la dernière version de schéma.

- **`<uri>`** : L'URI de la base de données, ici une base de données SQLite.

#### `mlflow experiments create --experiment-name <name>`

```bash
mlflow experiments create --experiment-name cli_experiment
```
Cette commande crée un nouvel expériment avec le nom spécifié.

- **`--experiment-name <name>`** : Le nom de l'expériment à créer.

#### `mlflow experiments rename --experiment-id <id> --new-name <name>`

```bash
mlflow experiments rename --experiment-id 26 --new-name test1
```
Cette commande renomme un expériment existant avec un nouvel identifiant et un nouveau nom.

- **`--experiment-id <id>`** : L'ID de l'expériment à renommer.
- **`--new-name <name>`** : Le nouveau nom de l'expériment.

#### `mlflow experiments delete --experiment-id <id>`

```bash
mlflow experiments delete --experiment-id 26
```
Cette commande supprime un expériment spécifié par son ID. Notez que cela marque l'expériment comme supprimé dans la base de données, mais ne le supprime pas physiquement.

- **`--experiment-id <id>`** : L'ID de l'expériment à supprimer.

#### `mlflow experiments restore --experiment-id <id>`

```bash
mlflow experiments restore --experiment-id 26
```
Cette commande restaure un expériment supprimé, le rendant à nouveau disponible.

- **`--experiment-id <id>`** : L'ID de l'expériment à restaurer.

#### `mlflow experiments search --view "all"`

```bash
mlflow experiments search --view "all"
```
Cette commande recherche et affiche tous les expériment présents, y compris ceux supprimés. Le paramètre `--view "all"` inclut les expériment actifs et supprimés.

#### `mlflow experiments csv --experiment-id <id> --filename <filename>`

```bash
mlflow experiments csv --experiment-id 6 --filename test.csv
```
Cette commande exporte les détails de l'expériment spécifié vers un fichier CSV.

- **`--experiment-id <id>`** : L'ID de l'expériment à exporter.
- **`--filename <filename>`** : Le nom du fichier CSV de sortie.

#### `mlflow runs list --experiment-id <id> --view "all"`

```bash
mlflow runs list --experiment-id 6 --view "all"
```
Cette commande liste tous les runs d'un expériment spécifié. Le paramètre `--view "all"` inclut les runs actifs, supprimés et restaurés.

- **`--experiment-id <id>`** : L'ID de l'expériment dont vous voulez lister les runs.

#### `mlflow runs describe --run-id <run-id>`

```bash
mlflow runs describe --run-id 97e72d1a3a074e97a4a59b95625cca64
```
Cette commande décrit un run spécifique en affichant ses détails, y compris les paramètres, les métriques et les artefacts.

- **`--run-id <run-id>`** : L'ID du run à décrire.

#### `mlflow runs delete --run-id <run-id>`

```bash
mlflow runs delete --run-id <run-id>
```
Cette commande marque un run spécifique comme supprimé.

- **`--run-id <run-id>`** : L'ID du run à supprimer.

#### `mlflow runs restore --run-id <run-id>`

```bash
mlflow runs restore --run-id <run-id>
```
Cette commande restaure un run supprimé, le rendant à nouveau disponible.

- **`--run-id <run-id>`** : L'ID du run à restaurer.

Ces commandes vous permettent de gérer efficacement vos expériences et runs MLflow, de la création à la suppression, en passant par la gestion des artefacts et des bases de données.





