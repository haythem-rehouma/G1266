# GUIDE DÉTAILLÉ – MLOps avec Docker + MLflow + PostgreSQL + pgAdmin + Portainer

Document pensé pour des étudiants qui découvrent Linux et la ligne de commande.
Chaque bloc “bash” doit être tapé exactement, sans supprimer ni ajouter d’options.



## 0. PRÉ‑REQUIS

* VM Ubuntu 22.04 (Azure, AWS, autre) disposant d’une IP publique.
* Ports 5000, 8080, 9000 ouverts dans le pare‑feu cloud (NSG Azure ou Security Group AWS).

### 0.1 Vérifier que Docker et Docker Compose sont installés

```bash
docker --version
docker-compose --version
```

Si l’une des deux lignes renvoie une erreur « command not found », installer :

```bash
sudo -s              # on passe root
git clone https://github.com/hrhouma/install-docker.git
cd install-docker
chmod +x install-docker.sh
./install-docker.sh  # installe docker + compose v2
exit                 # on sort du dépôt
```



## 1. CONNEXION À LA VM

```bash
ssh -i key.pem azureuser@IP_PUBLIQUE
```

* `key.pem` : chemin vers votre clé privée.
* `IP_PUBLIQUE` : adresse publique de la VM.

---

## 2. DOSSIER DE TRAVAIL

```bash
sudo -s                             # reste root pour éviter les sudo
cd /home/azureuser
mkdir mlops-redwine
cd mlops-redwine
pwd                                  # doit afficher /home/azureuser/mlops-redwine
```



## 3. ARBORESCENCE INITIALE

```bash
mkdir data          # jeu de données
mkdir mlruns        # artefacts MLflow
touch Dockerfile
touch requirements.txt
touch train_model.py
touch docker-compose.yml
apt update && apt install -y tree
tree
```

Affichage attendu :

```
.
├── data
├── mlruns
├── Dockerfile
├── requirements.txt
├── train_model.py
└── docker-compose.yml
```



## 4. TÉLÉCHARGER LE DATASET

```bash
cd data
wget -O red-wine-quality.csv https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv
ls -lh red-wine-quality.csv   # ~82K
cd ..
```



## 5. REMPLIR LES FICHIERS

### 5.1 `requirements.txt`

```
pandas
numpy
scikit-learn
mlflow
psycopg2-binary
```

### 5.2 `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["bash"]            # le conteneur démarre sur un shell
```

### 5.3 `train_model.py`

```python
import argparse, os, sys, mlflow, mlflow.sklearn
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet, Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ---------- CLI ----------
parser = argparse.ArgumentParser()
parser.add_argument("--model",    required=True, choices=["elasticnet", "ridge", "lasso"])
parser.add_argument("--alpha",    type=float, default=0.5)
parser.add_argument("--l1_ratio", type=float, default=0.5)  # ignoré par Ridge/Lasso
args = parser.parse_args()

# ---------- MLflow ----------
tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
mlflow.set_tracking_uri(tracking_uri)
mlflow.set_experiment(f"mlops_redwine_{args.model}")

# ---------- Data ----------
csv_path = "data/red-wine-quality.csv"
if not os.path.exists(csv_path):
    sys.exit(f"Fichier introuvable : {csv_path}")
df = pd.read_csv(csv_path)

X = df.drop("quality", axis=1)
y = df["quality"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

def calc_metrics(y_true, y_pred):
    return dict(
        rmse=np.sqrt(mean_squared_error(y_true, y_pred)),
        mae =mean_absolute_error(y_true, y_pred),
        r2  =r2_score(y_true, y_pred)
    )

# ---------- Entraînement ----------
with mlflow.start_run():
    if args.model == "elasticnet":
        model = ElasticNet(alpha=args.alpha, l1_ratio=args.l1_ratio, random_state=42)
        mlflow.log_param("l1_ratio", args.l1_ratio)
    elif args.model == "ridge":
        model = Ridge(alpha=args.alpha, random_state=42)
    else:
        model = Lasso(alpha=args.alpha, random_state=42)

    mlflow.log_param("alpha", args.alpha)

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    for k, v in calc_metrics(y_test, preds).items():
        mlflow.log_metric(k, float(v))

    mlflow.sklearn.log_model(model, "model")
    print(f"Terminé : {args.model}  alpha={args.alpha}")
```

### 5.4 `docker-compose.yml`

```yaml
version: "3.8"

services:
  postgres:
    image: postgres:14
    restart: unless-stopped
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
    restart: unless-stopped
    depends_on:
      - postgres
    environment:
      MLFLOW_TRACKING_URI: http://mlflow:5000
    command: >
      mlflow server
      --backend-store-uri postgresql://mlflow:mlflow@postgres:5432/mlflow_db
      --default-artifact-root /app/mlruns
      --host 0.0.0.0
    ports:
      - "5000:5000"
    volumes:
      - ./mlruns:/app/mlruns
      - ./data:/app/data

  pgadmin:
    image: dpage/pgadmin4
    restart: unless-stopped
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "8080:80"
    volumes:
      - pgadmin_data:/var/lib/pgadmin

  portainer:
    image: portainer/portainer-ce
    restart: unless-stopped
    command: -H unix:///var/run/docker.sock
    ports:
      - "9000:9000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data

volumes:
  postgres_data:
  pgadmin_data:
  portainer_data:
```



## 6. BUILD ET DÉMARRAGE

```bash
docker-compose up -d --build
docker ps        # vérifier les 4 conteneurs
```



## 7. LANCER DES RUNS PARAMÉTRÉS

Toujours ajouter `--network` et la variable d’environnement.

### 7.1 Première exécution (ElasticNet)

```bash
docker-compose run --rm \
  --network mlops-redwine_default \
  -e MLFLOW_TRACKING_URI=http://mlflow:5000 \
  mlflow python train_model.py --model elasticnet --alpha 0.3 --l1_ratio 0.2
```

### 7.2 Script de tests rapides

```bash
# ElasticNet
docker-compose run --rm --network mlops-redwine_default -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow python train_model.py --model elasticnet --alpha 0.2 --l1_ratio 0.2
docker-compose run --rm --network mlops-redwine_default -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow python train_model.py --model elasticnet --alpha 1.0 --l1_ratio 0.8
# Ridge
docker-compose run --rm --network mlops-redwine_default -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow python train_model.py --model ridge --alpha 0.5
# Lasso
docker-compose run --rm --network mlops-redwine_default -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow python train_model.py --model lasso --alpha 0.7
```



## 8. ACCÈS AUX INTERFACES WEB

| Service   | URL                          | Identifiants initiaux                             |
| --------- | ---------------------------- | ------------------------------------------------- |
| MLflow    | `http://IP_PUBLIQUE_VM:5000` | Aucun                                             |
| pgAdmin   | `http://IP_PUBLIQUE_VM:8080` | Email : `admin@admin.com`, mot de passe : `admin` |
| Portainer | `http://IP_PUBLIQUE_VM:9000` | Définir un mot de passe au premier accès          |

### pgAdmin : ajouter le serveur PostgreSQL

1. `Add New Server`
2. Onglet *General* → Name : `mlflow-db`
3. Onglet *Connection* :

```
Host name/address : postgres
Port              : 5432
Username          : mlflow
Password          : mlflow
```

Valider. Dans `Databases > mlflow_db > Schemas > public`, vous verrez les tables : `experiments`, `runs`, `params`, `metrics`, `tags`, `latest_metrics`.



## 9. OUVERTURE DES PORTS DANS AZURE

| Port | Usage     | Action NSG            |
| ---- | --------- | --------------------- |
| 5000 | MLflow    | Autoriser TCP entrant |
| 8080 | pgAdmin   | Autoriser TCP entrant |
| 9000 | Portainer | Autoriser TCP entrant |

Azure Portal → Ressource VM → Mise en réseau → “Ajouter une règle de port entrant”.



## 10. COMMANDES DE MAINTENANCE

```bash
# Arrêter les conteneurs mais garder volumes
docker-compose down

# Arrêter et supprimer les volumes (réinitialise PostgreSQL)
docker-compose down -v

# Logs live d’un conteneur
docker logs -f nom_conteneur
```



## 11. CONTRÔLES FINAUX

* Dataset présent : `/home/azureuser/mlops-redwine/data/red-wine-quality.csv`
* Artefacts locaux : `/home/azureuser/mlops-redwine/mlruns`
* Dans pgAdmin : tables MLflow remplies, lignes ajoutées après chaque run.
* Portainer affiche les conteneurs et leur consommation de ressources.
* Interface MLflow montre :

  * Expériences : `mlops_redwine_elasticnet`, `mlops_redwine_ridge`, `mlops_redwine_lasso`.
  * Runs avec paramètres et métriques correspondants.

