# Structure du Projet Final

![image](https://github.com/hrhouma/begining_IA_part1/assets/10111526/b9d2f189-f938-495d-8c2c-8fc7181473da)

## Structure du projet final avec  trois fichiers Python (`streamlit_basics.py`, `streamlit_layouts.py`, `streamlit_widgets.py`) et les fichiers médias :

```
3_STREAMLIT_PROJECT/
├── media/
│   ├── cat.jpg
│   ├── dog.jpg
│   ├── mountains.webp
│   ├── owl.jpg
│   └── star.mp4
├── upload/
│   ├── mountains.webp
│   └── star.mp4
├── fichiers-partie1.zip
├── streamlit_basics.py
├── streamlit_layouts.py
└── streamlit_widgets.py
```

# 1 - Fichier `streamlit_basics.py`

Ce fichier contiendra les bases de Streamlit, y compris le texte, les en-têtes, les sous-titres, les messages de statut et l'affichage de médias.

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
video_file = open('./media/star.mp4', 'rb').read()
st.video(video_file)
```

# 2 -  Fichier `streamlit_layouts.py`

Ce fichier contiendra la mise en page avec des barres latérales, des colonnes et des onglets.

```python
import streamlit as st

st.set_page_config(page_title="Layouts", layout='wide')
st.title('Streamlit Layout')  # display title format

# Sidebar
sidebar = st.sidebar
sidebar.write('This is my sidebar')
sidebar.header('Header in sidebar')

# Columns
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
    
# Tabs
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

# 3 - Fichier `streamlit_widgets.py`

Ce fichier contiendra les différents widgets interactifs.

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

# Radio Button
st.header('Radio Button')
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
