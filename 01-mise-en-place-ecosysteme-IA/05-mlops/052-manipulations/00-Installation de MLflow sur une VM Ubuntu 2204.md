# Installation de MLflow sur une VM Ubuntu 22.04

Ce guide vous aidera à installer MLflow sur une machine virtuelle Ubuntu 22.04. Suivez les étapes ci-dessous pour configurer votre environnement.

## Prérequis

- Une machine virtuelle (VM) Ubuntu 24.04 avec Python 3.12, ou une VM Ubuntu 22.04 avec Python 3.9 (et non Python 3.10, car cette version n'est pas stable). Si vous souhaitez exécuter le projet sur Ubuntu 22.04, veuillez consulter l'*annexe 00*.
- Accès à internet
- Droits sudo

## Étapes d'installation

### 1. Mettre à jour le système

Tout d'abord, assurez-vous que votre système est à jour :

```bash
sudo apt update
sudo apt upgrade -y (optionnel - ne le faites pas)
```

### 2. Installer Python et pip et création de l'environnement virtuel

MLflow nécessite Python. Nous allons installer Python 3 et pip (gestionnaire de paquets Python) :

```bash
sudo -s (ou su)
apt install python3 python3-pip -y
python3 --version
apt install python3.12-venv
python3 -m venv myenv (en cas de besoin : apt install python3.12-venv)
source myenv/bin/activate
pip install mlflow
deactivate (pour sortir)
```




### 3. Installer MLflow

Utilisez pip pour installer MLflow :

```bash
pip install mlflow
```

### 4. Installer d'autres dépendances (optionnel)

MLflow peut nécessiter des bibliothèques supplémentaires selon votre cas d'utilisation. Par exemple, pour une intégration avec scikit-learn :

```bash
pip install scikit-learn
```

### 5. Configurer le suivi de MLflow

Créez un répertoire pour stocker vos expériences MLflow :

```bash
mkdir ~/mlflow-experiments
cd ~/mlflow-experiments
```

Lancez le serveur de suivi MLflow en spécifiant ce répertoire :

```bash
mkdir database
mlflow server --backend-store-uri sqlite:///database/mlflow.db --default-artifact-root=file:mlruns --host 0.0.0.0 --port 5000
```


> Exercice - comparez les commandes suivantes (voir la réponse à l'annexe 4)

```
mlflow ui
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5000
mlflow server --backend-store-uri sqlite:///database/mlflow.db --default-artifact-root=file:mlruns --host 0.0.0.0 --port 5000
mlflow server --backend-store-uri sqlite:///database/mlflow.db  --default-artifact-root ~/mlflow-experiments --host 0.0.0.0 --port 5000
```

### Différence entre les commandes

 | Commande                                                                                                                                 | Rôle                                                  | Backend (métadonnées)                        | Artifacts (fichiers, modèles…)                                | Host / Accès                                    | Usage typique                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------- |
| `mlflow ui`                                                                                                                              | Interface rapide locale (sans vrai serveur configuré) | Dossier `./mlruns` par défaut                | `./mlruns` dans le dossier courant                            | `127.0.0.1` (local seulement)                   | Exploration rapide de runs sur sa machine perso                            |
| `mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5000`                    | Serveur MLflow simple, tout dans le projet local      | Fichier `mlflow.db` dans **dossier courant** | Dossier `./mlruns` dans **dossier courant**                   | `127.0.0.1` (local uniquement)                  | Dev solo, petit projet, tout centralisé dans le repo                       |
| `mlflow server --backend-store-uri sqlite:///database/mlflow.db --default-artifact-root=file:mlruns --host 0.0.0.0 --port 5000`          | Serveur MLflow accessible sur le réseau               | Fichier `mlflow.db` dans `./database/`       | URI `file:mlruns` → dossier `mlruns` local                    | `0.0.0.0` (accessible depuis d’autres machines) | Petit serveur partagé en LAN, structure un peu plus propre                 |
| `mlflow server --backend-store-uri sqlite:///database/mlflow.db --default-artifact-root ~/mlflow-experiments --host 0.0.0.0 --port 5000` | Serveur MLflow “un peu plus prod”                     | Fichier `mlflow.db` dans `./database/`       | Dossier global `~/mlflow-experiments` (indépendant du projet) | `0.0.0.0` (réseau)                              | Serveur central pour plusieurs projets / utilisateurs sur une même machine |



## Exercice 2

### Étape 1

> Terminal 1

```bash
mlflow server --backend-store-uri sqlite:///database/mlflow.db --default-artifact-root ~/mlflow-experiments --host 0.0.0.0 --port 5000
```

### Étape 2

> Terminal 2
> 
```bash
nano hello-world.py
python3 hello-world.py
```



```python
import mlflow

# Optionally set the tracking URI
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Set the experiment name
mlflow.set_experiment("Default")

# Start a new MLflow run
with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("metric1", 0.85)
    mlflow.set_tag("tag1", "example")
```


### Étape 3

### (optionnel) base de donnée sqlite

## 1. Aller au bon dossier

Selon ta commande :

```bash
mlflow server --backend-store-uri sqlite:///database/mlflow.db ...
```

la base est dans le dossier `database/` :

```bash
cd ~/mlflow-experiments/database
ls
# tu dois voir : mlflow.db
```

---

## 2. Installer l’outil SQLite (une fois)

```bash
sudo apt update
sudo apt install sqlite3 -y
```

---

## 3. Ouvrir la base `mlflow.db`

```bash
sqlite3 mlflow.db
```

Tu arrives dans un prompt `sqlite>`.

---

## 4. Commandes utiles dans SQLite

Dans le prompt :

```sql
.tables;                    -- liste les tables MLflow
.schema experiments;        -- structure de la table des expériences
SELECT * FROM experiments;  -- voir les expériences
SELECT * FROM runs LIMIT 5; -- voir les premiers runs
.quit                       -- pour sortir
```

🛑 **Conseil** : ne modifie rien (pas de DELETE/UPDATE) sinon tu risques de casser le tracking MLflow. Utilise ça seulement pour **consulter**.



### 6. Accéder à l'interface MLflow

Par défaut, le serveur MLflow s'exécute sur le port 5000. Vous pouvez y accéder via votre navigateur web à l'adresse suivante :

```
http://<IP-de-votre-VM>:5000
```

Remplacez `<IP-de-votre-VM>` par l'adresse IP de votre VM Ubuntu 22.04.

## Utilisation de base de MLflow

### Enregistrer un modèle

- Exemple hello-world d'enregistrement d'un modèle avec MLflow :
- Ouvrir un autre final 
```bash
apt-get update -y && apt-get install -y gcc && apt-get install -y git
nano hello-world.py
cd mlflow-experiments/
ls
cd database/
ls
cd ..
ls
nano hello-world.py
python hello-world.py
python3 hello-world.py
ls -la
cd ..
ls -la
source myenv/bin/activate
ls
cd mlflow-experiments/
ls
python3 hello-world.py
history

```
# troubleshooting : 
```bash
PATH=$PATH:/home/root/.local/bin
```

```bash
nano hello-world.py
```

```python
import mlflow

# Optionally set the tracking URI
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Set the experiment name
mlflow.set_experiment("Default")

# Start a new MLflow run
with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("metric1", 0.85)
    mlflow.set_tag("tag1", "example")
```


```bash
python3 hello-world.py
```

## Cette commande ne fonctionne pas 
```bash
mlflow server --backend-store-uri sqlite:///database/mlflow.db  --default-artifact-root ~/mlflow-experiments --host 0.0.0.0 --port 5000
```

## Utilisez cette commande :
```bash
mlflow ui
```

ou 

```bash
   mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5000
```

## Allez à http://127.0.0.1:5000

### Suivi des expériences

Vous pouvez visualiser les expériences et les métriques enregistrées dans l'interface MLflow.
## Utilisez cette commande :
```bash
mlflow ui
```
## Allez à http://127.0.0.1:5000

## Ressources supplémentaires

- [Documentation officielle de MLflow](https://mlflow.org/docs/latest/index.html)
- [Tutoriels MLflow](https://mlflow.org/docs/latest/tutorials-and-examples/index.html)

## Conclusion

Vous avez maintenant installé et configuré MLflow sur votre VM Ubuntu 22.04. Vous pouvez commencer à suivre et à gérer vos expériences de machine learning. N'hésitez pas à explorer davantage les fonctionnalités offertes par MLflow pour améliorer votre flux de travail de data science.





<br/>
<br/>


# Annexe 00: Installer python 3.9 et création d'un environnement virtuel dans Ubuntu 22.04

```python
rm -rf myenv
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.9 python3.9-venv python3.9-dev -y
python3.9 --version
python3.9 -m venv myenv
source myenv/bin/activate
```
 



<br/>
<br/>


# Annexe 01: Le ID d'expérience est obligatoire



- Il est obligatoire que MLflow crée une expérience s'il n'en existe pas.
- La définition d'un ID d'expérience est nécessaire, sinon on récupère le ID d'une expérience.

```python
import mlflow

# Définir ou créer une expérience nommée "Default" si elle n'existe pas
mlflow.set_experiment("Default")

with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("metric1", 0.85)
    mlflow.set_tag("tag1", "example")
```

### Explication des modifications
1. **mlflow.set_experiment("Default")** : Cette ligne permet de créer une nouvelle expérience si elle n'existe pas déjà, ce qui garantit que MLflow utilise un contexte d'expérience valide.
  
2. **Optionnel** : Si vous connaissez l'ID de l'expérience, vous pouvez le préciser dans `start_run` :
   ```python
   with mlflow.start_run(experiment_id=1):  # Remplacez 1 par l'ID de votre expérience
   ```


<br/>
<br/>



# Annexe 02: Différence entre mlflow server et mlflow ui ?




La différence principale entre `mlflow server` et `mlflow ui` réside dans les fonctionnalités de déploiement et la gestion de l'infrastructure de suivi des expériences.

### 1. **`mlflow server`** 

Cette commande démarre un **serveur MLflow** qui peut être utilisé en production pour stocker et suivre les expériences de manière centralisée. Elle permet de spécifier des configurations pour le backend (base de données) et les artefacts (fichiers générés lors des exécutions d'expérience) :

   - **`--backend-store-uri`** : définit l'emplacement de stockage des métadonnées des expériences (ID, paramètres, métriques, etc.). Ici, `sqlite:///database/mlflow.db` indique que MLflow utilisera une base de données SQLite.
   - **`--default-artifact-root`** : spécifie l'emplacement de stockage des artefacts. `file:mlruns` indique que les artefacts seront enregistrés dans un dossier local (`mlruns`). Pour un environnement de production, on peut aussi utiliser un stockage distant (S3, GCS, etc.).
   - **`--host` et `--port`** : configurent l'adresse IP et le port sur lesquels le serveur sera accessible. Avec `--host 0.0.0.0`, le serveur sera accessible depuis d'autres machines.

**Usage typique** : `mlflow server` est utilisé pour déployer un serveur MLflow centralisé, par exemple pour une équipe de data scientists travaillant sur des projets collaboratifs.

### 2. **`mlflow ui`**

Cette commande démarre une **interface utilisateur locale et temporaire** pour visualiser les expériences MLflow, sans options avancées de backend ou de stockage d'artefacts.

   - La base de données et les artefacts sont stockés par défaut dans un dossier local (`mlruns`) sans possibilité de personnaliser ces emplacements.
   - Elle est uniquement destinée à une utilisation rapide et locale, sur la machine de l'utilisateur.

**Usage typique** : `mlflow ui` est idéal pour des tests locaux rapides ou pour visualiser des expériences sans déployer de serveur centralisé.

### En résumé

- **`mlflow server`** : pour un déploiement robuste, multi-utilisateurs, et configurable en production.
- **`mlflow ui`** : pour une interface locale de visualisation rapide, sans configuration avancée.



<br/>
<br/>



# Annexe 03: Erreur serveur



![image](https://github.com/user-attachments/assets/b6be7222-80b2-45a7-8653-4588e21dc78d)


##### Exemple de code :

```python
import mlflow

# Optionally set the tracking URI
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Set the experiment name
mlflow.set_experiment("Default")

# Start a new MLflow run
with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("metric1", 0.85)
    mlflow.set_tag("tag1", "example")
```

Assurez-vous que le serveur MLflow est démarré avant d'exécuter ce code, comme expliqué précédemment.



Le code ci-haut  configure bien l'URI de traçage pour MLflow, mais l'erreur que vous voyez dans l'image ("Unable to connect to the server at 127.0.0.1:5000") indique que le serveur MLflow n'est pas en cours d'exécution sur cette adresse. Voici quelques vérifications et étapes de dépannage pour résoudre le problème :

1. **Vérifiez si le serveur MLflow est démarré** : Assurez-vous d'avoir démarré le serveur MLflow en exécutant cette commande dans le terminal :
   ```bash
   mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5000
   ```
   Cela démarrera le serveur MLflow sur `http://127.0.0.1:5000`.

2. **Vérifiez si le port 5000 est utilisé** : Si le port 5000 est déjà occupé par un autre service, MLflow ne pourra pas se connecter. Vous pouvez vérifier cela avec :
   ```bash
   lsof -i :5000
   ```
   Si le port est utilisé, vous pouvez choisir un autre port pour MLflow, par exemple 5001, et modifier votre code ainsi :
   ```python
   mlflow.set_tracking_uri("http://127.0.0.1:5001")
   ```

3. **Vérifiez votre pare-feu ou antivirus** : Assurez-vous que le port 5000 n'est pas bloqué par un pare-feu ou un antivirus.

4. **Relancez le navigateur** : Parfois, il peut s'agir d'un problème temporaire de connexion avec le navigateur. Relancer Firefox pourrait aider.

Après avoir suivi ces étapes, essayez de recharger la page et de voir si le problème persiste.



<br/>
<br/>


# Annexe 4 - Réponse à votre exercice - Comparaison entre les 4 commandes


# **1. `mlflow ui`**

- **Description** :  
  Lance simplement l'interface utilisateur de MLflow, **en mode local et simplifié**.

- **Caractéristiques** :
  - Pas de serveur d’expérimentation complet.
  - Utilise par défaut le répertoire `mlruns/` dans le dossier courant.
  - Pas de stockage backend explicitement défini.
  - Adapté pour un usage rapide ou exploratoire.

- **Utilisation typique** :  
  Démo locale, test rapide, sans base de données personnalisée.


# **2. `mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5000`**

- **Description** :  
  Démarre le **serveur complet MLflow Tracking Server**.

- **Caractéristiques** :
  - **Backend store** : SQLite (fichier `mlflow.db` à la racine).
  - **Artifact root** : dossier local `./mlruns`.
  - **Host** : accessible uniquement depuis la machine locale (`127.0.0.1`).
  - **Port** : 5000.

- **Utilisation typique** :  
  Projet local avec traçabilité durable via SQLite, **non accessible à distance**.


# **3. `mlflow server --backend-store-uri sqlite:///database/mlflow.db --default-artifact-root=file:mlruns --host 0.0.0.0 --port 5000`**

- **Description** :  
  Démarre un serveur MLflow **accessible depuis l’extérieur**.

- **Caractéristiques** :
  - **Backend store** : SQLite (dans `database/mlflow.db`).
  - **Artifact root** : `file:mlruns` — notation explicite pour URI locale.
  - **Host** : `0.0.0.0` → accessible depuis **toute adresse IP** (LAN, Docker, etc.).
  - **Port** : 5000.

- **Différence principale avec la commande 2** :
  - Meilleure accessibilité réseau.
  - Chemin des artefacts défini comme URI explicite.

- **Utilisation typique** :  
  Déploiement sur une machine partagée ou dans un conteneur, pour usage collaboratif.


# **4. `mlflow server --backend-store-uri sqlite:///database/mlflow.db  --default-artifact-root ~/mlflow-experiments --host 0.0.0.0 --port 5000`**

- **Description** :  
  Même logique que la commande 3, avec un répertoire d’artefacts plus personnalisé.

- **Caractéristiques** :
  - **Backend store** : SQLite dans un sous-dossier `database/`.
  - **Artifact root** : dans le répertoire personnel (`~/mlflow-experiments`).
  - **Host** : ouvert à tous (`0.0.0.0`).
  - **Port** : 5000.

- **Utilisation typique** :  
  Environnement de développement collaboratif, avec un emplacement d’artefacts plus stable et propre à l’utilisateur.


### **Comparaison synthétique**

| Commande | Backend Store | Artifact Root | Accessibilité | Cas d’usage |
|---------|----------------|----------------|----------------|-------------|
| `mlflow ui` | Par défaut (./mlruns) | Par défaut | Local uniquement | Exploration rapide |
| Cmd 2 | `sqlite:///mlflow.db` | `./mlruns` | Local (`127.0.0.1`) | Projet local solo |
| Cmd 3 | `sqlite:///database/mlflow.db` | `file:mlruns` | Réseau (`0.0.0.0`) | Collaboration, conteneurs |
| Cmd 4 | `sqlite:///database/mlflow.db` | `~/mlflow-experiments` | Réseau (`0.0.0.0`) | Collaboration, dossier dédié |




### Comparaison finale

```
+---------+-----------------------------------------+---------------------------+------------------+-----------------------------+
| Cmd N°  | Backend Store URI                       | Artifact Root             | Host / Access     | Usage recommandé            |
+---------+-----------------------------------------+---------------------------+------------------+-----------------------------+
| 1       | (Par défaut, implicite)                 | ./mlruns (défaut)         | 127.0.0.1         | Usage local rapide          |
|         |                                         |                           | (local seulement) | Interface simple (mlflow ui)|
+---------+-----------------------------------------+---------------------------+------------------+-----------------------------+
| 2       | sqlite:///mlflow.db                     | ./mlruns                  | 127.0.0.1         | Projet local avec traçage   |
|         | (fichier dans le dossier courant)       |                           | (local seulement) | Persistance avec SQLite     |
+---------+-----------------------------------------+---------------------------+------------------+-----------------------------+
| 3       | sqlite:///database/mlflow.db            | file:mlruns               | 0.0.0.0           | Serveur collaboratif local  |
|         | (fichier dans dossier `database/`)      | (notation URI explicite)  | (réseau ouvert)   | Compatible conteneurs       |
+---------+-----------------------------------------+---------------------------+------------------+-----------------------------+
| 4       | sqlite:///database/mlflow.db            | ~/mlflow-experiments      | 0.0.0.0           | Environnement partagé       |
|         | (même que commande 3)                   | (répertoire utilisateur)  | (réseau ouvert)   | Artefacts centralisés       |
+---------+-----------------------------------------+---------------------------+------------------+-----------------------------+
```


<br/>
<br/>


# Anenxe 5 - Utilisation de MLflow avec une Base de Données (Backend Store)

## 1. Pourquoi MLflow a-t-il besoin d'une base de données ?

MLflow permet de gérer le cycle de vie des expériences de machine learning. Pour assurer la **traçabilité**, **la persistance** et **la consultation des résultats**, un stockage structuré des métadonnées est requis. Ces métadonnées incluent :

- Les expériences (`experiments`)
- Les exécutions (`runs`)
- Les hyperparamètres (`params`)
- Les métriques (`metrics`)
- Les artefacts associés (chemin d’accès uniquement, pas le contenu)
- Les statuts, durées, auteurs, etc.

Par défaut, la commande `mlflow ui` utilise un **stockage local** (dossier `mlruns`) sans base de données. Toutefois, pour des cas d'usage réels, collaboratifs ou reproductibles, il est fortement recommandé de lancer le **serveur MLflow complet** (`mlflow server`) avec une base de données dédiée appelée **backend store**.



## 2. Options de base de données compatibles

| Type            | URI Exemple                                         | Cas d’usage              | Avantages                        | Limitations                         |
|------------------|----------------------------------------------------|---------------------------|-----------------------------------|-------------------------------------|
| SQLite (fichier local) | `sqlite:///mlflow.db`                        | Développement local       | Simple, portable                  | Non adapté à l’usage concurrent     |
| MySQL           | `mysql+pymysql://user:pass@host/db_name`           | Usage collaboratif        | Scalable, robuste                 | Configuration plus complexe         |
| PostgreSQL      | `postgresql://user:pass@host:port/db_name`         | Production                | Sécurité, robustesse              | Requiert une installation serveur   |
| Databricks      | Configuration spécifique à Databricks              | Cloud entreprise          | Intégré à leur écosystème         | Usage restreint, payant             |



## 3. Exemple de configuration avec SQLite

```bash
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns \
  --host 127.0.0.1 \
  --port 5000
```

- `--backend-store-uri` : précise l’emplacement du fichier de base de données (ici, `mlflow.db`)
- `--default-artifact-root` : dossier pour stocker les artefacts (modèles, images, logs)
- `--host` : définit la portée d’accès (127.0.0.1 = machine locale uniquement)
- `--port` : port d’écoute (5000 par défaut)

Ce serveur conserve toutes les informations importantes, même après redémarrage.



## 4. Pour un environnement multi-utilisateurs

Dans un contexte collaboratif (équipe MLOps, serveurs distants, Docker, etc.), il est préférable d’utiliser :

- `--host 0.0.0.0` pour rendre le serveur accessible à d’autres machines
- une base de données distante comme **PostgreSQL** ou **MySQL**
- un dossier d’artefacts accessible depuis toutes les machines (via NFS, S3, etc.)

Exemple avec PostgreSQL :

```bash
mlflow server \
  --backend-store-uri postgresql://user:pass@host:5432/mlflow_db \
  --default-artifact-root s3://mlflow-artifacts/ \
  --host 0.0.0.0 \
  --port 5000
```



## 5. Résumé

| Commande                  | Base de données requise | Persistant | Accessible en réseau | Recommandé en production |
|---------------------------|-------------------------|------------|------------------------|---------------------------|
| `mlflow ui`               | Non                     | Oui (fichiers locaux) | Non                    | Non                       |
| `mlflow server` + SQLite | Oui                     | Oui        | Optionnel (`--host`)   | Non (usage unique/local)  |
| `mlflow server` + PostgreSQL/MySQL | Oui         | Oui        | Oui                    | Oui                       |

