# (*sur Docker*) 
# Développer une Application Web de Détection d'Objets avec Streamlit et YOLO

*Objectif : Transformer le projet initial en une application web utilisant Docker-Compose et FastAPI*
### Conversion du Projet en Utilisant Docker-Compose et FastAPI

Nous allons transformer le projet de détection d'objets utilisant Streamlit et YOLO pour utiliser Docker-Compose et FastAPI. Nous allons créer une API REST avec FastAPI pour gérer les prédictions et utiliser Streamlit comme interface utilisateur pour interagir avec cette API.

### Étape 1 : Créer la Structure du Projet

Créez la structure suivante pour votre projet :

```
WEBAPP/
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── models/
│       ├── best.onnx
│       └── data.yaml
├── frontend/
│   ├── Dockerfile
│   ├── app/
│   │   ├── images/
│   │   │   ├── about.png
│   │   │   ├── camera.png
│   │   │   ├── home.png
│   │   │   └── object.png
│   │   ├── pages/
│   │   │   ├── 1_YOLO_for_image.py
│   │   │   ├── 2_YOLO_webrtc.py
│   │   │   ├── 3_About.py
│   │   ├── Home.py
│   │   └── yolo_predictions.py
├── docker-compose.yml
```

### Étape 2 : Configurer le Backend avec FastAPI

#### Fichier `backend/main.py`

```python
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import yaml
from yaml.loader import SafeLoader
from pydantic import BaseModel

app = FastAPI()

class YOLO_Pred():
    def __init__(self, onnx_model, data_yaml):
        with open(data_yaml, mode='r') as f:
            data_yaml = yaml.load(f, Loader=SafeLoader)
        self.labels = data_yaml['names']
        self.nc = data_yaml['nc']
        self.yolo = cv2.dnn.readNetFromONNX(onnx_model)
        self.yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.yolo.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    def predictions(self, image):
        row, col, d = image.shape
        max_rc = max(row, col)
        input_image = np.zeros((max_rc, max_rc, 3), dtype=np.uint8)
        input_image[0:row, 0:col] = image
        INPUT_WH_YOLO = 640
        blob = cv2.dnn.blobFromImage(input_image, 1/255, (INPUT_WH_YOLO, INPUT_WH_YOLO), swapRB=True, crop=False)
        self.yolo.setInput(blob)
        preds = self.yolo.forward()
        detections = preds[0]
        boxes = []
        confidences = []
        classes = []
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
        boxes_np = np.array(boxes).tolist()
        confidences_np = np.array(confidences).tolist()
        index = np.array(cv2.dnn.NMSBoxes(boxes_np, confidences_np, 0.25, 0.45)).flatten()
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

yolo = YOLO_Pred(onnx_model='./models/best.onnx', data_yaml='./models/data.yaml')

class PredictionResult(BaseModel):
    boxes: list
    confidences: list
    classes: list

@app.post("/predict", response_model=PredictionResult)
async def predict(file: UploadFile = File(...)):
    image = np.fromstring(await file.read(), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    pred_image = yolo.predictions(image)
    return JSONResponse({"boxes": pred_image["boxes"], "confidences": pred_image["confidences"], "classes": pred_image["classes"]})
```

#### Fichier `backend/requirements.txt`

```
fastapi
uvicorn
opencv-python-headless
numpy
pyyaml
```

#### Fichier `backend/Dockerfile`

```Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Étape 3 : Configurer le Frontend avec Streamlit

#### Fichier `frontend/app/pages/1_YOLO_for_image.py`

```python
import streamlit as st
import requests
from PIL import Image
import numpy as np
import io

st.set_page_config(page_title="YOLO Object Detection", layout='wide', page_icon='./images/object.png')
st.header('Get Object Detection for any Image')
st.write('Please Upload Image to get detections')

def upload_image():
    image_file = st.file_uploader(label='Upload Image')
    if image_file is not None:
        size_mb = image_file.size / (1024 ** 2)
        file_details = {"filename": image_file.name, "filetype": image_file.type, "filesize": "{:,.2f} MB".format(size_mb)}
        if file_details['filetype'] in ('image/png', 'image/jpeg'):
            st.success('VALID IMAGE file type (png or jpeg)')
            return image_file, file_details
        else:
            st.error('INVALID Image file type')
            st.error('Upload only png, jpg, jpeg')
            return None, None

def main():
    image_file, file_details = upload_image()
    if image_file:
        col1, col2 = st.columns(2)
        with col1:
            st.info('Preview of Image')
            image = Image.open(image_file)
            st.image(image)
        with col2:
            st.subheader('Check below for file details')
            st.json(file_details)
            button = st.button('Get Detection from YOLO')
            if button:
                with st.spinner("Getting objects from image. please wait"):
                    image_array = np.array(image)
                    image_bytes = io.BytesIO()
                    image.save(image_bytes, format=image.format)
                    files = {'file': image_bytes.getvalue()}
                    response = requests.post("http://backend:8000/predict", files=files)
                    pred_image = Image.open(io.BytesIO(response.content))
                    st.subheader("Predicted Image")
                    st.caption("Object detection from YOLO model")
                    st.image(pred_image)

if __name__ == "__main__":
    main()
```

#### Fichier `frontend/app/pages/2_YOLO_webrtc.py`

```python
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import requests
import av
import numpy as np

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    _, img_encoded = cv2.imencode('.jpg', img)
    response = requests.post("http://backend:8000/predict", files={'file': img_encoded.tobytes()})
    pred_img = np.array(Image.open(io.BytesIO(response.content)))
    return av.VideoFrame.from_ndarray(pred_img, format="bgr24")

webrtc_streamer(key="example", video_frame_callback=video_frame_callback, media_stream_constraints={"video": True, "audio": False})
```

#### Fichier `frontend/app/pages/3_About.py`

Ce fichier peut être vide ou contenir des informations sur l'application.

#### Fichier `frontend/app/Home.py`

```python


import streamlit as st

st.set_page_config(page_title="Home", layout='wide', page_icon='./images/home.png')
st.title("YOLO V5 Object Detection App")
st.caption('This web application demonstrates Object Detection')

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

#### Fichier `frontend/app/yolo_predictions.py`

Le fichier peut rester inchangé ou vous pouvez choisir de le supprimer si vous l'utilisez uniquement dans le backend.

#### Fichier `frontend/Dockerfile`

```Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app/Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Étape 4 : Configuration de Docker-Compose

#### Fichier `docker-compose.yml`

```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend/models:/app/models

  frontend:
    build:
      context: ./frontend
    ports:
      - "8501:8501"
    depends_on:
      - backend
    volumes:
      - ./frontend/app:/app/app
```

### Conclusion

Avec ces étapes, vous pouvez transformer le projet initial en une application web utilisant Docker-Compose et FastAPI. Cela permet de séparer les responsabilités entre le backend pour les prédictions de détection d'objets et le frontend pour l'interface utilisateur. Assurez-vous que tous les fichiers et dossiers nécessaires sont correctement configurés et que les chemins d'accès sont corrects pour éviter les erreurs lors de l'exécution.
