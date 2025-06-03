##  PyTorch – Réseau de neurones simple (CPU)

```python
# Installation (optionnelle sur Colab)
# !pip install torch torchvision

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import time

# Configuration CPU
device = torch.device('cpu')

# Préparation des données MNIST
transform = transforms.Compose([transforms.ToTensor()])
train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

# Modèle MLP simple
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
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entraînement (3 époques sur CPU)
start = time.time()
for epoch in range(3):
    total_loss = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Époque {epoch+1}, Perte moyenne : {total_loss/len(train_loader):.4f}")
end = time.time()
print(f"Temps d'entraînement total (CPU) : {round(end - start, 2)} secondes")
```

---

##  TensorFlow – Réseau dense simple (CPU)

```python
# TensorFlow est déjà installé sur Colab

import tensorflow as tf
import time

# Forçage explicite sur CPU
tf.config.set_visible_devices([], 'GPU')

# Chargement de MNIST
(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 28*28).astype("float32") / 255.0

# Modèle dense (MLP)
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(784,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entraînement sur CPU
start = time.time()
model.fit(x_train, y_train, epochs=3, batch_size=64)
end = time.time()
print("Temps d'entraînement (CPU) :", round(end - start, 2), "secondes")
```

---

## ✅ Instructions Colab

1. Ouvre [https://colab.research.google.com/](https://colab.research.google.com/)
2. Colle l’un des blocs dans une cellule
3. Clique sur **Exécuter**
4. Le GPU peut être activé si besoin via `Exécution > Modifier le type d'exécution`

