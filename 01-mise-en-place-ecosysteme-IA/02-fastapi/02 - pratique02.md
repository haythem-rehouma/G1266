# Projet Calculatrice avec Streamlit et FastAPI

Ce projet consiste à créer une calculatrice web simple en utilisant Streamlit pour le frontend et FastAPI pour le backend. Le frontend permet à l'utilisateur de choisir une opération (addition, soustraction, multiplication, division) et de saisir deux nombres. Le backend effectue le calcul demandé et renvoie le résultat au frontend.

## Prérequis

- Python 3.7 ou plus récent
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt sur votre machine locale :

    ```bash
    git clone https://votre-repo-git.git
    cd votre-repo
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv myenv
    # Sous Windows
    myenv\Scripts\activate
    # Sous macOS et Linux
    source myenv/bin/activate
    ```

3. Installez les dépendances nécessaires :

    ```bash
    pip install streamlit requests fastapi uvicorn
    ```

## Démarrage du Backend

1. Créez un fichier `backend.py` avec le code suivant :

    ```python
    from fastapi import FastAPI, HTTPException

    app = FastAPI()

    @app.get("/add")
    def add(a: float, b: float):
        return {"result": a + b}

    @app.get("/subtract")
    def subtract(a: float, b: float):
        return {"result": a - b}

    @app.get("/multiply")
    def multiply(a: float, b: float):
        return {"result": a * b}

    @app.get("/divide")
    def divide(a: float, b: float):
        if b == 0:
            raise HTTPException(status_code=400, detail="Division par zéro")
        return {"result": a / b}
    ```

2. Démarrez le serveur FastAPI :

    ```bash
    uvicorn backend:app --reload
    ```

## Démarrage du Frontend

1. Créez un fichier `frontend.py` avec le code suivant :

    ```python
    import streamlit as st
    import requests

    # URL de l'API FastAPI
    API_URL = "http://127.0.0.1:8000"

    st.title("Calculatrice avec Streamlit et FastAPI")

    operation = st.selectbox("Choisissez une opération", ["Addition", "Soustraction", "Multiplication", "Division"])
    a = st.number_input("Entrez le premier nombre", format="%f")
    b = st.number_input("Entrez le deuxième nombre", format="%f")

    if st.button("Calculer"):
        if operation == "Addition":
            response = requests.get(f"{API_URL}/add", params={"a": a, "b": b})
        elif operation == "Soustraction":
            response = requests.get(f"{API_URL}/subtract", params={"a": a, "b": b})
        elif operation == "Multiplication":
            response = requests.get(f"{API_URL}/multiply", params={"a": a, "b": b})
        elif operation == "Division":
            response = requests.get(f"{API_URL}/divide", params={"a": a, "b": b})
        
        if response.status_code == 200:
            result = response.json().get("result")
            st.success(f"Le résultat de {operation.lower()} est : {result}")
        else:
            st.error(f"Erreur: {response.json().get('detail')}")
    ```

2. Lancez l'application Streamlit :

    ```bash
    streamlit run frontend.py
    ```

## Utilisation

1. Accédez à l'interface web de Streamlit en ouvrant un navigateur et en vous rendant à l'adresse indiquée par Streamlit après avoir lancé l'application (par défaut : `http://localhost:8501`).
2. Sélectionnez une opération, entrez les nombres et cliquez sur "Calculer" pour voir le résultat.

## Structure du projet

```
.
├── backend.py
├── frontend.py
├── README.md
└── myenv/
```

## Remarques

- Assurez-vous que le backend FastAPI est démarré avant de lancer le frontend Streamlit.
- Si vous rencontrez des problèmes de connexion, vérifiez que l'URL de l'API dans `frontend.py` est correcte.

# Résumé des commandes:

```python
    # Cloner le dépôt
    git clone https://github.com/hrhouma/fastapi-calculator.git
    cd fastapi-calculator

    # Créer et activer un environnement virtuel
    python -m venv myenv
    # Sous Windows
    myenv\Scripts\activate
    # Sous macOS et Linux
    source myenv/bin/activate

    # Installer les dépendances
    pip install streamlit requests fastapi uvicorn

    # Démarrer le serveur FastAPI
    uvicorn backend:app --reload

    # Démarrer l'application Streamlit
    streamlit run frontend.py
```
