# Tutoriel Étape par Étape pour Apprendre les Widgets avec Streamlit

Ce tutoriel vous guidera pour créer une application Streamlit en utilisant différents widgets comme les boutons, les cases à cocher, les boutons radio, les listes déroulantes, les curseurs, les champs de texte et les téléversements de fichiers.

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

1. Créez un fichier Python, par exemple `widgets_app.py`, dans votre dossier de projet.

### Étape 4 : Utilisation des Widgets

**Bouton**

1. Ouvrez `widgets_app.py` et écrivez le code suivant pour afficher un bouton :

```python
import streamlit as st

st.title('Input Widgets')

# Button
st.header('Button')
button = st.button('Button')  # return True or False
if button:
    st.write('You pressed the Button')
```

2. Pour tester, ouvrez votre terminal (avec l'environnement virtuel activé) et exécutez :

```bash
streamlit run widgets_app.py
```

**Case à Cocher**

1. Ajoutez une case à cocher avec du texte conditionnel :

```python
# Checkbox (Toggle Button)
st.header('Checkbox')
checkbox = st.checkbox("Do you want to agree?")  # return bool (True or False)
if checkbox:
    st.write('You checked the box')
else:
    st.write('You unchecked the box')
```

2. Enregistrez et testez.

**Bouton Radio**

1. Ajoutez des boutons radio pour sélectionner une option parmi plusieurs :

```python
st.header('Radio Button')
options = ("India", "USA", "UK", "Australia")
radio_button = st.radio("What is your favorite country", options, index=2)  # return an element in a list/tuple
st.write('Your favorite country is', radio_button)
```

2. Enregistrez et testez.

**Liste Déroulante**

1. Ajoutez une liste déroulante pour sélectionner une option :

```python
# Select Box
st.header('Select Box')
options = ('Email', 'Phone', 'WhatsApp')
select_box = st.selectbox('How would you like to contact', options, index=1)
st.write('Your preferred mode of communication is', select_box)
```

2. Enregistrez et testez.

**Curseur**

1. Ajoutez un curseur pour sélectionner une valeur numérique :

```python
# Slider
st.header('Slider')
slider_range = st.slider('How old are you?', min_value=1, max_value=100, step=1, value=20)
st.write('Your age is', slider_range)
```

2. Enregistrez et testez.

**Champs de Texte**

1. Ajoutez des champs de texte pour entrer du texte et des nombres :

```python
# Text Inputs
st.header('Text Inputs')
name = st.text_input('Enter your Name')
st.write('Your name is', name)

age = st.number_input('Enter your age', min_value=1, max_value=100, step=1, value=25)
st.write('Your age is', age)
```

2. Enregistrez et testez.

**Téléversement de Fichiers**

1. Ajoutez une fonctionnalité de téléversement de fichiers :

```python
# Upload File
st.header('File Upload')
uploaded_file = st.file_uploader('Choose a File')

if uploaded_file is not None:
    st.success('File uploaded successfully')
    details = {'filename': uploaded_file.name, 'filetype': uploaded_file.type, 'filesize (bytes)': uploaded_file.size}
    st.json(details)
    
    # save the file
    path = os.path.join('./upload', uploaded_file.name)
    with open(path, mode='wb') as f:
        f.write(uploaded_file.getbuffer())
        st.success('File saved successfully')
```

2. Assurez-vous que le dossier `upload` existe dans votre projet.
3. Enregistrez et testez.

### Code Complet

Voici le code complet pour le fichier `widgets_app.py` :

```python
import streamlit as st
import os

st.title('Input Widgets')

# Button
st.header('Button')
button = st.button('Button')  # return True or False
if button:
    st.write('You pressed the Button')

# Checkbox (Toggle Button)
st.header('Checkbox')
checkbox = st.checkbox("Do you want to agree?")  # return bool (True or False)
if checkbox:
    st.write('You checked the box')
else:
    st.write('You unchecked the box')

st.header('Radio Button')
# Radio Button
options = ("India", "USA", "UK", "Australia")
radio_button = st.radio("What is your favorite country", options, index=2)  # return an element in a list/tuple
st.write('Your favorite country is', radio_button)

# Select Box
st.header('Select Box')
options = ('Email', 'Phone', 'WhatsApp')
select_box = st.selectbox('How would you like to contact', options, index=1)
st.write('Your preferred mode of communication is', select_box)

# Slider
st.header('Slider')
slider_range = st.slider('How old are you?', min_value=1, max_value=100, step=1, value=20)
st.write('Your age is', slider_range)

# Text Inputs
st.header('Text Inputs')
name = st.text_input('Enter your Name')
st.write('Your name is', name)

age = st.number_input('Enter your age', min_value=1, max_value=100, step=1, value=25)
st.write('Your age is', age)

# Upload File
st.header('File Upload')
uploaded_file = st.file_uploader('Choose a File')

if uploaded_file is not None:
    st.success('File uploaded successfully')
    details = {'filename': uploaded_file.name, 'filetype': uploaded_file.type, 'filesize (bytes)': uploaded_file.size}
    st.json(details)
    
    # save the file
    path = os.path.join('./upload', uploaded_file.name)
    with open(path, mode='wb') as f:
        f.write(uploaded_file.getbuffer())
        st.success('File saved successfully')
```

### Évaluation Formative

#### Instructions

1. Créez un nouvel environnement virtuel et activez-le.
2. Installez Streamlit dans cet environnement.
3. Créez un fichier `widgets_app.py` et implémentez les fonctionnalités suivantes une par une, en testant à chaque étape :
   - Afficher un bouton et réagir à son clic.
   - Ajouter une case à cocher et réagir à son état.
   - Ajouter des boutons radio pour sélectionner une option.
   - Ajouter une liste déroulante pour sélectionner une option.
   - Ajouter un curseur pour sélectionner une valeur numérique.
   - Ajouter des champs de texte pour entrer du texte et des nombres.
   - Ajouter une fonctionnalité de téléversement de fichiers.
4. Soumettez le fichier `widgets_app.py` final et une capture d'écran de chaque étape testée.

#### Exercice

1. **Bouton**
   - Affichez un bouton et écrivez un message lorsqu'il est cliqué.

2. **Case à Cocher**
   - Ajoutez une case à cocher et affichez un message en fonction de son état (coché/décoché).

3. **Bouton Radio**
   - Ajoutez des boutons radio pour sélectionner un pays favori parmi plusieurs options et affichez le choix.

4. **Liste Déroulante**
   - Ajoutez une liste déroulante pour sélectionner un mode de communication préféré et affichez le choix.

5. **Curseur**
   - Ajoutez un curseur pour sélectionner une valeur d'âge et affichez cette valeur.

6. **Champs de Texte**
   - Ajoutez des champs de texte pour entrer un nom et un âge, puis affichez les valeurs entrées.

7. **Téléversement de Fichiers**
   - Ajoutez une fonctionnalité de téléversement de fichiers et affichez les détails du fichier téléversé.

### Exemple de Solution

```python
import streamlit as st
import os

st.title('Input Widgets')

# Button
st.header('Button')
button = st.button('Button')
if button:
    st.write('You pressed the Button')

# Checkbox (Toggle Button)
st.header('Checkbox')
checkbox = st.checkbox("Do you want to agree?")
if checkbox:
    st.write('You checked the box')
else:
    st.write('You unchecked the box')

st.header('Radio Button')
options = ("India", "USA", "UK", "Australia")
radio_button = st.radio("What is your favorite country", options, index=2)
st.write('Your favorite country is', radio_button)

# Select Box
st.header('Select Box')
options = ('Email', 'Phone', 'WhatsApp')
select_box = st.selectbox('How would you like to contact', options, index=1)
st.write('Your preferred mode of communication is', select_box)

# Slider
st.header('Slider')
slider_range = st.slider('How old are you?', min_value=1, max_value=100, step=1, value=20)
st.write('Your age is', slider_range)

# Text Inputs
st.header('Text Inputs')
name = st.text_input('Enter your Name')
st.write('Your name is', name)

age = st.number_input('Enter your age', min_value=1, max_value=100, step=1, value=25)
st.write('Your age is', age)

# Upload File
st.header('File Upload')
uploaded_file = st.file_uploader('Choose a File')

if uploaded_file is not None:
    st.success('File uploaded successfully')
    details = {'filename': uploaded_file.name, 'filetype': uploaded_file.type, 'filesize (bytes)': uploaded_file.size}
    st.json(details)
    
    # save the file
    path = os.path.join('./upload', uploaded_file.name)
    with open(path, mode='wb') as f:
        f.write(uploaded_file.getbuffer())
        st.success('File saved successfully')
```
