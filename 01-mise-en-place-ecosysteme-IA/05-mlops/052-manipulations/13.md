# Nouveaux ajouts par rapport au script précédent

Dans cette version, nous avons ajouté :
  
- **Signature du modèle avec `infer_signature`** : Automatiquement déduit la signature en utilisant les données d'entrée `test_x` et les prédictions `predicted_qualities`.

- **Création d'un `input_example` basé sur `test_x`** : Un exemple d'entrée structuré est fourni pour aider les utilisateurs à comprendre la structure des données d'entrée.

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

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# get arguments from command
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
    
    # Division des données en ensembles d'entraînement et de test (0.75, 0.25)
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
    print("The set tracking uri is ", mlflow.get_tracking_uri())

    exp = mlflow.set_experiment(experiment_name="experiment_signature")
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

    # Utilisation de `infer_signature` pour générer la signature du modèle
    signature = infer_signature(test_x, predicted_qualities)

    # Création d'un exemple d'entrée basé sur `test_x`
    input_example = {
        "columns": np.array(test_x.columns),
        "data": np.array(test_x.values)
    }

    mlflow.log_artifact("red-wine-quality.csv")
    # Enregistrement du modèle avec signature et exemple d'entrée
    mlflow.sklearn.log_model(lr, "model", signature=signature, input_example=input_example)
    
    artifacts_uri = mlflow.get_artifact_uri()
    print("The artifact path is", artifacts_uri)
    mlflow.end_run()

    run = mlflow.last_active_run()
    print("Active run id is {}".format(run.info.run_id))
    print("Active run name is {}".format(run.info.run_name))
```

---

# 2 - Exécution du Script

Pour exécuter le script, utilisez simplement :

```bash
python <nom_du_script>.py
```

Ce script :

- Entraîne un modèle ElasticNet avec `alpha` et `l1_ratio`.
- Enregistre les métriques de performance.
- Génère et enregistre la signature et l'exemple d'entrée du modèle, facilitant son utilisation dans MLflow.

---

# 3 - Annexe des Explications

### Explications des Ajouts :

1. **Signature Automatique avec `infer_signature`** : 
   - Utilise les données `test_x` et les prédictions pour déduire les types d'entrée et de sortie.
   - **Avantage** : Rend la documentation des entrées/sorties du modèle automatique et fiable.

2. **Exemple d'Entrée (`input_example`) basé sur `test_x`** : 
   - Structure les valeurs d'exemple avec les colonnes de `test_x`.
   - **Avantage** : Fournit des données claires sur le format attendu en entrée.

3. **Enregistrement avec Signature et Exemple** :
   - **Commandes** : `mlflow.sklearn.log_model()` enregistre la signature et l'exemple d'entrée.
   - **Bénéfices** : Offre une meilleure traçabilité et documentation dans l'interface MLflow.
