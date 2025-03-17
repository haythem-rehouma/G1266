# Projet simple utilisant TensorFlow, FastAPI pour le backend, et Streamlit pour le frontend. Le projet entraînera un modèle de classification simple avec TensorFlow et exposera une API via FastAPI pour faire des prédictions. Le frontend avec Streamlit permettra de saisir des données et d'afficher les prédictions.

# 1 - Structure du projet

```
.
├── backend.py
├── frontend.py
├── model.py
├── README.md
└── requirements.txt
```

# 2 - Fichier `model.py`

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Générer des données d'entraînement factices
def generate_data():
    X = np.random.rand(1000, 8)  # 1000 échantillons, 8 caractéristiques
    y = (X.sum(axis=1) > 4).astype(int)  # 1 si la somme des caractéristiques > 4, sinon 0
    return X, y

# Créer et entraîner un modèle simple
def train_model():
    X, y = generate_data()
    model = Sequential([
        Dense(16, activation='relu', input_shape=(8,)),
        Dense(8, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=10)
    model.save('model.h5')

if __name__ == "__main__":
    train_model()
```

# 3 - Fichier `backend.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

# Charger le modèle entraîné
model = tf.keras.models.load_model('model.h5')

# Définir la structure des données d'entrée
class PredictionInput(BaseModel):
    features: list

app = FastAPI()

@app.post("/predict")
def predict(input: PredictionInput):
    features = np.array(input.features).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": float(prediction[0, 0])}
```

# 4 -  Fichier `frontend.py`

```python
import streamlit as st
import requests

# URL de l'API FastAPI
API_URL = "http://127.0.0.1:8000"

st.title("Prédiction avec TensorFlow, FastAPI et Streamlit")

features = [st.number_input(f"Caractéristique {i+1}", format="%f") for i in range(8)]

if st.button("Prédire"):
    response = requests.post(f"{API_URL}/predict", json={"features": features})
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.success(f"La prédiction est : {prediction}")
    else:
        st.error("Erreur dans la prédiction")
```

# 5 - Fichier `requirements.txt`

```
tensorflow
fastapi
uvicorn
pydantic
streamlit
requests
```

# 6 -  Étapes

6.1. Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/hrhouma/fastapi-calculator-tensorflow-1.git
cd fastapi-calculator-tensorflow-1
```


6.2. Créez un environnement virtuel et activez-le :

```bash
python -m venv myenv
# Sous Windows
myenv\Scripts\activate
# Sous macOS et Linux
source myenv/bin/activate
```

6.3. Installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

6.4. Entraînement du modèle

1. Exécutez le script `model.py` pour entraîner et sauvegarder le modèle :

```bash
python model.py
```

6.5. Démarrage du Backend

1. Démarrez le serveur FastAPI :

```bash
uvicorn backend:app --reload
```

6.6. Démarrage du Frontend

1. Lancez l'application Streamlit :

```bash
streamlit run frontend.py
```

6.7. Utilisation

1. Accédez à l'interface web de Streamlit en ouvrant un navigateur et en vous rendant à l'adresse indiquée par Streamlit après avoir lancé l'application (par défaut : `http://localhost:8501`).
2. Entrez les valeurs des caractéristiques et cliquez sur "Prédire" pour voir la prédiction.

## Structure du projet

```
.
├── backend.py
├── frontend.py
├── model.py
├── README.md
└── requirements.txt
```

---


### Commandes

```bash
# Cloner le dépôt
git clone https://github.com/hrhouma/fastapi-calculator-tensorflow-1.git
cd fastapi-calculator-tensorflow-1

# Créer et activer un environnement virtuel
python -m venv myenv
# Sous Windows
myenv\Scripts\activate
# Sous macOS et Linux
source myenv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Entraîner et sauvegarder le modèle
python model.py

# Démarrer le serveur FastAPI
uvicorn backend:app --reload

# Démarrer l'application Streamlit
streamlit run frontend.py
```
