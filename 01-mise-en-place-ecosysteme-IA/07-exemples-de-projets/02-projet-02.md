# GUIDE – MLOps **Red Wine**

Docker + MLflow + PostgreSQL + pgAdmin + Portainer

> **Public visé** : étudiants débutants sur Linux.
> **Règle d’or** : copier‑coller **chaque** commande exactement, sans supprimer ni ajouter d’options.



# 0 . PRÉ‑REQUIS INDISPENSABLES

| Élément            | Détails / Version minimale                                                    |
| ------------------ | ----------------------------------------------------------------------------- |
| **VM**             | Ubuntu 22.04 (Azure, AWS, GCP ou local) – IP publique obligatoire             |
| **Ports ouverts**  | `5000` (MLflow) • `5432` (PostgreSQL) • `8080` (pgAdmin) • `9000` (Portainer) |
| **RAM conseillée** | 4 Go (8 Go à l’aise)                                                          |
| **Docker Engine**  | ≥ 20.10                                                                       |
| **docker‑compose** | ≥ 1.29                                                                        |

### 0.1 Vérification rapide

```bash
docker --version        # doit afficher la version
docker-compose --version
```

Si l’une des deux commandes renvoie « command not found » :

```bash
sudo -s                     # passer root
git clone https://github.com/hrhouma/install-docker.git
cd install-docker
chmod +x install-docker.sh
./install-docker.sh         # installe Docker + compose v2
exit                        # revenir utilisateur normal
```



# 1 . CONNEXION SSH À LA VM

```bash
ssh -i key.pem azureuser@IP_PUBLIQUE
```

* `key.pem` : chemin vers votre clé privée
* `IP_PUBLIQUE` : adresse publique de la VM



# 2 . CRÉATION DU DOSSIER DE PROJET

```bash
sudo -s                    # rester root ⇒ évite sudo répétés
cd /home/azureuser
mkdir -p mlops-redwine
cd mlops-redwine
pwd                        # → /home/azureuser/mlops-redwine
```



# 3 . STRUCTURE INITIALe

```bash
mkdir data  mlruns
touch Dockerfile requirements.txt train_model.py docker-compose.yml
apt update && apt install -y tree
tree -L 1
```

Sortie attendue :

```
.
├── data/
├── mlruns/
├── Dockerfile
├── requirements.txt
├── train_model.py
└── docker-compose.yml
```



# 4 . DATASET – Red Wine Quality

```bash
cd data
wget -O red-wine-quality.csv \
  https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv
ls -lh red-wine-quality.csv   # ~82 Kio
cd ..
```



# 5 . CONTENU DES FICHIERS

### 5.1 `requirements.txt`

```
pandas
numpy
scikit-learn
mlflow
psycopg2-binary           # driver PostgreSQL
```

### 5.2 `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

CMD ["bash"]    # conteneur démarre sur un shell
```

### 5.3 `train_model.py`

```python
import argparse, os, sys
import mlflow, mlflow.sklearn
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet, Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ---------- 1. CLI ----------
cli = argparse.ArgumentParser()
cli.add_argument("--model",    required=True,
                 choices=["elasticnet", "ridge", "lasso"])
cli.add_argument("--alpha",    type=float, default=0.5)
cli.add_argument("--l1_ratio", type=float, default=0.5)   # ignore par Ridge/Lasso
args = cli.parse_args()

# ---------- 2. MLflow ----------
tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
mlflow.set_tracking_uri(tracking_uri)
mlflow.set_experiment(f"mlops_redwine_{args.model}")

# ---------- 3. Données ----------
csv_path = "data/red-wine-quality.csv"
if not os.path.exists(csv_path):
    sys.exit(f"❌ Fichier introuvable : {csv_path}")
df = pd.read_csv(csv_path)

X = df.drop("quality", axis=1)
y = df["quality"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

def metrics(y_true, y_pred):
    return {
        "rmse": np.sqrt(mean_squared_error(y_true, y_pred)),
        "mae":  mean_absolute_error(y_true, y_pred),
        "r2":   r2_score(y_true, y_pred)
    }

# ---------- 4. Entraînement ----------
with mlflow.start_run():
    if args.model == "elasticnet":
        model = ElasticNet(alpha=args.alpha,
                           l1_ratio=args.l1_ratio,
                           random_state=42)
        mlflow.log_param("l1_ratio", args.l1_ratio)
    elif args.model == "ridge":
        model = Ridge(alpha=args.alpha, random_state=42)
    else:
        model = Lasso(alpha=args.alpha, random_state=42)

    mlflow.log_param("alpha", args.alpha)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    for k, v in metrics(y_test, preds).items():
        mlflow.log_metric(k, float(v))

    mlflow.sklearn.log_model(model, "model")
    print(f"✅ Terminé : {args.model}  alpha={args.alpha}")
```

### 5.4 `docker-compose.yml`

```yaml
version: "3.8"

services:
# --------------------- PostgreSQL ---------------------
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

# --------------------- MLflow -------------------------
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
    ports:
      - "5000:5000"
    volumes:
      - ./mlruns:/app/mlruns
      - ./data:/app/data

# --------------------- pgAdmin ------------------------
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

# --------------------- Portainer ----------------------
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



# 6 . BUILD & LANCEMENT INITIAL

```bash
docker-compose pull              # récupère images officielles
docker-compose build --no-cache mlflow   # construit l’image locale propre
docker-compose up -d             # démarre les 4 services
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

Vous devez voir : `postgres`, `mlflow`, `pgadmin`, `portainer` « Up ».



# 7 . ENTRAÎNER UN MODÈLE

### 7.1 Méthode la plus simple (exec)

```bash
docker-compose exec mlflow \
  python train_model.py --model elasticnet --alpha 0.3 --l1_ratio 0.2
```

### 7.2 Méthode conteneur éphémère (run)

```bash
docker-compose run --rm \
  -e MLFLOW_TRACKING_URI=http://mlflow:5000 \
  mlflow python train_model.py --model ridge --alpha 0.7
```



# 8 . INTERFACES WEB

| Service       | URL                                   | Authentification            |
| ------------- | ------------------------------------- | --------------------------- |
| **MLflow**    | `http://<IP_VM>:5000`                 | Aucune                      |
| **pgAdmin**   | `http://<IP_VM>:8080`                 | `admin@admin.com` / `admin` |
| **Portainer** | `http://<IP_VM>:9000` *premier accès* | Créez un mot de passe admin |

### Ajouter PostgreSQL dans pgAdmin

1. `Add New Server`
2. **General → Name** : `mlflow-db`
3. **Connection** :

```
Host name/address : postgres
Port              : 5432
Username          : mlflow
Password          : mlflow
```



# 9 . OUVERTURE DES PORTS (Azure NSG)

| Port | Rôle                   | Règle NSG (TCP entrant)  |
| ---- | ---------------------- | ------------------------ |
| 5000 | MLflow                 | Autoriser                |
| 8080 | pgAdmin                | Autoriser                |
| 9000 | Portainer              | Autoriser                |
| 5432 | (optionnel) Exposer DB | Laisser fermé (sécurité) |



# 10 . MAINTENANCE & DÉPANNAGE

| Action                             | Commande                            |
| ---------------------------------- | ----------------------------------- |
| Arrêt propre (volumes conservés)   | `docker-compose down`               |
| Réinitialisation complète          | `docker-compose down -v`            |
| Logs d’un service                  | `docker-compose logs -f mlflow`     |
| Accès shell conteneur              | `docker-compose exec mlflow bash`   |
| Nettoyage images/volumes orphelins | `docker system prune -af --volumes` |



# 11 . CONTRÔLES FINAUX

* **Dataset** : `/home/azureuser/mlops-redwine/data/red-wine-quality.csv`
* **Artefacts** : répertoire `mlruns/` plein de sous‑dossiers d’expériences
* **pgAdmin** : tables `experiments`, `runs`, `metrics` peuplées
* **MLflow UI** : expériences `mlops_redwine_*` et runs visibles
* **Portainer** : quatre conteneurs en exécution, stats CPU/RAM OK

- Le projet est maintenant opérationnel, prêt pour vos expériences MLOps !
