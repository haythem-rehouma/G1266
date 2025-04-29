# Exécution d'une expérience MLflow avec `log_artifacts`

## Objectif

L'objectif de ce tutoriel est de vous guider dans l'exécution d'une expérience MLflow en utilisant la fonction `log_artifacts` pour enregistrer des artefacts, tels que des fichiers de données, sur une VM Ubuntu 22.04.

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
import os

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
    os.makedirs("data", exist_ok=True)
    data.to_csv("data/red-wine-quality.csv", index=False)
    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)
    train.to_csv("data/train.csv", index=False)
    test.to_csv("data/test.csv", index=False)
    
    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio

    mlflow.set_tracking_uri(uri="http://<IP-de-votre-VM>:5000")

    print("The set tracking URI is ", mlflow.get_tracking_uri())
    exp = mlflow.set_experiment(experiment_name="experiment_4")
    
    print("Name: {}".format(exp.name))
    print("Experiment_id: {}".format(exp.experiment_id))
    print("Artifact Location: {}".format(exp.artifact_location))
    print("Tags: {}".format(exp.tags))
    print("Lifecycle_stage: {}".format(exp.lifecycle_stage))
    print("Creation timestamp: {}".format(exp.creation_time))

    mlflow.start_run()

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)

    predicted_qualities = lr.predict(test_x)

    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

    # Log parameters
    params = {
        "alpha": alpha,
        "l1_ratio": l1_ratio
    }
    mlflow.log_params(params)
    
    # Log metrics
    metrics = {
        "rmse": rmse,
        "r2": r2,
        "mae": mae
    }
    mlflow.log_metrics(metrics)
    
    # Log model
    mlflow.sklearn.log_model(lr, "my_new_model_1")
    
    # Log artifacts
    mlflow.log_artifacts("data/")

    artifacts_uri = mlflow.get_artifact_uri()
    print("The artifact path is", artifacts_uri)

    mlflow.end_run()
    run = mlflow.last_active_run()
    print("Active run id is {}".format(run.info.run_id))
    print("Active run name is {}".format(run.info.run_name))
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

Vous avez maintenant exécuté et suivi une expérience MLflow en utilisant la fonction `log_artifacts` pour enregistrer des artefacts sur une VM Ubuntu 22.04. Vous pouvez explorer davantage les fonctionnalités de MLflow pour améliorer votre flux de travail de machine learning. N'hésitez pas à expérimenter avec différents modèles et paramètres pour optimiser vos résultats.



# Annexe 1 -  C'est quoi un *artifact* en MLflow ?

Un **artifact** est **n'importe quel fichier produit par ton script** que tu veux **sauvegarder** **et retrouver plus tard** dans MLflow.  
👉 Ce sont des *sorties de ton projet* (outputs) que tu veux **garder dans l’historique**.

Un artifact peut être :

| Exemple d’Artifact | Type |
|:-------------------|:-----|
| Un fichier CSV | Tableau de données |
| Un modèle `.pkl`, `.onnx`, `.joblib` | Modèle Machine Learning |
| Une image `.png`, `.jpg` | Visualisation |
| Un fichier texte `.txt`, `.log` | Logs |
| Un graphique de courbes d'apprentissage | Matplotlib, Seaborn plots |
| Un répertoire complet | Dossier contenant plusieurs fichiers |
| Un fichier HTML ou JSON | Résultats, rapports, dashboards |



### Comment voir les artifacts dans ton code ?

Dans ton script tu as cette ligne :
```python
mlflow.log_artifacts("data/")
```
Cela veut dire :

- **Prends tout ce qu’il y a dans le dossier `data/`** (donc : `train.csv`, `test.csv`, `red-wine-quality.csv`).
- **Sauvegarde-le dans MLflow** sous l’expérience du run en cours.

Ces fichiers deviennent donc **des artifacts** du run.



### Exemple concret :

Imaginons ton projet génère ces fichiers :
```
data/train.csv
data/test.csv
model.pkl
courbe_apprentissage.png
```
Si tu fais :
```python
mlflow.log_artifacts("data/")
mlflow.log_artifact("model.pkl")
mlflow.log_artifact("courbe_apprentissage.png")
```
Alors dans MLflow tu verras que ton run a **ces artifacts attachés** :
- Les CSV du dossier `data/`
- Ton modèle enregistré
- Ton image de courbe



### Pourquoi c’est super utile ?

- **Retrouver ce que tu as produit** pour chaque expérience.
- **Partager** les modèles et résultats facilement (par téléchargement ou API).
- **Comparer** visuellement plusieurs runs : qui a produit quel fichier, dans quelles conditions.
- **Rejouer** une expérience facilement : tu as tout stocké (modèle + données).


### Résumé 

| Artifacts sont… | Exemples |
|:---------------|:---------|
| Des fichiers **produits** ou **sauvegardés** pendant un run MLflow | CSV, images, modèles, logs, dossiers entiers |
| Utilisés pour **suivre, réutiliser ou comparer** des expériences | |



# 📍 Dans notre cas précis

Dans ton code actuel :
- Les artifacts sont les 3 CSV (`train.csv`, `test.csv`, `red-wine-quality.csv`) générés.
- Si nous voudrons, nous pouvons aussi logger d'autres artifacts comme :
  - Notre modèle entraîné (`my_new_model_1/` est automatiquement loggué par `mlflow.sklearn.log_model`).
  - Des visualisations que nous pourrons générer (ex: graphiques matplotlib).



<br/>
<br/>

# Annexe 2

### 1. **Exécuter ton script avec des arguments**
Lance ton fichier `train.py` en passant les arguments `--alpha` et `--l1_ratio` que tu veux.

Exemple :  
```bash
python3 train.py --alpha 0.5 --l1_ratio 0.3
```

👉 Cela va :
- entraîner un modèle ElasticNet,
- logger les métriques et paramètres dans MLflow,
- sauver des CSV dans `data/`,
- logger tout dans ton serveur MLflow.

---

### 2. **Vérifier les fichiers créés localement**
Après l'exécution :

```bash
ls data/
```
Tu dois voir :
- `red-wine-quality.csv`
- `train.csv`
- `test.csv`

---

### 3. **Voir les logs de ta console**
Pendant l'exécution, le script affiche :
```bash
The set tracking URI is  http://<IP-de-votre-VM>:5000
Name: experiment_4
Experiment_id: ...
Artifact Location: ...
Tags: ...
Lifecycle_stage: ...
Creation timestamp: ...
Elasticnet model (alpha=0.500000, l1_ratio=0.300000):
  RMSE: ...
  MAE: ...
  R2: ...
The artifact path is mlflow-artifacts:/...
Active run id is ...
Active run name is ...
```
**Tout est imprimé en direct** sur ton terminal.

---

### 4. **Aller voir dans MLflow UI**

MLflow expose une **interface web** sur ta machine :
```bash
http://<IP-de-votre-VM>:5000
```

**Dans ton navigateur :**
- Tu verras **l'expérience** `experiment_4`
- Tu verras **le run** avec :
  - **Parameters** (alpha, l1_ratio)
  - **Metrics** (RMSE, MAE, R²)
  - **Artifacts** (les fichiers CSV, le modèle sauvegardé)

---

### 5. **Commandes avancées (facultatif)**

**Lister les expériences via CLI MLflow** :
```bash
mlflow experiments list
```

**Lister les runs d'une expérience** (par ID par exemple) :
```bash
mlflow runs list --experiment-id <ID>
```

**Télécharger un artefact depuis MLflow** :
```bash
mlflow artifacts download --run-id <RUN_ID> --artifact-path my_new_model_1
```
Ça va télécharger ton modèle entraîné (ElasticNet sauvegardé).

---

#  Résumé 

| Action | Commande rapide |
|:------|:----------------|
| Lancer le script avec alpha/l1 | `python3 train.py --alpha 0.5 --l1_ratio 0.3` |
| Voir les CSV | `ls data/` |
| Ouvrir interface MLflow | Naviguer vers `http://<IP>:5000` |
| Voir les expériences (CLI) | `mlflow experiments list` |
| Voir les runs (CLI) | `mlflow runs list --experiment-id <ID>` |
| Télécharger artefacts | `mlflow artifacts download --run-id <RUN_ID> --artifact-path my_new_model_1` |

