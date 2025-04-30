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


<br/> 

# Annexe 1 - justification du calcul




L’objectif est d’estimer la valeur de π à l’aide d’une méthode probabiliste appelée méthode de Monte Carlo. L’idée repose sur un raisonnement géométrique simple : comparer l’aire d’un cercle inscrit à l’aire d’un carré.

On considère un carré centré à l’origine du plan, de côté 2. Cela signifie que ses coins sont situés aux points de coordonnées $(-1, -1), (-1, 1), (1, -1), (1, 1)$. À l’intérieur de ce carré, on inscrit un cercle également centré à l’origine et de rayon 1.

L’aire de ce carré est donnée par :

$$
A_{\text{carré}} = 2 \times 2 = 4
$$

L’aire du cercle inscrit est donnée par la formule classique :

$$
A_{\text{cercle}} = \pi \times r^2 = \pi \times 1^2 = \pi
$$

On observe donc que la proportion de la surface du carré occupée par le cercle est :

$$
\frac{A_{\text{cercle}}}{A_{\text{carré}}} = \frac{\pi}{4}
$$

Cette proportion peut être interprétée comme une probabilité : si l’on choisit un point au hasard dans le carré (avec une distribution uniforme), la probabilité que ce point tombe à l’intérieur du cercle est égale à $\frac{\pi}{4}$.

Dans l’implémentation Python, on génère $n$ points au hasard dans ce carré, c’est-à-dire $n$ couples $(x_i, y_i)$ avec $x_i, y_i \in [-1, 1]$. Pour chaque point, on calcule sa distance à l’origine :

$$
r_i = \sqrt{x_i^2 + y_i^2}
$$

Si $r_i \leq 1$, alors le point est à l’intérieur du cercle. On note $n_{\text{cercle}}$ le nombre de points qui vérifient cette condition.

D’un point de vue statistique, la fréquence observée des points à l’intérieur du cercle est une estimation de la probabilité réelle :

$$
\frac{n_{\text{cercle}}}{n} \approx \frac{A_{\text{cercle}}}{A_{\text{carré}}}  \approx   \frac{\pi}{4}
$$

Il suffit alors de multiplier cette estimation par 4 pour obtenir une approximation de π :

$$
\pi \approx 4 \times \frac{n_{\text{cercle}}}{n}
$$

Ainsi, la multiplication par 4 s’explique directement par le fait que le carré a une aire égale à 4, alors que le cercle inscrit a une aire égale à π. La méthode repose sur cette proportion géométrique fondamentale entre deux aires connues.


<br/>

# Annexe 2 - Pourquoi c'est du Monte-Carlo



Le nom **"Monte Carlo"** fait référence à la ville de Monte Carlo, célèbre pour ses casinos. Cette méthode porte ce nom car elle repose sur le **hasard** et l'**aléatoire**, tout comme les jeux de hasard.

La méthode de Monte Carlo désigne une **classe de techniques numériques** qui utilisent des **expériences aléatoires répétées** pour approximer des résultats déterministes, c’est-à-dire des valeurs fixes comme des intégrales, des probabilités, ou ici, la constante π.

Dans notre cas, au lieu de calculer π de manière analytique avec une formule mathématique exacte, on le **simule** en lançant des points aléatoires et en observant la proportion qui tombe dans une région géométrique (le cercle inscrit dans un carré).

On résume cette logique par :

$$
\pi \approx 4 \times \frac{n_{\text{cercle}}}{n}
$$

où :

- $n$ est le nombre total de points générés de manière aléatoire,
- $n_{\text{cercle}}$ est le nombre de points dont la distance à l’origine est inférieure ou égale à 1.

Cette proportion est une estimation **statistique** d’une valeur **géométrique connue**, basée uniquement sur des **tirages aléatoires**.

La clé qui fait que cette méthode appartient à la famille Monte Carlo est la suivante :  
on n’utilise **aucune formule analytique directe**, mais on obtient une estimation par des **simulations aléatoires répétées**, en s’appuyant sur la **loi des grands nombres**.

Plus on génère de points, plus la fréquence observée $\frac{n_{\text{cercle}}}{n}$ converge vers la probabilité réelle $\frac{\pi}{4}$, ce qui améliore la précision de l’estimation.


