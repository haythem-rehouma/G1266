#  Cours théorique : Comprendre le Workflow Complet de MLflow (0 → 29)

---

**Code 0 – Installation de MLflow**  
MLflow est une plateforme de gestion du cycle de vie des modèles machine learning. Son installation permet de créer un serveur local pour suivre les expériences, stocker les artefacts et visualiser les résultats via une interface web.

---

**Code 1 – Première expérience**  
La première expérience consiste à enregistrer manuellement un paramètre, une métrique et un modèle. Cela établit les bases de la traçabilité des essais dans MLflow en documentant les performances des premiers modèles.

---

**Code 2 – Requirements.txt**  
Pour assurer la reproductibilité, un fichier `requirements.txt` regroupe toutes les dépendances Python nécessaires. Ce fichier garantit que toute personne exécutant le projet aura un environnement logiciel cohérent.

---

**Code 3 – Tracking URI**  
La Tracking URI configure l’emplacement où MLflow envoie les informations de suivi (base SQLite locale ou serveur distant). Cela permet d'adapter l'infrastructure selon que l’on travaille seul ou en équipe.

---

**Code 4 – Créer une expérience**  
Créer une expérience MLflow permet d'organiser logiquement les runs. Chaque expérience représente un projet, facilitant la séparation claire entre différentes lignes de recherche ou types de modèles.

---

**Code 5 – Informations sur les runs**  
Accéder aux informations d’un run en cours ou passé sans passer par l’interface web est crucial pour automatiser des vérifications, faire du debug ou programmer des pipelines sans intervention manuelle.

---

**Code 6 – Logger des artefacts**  
Les artefacts sont des fichiers produits lors de l’entraînement : datasets, figures, modèles. Les logger permet d'associer ces fichiers à un run, garantissant la conservation complète des résultats.

---

**Code 7 – Ajouter des tags**  
Les tags sont des paires clé/valeur qui annotent un run. Ils permettent de filtrer, de rechercher, et de mieux documenter chaque expérimentation, surtout dans des projets complexes ou collaboratifs.

---

**Code 8 – Plusieurs runs dans un même script**  
Pouvoir exécuter plusieurs runs dans un seul script permet d'automatiser des expérimentations, par exemple en testant différentes combinaisons d'hyperparamètres, sans relancer manuellement chaque configuration.

---

**Code 9 – Plusieurs expériences différentes**  
Changer dynamiquement d’expérience permet de structurer clairement les essais : chaque type de modèle ou de stratégie de validation peut avoir son propre historique, proprement isolé.

---

**Code 10 – Auto-log**  
L’auto-logging capture automatiquement tous les paramètres, métriques et modèles sans avoir à écrire manuellement les commandes de log. Cela réduit le risque d'oubli et accélère le développement.

---

**Code 11 – Production avec S3/PostgreSQL**  
Utiliser PostgreSQL pour les métadonnées et S3 pour les artefacts permet de rendre MLflow adapté aux usages de production : haute disponibilité, stockage distribué, support du multi-utilisateur.

---

**Code 12 – Signature + Input Example**  
Définir une signature explicite et un exemple d’entrée documente formellement ce que le modèle attend en entrée et ce qu'il produit en sortie, renforçant la clarté et la portabilité.

---

**Code 13 – Signature automatique avec infer_signature**  
Avec `infer_signature`, MLflow déduit automatiquement la structure des entrées et sorties du modèle, simplifiant la documentation tout en réduisant les erreurs humaines.

---

**Code 14 – Signature manuelle avec Schema/ColSpec**  
Définir manuellement un schéma avec `Schema` et `ColSpec` offre un contrôle total sur la définition des entrées/sorties, indispensable dans des cas critiques ou fortement réglementés.

---

**Code 15 – Pyfunc Wrapper**  
Créer un wrapper Pyfunc permet d'encapsuler n'importe quel modèle dans une interface uniforme. Cela facilite la standardisation du déploiement et l’intégration avec divers outils ou APIs.

---

**Code 16 – Environnement Conda**  
Définir un environnement Conda pour le modèle assure que l'environnement logiciel peut être reconstruit à l'identique ailleurs, ce qui est essentiel pour la portabilité et la reproductibilité.

---

**Code 17 – Chargement du modèle MLflow**  
Recharger un modèle depuis MLflow permet de refaire des prédictions sans devoir régénérer ou réentraîner le modèle, ce qui accélère considérablement les itérations et tests.

---

**Code 18 – Évaluation automatique**  
Avec `mlflow.evaluate`, on peut générer automatiquement des métriques standards pour évaluer un modèle sur un jeu de données, réduisant le temps de validation et uniformisant l’évaluation.

---

**Code 19 – Métriques et artefacts personnalisés**  
Ajouter des métriques customisées et générer des artefacts visuels permet d’aller plus loin que les métriques standards, offrant des analyses enrichies et adaptées à des besoins spécifiques.

---

**Code 20 – Modèle baseline Dummy**  
Utiliser un modèle de base (`DummyRegressor`) donne un point de comparaison minimal : un modèle de production doit toujours surpasser la performance d’un modèle trivial.

---

**Code 21 – Registry de modèle**  
Le registre de modèles MLflow permet de versionner, promouvoir, ou retirer des modèles. Cela transforme le suivi des modèles en un processus rigoureux et industriel.

---

**Code 22 – Vérification des chemins**  
Vérifier le type et l’existence des chemins (fichiers, répertoires) avant de logger des artefacts sécurise le processus et évite les erreurs dues à des chemins invalides ou absents.

---

**Code 23 – Chargement Pyfunc universel**  
Charger un modèle via Pyfunc standardise l’interface d'appel : tous les modèles, quel que soit leur framework, sont utilisables via une simple méthode `predict()`.

---

**Code 24 – Import modèle existant**  
Importer un modèle déjà entraîné dans MLflow permet d'intégrer des historiques extérieurs, de centraliser les assets et de rendre MLflow comme point unique de vérité.

---

**Code 25 – Script d’expérience complet**  
Structurer un script d’entraînement complet (préparation, entraînement, évaluation, log) pose les bases d’une approche professionnelle, prête pour la production.

---

**Code 26 – Projet MLflow paramétré**  
Utiliser MLflow Projects avec paramètres (`MLproject`) permet de transformer des scripts en expériences réutilisables, paramétrables et exécutables sur différents environnements.

---

**Code 27 – Diagnostic MLflow**  
`mlflow doctor` analyse l’installation pour détecter automatiquement des problèmes de version, de configuration réseau, ou de dépendances, évitant ainsi des erreurs difficiles à diagnostiquer.

---

**Code 28 – Gestion avancée des artefacts**  
Grâce aux commandes CLI (`mlflow artifacts`), il est possible de manipuler les fichiers produits par les runs : téléchargement, rechargement, modification, ou archivage.

---

**Code 29 – Gestion avancée des expériences et runs**  
Avec la CLI (`mlflow experiments`, `mlflow runs`), on peut créer, renommer, supprimer, restaurer, et lister des expériences ou des runs, offrant un contrôle fin sans dépendre de l’interface web.

