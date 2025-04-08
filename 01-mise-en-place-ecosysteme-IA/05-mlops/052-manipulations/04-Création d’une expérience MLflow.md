# **1. Connexion à un serveur MLflow distant**
```python
mlflow.set_tracking_uri(uri="http://<IP-de-votre-VM>:5000")
```
- Cela définit l'URI du serveur MLflow où seront stockées les expériences.
- Tu dois remplacer `<IP-de-votre-VM>` par l’adresse IP réelle (ex. `192.168.1.10`).



# **2. Vérification de l’URI actuelle**
```python
print("The set tracking URI is ", mlflow.get_tracking_uri())
```
- Affiche l’URI actuellement utilisée (utile pour debug).



# **3. Création d’une expérience MLflow**
```python
exp_id = mlflow.create_experiment(
    name="exp_create_exp_artifact",
    tags={"version": "v1", "priority": "p1"},
    artifact_location=Path.cwd().joinpath("myartifacts").as_uri()
)
```
- Crée une **nouvelle expérience** MLflow avec :
  - `name` : nom de l’expérience.
  - `tags` : métadonnées personnalisées (version, priorité…).
  - `artifact_location` : où stocker les artefacts (résultats, modèles…), ici dans un dossier `myartifacts` du dossier courant.



# 4. Décomposons cette ligne :

```python
artifact_location = Path.cwd().joinpath("myartifacts").as_uri()
```



### **4.1. `Path.cwd()`**
- Renvoie le **chemin du répertoire courant** (le dossier où le script est exécuté).
  - Exemple : `/home/haythem/mlflow_project`

Testez : 

```python
 python -c "from pathlib import Path; print(Path.cwd())"
```

### **4.2. `.joinpath("myartifacts")`**
- Ajoute le dossier `"myartifacts"` à ce chemin.
  - Résultat : `/home/haythem/mlflow_project/myartifacts`



### **4.3. `.as_uri()`**
- Convertit ce chemin en **URI** (format reconnu par MLflow).
  - Résultat : `file:///home/haythem/mlflow_project/myartifacts`



### **Donc au final :**
Tu dis à MLflow :
> "Stocke les artefacts (modèles, fichiers, images…) dans un dossier local nommé `myartifacts` à côté de mon script, et voici son URI."



### **À quoi ça sert ?**
MLflow a besoin de savoir **où enregistrer les artefacts** (modèle entraîné, métriques, fichiers produits…).

Tu peux aussi mettre :
```python
artifact_location="s3://mon-bucket-mlflow/artifacts"
```
si tu veux tout stocker dans un **cloud S3** par exemple.


# **5. Récupération de l’expérience**
```python
get_exp = mlflow.get_experiment(exp_id)
```
- Récupère les métadonnées de l’expérience créée (`name`, `id`, `tags`, etc.).



# **6. Affichage des métadonnées**
```python
print("Name: {}".format(get_exp.name))
print("Experiment_id: {}".format(get_exp.experiment_id))
print("Artifact Location: {}".format(get_exp.artifact_location))
print("Tags: {}".format(get_exp.tags))
print("Lifecycle_stage: {}".format(get_exp.lifecycle_stage))
print("Creation timestamp: {}".format(get_exp.creation_time))
```
- Affiche les infos utiles de l’expérience, pour vérification.


# **7. Démarrage d’un run MLflow**
```python
with mlflow.start_run(experiment_id=exp_id):
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)
```
- Lance une session d’entraînement sous MLflow.
- `ElasticNet` est un modèle de régression.
- Ce bloc exécute l'entraînement et **MLflow enregistrera** automatiquement ce run dans l’expérience créée.



# 8.**Conclusion**
Ce script :
1. Configure un serveur MLflow distant.
2. Crée une expérience.
3. Lance un run d'entraînement.
4. Enregistre tous les artefacts, paramètres, métriques, modèle, etc.


# 9.Exercice :

- *Comparez create_experiment et set_tracking_uri pour la création d'expériences*

```python
  mlflow.set_tracking_uri("http://127.0.0.1:5000")
  print("Haythem test ", mlflow.get_tracking_uri())
  exp1 = mlflow.set_experiment(experiment_name="experience_2")
  exp2 = mlflow.set_experiment(experiment_name="experience_3")
  with mlflow.start_run(experiment_id=exp1.experiment_id):
        lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        lr.fit(train_x, train_y)
```



## Comparaison : `set_experiment()` vs `create_experiment()`

| Fonction | Rôle | Retourne | Si l’expérience existe déjà | À utiliser avec |
|----------|------|----------|------------------------------|------------------|
| `mlflow.create_experiment()` | Crée une nouvelle expérience | Un `experiment_id` (int) | Lève une erreur (expérience déjà existante) | Lorsque l'on veut contrôler précisément l’ID et l’emplacement des artefacts |
| `mlflow.set_experiment()` | Définit une expérience à utiliser (et la crée si elle n'existe pas) | Un objet `Experiment` | Ne lève pas d’erreur, l’expérience est simplement réutilisée | Pour une gestion simple, souvent utilisée avec `mlflow.start_run()` sans préciser d’ID |



### Exemple avec `create_experiment` (approche manuelle)


>```python
>mlflow.set_tracking_uri("http://127.0.0.1:5000")
>print("Haythem test ", mlflow.get_tracking_uri())
>```

```python
exp_id = mlflow.create_experiment(
    name="experience_1",
    artifact_location="file:///tmp/mlruns",
    tags={"version": "v1"}
)

with mlflow.start_run(experiment_id=exp_id):
    # Code d'entraînement
```

Comportement : une erreur sera levée si "experience_1" existe déjà.



### Exemple avec `set_experiment` (approche automatique)

```python
exp = mlflow.set_experiment("experience_1")

with mlflow.start_run():
    # Code d'entraînement
```

Comportement : si l’expérience existe, elle est utilisée ; sinon, elle est créée automatiquement.



## Résumé

| Objectif | Fonction recommandée |
|----------|----------------------|
| Créer une expérience une seule fois, avec un chemin d’artefacts spécifique | `create_experiment()` |
| Réutiliser ou créer automatiquement une expérience sans lever d’erreur | `set_experiment()` |


