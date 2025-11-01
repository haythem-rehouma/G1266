# Introduction au calcul de Pi en utilisant la méthode Monte Carlo

Commençons par un projet simple : estimer la valeur de **π** en utilisant la méthode de Monte Carlo, qui est au cœur des algorithmes d'apprentissage par renforcement sans modèle.

## Qu'est-ce que la méthode Monte Carlo ?

Une **méthode Monte Carlo** est une technique qui utilise le hasard pour résoudre des problèmes. Elle consiste à répéter des **échantillons aléatoires** et à observer la fraction des échantillons qui respectent certaines propriétés pour faire des estimations numériques.

---

## Approximons la valeur de Pi

Nous allons faire un exercice amusant où nous approchons la valeur de **π** en utilisant la méthode Monte Carlo. Nous allons placer un grand nombre de points aléatoires dans un carré de côté 2, avec :

$$
-1 < x < 1 \quad \text{et} \quad -1 < y < 1
$$

Ensuite, nous allons compter combien de points tombent à l'intérieur d’un cercle de rayon 1 centré à l’origine.

### Calcul des aires

L'aire du carré est :

$$
C = 2^2 = 4
$$

L'aire du cercle est donnée par :

$$
S = \pi \times 1^2 = \pi
$$

En divisant l'aire du cercle par celle du carré, nous obtenons :

$$
\frac{S}{C} = \frac{\pi}{4}
$$

La fraction $$\frac{S}{C}$$ peut être mesurée en comptant le nombre de points qui tombent dans le cercle par rapport au nombre total de points dans le carré. En conséquence, la valeur de **π** peut être estimée par :

$$
\pi \approx 4 \times \frac{S}{C}
$$

---

## Étapes pour estimer **π** avec la méthode Monte Carlo

Voici les étapes pour estimer la valeur de **π** avec un programme Python en utilisant la méthode Monte Carlo :

1. **Importer les modules nécessaires**, y compris `random` pour générer des nombres aléatoires et `matplotlib` pour visualiser les points dans le carré.

2. **Générer aléatoirement 1 000 points** dans le carré avec les coordonnées $$x$$ et $$y$$ comprises entre -1 et 1.

3. **Initialiser un compteur** pour compter le nombre de points qui tombent dans le cercle.

4. Pour chaque point aléatoire, calculer la distance de ce point à l'origine. Un point est à l'intérieur du cercle si sa distance est inférieure à 1

   

$$
   d = \sqrt{x^2 + y^2}
$$

   Si $$d < 1$$, le point est dans le cercle.

6. **Compter les points** qui tombent dans le cercle.

7. **Tracer tous les points** et utiliser une couleur différente pour ceux qui sont dans le cercle.

8. **Dessiner le cercle** pour une meilleure visualisation.

9. Enfin, **calculer la valeur de **π** en utilisant la formule précédente**.

En suivant ces étapes, vous pouvez visualiser et estimer π efficacement grâce à cette méthode intuitive et probabiliste.


# Annexe :



<img width="655" height="644" alt="image" src="https://github.com/user-attachments/assets/152eaad5-81b7-4d31-89d9-7b9515eee006" />



## Principe de la méthode

La méthode de Monte Carlo pour estimer π repose sur la génération de points aléatoires dans un carré de côté 2, centré à l'origine, et l'observation de la proportion de ces points qui tombent à l'intérieur d'un cercle inscrit de rayon 1.

## Analyse de l'image

### Répartition des points

- **Points bleus** : Représentent les points tombés à l'intérieur du cercle unitaire.
- **Points rouges** : Indiquent les points situés à l'extérieur du cercle mais à l'intérieur du carré.

### Caractéristiques du graphique

- Un cercle vert est tracé pour délimiter clairement la frontière entre les points intérieurs et extérieurs.
- Les axes s'étendent de -1.5 à 1.5 pour les coordonnées x et y, offrant une marge autour du carré unitaire.
- Une grille est présente pour faciliter la lecture des coordonnées.
- Le titre "Estimation de Pi par la méthode de Monte Carlo" résume clairement l'objectif de la simulation.

## Interprétation

La densité des points bleus par rapport à l'ensemble des points (bleus et rouges) donne une approximation visuelle du rapport entre l'aire du cercle (πr²) et celle du carré (4r²), où r est le rayon du cercle (ici, r = 1).

## Calcul de π

Pour estimer π à partir de cette simulation, on utiliserait la formule :

$$\pi \approx 4 \times \frac{\text{Nombre de points dans le cercle}}{\text{Nombre total de points}}$$

La précision de cette estimation augmente avec le nombre de points générés. Dans cette visualisation, il semble y avoir environ 1000 points au total, ce qui devrait donner une estimation raisonnablement proche de la valeur réelle de π.

## Conclusion

Cette méthode de Monte Carlo offre une approche intuitive et visuelle pour estimer π. 
Elle démontre comment des techniques probabilistes peuvent être utilisées pour résoudre des problèmes mathématiques complexes de manière approximative mais efficace. 
C'est un excellent exemple de l'application des méthodes de simulation en mathématiques et en informatique.



