
# 0 - Nouveaux ajouts par rapport au script précédent 💀🚨

Les ajouts dans cette version incluent :

💀🚨 **Chargement du modèle `MLflow` pour faire des prédictions** après avoir été enregistré dans MLflow.

💀🚨 **Calcul des métriques RMSE, MAE et R2** sur le jeu de test pour vérifier les performances du modèle après son chargement.

---

# 1 - Script avec les nouveaux ajouts 🎛️

```python
# Importation des bibliothèques nécessaires
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
from mlflow.models.signature import ModelSignature, infer_signature  # 💀🚨 Pour la signature du modèle
from mlflow.types.schema import Schema, ColSpec  # 💀🚨 Pour les schémas d'entrée et de sortie
import sklearn
import joblib
import cloudpickle

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# get arguments from command
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.4)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.4)
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
    train, test = train_test_split(data)

    data_dir = 'red-wine-data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    data.to_csv(data_dir + '/data.csv')
    train.to_csv(data_dir + '/train.csv')
    test.to_csv(data_dir + '/test.csv')

    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio

    mlflow.set_tracking_uri(uri="")
    print("The set tracking uri is ", mlflow.get_tracking_uri())

    exp = mlflow.set_experiment(experiment_name="experiment_custom_sklearn")
    print("Name: {}".format(exp.name))
    print("Experiment_id: {}".format(exp.experiment_id))
    print("Artifact Location: {}".format(exp.artifact_location))
    print("Tags: {}".format(exp.tags))
    print("Lifecycle_stage: {}".format(exp.lifecycle_stage))
    print("Creation timestamp: {}".format(exp.creation_time))

    mlflow.start_run()
    tags = {
        "engineering": "ML platform",
        "release.candidate": "RC1",
        "release.version": "2.0"
    }
    mlflow.set_tags(tags)

    mlflow.sklearn.autolog(
        log_input_examples=False,
        log_model_signatures=False,
        log_models=False
    )

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)
    predicted_qualities = lr.predict(test_x)
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

    mlflow.log_params({
        "alpha": 0.4,
        "l1_ratio": 0.4
    })

    mlflow.log_metrics({
        "rmse": rmse,
        "r2": r2,
        "mae": mae
    })

    sklearn_model_path = "sklearn_model.pkl"
    joblib.dump(lr, sklearn_model_path)
    artifacts = {
        "sklearn_model": sklearn_model_path,
        "data": data_dir
    }

    # 💀🚨 Création d'un Wrapper `SklearnWrapper` pour le modèle
    class SklearnWrapper(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            self.sklearn_model = joblib.load(context.artifacts["sklearn_model"])

        def predict(self, context, model_input):
            return self.sklearn_model.predict(model_input.values)

    # 💀🚨 Création d’un environnement conda pour MLflow
    conda_env = {
        "channels": ["defaults"],
        "dependencies": [
            "python={}".format(3.10),
            "pip",
            {
                "pip": [
                    "mlflow=={}".format(mlflow.__version__),
                    "scikit-learn=={}".format(sklearn.__version__),
                    "cloudpickle=={}".format(cloudpickle.__version__),
                ],
            },
        ],
        "name": "sklearn_env",
    }

    # 💀🚨 Enregistrement du modèle `pyfunc` dans MLflow
    mlflow.pyfunc.log_model(
        artifact_path="sklear_mlflow_pyfunc",
        python_model=SklearnWrapper(),
        artifacts=artifacts,
        code_path=["main.py"],
        conda_env=conda_env
    )

    # 💀🚨 Chargement du modèle `pyfunc` depuis MLflow pour prédictions
    ld = mlflow.pyfunc.load_model(model_uri="runs:/ee0c9144a0e941168dcdebe82e9cae47/sklear_mlflow_pyfunc")
    predicted_qualities = ld.predict(test_x)
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)
    print("  RMSE_test: %s" % rmse)
    print("  MAE_test: %s" % mae)
    print("  R2_test: %s" % r2)

    artifacts_uri = mlflow.get_artifact_uri()
    print("The artifact path is", artifacts_uri)
    mlflow.end_run()

    run = mlflow.last_active_run()
    print("Active run id is {}".format(run.info.run_id))
    print("Active run name is {}".format(run.info.run_name))
```

---

# 2 - Exécution du Script 🏃‍♂️

Exécutez le script en utilisant la commande suivante :

```bash
python <nom_du_script>.py
```

Ce script :
- 🚀 Entraîne et évalue un modèle ElasticNet, puis enregistre les métriques et les paramètres.
- 🚀 Sauvegarde le modèle scikit-learn avec joblib et enregistre le modèle `pyfunc` dans MLflow avec un Wrapper `SklearnWrapper`.
- 🚀 Charge le modèle depuis MLflow pour effectuer des prédictions sur le jeu de test, puis évalue ces prédictions avec RMSE, MAE, et R2.

---

# 3 - Annexe des Explications 📖

### Explications des Ajouts

1. **Chargement du Modèle pour Prédiction** :
   - Utilise `mlflow.pyfunc.load_model` pour recharger le modèle sauvegardé dans MLflow et faire des prédictions sur un jeu de test.

2. **Calcul des métriques après chargement** :
   - Vérifie les performances du modèle après son chargement en calculant les métriques (RMSE, MAE, R2).

Avec cette version, le script est prêt à entraîner, sauvegarder, charger et tester un modèle de bout en bout dans un pipeline MLflow.
