## Comparatif : Calculs scientifiques sur CPU vs GPU (NumPy, CuPy, PyTorch, cuML)

### Installation des bibliothèques GPU

```python
# Installer CuPy (pour CUDA 11.x)
!pip install -q cupy-cuda11x

# Installer cuML (RAPIDS ML GPU)
!pip install -q cuml-cu11 --extra-index-url=https://pypi.nvidia.com
```

---

### Exemple 1 – NumPy (CPU) vs CuPy (GPU)

```python
import numpy as np
import cupy as cp
import time

N = 2000

# NumPy (CPU)
start_cpu = time.time()
A_cpu = np.random.rand(N, N)
B_cpu = np.random.rand(N, N)
C_cpu = np.dot(A_cpu, B_cpu)
end_cpu = time.time()
print("Temps NumPy (CPU) :", round(end_cpu - start_cpu, 4), "secondes")

# CuPy (GPU)
cp.cuda.Device(0).synchronize()
start_gpu = time.time()
A_gpu = cp.random.rand(N, N)
B_gpu = cp.random.rand(N, N)
C_gpu = cp.dot(A_gpu, B_gpu)
cp.cuda.Device(0).synchronize()
end_gpu = time.time()
print("Temps CuPy (GPU) :", round(end_gpu - start_gpu, 4), "secondes")
```

---

### Exemple 2 – PyTorch (Deep Learning sur GPU)

```python
import torch
import torch.nn as nn
import torch.optim as optim

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = nn.Sequential(
    nn.Linear(1000, 500),
    nn.ReLU(),
    nn.Linear(500, 1)
).to(device)

X = torch.randn(10000, 1000, device=device)
y = torch.randn(10000, 1, device=device)

optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

for epoch in range(3):
    optimizer.zero_grad()
    outputs = model(X)
    loss = loss_fn(outputs, y)
    loss.backward()
    optimizer.step()
    print(f"Époque {epoch + 1} - Perte : {loss.item():.4f}")
```

---

### Exemple 3 – cuML : Régression linéaire sur GPU

```python
import cupy as cp
import cudf
from cuml.linear_model import LinearRegression

X = cp.random.rand(100000, 10)
y = 3.5 * X[:, 0] + 1.2 * X[:, 1] + cp.random.normal(0, 0.1, size=100000)

X_cudf = cudf.DataFrame(X)
y_cudf = cudf.Series(y)

model = LinearRegression()
model.fit(X_cudf, y_cudf)

pred = model.predict(X_cudf)
print("Régression terminée sur GPU avec cuML.")
```
