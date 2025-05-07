#  Tutoriel Complet : MLOps avec Docker, MLflow, PostgreSQL et Expériences CLI

##  Objectifs

À la fin de ce projet, vous serez capables de :

* Lancer des **expériences multiples** avec `ElasticNet`, `Ridge` et `Lasso`.
* Passer dynamiquement les **paramètres alpha et l1\_ratio** via la CLI.
* Observer les résultats dans l’interface MLflow.
* Stocker tous les artefacts dans PostgreSQL.
* Utiliser Docker pour tout encapsuler (aucune installation locale de Python requise).


##  Outils

* Docker,
* MLflow,
* PostgreSQL,
* exécutions paramétrées via la ligne de commande,
* **stockage des artefacts dans PostgreSQL**,
* avec une interface graphique sur `localhost:5000`.



##  Étape 1 – Structure des fichiers attendue

```
mlops-redwine/
├── data/
│   └── red-wine-quality.csv
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── train_model.py
```



##  Fichier `Dockerfile`

```Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "train_model.py"]
```



##  Fichier `requirements.txt`

```txt
pandas
numpy
scikit-learn
mlflow
psycopg2-binary
```



##  Fichier `docker-compose.yml`

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
    depends_on:
      - postgres
    ports:
      - "5000:5000"
    command: >
      mlflow server
      --backend-store-uri postgresql://mlflow:mlflow@postgres:5432/mlflow_db
      --default-artifact-root /app/mlruns
      --host 0.0.0.0
    volumes:
      - ./mlruns:/app/mlruns
      - ./data:/app/data

volumes:
  postgres_data:
```



##  Fichier `train_model.py`

```python
import argparse
import pandas as pd
import numpy as np
import warnings
import os
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import ElasticNet, Ridge, Lasso

warnings.filterwarnings("ignore")
np.random.seed(42)

parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, required=True, choices=["elasticnet", "ridge", "lasso"])
parser.add_argument("--alpha", type=float, required=False, default=0.5)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.5)
args = parser.parse_args()

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment(f"mlops_redwine_{args.model}")

data = pd.read_csv("data/red-wine-quality.csv")
X = data.drop("quality", axis=1)
y = data["quality"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

with mlflow.start_run():
    if args.model == "elasticnet":
        model = ElasticNet(alpha=args.alpha, l1_ratio=args.l1_ratio)
        mlflow.log_param("l1_ratio", args.l1_ratio)
    elif args.model == "ridge":
        model = Ridge(alpha=args.alpha)
    elif args.model == "lasso":
        model = Lasso(alpha=args.alpha)

    mlflow.log_param("alpha", args.alpha)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    rmse, mae, r2 = eval_metrics(y_test, predictions)
    mlflow.log_metrics({"rmse": rmse, "mae": mae, "r2": r2})
    mlflow.sklearn.log_model(model, "model")
    print(f"✅ {args.model} | alpha={args.alpha} | RMSE={rmse:.3f}, R2={r2:.3f}")
```


## 🧪 Étape 2 – Lancer les services

```bash
docker-compose up -d --build
```



##  Étape 3 – Lancer les expériences

Voici comment lancer plusieurs runs avec différents paramètres :

```bash
docker-compose run --rm mlflow python train_model.py --model elasticnet --alpha 0.3 --l1_ratio 0.2
docker-compose run --rm mlflow python train_model.py --model elasticnet --alpha 0.6 --l1_ratio 0.7
docker-compose run --rm mlflow python train_model.py --model ridge --alpha 0.5
docker-compose run --rm mlflow python train_model.py --model lasso --alpha 1.0
```

Chaque ligne :

✅ crée un run
✅ enregistre les paramètres `alpha`, `l1_ratio`
✅ sauvegarde les métriques dans PostgreSQL
✅ stocke le modèle dans `/app/mlruns`



##  Étape 4 – Accéder à l’interface

Ouvre :

```
http://localhost:5000
```

Tu verras :

* Plusieurs **expériences** (`mlops_redwine_elasticnet`, etc.)
* Des **runs** avec les bons noms
* Les paramètres et métriques
* Lien vers le **modèle sauvegardé**


##  Résumé 

| Élément                 | Description                                    |
| ----------------------- | ---------------------------------------------- |
| Modèles testés          | ElasticNet, Ridge, Lasso                       |
| Lancement               | `docker-compose run` avec CLI params           |
| Visualisation           | [http://localhost:5000](http://localhost:5000) |
| Base de données backend | PostgreSQL via `docker-compose`                |
| Artifacts               | `/mlruns` monté + DB                           |
| Autonomie               | Aucun besoin de Python local                   |

