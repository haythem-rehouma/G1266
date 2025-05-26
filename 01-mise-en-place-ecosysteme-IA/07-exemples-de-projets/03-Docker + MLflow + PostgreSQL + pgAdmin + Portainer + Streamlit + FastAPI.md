# GUIDE – MLOps **Red Wine Quality**

Docker + MLflow + PostgreSQL + pgAdmin + Portainer + **FastAPI** + **Streamlit**

> **Extension par rapport à la version précédente** :
> – Ajout d’une API REST (FastAPI : port 8000)
> – Ajout d’un tableau de bord interactif (Streamlit : port 8501)
> – Possibilité de lancer – depuis le navigateur – des entraînements MLflow avec hyper‑paramètres choisis à la volée, d’observer les runs en temps réel et de servir les prédictions.


<br/>

# 0. TABLE DES PORTS

| Service    | Port conteneur | Port hôte | Description courte         |
| ---------- | -------------- | --------- | -------------------------- |
| MLflow UI  | 5000           | 5000      | Suivi des expériences      |
| FastAPI    | 8000           | 8000      | API REST (train + predict) |
| Streamlit  | 8501           | 8501      | Dashboard interactif       |
| PostgreSQL | 5432           | 5432      | Base de données MLflow     |
| pgAdmin    | 80             | 8080      | GUI PostgreSQL             |
| Portainer  | 9000           | 9000      | Supervision conteneurs     |

Assurez‑vous d’ouvrir **5000, 8000, 8501, 8080, 9000** (TCP entrants) dans votre pare‑feu / NSG.



<br/>

# 1. FICHIERS À CRÉER / MODIFIER

```
mlops-redwine/
├── Dockerfile
├── requirements.txt
├── train_model.py
├── api_app.py           <-- FastAPI
├── streamlit_app.py     <-- Streamlit
├── docker-compose.yml
├── data/
│   └── red-wine-quality.csv
└── mlruns/
```



### 1.1 `requirements.txt` (complété)

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



### 1.2 `Dockerfile` (un seul conteneur « mlflow » sachant tout faire)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y git \
 && pip install --upgrade pip \
 && pip install -r requirements.txt \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Entrée par défaut : shell
CMD ["bash"]
```



### 1.3 `train_model.py`

*(identique sauf séparateur `sep=';'`) – déjà présenté, donc inchangé.*

---

### 1.4 `api_app.py` — **FastAPI**

```python
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess, uuid, os

app = FastAPI(title="Red‑Wine MLOps API")

class TrainRequest(BaseModel):
    model: str       # elasticnet | ridge | lasso
    alpha: float
    l1_ratio: float | None = None   # ignoré hors ElasticNet

@app.post("/train")
def train(req: TrainRequest):
    """Lance un entraînement MLflow en sous‑processus."""
    run_id = str(uuid.uuid4())[:8]
    cmd = [
        "python", "train_model.py",
        "--model", req.model,
        "--alpha", str(req.alpha)
    ]
    if req.model == "elasticnet":
        cmd += ["--l1_ratio", str(req.l1_ratio or 0.5)]
    # On passe la variable d'env pour que le sous‑processus parle à MLflow
    env = os.environ.copy()
    env["MLFLOW_TRACKING_URI"] = env.get("MLFLOW_TRACKING_URI", "http://mlflow:5000")
    subprocess.Popen(cmd, env=env)
    return {"status": "started", "run_id": run_id, "cmd": " ".join(cmd)}

class PredictRequest(BaseModel):
    alcohol: float
    volatile_acidity: float
    sulphates: float

@app.post("/predict")
def predict(inp: PredictRequest):
    """Exemple minimal de prédiction ‘à la main’. 
       (On chargerait normalement un modèle MLflow.)"""
    # Formule naïve pour démonstration
    score = 3 + 0.3*inp.alcohol - 1.2*inp.volatile_acidity + 0.8*inp.sulphates
    return {"quality_estimate": round(score, 2)}
```



### 1.5 `streamlit_app.py` — **Dashboard**

```python
import streamlit as st
import requests, json, pandas as pd

st.set_page_config(page_title="Red‑Wine Trainer", layout="wide")

st.title("🍷 Red‑Wine Trainer – Interface Streamlit")
st.markdown(
    "Lancez des entraînements MLflow et observez‑les en temps réel dans "
    "[MLflow UI](http://localhost:5000).")

with st.form("train_form"):
    model = st.selectbox("Modèle", ["elasticnet", "ridge", "lasso"])
    alpha = st.slider("alpha", 0.01, 2.0, 0.5, 0.01)
    l1_ratio = st.slider("l1_ratio (ElasticNet)", 0.0, 1.0, 0.5, 0.05)
    submitted = st.form_submit_button("🚀 Lancer l'entraînement")
    if submitted:
        payload = {"model": model, "alpha": alpha, "l1_ratio": l1_ratio}
        resp = requests.post("http://api:8000/train",
                             data=json.dumps(payload),
                             headers={"Content-Type": "application/json"})
        if resp.ok:
            st.success(f"Run démarré : {resp.json()['run_id']}")
        else:
            st.error("Erreur lors de l’appel API")

st.header("Prévision rapide (démonstration)")
col1, col2, col3 = st.columns(3)
with col1: alcohol   = st.number_input("Alcohol",  8.0, 15.0, 10.0, 0.1)
with col2: vola_acid = st.number_input("Volatile acidity", 0.1, 1.5, 0.5, 0.01)
with col3: sulphates = st.number_input("Sulphates", 0.3, 1.8, 0.8, 0.05)

if st.button("🔮 Prédire qualità"):
    payload = {"alcohol": alcohol,
               "volatile_acidity": vola_acid,
               "sulphates": sulphates}
    r = requests.post("http://api:8000/predict",
                      data=json.dumps(payload),
                      headers={"Content-Type": "application/json"})
    st.write(r.json())
```



### 1.6 `docker-compose.yml` (mis à jour)

```yaml
version: "3.8"

services:
  # ---------- PostgreSQL ----------
  postgres:
    image: postgres:14
    restart: unless-stopped
    environment:
      POSTGRES_USER: mlflow
      POSTGRES_PASSWORD: mlflow
      POSTGRES_DB: mlflow_db
    ports: ["5432:5432"]
    volumes: [postgres_data:/var/lib/postgresql/data]

  # ---------- Backend MLflow + code commun ----------
  mlflow:
    build: .
    restart: unless-stopped
    depends_on: [postgres]
    environment:
      MLFLOW_TRACKING_URI: http://mlflow:5000
    command: >
      mlflow server
      --backend-store-uri postgresql://mlflow:mlflow@postgres:5432/mlflow_db
      --default-artifact-root /app/mlruns
      --host 0.0.0.0
    ports: ["5000:5000"]
    volumes:
      - ./mlruns:/app/mlruns
      - ./data:/app/data

  # ---------- FastAPI ----------
  api:
    build: .
    restart: unless-stopped
    depends_on: [mlflow]
    environment:
      MLFLOW_TRACKING_URI: http://mlflow:5000
    command: uvicorn api_app:app --host 0.0.0.0 --port 8000 --reload
    ports: ["8000:8000"]
    volumes:
      - ./data:/app/data          # accès dataset

  # ---------- Streamlit ----------
  streamlit:
    build: .
    restart: unless-stopped
    depends_on: [api]
    environment:
      STREAMLIT_SERVER_PORT: 8501
      MLFLOW_TRACKING_URI: http://mlflow:5000
    command: streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
    ports: ["8501:8501"]
    volumes:
      - ./data:/app/data

  # ---------- pgAdmin ----------
  pgadmin:
    image: dpage/pgadmin4
    restart: unless-stopped
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports: ["8080:80"]
    volumes: [pgadmin_data:/var/lib/pgadmin]

  # ---------- Portainer ----------
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

<br/>

# 2. BUILD & LANCEMENT

```bash
sudo -s
git clone https://github.com/hrhouma/install-docker.git
cd install-docker
chmod +x install-docker.sh
./install-docker.sh           # installe Docker + compose plugin v2
apt install docker-compose
cd /home/azureuser/
git clone https://github.com/haythem-rehouma/projetsmlops-3.git
docker-compose pull
docker-compose build --no-cache mlflow
docker-compose up -d
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

Vous devez voir **6 services** : `postgres`, `mlflow`, `api`, `streamlit`, `pgadmin`, `portainer`.


<br/>

# 3. UTILISATION

| Étape | Action                                                                                                                                                                                                                                              |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Visitez **Streamlit** : `http://<IP_VM>:8501`.<br>Choisissez un modèle, réglez `alpha` et (pour ElasticNet) `l1_ratio`, cliquez **Lancer l'entraînement**.<br>Le run démarre et apparaît instantanément dans **MLflow UI** (`http://<IP_VM>:5000`). |
| 2     | Testez l’API REST :                                                                                                                                                                                                                                 |

*Depuis votre machine locale* :

```bash
curl -X POST http://<IP_VM>:8000/train \
  -H "Content-Type: application/json" \
  -d '{"model":"ridge","alpha":0.4}'
```

*Prédiction rapide* :

```bash
curl -X POST http://<IP_VM>:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"alcohol":11.0,"volatile_acidity":0.6,"sulphates":0.75}'
```

Vous obtenez un JSON avec l’estimation de qualité.

<br/>

# 4. POINTS D’AMÉLIORATION

| Idée                         | Piste de mise en œuvre                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------- |
| Signature MLflow             | Utiliser `mlflow.models.signature.infer_signature` pour logger `input_example` et la `signature`. |
| Prediction via modèle MLflow | Charger le dernier modèle avec `mlflow.pyfunc.load_model` dans `api_app.py`.                      |
| Authentification API         | Ajouter `fastapi.security` + JWT ou clé API simple.                                               |
| Monitoring                   | Activer Prometheus + Grafana via Portainer pour CPU/RAM.                                          |
| Tests unitaires              | Ajouter `pytest` + GitHub Actions CI/CD (build + docker push).                                    |

<br/>

#  5. Notre stack MLOps est prête !

- Page Streamlit conviviale, API REST pour scripts externes, suivi MLflow complet, base PostgreSQL, pgAdmin, Portainer — le tout en **un seul `docker-compose up -d`**.
