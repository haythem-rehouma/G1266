# GUIDE 

- MLOps complet : Docker + MLflow + PostgreSQL + pgAdmin + Portainer + FastAPI + Streamlit + CI/CD GitHub Actions + Docker Hub + déploiement automatisé sur VM Azure


## TABLE DES MATIÈRES

1. Pré‑requis généraux
2. Installation (éventuelle) de Docker & Docker Compose
3. Création et organisation du dépôt local
4. Téléchargement du dataset
5. Contenu exhaustif des fichiers source
6. Construction et démarrage des conteneurs (4 puis 6 services)
7. Lancement de runs MLflow paramétrés
8. Accès aux interfaces web (MLflow, pgAdmin, Portainer, FastAPI, Streamlit)
9. Ouverture des ports dans le NSG Azure
10. Mise en place des dépôts Docker Hub
11. Configuration des secrets GitHub
12. Pipeline GitHub Actions `.github/workflows/ci-cd.yml`
13. Premier push / première exécution CI/CD
14. Vérifications post‑déploiement
15. Commandes de maintenance

---

## 1. PRÉ‑REQUIS GÉNÉRAUX

* VM Ubuntu 22.04 (Azure, AWS ou tout autre fournisseur) avec une **IP publique fixe**.
* Accès SSH via clé privée (`key.pem`).
* Ports à autoriser dans le pare‑feu cloud : 5000 (MLflow), 8080 (pgAdmin), 9000 (Portainer), 8000 (FastAPI), 8501 (Streamlit).

---

## 2. INSTALLATION DE DOCKER (SI NÉCESSAIRE)

```bash
docker --version
docker-compose --version
```

Si l’une des deux commandes renvoie « command not found » :

```bash
sudo -s
git clone https://github.com/hrhouma/install-docker.git
cd install-docker
chmod +x install-docker.sh
./install-docker.sh
cd ..
exit
```

---

## 3. CRÉATION DU DÉPÔT LOCAL

Connexion :

```bash
ssh -i key.pem azureuser@IP_PUBLIQUE
sudo -s                                   # on reste root jusqu’à la fin
cd /home/azureuser
apt update && apt install -y git tree
mkdir mlops-redwine
cd mlops-redwine
```

Arborescence initiale :

```bash
mkdir data mlruns
touch Dockerfile requirements.txt train_model.py docker-compose.yml
tree
```

Doit afficher :

```
.
├── data
├── mlruns
├── Dockerfile
├── requirements.txt
├── train_model.py
└── docker-compose.yml
```

---

## 4. TÉLÉCHARGEMENT DU DATASET

```bash
cd data
wget -O red-wine-quality.csv https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv
ls -lh red-wine-quality.csv    # ~82 Kio
cd ..
```

---

## 5. CONTENU DES FICHIERS

### 5.1 `requirements.txt`

```
pandas
numpy
scikit-learn
mlflow
psycopg2-binary
fastapi
uvicorn[standard]
streamlit
```

### 5.2 `Dockerfile` (image de base MLflow + script d’entraînement)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["bash"]
```

### 5.3 `train_model.py` (script paramétrable)

```python
import argparse, os, sys, mlflow, mlflow.sklearn
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet, Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

parser = argparse.ArgumentParser()
parser.add_argument("--model",    required=True, choices=["elasticnet", "ridge", "lasso"])
parser.add_argument("--alpha",    type=float, default=0.5)
parser.add_argument("--l1_ratio", type=float, default=0.5)
args = parser.parse_args()

tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
mlflow.set_tracking_uri(tracking_uri)
mlflow.set_experiment(f"mlops_redwine_{args.model}")

csv_path = "data/red-wine-quality.csv"
if not os.path.exists(csv_path):
    sys.exit(f"{csv_path} introuvable")
df = pd.read_csv(csv_path)

X = df.drop("quality", axis=1)
y = df["quality"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

def compute_metrics(y_true, y_pred):
    return dict(
        rmse=np.sqrt(mean_squared_error(y_true, y_pred)),
        mae =mean_absolute_error(y_true, y_pred),
        r2  =r2_score(y_true, y_pred)
    )

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

    for k, v in compute_metrics(y_test, preds).items():
        mlflow.log_metric(k, float(v))

    mlflow.sklearn.log_model(model, "model")
    print(f"OK {args.model} alpha={args.alpha}")
```

### 5.4 `api_fastapi.py`

```python
import mlflow
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Wine(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

def load_latest():
    client = mlflow.tracking.MlflowClient("http://mlflow:5000")
    exp = client.get_experiment_by_name("mlops_redwine_elasticnet")
    run = client.search_runs(exp.experiment_id, max_results=1,
                             order_by=["attributes.start_time DESC"])[0]
    return mlflow.sklearn.load_model(run.info.artifact_uri + "/model")

model = None
@app.on_event("startup")
def _load():
    global model
    model = load_latest()

@app.post("/predict")
def predict(wine: Wine):
    x = [[getattr(wine, f) for f in wine.__fields__]]
    y = model.predict(x)[0]
    return {"quality": float(y)}
```

### 5.5 `app_streamlit.py`

```python
import streamlit as st, requests, json

st.title("Prédiction de la qualité du vin rouge")

API_URL = st.sidebar.text_input("URL FastAPI", "http://fastapi:8000/predict")

default = {
 "fixed_acidity":7.4, "volatile_acidity":0.7, "citric_acid":0.0,
 "residual_sugar":1.9, "chlorides":0.076, "free_sulfur_dioxide":11.0,
 "total_sulfur_dioxide":34.0, "density":0.9978, "pH":3.51,
 "sulphates":0.56, "alcohol":9.4
}

values = {}
st.sidebar.header("Variables d'entrée")
for k, v in default.items():
    values[k] = st.sidebar.number_input(k, value=float(v))

if st.button("Prédire"):
    r = requests.post(API_URL, data=json.dumps(values))
    st.success(f"Qualité prédite : {r.json()['quality']:.2f}")
```

### 5.6 `Dockerfile.fastapi`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY api_fastapi.py .
CMD ["uvicorn", "api_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 5.7 `Dockerfile.streamlit`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app_streamlit.py .
EXPOSE 8501
CMD ["streamlit", "run", "app_streamlit.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
```

### 5.8 `docker-compose.yml` (version finale – 6 services)

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
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports: ["5432:5432"]

  mlflow:
    image: VOTRE_USER/mlflow:latest
    restart: unless-stopped
    depends_on: [postgres]
    environment:
      MLFLOW_TRACKING_URI: http://mlflow:5000
    command: >
      mlflow server
      --backend-store-uri postgresql://mlflow:mlflow@postgres:5432/mlflow_db
      --default-artifact-root /app/mlruns
      --host 0.0.0.0
    volumes:
      - ./mlruns:/app/mlruns
      - ./data:/app/data
    ports: ["5000:5000"]

  fastapi:
    image: VOTRE_USER/fastapi:latest
    restart: unless-stopped
    depends_on: [mlflow]
    environment:
      MLFLOW_TRACKING_URI: http://mlflow:5000
    ports: ["8000:8000"]

  streamlit:
    image: VOTRE_USER/streamlit:latest
    restart: unless-stopped
    depends_on: [fastapi]
    ports: ["8501:8501"]

  pgadmin:
    image: dpage/pgadmin4
    restart: unless-stopped
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports: ["8080:80"]
    volumes:
      - pgadmin_data:/var/lib/pgadmin

  portainer:
    image: portainer/portainer-ce
    restart: unless-stopped
    command: -H unix:///var/run/docker.sock
    ports: ["9000:9000"]
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data

volumes:
  postgres_data:
  pgadmin_data:
  portainer_data:
```

---

## 6. BUILD ET DÉMARRAGE (PHASE INITIALE 4 SERVICES)

```bash
docker-compose up -d --build          # quatre services
docker ps                              # vérifier
```

Une fois les images publiées (section CI/CD), on remplacera la composition par la version 6 services, puis :

```bash
docker-compose pull
docker-compose up -d
```

---

## 7. LANCEMENT DE RUNS MLFLOW

Syntaxe générique :

```bash
docker-compose run --rm \
  --network mlops-redwine_default \
  -e MLFLOW_TRACKING_URI=http://mlflow:5000 \
  mlflow python train_model.py --model elasticnet --alpha 0.3 --l1_ratio 0.2
```

---

## 8. INTERFACES WEB

| Service   | URL                               | Authentification                                  |
| --------- | --------------------------------- | ------------------------------------------------- |
| MLflow    | `http://IP_PUBLIQUE_VM:5000`      | aucune                                            |
| FastAPI   | `http://IP_PUBLIQUE_VM:8000/docs` | Swagger auto‑généré                               |
| Streamlit | `http://IP_PUBLIQUE_VM:8501`      | aucune                                            |
| pgAdmin   | `http://IP_PUBLIQUE_VM:8080`      | [admin@admin.com](mailto:admin@admin.com) / admin |
| Portainer | `http://IP_PUBLIQUE_VM:9000`      | définir un mot de passe au 1er accès              |

---

## 9. OUVERTURE DES PORTS DANS AZURE

Créer cinq règles TCP entrantes (Priorité libre) : 5000, 8000, 8080, 8501, 9000.

---

## 10. DÉPÔTS DOCKER HUB

Créer sur hub.docker.com :

* `VOTRE_USER/mlflow`
* `VOTRE_USER/fastapi`
* `VOTRE_USER/streamlit`

---

## 11. SECRETS GITHUB

Répertoire GitHub → Settings → Secrets → Actions :

| Nom           | Valeur                                    |
| ------------- | ----------------------------------------- |
| `DH_USERNAME` | votre identifiant Docker Hub              |
| `DH_TOKEN`    | token personnel Docker Hub                |
| `AZURE_HOST`  | IP publique de la VM                      |
| `AZURE_USER`  | azureuser                                 |
| `SSH_KEY`     | contenu intégral de `key.pem` (chmod 600) |

---

## 12. PIPELINE `ci-cd.yml`

Copier le fichier donné dans la section 5.8 (build trois images, push, déploiement SSH).

---

## 13. PREMIER PUSH

```bash
git init
git add .
git commit -m "projet complet mlops"
git remote add origin git@github.com:VOTRE_USER/mlops-redwine.git
git branch -M main
git push -u origin main
```

GitHub > **Actions** : attendre la fin des jobs `build-push` puis `deploy`.

---

## 14. VÉRIFICATIONS POST‑DÉPLOIEMENT

Sur la VM :

```bash
docker ps                             # six conteneurs
```

Depuis votre navigateur :

* Swagger FastAPI → `POST /predict` avec un JSON d’exemple, vérifier la réponse.
* Streamlit → saisir des valeurs, cliquer “Prédire”, vérifier l’affichage.
* Portainer → visualiser ressources, logs.

Dans pgAdmin : tables `runs`, `metrics` se remplissent après chaque appel FastAPI si vous avez lancé des entraînements.

---

## 15. COMMANDES DE MAINTENANCE

```bash
# Mettre à jour manuellement les images et relancer
cd /home/azureuser/mlops-redwine
docker-compose pull
docker-compose up -d

# Sauvegarde de la base PostgreSQL
docker exec -t $(docker ps -qf "ancestor=postgres:14") pg_dump -U mlflow mlflow_db > backup.sql

# Réinitialiser complètement le projet
docker-compose down -v
rm -rf mlruns postgres_data pgadmin_data portainer_data
```



Le projet est désormais entièrement opérationnel : pipeline CI/CD GitHub Actions → Docker Hub → VM Azure, stockage robuste dans PostgreSQL, serveur MLflow, API FastAPI, dashboard Streamlit, et supervision Portainer. 
