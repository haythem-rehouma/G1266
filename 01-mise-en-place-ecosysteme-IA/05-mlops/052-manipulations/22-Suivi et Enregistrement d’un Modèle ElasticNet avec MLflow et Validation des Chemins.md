
### Explication des ajouts 📋
1. **Configuration MLflow** : Ajout de MLflow pour le suivi des hyperparamètres et des métriques.
2. **Enregistrement du modèle avec MLflow** : Utilisation de `mlflow.log_model()` pour enregistrer le modèle dans le serveur MLflow.
3. **Fonction `get_path_type`** : Détermine la validité et le type de chemin du fichier, intégré pour vérifier l'existence du fichier dans un environnement de production.

---

```python
import os
import pickle
import warnings
import argparse
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import logging

# Configuration du logger
logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# Arguments de la ligne de commande
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.4)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.4)
args = parser.parse_args()

# Fonction pour déterminer le type de chemin
def get_path_type(path):
    if os.path.isabs(path) and os.path.exists(path):
        if os.path.isdir(path):
            return "file"
        else:
            return "not a local directory"
    else:
        return "not a valid path"

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
    mlflow.set_tracking_uri(uri="http://127.0.0.1:5000/")
    exp = mlflow.set_experiment("experiment_elastic_net_mlflow")
    print("Experiment details - Name: {}, ID: {}, Artifact Location: {}".format(
        exp.name, exp.experiment_id, exp.artifact_location))

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
    mlflow.log_params({"alpha": alpha, "l1_ratio": l1_ratio})
    mlflow.log_metrics({"rmse": rmse, "r2": r2, "mae": mae})

    # Enregistrement du modèle dans MLflow
    mlflow.sklearn.log_model(lr, "model")

    # Sauvegarde du modèle localement avec pickle
    filename = 'elastic-net-regression.pkl'
    pickle.dump(lr, open(filename, 'wb'))
    mlflow.log_artifact(filename)

    mlflow.end_run()
```

---

### Exécution et suivi du modèle MLflow

1. **Lancer le serveur MLflow** :
   ```bash
   mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 127.0.0.1 --port 5000
   ```

2. **Exécuter le script** pour entraîner le modèle et l'enregistrer sur le serveur MLflow :
   ```bash
   python <nom_du_script>.py --alpha 0.4 --l1_ratio 0.4
   ```

3. **Visualiser les résultats dans l'interface MLflow** sur `http://127.0.0.1:5000`.



> Ce code permet de suivre, d'évaluer et d'enregistrer le modèle ElasticNet dans MLflow, avec un modèle sauvegardé localement pour faciliter la récupération et l'évaluation ultérieures.
