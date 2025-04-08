**MLflow** est une **plateforme open source** conçue pour **gérer le cycle de vie des modèles de machine learning**. Elle est très utilisée pour suivre les expériences, reproduire les résultats, déployer des modèles et organiser les workflows ML de bout en bout.

### **À quoi sert MLflow ?**

MLflow sert principalement à :


#### 1. **Suivi des expériences (MLflow Tracking)**
- Permet d’enregistrer **les paramètres**, **les métriques**, **les artefacts** (modèles, images, etc.) et **le code source** utilisé dans chaque expérience.
- Utile pour **comparer les performances** entre différents essais de modèles.

#### 2. **Gestion des modèles (MLflow Models)**
- Supporte **l’enregistrement de modèles** dans différents formats (TensorFlow, PyTorch, Scikit-learn, etc.).
- Fournit une **API pour charger, évaluer et déployer** les modèles.

#### 3. **Registry des modèles (MLflow Model Registry)**
- Sert à **gérer les versions de modèles**, ajouter des commentaires, des métadonnées, marquer des modèles comme *Staging*, *Production*, etc.
- Parfait pour une **collaboration d’équipe** autour de la validation et du déploiement des modèles.

#### 4. **Déploiement facile (MLflow Projects et MLflow Serving)**
- Déploiement rapide avec `mlflow serve` pour exposer un modèle comme **API REST**.
- Intégration possible avec **Docker, Kubernetes, SageMaker**, etc.



### **Cas d’utilisation concrets**
- Entraîner un modèle plusieurs fois avec des hyperparamètres différents et **comparer automatiquement les résultats**.
- Suivre l’historique des modèles testés, reproduire les meilleures versions.
- Déployer un modèle directement depuis un notebook Jupyter.
- Travailler en équipe et suivre l’évolution des modèles dans le temps.

