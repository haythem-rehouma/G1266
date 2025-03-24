# mini-lab 1 : Développement d'une Application de Visualisation de Données CSV avec Streamlit

**Objectif:** Développer une application avec Streamlit permettant de charger un fichier CSV, d'afficher les données, et de générer un graphique basé sur une colonne numérique sélectionnée.

# Lien des données + VIDÉO : 
- https://drive.google.com/drive/folders/17Cmg05yZFeWIC_ZCNwEGjQPB030Nk1EE?usp=sharing
- https://drive.google.com/drive/folders/1AvnBZcGnTznxmJE2sMPMkdMXK_a5gDnw?usp=sharing

# 1 - Instructions:

1. **Titre de l'application:**
   - Ajouter un titre en haut de la page indiquant "Application de Visualisation de Données CSV".

2. **Chargement du fichier CSV:**
   - Utiliser une fonction Streamlit pour permettre aux utilisateurs de charger un fichier CSV.
   - Spécifier que seuls les fichiers de type CSV sont acceptés.

![image](https://github.com/hrhouma/begining_IA_part1/assets/10111526/de4d848a-0fbd-4410-9f38-fe125421db67)


3. **Lecture et affichage des données:**
   - Lire le fichier CSV chargé.
   - Afficher un aperçu des données dans un tableau.

![image](https://github.com/hrhouma/begining_IA_part1/assets/10111526/f365ee79-7af8-4ecb-b976-b0104deb1564)

4. **Sélection de colonne pour le graphique:**
   - Permettre aux utilisateurs de sélectionner une colonne parmi celles contenant des données numériques (types `float` ou `int`).
![image](https://github.com/hrhouma/begining_IA_part1/assets/10111526/5dbb6271-e52b-4e68-b666-8e300f897b97)


5. **Génération du graphique:**
   - Générer un graphique en ligne basé sur la colonne sélectionnée.
![image](https://github.com/hrhouma/begining_IA_part1/assets/10111526/d5972913-0f0e-4d4c-9217-7a272e9116be)


6. **Gestion des erreurs et des cas particuliers:**
   - Afficher un message demandant aux utilisateurs de charger un fichier CSV si aucun fichier n'est chargé.
   - S'assurer que l'application ne plante pas en cas d'erreurs ou de fichiers incorrects.

7. **Bonus: Chargement du fichier CSV depuis la barre latérale:**
   - Utiliser une fonction Streamlit pour permettre le chargement du fichier CSV depuis la barre latérale.

# 2 - Exigences spécifiques:

1. **Afficher un message clair si aucun fichier n'est chargé.**
2. **Vérifier que le fichier CSV contient des colonnes numériques avant de permettre la sélection d'une colonne.**
3. **Gérer les erreurs potentielles lors de la lecture du fichier CSV.**
4. **Ajouter la possibilité de charger le fichier CSV depuis la barre latérale.**

# 3 - Structure attendue:

1. **Titre de l'application:**
   - Utiliser `st.title` pour afficher le titre de l'application.

2. **Chargement du fichier CSV:**
   - Utiliser `st.file_uploader` pour permettre le chargement de fichiers CSV.

3. **Lecture et affichage des données:**
   - Lire le fichier CSV chargé avec une fonction appropriée.
   - Afficher les données dans un tableau.

4. **Sélection de colonne pour le graphique:**
   - Permettre la sélection de colonnes numériques avec une fonction appropriée.

5. **Génération du graphique:**
   - Générer un graphique en ligne basé sur la colonne sélectionnée avec une fonction appropriée.

6. **Gestion des erreurs et des cas particuliers:**
   - Ajouter des conditions pour afficher des messages appropriés si aucun fichier n'est chargé ou si le fichier ne contient pas de colonnes numériques.

7. **Bonus: Chargement du fichier CSV depuis la barre latérale:**
   - Ajouter une option de chargement du fichier CSV dans la barre latérale avec une fonction appropriée.

# 4 - Critères d'évaluation:

1. **Fonctionnalité:**
   - L'application doit charger et lire correctement un fichier CSV.
   - L'application doit afficher les données du fichier CSV.
   - L'application doit permettre la sélection d'une colonne numérique pour générer un graphique.
   - L'application doit générer et afficher correctement un graphique en ligne basé sur la colonne sélectionnée.
   - L'application doit permettre le chargement du fichier CSV depuis la barre latérale (bonus).

2. **Interface utilisateur:**
   - L'application doit être intuitive et facile à utiliser.
   - Les messages d'erreur doivent être clairs et informatifs.

3. **Code:**
   - Le code doit être bien structuré et commenté.
   - Le code doit gérer les erreurs et les cas particuliers de manière appropriée.
   - Le code doit inclure l'option de chargement du fichier CSV depuis la barre latérale (bonus).

# 5 - Soumission:

- Soumettre le code source de l'application sur LÉA.
- Les fichiers soumis doivent être bien nommés et inclure des commentaires expliquant les différentes sections du code.

Bonne chance et bon développement !
