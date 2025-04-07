

# Nouveaux ajouts 💥

1. **Ajout de métriques personnalisées avec `make_metric`** 💡 : Utilisation de métriques personnalisées `squared_diff_plus_one` et `sum_on_target_divided_by_two` pour évaluer la prédiction du modèle.
2. **Ajout d'un artefact visuel avec un graphique de dispersion** 📊 : Fonction `prediction_target_scatter` pour créer un graphique comparant les cibles et les prédictions.

---

# Script avec les nouveaux ajouts 🎛️

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
from mlflow.models.signature import ModelSignature, infer_signature
from mlflow.types.schema import Schema, ColSpec
import sklearn
import joblib
import cloudpickle
from mlflow.models import make_metric
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.7)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.7)
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

    exp = mlflow.set_experiment(experiment_name="experiment_model_evaluation")
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

    # Entraînement du modèle
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)
    predicted_qualities = lr.predict(test_x)
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

    mlflow.log_params({
        "alpha": 0.7,
        "l1_ratio": 0.7
    })

    mlflow.log_metrics({
        "rmse": rmse,
        "r2": r2,
        "mae": mae
    })

    # Sauvegarde du modèle
    sklearn_model_path = "sklearn_model.pkl"
    joblib.dump(lr, sklearn_model_path)
    artifacts = {
        "sklearn_model": sklearn_model_path,
        "data": data_dir
    }

    class SklearnWrapper(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            self.sklearn_model = joblib.load(context.artifacts["sklearn_model"])

        def predict(self, context, model_input):
            return self.sklearn_model.predict(model_input.values)

    # Environnement Conda
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

    mlflow.pyfunc.log_model(
        artifact_path="sklear_mlflow_pyfunc",
        python_model=SklearnWrapper(),
        artifacts=artifacts,
        code_path=["main.py"],
        conda_env=conda_env
    )

    # 💥 Définition des métriques personnalisées
    def squared_diff_plus_one(eval_df, _builtin_metrics):
        return np.sum(np.abs(eval_df["prediction"] - eval_df["target"] + 1) ** 2)

    def sum_on_target_divided_by_two(_eval_df, builtin_metrics):
        return builtin_metrics["sum_on_target"] / 2

    squared_diff_plus_one_metric = make_metric(
        eval_fn=squared_diff_plus_one,
        greater_is_better=False,
        name="squared diff plus one"
    )

    sum_on_target_divided_by_two_metric = make_metric(
        eval_fn=sum_on_target_divided_by_two,
        greater_is_better=True,
        name="sum on target divided by two"
    )

    # 💥 Création d’un artefact visuel
    def prediction_target_scatter(eval_df, _builtin_metrics, artifacts_dir):
        plt.scatter(eval_df["prediction"], eval_df["target"])
        plt.xlabel("Targets")
        plt.ylabel("Predictions")
        plt.title("Targets vs. Predictions")
        plot_path = os.path.join(artifacts_dir, "example_scatter_plot.png")
        plt.savefig(plot_path)
        return {"example_scatter_plot_artifact": plot_path}

    # 💥 Évaluation du modèle
    artifacts_uri = mlflow.get_artifact_uri("sklear_mlflow_pyfunc")
    mlflow.evaluate(
        artifacts_uri,
        test,
        targets="quality",
        model_type="regressor",
        evaluators=["default"],
        custom_metrics=[
            squared_diff_plus_one_metric,
            sum_on_target_divided_by_two_metric
        ],
        custom_artifacts=[prediction_target_scatter]
    )

    print("The artifact path is", artifacts_uri)
    mlflow.end_run()
    run = mlflow.last_active_run()
    print("Active run id is {}".format(run.info.run_id))
    print("Active run name is {}".format(run.info.run_name))
```

---

# Exécution et Analyse 🏃‍♂️

Pour exécuter ce script, utilisez :

```bash
python <nom_du_script>.py
```

# Explication des Nouveaux Ajouts 🛠️

1. **Métriques Personnalisées** :
   - `squared_diff_plus_one`: Calcule la somme des carrés de la différence entre chaque prédiction et cible, en ajoutant 1 à chaque différence.
   - `sum_on_target_divided_by_two`: Calcule la somme des cibles divisée par 2, en utilisant la métrique intégrée `sum_on_target` comme référence.

2. **Artefact de Visualisation** :
   - `prediction_target_scatter`: Génére un graphique de dispersion des cibles vs prédictions, sauvegardé comme fichier PNG dans les artefacts.

3. **Évaluation du Modèle** :
   - `mlflow.evaluate`: Lance l’évaluation avec les métriques par défaut et les métriques personnalisées, ainsi que l’artefact visuel.

--- 

Ce script est conçu pour une évaluation avancée du modèle, offrant des analyses avec des métriques et visualisations spécifiques.
