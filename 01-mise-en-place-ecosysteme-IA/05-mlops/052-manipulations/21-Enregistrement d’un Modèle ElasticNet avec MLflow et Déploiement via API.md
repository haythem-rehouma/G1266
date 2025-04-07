

# Explication des ajouts 📋
1. **Enregistrement du modèle** : Utilisation de `registered_model_name` pour inscrire le modèle ElasticNet dans MLflow, prêt à être déployé.
2. **API MLflow** : Configuration de l'URI de suivi pour permettre l'interaction avec un serveur MLflow externe.

---

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
from pathlib import Path
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

    # Configuration de l'URI de suivi MLflow
    mlflow.set_tracking_uri(uri="http://127.0.0.1:5000/")
    print("The set tracking URI is", mlflow.get_tracking_uri())

    # Création de l'expérience
    exp = mlflow.set_experiment(experiment_name="experiment_register_model_api")
    print("Experiment details - Name: {}, ID: {}, Artifact Location: {}".format(
        exp.name, exp.experiment_id, exp.artifact_location))

    # Démarrage de la session MLflow
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
    print("ElasticNet model (alpha={:f}, l1_ratio={:f}): RMSE: {}, MAE: {}, R2: {}".format(alpha, l1_ratio, rmse, mae, r2))

    # Enregistrement des hyperparamètres et des métriques dans MLflow
    mlflow.log_params({
        "alpha": alpha,
        "l1_ratio": l1_ratio
    })
    mlflow.log_metrics({
        "rmse": rmse,
        "r2": r2,
        "mae": mae
    })

    # Enregistrement du modèle dans MLflow avec nom d'inscription
    mlflow.sklearn.log_model(lr, "model", registered_model_name='elasticnet-api')
    mlflow.end_run()

    # Récupération et affichage des informations de la dernière exécution
    run = mlflow.last_active_run()
    print("Active run id: {}".format(run.info.run_id))
```

---

# Exécution et publication du modèle 📡
1. **Lancer le serveur MLflow** si nécessaire :
   ```bash
   mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 127.0.0.1 --port 5000
   ```

2. **Exécuter le script** pour entraîner le modèle et l'enregistrer sur le serveur MLflow :
   ```bash
   python <nom_du_script>.py --alpha 0.6 --l1_ratio 0.6
   ```

3. **Vérifier l'inscription du modèle** dans l'interface de MLflow sur `http://127.0.0.1:5000`.

---

Cette version configure le modèle ElasticNet avec MLflow, l’enregistre sous un nom unique (`elasticnet-api`) pour le rendre accessible via l’API de modèle de MLflow. Cela permet de déployer facilement le modèle et de l’utiliser dans un flux de production.
