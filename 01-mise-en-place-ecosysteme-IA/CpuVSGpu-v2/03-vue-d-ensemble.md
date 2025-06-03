### Comparatif des bibliothèques scientifiques et de machine learning Python (CPU vs GPU)

Ce document fournit une vue d'ensemble complète des bibliothèques Python les plus utilisées pour les calculs scientifiques, le machine learning, et le deep learning, avec un accent sur leur compatibilité avec les CPU et GPU, leurs niveaux d'abstraction, leurs cas d'usage, et leur interopérabilité.

---

#### 1. Aperçu global des bibliothèques comparées

| Critère                         | NumPy                       | SciPy                         | scikit-learn               | cuML (RAPIDS)             | PyTorch                  |
| ------------------------------- | --------------------------- | ----------------------------- | -------------------------- | ------------------------- | ------------------------ |
| Type                            | Calcul numérique bas niveau | Calcul scientifique avancé    | Machine learning classique | ML GPU classique          | Deep learning            |
| Abstraction                     | Bas                         | Moyen                         | Élevé                      | Élevé                     | Moyen à élevé            |
| Support GPU                     | Non                         | Non                           | Non                        | Oui (CUDA NVIDIA requis)  | Oui (CUDA, ROCm)         |
| Compatibilité NumPy             | Native                      | Très forte                    | Très forte                 | Faible                    | Moyenne                  |
| Basé sur NumPy                  | Oui                         | Oui                           | Oui                        | Non                       | Non (API inspirée NumPy) |
| Domaine principal               | Maths, vecteurs             | Algèbre linéaire, optimsation | Classification, régression | SVM, PCA, kNN, clustering | CNN, LSTM, Transformers  |
| Installation via pip            | Oui                         | Oui                           | Oui                        | Partielle (selon CUDA)    | Oui                      |
| Fonctionne sans GPU             | Oui                         | Oui                           | Oui                        | Non                       | Oui                      |
| Maturité / communauté           | Très mature                 | Très mature                   | Très mature                | Moyenne, croissante       | Très large               |
| Licence                         | BSD                         | BSD                           | BSD                        | Apache 2.0                | BSD                      |
| Interopérabilité                | Standard                    | NumPy                         | NumPy, pandas              | cuDF, Dask                | TorchScript, ONNX        |
| API adaptée aux débutants       | Moyenne                     | Moyenne                       | Oui                        | Moyenne                   | Oui                      |
| Exemples de fonctions / modèles | np.array, dot, mean         | scipy.linalg, fft, ode        | SVM, kNN, arbres, PCA      | SVM, DBSCAN, t-SNE        | nn.Linear, autograd      |
| Cas d’usage typiques            | Statistiques, algèbre       | Résolution équations, FFT     | ML rapide et standard      | Pipelines ML très rapides | DL, NLP, vision, audio   |

---

#### 2. Rôles et niveaux d'abstraction

NumPy est une bibliothèque de base pour les tableaux, les calculs vectoriels, les statistiques, utilisée comme fondation de toutes les autres.

SciPy est une extension scientifique de NumPy, pour l'algèbre linéaire avancée, l'intégration, l'optimisation, les FFT.

scikit-learn est une bibliothèque de machine learning traditionnelle (SVM, forêts aléatoires, régression, clustering), très simple à utiliser.

cuML est la version GPU de scikit-learn, optimisée pour grands volumes de données avec accélération CUDA.

PyTorch est un framework de deep learning flexible, utilisable aussi pour des calculs tensoriels hors ML.

---

#### 3. Cas d’usage recommandés

| Objectif                                       | Bibliothèque recommandée |
| ---------------------------------------------- | ------------------------ |
| Algèbre linéaire, statistiques, traitement CPU | NumPy                    |
| Équations différentielles, optimisation        | SciPy                    |
| Modèles ML classiques sur CPU (rapide)         | scikit-learn             |
| Modèles ML classiques sur GPU (rapide)         | cuML                     |
| Deep learning (vision, texte, etc.)            | PyTorch                  |
| Calcul tensoriel sur GPU sans DL               | CuPy (optionnel)         |

---

#### 4. Remarques sur la compatibilité GPU

NumPy, SciPy, et scikit-learn n’ont aucun support GPU natif.

Pour passer au GPU, il faut utiliser des bibliothèques compatibles CUDA : CuPy, cuML, PyTorch.

Les performances GPU ne sont significatives que sur des volumes de données importants (tableaux > 1000x1000).

---

#### 5. Peut-on apprendre le deep learning sans GPU ?

Oui, il est possible de faire tous les travaux pratiques et les expérimentations de base sur CPU, en particulier avec des petits jeux de données (MNIST, CIFAR-10 réduit, etc.). L’exécution sera plus lente, mais l’apprentissage des concepts ne dépend pas du matériel.

Pour entraîner des modèles plus complexes ou tester des architectures de type Transformer, l’usage du GPU devient fortement recommandé.

---

#### 6. Alternatives sans GPU local

* Google Colab (gratuit) : accès à des GPU T4 ou K80 pendant 12 heures par session
* Google Colab Pro : accès prioritaire à des GPU plus puissants (V100, A100)
* Kaggle Notebooks : exécution gratuite avec GPU T4
* Paperspace, Vast.ai : location horaire de GPU NVIDIA

Ces options permettent d’utiliser des GPU à distance sans achat de matériel.

---

#### 7. Quel GPU choisir si l’on veut investir ?

| Usage prévu                     | GPU recommandé        | Mémoire VRAM | Remarques                                  |
| ------------------------------- | --------------------- | ------------ | ------------------------------------------ |
| Projets simples / budget réduit | GTX 1660 / RTX 2060   | 6–8 Go       | Suffisant pour CNN et MLP                  |
| Usage polyvalent                | RTX 3060 / 3060 Ti    | 12 Go        | Très bon compromis pour tous les projets   |
| Projets complexes / recherche   | RTX 4070 / 4080       | 12–16 Go     | Adapté aux grands modèles ou batchs longs  |
| LLMs / entraînement lourd       | RTX 4090 / A100 (pro) | 24–40 Go     | Usage professionnel ou scientifique avancé |

Un minimum de 8 Go de VRAM est recommandé pour travailler confortablement avec des modèles Transformer ou des batchs de taille moyenne.

