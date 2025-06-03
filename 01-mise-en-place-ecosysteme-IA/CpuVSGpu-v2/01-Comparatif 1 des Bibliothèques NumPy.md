# Comparatif 1 des Bibliothèques NumPy, SciPy, scikit-learn, cuML, PyTorch

## 1. Introduction

Python dispose d’un riche écosystème de bibliothèques scientifiques. Ce document compare cinq bibliothèques clés utilisées pour les calculs numériques et l’apprentissage automatique, en distinguant celles optimisées pour **CPU** et celles capables de tirer parti du **GPU**.

---

## 2. Présentation rapide des bibliothèques

| Bibliothèque  | Domaine principal                   | Orientation matérielle | Type d’API          |
| ------------- | ----------------------------------- | ---------------------- | ------------------- |
| NumPy         | Calcul numérique et vectoriel       | CPU                    | Bas niveau          |
| SciPy         | Algèbre, FFT, intégration, stats    | CPU                    | Moyen niveau        |
| scikit-learn  | Apprentissage automatique classique | CPU                    | Haut niveau         |
| cuML (RAPIDS) | ML classique accéléré sur GPU       | GPU (CUDA)             | Haut niveau         |
| PyTorch       | Apprentissage profond et tenseurs   | CPU / GPU (CUDA, ROCm) | Moyen à haut niveau |

---

## 3. Comparaison technique détaillée

### 3.1 Niveaux d’abstraction

| Fonctionnalité           | NumPy     | SciPy        | scikit-learn               | cuML               | PyTorch             |
| ------------------------ | --------- | ------------ | -------------------------- | ------------------ | ------------------- |
| Abstraction              | Bas       | Moyen        | Élevée                     | Élevée             | Moyenne à élevée    |
| Type de programmation    | Numérique | Scientifique | ML supervisé/non supervisé | ML supervisé GPU   | Réseaux de neurones |
| Utilise NumPy en interne | —         | Oui          | Oui                        | Non (cuDF/cuArray) | Optionnel           |

---

### 3.2 Compatibilité GPU et performance

| Critère                  | NumPy | SciPy | scikit-learn | cuML          | PyTorch         |
| ------------------------ | ----- | ----- | ------------ | ------------- | --------------- |
| Exécution sur GPU        | Non   | Non   | Non          | Oui           | Oui             |
| Nécessite CUDA           | Non   | Non   | Non          | Oui           | Oui (ou ROCm)   |
| Accélération GPU         | Non   | Non   | Non          | Oui (massive) | Oui (adaptatif) |
| Optimisation automatique | Non   | Non   | Non          | Partielle     | Oui (Autograd)  |

---

### 3.3 Cas d’usage typiques

| Cas d’usage                            | Bibliothèque recommandée |
| -------------------------------------- | ------------------------ |
| Calcul vectoriel rapide                | NumPy                    |
| Résolution d’équations, intégrales     | SciPy                    |
| Régression linéaire, k-NN, SVM (CPU)   | scikit-learn             |
| Régression linéaire, PCA, KMeans (GPU) | cuML                     |
| CNN, RNN, Transformers                 | PyTorch                  |

---

### 3.4 Exemples d’API

**NumPy** :

```python
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.dot(A, A.T)
```

**SciPy** :

```python
from scipy.linalg import inv
import numpy as np
A = np.array([[1, 2], [3, 4]])
A_inv = inv(A)
```

**scikit-learn** :

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
clf = LogisticRegression().fit(X, y)
```

**cuML** :

```python
from cuml.linear_model import LinearRegression
import cudf
import cupy as cp
X = cudf.DataFrame({'x': cp.random.rand(1000)})
y = cudf.Series(cp.random.rand(1000))
model = LinearRegression().fit(X, y)
```

**PyTorch** :

```python
import torch
x = torch.tensor([[1., 2.], [3., 4.]], device='cuda')
w = torch.nn.Linear(2, 1).cuda()
y = w(x)
```

---

## 4. Limitations et avantages

| Bibliothèque | Avantages                                          | Limites                                     |
| ------------ | -------------------------------------------------- | ------------------------------------------- |
| NumPy        | Rapide sur CPU, fondation de tout l’écosystème     | Aucune prise en charge GPU                  |
| SciPy        | Outils puissants pour la science et l’optimisation | Peut être complexe à configurer             |
| scikit-learn | Simple, modulaire, très utilisé                    | Pas de GPU, modèles peu adaptés au big data |
| cuML         | Très rapide sur GPU pour ML classique              | Dépend du matériel NVIDIA                   |
| PyTorch      | Très flexible, utilisé en recherche et production  | Courbe d’apprentissage pour débutants       |

---

## 5. Cas d’intégration dans un pipeline Data Science

### Exemple : pipeline CPU

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Données synthétiques
X = np.random.rand(1000, 10)
y = (X[:, 0] > 0.5).astype(int)

X_scaled = StandardScaler().fit_transform(X)
model = LogisticRegression().fit(X_scaled, y)
```

### Exemple : pipeline GPU avec RAPIDS

```python
import cupy as cp
import cudf
from cuml.preprocessing.model_selection import train_test_split
from cuml.linear_model import LogisticRegression

X = cudf.DataFrame(cp.random.rand(1000, 10))
y = cudf.Series((X[0] > 0.5).astype(cp.int32))
X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression().fit(X_train, y_train)
```

---

## 6. Conclusion

* **NumPy + SciPy** : excellents pour les fondations scientifiques CPU.
* **scikit-learn** : idéal pour les projets classiques de machine learning avec faible à moyen volume.
* **cuML** : solution moderne pour des modèles ML classiques exécutés à grande échelle sur GPU.
* **PyTorch** : recommandé pour tous les cas de deep learning, et aussi utilisable pour du calcul tensoriel général.
