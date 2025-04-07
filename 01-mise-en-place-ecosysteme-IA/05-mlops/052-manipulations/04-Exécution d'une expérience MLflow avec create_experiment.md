# Exécution d'une expérience MLflow avec `create_experiment`

## Objectif

L'objectif de ce tutoriel est de vous guider dans l'exécution d'une expérience MLflow en utilisant la fonction `create_experiment` pour créer une nouvelle expérience avec des artefacts et des métadonnées sur une VM Ubuntu 22.04.

## Prérequis

- Avoir suivi le [guide d'installation de MLflow](#installation-de-mlflow-sur-une-vm-ubuntu-2204) sur votre VM.
- Avoir accès à un fichier CSV de qualité du vin rouge (`red-wine-quality.csv`).

## Étapes d'exécution de l'expérience

### 1. Préparer l'environnement

Assurez-vous que votre environnement est configuré correctement :

```bash
cd ~
mkdir mlflow-experiment
cd mlflow-experiment
```

### 2. Télécharger le fichier de données

Placez votre fichier `red-wine-quality.csv` dans le répertoire `mlflow-experiment`. Vous pouvez télécharger un exemple de [ce lien](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv).

### 3. Créer le fichier `requirements.txt`

Créez un fichier nommé `requirements.txt` et ajoutez les dépendances suivantes :

```txt
pandas
numpy
scikit-learn
mlflow
```

### 4. Installer les dépendances

Installez les dépendances listées dans le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

### 5. Créer le script Python

Créez un fichier nommé `train.py` et ajoutez le code suivant :

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

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# get arguments from command
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.7)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.7)
args = parser.parse_args()

# evaluation function
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read the wine-quality csv file from local
    data = pd.read_csv("red-wine-quality.csv")

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio

    mlflow.set_tracking_uri(uri="http://<IP-de-votre-VM>:5000")

    print("The set tracking URI is ", mlflow.get_tracking_uri())
    exp_id = mlflow.create_experiment(
        name="exp_create_exp_artifact",
        tags={"version": "v1", "priority": "p1"},
        artifact_location=Path.cwd().joinpath("myartifacts").as_uri()
    )
    get_exp = mlflow.get_experiment(exp_id)

    print("Name: {}".format(get_exp.name))
    print("Experiment_id: {}".format(get_exp.experiment_id))
    print("Artifact Location: {}".format(get_exp.artifact_location))
    print("Tags: {}".format(get_exp.tags))
    print("Lifecycle_stage: {}".format(get_exp.lifecycle_stage))
    print("Creation timestamp: {}".format(get_exp.creation_time))

    with mlflow.start_run(experiment_id=exp_id):
        lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        predicted_qualities = lr.predict(test_x)

        (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

        print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)
        mlflow.sklearn.log_model(lr, "mymodel")
```

### 6. Exécuter le script

Pour exécuter le script avec les paramètres par défaut (alpha=0.7 et l1_ratio=0.7), utilisez la commande suivante :

```bash
python3 train.py
```

Vous pouvez également spécifier différents paramètres pour `alpha` et `l1_ratio` :

```bash
python3 train.py --alpha 0.1 --l1_ratio 0.1
```

### 7. Exécuter l'expérience et visualiser les résultats

Pour exécuter l'expérience et enregistrer les résultats dans MLflow, lancez le serveur MLflow :

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0
```

Accédez à l'interface MLflow dans votre navigateur à l'adresse suivante :

```
http://<IP-de-votre-VM>:5000
```

Remplacez `<IP-de-votre-VM>` par l'adresse IP de votre VM Ubuntu 22.04.

## Conclusion

Vous avez maintenant exécuté et suivi une expérience MLflow en utilisant la fonction `create_experiment` pour créer une nouvelle expérience avec des artefacts et des métadonnées sur une VM Ubuntu 22.04. Vous pouvez explorer davantage les fonctionnalités de MLflow pour améliorer votre flux de travail de machine learning. N'hésitez pas à expérimenter avec différents modèles et paramètres pour optimiser vos résultats.
