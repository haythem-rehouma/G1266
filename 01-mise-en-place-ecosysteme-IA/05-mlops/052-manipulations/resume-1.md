# Résumé Final Ultra-Rapide

| Code | Ajout principal | Objectif |
|:----:|:----------------|:---------|
| 0 | Installation MLflow | Initialiser serveur local |
| 1 | Première expérience | Log simple |
| 2 | Requirements.txt | Gérer les dépendances |
| 3 | Tracking URI | Cibler un serveur |
| 4 | Créer une expérience | Structurer le tracking |
| 5 | Infos sur les runs | Debug efficace |
| 6 | Logger artefacts | Sauver des fichiers |
| 7 | Ajouter des tags | Améliorer la recherche |
| 8 | Multi-runs | Hyperparameter tuning |
| 9 | Multi-expériences | Séparer les projets |
| 10 | Auto-log | Logging automatique |
| 11 | Production avec S3/PostgreSQL | Architecture scalable |
| 12 | Signature + Input Example | Documenter les entrées/sorties |
| 13 | Signature auto avec infer_signature | Automatiser les schémas |
| 14 | Signature manuelle Schema/ColSpec | Contrôler précisément le modèle |
| 15 | Pyfunc Wrapper | Modèle 100% customisable |
| 16 | Environnement Conda | Portabilité totale |
| 17 | Chargement modèle MLflow | Faire des prédictions |
| 18 | Évaluation automatique | Obtenir les métriques |
| 19 | Métriques et artefacts custom | Analyse enrichie |
| 20 | Modèle baseline Dummy | Comparaison obligatoire |
| 21 | Registry de modèle | Versionner proprement |
| 22 | Vérification des chemins | Sécuriser les enregistrements |
| 23 | Chargement pyfunc universel | Support multi-langages |
| 24 | Import modèle existant | Centraliser l'historique |
| 25 | Script d'expérience complet | Standardiser l'entraînement |
| 26 | Projet MLflow paramétré | Déploiement flexible |
| 27 | Diagnostic MLflow | Maintenance environnementale |
| 28 | Gestion avancée artefacts | Manipuler manuellement les fichiers |
| 29 | Gestion avancée expériences/runs | Administration serveur MLflow |


---

# Code 0 – Installation MLflow

**Ajout principal** :  
Installation et configuration de base de MLflow (serveur MLflow, MLflow UI, backend sqlite, dossier `mlruns`).

**But** :  
Démarrer un serveur de suivi MLflow local pour stocker et visualiser les expériences.

**Dans le code** :

```bash
pip install mlflow
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000
```

---

# Code 1 – Première expérience MLflow basique

**Ajout principal** :  
Création et exécution d'une première expérience MLflow (`set_experiment`, `start_run`).

**But** :  
Lancer un modèle simple et logger les paramètres, métriques et le modèle.

**Dans le code** :

```python
import mlflow
import mlflow.sklearn

mlflow.set_experiment("experience_1")

with mlflow.start_run():
    mlflow.log_param("alpha", 0.5)
    mlflow.log_metric("rmse", 0.25)
    mlflow.sklearn.log_model(model, "model")
```

---

# Code 2 – Ajout d'un requirements.txt

**Ajout principal** :  
Création d'un fichier `requirements.txt` pour centraliser toutes les dépendances.

**But** :  
Simplifier l’installation de l’environnement de développement.

**Dans le code** :

- Fichier `requirements.txt` :
  ```
  mlflow
  scikit-learn
  pandas
  numpy
  ```
- Installation rapide :

```bash
pip install -r requirements.txt
```

---

# Code 3 – Utilisation de set_tracking_uri et get_tracking_uri

**Ajout principal** :  
Changer dynamiquement l’URI de suivi pour envoyer les logs vers un autre serveur ou un autre répertoire.

**But** :  
Flexibilité totale sur l’emplacement du backend MLflow.

**Dans le code** :

```python
mlflow.set_tracking_uri("http://127.0.0.1:5000")
print(mlflow.get_tracking_uri())
```

---

# Code 4 – Utilisation de create_experiment

**Ajout principal** :  
Créer une nouvelle expérience MLflow manuellement avec une `artifact_location` personnalisée.

**But** :  
Organiser les expériences de manière propre dès leur création.

**Dans le code** :

```python
experiment_id = mlflow.create_experiment(
    name="nouvelle_experience",
    artifact_location="file:///chemin/vers/artifacts"
)
mlflow.get_experiment(experiment_id)
```

---

# Code 5 – Utilisation de active_run et last_active_run

**Ajout principal** :  
Récupérer en direct l'ID de l'exécution en cours (`active_run`) ou la dernière exécution (`last_active_run`).

**But** :  
Faciliter le debug et les automatisations basées sur les runs.

**Dans le code** :

```python
with mlflow.start_run() as run:
    print(mlflow.active_run().info.run_id)

print(mlflow.last_active_run().info.run_id)
```

---

# Code 6 – Utilisation de log_artifacts

**Ajout principal** :  
Enregistrer un fichier ou un répertoire complet comme artefact lié au run.

**But** :  
Stocker et tracer des fichiers auxiliaires (images, datasets, modèles manuels, etc.).

**Dans le code** :

```python
mlflow.log_artifacts("dossier_a_logger/")
```
Exemple pour tout logger depuis un sous-dossier `data/` :

```python
mlflow.log_artifacts("data/")
```

---

# Code 7 – Utilisation de set_tags

**Ajout principal** :  
Ajouter des métadonnées (`tags`) pour enrichir les runs MLflow.

**But** :  
Faciliter le filtrage, le tri, et la recherche de runs dans MLflow UI.

**Dans le code** :

```python
mlflow.set_tags({
    "framework": "scikit-learn",
    "type": "ElasticNet",
    "phase": "experiment",
    "version": "v1.0"
})
```

---

# Code 8 – Lancer plusieurs exécutions (runs) dans le même script

**Ajout principal** :  
Enchainer plusieurs exécutions MLflow au sein du même script avec des paramètres différents.

**But** :  
Tester plusieurs variantes d'hyperparamètres en une seule fois.

**Dans le code** :

```python
for alpha in [0.1, 0.3, 0.5, 0.7]:
    with mlflow.start_run(run_name=f"run_alpha_{alpha}"):
        mlflow.log_param("alpha", alpha)
        model = ElasticNet(alpha=alpha)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        rmse = mean_squared_error(y_test, preds, squared=False)
        mlflow.log_metric("rmse", rmse)
```

---

# Code 9 – Lancer plusieurs expériences (experiments) différentes

**Ajout principal** :  
Changer l'expérience (`set_experiment`) selon la nature de chaque modèle testé.

**But** :  
Séparer clairement les runs par famille de modèles ou type d'expérience.

**Dans le code** :

```python
# Expérience ElasticNet
mlflow.set_experiment("ElasticNet_experiment")
with mlflow.start_run():
    train_elasticnet()

# Expérience Ridge
mlflow.set_experiment("Ridge_experiment")
with mlflow.start_run():
    train_ridge()

# Expérience Lasso
mlflow.set_experiment("Lasso_experiment")
with mlflow.start_run():
    train_lasso()
```

---

# Code 10 – Utilisation de mlflow.autolog

**Ajout principal** :  
Activer l’auto-logging pour ne plus avoir à écrire explicitement `log_param`, `log_metric`, `log_model`.

**But** :  
Simplifier considérablement le code d'entraînement.

**Dans le code** :

```python
mlflow.autolog()

model = ElasticNet(alpha=0.5, l1_ratio=0.5)
model.fit(X_train, y_train)
```
*(Plus besoin de mlflow.log_param(), mlflow.log_metric(), mlflow.log_model(), tout est automatique.)*

---

# Code 11 – Configurer un stockage externe (S3 + PostgreSQL)

**Ajout principal** :  
Configurer MLflow pour utiliser PostgreSQL comme base de données (`backend-store`) et Amazon S3 comme stockage des artefacts (`artifact-root`).

**But** :  
Passer à une architecture cloud scalable pour la production.

**Dans le code** :

```bash
mlflow server \
    --backend-store-uri postgresql://user:password@host:5432/mlflowdb \
    --default-artifact-root s3://nom-du-bucket/artifacts \
    --host 0.0.0.0 --port 5000
```





---

# Code 12 – Ajout d'une Signature et d'un Input Example dans MLflow

**Ajout principal** :  
Utilisation de `ModelSignature` et `input_example` lors de l'enregistrement du modèle.

**But** :  
Documenter automatiquement les types d'entrée et de sortie du modèle.

**Dans le code** :

```python
from mlflow.models.signature import infer_signature

signature = infer_signature(X_test, preds)
mlflow.sklearn.log_model(model, "model", signature=signature, input_example=X_test.iloc[:5])
```

---

# Code 13 – Signature Automatique avec infer_signature

**Ajout principal** :  
Utiliser `infer_signature()` pour générer dynamiquement la signature sans tout écrire à la main.

**But** :  
Éviter de spécifier manuellement les types d'entrées/sorties.

**Dans le code** :

```python
signature = infer_signature(X_test, preds)
```

---

# Code 14 – Création manuelle d'une Signature avec Schema et ColSpec

**Ajout principal** :  
Définir une signature de modèle de manière explicite et contrôlée.

**But** :  
Préciser finement les types et noms des colonnes d'entrée et sortie.

**Dans le code** :

```python
from mlflow.types.schema import Schema, ColSpec
input_schema = Schema([ColSpec("double", "feature1"), ColSpec("double", "feature2")])
output_schema = Schema([ColSpec("double")])
signature = ModelSignature(inputs=input_schema, outputs=output_schema)
```

---

# Code 15 – Sauvegarde Custom du Modèle avec Pyfunc Wrapper

**Ajout principal** :  
Créer un `PythonModel` personnalisé pour charger/prédire avec flexibilité.

**But** :  
Permettre un contrôle total sur le comportement du modèle.

**Dans le code** :

```python
import mlflow.pyfunc

class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        import joblib
        self.model = joblib.load(context.artifacts["model.pkl"])
        
    def predict(self, context, model_input):
        return self.model.predict(model_input)

mlflow.pyfunc.log_model(
    artifact_path="custom_model",
    python_model=CustomModel(),
    artifacts={"model.pkl": "path/to/model.pkl"},
    code_path=["script.py"]
)
```

---

# Code 16 – Sauvegarde Custom avec Environnement Conda

**Ajout principal** :  
Créer un environnement `conda.yaml` pour encapsuler toutes les dépendances du modèle.

**But** :  
Rendre le modèle totalement portable.

**Dans le code** :

```python
conda_env = {
    "channels": ["defaults"],
    "dependencies": [
        "python=3.8",
        "scikit-learn=0.24.1",
        "mlflow",
        "cloudpickle"
    ],
    "name": "mlflow-env"
}

mlflow.pyfunc.log_model(
    artifact_path="model_custom",
    python_model=CustomModel(),
    conda_env=conda_env,
    artifacts={"model.pkl": "path/to/model.pkl"},
)
```

---

# Code 17 – Chargement du Modèle depuis MLflow

**Ajout principal** :  
Utiliser `mlflow.pyfunc.load_model()` pour récupérer et utiliser un modèle sauvegardé.

**But** :  
Faire des prédictions directement à partir du modèle stocké dans MLflow.

**Dans le code** :

```python
model_loaded = mlflow.pyfunc.load_model(model_uri="runs:/<run_id>/model")
preds = model_loaded.predict(X_test)
```

---

# Code 18 – Évaluation du Modèle avec mlflow.evaluate

**Ajout principal** :  
Utiliser `mlflow.evaluate()` pour évaluer automatiquement un modèle sur un jeu de test.

**But** :  
Calculer RMSE, MAE, R2 et d'autres métriques sans effort.

**Dans le code** :

```python
mlflow.evaluate(
    model="runs:/<run_id>/model",
    data=test,
    targets="quality",
    model_type="regressor"
)
```

---

# Code 19 – Ajout de Métriques Personnalisées et Artefacts Visuels

**Ajout principal** :  
Créer des métriques et artefacts personnalisés pour enrichir l'évaluation.

**But** :  
Obtenir des insights supplémentaires visuellement et analytiquement.

**Dans le code** :

```python
from mlflow.models import make_metric

def custom_metric(eval_df, _):
    return np.mean((eval_df["prediction"] - eval_df["target"]) ** 2)

custom_metric_fn = make_metric(
    eval_fn=custom_metric,
    greater_is_better=False,
    name="custom_mse"
)
```

Et artefact graphique :

```python
def scatter_plot(eval_df, _, artifacts_dir):
    import matplotlib.pyplot as plt
    plt.scatter(eval_df["prediction"], eval_df["target"])
    plt.savefig(os.path.join(artifacts_dir, "scatter.png"))
    return {"scatter_plot": "scatter.png"}
```

---

# Code 20 – Validation avec un Modèle Baseline

**Ajout principal** :  
Comparer les performances d'un modèle avancé par rapport à un modèle de base (DummyRegressor).

**But** :  
S'assurer que le modèle produit vraiment un gain par rapport à du hasard.

**Dans le code** :

```python
from sklearn.dummy import DummyRegressor

baseline = DummyRegressor()
baseline.fit(X_train, y_train)
baseline_preds = baseline.predict(X_test)
```

---

# Code 21 – Enregistrement du Modèle avec registered_model_name

**Ajout principal** :  
Enregistrer un modèle sous un nom pour gestion multi-versions (Model Registry).

**But** :  
Permettre versioning, validation et déploiement.

**Dans le code** :

```python
mlflow.sklearn.log_model(model, artifact_path="model", registered_model_name="elasticnet_model")
```

---

# Code 22 – Vérification du Type de Chemin avant Sauvegarde

**Ajout principal** :  
S'assurer que les chemins sont valides et existants avant de logger des fichiers.

**But** :  
Robustesse du script en environnement de production.

**Dans le code** :

```python
def get_path_type(path):
    if os.path.exists(path):
        return "directory" if os.path.isdir(path) else "file"
    return "invalid"
```

---

# Code 23 – Utilisation de MLflow pour charger un modèle avec Pyfunc

**Ajout principal** :  
Utiliser `mlflow.pyfunc.load_model()` pour rendre un modèle universel (support multiple langages).

**But** :  
Faciliter l'intégration du modèle dans tout type d'application.

**Dans le code** :

```python
model = mlflow.pyfunc.load_model(model_uri="models:/elasticnet_model/Production")
```

---

# Code 24 – Enregistrement d'un modèle externe existant dans MLflow

**Ajout principal** :  
Logger un modèle déjà entraîné hors de MLflow dans le système MLflow.

**But** :  
Centraliser tout l'historique même pour les anciens modèles.

**Dans le code** :

```python
import pickle

model = pickle.load(open("model.pkl", "rb"))
mlflow.sklearn.log_model(model, "model", registered_model_name="external_model")
```

---

# Code 25 – Script complet d'expérience avec sauvegarde automatique

**Ajout principal** :  
Écrire un script `train.py` propre pour lancer, logger, sauvegarder un modèle MLflow.

**But** :  
Industrialiser l’entraînement et la traçabilité.

*(déjà vu en grande partie précédemment avec `train.py` propre.)*

---

# Code 26 – Lancer un projet MLflow avec parameters

**Ajout principal** :  
Utiliser `mlflow.projects.run()` pour lancer un projet paramétré.

**But** :  
Déployer un projet standardisé (`MLproject`) sur tout serveur.

**Dans le code** :

```python
mlflow.projects.run(
    uri=".",
    entry_point="main",
    parameters={"alpha": 0.3, "l1_ratio": 0.3},
    experiment_name="exp_project"
)
```

---

# Code 27 – Diagnostiquer MLflow avec mlflow doctor

**Ajout principal** :  
Analyser l'installation pour résoudre problèmes potentiels.

**But** :  
Assurer la compatibilité environnementale.

**Dans le code** :

```bash
mlflow doctor
mlflow doctor --mask-envs
```

---

# Code 28 – Gestion avancée des artefacts MLflow

**Ajout principal** :  
Lister, télécharger, uploader des artefacts manuellement depuis CLI.

**But** :  
Manipuler les fichiers associés à un run.

**Dans le code** :

```bash
mlflow artifacts list --run-id <RUN_ID>
mlflow artifacts download --run-id <RUN_ID> --dst-path local_dir
mlflow artifacts log-artifacts --local-dir local_dir --run-id <RUN_ID>
```

---

# Code 29 – Gestion avancée des expériences et des runs

**Ajout principal** :  
Créer, renommer, supprimer, restaurer des expériences et runs.

**But** :  
Gérer un serveur MLflow de manière propre et professionnelle.

**Dans le code** :

```bash
mlflow experiments create --experiment-name new_experiment
mlflow experiments rename --experiment-id 2 --new-name better_experiment
mlflow experiments delete --experiment-id 2
mlflow experiments restore --experiment-id 2

mlflow runs delete --run-id <RUN_ID>
mlflow runs restore --run-id <RUN_ID>
```


# Résumé Global

| Code | Fonction Principale | Objectif |
|:----:|:--------------------|:---------|
| 12–14 | Signatures et Input Example | Documentation du modèle |
| 15–17 | Custom Model + Environnements | Flexibilité et reproductibilité |
| 18–20 | Évaluation Automatique et Baseline | Analyse et comparaison avancée |
| 21–24 | Enregistrement + Registry | Gestion multi-versions |
| 25–26 | Projets MLflow | Déploiement standardisé |
| 27–29 | Diagnostics + Artefacts | Maintenance et gestion serveur |

