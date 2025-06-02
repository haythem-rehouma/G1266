# 1 - Installer Anaconda
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/340a2015-9f0a-4e81-bc3b-0bb3915614e9)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/aa96bd9e-c3b5-4229-88e6-28cff2ad07db) 
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/296c0983-1647-47bf-b8e1-f6d427498e08) 
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/dc5ec661-8386-48a4-b02a-965ef9099a0b)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/63556828-37e6-454e-9b31-a5eb289393f1) 
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/38904ef4-c55b-4e06-b7fe-c2dd06189154) 
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/e44e39ec-692d-4ce5-be6c-48ab0e053179)

# 2 - Installer Git
https://phoenixnap.com/kb/how-to-install-git-windows

# 3 - Installer GPU Driver
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/0e15ddf5-9165-4a99-8cec-739b1e2fcdbb)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/70d36c5a-f023-4880-8191-be2e169ce41f)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/ad43bcaa-b222-4b6c-a35c-2775cd6b9c94)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/00e2f92a-f705-44f5-b832-e09dcf82fbf2)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/2ecd3860-1369-40e4-9d2a-da5f6b0e5ec1)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/6cb147ac-0b4d-4ec2-a212-20a01be97fcb)

```ssh
cmd
nvidia-smi
```


![image](https://github.com/hrhouma/YOLO-2/assets/10111526/406c34dc-3b12-449e-a8cf-3f7c2a154aab) 
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/822a1e2b-eb8f-42bc-aa7e-b934bc274c52)

# 4 - Installer CUDA
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/d328dc38-be3c-4630-beba-b59743c61c6e)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/9e3e9796-cb28-4051-94ad-7e031224e8a6)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/c93038bb-a3ef-48fe-a963-14d1cd74f988)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/a61492ed-c2b3-4763-b505-bb107b962ce7)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/b460abc0-19e8-4054-943e-04c54d1b58f6)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/85172243-795c-4027-8ec7-f943c28a639d)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/707de5ab-b696-417d-8872-42d1bf01d54e)
![image](https://github.com/hrhouma/YOLO-2/assets/10111526/2f76a16d-26fe-4399-91c8-83768f4f92ec)

```ssh
cmd
nvcc --version
```

# 5 - Introduction au librairies PYTHON


## Une librairie, c'est quoi ?

Imaginez une librairie comme une boîte à outils. Lorsque vous commencez un projet de bricolage, vous n'avez pas besoin de fabriquer chaque outil à partir de zéro, comme un marteau ou un tournevis. À la place, vous allez à la librairie et vous empruntez les outils dont vous avez besoin.

Dans le monde de la programmation, une librairie est semblable à cette boîte à outils. C’est une collection d'outils préfabriqués, ou de "codes", que les programmeurs peuvent utiliser pour réaliser des tâches spécifiques sans avoir à réinventer la roue. Par exemple, si vous programmez un site web et que vous avez besoin de gérer les données saisies par les utilisateurs, au lieu d'écrire le code vous-même, vous pouvez utiliser une librairie qui contient déjà les fonctions nécessaires pour faire cela.

En utilisant des librairies, vous gagnez du temps, vous réduisez les erreurs potentielles, et vous bénéficiez souvent de l'expertise et des connaissances de la communauté des développeurs qui les ont créées et améliorées au fil du temps.

## Une définition d'une librairie plus technique ?

Une librairie en programmation est une collection de modules ou de fonctions prédéfinies qui fournissent des solutions à des problèmes courants ou permettent d'effectuer des tâches spécifiques. Chaque module ou fonction dans une librairie peut être considéré comme un bloc de construction que les développeurs peuvent utiliser pour construire leurs propres programmes plus efficacement, sans avoir à réécrire le code commun à partir de zéro.

Techniquement, les librairies diffèrent des frameworks. Dans le cas d'une librairie, le développeur est aux commandes du flux d'exécution du programme, appelant spécifiquement les ressources dont il a besoin quand il en a besoin. Avec un framework, en revanche, c'est le framework lui-même qui prend le contrôle, appelant le code du développeur à des points prédéfinis.

Les librairies peuvent être implémentées dans presque tous les langages de programmation et sont généralement distribuées sous forme de fichiers compilés que les développeurs peuvent lier à leurs programmes lors de la compilation ou de l'exécution. Elles peuvent couvrir un large éventail de fonctionnalités, des opérations mathématiques de base à la gestion complexe des données en passant par les interactions réseau et la visualisation graphique.

En somme, utiliser des librairies permet aux développeurs de se concentrer sur les aspects uniques et innovants de leurs projets en tirant parti des solutions standardisées pour des problèmes courants, améliorant ainsi l'efficacité du développement et la qualité du code produit.


## Librairies Python les plus utilisés en 2023 ?

**Requêtes HTTP et Développement Web :**
- Requests: Pour les requêtes HTTP simplifiées.
- FastAPI: Cadre moderne pour le développement rapide d'APIs.
- aiohttp: Client/serveur HTTP asynchrone.

**Programmation Asynchrone :**
- Asyncio: Pour l'écriture de code asynchrone avec la syntaxe async/await.

**Interfaces Graphiques Utilisateur (GUI) :**
- Tkinter: Outil standard pour créer des applications GUI en Python.

**Manipulation de Données :**
- Pandas: Pour la manipulation et l'analyse des données.

**Visualisation de Données :**
- Matplotlib: Pour créer des visualisations statiques, interactives et animées.
- Seaborn: Pour des visualisations statistiques attrayantes basées sur Matplotlib.
- Plotly: Pour des visualisations de données interactives.

**Apprentissage Automatique (Machine Learning) :**
- Scikit-Learn: Outils simples et efficaces pour l'analyse prédictive des données.
- LightGBM, XGBoost, CatBoost: Bibliothèques pour le boosting de gradient.

**Modélisation Statistique :**
- Statsmodels: Pour estimer divers modèles statistiques et réaliser des tests statistiques.

Cette liste n'est pas exhaustive.

# 6 - Les bibliothèques Python prenant en charge le GPU

Les bibliothèques Python prenant en charge le GPU sont souvent utilisées pour des calculs intensifs, comme le traitement de données volumineuses ou l'apprentissage automatique. Voici un tableau résumant quelques-unes de ces bibliothèques et leurs équivalents standard en CPU :

| CPU             | GPU              | Utilisation                                        |
|-----------------|------------------|----------------------------------------------------|
| NumPy           | CuPy             | Calcul numérique généraliste                       |
| SciPy           | CuPy/PyCUDA      | Algorithmes scientifiques et techniques            |
| Pandas          | cuDF             | Manipulation et analyse de données                 |
| Scikit-Learn    | cuML             | Apprentissage automatique                          |
| Matplotlib      | ---              | Visualisation de données (pas d'équivalent direct) |
| Seaborn         | ---              | Visualisation de données (pas d'équivalent direct) |
| Plotly          | ---              | Visualisation interactive (supporte le GPU indirectement via Dask) |
| LightGBM        | LightGBM avec support GPU | Boosting de gradient                          |
| XGBoost         | XGBoost avec support GPU  | Boosting de gradient                          |
| CatBoost        | CatBoost avec support GPU | Boosting de gradient                          |
| Statsmodels     | ---              | Modélisation statistique (pas d'équivalent direct) |
| TensorFlow      | TensorFlow avec support GPU | Réseaux de neurones profonds                  |
| PyTorch         | PyTorch avec support GPU   | Réseaux de neurones profonds                  |

Il est important de noter que certaines bibliothèques comme Matplotlib, Seaborn et Statsmodels n'ont pas d'équivalents directs en GPU car elles ne sont pas axées sur des calculs lourds où le GPU offrirait un avantage significatif. Cependant, pour les tâches de visualisation de données, le calcul des données peut être accéléré avec le GPU avant la visualisation.

Pour la visualisation interactive, Plotly peut utiliser le GPU indirectement à travers Dask pour gérer de gros volumes de données, mais le rendu final est généralement effectué sur le CPU.

Les bibliothèques d'apprentissage automatique comme LightGBM, XGBoost, et CatBoost offrent des options pour utiliser le GPU afin d'accélérer l'entraînement des modèles.

TensorFlow et PyTorch sont des bibliothèques de réseaux de neurones profonds qui ont une intégration native avec le GPU, permettant un traitement et un entraînement des modèles beaucoup plus rapides sur des données de grande taille.
