# GUIDE EXHAUSTIF – MLOps **Red Wine Quality**

Docker + MLflow + PostgreSQL + pgAdmin + Portainer + CLI


---

## 0. PRÉ‑REQUIS

| Élément        | Détails / Version minimale                                            |
| -------------- | --------------------------------------------------------------------- |
| VM             | Ubuntu 22.04 (Azure, AWS, GCP ou local) – IP publique obligatoire     |
| Ports ouverts  | 5000 (MLflow) · 5432 (PostgreSQL) · 8080 (pgAdmin) · 9000 (Portainer) |
| RAM conseillée | 4 Go (8 Go confortable)                                               |
| Docker Engine  | ≥ 20.10                                                               |
| docker‑compose | ≥ 1.29 (ou plugin v2)                                                 |

### 0.1 Vérifier l’installation Docker / Compose

```bash
docker --version          # doit afficher une version
docker-compose --version  # idem
```

Si l’une renvoie « command not found » :

```bash
sudo -s
git clone https://github.com/hrhouma/install-docker.git
cd install-docker
chmod +x install-docker.sh
./install-docker.sh           # installe Docker + compose plugin v2
exit
```

---

## 1. CONNEXION SSH

```bash
ssh -i key.pem azureuser@IP_PUBLIQUE
```

---

## 2. PRÉPARATION DU PROJET

```bash
sudo -s                               # rester root pour la session
cd /home/azureuser
mkdir -p mlops-redwine
cd mlops-redwine
mkdir data mlruns
touch Dockerfile requirements.txt train_model.py docker-compose.yml
apt update && apt install -y tree
tree -L 1
```

---

## 3. TÉLÉCHARGEMENT DU DATASET

```bash
cd data
wget -O red-wine-quality.csv \
  https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv
ls -lh red-wine-quality.csv           # ~82 Kio
cd ..
```

---

## 4. CONTENU DES FICHIERS

### 4.1 `requirements.txt`

```
pandas
numpy
scikit-learn
mlflow
psycopg2-binary
```

### 4.2 `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["bash"]                     # conteneur démarre sur un shell
```

### 4.3 `train_model.py`

*(notez `sep=';'` pour lire correctement le CSV)*

```python
import argparse, os, sys
import pandas as pd, numpy as np
import mlflow, mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet, Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ---------- 1. CLI ----------
cli = argparse.ArgumentParser()
cli.add_argument("--model",    required=True,
                 choices=["elasticnet", "ridge", "lasso"])
cli.add_argument("--alpha",    type=float, default=0.5)
cli.add_argument("--l1_ratio", type=float, default=0.5)
args = cli.parse_args()

# ---------- 2. MLflow ----------
tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
mlflow.set_tracking_uri(tracking_uri)
mlflow.set_experiment(f"mlops_redwine_{args.model}")

# ---------- 3. Données ----------
csv_path = "data/red-wine-quality.csv"
if not os.path.exists(csv_path):
    sys.exit(f"Fichier introuvable : {csv_path}")
df = pd.read_csv(csv_path, sep=';')        # <‑‑ séparateur correct

X = df.drop("quality", axis=1)
y = df["quality"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

def log_metrics(y_true, y_pred):
    return {
        "rmse": np.sqrt(mean_squared_error(y_true, y_pred)),
        "mae":  mean_absolute_error(y_true, y_pred),
        "r2":   r2_score(y_true, y_pred)
    }

# ---------- 4. Entraînement ----------
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

    for k, v in log_metrics(y_test, preds).items():
        mlflow.log_metric(k, float(v))

    mlflow.sklearn.log_model(model, "model")
    print(f"Terminé : {args.model}  alpha={args.alpha}")
```

### 4.4 `docker-compose.yml`

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

  # ---------- MLflow ----------
  mlflow:
    build: .
    depends_on: [postgres]
    restart: unless-stopped
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

---

## 5. BUILD ET DÉMARRAGE

```bash
git clone https://github.com/haythem-rehouma/projetsmlops-2.git
docker-compose pull                       # images officielles
docker-compose build --no-cache mlflow    # image locale propre
docker-compose up -d                      # 4 services en arrière‑plan
docker ps --format "table {{.Names}}\t{{.Status}}"   # tout doit être Up
```

---

## 6. PREMIER ENTRAÎNEMENT

### 6.1 Utilisation du conteneur en cours

```bash
docker-compose exec mlflow \
  python train_model.py --model elasticnet --alpha 0.3 --l1_ratio 0.2
```

### 6.2 Conteneur éphémère (optionnel)

```bash
docker-compose run --rm \
  -e MLFLOW_TRACKING_URI=http://mlflow:5000 \
  mlflow python train_model.py --model ridge --alpha 0.7
```

---

## 7. URL DES INTERFACES

| Service   | URL                   | Identifiants par défaut                    |
| --------- | --------------------- | ------------------------------------------ |
| MLflow    | `http://<IP_VM>:5000` | aucun                                      |
| pgAdmin   | `http://<IP_VM>:8080` | `admin@admin.com` / `admin`                |
| Portainer | `http://<IP_VM>:9000` | définir un mot de passe à la 1ʳᵉ connexion |

*Dans pgAdmin, ajoutez un serveur PostgreSQL : host `postgres`, port `5432`, user `mlflow`, pwd `mlflow`.*

---

## 8. MAINTENANCE

| Action                        | Commande                            |
| ----------------------------- | ----------------------------------- |
| Arrêt propre                  | `docker-compose down`               |
| Réinitialisation complète     | `docker-compose down -v`            |
| Logs continus de MLflow       | `docker-compose logs -f mlflow`     |
| Accès shell conteneur MLflow  | `docker-compose exec mlflow bash`   |
| Nettoyage système (optionnel) | `docker system prune -af --volumes` |

---

## 9. CONTRÔLES FINAUX

* **Dataset** présent : `data/red-wine-quality.csv`
* **Artefacts** écrits dans `mlruns/`
* **pgAdmin** montre : `experiments`, `runs`, `metrics`, etc.
* **MLflow UI** liste les expériences `mlops_redwine_*` avec métriques.
* **Portainer** affiche 4 conteneurs « running ».

> Le projet est maintenant prêt pour vos expériences MLOps.


# Annexe 1 - SÉRIE DE COMMANDES D’ESSAI — MLflow en ligne de commande

> Objectif : lancer rapidement **18 runs** (6 ElasticNet, 6 Ridge, 6 Lasso) pour peupler l’interface MLflow et vérifier l’écriture dans PostgreSQL.
> Chaque bloc peut être copié tel quel. Vous pouvez interrompre à tout moment : chaque commande est indépendante.

---

### 12.1 ElasticNet – balayage α / l1\_ratio

```bash
# α fixes (0.1 ; 0.5 ; 1.0) – l1_ratio fixes (0.2 ; 0.8)

docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
  python train_model.py --model elasticnet --alpha 0.1 --l1_ratio 0.2
docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
  python train_model.py --model elasticnet --alpha 0.1 --l1_ratio 0.8
docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
  python train_model.py --model elasticnet --alpha 0.5 --l1_ratio 0.2
docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
  python train_model.py --model elasticnet --alpha 0.5 --l1_ratio 0.8
docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
  python train_model.py --model elasticnet --alpha 1.0 --l1_ratio 0.2
docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
  python train_model.py --model elasticnet --alpha 1.0 --l1_ratio 0.8
```

---

### 12.2 Ridge – balayage α

```bash
# α : 0.1 ; 0.3 ; 0.5 ; 0.7 ; 1.0 ; 2.0

for a in 0.1 0.3 0.5 0.7 1.0 2.0; do
  docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
    python train_model.py --model ridge --alpha "$a"
done
```

---

### 12.3 Lasso – balayage α

```bash
# α : 0.05 ; 0.1 ; 0.3 ; 0.5 ; 0.8 ; 1.5

for a in 0.05 0.1 0.3 0.5 0.8 1.5; do
  docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
    python train_model.py --model lasso --alpha "$a"
done
```

---

### 12.4 Boucle complète (18 runs enchaînés)

Copiez‑collez le bloc suivant dans le terminal :

```bash
# --------- ElasticNet ----------
for a in 0.1 0.5 1.0; do
  for l1 in 0.2 0.8; do
    docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
      python train_model.py --model elasticnet --alpha "$a" --l1_ratio "$l1"
  done
done

# --------- Ridge ----------
for a in 0.1 0.3 0.5 0.7 1.0 2.0; do
  docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
    python train_model.py --model ridge --alpha "$a"
done

# --------- Lasso ----------
for a in 0.05 0.1 0.3 0.5 0.8 1.5; do
  docker-compose run --rm -e MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow \
    python train_model.py --model lasso --alpha "$a"
done
```

Chaque run apparaîtra :

* Dans **MLflow UI** (`http://IP_VM:5000`) → nouvel enregistrement avec hyperparamètres et métriques.
* Dans **PostgreSQL** (`experiments`, `runs`, `metrics` via pgAdmin).

Vous disposez ainsi d’un jeu de résultats suffisant pour comparer algorithmes et hyperparamètres.








<br/>
<br/>

# Annexe 1

```git
root@dockerVM:/home/azureuser/proj2/proj2/projetsmlops-2# docker-compose run --rm \
  -e MLFLOW_TRACKING_URI=http://mlflow:5000 \
  mlflow python train_model.py --model ridge --alpha 0.7
Creating projetsmlops-2_mlflow_run ... done
2025/05/07 20:58:35 INFO mlflow.tracking.fluent: Experiment with name 'mlops_redwine_ridge' does not exist. Creating a new experiment.
2025/05/07 20:58:35 WARNING mlflow.utils.git_utils: Failed to import Git (the Git executable is probably not on your PATH), so Git SHA is not available. Error: Failed to initialize: Bad git executable.
The git executable must be specified in one of the following ways:
    - be included in your $PATH
    - be set via $GIT_PYTHON_GIT_EXECUTABLE
    - explicitly set via git.refresh(<full-path-to-git-executable>)

All git commands will error until this is rectified.

This initial message can be silenced or aggravated in the future by setting the
$GIT_PYTHON_REFRESH environment variable. Use one of the following values:
    - quiet|q|silence|s|silent|none|n|0: for no message or exception
    - warn|w|warning|log|l|1: for a warning message (logging level CRITICAL, displayed by default)
    - error|e|exception|raise|r|2: for a raised exception

Example:
    export GIT_PYTHON_REFRESH=quiet

2025/05/07 20:58:40 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
Terminé : ridge  alpha=0.7

```

- Il n’y a **pas d’erreur bloquante** : le script s’est exécuté jusqu’au bout et a logué le modèle.
- Les lignes que vous voyez sont de simples **warnings**.

| Message                                                                                 | Signification                                                                              | Impact                                                                                        | Comment corriger ou ignorer                                                                                        |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `Experiment with name 'mlops_redwine_ridge' does not exist. Creating a new experiment.` | MLflow crée automatiquement l’expérience car elle n’existait pas encore.                   | Aucun problème.                                                                               | Normal au premier run d’un nouveau modèle.                                                                         |
| `Failed to import Git … Git SHA is not available.`                                      | Le conteneur n’a pas le binaire `git`; MLflow ne peut donc pas enregistrer l’ID du commit. | Aucune incidence sur l’entraînement ou les métriques.                                         | *Optionnel* : ajouter `git` au conteneur :<br>`RUN apt-get update && apt-get install -y git` dans le `Dockerfile`. |
| `Model logged without a signature and input example.`                                   | Vous n’avez pas fourni d’`input_example` à `mlflow.sklearn.log_model`.                     | Le modèle est bien enregistré, mais MLflow ne connaît pas automatiquement le schéma d’entrée. | *Optionnel* : ajouter :<br>`mlflow.sklearn.log_model(model, "model", input_example=X_test.head(1))`                |

### Conclusion

Le run est réussi ; les avertissements sont purement informatifs.
Si vous n’avez pas besoin de la trace Git ni de la signature, vous pouvez les ignorer en toute sécurité.

