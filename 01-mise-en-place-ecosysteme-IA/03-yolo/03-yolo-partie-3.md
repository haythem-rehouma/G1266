# (*sur VM*) 
#Développer une Application Web de Détection d'Objets avec Streamlit et YOLO

Ce tutoriel vous guidera pour créer une application web utilisant Streamlit et YOLO pour la détection d'objets. Nous allons procéder étape par étape pour configurer l'environnement, créer les fichiers nécessaires et implémenter les fonctionnalités, en ajoutant des commentaires détaillés pour chaque partie du code.

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

### Étape 2 : Installation des Dépendances

1. Avec l'environnement virtuel activé, installez Streamlit et les autres dépendances nécessaires :

```bash
pip install streamlit opencv-python-headless pyyaml numpy streamlit-webrtc
```

### Étape 3 : Création de la Structure du Projet

Créez la structure suivante pour votre projet :

```
WEBAPP/
├── images/
│   ├── about.png
│   ├── camera.png
│   ├── home.png
│   └── object.png
├── models/
│   ├── best.onnx
│   └── data.yaml
├── pages/
│   ├── 1_YOLO_for_image.py
│   ├── 2_YOLO_webrtc.py
│   ├── 3_About.py
├── Home.py
└── yolo_predictions.py
```

### Étape 4 : Configuration des Fichiers

#### Fichier `models/data.yaml`

```yaml
train: data_images/train
val: data_images/test
nc: 20
names: [
  'person', 'car', 'chair', 'bottle', 'pottedplant', 'bird', 'dog', 'sofa',
  'bicycle', 'horse', 'boat', 'motorbike', 'cat', 'tvmonitor', 'cow', 'sheep',
  'aeroplane', 'train', 'diningtable', 'bus'
]
```

### Étape 5 : Implémentation du Fichier de Prédictions YOLO

#### Fichier `yolo_predictions.py`

```python
import cv2  # OpenCV pour le traitement d'images
import numpy as np  # Numpy pour les opérations sur les tableaux
import yaml  # PyYAML pour lire le fichier YAML
from yaml.loader import SafeLoader  # Chargement sécurisé du fichier YAML

class YOLO_Pred():
    def __init__(self, onnx_model, data_yaml):
        # Charger les données du fichier YAML
        with open(data_yaml, mode='r') as f:
            data_yaml = yaml.load(f, Loader=SafeLoader)

        # Extraire les noms des classes et le nombre de classes
        self.labels = data_yaml['names']
        self.nc = data_yaml['nc']
        
        # Charger le modèle YOLO à partir du fichier ONNX
        self.yolo = cv2.dnn.readNetFromONNX(onnx_model)
        self.yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.yolo.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    def predictions(self, image):
        # Obtenir la taille de l'image
        row, col, d = image.shape
        
        # Convertir l'image en une image carrée
        max_rc = max(row, col)
        input_image = np.zeros((max_rc, max_rc, 3), dtype=np.uint8)
        input_image[0:row, 0:col] = image
        
        # Préparer l'image pour le modèle YOLO
        INPUT_WH_YOLO = 640
        blob = cv2.dnn.blobFromImage(input_image, 1/255, (INPUT_WH_YOLO, INPUT_WH_YOLO), swapRB=True, crop=False)
        self.yolo.setInput(blob)
        
        # Obtenir les prédictions du modèle YOLO
        preds = self.yolo.forward()
        
        # Filtrer les prédictions basées sur la confiance et le score de probabilité
        detections = preds[0]
        boxes = []
        confidences = []
        classes = []

        # Dimensions de l'image
        image_w, image_h = input_image.shape[:2]
        x_factor = image_w / INPUT_WH_YOLO
        y_factor = image_h / INPUT_WH_YOLO

        for i in range(len(detections)):
            row = detections[i]
            confidence = row[4]
            if confidence > 0.4:
                class_score = row[5:].max()
                class_id = row[5:].argmax()
                if class_score > 0.25:
                    cx, cy, w, h = row[0:4]
                    left = int((cx - 0.5 * w) * x_factor)
                    top = int((cy - 0.5 * h) * y_factor)
                    width = int(w * x_factor)
                    height = int(h * y_factor)
                    box = np.array([left, top, width, height])

                    confidences.append(confidence)
                    boxes.append(box)
                    classes.append(class_id)

        # Conversion des listes en tableaux numpy
        boxes_np = np.array(boxes).tolist()
        confidences_np = np.array(confidences).tolist()
        
        # Application de la suppression non maximale (NMS) pour supprimer les détections redondantes
        index = np.array(cv2.dnn.NMSBoxes(boxes_np, confidences_np, 0.25, 0.45)).flatten()

        # Dessiner les boîtes de détection sur l'image
        for ind in index:
            x, y, w, h = boxes_np[ind]
            bb_conf = int(confidences_np[ind] * 100)
            classes_id = classes[ind]
            class_name = self.labels[classes_id]
            colors = self.generate_colors(classes_id)
            text = f'{class_name}: {bb_conf}%'
            cv2.rectangle(image, (x, y), (x + w, y + h), colors, 2)
            cv2.rectangle(image, (x, y - 30), (x + w, y), colors, -1)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 0), 1)

        return image

    def generate_colors(self, ID):
        np.random.seed(10)
        colors = np.random.randint(100, 255, size=(self.nc, 3)).tolist()
        return tuple(colors[ID])
```

### Étape 6 : Implémentation des Pages de l'Application

#### Fichier `pages/1_YOLO_for_image.py`

```python
import streamlit as st  # Importer Streamlit pour créer l'application web
from yolo_predictions import YOLO_Pred  # Importer la classe YOLO_Pred pour les prédictions
from PIL import Image  # PIL pour manipuler les images
import numpy as np  # Numpy pour les opérations sur les tableaux

# Configurer la page avec un titre, une disposition large et une icône
st.set_page_config(page_title="YOLO Object Detection", layout='wide', page_icon='./images/object.png')
st.header('Get Object Detection for any Image')  # Afficher un en-tête
st.write('Please Upload Image to get detections')  # Afficher une instruction

# Charger le modèle YOLO avec un spinner pour indiquer que quelque chose se passe
with st.spinner('Please wait while your model is loading'):
    yolo = YOLO_Pred(onnx_model='./models/best.onnx', data_yaml='./models/data.yaml')

def upload_image():
    # Fonction pour téléverser une image
    image_file = st.file_uploader(label='Upload Image')
    if image_file is not None:
        size_mb = image_file.size / (1024 ** 2)
        file_details = {"filename": image_file.name, "filetype": image_file.type, "filesize": "{:,.2f} MB".format(size_mb)}
        if file_details['filetype'] in ('image/png', 'image/jpeg'):
            st.success('VALID IMAGE file type (png or jpeg)')
            return {"file": image_file, "details": file_details}
        else:
            st.error('INVALID Image file type')
            st.error('Upload only png, jpg, jpeg')
            return None

def main():
    object = upload_image()  # Appeler la fonction pour téléverser l'image
    if object:
        prediction = False  # Initialiser la variable de prédiction
        image_obj = Image.open(object['file'])  # Ouvrir l'image téléversée
        col1, col2 = st.columns(2)  # Créer deux colonnes pour l'affichage
        with col1:
            st.info('Preview of Image')  # Afficher un aperçu de l'image
            st.image(image

_obj)
        with col2:
            st.subheader('Check below for file details')  # Afficher les détails du fichier
            st.json(object['details'])
            button = st.button('Get Detection from YOLO')  # Bouton pour obtenir les détections
            if button:
                with st.spinner("Getting objects from image. please wait"):
                    image_array = np.array(image_obj)  # Convertir l'image en tableau numpy
                    pred_img = yolo.predictions(image_array)  # Obtenir les prédictions du modèle YOLO
                    pred_img_obj = Image.fromarray(pred_img)  # Convertir le tableau numpy en image
                    prediction = True  # Mettre à jour la variable de prédiction
        if prediction:
            st.subheader("Predicted Image")  # Afficher l'image prédite
            st.caption("Object detection from YOLO V5 model")
            st.image(pred_img_obj)

if __name__ == "__main__":
    main()  # Exécuter la fonction principale
```

#### Fichier `pages/2_YOLO_webrtc.py`

```python
import streamlit as st  # Importer Streamlit pour créer l'application web
from streamlit_webrtc import webrtc_streamer  # Importer webrtc_streamer pour le streaming vidéo
import av  # Bibliothèque pour manipuler les flux vidéo
from yolo_predictions import YOLO_Pred  # Importer la classe YOLO_Pred pour les prédictions

# Charger le modèle YOLO
yolo = YOLO_Pred('./models/best.onnx', './models/data.yaml')

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")  # Convertir le frame en tableau numpy
    pred_img = yolo.predictions(img)  # Obtenir les prédictions du modèle YOLO
    return av.VideoFrame.from_ndarray(pred_img, format="bgr24")  # Retourner le frame prédit

# Configurer le streaming vidéo
webrtc_streamer(key="example", video_frame_callback=video_frame_callback, media_stream_constraints={"video": True, "audio": False})
```

#### Fichier `pages/3_About.py`

Ce fichier peut être vide ou contenir des informations sur l'application.

### Étape 7 : Implémentation de la Page d'Accueil

#### Fichier `Home.py`

```python
import streamlit as st  # Importer Streamlit pour créer l'application web

# Configurer la page avec un titre, une disposition large et une icône
st.set_page_config(page_title="Home", layout='wide', page_icon='./images/home.png')
st.title("YOLO V5 Object Detection App")  # Afficher le titre de la page
st.caption('This web application demonstrates Object Detection')  # Afficher une légende

# Afficher le contenu principal
st.markdown("""
### This App detects objects from Images
- Automatically detects 20 objects from image
- [Click here for App](/YOLO_for_image/)  

Below are the objects that our model will detect:
1. Person
2. Car
3. Chair
4. Bottle
5. Sofa
6. Bicycle
7. Horse
8. Boat
9. Motorbike
10. Cat
11. TV Monitor
12. Cow
13. Sheep
14. Aeroplane
15. Train
16. Dining Table
17. Bus
18. Potted Plant
19. Bird
20. Dog 
""")
```
