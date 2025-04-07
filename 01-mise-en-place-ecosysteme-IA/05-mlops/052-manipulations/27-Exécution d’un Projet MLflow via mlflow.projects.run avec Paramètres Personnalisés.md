

```python
import mlflow

# Définition des paramètres d'entraînement
parameters = {
    "alpha": 0.3,
    "l1_ratio": 0.3
}

# Nom de l'expérience et point d'entrée
experiment_name = "Project exp 1"
entry_point = "ElasticNet"

# Exécution du projet MLflow
mlflow.projects.run(
    uri=".",  # Exécution dans le répertoire actuel
    entry_point=entry_point,
    parameters=parameters,
    experiment_name=experiment_name
)
```

### Explications 

- **parameters** : Contient les valeurs de `alpha` et `l1_ratio` pour le modèle ElasticNet, ici définies à `0.3`.
- **experiment_name** : Nom de l'expérience dans laquelle MLflow enregistrera les résultats, ici `"Project exp 1"`.
- **entry_point** : Nom du point d'entrée dans le fichier YAML de votre projet, spécifié ici comme `"ElasticNet"`.

### Utilisation 

> Ce script lance l'exécution de l'expérience avec les paramètres donnés. Assurez-vous que le fichier YAML (`MLproject`) est bien configuré avec le même nom de point d'entrée (`ElasticNet`).
