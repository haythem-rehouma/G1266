

### Code 📝

```python
import pickle
import mlflow
import mlflow.sklearn

# Charger le modèle depuis un fichier .pkl
filename = 'elastic-net-regression.pkl'
loaded_model = pickle.load(open(filename, "rb"))

# Configurer le serveur de suivi MLflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")
exp = mlflow.set_experiment("experiment_register_outside")

# Démarrer une session MLflow
mlflow.start_run()

# Enregistrer le modèle chargé dans MLflow avec un nom spécifique
mlflow.sklearn.log_model(
    sk_model=loaded_model,
    artifact_path="model",
    serialization_format="cloudpickle",
    registered_model_name="elastic-net-regression-outside-mlflow"
)

# Terminer la session MLflow
mlflow.end_run()
```

---

### Instructions d'utilisation 📖

1. **Démarrer le serveur MLflow** :
   ```bash
   mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 127.0.0.1 --port 5000
   ```

2. **Exécuter le script** pour enregistrer le modèle dans MLflow :
   ```bash
   python <nom_du_script>.py
   ```

3. **Visualiser dans MLflow** à l'adresse `http://127.0.0.1:5000`.


> Ce script permet d'enregistrer un modèle déjà entraîné en dehors de MLflow dans l'interface MLflow en utilisant `cloudpickle` pour la sérialisation. Le modèle est également accessible via un nom de modèle MLflow enregistré pour une réutilisation facile.
