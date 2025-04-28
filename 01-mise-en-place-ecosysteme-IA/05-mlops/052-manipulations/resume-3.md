

| Bloc | Sujet | Fait ? |
|:----:|:-----------------------------|:-------:|
| 0 | Installer MLflow + démarrer serveur  |
| 1 | Première expérience (`set_experiment`, `start_run`)  |
| 2 | Ajouter `requirements.txt` |
| 3 | Utiliser `set_tracking_uri`, `get_tracking_uri`  |
| 4 | Créer une expérience avec `create_experiment`  |
| 5 | Utiliser `active_run`, `last_active_run`  |
| 6 | Logger artefacts avec `log_artifacts`  |
| 7 | Ajouter des tags `set_tags` |
| 8 | Boucles : plusieurs `start_run()` dans le même script  |
| 9 | Gérer plusieurs expériences différentes  |
| 10 | `mlflow.autolog` |
| 11 | Démarrer en production (PostgreSQL + S3)  |
| 12 → 24 | Plus avancé : evaluation, artefacts visuels, promotion de modèle, baselines, metrics customisées  |
| 25 | Promotion automatique (`MlflowClient`, `transition_model_version_stage`) |
| 26 | Récupération automatique de la version | Ne plus fixer `version=1`, détecter dynamiquement |
| 27 | Ajouter un **commentaire automatique** à la version | Avec `set_model_version_tag` |
| 28 | Déploiement local simple (`mlflow models serve`) | Tester ton modèle via une API locale Flask-like |
| 29 | Résumé visuel final du pipeline complet | (le "poster" final pour bien fixer tout) |




# Bloc 0 – Code initial

```python
# 1. Importation des bibliothèques
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

# 2. Chargement des données
data = pd.read_csv("red-wine-quality.csv")

# 3. Séparation en variables explicatives et variable cible
X = data.drop(["quality"], axis=1)
y = data["quality"]

# 4. Division en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 5. Entraînement d'un modèle ElasticNet
model = ElasticNet(alpha=0.5, l1_ratio=0.5)
model.fit(X_train, y_train)

# 6. Prédictions
predictions = model.predict(X_test)

# 7. Affichage simple
print(predictions[:5])
```

---

# Bloc 1 – Ajout 1 : Importer mlflow

**Instruction** :  
Ajoutez juste après les imports standards (**après la ligne 3**).

```python
import mlflow
import mlflow.sklearn
```

**Pourquoi** :  
Préparer l'intégration avec MLflow pour tracer les expériences.

**Code complet après Ajout 1** :

```python
# 1. Importation des bibliothèques
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn

# 2. Chargement des données
data = pd.read_csv("red-wine-quality.csv")

# 3. Séparation en variables explicatives et variable cible
X = data.drop(["quality"], axis=1)
y = data["quality"]

# 4. Division en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 5. Entraînement d'un modèle ElasticNet
model = ElasticNet(alpha=0.5, l1_ratio=0.5)
model.fit(X_train, y_train)

# 6. Prédictions
predictions = model.predict(X_test)

# 7. Affichage simple
print(predictions[:5])
```

---

# Bloc 2 – Ajout 2 : Définir une expérience

**Instruction** :  
Ajoutez juste avant de charger les données (**avant la ligne 8**).

```python
mlflow.set_experiment("exp_wine_quality")
```

**Pourquoi** :  
Définir l'expérience MLflow à laquelle le run sera rattaché.

**Code complet après Ajout 2** :

```python
# 1. Importation des bibliothèques
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn

# 2. Définir l'expérience MLflow
mlflow.set_experiment("exp_wine_quality")

# 3. Chargement des données
data = pd.read_csv("red-wine-quality.csv")

# 4. Séparation en variables explicatives et variable cible
X = data.drop(["quality"], axis=1)
y = data["quality"]

# 5. Division en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 6. Entraînement d'un modèle ElasticNet
model = ElasticNet(alpha=0.5, l1_ratio=0.5)
model.fit(X_train, y_train)

# 7. Prédictions
predictions = model.predict(X_test)

# 8. Affichage simple
print(predictions[:5])
```

---

# Bloc 3 – Ajout 3 : Démarrer un run

**Instruction** :  
Ajoutez juste avant l'entraînement du modèle (**avant la ligne 17**).

```python
mlflow.start_run()
```

**Pourquoi** :  
Démarrer la session de tracking MLflow pour le run courant.

**Code complet après Ajout 3** :

```python
# 1. Importation des bibliothèques
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn

# 2. Définir l'expérience MLflow
mlflow.set_experiment("exp_wine_quality")

# 3. Chargement des données
data = pd.read_csv("red-wine-quality.csv")

# 4. Séparation en variables explicatives et variable cible
X = data.drop(["quality"], axis=1)
y = data["quality"]

# 5. Division en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 6. Démarrer un run MLflow
mlflow.start_run()

# 7. Entraînement d'un modèle ElasticNet
model = ElasticNet(alpha=0.5, l1_ratio=0.5)
model.fit(X_train, y_train)

# 8. Prédictions
predictions = model.predict(X_test)

# 9. Affichage simple
print(predictions[:5])
```













# Bloc 14 – Ajout 14 : Activation de `mlflow.autolog` pour automatiser la capture des paramètres, métriques et modèles

## Objectif de ce bloc

- Éviter d’écrire manuellement `mlflow.log_param`, `mlflow.log_metric`, et `mlflow.log_model`.
- Capturer automatiquement toutes les métriques et artefacts générés par Scikit-learn.

---

## Instructions détaillées

**À faire dans ton script existant :**

### 1. Ajouter `mlflow.sklearn.autolog()` **avant** l'entraînement du modèle

**Juste avant** de créer et d’entraîner ton modèle `ElasticNet`, ajoute la ligne suivante :

```python
mlflow.sklearn.autolog()
```

**Position** :  
Juste avant cette ligne existante :

```python
lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
```

Donc environ **ligne 45-48** dans ton script.

---

### 2. Supprimer les appels manuels à `log_param`, `log_metric`, `log_model`

**Supprime** les lignes suivantes car elles deviendront inutiles :

```python
mlflow.log_params({...})
mlflow.log_metrics({...})
mlflow.sklearn.log_model(...)
```

À partir d’ici, tout sera fait **automatiquement**.

---

## Important

- Le `autolog()` doit être appelé **avant** l'entraînement du modèle.
- Le tracking automatique s'occupe aussi de :
  - Hyperparamètres du modèle
  - Métriques d’évaluation (MSE, RMSE, MAE, etc.)
  - Sérialisation du modèle
  - Signature et input example (si possible)

---

# Résumé Bloc 14

| Étape | Où ? |
|:-----:|:----:|
| Ajouter `mlflow.sklearn.autolog()` | Avant la création du modèle ElasticNet |
| Supprimer tous les appels manuels à `log_params`, `log_metrics`, `log_model` | Après |

---

# Code modifié ajouté à ce stade

```python
# Avant de créer le modèle
mlflow.sklearn.autolog()

# Création et entraînement
lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
lr.fit(train_x, train_y)
predicted_qualities = lr.predict(test_x)

# Plus besoin de log_params, log_metrics, log_model manuellement
signature = infer_signature(test_x, predicted_qualities)
input_example = train_x.iloc[:5]
```












# Bloc 15 – Ajout 15 : Encapsulation du modèle Scikit-learn dans un `PythonModel` personnalisé (wrapper)

## Objectif de ce bloc

- Encapsuler ton modèle Scikit-learn dans une classe `PythonModel`.
- Préparer ton modèle pour un déploiement plus flexible via `mlflow.pyfunc`.
- Pouvoir personnaliser le comportement du modèle à l’inférence si besoin.

---

## Instructions détaillées

**À faire dans ton script existant :**

### 1. Définir une classe `SklearnWrapper`

**Ajoute** cette classe **après** tes imports, mais **avant** le `if __name__ == "__main__":`.

```python
class SklearnWrapper(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        import joblib
        self.model = joblib.load(context.artifacts["sklearn_model"])

    def predict(self, context, model_input):
        return self.model.predict(model_input)
```

**Position** :  
- Immédiatement **après les imports** (`import pandas as pd`, etc.)
- Vers **ligne 20-25** selon ton script.

---

### 2. Sauvegarder ton modèle Scikit-learn avec `joblib`

**Ajoute** avant la fin du `start_run()` :

```python
import joblib

# Sauvegarder le modèle entrainé
model_path = "sklearn_model.pkl"
joblib.dump(lr, model_path)
```

**Position** :  
Juste après `lr.fit(...)` et `predicted_qualities = lr.predict(...)`.

---

### 3. Utiliser `mlflow.pyfunc.log_model` pour enregistrer ton modèle encapsulé

**Ajoute** après la sauvegarde du modèle :

```python
mlflow.pyfunc.log_model(
    artifact_path="sklearn_pyfunc_model",
    python_model=SklearnWrapper(),
    artifacts={"sklearn_model": model_path}
)
```

**Position** :  
À la place où tu faisais `mlflow.sklearn.log_model` (si existant).

---

## Important

- Le fichier `sklearn_model.pkl` sera enregistré en tant qu’artefact de run.
- L’API d'inférence passera par ton `predict()` du `SklearnWrapper`.
- Ce modèle est compatible avec les API Serveur de MLflow (`mlflow models serve`).

---

# Résumé Bloc 15

| Étape | Où ? |
|:-----:|:----:|
| Créer `SklearnWrapper` | Après les imports |
| Sauvegarder `sklearn_model.pkl` | Après entraînement modèle |
| Utiliser `mlflow.pyfunc.log_model` | À la place de `mlflow.sklearn.log_model` |

---

# Code modifié ajouté à ce stade

```python
# Définition du Wrapper
class SklearnWrapper(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        import joblib
        self.model = joblib.load(context.artifacts["sklearn_model"])

    def predict(self, context, model_input):
        return self.model.predict(model_input)

# Entraînement
lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
lr.fit(train_x, train_y)
predicted_qualities = lr.predict(test_x)

# Sauvegarde du modèle Scikit-learn
import joblib
model_path = "sklearn_model.pkl"
joblib.dump(lr, model_path)

# Logging du modèle encapsulé avec Pyfunc
mlflow.pyfunc.log_model(
    artifact_path="sklearn_pyfunc_model",
    python_model=SklearnWrapper(),
    artifacts={"sklearn_model": model_path}
)
```








# Bloc 16 – Ajout 16 : Définir un environnement Conda pour le modèle

---

## Objectif de ce bloc

- Créer **manuellement** un environnement `conda.yaml` **lié au modèle**.
- Permettre que ton modèle soit **exécutable partout** (serveur, production).
- S'assurer que toutes les **dépendances** nécessaires sont présentes.

---

## Instructions détaillées

**À faire dans ton script existant :**

---

### 1. Définir un dictionnaire `conda_env`

**Ajoute** ce bloc **juste avant** `mlflow.pyfunc.log_model(...)`  
(autrement dit, **avant l'enregistrement du modèle** encapsulé par `SklearnWrapper`).

```python
# Définir l'environnement Conda
conda_env = {
    "channels": ["defaults"],
    "dependencies": [
        "python=3.10",
        "pip",
        {
            "pip": [
                f"mlflow=={mlflow.__version__}",
                f"scikit-learn=={sklearn.__version__}",
                f"cloudpickle=={cloudpickle.__version__}"
            ]
        }
    ],
    "name": "sklearn_env"
}
```

---

### 2. Modifier ton appel à `mlflow.pyfunc.log_model`

**Ajoute le paramètre** `conda_env=conda_env` dans l'appel à `log_model`, comme ceci :

```python
mlflow.pyfunc.log_model(
    artifact_path="sklearn_pyfunc_model",
    python_model=SklearnWrapper(),
    artifacts={"sklearn_model": model_path},
    conda_env=conda_env
)
```

---

## Position exacte dans ton script :

| Partie | Emplacement |
|:------:|:------------|
| Définir `conda_env` | Avant `mlflow.pyfunc.log_model(...)` |
| Ajouter `conda_env=conda_env` | Dans l'appel à `log_model` |

---

## Pourquoi on fait ça ?

- Ton modèle sera **portable** avec un fichier `conda.yaml` généré automatiquement.
- Tu pourras **servir** (`mlflow models serve`) ton modèle sur n'importe quelle machine sans surprises.
- Bonne **pratique professionnelle** : toujours versionner l'environnement.

---

# Code modifié après ce Bloc

```python
# Définir l'environnement Conda
conda_env = {
    "channels": ["defaults"],
    "dependencies": [
        "python=3.10",
        "pip",
        {
            "pip": [
                f"mlflow=={mlflow.__version__}",
                f"scikit-learn=={sklearn.__version__}",
                f"cloudpickle=={cloudpickle.__version__}"
            ]
        }
    ],
    "name": "sklearn_env"
}

# Logging du modèle encapsulé avec Pyfunc + Conda env
mlflow.pyfunc.log_model(
    artifact_path="sklearn_pyfunc_model",
    python_model=SklearnWrapper(),
    artifacts={"sklearn_model": model_path},
    conda_env=conda_env
)
```

---

# Résumé du Bloc 16

| Étape | Où l'ajouter | Pourquoi |
|:-----:|:------------:|:--------:|
| Ajouter `conda_env` | Avant `log_model` | Définir un environnement reproductible |
| Ajouter `conda_env=conda_env` | Dans `log_model` | Lier l'environnement au modèle enregistré |














# Bloc 17 – Ajout 17 : Charger le modèle sauvegardé avec `load_model` et prédire

---

## Objectif de ce bloc

- **Vérifier** que le modèle enregistré fonctionne en le **rechargeant** depuis MLflow.
- **Faire une prédiction** sur `test_x` après rechargement.
- **Évaluer** les métriques de prédiction après rechargement (RMSE, MAE, R²).

---

## Instructions détaillées

**À faire dans ton script existant :**

---

### 1. Charger le modèle depuis MLflow

**Ajoute** ce bloc **après** avoir fait `mlflow.end_run()`.

Juste après `mlflow.end_run()`, ajoute :

```python
# Chargement du modèle sauvegardé depuis MLflow
loaded_model = mlflow.pyfunc.load_model(model_uri="runs:/"+run.info.run_id+"/sklearn_pyfunc_model")
```

---

### 2. Utiliser le modèle rechargé pour prédire

Ajoute immédiatement après :

```python
# Faire des prédictions avec le modèle rechargé
reloaded_predictions = loaded_model.predict(test_x)
```

---

### 3. Réévaluer les métriques sur les prédictions rechargées

Ajoute :

```python
# Réévaluer les métriques sur les prédictions reloadées
rmse_reload, mae_reload, r2_reload = eval_metrics(test_y, reloaded_predictions)

print("Évaluation du modèle rechargé depuis MLflow :")
print(f"  RMSE (Reloaded): {rmse_reload}")
print(f"  MAE  (Reloaded): {mae_reload}")
print(f"  R2   (Reloaded): {r2_reload}")
```

---

## Position exacte dans ton script :

| Partie | Emplacement |
|:------:|:------------|
| Charger modèle | Immédiatement après `mlflow.end_run()` |
| Prédire et évaluer | Après le chargement |

---

## Pourquoi on fait ça ?

- **Valider** que ton modèle est bien sauvegardé **correctement** dans MLflow.
- **S’assurer** que les performances sont **identiques** après sauvegarde et rechargement.
- **Préparer** la future utilisation de ton modèle en production.

---

# Code ajouté après ce Bloc

```python
mlflow.end_run()

# Chargement du modèle sauvegardé depuis MLflow
loaded_model = mlflow.pyfunc.load_model(model_uri="runs:/"+run.info.run_id+"/sklearn_pyfunc_model")

# Faire des prédictions avec le modèle rechargé
reloaded_predictions = loaded_model.predict(test_x)

# Réévaluer les métriques sur les prédictions reloadées
rmse_reload, mae_reload, r2_reload = eval_metrics(test_y, reloaded_predictions)

print("Évaluation du modèle rechargé depuis MLflow :")
print(f"  RMSE (Reloaded): {rmse_reload}")
print(f"  MAE  (Reloaded): {mae_reload}")
print(f"  R2   (Reloaded): {r2_reload}")
```

---

# Résumé du Bloc 17

| Étape | Où l'ajouter | Pourquoi |
|:-----:|:------------:|:--------:|
| Charger modèle MLflow | Après `end_run()` | Récupérer modèle |
| Prédire avec modèle chargé | Suite directe | Vérifier la sauvegarde correcte |
| Réévaluer métriques | Suite directe | Confirmer qu'il n'y a pas de perte de performance |















# Bloc 18 – Ajout 18 : Utiliser `mlflow.evaluate()` pour évaluer automatiquement

---

## Objectif de ce bloc

- **Automatiser** l’évaluation du modèle **rechargé**.
- **Générer un rapport complet** de métriques d’évaluation (RMSE, MAE, R²…).
- **Visualiser** facilement les résultats et les comparer plus tard.

---

## Instructions détaillées

**À faire après avoir chargé et utilisé ton modèle.**

---

### 1. Évaluer automatiquement avec `mlflow.evaluate()`

Ajoute **immédiatement après** le bloc précédent (après avoir réévalué manuellement).

```python
import mlflow.models

# Utiliser mlflow.evaluate pour évaluer automatiquement le modèle
eval_result = mlflow.evaluate(
    model=loaded_model,
    data=test_x.assign(quality=test_y),
    targets="quality",
    model_type="regressor",
    evaluators="default"
)

print("Résultats d'évaluation automatique avec mlflow.evaluate :")
print(eval_result.metrics)
```

---

### 2. Points très importants :

- `model=loaded_model` : C’est ton modèle rechargé.
- `data=test_x.assign(quality=test_y)` : On fournit X **et** y sous forme d’un même DataFrame.
- `targets="quality"` : On précise la colonne cible.
- `model_type="regressor"` : C’est un modèle de régression, pas de classification.
- `evaluators="default"` : Utiliser les évaluateurs standards de MLflow.

---

## Position exacte dans ton script

| Partie | Emplacement |
|:------:|:------------|
| Appel à `evaluate` | Juste après avoir réévalué manuellement le modèle |

---

## Pourquoi on fait ça ?

- **Éviter** de coder manuellement le calcul des métriques.
- **Avoir** un **rapport standardisé** compatible avec d’autres outils MLflow.
- **Automatiser** complètement la validation des modèles.

---

# Code ajouté après ce Bloc

```python
import mlflow.models

# Utiliser mlflow.evaluate pour évaluer automatiquement le modèle
eval_result = mlflow.evaluate(
    model=loaded_model,
    data=test_x.assign(quality=test_y),
    targets="quality",
    model_type="regressor",
    evaluators="default"
)

print("Résultats d'évaluation automatique avec mlflow.evaluate :")
print(eval_result.metrics)
```

---

# Résumé du Bloc 18

| Étape | Où l'ajouter | Pourquoi |
|:-----:|:------------:|:--------:|
| Appeler `mlflow.evaluate()` | Après la réévaluation manuelle | Avoir un rapport automatique complet |

---

# **Résumé de ta progression actuelle**

| Bloc | Fonction ajoutée | Pourquoi |
|:----:|:-----------------|:---------|
| 17 | Charger modèle MLflow | Tester le modèle sauvegardé |
| 18 | Évaluer automatiquement | Avoir toutes les métriques standardisées |

---

# Ce que tu as maintenant dans ton projet

- Un modèle qui est :
  - entraîné,
  - loggé dans MLflow,
  - rechargé depuis MLflow,
  - évalué **manuellement**,
  - évalué **automatiquement** par MLflow.

Tu arrives à **un script semi-professionnel**, très proche d’un **workflow de production**.














# Bloc 19 – Ajout 19 : Ajouter des métriques personnalisées avec `make_metric`

---

## Objectif de ce bloc

- **Définir** des métriques personnalisées spécifiques aux besoins du projet.
- **Étendre** les métriques disponibles par défaut dans MLflow.

---

## Instructions détaillées

**À faire juste après** l'utilisation de `mlflow.evaluate()` (Bloc 18).

---

### 1. Définir des métriques personnalisées

Ajoute ce code **immédiatement après l’évaluation automatique** :

```python
from mlflow.models import make_metric
import numpy as np

# Définir une métrique personnalisée : somme des erreurs au carré plus 1
def squared_diff_plus_one(eval_df, _builtin_metrics):
    return np.sum(np.abs(eval_df["prediction"] - eval_df["target"] + 1) ** 2)

# Définir une autre métrique personnalisée : somme des cibles divisée par deux
def sum_on_target_divided_by_two(eval_df, builtin_metrics):
    return builtin_metrics["sum_on_target"] / 2

# Créer les objets métriques pour MLflow
squared_diff_plus_one_metric = make_metric(
    eval_fn=squared_diff_plus_one,
    greater_is_better=False,
    name="squared_diff_plus_one"
)

sum_on_target_divided_by_two_metric = make_metric(
    eval_fn=sum_on_target_divided_by_two,
    greater_is_better=True,
    name="sum_on_target_divided_by_two"
)
```

---

### 2. Pourquoi ce code est important ?

- **`squared_diff_plus_one`** : Modifie l'erreur quadratique pour tester des variantes.
- **`sum_on_target_divided_by_two`** : Utilise une métrique simple dérivée d’une somme intégrée.
- **`make_metric`** : Standardise l'intégration de métriques personnalisées dans MLflow.

---

## Position exacte dans ton script

| Partie | Emplacement |
|:------:|:------------|
| Définitions de métriques personnalisées | Juste après `mlflow.evaluate()` |

---

## Ce que ces métriques vont faire :

- **`squared_diff_plus_one`** : Donne une idée de la robustesse aux petites erreurs.
- **`sum_on_target_divided_by_two`** : Teste une propriété du dataset (pas du modèle).

---

# Code ajouté après ce Bloc

```python
from mlflow.models import make_metric
import numpy as np

def squared_diff_plus_one(eval_df, _builtin_metrics):
    return np.sum(np.abs(eval_df["prediction"] - eval_df["target"] + 1) ** 2)

def sum_on_target_divided_by_two(eval_df, builtin_metrics):
    return builtin_metrics["sum_on_target"] / 2

squared_diff_plus_one_metric = make_metric(
    eval_fn=squared_diff_plus_one,
    greater_is_better=False,
    name="squared_diff_plus_one"
)

sum_on_target_divided_by_two_metric = make_metric(
    eval_fn=sum_on_target_divided_by_two,
    greater_is_better=True,
    name="sum_on_target_divided_by_two"
)
```

---

# Résumé du Bloc 19

| Étape | Où l'ajouter | Pourquoi |
|:-----:|:------------:|:--------:|
| Définir des métriques personnalisées | Après `mlflow.evaluate()` standard | Étendre l’évaluation de modèle |

---

# **Résumé actuel du projet**

| Bloc | Fonction ajoutée | Pourquoi |
|:----:|:-----------------|:---------|
| 17 | Charger modèle | Tester après sauvegarde |
| 18 | Évaluation automatique | Obtenir des métriques standard |
| 19 | Ajouter métriques custom | Enrichir l’évaluation |

---

# Ce que tu as maintenant dans ton projet

- Modèle rechargé.
- Évalué automatiquement.
- Avec des **métriques personnalisées prêtes à être utilisées**.












# Bloc 20 – Ajout 20 : Générer des artefacts visuels lors de l’évaluation

---

## Objectif de ce bloc

- **Créer automatiquement** un **graphe visuel** dans MLflow (scatter plot entre prédictions et vraies valeurs).
- **Ajouter cet artefact** comme preuve visuelle de la qualité du modèle.

---

## Instructions détaillées

**À faire juste après** la définition des métriques personnalisées (Bloc 19).

---

### 1. Définir une fonction de création d'artefact

Ajoute ce code :

```python
import matplotlib.pyplot as plt
import os

# Fonction pour créer un graphique de dispersion
def prediction_target_scatter(eval_df, _builtin_metrics, artifacts_dir):
    plt.scatter(eval_df["prediction"], eval_df["target"])
    plt.xlabel("Predictions")
    plt.ylabel("True Values")
    plt.title("Scatter Plot: Predictions vs True Values")
    plot_path = os.path.join(artifacts_dir, "scatter_plot.png")
    plt.savefig(plot_path)
    plt.close()
    return {"scatter_plot_artifact": plot_path}
```

---

### 2. Pourquoi ce code est important ?

- **Visualisation immédiate** dans MLflow de la qualité de la prédiction.
- **Artefact** : Fichier `.png` sauvegardé automatiquement dans l’onglet Artefacts du run MLflow.

---

## Position exacte dans ton script

| Partie | Emplacement |
|:------:|:------------|
| Définir `prediction_target_scatter()` | Après la définition des métriques personnalisées |

---

### 3. Intégrer la fonction d'artefact dans `mlflow.evaluate`

Quand tu appelles `mlflow.evaluate`, ajoute :

```python
mlflow.evaluate(
    model=artifacts_uri,
    data=test,
    targets="quality",
    model_type="regressor",
    evaluators=["default"],
    custom_metrics=[
        squared_diff_plus_one_metric,
        sum_on_target_divided_by_two_metric
    ],
    custom_artifacts=[prediction_target_scatter]
)
```

Regarde bien :  
`custom_artifacts=[prediction_target_scatter]` est **la partie ajoutée**.

---

# Code ajouté après ce Bloc

```python
import matplotlib.pyplot as plt
import os

def prediction_target_scatter(eval_df, _builtin_metrics, artifacts_dir):
    plt.scatter(eval_df["prediction"], eval_df["target"])
    plt.xlabel("Predictions")
    plt.ylabel("True Values")
    plt.title("Scatter Plot: Predictions vs True Values")
    plot_path = os.path.join(artifacts_dir, "scatter_plot.png")
    plt.savefig(plot_path)
    plt.close()
    return {"scatter_plot_artifact": plot_path}
```

Et modification de `mlflow.evaluate` :

```python
mlflow.evaluate(
    model=artifacts_uri,
    data=test,
    targets="quality",
    model_type="regressor",
    evaluators=["default"],
    custom_metrics=[
        squared_diff_plus_one_metric,
        sum_on_target_divided_by_two_metric
    ],
    custom_artifacts=[prediction_target_scatter]
)
```

---

# Résumé du Bloc 20

| Étape | Où l'ajouter | Pourquoi |
|:-----:|:------------:|:--------:|
| Définir `prediction_target_scatter()` | Après définition des métriques personnalisées | Ajouter un visuel à l’évaluation |
| Modifier `mlflow.evaluate()` | Ajouter `custom_artifacts` | Voir l’alignement prédictions / valeurs réelles |

---

# Ce que tu as maintenant dans ton projet

- En plus des métriques, **un artefact visuel** est automatiquement généré pour chaque évaluation.
- Le **scatter plot** permet **de juger visuellement la performance** sans lire uniquement les chiffres.











# Bloc 21 – Ajout 21 : Intégrer un modèle de base (`DummyRegressor`)

---

## Objectif de ce bloc

- **Ajouter un modèle de base naïf** (DummyRegressor) qui sert de **référence minimale** pour évaluer si ElasticNet est **réellement meilleur**.
- **Logger les métriques** du DummyRegressor pour comparer avec ElasticNet.

---

## Instructions détaillées

**À faire juste après** l'entraînement du modèle ElasticNet.

---

### 1. Importer le DummyRegressor

Ajoute cette ligne **tout en haut du fichier** (près des imports) :

```python
from sklearn.dummy import DummyRegressor
```

---

### 2. Entraîner le modèle Dummy

Ajoute ce bloc de code :

```python
# Entraîner un modèle de base (DummyRegressor)
dummy = DummyRegressor(strategy="mean")
dummy.fit(train_x, train_y)

# Prédictions du modèle de base
dummy_predicted = dummy.predict(test_x)

# Calculer les métriques du DummyRegressor
(dummy_rmse, dummy_mae, dummy_r2) = eval_metrics(test_y, dummy_predicted)

print("DummyRegressor model:")
print("  RMSE: %s" % dummy_rmse)
print("  MAE: %s" % dummy_mae)
print("  R2: %s" % dummy_r2)
```

---

### 3. Logger les métriques Dummy dans MLflow

Après l’entraînement du modèle de base, ajoute :

```python
mlflow.log_metrics({
    "dummy_rmse": dummy_rmse,
    "dummy_mae": dummy_mae,
    "dummy_r2": dummy_r2
})
```

---

## Position exacte dans ton script

| Partie | Emplacement |
|:------:|:------------|
| Importer DummyRegressor | Ligne des imports |
| Entraîner et évaluer DummyRegressor | Après l'entraînement et le logging ElasticNet |
| Logger les métriques Dummy dans MLflow | Après le logging ElasticNet |

---

# Code ajouté après ce Bloc

```python
from sklearn.dummy import DummyRegressor

# Après entraînement ElasticNet
dummy = DummyRegressor(strategy="mean")
dummy.fit(train_x, train_y)
dummy_predicted = dummy.predict(test_x)

(dummy_rmse, dummy_mae, dummy_r2) = eval_metrics(test_y, dummy_predicted)

print("DummyRegressor model:")
print("  RMSE: %s" % dummy_rmse)
print("  MAE: %s" % dummy_mae)
print("  R2: %s" % dummy_r2)

mlflow.log_metrics({
    "dummy_rmse": dummy_rmse,
    "dummy_mae": dummy_mae,
    "dummy_r2": dummy_r2
})
```

---

# Résumé du Bloc 21

| Étape | Où l'ajouter | Pourquoi |
|:-----:|:------------:|:--------:|
| Importer DummyRegressor | En haut du fichier | Utiliser un modèle de base |
| Entraîner / prédire Dummy | Après ElasticNet | Avoir un benchmark minimum |
| Logger les métriques Dummy | Après métriques ElasticNet | Comparaison objective dans MLflow |

---

# Ce que tu as maintenant dans ton projet

- Tu as **deux modèles évalués** : ElasticNet **et** DummyRegressor.
- Tu pourras **prouver objectivement** que ElasticNet apporte une **valeur ajoutée réelle** (ou pas).
















# Bloc 22 – Ajout 22 : Ajouter des seuils de validation automatique avec `MetricThreshold`

---

## Objectif de ce bloc

- **Définir des critères** qui valident **automatiquement** si ElasticNet est **vraiment meilleur que le modèle de base**.
- **Utiliser `MetricThreshold`** pour comparer les métriques entre ElasticNet et Dummy.

---

## Instructions détaillées

**À faire après** l'entraînement de DummyRegressor et après avoir loggé ses métriques.

---

### 1. Importer MetricThreshold

Ajoute cette ligne **dans la partie des imports** :

```python
from mlflow.models import MetricThreshold
```

---

### 2. Définir les seuils de validation

Ajoute ce bloc **après le logging du modèle ElasticNet et Dummy** :

```python
# Définir un seuil sur la métrique "rmse"
thresholds = {
    "rmse": MetricThreshold(
        threshold=dummy_rmse,  # On exige que RMSE soit meilleur que celui du Dummy
        min_absolute_change=0.1,  # Minimum 0.1 de mieux
        min_relative_change=0.05,  # Minimum 5% de mieux
        greater_is_better=False  # Un RMSE plus petit est meilleur
    )
}
```

---

### 3. Préparer le chemin des modèles pour évaluation

Ajoute :

```python
# Récupérer l'URI du modèle ElasticNet
elasticnet_uri = mlflow.get_artifact_uri("model")
```

---

### 4. Évaluer et appliquer les seuils avec mlflow.evaluate

Ajoute ce bloc :

```python
mlflow.evaluate(
    model=elasticnet_uri,
    data=test,
    targets="quality",
    model_type="regressor",
    validation_thresholds=thresholds
)
```

---

## Position exacte dans ton script

| Partie | Emplacement |
|:------:|:------------|
| Importer `MetricThreshold` | Partie imports |
| Définir seuils | Après logging ElasticNet et Dummy |
| Obtenir ElasticNet URI | Après entraînement et logging ElasticNet |
| Évaluer avec mlflow.evaluate | Juste après définition des seuils |

---

# Code ajouté après ce Bloc

```python
from mlflow.models import MetricThreshold

# Définir un seuil sur la métrique "rmse"
thresholds = {
    "rmse": MetricThreshold(
        threshold=dummy_rmse,
        min_absolute_change=0.1,
        min_relative_change=0.05,
        greater_is_better=False
    )
}

# Obtenir l'URI du modèle ElasticNet
elasticnet_uri = mlflow.get_artifact_uri("model")

# Évaluer le modèle ElasticNet avec les seuils définis
mlflow.evaluate(
    model=elasticnet_uri,
    data=test,
    targets="quality",
    model_type="regressor",
    validation_thresholds=thresholds
)
```

---

# Résumé du Bloc 22

| Étape | Où l'ajouter | Pourquoi |
|:-----:|:------------:|:--------:|
| Importer MetricThreshold | En haut du fichier | Pouvoir définir des règles d'acceptation |
| Définir des seuils sur RMSE | Après log ElasticNet/Dummy | Vérifier que ElasticNet est utile |
| Évaluer avec mlflow.evaluate | Fin du script | Automatiser la validation des modèles |

---

# Ce que tu as maintenant dans ton projet

- Tu n'as **plus besoin d'inspecter manuellement** si ElasticNet est meilleur :  
Le script **refusera automatiquement** les modèles qui **ne surpassent pas** le modèle de base Dummy selon les critères définis.

















# Bloc 23 – Ajout 23 : Générer un graphique de comparaison prédictions vs cibles et l’enregistrer dans MLflow

---

## Objectif de ce bloc

- **Créer une figure** comparant visuellement les **prédictions** à la **réalité** (les vraies valeurs cibles).
- **Sauvegarder automatiquement** cette figure comme **artefact** attaché au run dans MLflow.

---

## Instructions détaillées

---

### 1. Importer `matplotlib.pyplot`

Ajoute cette ligne **dans la section imports** si ce n’est pas encore fait :

```python
import matplotlib.pyplot as plt
```

---

### 2. Créer une fonction pour générer le graphique

Ajoute cette fonction **juste avant la fin du script**, **avant `mlflow.end_run()`** :

```python
def plot_predictions_vs_targets(predictions, targets, save_path="scatter_plot.png"):
    plt.figure(figsize=(8, 6))
    plt.scatter(targets, predictions, alpha=0.5)
    plt.plot([targets.min(), targets.max()], [targets.min(), targets.max()], 'r--')
    plt.xlabel("Valeurs réelles (Target)")
    plt.ylabel("Prédictions")
    plt.title("Comparaison : Prédictions vs Cibles")
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()
```

---

### 3. Appeler la fonction pour créer le graphique

Ajoute ce bloc **immédiatement après avoir évalué ElasticNet sur `test_x` et obtenu `predicted_qualities`** :

```python
# Générer le graphique scatter plot
plot_predictions_vs_targets(predicted_qualities, test_y.values.flatten())
```

---

### 4. Logger le graphique comme artefact dans MLflow

Ajoute juste après avoir généré le fichier `scatter_plot.png` :

```python
mlflow.log_artifact("scatter_plot.png", artifact_path="plots")
```

---

## Position exacte dans ton script

| Partie | Emplacement précis |
|:------:|:--------------------|
| Importer matplotlib | Dans la partie imports |
| Fonction plot_predictions_vs_targets | Avant `mlflow.end_run()` |
| Génération du graphique | Après prédictions ElasticNet |
| Log du graphique dans MLflow | Juste après avoir généré le PNG |

---

# Code ajouté dans ce Bloc

```python
import matplotlib.pyplot as plt

def plot_predictions_vs_targets(predictions, targets, save_path="scatter_plot.png"):
    plt.figure(figsize=(8, 6))
    plt.scatter(targets, predictions, alpha=0.5)
    plt.plot([targets.min(), targets.max()], [targets.min(), targets.max()], 'r--')
    plt.xlabel("Valeurs réelles (Target)")
    plt.ylabel("Prédictions")
    plt.title("Comparaison : Prédictions vs Cibles")
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()

# Après prédictions ElasticNet
plot_predictions_vs_targets(predicted_qualities, test_y.values.flatten())

# Log du graphique
mlflow.log_artifact("scatter_plot.png", artifact_path="plots")
```

---

# Résumé du Bloc 23

| Étape | Où l'ajouter | Pourquoi |
|:-----:|:------------:|:--------:|
| Importer matplotlib | En haut du script | Pouvoir créer des figures |
| Définir fonction de scatter plot | Fin du script | Générer un graphique clair |
| Générer graphique après prédictions | Juste après prédiction | Visualiser la qualité du modèle |
| Log du PNG dans MLflow | Après génération | Sauvegarder la figure dans les artefacts |

---

# Ce que ton script sait faire après ce Bloc

- Il **entraîne** ElasticNet.
- Il **évalue** et **compare** les performances contre Dummy.
- Il **applique des règles de validation automatique** avec des seuils.
- Il **génère une figure** et **la sauvegarde** automatiquement dans MLflow comme artefact.
















# Bloc 24 – Ajout 24 : Inscription automatique du modèle ElasticNet dans le registre de modèles MLflow

---

## Objectif de ce bloc

- **Enregistrer** automatiquement notre modèle ElasticNet dans le **registre de modèles MLflow**.
- Permettre **une meilleure gestion** : historique des versions, promotion en staging/production, etc.

---

## Instructions détaillées

---

### 1. Modifier `mlflow.pyfunc.log_model`

Actuellement, tu utilises une commande comme :

```python
mlflow.pyfunc.log_model(
    artifact_path="sklear_mlflow_pyfunc",
    python_model=SklearnWrapper(),
    artifacts=artifacts,
    code_path=["main.py"],
    conda_env=conda_env
)
```

Tu dois **ajouter** le paramètre suivant :

```python
registered_model_name="ElasticNet-Production-Model"
```

Cela devient :

```python
mlflow.pyfunc.log_model(
    artifact_path="sklear_mlflow_pyfunc",
    python_model=SklearnWrapper(),
    artifacts=artifacts,
    code_path=["main.py"],
    conda_env=conda_env,
    registered_model_name="ElasticNet-Production-Model"
)
```

---

### 2. Où faire cette modification

| Partie | Emplacement précis |
|:------:|:--------------------|
| Log du modèle pyfunc | Lors de l'appel `mlflow.pyfunc.log_model` |

**Attention** : Ne pas confondre avec `mlflow.sklearn.log_model`, ici on est sur `mlflow.pyfunc.log_model`.

---

### 3. Résultat attendu

- Le modèle sera automatiquement enregistré dans **le registre de modèles** MLflow.
- Tu verras ton modèle dans l'interface web, dans **"Models"** avec le nom **ElasticNet-Production-Model**.

---

# Code ajouté dans ce Bloc

Version corrigée :

```python
mlflow.pyfunc.log_model(
    artifact_path="sklear_mlflow_pyfunc",
    python_model=SklearnWrapper(),
    artifacts=artifacts,
    code_path=["main.py"],
    conda_env=conda_env,
    registered_model_name="ElasticNet-Production-Model"
)
```

---

# Résumé du Bloc 24

| Étape | Où l'ajouter | Pourquoi |
|:-----:|:------------:|:--------:|
| Ajouter `registered_model_name` | Dans l'appel `log_model` | Inscrire le modèle ElasticNet dans MLflow Model Registry |

---

# Ce que ton script sait faire après ce Bloc

- Il **entraîne** un modèle.
- Il **génère** un graphique d'évaluation.
- Il **valide** automatiquement les performances.
- Il **log** tout dans MLflow (params, métriques, artefacts).
- Il **inscrit** automatiquement le modèle dans **Model Registry** prêt pour être promu.











# Bloc 25 – Ajout 25 : Promotion automatique du modèle dans le registre MLflow (Staging ou Production)

---

## Objectif de ce bloc

- **Automatiser** la promotion du modèle dans **Model Registry** selon sa performance.
- Si le **RMSE** est **inférieur** à un seuil fixé (par exemple 0.6), le modèle est directement promu vers **Staging** ou **Production**.

---

## Instructions détaillées

---

### 1. Importer les bibliothèques nécessaires pour manipuler le registre

Ajoute **en haut de ton script** dans la section importations, à côté de `import mlflow`, **cette ligne** :

```python
from mlflow import MlflowClient
```

**Où** :  
Juste après les autres imports MLflow (`import mlflow`, `import mlflow.sklearn`, etc.)

---

### 2. Définir un seuil de validation

Juste **après** avoir évalué ton modèle avec `eval_metrics`, ajoute :

```python
SEUIL_RMSE = 0.6
```

**Où** :  
Après ce bloc existant :

```python
rmse, mae, r2 = eval_metrics(test_y, predicted_qualities)
```

---

### 3. Ajouter la logique de promotion

Après avoir **loggé** ton modèle dans le registre avec `mlflow.pyfunc.log_model(...)`, **immédiatement après**, ajoute ce bloc :

```python
client = MlflowClient()
run_id = mlflow.active_run().info.run_id

if rmse < SEUIL_RMSE:
    # Promotion vers "Staging"
    client.transition_model_version_stage(
        name="ElasticNet-Production-Model",
        version=1,
        stage="Staging"
    )
    print(f"Modèle promu vers Staging car RMSE ({rmse:.3f}) est inférieur à {SEUIL_RMSE}")
else:
    print(f"Modèle NON promu (RMSE = {rmse:.3f} >= {SEUIL_RMSE})")
```

---

### 4. Attention sur le **version number**

Ici on a mis :

```python
version=1
```

**Important** :
- Cela suppose que c'est le premier modèle inscrit.
- Si plusieurs modèles sont enregistrés, il faudrait récupérer dynamiquement la bonne version.  
  (Je te donnerai la méthode plus avancée si besoin.)

---

## Code ajouté dans ce Bloc

Version ajoutée :

```python
from mlflow import MlflowClient

SEUIL_RMSE = 0.6

client = MlflowClient()
run_id = mlflow.active_run().info.run_id

if rmse < SEUIL_RMSE:
    client.transition_model_version_stage(
        name="ElasticNet-Production-Model",
        version=1,
        stage="Staging"
    )
    print(f"Modèle promu vers Staging car RMSE ({rmse:.3f}) est inférieur à {SEUIL_RMSE}")
else:
    print(f"Modèle NON promu (RMSE = {rmse:.3f} >= {SEUIL_RMSE})")
```

---

## Résultat attendu

- Si ton modèle est **meilleur que le seuil** (par exemple RMSE < 0.6), **MLflow passe directement** la version du modèle dans l’état **Staging**.
- Sinon, le modèle reste en **None** (non promu).

---

# Résumé du Bloc 25

| Étape | Où l'ajouter | Pourquoi |
|:-----:|:------------:|:--------:|
| Importer `MlflowClient` | En haut, avec les imports MLflow | Permet d'interagir avec Model Registry |
| Définir `SEUIL_RMSE` | Après l’évaluation `eval_metrics` | Fixe un seuil de promotion automatique |
| Logique de promotion | Après `log_model` | Passe automatiquement en **Staging** si le modèle est performant |

---

# Ce que ton script sait faire après ce Bloc

- Il **entraîne** un modèle ElasticNet.
- Il **évalue** les performances du modèle.
- Il **logge** tout (params, métriques, modèle).
- Il **inscrit** automatiquement le modèle dans le registre MLflow.
- Il **promeut** automatiquement le modèle si les performances sont au niveau attendu.



