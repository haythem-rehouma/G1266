

### Code 📝

```python
import os
import warnings
import argparse
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn
import logging

# Configurer le niveau de logging
logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# Fonction pour évaluer les métriques
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

# Fonction principale
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha", type=float, required=False, default=0.4)
    parser.add_argument("--l1_ratio", type=float, required=False, default=0.4)
    args = parser.parse_args()

    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Charger les données de qualité du vin
    data = pd.read_csv("red-wine-quality.csv")
    data.to_csv("data/red-wine-quality.csv", index=False)

    # Diviser les données en ensembles d'entraînement et de test (0.75, 0.25)
    train, test = train_test_split(data)

    # La colonne à prédire est "quality" qui est un scalaire de [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio

    # Configurer l'URI de suivi de MLflow
    mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")

    # Créer une nouvelle expérience dans MLflow
    experiment = mlflow.set_experiment(experiment_name="Project exp 1")

    print("Name: {}".format(experiment.name))
    print("Experiment_id: {}".format(experiment.experiment_id))

    # Démarrer une nouvelle exécution dans MLflow
    with mlflow.start_run(experiment_id=experiment.experiment_id):
        run = mlflow.last_active_run()
        print("Active run_id: {}".format(run.info.run_id))
        print("Active run name: {}".format(run.info.run_name))

        # Entraîner le modèle ElasticNet
        lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        # Prédictions et évaluation des métriques
        predicted_qualities = lr.predict(test_x)
        (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

        print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        # Enregistrer les métriques et les paramètres dans MLflow
        mlflow.log_metrics({
            "rmse": rmse,
            "r2": r2,
            "mae": mae
        })

        mlflow.log_params({
            "alpha": alpha,
            "l1 ratio": l1_ratio
        })

        # Enregistrer le modèle dans MLflow
        mlflow.sklearn.log_model(lr, "model")

# Exécuter la fonction principale
if __name__ == "__main__":
    main()
```

---

### Instructions pour l'exécution 📖

1. **Démarrez le serveur MLflow** avec la commande suivante :
   ```bash
   mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 127.0.0.1 --port 5000
   ```

2. **Exécutez le script** pour enregistrer l'expérience et le modèle dans MLflow :
   ```bash
   python <nom_du_script>.py
   ```

3. **Accédez à MLflow** à l'adresse [http://127.0.0.1:5000](http://127.0.0.1:5000) pour visualiser les résultats.



> Ce script enregistre l'expérience dans MLflow avec les paramètres et les métriques. Le modèle est également sauvegardé dans l'interface MLflow pour une réutilisation future.
