
En **MLflow**, le **Tracking URI** définit **où** les expériences (runs, paramètres, modèles, métriques…) seront stockées.



### **1. `mlflow.get_tracking_uri()`**
- **But :** Affiche l’URL actuelle de suivi (par défaut : dossier local).
- **Exemple :**
```python
import mlflow
print(mlflow.get_tracking_uri())
```

---

### **2. `mlflow.set_tracking_uri("URI")`**
- **But :** Change l’emplacement de stockage des expériences MLflow.
- **Exemples d'URI possibles :**

| URI                           | Signification                                     |
|------------------------------|---------------------------------------------------|
| `"file:/chemin/local"`       | Sauvegarde locale sur le disque                   |
| `"http://localhost:5000"`    | Serveur MLflow distant (par ex. lancé avec `mlflow ui`) |
| `"sqlite:///mlflow.db"`      | Base de données SQLite locale                     |
| `"postgresql://user:pwd@host/db"` | Base PostgreSQL distante                         |

- **Exemple concret :**
```python
mlflow.set_tracking_uri("http://localhost:5000")
```

---

### **Conclusion rapide**
- `get_tracking_uri()` : pour voir où MLflow enregistre.
- `set_tracking_uri(uri)` : pour **choisir l’endroit** où MLflow va enregistrer (local, distant, base de données...).
