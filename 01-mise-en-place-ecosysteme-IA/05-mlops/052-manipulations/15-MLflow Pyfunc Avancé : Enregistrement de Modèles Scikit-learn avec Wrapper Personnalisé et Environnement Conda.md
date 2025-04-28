# Nouveaux ajouts par rapport au script précédent

Les ajouts dans cette version incluent :

- **Création d’un Wrapper `SklearnWrapper`** : Définit une classe Python qui encapsule le modèle scikit-learn pour personnaliser le chargement et la prédiction du modèle.

- **Enregistrement du modèle avec `pyfunc` dans MLflow** : Utilisation de `mlflow.pyfunc.log_model` pour consigner le modèle avec un environnement conda personnalisé, en encapsulant toutes les dépendances nécessaires.

- **Utilisation de joblib pour le modèle scikit-learn** : Le modèle est sauvegardé et rechargé via joblib, permettant un déploiement plus modulaire.

---

# 1 - Script avec les nouveaux ajouts

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
    exp = mlflow.set_experiment(experiment_name="experiment_custom_sklearn")

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

    # Utilisation de joblib pour enregistrer le modèle scikit-learn
    sklearn_model_path = "sklearn_model.pkl"
    joblib.dump(lr, sklearn_model_path)
    
    # Enregistrement des artefacts, dont le modèle scikit-learn sauvegardé
    artifacts = {
        "sklearn_model": sklearn_model_path,
        "data": data_dir
    }

    # Création d'un Wrapper `SklearnWrapper` pour encapsuler le modèle scikit-learn
    class SklearnWrapper(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            self.sklearn_model = joblib.load(context.artifacts["sklearn_model"])

        def predict(self, context, model_input):
            return self.sklearn_model.predict(model_input.values)

    # Définition d'un environnement conda pour le modèle MLflow
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

    # Enregistrement du modèle `pyfunc` dans MLflow
    mlflow.pyfunc.log_model(
        artifact_path="sklear_mlflow_pyfunc",
        python_model=SklearnWrapper(),
        artifacts=artifacts,
        code_path=["main.py"],
        conda_env=conda_env
    )

    mlflow.end_run()
```

---

# 2 - Exécution du Script

Pour exécuter le script, utilisez simplement :

```bash
python <nom_du_script>.py
```

Ce script :
- Entraîne un modèle ElasticNet avec `alpha` et `l1_ratio`.
- Enregistre un modèle `pyfunc` avec un `SklearnWrapper` pour personnaliser le chargement et la prédiction.
- Définit un environnement conda pour MLflow, encapsulant toutes les dépendances nécessaires.

---

# 3 - Explications des Ajouts

1. **Wrapper `SklearnWrapper` pour Modèle Scikit-learn** :
   - Cette classe Python encapsule le modèle scikit-learn, permettant une personnalisation des méthodes `load_context` (chargement) et `predict` (prédiction).
   - Avantage : Offre une grande flexibilité pour intégrer des modèles scikit-learn dans MLflow, avec des prétraitements ou post-traitements personnalisés.

2. **Enregistrement du Modèle avec `mlflow.pyfunc.log_model`** :
   - Enregistre le modèle dans MLflow avec un environnement conda personnalisé et des exemples de code.
   - Bénéfices : Facilite la reproductibilité et le déploiement sur différentes plateformes avec toutes les dépendances.

3. **Sauvegarde et Chargement du Modèle avec `joblib`** :
   - `joblib` est utilisé pour sauvegarder le modèle scikit-learn.
   - Avantage : Rend le modèle facilement sérialisable, permettant un stockage et un chargement rapides.
