# Examen Final – Projet libre en Machine Learning

<br/>

# 1 - Objectif et instructions

Vous devez concevoir un **projet complet de Machine Learning**, en totale liberté de choix sur :

* Le **type de problème ML** (classification, régression, clustering, apprentissage supervisé , non supervisé, RL, ...etc.)
* Le **dataset** utilisé
* Le **langage**, les **frameworks** (ML, API, frontend)
* L’architecture technique (microservices ou non, BDD ou non)
* L’interface utilisateur (optionnelle mais encouragée)

> **Seule contrainte obligatoire : le projet doit être déployable via `docker-compose`.**

<br/>

# 2 - Contraintes techniques

| Élément                                          | Obligatoire ?        |
| ------------------------------------------------ | -------------------- |
| Sujet du projet                                  |  Libre              |
| Type de données / dataset                        |  Libre              |
| Choix du backend (FastAPI, Flask, Django, etc.)  |  Libre              |
| Choix du frontend (HTML, React, Streamlit, etc.) |  Libre              |
| Gestion des modèles (MLflow, Pickle, etc.)       |  Libre              |
| CI/CD (GitHub Actions, GitLab CI, etc.)          |  Facultatif (bonus) |
| **Déploiement avec `docker-compose`**            |  **Obligatoire**    |

<br/>

# 3 - Critères et grille d’évaluation

| Critère                                         | Points  |
| ----------------------------------------------- | ------- |
| Fonctionnalité générale du projet               | 25      |
| Cohérence technique globale et réponses aux questions    | 20      |
| Utilisation pertinente des bibliothèques/outils | 15      |
| Qualité et organisation du code                 | 15      |
| Documentation (`README.md`)                     | 10      |
| **Déploiement avec `docker-compose`**           | 15      |
| **Total**                                       | **100** |

<br/>

# 4 - Bonus (jusqu’à 30 points)

Des points supplémentaires peuvent être accordés pour :

* Mise en place d’un **pipeline CI/CD** (tests, build, déploiement)
* Présentation soignée (ex. interface web claire)
* Richesse fonctionnelle ou innovation
* Démonstration vidéo ou site en ligne


<br/>











# 5 - Livrables attendus

### 1. Code source complet

* Inclure tous les scripts et fichiers nécessaires (ML, backend, frontend s’il y a lieu)
* Code clair, structuré, commenté et organisé par dossier

> ⚠ Un code très désorganisé entraînera des pertes de points.



### 2. `docker-compose.yml` 

* Permet de lancer l’ensemble du projet (API, ML, interface, etc.)
* Peut inclure des volumes, réseaux, services, dépendances



### 3. Fichier `README.md`

Doit contenir obligatoirement :

* Une **description claire** du projet
* Les **étapes pour installer, exécuter et tester** le projet
* Les **commandes Docker et Docker Compose**
* Le **nom des bibliothèques principales** utilisées
* (Optionnel) instructions CI/CD si applicable


### 4. Documentation technique synthétique

* Architecture générale - Structure de l’architecture (ML, API, frontend s’il y en a)
* Explication du modèle et de son fonctionnement - Description du modèle de ML : type, but, format d’entrée/sortie
* Comment le backend interagit avec le modèle et exemple(s) d’utilisation ou de requête API
* Quels services sont lancés par `docker-compose`
* Réponses aux questions techniques qui pourraient vous être posées à l’oral











<br/>

# 6 - Date de remise

> **Date limite : 06 juin 2024 à 23h59**

<br/>

# 7 - Remarques finales

* Le projet est à réalisé d'une façon individuelle.
* Un projet simple mais bien structuré et déployé vaut mieux qu’un projet trop ambitieux non terminé
* L’intégration d’un pipeline **CI/CD**, même minimal, sera **très bien vue**







































