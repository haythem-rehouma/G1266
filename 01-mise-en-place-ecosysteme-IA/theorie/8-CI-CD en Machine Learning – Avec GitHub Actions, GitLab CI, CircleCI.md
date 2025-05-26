
# <h1 id="ci-cd-ml">CI-CD en Machine Learning – Avec GitHub Actions, GitLab CI, CircleCI</h1>



## <h2 id="serveurs-ci-cd">1. C’est quoi un serveur de CI/CD ?</h2>

Un **serveur CI/CD** est un **outil automatisé dans le cloud** (ou sur vos serveurs) qui **exécute vos tests, vos entraînements, vos validations, vos déploiements**, selon des règles définies.

Il :

* Surveille votre dépôt Git
* Lance des scripts dès qu’un changement est détecté (CI)
* Construit l’image Docker, la pousse et déploie (CD)
* Écrit des logs, crée des artefacts, et vous alerte en cas d’échec

---

## <h2 id="outils-ci-cd">2. Outils CI/CD populaires en ML</h2>

### 🟩 GitHub Actions

* **Gratuit pour les projets publics**, quotas pour privés
* Intégré directement à GitHub
* Simple à configurer (`.github/workflows/*.yml`)
* Très adapté aux projets **FastAPI + Streamlit + MLflow**
* Large support communautaire

---

### 🟦 GitLab CI/CD

* Intégré à GitLab
* Configuration dans `.gitlab-ci.yml`
* Supporte très bien les pipelines complexes (multi-stage)
* Très apprécié dans les équipes **DevOps/Data** en entreprise
* Peut être **auto-hébergé**

---

### 🟧 CircleCI

* Outil spécialisé dans la **vitesse et la scalabilité**
* Configuration dans `.circleci/config.yml`
* Optimisé pour les **Docker workflows**
* Intégrations avancées avec **AWS, Kubernetes, Terraform**
* Interface riche pour visualiser les builds

---

## <h2 id="workflow">3. Exemple de pipeline en Machine Learning</h2>

Imaginons une équipe de 3 personnes :

* Dev 1 change le code d'entraînement `train.py`
* Dev 2 met à jour `api.py` (FastAPI)
* Dev 3 modifie l’interface `ui.py` (Streamlit)

Un **serveur CI/CD** comme GitHub Actions :

1. Déclenche un pipeline :

   * Lint du code (`black`, `flake8`)
   * Tests unitaires (`pytest`)
   * Entraînement du modèle
   * Tracking avec MLflow
   * Construction d’un conteneur Docker avec API + UI
   * Déploiement vers staging via Docker Compose
2. Effectue des vérifications automatiques :

   * **/predict** de l’API renvoie une réponse en < 200ms ?
   * L’UI Streamlit se lance ?
   * Modèle validé > 90 % F1 ?
3. Si tout est OK → **déploiement green**

---

## <h2 id="comparatif">4. Comparatif des outils CI/CD en ML</h2>

| Critère                    | GitHub Actions         | GitLab CI/CD           | CircleCI                       |
| -------------------------- | ---------------------- | ---------------------- | ------------------------------ |
| **Intégration Git**        | GitHub native          | GitLab native          | GitHub, GitLab, Bitbucket      |
| **Configuration**          | Facile (`YAML`)        | Moyenne (`YAML`)       | Moyenne (`YAML`)               |
| **Support Docker**         | Très bon               | Excellent              | Excellent (optimisé)           |
| **Déploiement Kubernetes** | Possible (via scripts) | Oui natif              | Très bien intégré              |
| **Auto-hébergement**       | Non                    | Oui                    | Non                            |
| **Communauté / exemples**  | Enorme                 | Solide                 | Moyenne                        |
| **Prix**                   | Gratuit (limites)      | Gratuit (auto-hébergé) | Gratuit limité + payant rapide |
| **Adapté pour ML**         | ✔️ Simple & direct     | ✔️ Complexe & robuste  | ✔️ Pour projets plus lourds    |

---

## <h2 id="conclusion">5. Conclusion</h2>

En Machine Learning :

* Le **serveur CI/CD** devient le **chef d’orchestre automatique** de vos modèles, API, UI et livrables.
* Il permet de tester, valider, versionner, packager, déployer **sans intervention humaine**.
* Des outils comme **GitHub Actions** sont idéaux pour démarrer rapidement sur des projets ML typiques (FastAPI, Streamlit, MLflow, Docker).
* Pour des workflows **plus complexes**, **GitLab CI/CD** ou **CircleCI** sont des alternatives solides.

