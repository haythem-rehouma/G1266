
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








## Bilan clair de ce qu'on a fait :

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



