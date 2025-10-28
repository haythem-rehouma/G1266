# Tutoriel Étape par Étape pour Apprendre Streamlit avec des Environnements Virtuels

Ce tutoriel vous guidera  pour créer une application Streamlit en utilisant le module `streamlit` dans un environnement virtuel. Le but est de vous apprendre à créer un environnement virtuel, écrire du code, tester les résultats, puis continuer à écrire et tester.

#### Pré-requis
- Python installé sur votre machine.
- `virtualenv` installé (`pip install virtualenv`).

# Étape 1 : Création de l'Environnement Virtuel

1. Ouvrez votre terminal et naviguez vers le dossier où vous souhaitez créer votre projet.
2. Créez un environnement virtuel :

```bash
python -m venv myenv
```
ou


```bash
python3.7 -m venv myenv37
python3.8 -m venv myenv38
python3.9 -m venv myenv39
python3.10 -m venv myenv310
python3.11 -m venv myenv311
python3.12 -m venv myenv312
```


3. Activez l'environnement virtuel :

   - Sur Windows :

   ```bash
   myenv\Scripts\activate
   ```

   - Sur macOS/Linux :

   ```bash
   source myenv/bin/activate
   ```

### Troubleshooting en cas de problèmes

<img width="1843" height="323" alt="image" src="https://github.com/user-attachments/assets/0f3a060f-faa9-4a2d-b1e7-6e4e2b0780a4" />


> Il se peut que vous ayez des restrictions Powershell pour la première fois.

### Solution:

- Exécutez en mode admin les commandes suivantes:

  
 ```bash
 Set-ExecutionPolicy Unrestricted
 ```

ou 

 ```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
 ```


# Étape 2 : Installation de Streamlit

1. Avec l'environnement virtuel activé, installez Streamlit :

```bash
pip install streamlit
```

# Étape 3 : Création du Fichier Principal

1. Créez un fichier Python, par exemple `app.py`, dans votre dossier de projet.

# Étape 4 : Écrire et Tester le Code

**Afficher du texte simple**

1. Ouvrez `app.py` et écrivez le code suivant :

```python
import streamlit as st

st.write("Hello World")
```

2. Pour tester, ouvrez votre terminal (avec l'environnement virtuel activé) et exécutez :

```bash
streamlit run app.py
```

**Formater du texte**

1. Ajoutez les lignes suivantes pour afficher différents formats de texte :

```python
st.header("This is Header")
st.subheader("This is subheader")
st.caption('This is caption')
st.text('This is plain text')
```

2. Enregistrez et testez à nouveau avec la commande `streamlit run app.py`.

**Utiliser Markdown**

1. Ajoutez le code suivant pour afficher du texte formaté avec Markdown :

```python
st.markdown("""
# This is title
## This header
### subheader -1
#### subheader -2

simple plain text

for *italic* use asterisk
for **bold** format use two asterisk
""")
```

2. Enregistrez et testez.

# Étape 5 : Afficher des Messages de Statut

1. Ajoutez les lignes suivantes pour afficher des messages de succès, d'avertissement et d'erreur :

```python
st.success("this message display text in green background")
st.warning("this message display text in yellow background")
st.error("this message display text in red background")
```

2. Enregistrez et testez.

# Étape 6 : Afficher des Médias

**Afficher des Images**

1. Ajoutez ce code pour afficher une image :

```python
st.subheader("Display Image")

st.image('./media/mountains.webp',
         caption='mountains',
         width=300)
```

2. Assurez-vous d'avoir une image `mountains.webp` dans le dossier `media`.

3. Enregistrez et testez.

**Afficher des Vidéos**

1. Ajoutez le code suivant pour afficher une vidéo :

```python
st.subheader('Display Video')
video_file = open('./media/star.mp4',mode='rb').read()
st.video(video_file)
```

2. Assurez-vous d'avoir une vidéo `star.mp4` dans le dossier `media`.

3. Enregistrez et testez.

### Code Complet

Voici le code complet pour le fichier `app.py` :

```python
import streamlit as st

# Afficher du texte simple
st.write("Hello World")

# Formater du texte
st.header("This is Header")
st.subheader("This is subheader")
st.caption('This is caption')
st.text('This is plain text')

# Utiliser Markdown
st.markdown("""
# This is title
## This header
### subheader -1
#### subheader -2

simple plain text

for *italic* use asterisk
for **bold** format use two asterisk
""")

# Afficher des Messages de Statut
st.success("this message display text in green background")
st.warning("this message display text in yellow background")
st.error("this message display text in red background")

# Afficher des Images
st.subheader("Display Image")
st.image('./media/mountains.webp', caption='mountains', width=300)

# Afficher des Vidéos
st.subheader('Display Video')
video_file = open('./media/star.mp4',mode='rb').read()
st.video(video_file)
```

# Étape 7 : Évaluation Formative

#### Instructions

1. Créez un nouvel environnement virtuel et activez-le.
2. Installez Streamlit dans cet environnement.
3. Créez un fichier `app.py` et implémentez les fonctionnalités suivantes une par une, en testant à chaque étape :
   - Afficher du texte simple.
   - Formater du texte avec différentes méthodes.
   - Utiliser Markdown pour formater du texte.
   - Afficher des messages de succès, d'avertissement et d'erreur.
   - Afficher une image.
   - Afficher une vidéo.
4. Soumettez le fichier `app.py` final et une capture d'écran de chaque étape testée.

#### Exercice

1. **Affichage de Texte**
   - Affichez "Hello Streamlit" avec `st.write`.
   - Ajoutez un header, un subheader, une caption, et un texte simple.

2. **Markdown**
   - Utilisez `st.markdown` pour afficher un titre, un sous-titre, et du texte en italique et en gras.

3. **Messages de Statut**
   - Affichez des messages de succès, d'avertissement, et d'erreur.

4. **Médias**
   - Affichez une image et une vidéo de votre choix. Utilisez des fichiers locaux ou des liens URL.

5. **Fonctionnalités Avancées (Optionnel)**
   - Ajoutez une barre latérale avec un titre.
   - Utilisez un élément de formulaire pour obtenir une entrée utilisateur.

### Exemple de Solution

```python
import streamlit as st

# Afficher du texte simple
st.write("Hello Streamlit")

# Formater du texte
st.header("This is a Header")
st.subheader("This is a Subheader")
st.caption("This is a caption")
st.text("This is plain text")

# Utiliser Markdown
st.markdown("""
# This is a Title
## This is a Subtitle
This is *italic* text and this is **bold** text.
""")

# Afficher des Messages de Statut
st.success("This is a success message")
st.warning("This is a warning message")
st.error("This is an error message")

# Afficher des Images
st.subheader("Display Image")
st.image('path/to/your/image.jpg', caption='Sample Image', width=300)

# Afficher des Vidéos
st.subheader("Display Video")
video_file = open('path/to/your/video.mp4', 'rb').read()
st.video(video_file)

# Optionnel: Barre latérale et formulaire
st.sidebar.title("Sidebar Title")
with st.sidebar.form(key='my_form'):
    name = st.text_input('Enter your name')
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        st.write(f'Hello {name}')
```
# Exercice : 
- Ajoutez un champ pour le password dans le formulaire.
