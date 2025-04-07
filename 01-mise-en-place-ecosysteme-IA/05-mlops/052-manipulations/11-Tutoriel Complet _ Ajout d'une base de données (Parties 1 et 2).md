# Tutoriel Complet :  Ajout d'une base de données (Parties 1 et 2)

## Partie 1 - Configuration de S3 après PostgreSQL sur une Machine Virtuelle Ubuntu 22.04

## Objectif

L'objectif de ce tutoriel est de vous guider dans la configuration de S3 comme stockage des artefacts après avoir configuré PostgreSQL comme backend store sur une machine virtuelle Ubuntu 22.04 pour MLflow.

## Prérequis

- Une machine virtuelle Ubuntu 22.04
- PostgreSQL installé et configuré
- AWS CLI installé et configuré
- Un bucket S3 créé sur AWS

## Étapes

### 1. Installation de PostgreSQL

Si PostgreSQL n'est pas encore installé sur votre machine virtuelle, vous pouvez l'installer en suivant ces étapes :

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Vérifiez que PostgreSQL est en cours d'exécution :

```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### 2. Configuration de PostgreSQL

Créez une base de données et un utilisateur pour MLflow :

```bash
sudo -u postgres psql
```

Dans l'invite PostgreSQL, exécutez les commandes suivantes :

```sql
CREATE DATABASE mlflowdb;
CREATE USER mlflowuser WITH ENCRYPTED PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE mlflowdb TO mlflowuser;
```

Remplacez `yourpassword` par un mot de passe sécurisé.

### 3. Installation d'AWS CLI

Installez AWS CLI en suivant ces étapes :

```bash
sudo apt update
sudo apt install awscli -y
```

Configurez AWS CLI avec vos identifiants AWS :

```bash
aws configure
```

Entrez vos `AWS Access Key ID`, `AWS Secret Access Key`, `Default region name`, et `Default output format`.

### 4. Configuration de S3

1. **Créer un Bucket S3**

   Connectez-vous à votre console AWS, allez à S3, et créez un bucket. Notez le nom du bucket.

2. **Configurer les Permissions IAM**

   Assurez-vous que votre utilisateur IAM dispose des permissions nécessaires pour accéder au bucket S3. Voici un exemple de politique IAM :

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "s3:ListBucket",
           "s3:GetObject",
           "s3:PutObject"
         ],
         "Resource": [
           "arn:aws:s3:::mlflow-artifacts-bucket",
           "arn:aws:s3:::mlflow-artifacts-bucket/*"
         ]
       }
     ]
   }
   ```

### 5. Lancer le Serveur MLflow

Utilisez la commande suivante pour lancer le serveur MLflow avec PostgreSQL comme backend store et S3 comme stockage des artefacts :

```bash
mlflow server --backend-store-uri postgresql://mlflowuser:yourpassword@localhost/mlflowdb \
              --default-artifact-root s3://mlflow-artifacts-bucket \
              --host 0.0.0.0 \
              --port 5000 \
              --no-serve-artifacts
```

Remplacez `yourpassword` par le mot de passe de votre utilisateur PostgreSQL et `mlflow-artifacts-bucket` par le nom de votre bucket S3.

### 6. Vérifier l'Accès

Accédez à l'interface MLflow dans votre navigateur à l'adresse suivante :

```
http://<IP-de-votre-VM>:5000
```

### Exemple Complet de Commande

Voici un exemple de script complet pour lancer le serveur MLflow avec PostgreSQL et S3 :

```bash
# Lancer le serveur MLflow avec PostgreSQL comme backend store et S3 comme stockage des artefacts
mlflow server --backend-store-uri postgresql://mlflowuser:yourpassword@localhost/mlflowdb \
              --default-artifact-root s3://mlflow-artifacts-bucket \
              --host 0.0.0.0 \
              --port 5000 \
              --no-serve-artifacts
```

### Conclusion

En suivant ces étapes, vous avez configuré PostgreSQL comme backend store et S3 comme stockage des artefacts pour MLflow sur une machine virtuelle Ubuntu 22.04. Vous pouvez maintenant suivre et gérer vos expériences de machine learning en utilisant une configuration robuste et évolutive.



# Partie 2 - Tutoriel : Lancement d'un Serveur MLflow

## Objectif

L'objectif de ce tutoriel est de vous guider dans le lancement d'un serveur MLflow en utilisant différentes configurations de stockage des métadonnées et des artefacts. Nous verrons comment utiliser SQLite et PostgreSQL comme backend stores, ainsi que S3 pour le stockage des artefacts.

## Prérequis

- Avoir MLflow installé sur votre machine ou serveur.
- Avoir accès à une base de données SQLite ou PostgreSQL.
- Avoir un bucket S3 configuré (si vous utilisez S3 pour le stockage des artefacts).

## Étapes pour Lancer le Serveur MLflow

### 1. Utilisation de SQLite comme Backend Store

#### Commande

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 127.0.0.1 --port 5000
```

#### Explication

- **`--backend-store-uri sqlite:///mlflow.db`** : Utilise une base de données SQLite nommée `mlflow.db` pour stocker les métadonnées des expériences MLflow.
- **`--default-artifact-root ./mlflow-artifacts`** : Définit le répertoire local `mlflow-artifacts` pour stocker les artefacts.
- **`--host 127.0.0.1`** : Définit l'adresse IP du serveur (localhost dans ce cas).
- **`--port 5000`** : Définit le port sur lequel le serveur MLflow sera accessible.

#### Exécution

Pour lancer le serveur MLflow avec cette configuration, exécutez la commande suivante dans votre terminal :

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 127.0.0.1 --port 5000
```

Accédez ensuite au serveur MLflow dans votre navigateur à l'adresse suivante :

```
http://127.0.0.1:5000
```

### 2. Utilisation de PostgreSQL comme Backend Store et S3 pour le Stockage des Artefacts

#### Commande

```bash
mlflow server --backend-store-uri postgresql://user:password@postgres:5432/mlflowdb --default-artifact-root s3://bucket_name --host remote_host --no-serve-artifacts
```

#### Explication

- **`--backend-store-uri postgresql://user:password@postgres:5432/mlflowdb`** : Utilise une base de données PostgreSQL pour stocker les métadonnées des expériences MLflow. Remplacez `user`, `password`, `postgres`, et `mlflowdb` par vos informations de connexion PostgreSQL.
- **`--default-artifact-root s3://bucket_name`** : Définit un bucket S3 pour stocker les artefacts. Remplacez `bucket_name` par le nom de votre bucket S3.
- **`--host remote_host`** : Définit l'adresse IP ou le nom de domaine du serveur. Remplacez `remote_host` par l'adresse de votre serveur.
- **`--no-serve-artifacts`** : Désactive le service des artefacts par le serveur MLflow. Utilisez cette option si les artefacts sont déjà accessibles via un autre service (par exemple, S3).

#### Exécution

Pour lancer le serveur MLflow avec cette configuration, exécutez la commande suivante dans votre terminal :

```bash
mlflow server --backend-store-uri postgresql://user:password@postgres:5432/mlflowdb --default-artifact-root s3://bucket_name --host remote_host --no-serve-artifacts
```

Remplacez les valeurs des paramètres par vos informations spécifiques. 

### Conclusion

En suivant ce tutoriel, vous avez appris à lancer un serveur MLflow en utilisant deux configurations différentes pour le stockage des métadonnées et des artefacts. Utilisez SQLite pour un stockage local simple ou PostgreSQL et S3 pour une configuration plus robuste et évolutive. Accédez à votre serveur MLflow pour suivre et gérer vos expériences de machine learning efficacement.

# Annexe : 


```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 127.0.0.1 --port 5000
mlflow server --backend-store-uri postgresql://user:password@postgres:5432/mlflowdb --default-artifact-root s3://bucket_name --host remote_host --no-serve-artifacts
```

# Explications :

### Explication des Commandes MLflow Server

#### Commande 1 : Utilisation de SQLite comme Backend Store

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 127.0.0.1 --port 5000
```

**Détails de la Commande :**

- **`mlflow server`** : Cette commande lance le serveur MLflow.

- **`--backend-store-uri sqlite:///mlflow.db`** : 
  - Utilise SQLite comme base de données pour stocker les métadonnées des expériences MLflow.
  - `sqlite:///mlflow.db` spécifie le chemin vers la base de données SQLite. Si `mlflow.db` n'existe pas, il sera créé dans le répertoire courant.

- **`--default-artifact-root ./mlflow-artifacts`** : 
  - Définit le répertoire par défaut pour stocker les artefacts des expériences.
  - `./mlflow-artifacts` est un chemin relatif qui spécifie que les artefacts seront stockés dans un répertoire nommé `mlflow-artifacts` dans le répertoire courant. Ce répertoire sera créé s'il n'existe pas déjà.

- **`--host 127.0.0.1`** : 
  - Spécifie l'adresse IP sur laquelle le serveur MLflow écoute.
  - `127.0.0.1` signifie que le serveur est accessible uniquement depuis le localhost (la machine locale).

- **`--port 5000`** : 
  - Spécifie le port sur lequel le serveur MLflow écoute.
  - `5000` est le numéro de port par défaut. Vous pouvez choisir n'importe quel port qui n'est pas utilisé par un autre service.

**Utilisation :**
Cette commande est idéale pour des environnements de développement ou des petites configurations locales. Elle est simple à configurer et ne nécessite pas de dépendances externes comme un serveur de base de données.

#### Commande 2 : Utilisation de PostgreSQL comme Backend Store et S3 pour le Stockage des Artefacts

```bash
mlflow server --backend-store-uri postgresql://user:password@postgres:5432/mlflowdb --default-artifact-root s3://bucket_name --host remote_host --no-serve-artifacts
```

**Détails de la Commande :**

- **`mlflow server`** : Cette commande lance le serveur MLflow.

- **`--backend-store-uri postgresql://user:password@postgres:5432/mlflowdb`** :
  - Utilise PostgreSQL comme base de données pour stocker les métadonnées des expériences MLflow.
  - `postgresql://user:password@postgres:5432/mlflowdb` spécifie l'URI de connexion à la base de données PostgreSQL.
    - `user` : Nom d'utilisateur de la base de données.
    - `password` : Mot de passe de l'utilisateur de la base de données.
    - `postgres` : Nom de domaine ou adresse IP du serveur PostgreSQL.
    - `5432` : Port sur lequel PostgreSQL écoute (port par défaut pour PostgreSQL).
    - `mlflowdb` : Nom de la base de données utilisée pour stocker les métadonnées MLflow.

- **`--default-artifact-root s3://bucket_name`** :
  - Définit le répertoire par défaut pour stocker les artefacts des expériences.
  - `s3://bucket_name` spécifie que les artefacts seront stockés dans un bucket S3 nommé `bucket_name`.
    - S3 (Simple Storage Service) est un service de stockage d'objets d'Amazon Web Services (AWS).

- **`--host remote_host`** :
  - Spécifie l'adresse IP ou le nom de domaine sur lequel le serveur MLflow écoute.
  - `remote_host` doit être remplacé par l'adresse de votre serveur accessible à distance.

- **`--no-serve-artifacts`** :
  - Désactive le service des artefacts par le serveur MLflow.
  - Utilisez cette option si les artefacts sont déjà accessibles via un autre service (par exemple, S3).

**Utilisation :**
Cette commande est idéale pour des environnements de production ou des configurations nécessitant des bases de données robustes et un stockage d'artefacts évolutif. PostgreSQL offre une gestion plus performante des transactions et des requêtes complexes, tandis que S3 fournit un stockage évolutif et sécurisé pour les artefacts.

### Résumé

- **Commande 1 :**
  - Simple à configurer.
  - Utilise SQLite pour les métadonnées et un répertoire local pour les artefacts.
  - Idéal pour le développement local.

- **Commande 2 :**
  - Utilise PostgreSQL pour les métadonnées et S3 pour les artefacts.
  - Nécessite des configurations externes (PostgreSQL, AWS S3).
  - Idéal pour les environnements de production.

Ces deux configurations permettent de choisir entre une solution rapide et locale pour le développement et une solution robuste et évolutive pour la production.

