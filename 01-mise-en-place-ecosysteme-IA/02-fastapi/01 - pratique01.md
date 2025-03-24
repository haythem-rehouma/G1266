# Tutoriel complet : API de calculatrice avec FastAPI et Swagger UI

Nous allons créer une API de calculatrice simple avec FastAPI qui inclut des opérations d'addition, de soustraction, de multiplication et de division, ainsi que la documentation interactive générée par Swagger UI.




## Créer et gérer un environnement virtuel Python appelé `monfastapi` :

```bash
cd mon_projet
python -m venv monfastapi
monfastapi\Scripts\activate
python -- version
pip install fastapi uvicorn
deactivate
```

Ces commandes :

1. Naviguent vers le dossier de votre projet.
2. Créent l'environnement virtuel `monfastapi`.
3. Activent l'environnement.
4. Installent FastAPI et Uvicorn.
5. Désactivent l'environnement. 

Vous pouvez réactiver l'environnement plus tard en utilisant :
```bash
monfastapi\Scripts\activate
```


### Alternative pour python 3.9


```bash
cd mon_projet_2
python3.9 -m venv monfastapi
monfastapi\Scripts\activate
python -- version
pip install fastapi uvicorn
deactivate
```

#### Étape 1 : Installation de FastAPI et Uvicorn


Commencez par installer FastAPI et Uvicorn. Exécutez les commandes suivantes dans votre terminal :

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

#### Étape 2 : Créer le fichier principal de l'application

Créez un fichier `main.py` et ajoutez le code suivant pour définir les points de terminaison de l'API :

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Calculator API"}

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
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": a / b}
```

#### Étape 3 : Lancer l'application

Pour démarrer votre application, utilisez la commande suivante :

```bash
uvicorn main:app --reload
```

L'application sera accessible sur `http://127.0.0.1:8000`.

#### Étape 4 : Accéder à Swagger UI

Swagger UI est une interface web interactive qui permet de tester votre API. Pour y accéder :

1. Ouvrez votre navigateur.
2. Rendez-vous à l'URL `http://127.0.0.1:8000/docs`.

# http://127.0.0.1:8000/docs
#### Étape 5 : Utilisation de Swagger UI

Une fois sur la page de documentation, vous verrez une liste des points de terminaison disponibles.

1. **Point de terminaison principal** : `GET /`
   - Description : Affiche un message de bienvenue.
   - URL : `http://127.0.0.1:8000/`
   - Exemple : 
     - Requête : `GET /`
     - Réponse : `{"message": "Welcome to the Calculator API"}`

2. **Addition** : `GET /add`
   - Description : Additionne deux nombres.
   - Paramètres : `a` (float), `b` (float)
   - URL : `http://127.0.0.1:8000/add?a=10&b=5`
   - Exemple : 
     - Requête : `GET /add?a=10&b=5`
     - Réponse : `{"result": 15.0}`

3. **Soustraction** : `GET /subtract`
   - Description : Soustrait le second nombre du premier.
   - Paramètres : `a` (float), `b` (float)
   - URL : `http://127.0.0.1:8000/subtract?a=10&b=5`
   - Exemple : 
     - Requête : `GET /subtract?a=10&b=5`
     - Réponse : `{"result": 5.0}`

4. **Multiplication** : `GET /multiply`
   - Description : Multiplie deux nombres.
   - Paramètres : `a` (float), `b` (float)
   - URL : `http://127.0.0.1:8000/multiply?a=10&b=5`
   - Exemple : 
     - Requête : `GET /multiply?a=10&b=5`
     - Réponse : `{"result": 50.0}`

5. **Division** : `GET /divide`
   - Description : Divise le premier nombre par le second. Lève une exception si le diviseur est zéro.
   - Paramètres : `a` (float), `b` (float)
   - URL : `http://127.0.0.1:8000/divide?a=10&b=5`
   - Exemple : 
     - Requête : `GET /divide?a=10&b=5`
     - Réponse : `{"result": 2.0}`

#### Étape 6 : Tester l'API avec Swagger UI
- Pour accéder à Swagger , ajoutez /docs
# http://127.0.0.1:8000/docs

Pour tester chaque point de terminaison :

1. Cliquez sur un point de terminaison (par exemple, `/add`) dans Swagger UI.
2. Cliquez sur le bouton "Try it out".
3. Entrez les valeurs des paramètres nécessaires (par exemple, `a` et `b` pour `/add`).
4. Cliquez sur "Execute" pour envoyer la requête et voir la réponse directement dans l'interface.

### Conclusion

Vous avez maintenant une API de calculatrice simple avec FastAPI, et vous pouvez utiliser Swagger UI pour tester et documenter vos points de terminaison. Cette API peut être facilement étendue pour inclure des fonctionnalités supplémentaires selon vos besoins. Pour plus d'informations, consultez la [documentation officielle de FastAPI](https://fastapi.tiangolo.com/).


# Annexe 1

- /add?a=2&b=5
- /subtract?a=2&b=5
- /multiply?a=2&b=5
- /divide?a=2&b=5
