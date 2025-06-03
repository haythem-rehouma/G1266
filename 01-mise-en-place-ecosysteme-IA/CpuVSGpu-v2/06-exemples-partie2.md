##  Pré-requis pour exécuter localement sur Python 3.9

### 1. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python3.9 -m venv dl_cpu_env
source dl_cpu_env/bin/activate  # sous Windows : dl_cpu_env\\Scripts\\activate
```

### 2. Installer PyTorch (version CPU)

```bash
pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cpu
```

### 3. Installer TensorFlow (version CPU)

```bash
pip install tensorflow==2.13.0
```

> Vérifie ta version de Python avec `python --version`.
> Assure-toi d’avoir `pip` à jour : `pip install --upgrade pip`

---

## Exécution locale – PyTorch MLP sur MNIST (CPU, Python 3.9)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import time

device = torch.device('cpu')  # Aucun GPU requis

# Données MNIST
transform = transforms.Compose([transforms.ToTensor()])
train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

# Modèle
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.model = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )
    def forward(self, x):
        return self.model(x)

model = MLP().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entraînement
start = time.time()
for epoch in range(3):
    total_loss = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = loss_fn(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Époque {epoch+1}, Perte moyenne : {total_loss/len(train_loader):.4f}")
end = time.time()
print(f"Temps d'entraînement : {round(end - start, 2)} secondes")
```

---

## Exécution locale – TensorFlow MLP sur MNIST (CPU, Python 3.9)

```python
import tensorflow as tf
import time

# Chargement de MNIST
(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 28*28).astype("float32") / 255.0

# Modèle
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(784,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entraînement
start = time.time()
model.fit(x_train, y_train, epochs=3, batch_size=64)
end = time.time()
print("Temps d'entraînement :", round(end - start, 2), "secondes")
```

---

## Résultat attendu (CPU)

* Entraînement en quelques minutes seulement
* Pas besoin de carte graphique
* Parfaitement fonctionnel avec Python 3.9 sur Windows, macOS ou Linux
