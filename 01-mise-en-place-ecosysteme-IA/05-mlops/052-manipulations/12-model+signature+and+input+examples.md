# Nouveaux ajouts par rapport au script précédent

Dans cette version, nous avons introduit les concepts de signature de modèle et d’exemple d’entrée pour MLflow. Ces fonctionnalités permettent de spécifier la structure des entrées et sorties d’un modèle, ainsi que de fournir un exemple d’entrée pour aider les utilisateurs à comprendre les types de données attendus par le modèle.

**Importation des modules `ModelSignature` et `Schema`** : Nécessaire pour définir la signature du modèle, indiquant les types de données en entrée et en sortie.

**Création d'un `input_example`** : Un exemple d’entrée réel est fourni, montrant les valeurs typiques pour chaque caractéristique d'entrée, ce qui est utile pour la documentation et le déploiement.

**Ajout de la signature et de l’exemple d’entrée à `mlflow.sklearn.log_model()`** : La signature et l'exemple sont spécifiés lors de l'enregistrement du modèle pour que MLflow puisse générer une documentation plus claire.

---

# 1 - Script avec les nouveaux ajouts

Ce script inclut les ajouts en **highlight** dans les commentaires.

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
from mlflow.models.signature import ModelSignature, infer_signature
from mlflow.types.schema import Schema, ColSpec

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

    data = pd.read_csv("red-wine-quality.csv")
    data.to_csv("data/red-wine-quality.csv", index=False)

    train, test = train_test_split(data)
    train.to_csv("data/train.csv")
    test.to_csv("data/test.csv")

    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio

    mlflow.set_tracking_uri(uri="")
    exp = mlflow.set_experiment(experiment_name="experiment_signature")

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

    input_data = [
        {"name": "fixed acidity", "type": "double"},
        {"name": "volatile acidity", "type": "double"},
        {"name": "citric acid", "type": "double"},
        {"name": "residual sugar", "type": "double"},
        {"name": "chlorides", "type": "double"},
        {"name": "free sulfur dioxide", "type": "double"},
        {"name": "total sulfur dioxide", "type": "double"},
        {"name": "density", "type": "double"},
        {"name": "pH", "type": "double"},
        {"name": "sulphates", "type": "double"},
        {"name": "alcohol", "type": "double"},
        {"name": "quality", "type": "double"}
    ]
    output_data = [{'type': 'long'}]

    input_schema = Schema([ColSpec(col["type"], col['name']) for col in input_data])
    output_schema = Schema([ColSpec(col['type']) for col in output_data])
    signature = ModelSignature(inputs=input_schema, outputs=output_schema)

    input_example = {
        "fixed acidity": np.array([7.2, 7.5, 7.0, 6.8, 6.9]),
        "volatile acidity": np.array([0.35, 0.3, 0.28, 0.38, 0.25]),
        "citric acid": np.array([0.45, 0.5, 0.55, 0.4, 0.42]),
        "residual sugar": np.array([8.5, 9.0, 8.2, 7.8, 8.1]),
        "chlorides": np.array([0.045, 0.04, 0.035, 0.05, 0.042]),
        "free sulfur dioxide": np.array([30, 35, 40, 28, 32]),
        "total sulfur dioxide": np.array([120, 125, 130, 115, 110]),
        "density": np.array([0.997, 0.996, 0.995, 0.998, 0.994]),
        "pH": np.array([3.2, 3.1, 3.0, 3.3, 3.2]),
        "sulphates": np.array([0.65, 0.7, 0.68, 0.72, 0.62]),
        "alcohol": np.array([9.2, 9.5, 9.0, 9.8, 9.4]),
        "quality": np.array([6, 7, 6, 8, 7])
    }

    mlflow.log_artifact("red-wine-quality.csv")
    mlflow.sklearn.log_model(lr, "model", signature=signature, input_example=input_example)
    
    mlflow.end_run()

    run = mlflow.last_active_run()
    print("Active run id is {}".format(run.info.run_id))
```

---

# 2 - Exécution du Script

Pour exécuter le script, utilisez simplement la commande suivante dans le terminal :

```bash
python <nom_du_script>.py
```

---

# 3 - Résumé des Ajouts

- Signature de modèle (`ModelSignature`) pour définir les types de données d'entrée et de sortie.
- Exemple d'entrée (`input_example`) pour illustrer les types de données attendus par le modèle.
- Enregistrement de la signature et de l'exemple avec `mlflow.sklearn.log_model()`.

