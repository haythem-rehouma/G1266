# Démo YOLO 7

Suivez ces étapes pour exécuter la démonstration YOLO 7 :

1. Téléchargez le fichier à partir de ce lien : https://drive.google.com/drive/folders/1ABpMLxARb2Pz0jEXkEDV99KgiL1bAzSV?usp=sharing
2. Dézippez le fichier téléchargé.
3. Naviguez jusqu'au dossier extrait.
4. Ouvrez le dossier `yolov7-python`.
5. Dans la barre de recherche en haut, remplacez le chemin par `cmd` et appuyez sur `Entrée`.
6. Pour lister les fichiers du dossier, utilisez la commande `dir`.
7. Ouvrez le projet dans Visual Studio Code en écrivant la commande `code .` (notez l'espace avant le point).
8. Ajoutez les dépendances nécessaires dans `requirements.txt`.
```plaintext
opencv-python
onnxruntime
pandas
seaborn
plotly
``` 

9. Ouvrez le terminal.
10. Installez les dépendances avec la commande `pip install -r requirements.txt`.
11. Ajouter le modèle pré entrainé yolov7.onnx dans le même dossier.
12. Pour lancer la détection, exécutez `python detection.py --weights yolov7.onnx --source data\videos\road.mp4`.
13. Appuyez sur `Q` pour quitter.
14. Exécutez `python detection.py --weights yolov7-tiny.onnx --source data\videos\road.mp4`.
15. Exécutez `python detection.py --weights yolov7.onnx --source data\images\horses.jpg`.
16. Pour utiliser la webcam comme source, exécutez `python detection.py --weights yolov7.onnx --source 0`.

# Démo YOLO 8

Suivez ces étapes pour exécuter la démonstration YOLO 8 :

1. Téléchargez le dossier à partir de ce lien : [Télécharger YOLO 8](https://drive.google.com/drive/folders/1-O2maCmNsMKwGejuyzOYix3bHOAfMFFB?usp=sharing)
2. Installez les dépendances nécessaires avec la commande `pip install -r requirements.txt`.
3. Pour lancer la détection avec la webcam, exécutez `python detection.py --model yolov8n.onnx --source 0`.

# Commandes 

# Démo YOLO 7
```ssh
pip install -r requirements.txt
python detection.py --weights yolov7.onnx --source data\videos\road.mp4
python detection.py --weights yolov7-tiny.onnx --source data\videos\road.mp4
python detection.py --weights yolov7.onnx --source data\images\horses.jpg
python detection.py --weights yolov7.onnx --source 0
```
# Démo YOLO 8
```ssh
pip install -r requirements.txt
python detection.py --model yolov8n.onnx --source data\images\horses.jpg
python detection.py --model yolov8n.onnx --source data\videos\road.mp4
python detection.py --model yolov8n.onnx --source 0
```
