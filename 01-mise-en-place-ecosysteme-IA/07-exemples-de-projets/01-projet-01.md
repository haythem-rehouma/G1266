# Projet 1 MLOps  – Docker + MLflow + PostgreSQL + pgAdmin + Modèle ML

## Objectif :

À la fin de ce tutoriel, tu dois :

* Lancer un environnement complet avec MLflow et pgAdmin
* Enregistrer automatiquement 3 entraînements de modèles avec MLflow
* Comprendre comment exécuter et observer les résultats dans une vraie interface
* Résoudre les erreurs d’installation 


# AVANT DE COMMENCER – EXIGENCES TECHNIQUES

Tu DOIS avoir :

* Docker et Docker Compose installés

> Tape dans ton terminal (PowerShell, Ubuntu ou Terminal Mac) :

```bash
docker --version
docker-compose --version
```

Si ça ne fonctionne pas, **demande de l’aide immédiatement**. Ce projet ne peut pas être lancé sans Docker.

```bash
su
#ou sudo -s
pwd
git clone https://github.com/hrhouma/install-docker.git
cd install-docker/
chmod +x install-docker.sh
./install-docker.sh
#ou sh install-docker.sh
docker version
apt-install docker-compose
docker-compose version
```

# 1️ CRÉATION DU DOSSIER DU PROJET

> Ouvre ton terminal et tape exactement ceci :

```bash
mkdir mlops-redwine
cd mlops-redwine
mkdir data
```



# 2 TÉLÉCHARGEMENT DU DATASET RED WINE

> Toujours dans ton terminal :

```bash
wget -O data/red-wine-quality.csv https://raw.githubusercontent.com/mlflow/mlflow/master/tests/datasets/winequality-red.csv
```



# 3 CRÉATION DES FICHIERS DU PROJET

> Tu vas créer **5 fichiers** obligatoires.



### 3.1 `requirements.txt` (liste des dépendances)

> Crée le fichier avec la commande suivante :

```bash
nano requirements.txt
```

> Colle exactement ceci :

```
pandas
numpy
scikit-learn
mlflow
```

> Enregistre :

* CTRL + O (valide avec Entrée)
* CTRL + X (pour quitter)



### 3.2 `train_model.py` (code d'entraînement ML)

> Crée le fichier :

```bash
nano train_model.py
```

> Colle [le code complet ici](https://chat.openai.com/share/212f8ac5-99a7-4ad0-87a1-b291ed8a1e92) (ou celui de la réponse précédente).
> 💡 **Pas besoin de modifier l’IP**, le script utilisera automatiquement `http://mlflow:5000` (nom du conteneur Docker).

> Enregistre et quitte.



### 3.3 `Dockerfile`

```bash
nano Dockerfile
```

Colle :

```Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "train_model.py"]
```



### 3.4 `pgadmin_config_local.py`

```bash
nano pgadmin_config_local.py
```

Colle :

```python
SESSION_DB_PATH = '/tmp/pgadmin_sessions'
```



### 3.5 `docker-compose.yml`

```bash
nano docker-compose.yml
```

Colle :

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



# 4️ LANCEMENT DU PROJET

> Tu vas maintenant tout démarrer :

```bash
docker-compose up --build
```

Attends jusqu’à ce que tout soit bien démarré. Laisse tourner dans un onglet.



# 5️ OUVERTURE DES INTERFACES

### ➤ MLflow :

[http://localhost:5000](http://localhost:5000)

### ➤ pgAdmin :

[http://localhost:8080](http://localhost:8080)

* Email : `admin@admin.com`
* Mot de passe : `admin`

Dans pgAdmin :

1. Clique **"Add New Server"**
2. Onglet *General* → Nom : `mlflow-db`
3. Onglet *Connection* →

   * Host: `postgres`
   * Username: `mlflow`
   * Password: `mlflow`
   * Save



# 6️ LANCEMENT DU SCRIPT D’ENTRAÎNEMENT

> Dans un **nouveau terminal**, tape :

```bash
docker-compose run --rm mlflow
```

Tu verras les résultats des 3 exécutions.
**Va dans MLflow** : tu verras les 3 *runs* loggués avec les métriques.


# 7️ (OPTIONNEL) CORRIGER L’ERREUR `pgadmin/sessions`

Si tu vois cette erreur dans les logs de pgAdmin :

```
[Errno 13] Permission denied: '/var/lib/pgadmin/sessions'
```

> Tu dois entrer dans le serveur et corriger les permissions.

### Étapes **exhaustives** :

```bash
# 1. Entrer dans le conteneur pgAdmin
docker exec -it $(docker ps -qf "ancestor=dpage/pgadmin4") bash

# 2. Passer root si nécessaire
apt update && apt install sudo -y
sudo -s

# 3. Créer le bon dossier
mkdir -p /var/lib/pgadmin/sessions
chown -R pgadmin:pgadmin /var/lib/pgadmin/sessions
chmod 700 /var/lib/pgadmin/sessions

# 4. Quitter
exit
exit
```

Redémarre ensuite :

```bash
docker-compose restart pgadmin
```



# TU AS RÉUSSI SI...

* MLflow est accessible et montre 3 runs ✔️
* pgAdmin fonctionne et affiche `mlflow_db` ✔️
* Aucune erreur rouge n’apparaît dans les logs ✔️
* Tu as bien compris où est stocké chaque modèle et métrique ✔️

