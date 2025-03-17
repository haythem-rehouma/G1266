# Tutoriel Étape par Étape pour Apprendre les Layouts avec Streamlit

Ce tutoriel vous guidera pour créer une application Streamlit en utilisant différentes dispositions comme les barres latérales, les colonnes et les onglets. Le but est de vous aider à configurer des layouts avancés tout en testant leur code à chaque étape.

#### Pré-requis
- Python installé sur votre machine.
- `virtualenv` installé (`pip install virtualenv`).

### Étape 1 : Création de l'Environnement Virtuel

1. Ouvrez votre terminal et naviguez vers le dossier où vous souhaitez créer votre projet.
2. Créez un environnement virtuel :

```bash
python -m venv myenv
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

### Étape 2 : Installation de Streamlit

1. Avec l'environnement virtuel activé, installez Streamlit :

```bash
pip install streamlit
```

### Étape 3 : Création du Fichier Principal

1. Créez un fichier Python, par exemple `layout_app.py`, dans votre dossier de projet.

### Étape 4 : Configuration de la Page

1. Ouvrez `layout_app.py` et écrivez le code suivant pour configurer la page et afficher un titre :

```python
import streamlit as st

st.set_page_config(page_title="Layouts", layout='wide')
st.title('Streamlit Layout')  # display title format
```

2. Pour tester, ouvrez votre terminal (avec l'environnement virtuel activé) et exécutez :

```bash
streamlit run layout_app.py
```

### Étape 5 : Ajout d'une Barre Latérale

1. Ajoutez une barre latérale avec du texte et un en-tête :

```python
# sidebar
sidebar = st.sidebar
sidebar.write('This is my sidebar')
sidebar.header('Header in sidebar')
```

2. Enregistrez et testez en exécutant `streamlit run layout_app.py`.

### Étape 6 : Utilisation des Colonnes

1. Ajoutez des colonnes pour organiser le contenu :

```python
# columns
col1, col2, col3 = st.columns(3)
with col1:
    st.write('This is column -1')
    st.image('./media/cat.jpg')
    
with col2:
    st.write('This is column -2')
    st.image('./media/dog.jpg')
    
with col3:
    st.write('This is column -3')
    st.image('./media/owl.jpg')
```

2. Assurez-vous d'avoir des images `cat.jpg`, `dog.jpg`, et `owl.jpg` dans le dossier `media`.

3. Enregistrez et testez.

### Étape 7 : Ajout d'Onglets

1. Ajoutez des onglets pour organiser le contenu :

```python
# tabs
st.header('Display in Tabs')
tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])

with tab1:
    st.write('You are in Cat Tab')
    st.image('./media/cat.jpg')
with tab2:
    st.write('You are in Dog Tab')
    st.image('./media/dog.jpg')
with tab3:
    st.write('You are in Owl Tab')
    st.image('./media/owl.jpg')
```

2. Enregistrez et testez.

### Code Complet

Voici le code complet pour le fichier `layout_app.py` :

```python
import streamlit as st

st.set_page_config(page_title="Layouts", layout='wide')
st.title('Streamlit Layout')  # display title format

# sidebar
sidebar = st.sidebar
sidebar.write('This is my sidebar')
sidebar.header('Header in sidebar')

# columns
col1, col2, col3 = st.columns(3)
with col1:
    st.write('This is column -1')
    st.image('./media/cat.jpg')
    
with col2:
    st.write('This is column -2')
    st.image('./media/dog.jpg')
    
with col3:
    st.write('This is column -3')
    st.image('./media/owl.jpg')
    
# tabs
st.header('Display in Tabs')
tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])

with tab1:
    st.write('You are in Cat Tab')
    st.image('./media/cat.jpg')
with tab2:
    st.write('You are in Dog Tab')
    st.image('./media/dog.jpg')
with tab3:
    st.write('You are in Owl Tab')
    st.image('./media/owl.jpg')
```

### Évaluation Formative

#### Instructions

1. Créez un nouvel environnement virtuel et activez-le.
2. Installez Streamlit dans cet environnement.
3. Créez un fichier `layout_app.py` et implémentez les fonctionnalités suivantes une par une, en testant à chaque étape :
   - Configurer la page et afficher un titre.
   - Ajouter une barre latérale avec du texte et un en-tête.
   - Utiliser des colonnes pour organiser le contenu.
   - Ajouter des onglets pour organiser le contenu.
4. Soumettez le fichier `layout_app.py` final et une capture d'écran de chaque étape testée.

#### Exercice

1. **Configuration de la Page**
   - Configurez la page pour avoir un titre et un layout large.
   - Affichez un titre "Streamlit Layout".

2. **Barre Latérale**
   - Ajoutez une barre latérale avec un texte "This is my sidebar".
   - Ajoutez un en-tête "Header in sidebar" dans la barre latérale.

3. **Colonnes**
   - Créez trois colonnes et affichez une image et un texte dans chaque colonne.

4. **Onglets**
   - Ajoutez trois onglets ("Cat", "Dog", "Owl") et affichez une image et un texte correspondant dans chaque onglet.

5. **Fonctionnalités Avancées (Optionnel)**
   - Ajoutez des boutons dans la barre latérale pour changer dynamiquement les images affichées dans les colonnes.

### Exemple de Solution

```python
import streamlit as st

st.set_page_config(page_title="Layouts", layout='wide')
st.title('Streamlit Layout')

# sidebar
sidebar = st.sidebar
sidebar.write('This is my sidebar')
sidebar.header('Header in sidebar')

# columns
col1, col2, col3 = st.columns(3)
with col1:
    st.write('This is column -1')
    st.image('path/to/your/cat.jpg')
    
with col2:
    st.write('This is column -2')
    st.image('path/to/your/dog.jpg')
    
with col3:
    st.write('This is column -3')
    st.image('path/to/your/owl.jpg')

# tabs
st.header('Display in Tabs')
tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])

with tab1:
    st.write('You are in Cat Tab')
    st.image('path/to/your/cat.jpg')
with tab2:
    st.write('You are in Dog Tab')
    st.image('path/to/your/dog.jpg')
with tab3:
    st.write('You are in Owl Tab')
    st.image('path/to/your/owl.jpg')
```

# Exercice :

- Ajoutez des emojis
