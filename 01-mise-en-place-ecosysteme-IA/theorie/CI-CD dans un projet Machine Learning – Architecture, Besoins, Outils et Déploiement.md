# <h1 id="ci-cd-ml">CI-CD dans un projet Machine Learning – Architecture, Besoins, Outils et Déploiement</h1>



## <h2 id="intro">1. Pourquoi CI/CD est crucial en Machine Learning ?</h2>

Les projets de **Machine Learning** ne sont pas seulement des modèles. Ils impliquent :

* Des scripts de **prétraitement de données**
* Des pipelines de **formation automatique**
* Des **API (FastAPI)** pour servir les modèles
* Des **interfaces utilisateurs (Streamlit, React)**
* Des **notebooks et logs de versionnage (MLflow, H2O AI)**

Le CI/CD permet de :

* Automatiser les **tests de data/code/model**
* Standardiser le **déploiement d’API et d’UI**
* Assurer des **mises à jour fiables** (green/blue)
* Travailler efficacement en **équipe multidisciplinaire**
* Suivre les **expériences** et contrôler les versions

---

## <h2 id="archi">2. Architecture typique CI/CD pour un projet ML</h2>

```
                ┌────────────────────────────┐
                │      Développeurs ML       │
                │  (Data + API + UI Team)    │
                └────────────┬───────────────┘
                             │
                   Git Commit / Push
                             │
        ┌────────────────────▼────────────────────┐
        │             Pipeline CI/CD               │
        │  (GitHub Actions, GitLab CI, Jenkins...) │
        └────────────┬────────────┬───────────────┘
                     │            │
      ┌──────────────▼──┐       ┌─▼─────────────────────┐
      │  1. Tests & Lint │       │ 2. Build Docker Images │
      └──────────────▲──┘       └────────────▲──────────┘
                     │                       │
         ┌───────────▼────────────┐   ┌──────▼──────────────┐
         │  3. Modèle Validé (ML) │   │ 4. API (FastAPI)     │
         │  + Tracking MLflow     │   │    UI (Streamlit)    │
         └────────────┬───────────┘   └─────────┬────────────┘
                      │                        │
        ┌─────────────▼────────────────────────▼────────────┐
        │     Docker Compose / Kubernetes (Staging)         │
        └────────────────────────────────────────────────────┘
                      │
      ┌───────────────▼─────────────────────────────────────┐
      │        Green / Blue Deployment en Production         │
      └──────────────────────────────────────────────────────┘
```

---

## <h2 id="groupe">3. Travail en groupe – Rôles et organisation</h2>

| Rôle                   | Responsabilités principales                                         |
| ---------------------- | ------------------------------------------------------------------- |
| **Data Scientist**     | Préparation des données, entraînement du modèle, évaluation         |
| **ML Engineer**        | Intégration du modèle dans un service, export `.pkl`, `.onnx`, etc. |
| **Backend Developer**  | Création de l’API avec FastAPI pour servir les prédictions          |
| **Frontend Developer** | Interface utilisateur avec Streamlit, Dash ou Next.js               |
| **DevOps Engineer**    | Mise en place du CI/CD, Docker, gestion des secrets, déploiement    |

**Organisation recommandée :**

* Code versionné dans **Git**
* **Branches par fonctionnalité** (`feature/ui`, `feature/api`, `train/model`)
* **Merge Request + Revue de code**
* **Pipeline CI/CD déclenché automatiquement** à chaque `push`

---

## <h2 id="pipeline">4. Contenu typique d’un pipeline CI/CD ML</h2>

### Étape CI (Intégration continue) :

* Vérifier que le modèle s’entraîne sans erreur (`train.py`)
* Tester les scripts de preprocessing
* Vérifier que l’API FastAPI se lance (`test_api.py`)
* Linter et formatter le code (`black`, `flake8`)

### Étape CD (Déploiement continu) :

* Générer l’image Docker :

  * `backend/Dockerfile` (FastAPI)
  * `frontend/Dockerfile` (Streamlit)
* Déployer avec Docker Compose ou Kubernetes
* Effectuer des **tests de santé** (API health check)
* Pousser automatiquement vers **staging**
* Effectuer un **déploiement blue/green** vers production

---

## <h2 id="green-blue">5. Déploiement Blue/Green</h2>

Le déploiement **Blue/Green** permet de déployer une nouvelle version sans interruption de service :

| Version actuelle | Nouvelle version déployée ? | Comportement                                |
| ---------------- | --------------------------- | ------------------------------------------- |
| **Blue**         | Oui, déployée en parallèle  | Les utilisateurs continuent d’utiliser Blue |
| Blue             | Green validée               | Le **trafic bascule vers Green**            |
| Green            | Problème détecté ?          | On revient à **Blue** (rollback)            |

> Cela permet de **tester une version en production** avec **0 interruption**.

---

## <h2 id="outils">6. Outils recommandés pour CI/CD ML</h2>

| Besoin                       | Outils recommandés                            |
| ---------------------------- | --------------------------------------------- |
| Versionnage code             | Git, GitHub, GitLab                           |
| Pipelines CI/CD              | GitHub Actions, GitLab CI, Jenkins            |
| Tests & qualité de code      | `pytest`, `flake8`, `black`, `isort`          |
| Suivi d’expériences ML       | MLflow, Weights & Biases, H2O.ai DriverlessAI |
| Conteneurisation             | Docker, Docker Compose                        |
| Orchestration et déploiement | Kubernetes, Helm, Docker Swarm                |
| Surveillance / logging       | Prometheus, Grafana, ELK, Sentry              |

---

## <h2 id="ml-cas">7. Cas d’application CI/CD – Projet ML réel</h2>

### Objectif :

Créer une application ML de **prédiction de prix immobiliers**.

### Architecture :

* **`train.py`** : entraînement et sauvegarde modèle `.pkl` (MLflow)
* **`api.py`** : FastAPI pour exposer `/predict`
* **`ui.py`** : Streamlit permettant d’entrer les caractéristiques
* **CI/CD** :

  * Training validé → modèle envoyé dans `models/`
  * API mise à jour et testée
  * Dockerfile reconstruit
  * Déploiement en **staging**
  * Blue/green vers production

---

## <h2 id="conclusion">8. Conclusion</h2>

Le CI/CD est **indispensable** en Machine Learning moderne :

* Il garantit la **qualité du code**
* Réduit les **erreurs de production**
* Automatique les livraisons répétitives
* Permet une vraie **collaboration interdisciplinaire**

Il s’intègre parfaitement avec des outils comme **FastAPI**, **Streamlit**, **MLflow**, **Docker** et les solutions **MLOps** modernes.


