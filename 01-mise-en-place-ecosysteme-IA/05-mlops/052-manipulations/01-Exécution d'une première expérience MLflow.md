# Exécution d'une première expérience MLflow

Ce guide vous aidera à exécuter votre première expérience MLflow sur une VM Ubuntu 22.04. Nous utiliserons un modèle de régression ElasticNet pour prédire la qualité du vin.

## 1 - Prérequis

- Avoir suivi le [guide d'installation de MLflow](#installation-de-mlflow-sur-une-vm-ubuntu-2204) sur votre VM.
- Avoir accès à un fichier CSV de qualité du vin rouge (`red-wine-quality.csv`).




## 2 - Objectif du TP : Exécuter et tracer une expérience ML avec MLflow


## 3 - **Objectif pédagogique**

L’objectif principal de ce TP est de :

> **Comprendre le fonctionnement de MLflow en pratique, en exécutant une expérience de machine learning complète avec traçabilité des paramètres, des métriques, et du modèle entraîné.**

À la fin de ce TP, l’apprenant saura :

- Préparer un environnement de travail pour MLflow.
- Exécuter un script d'entraînement de modèle.
- Utiliser MLflow pour tracer automatiquement les paramètres, les métriques et le modèle.
- Visualiser les résultats via l’interface web MLflow.
- Comparer différentes expériences avec des hyperparamètres variés.



## 4 - **Méthodologie / Étapes**

Ce TP suit une démarche pédagogique en 6 étapes :

| Étape | Description | Compétence visée |
|-------|-------------|------------------|
| **1. Préparation** | Créer un environnement de travail propre et structuré. | Organisation de projet ML |
| **2. Ingestion des données** | Télécharger et comprendre un fichier CSV réel. | Lecture de données tabulaires |
| **3. Écriture du modèle** | Implémenter un script Python qui entraîne un modèle de régression (ElasticNet). | Programmation ML avec scikit-learn |
| **4. Paramétrage dynamique** | Ajouter des arguments en ligne de commande (`alpha`, `l1_ratio`). | Reproductibilité et flexibilité |
| **5. Intégration de MLflow** | Tracer les expériences avec MLflow (paramètres, métriques, modèle). | MLOps : traçabilité des runs |
| **6. Visualisation** | Démarrer l’interface web de MLflow et analyser les résultats. | Interprétation de résultats et comparaison |



## 5 - **Compétences techniques visées**

- Utiliser MLflow en mode tracking local.
- Comprendre le lien entre modèle, paramètres, métriques et versioning.
- Créer une interface ligne de commande pour entraîner un modèle avec flexibilité.
- Structurer un projet de machine learning de manière professionnelle.





## 6 - Étapes d'exécution de l'expérience

### 6.1. Préparer l'environnement

Assurez-vous que votre environnement est configuré correctement :

```bash
cd ~
mkdir mlflow-experiment
cd mlflow-experiment
```

### 6.2. Télécharger le fichier de données

Placez votre fichier `red-wine-quality.csv` dans le répertoire `mlflow-experiment`. Vous pouvez télécharger un exemple de [ce lien](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv). ou le répertoire fichier du cours.


### 6.3. Créer le script Python
- # cat > red-wine-quality.csv
- coller le contenu du fichier csv
- faites CTL + C
- # cat red-wine-quality.csv
- Créez un fichier nommé `train.py` et ajoutez le code suivant :

```python
import warnings
import argparse
import logging
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# get arguments from command
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.5)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.5)
args = parser.parse_args()

# evaluation function
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)  # Removed the extra closing parenthesis
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read the wine-quality csv file from local
    data = pd.read_csv("red-wine-quality.csv")
    data.to_csv("red-wine-quality.csv", index=False)

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)

    predicted_qualities = lr.predict(test_x)

    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

```

### 6.4. Exécuter le script

Pour exécuter le script avec les paramètres par défaut (alpha=0.5 et l1_ratio=0.5), utilisez la commande suivante :

```bash
python3 train.py
```

Vous pouvez également spécifier différents paramètres pour `alpha` et `l1_ratio` :

```bash
python3 train.py --alpha 0.1 --l1_ratio 0.1
```

### 6.5. Enregistrement des résultats dans MLflow

Pour enregistrer les résultats de l'expérience dans MLflow, nous devons modifier légèrement le script Python pour inclure MLflow. Ajoutez les lignes suivantes après l'importation des bibliothèques :

```python
import mlflow
import mlflow.sklearn

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

    with mlflow.start_run():
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
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        mlflow.sklearn.log_model(lr, "model")
```

### 6.6. Exécuter l'expérience et visualiser les résultats

Pour exécuter l'expérience :

```bash
python3 train.py --alpha 0.1 --l1_ratio 0.1
```

Ensuite, ouvrez le serveur de suivi MLflow pour visualiser les résultats :

```bash
mlflow ui
```

Accédez à l'interface MLflow dans votre navigateur à l'adresse suivante :

```
http://<IP-de-votre-VM>:5000
```

Remplacez `<IP-de-votre-VM>` par l'adresse IP de votre VM Ubuntu 22.04.

## 7 - Conclusion

Vous avez maintenant exécuté et suivi votre première expérience MLflow sur une VM Ubuntu 22.04. Vous pouvez explorer davantage les fonctionnalités de MLflow pour améliorer votre flux de travail de machine learning. N'hésitez pas à expérimenter avec différents modèles et paramètres pour optimiser vos résultats.


# Exercice : 
- Combinez les deux programmes 1 et 2 pour faire fonctionner l'expérience



# Réponse:

## Téléchargement du fichier .csv

- Allez à Github et choisir le fichier csv (Cliquez sur raw sinon il copiera le html)
- wget https://raw.githubusercontent.com/haythem-rehouma/G1266/refs/heads/main/01-mise-en-place-ecosysteme-IA/05-mlops/050-fichiers/red-wine-quality.csv

```python
nano train.py
```

```python
import mlflow
import mlflow.sklearn
import warnings
import argparse
import logging
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# get arguments from command
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.5)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.5)
args = parser.parse_args()

# evaluation function
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)  # Removed the extra closing parenthesis
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read the wine-quality csv file from local
    data = pd.read_csv("red-wine-quality.csv")
    data.to_csv("red-wine-quality.csv", index=False)

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    exp = mlflow.set_experiment(experiment_name="experience_1")

    with mlflow.start_run(experiment_id=exp.experiment_id):
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
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        mlflow.sklearn.log_model(lr, "model")
```

- python3 train.py --alpha 0.1 --l1_ratio 0.1
- python3 train.py --alpha 0.3 --l1_ratio 0.8

*Cherchez le bouton comparez les expériences dans MLFlow*

<br/>
<br/>

# Annexe 1 : 


- Ce programme guide l'exécution d'une première expérience de machine learning avec MLflow sur une VM Ubuntu 22.04. Il utilise un modèle de régression `ElasticNet` pour prédire la qualité du vin à partir d'un fichier CSV. 

L'objectif est d'apprendre à :
- Structurer un projet ML
- Paramétrer dynamiquement un modèle
- Tracer les paramètres, métriques et modèles avec MLflow
- Visualiser les résultats via l'interface web de MLflow

Le TP suit 6 étapes : préparation de l'environnement, ingestion des données, création du modèle, ajout de paramètres dynamiques, intégration de MLflow, visualisation des résultats.


<br/>
<br/>

# Annexe 2 - Résumé rapide :

- **But** : Entraîner un modèle de régression (`ElasticNet`) pour prédire la qualité du vin à partir d’un fichier CSV.
- **Objectif pédagogique** : Apprendre à utiliser **MLflow** pour suivre :
  - Les **paramètres** (`alpha`, `l1_ratio`)
  - Les **métriques** (RMSE, MAE, R²)
  - Le **modèle entraîné**
- **Technos utilisées** : Python, scikit-learn, MLflow



###  **Ce que l’apprenant fait concrètement :**

1. **Créer un environnement propre** pour l'expérience.
2. **Charger les données** (`red-wine-quality.csv`).
3. **Coder un script Python** d'entraînement avec `ElasticNet`.
4. **Ajouter des paramètres dynamiques** via ligne de commande.
5. **Intégrer MLflow** pour tracer chaque exécution.
6. **Visualiser les résultats** dans l’interface web de MLflow.



###  **Compétences acquises :**

- Lancer un projet ML bien structuré.
- Exécuter des scripts paramétrables.
- Utiliser MLflow pour :
  - le tracking d’expériences,
  - la comparaison de modèles,
  - le versioning de résultats.
- Interpréter les métriques de régression (RMSE, MAE, R²).



# Annexe 3 - Résumé visuel et structuré du script `train.py`

### **Structure du script Python (train.py)**

```
1. Importations
   ├─ Standard : warnings, argparse, logging
   ├─ Data : pandas, numpy
   ├─ Modèle : sklearn.linear_model.ElasticNet
   ├─ Évaluation : sklearn.metrics
   └─ MLflow : mlflow, mlflow.sklearn

2. Configuration
   ├─ Logging
   └─ ArgumentParser (--alpha, --l1_ratio)

3. Fonction utilitaire
   └─ eval_metrics(actual, pred) → RMSE, MAE, R²

4. Main (bloc if __name__ == "__main__")
   ├─ Suppression des warnings
   ├─ Fixation du random seed
   ├─ Chargement du CSV local
   ├─ Split train/test
   ├─ Séparation X (features) / Y (label)
   ├─ Récupération des arguments alpha, l1_ratio

   └─ Bloc MLflow.start_run()
       ├─ Entraînement du modèle ElasticNet
       ├─ Prédictions
       ├─ Évaluation (RMSE, MAE, R²)
       ├─ Affichage des scores
       ├─ Log des paramètres (alpha, l1_ratio)
       ├─ Log des métriques (rmse, mae, r2)
       └─ Log du modèle (mlflow.sklearn.log_model)
```



# Annexe 4 - instructions supplémentaires


*Vous devez  **exécuter la deuxième version du script** : celle **avec l’intégration de MLflow**.*


### Pourquoi ?
Le **premier script** est une version simple, **sans traçabilité avec MLflow** : il entraîne un modèle mais **ne trace rien automatiquement**.

Le **deuxième script** (celui avec `mlflow.start_run()`) permet :
- de **logger les paramètres** (`alpha`, `l1_ratio`)
- de **logger les métriques** (`rmse`, `mae`, `r2`)
- de **sauvegarder le modèle entraîné**
- de **visualiser les résultats** dans l’interface web de MLflow



### Étapes :

1. Crée le fichier `train.py` avec **le code complet incluant MLflow** (la 2e version).
2. Place le fichier `red-wine-quality.csv` dans le bon dossier.
3. Lance une exécution avec des paramètres par défaut ou personnalisés :
   ```bash
   python3 train.py --alpha 0.1 --l1_ratio 0.2
   ```
4. Lance l’interface MLflow :
   ```bash
   mlflow ui
   ```
5. Accède à l’interface via `http://<IP-de-ta-VM>:5000`

