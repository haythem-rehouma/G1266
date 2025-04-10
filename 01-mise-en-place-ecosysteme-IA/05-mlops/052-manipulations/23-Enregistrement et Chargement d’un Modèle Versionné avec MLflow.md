


### Code 📝

```python
import warnings
import argparse
import logging
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn
import os

# Configuration du logger
logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# Arguments de la ligne de commande
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.6)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.6)
args = parser.parse_args()

# Fonction d'évaluation
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Lecture des données
    data = pd.read_csv("red-wine-quality.csv")
    data.to_csv("data/red-wine-quality.csv", index=False)
    train, test = train_test_split(data, test_size=0.25)

    # Séparation des caractéristiques et de la variable cible
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio

    # Configuration MLflow
    mlflow.set_tracking_uri("http://127.0.0.1:5000/")
    exp = mlflow.set_experiment("experiment_register_model_api")
    print(f"Experiment details - Name: {exp.name}, ID: {exp.experiment_id}, Artifact Location: {exp.artifact_location}")

    # Début de la session MLflow
    mlflow.start_run()
    tags = {
        "engineering": "ML platform",
        "release.candidate": "RC1",
        "release.version": "2.0"
    }
    mlflow.set_tags(tags)

    # Entraînement du modèle ElasticNet
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)
    predicted_qualities = lr.predict(test_x)

    # Évaluation des performances
    rmse, mae, r2 = eval_metrics(test_y, predicted_qualities)
    print(f"ElasticNet model (alpha={alpha}, l1_ratio={l1_ratio}): RMSE: {rmse}, MAE: {mae}, R2: {r2}")

    # Enregistrement des hyperparamètres et des métriques dans MLflow
    mlflow.log_params({"alpha": alpha, "l1_ratio": l1_ratio})
    mlflow.log_metrics({"rmse": rmse, "r2": r2, "mae": mae})

    # Enregistrement du modèle dans MLflow et enregistrement dans le modèle MLflow
    mlflow.sklearn.log_model(lr, "model")
    run = mlflow.active_run()
    mlflow.register_model(model_uri=f"runs:/{run.info.run_id}/model", name="elastic-api-2")

    # Chargement et évaluation du modèle enregistré
    ld = mlflow.pyfunc.load_model(model_uri="models:/elastic-api-2/1")
    predicted_qualities = ld.predict(test_x)
    rmse, mae, r2 = eval_metrics(test_y, predicted_qualities)
    print(f"Registered Model Evaluation - RMSE_test: {rmse}, MAE_test: {mae}, R2_test: {r2}")

    # Fin de la session MLflow
    mlflow.end_run()
```

---

### Instructions d'utilisation 📖

1. **Lancer le serveur MLflow** :
   ```bash
   mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 127.0.0.1 --port 5000
   ```

2. **Exécuter le script** pour entraîner et enregistrer le modèle :
   ```bash
   python <nom_du_script>.py --alpha 0.6 --l1_ratio 0.6
   ```

3. **Visualiser dans MLflow** sur `http://127.0.0.1:5000`.



> Ce code permet d'entraîner le modèle, d'enregistrer les paramètres et les métriques, et de sauvegarder le modèle pour un chargement et une évaluation ultérieurs dans un environnement de production.
