# 04 - Estimation de Pi : Implémentation Python simple (Partie 1)

Dans cet exercice, nous allons implémenter un script Python pour estimer la valeur de π en utilisant la méthode Monte Carlo. Nous utiliserons les bibliothèques PyTorch pour générer des points aléatoires et matplotlib pour visualiser les résultats.

## Étape 1 : Importation des bibliothèques

Commençons par importer les bibliothèques nécessaires :

```python
import torch
import math
import matplotlib.pyplot as plt
```

## Étape 2 : Génération de points aléatoires

Définissons le nombre de points à générer et créons ces points dans le carré [-1, 1] x [-1, 1] :

```python
n_point = 1000
points = torch.rand((n_point, 2)) * 2 - 1
```

## Étape 3 : Comptage des points dans le cercle

Initialisons les compteurs et calculons la distance de chaque point par rapport à l'origine :

```python
n_point_circle = 0
points_circle = []

for point in points:
    r = torch.sqrt(point[0] ** 2 + point[1] ** 2)
    if r <= 1:
        points_circle.append(point)
        n_point_circle += 1

points_circle = torch.stack(points_circle)
```

## Étape 4 : Visualisation des résultats

Traçons tous les points, en mettant en évidence ceux qui sont dans le cercle :

```python
plt.plot(points[:,0].numpy(), points[:, 1].numpy(), 'y.')
plt.plot(points_circle[:,0].numpy(), points_circle[:, 1].numpy(), 'g.')

i = torch.linspace(0, 2 * math.pi)
plt.plot(torch.cos(i).numpy(), torch.sin(i).numpy())

plt.axes().set_aspect('equal')
plt.show()
```

## Étape 5 : Estimation de π

Calculons et affichons la valeur estimée de π :

```python
pi_estimated = 4 * (n_point_circle / n_point)
print('La valeur estimée de Pi est :', pi_estimated)
```

## Explication du code

1. Nous générons 1000 points aléatoires dans un carré de côté 2, centré à l'origine.
2. Pour chaque point, nous calculons sa distance par rapport à l'origine ($$d = \sqrt{x^2 + y^2}$$). Si cette distance est inférieure ou égale à 1, le point est dans le cercle.
3. Nous utilisons matplotlib pour afficher les points générés, en coloriant différemment ceux qui tombent dans le cercle.
4. Nous traçons un cercle de rayon 1 pour montrer la zone où les points sont comptabilisés.
5. Enfin, nous estimons π en utilisant la formule : $$\pi \approx 4 \times \frac{\text{points dans le cercle}}{\text{points totaux}}$$

## Résultat

Lorsque vous exécutez ce code, vous verrez une visualisation des points dans un carré avec un cercle centré à l'origine. Le code imprimera également une estimation de π basée sur la méthode Monte Carlo.

Ce tutoriel vous a montré comment implémenter la méthode Monte Carlo pour estimer π de manière simple et visuelle. N'hésitez pas à expérimenter en modifiant le nombre de points pour voir comment cela affecte la précision de l'estimation.
