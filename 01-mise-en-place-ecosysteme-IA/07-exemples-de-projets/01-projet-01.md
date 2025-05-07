# PROJET 1 — MLOps avec Docker, MLflow, PostgreSQL et pgAdmin

## Objectifs pédagogiques :

À la fin de ce projet, vous serez capable de :

1. Mettre en place un environnement MLOps local avec Docker.
2. Lancer un serveur MLflow connecté à PostgreSQL.
3. Visualiser les exécutions dans MLflow.
4. Gérer la base de données via pgAdmin.
5. Automatiser l'entraînement de 3 modèles avec un script Python.
6. Identifier les erreurs d’installation et les résoudre.

---

## AVANT DE COMMENCER – PRÉREQUIS TECHNIQUES

Vous devez absolument avoir les logiciels suivants installés :

* Docker
* Docker Compose

### Vérification de l’installation :

Dans un terminal, tapez :

```bash
docker --version
docker-compose --version
```

Si ces commandes ne fonctionnent pas, installez Docker avec ce script :

```bash
su         # ou sudo -s
pwd
git clone https://github.com/hrhouma/install-docker.git
cd install-docker/
chmod +x install-docker.sh
./install-docker.sh
```

Puis vérifiez à nouveau :

```bash
docker version
docker-compose version
```

---

## STRUCTURE DU PROJET

Le projet s'appelle **mlops-redwine**. Voici les dossiers/fichiers finaux que vous devez obtenir :

```plaintext
mlops-redwine/
├── data/
│   └── red-wine-quality.csv         # Fichier CSV avec les données
├── mlruns/                          # Artefacts générés par MLflow
├── pgadmin_config_local.py          # Fixe les sessions pgAdmin
├── requirements.txt                 # Dépendances Python
├── Dockerfile                       # Dockerfile pour l'environnement Python
├── train_model.py                   # Script d'entraînement
├── docker-compose.yml               # Orchestrateur Docker
```

---

## PHASE 1 — CRÉATION DES DOSSIERS ET STRUCTURE

Tapez ces commandes **une à une**, sans les modifier :

```bash
sudo -s                              # Passe en superutilisateur
mkdir mlops-redwine
cd mlops-redwine

mkdir data                           # Contiendra le fichier CSV
cd data
wget -O red-wine-quality.csv https://raw.githubusercontent.com/mlflow/mlflow/master/tests/datasets/winequality-red.csv
cd ..                                # Retour à la racine du projet

mkdir mlruns                         # Contiendra les artefacts MLflow

touch requirements.txt               # Dépendances Python
touch train_model.py                 # Script d'entraînement
touch Dockerfile                     # Dockerfile pour builder l'image
touch pgadmin_config_local.py        # Fix pgAdmin sessions
touch docker-compose.yml             # Stack Docker complète
apt install tree
tree ../mlops-redwine
```

---

## PHASE 2 — CONTENU DES FICHIERS (à copier dans chaque fichier)

### Fichier : `requirements.txt`

```txt
pandas
numpy
scikit-learn
mlflow
```

---

### Fichier : `train_model.py`

> Voici le code minimal pour entraîner automatiquement 3 modèles :

```python
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

data = pd.read_csv("data/red-wine-quality.csv")

X = data.drop(["quality"], axis=1)
y = data["quality"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

for i in range(3):
    alpha = 0.4 + i * 0.1
    l1_ratio = 0.5 + i * 0.1

    with mlflow.start_run():
        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        model.fit(X_train, y_train)
        predicted = model.predict(X_test)

        rmse, mae, r2 = eval_metrics(y_test, predicted)

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)
        mlflow.sklearn.log_model(model, "model")
```

---

### Fichier : `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "train_model.py"]
```

---

### Fichier : `pgadmin_config_local.py`

```python
SESSION_DB_PATH = '/tmp/pgadmin_sessions'
```

---

### Fichier : `docker-compose.yml`

```yaml
version: "3.8"

services:

  postgres:
    image: postgres:14
    environment:
      POSTGRES_USER: mlflow
      POSTGRES_PASSWORD: mlflow
      POSTGRES_DB: mlflow_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  mlflow:
    build: .
    environment:
      MLFLOW_TRACKING_URI: http://mlflow:5000
    ports:
      - "5000:5000"
    depends_on:
      - postgres
    command: >
      mlflow server 
      --backend-store-uri postgresql://mlflow:mlflow@postgres:5432/mlflow_db 
      --default-artifact-root /app/mlruns 
      --host 0.0.0.0
    volumes:
      - ./mlruns:/app/mlruns

  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "8080:80"
    volumes:
      - pgadmin_data:/var/lib/pgadmin
      - ./pgadmin_config_local.py:/pgadmin4/config_local.py

volumes:
  postgres_data:
  pgadmin_data:
```

---

## PHASE 3 — LANCEMENT DU PROJET

Dans le terminal :

```bash
docker-compose up --build
```

Attendez que les 3 services soient bien démarrés : `postgres`, `mlflow`, `pgadmin`.

---

## PHASE 4 — ACCÈS AUX INTERFACES

### Interface MLflow :

Ouvrir dans un navigateur :

```
http://localhost:5000
```

---

### Interface pgAdmin :

Ouvrir dans un navigateur :

```
http://localhost:8080
```

**Identifiants :**

* Email : `admin@admin.com`
* Mot de passe : `admin`

**Ajout manuel de la base PostgreSQL dans pgAdmin :**

1. Cliquez sur "Add New Server"
2. Onglet "General" : Nom du serveur : `mlflow-db`
3. Onglet "Connection" :

   * Host : `postgres`
   * Username : `mlflow`
   * Password : `mlflow`
4. Cliquez sur "Save"

---

## PHASE 5 — LANCEMENT DU SCRIPT D’ENTRAÎNEMENT

Dans un nouveau terminal, dans le dossier du projet :

```bash
docker-compose run --rm mlflow
```

Retournez sur l’interface MLflow : vous verrez 3 exécutions apparaître.

---

## PHASE 6 — RÉPARATION DES ERREURS (pgAdmin sessions)

Si vous voyez cette erreur :

```
[Errno 13] Permission denied: '/var/lib/pgadmin/sessions'
```

Exécutez ces commandes dans l’ordre :

```bash
docker exec -it $(docker ps -qf "ancestor=dpage/pgadmin4") bash
apt update && apt install sudo -y
sudo -s
mkdir -p /var/lib/pgadmin/sessions
chown -R pgadmin:pgadmin /var/lib/pgadmin/sessions
chmod 700 /var/lib/pgadmin/sessions
exit
exit
docker-compose restart pgadmin
```

---

## PHASE 7 — VÉRIFICATION FINALE

### Vous avez réussi si :

* MLflow s’ouvre sans erreur sur `http://localhost:5000`
* Vous voyez les 3 runs avec les métriques
* pgAdmin fonctionne sur `http://localhost:8080`
* Vous accédez à la base `mlflow_db` via pgAdmin







<br/>

# Annexe 0 -  Modifications critiques à appliquer

###  1. `requirements.txt` — Ajoute `psycopg2-binary`

Remplace le contenu par :

```txt
pandas
numpy
scikit-learn
mlflow
psycopg2-binary
```

> Cela permet à MLflow de se connecter à PostgreSQL sans erreur.



###  2. `pgadmin_config_local.py` — Remplace par une vraie config Python

Corrige ce fichier avec ce contenu **valide** :

```python
import os

DATA_DIR = "/var/lib/pgadmin"
LOG_FILE = os.path.join(DATA_DIR, "pgadmin4.log")
SQLITE_PATH = os.path.join(DATA_DIR, "pgadmin4.db")
SESSION_DB_PATH = '/tmp/pgadmin_sessions'
```

> Cela évite l'erreur `[Errno 13] Permission denied`.

---

###  3. Rebuild complet du projet

Après les modifications :

```bash
docker-compose down          # Arrêter proprement
docker-compose build         # Rebuild avec psycopg2
docker-compose up -d         # Relancer en mode détaché
```



##  Résumé des étapes MLOps

```bash
# 1. Crée la structure
mkdir mlops-redwine && cd mlops-redwine
mkdir data mlruns
wget -O data/red-wine-quality.csv https://raw.githubusercontent.com/mlflow/mlflow/master/tests/datasets/winequality-red.csv
touch requirements.txt train_model.py Dockerfile docker-compose.yml pgadmin_config_local.py

# 2. Copie les bons contenus dans chaque fichier (inclus ci-dessus)

# 3. Build et lance
docker-compose up --build

# 4. Lancement du script d’entraînement (3 modèles loggés dans MLflow)
docker-compose run --rm mlflow
```




<br/>

# Annexe 1 - Arborescence complète du projet `mlops-redwine/`


### Étape 1

```
sudo -s
apt install tree
mkdir mlops-redwine
tree mlops-redwine
```

### Étape 2

```
mlops-redwine/
├── data/
│   └── red-wine-quality.csv         ← Dataset téléchargé
├── mlruns/                          ← Dossier local pour stocker les artefacts
├── pgadmin_config_local.py          ← Fix sessions pgAdmin
├── requirements.txt                 ← Dépendances Python
├── Dockerfile                       ← Environnement d'entraînement
├── train_model.py                   ← Script d'entraînement
├── docker-compose.yml               ← Stack MLOps complète
```




<br/>

# Annexe 2 - Ports à ouvrir sur votre machine ou VM (Azure, AWS, etc.)

Pour que les services soient accessibles depuis un navigateur web (local ou distant), les ports suivants doivent impérativement être **ouverts** dans :

* Le pare-feu de votre système d'exploitation (Ubuntu, Windows, etc.)
* Les règles de sécurité de votre fournisseur cloud (Azure NSG, AWS Security Groups, etc.)

| Service           | Port interne (dans Docker) | Port externe (à exposer) | Nécessaire d’ouvrir               | Accès via navigateur |
| ----------------- | -------------------------- | ------------------------ | --------------------------------- | -------------------- |
| MLflow            | 5000                       | 5000                     | Oui                               | Oui                  |
| pgAdmin           | 80                         | 8080                     | Oui                               | Oui                  |
| PostgreSQL        | 5432                       | Facultatif               | Non (si usage interne uniquement) | Non                  |
| Docker Remote API | 2375 / 2376                | Non                      | Non                               | Non                  |

> Remarque : Le port PostgreSQL (5432) est uniquement requis si vous devez y accéder depuis un client externe (comme DBeaver). Pour ce projet, il est utilisé uniquement par MLflow dans le même réseau Docker, donc il n’est pas nécessaire de l’exposer à l’extérieur.

---

# Extrait à inclure dans `docker-compose.yml`

Assurez-vous que les ports suivants sont bien mappés dans le fichier `docker-compose.yml` :

```yaml
services:

  mlflow:
    ports:
      - "5000:5000"

  pgadmin:
    ports:
      - "8080:80"

  postgres:
    ports:
      - "5432:5432"  # peut être conservé mais pas nécessaire si pas d'accès externe
```

---

# URLs à tester dans votre navigateur

Selon que vous exécutez le projet **en local** ou sur une **machine virtuelle distante**, voici les adresses à tester :

### Si le projet tourne localement

| Service              | URL                                            | Authentification                                  |
| -------------------- | ---------------------------------------------- | ------------------------------------------------- |
| MLflow               | [http://localhost:5000](http://localhost:5000) | Aucune                                            |
| pgAdmin              | [http://localhost:8080](http://localhost:8080) | Email : [admin@admin.com](mailto:admin@admin.com) |
| Mot de passe : admin |                                                |                                                   |

### Si le projet tourne sur une VM distante (ex. Azure, AWS)

Admettons que l'adresse IP publique de votre VM soit `20.45.123.87` :

| Service              | URL externe à tester                                 | Authentification                                  |
| -------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| MLflow               | [http://20.45.123.87:5000](http://20.45.123.87:5000) | Aucune                                            |
| pgAdmin              | [http://20.45.123.87:8080](http://20.45.123.87:8080) | Email : [admin@admin.com](mailto:admin@admin.com) |
| Mot de passe : admin |                                                      |                                                   |

> Si ces URL ne s’ouvrent pas, c’est probablement que les ports 5000 et 8080 ne sont pas encore autorisés dans la configuration de votre fournisseur cloud (NSG Azure ou Security Group AWS).

---

# Vérification des ports ouverts sur Linux

Ouvrez un terminal et tapez :

```bash
sudo ss -tuln
```

Cela vous permettra de vérifier si vos services Docker écoutent bien sur les bons ports. Par exemple, vous devez voir des lignes comme :

```
LISTEN  0  128  0.0.0.0:5000  ...
LISTEN  0  128  0.0.0.0:8080  ...
```

---

# Vérification des règles de sécurité (exemple Azure)

1. Connectez-vous à [https://portal.azure.com](https://portal.azure.com)
2. Ouvrez la section de votre machine virtuelle.
3. Allez dans l’onglet **Mise en réseau** ou **Network security group** (NSG).
4. Cliquez sur **Ajouter une règle de port entrant**.
5. Créez deux règles :

   * **Nom** : `mlflow-rule` — Port : `5000` — Protocole : `TCP` — Action : `Autoriser`
   * **Nom** : `pgadmin-rule` — Port : `8080` — Protocole : `TCP` — Action : `Autoriser`

> Sans ces règles, les URL http\://\<ip\_publique>:5000 ou http\://\<ip\_publique>:8080 ne seront pas accessibles.




<br/>

# Annexe 3 - est-ce que j'ai besoin d'installer mlops sur la VM ?


Non, **ces commandes ne sont pas nécessaires pour installer ou lancer le projet MLOps basé sur Docker** avec MLflow, PostgreSQL, et pgAdmin.




## ❌ Pourquoi ce script n’est **pas nécessaire** pour ce projet :

Le projet que tu suis est **100 % basé sur Docker**. Cela signifie que :

* **Toutes les dépendances Python sont gérées dans un conteneur Docker** (dans le `Dockerfile`).
* **Tu ne travailles pas avec un environnement virtuel local** (`venv`) sur ta machine.
* **Tu n’as pas besoin d’installer Python 3.9 manuellement**, car Docker télécharge une image Python (`python:3.11-slim`) et utilise un `pip install` isolé dans le conteneur.



##  Cas où **ce script est utile** :

Ce script est utile **seulement si** :

1. Tu veux **installer manuellement Python 3.9 sur ton système Linux local** (hors Docker).
2. Tu veux créer un **environnement virtuel local** (`venv`) avec Python 3.9 pour exécuter un projet **hors conteneur Docker**.
3. Tu ne veux pas utiliser Docker du tout.



##  Contenu du script analysé ligne par ligne :

```bash
rm -rf myenv                        # Supprime un ancien environnement virtuel
sudo apt update                     # Met à jour les paquets
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.9 python3.9-venv python3.9-dev -y  # Installe Python 3.9 et les outils venv/dev
python3.9 --version
python3.9 -m venv myenv            # Crée un environnement virtuel
source myenv/bin/activate          # Active l’environnement virtuel
```


##  Ce que tu dois faire dans ton projet actuel :

Dans le contexte **du projet `mlops-redwine`**, tu dois simplement faire :

```bash
docker-compose up --build
docker-compose run --rm mlflow
```

C’est tout.



