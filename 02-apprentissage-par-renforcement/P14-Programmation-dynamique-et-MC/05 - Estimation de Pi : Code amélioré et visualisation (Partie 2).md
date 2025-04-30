# Estimation de π avec la méthode Monte Carlo (Code amélioré)

Ce tutoriel vous guidera à travers l'implémentation d'un script Python pour estimer la valeur de π en utilisant la méthode Monte Carlo. Nous utiliserons PyTorch pour générer des points aléatoires et matplotlib pour visualiser les résultats.

## Code Python

```python
import torch
import math
import matplotlib.pyplot as plt

# Nombre de points à générer
n_point = 1000

# Génération de points aléatoires dans le carré [-1, 1] x [-1, 1]
points = torch.rand((n_point, 2)) * 2 - 1

# Initialisation des compteurs
n_point_circle = 0
points_circle = []

# Calcul de la distance de chaque point par rapport à l'origine
for point in points:
    r = torch.sqrt(point[0] ** 2 + point[1] ** 2)
    if r <= 1:
        points_circle.append(point)
        n_point_circle += 1

# Conversion de la liste en tenseur pour l'affichage
points_circle = torch.stack(points_circle)

# Tracer tous les points
plt.plot(points[:, 0].numpy(), points[:, 1].numpy(), 'y.')

# Tracer les points dans le cercle
plt.plot(points_circle[:, 0].numpy(), points_circle[:, 1].numpy(), 'c.')

# Tracer le cercle
i = torch.linspace(0, 2 * math.pi)
plt.plot(torch.cos(i).numpy(), torch.sin(i).numpy())

# Fixer les axes pour une visualisation correcte
plt.axes().set_aspect('equal')
plt.show()

# Estimation de Pi
pi_estimated = 4 * (n_point_circle / n_point)

# Affichage de la valeur estimée de Pi
print('La valeur estimée de Pi est :', pi_estimated)

# Fonction pour estimer Pi avec plusieurs itérations
def estimate_pi_mac(n_iteration):
    n_point_circle = 0
    pi_iteration = []
    for i in range(1, n_iteration + 1):
        point = torch.rand(2) * 2 - 1
        r = torch.sqrt(point[0] ** 2 + point[1] ** 2)
        if r <= 1:
            n_point_circle += 1
        pi_iteration.append(4 * (n_point_circle / i))
    
    # Tracer l'évolution de l'estimation de Pi
    plt.plot(pi_iteration)
    plt.plot([math.pi] * n_iteration, '--')
    plt.xlabel('Itérations')
    plt.ylabel('Estimation de Pi')
    plt.title('Historique de l\'estimation')
    plt.show()

    # Afficher la dernière estimation de Pi
    print('La valeur estimée de Pi est :', pi_iteration[-1])

# Appel de la fonction avec 10 000 itérations
estimate_pi_mac(10000)
```

## Explication des étapes

1. **Génération de points aléatoires** : 
   - Nous générons 1 000 points dans un carré de côté 2 (chaque point a des coordonnées x et y comprises entre -1 et 1).
   - Les points sont stockés dans un tenseur `points`.

2. **Calcul de la distance par rapport à l'origine** :
   - Pour chaque point, nous calculons la distance à l'origine avec la formule : $$d = \sqrt{x^2 + y^2}$$
   - Si cette distance est inférieure ou égale à 1, le point est à l'intérieur du cercle.

3. **Compter les points dans le cercle** :
   - Les points qui tombent à l'intérieur du cercle sont ajoutés à une liste `points_circle` et le compteur `n_point_circle` est incrémenté.

4. **Tracer les points** :
   - Nous utilisons matplotlib pour tracer les points dans le carré en jaune, et ceux qui sont dans le cercle en cyan. Nous traçons aussi le contour du cercle pour une meilleure visualisation.

5. **Calcul de π** :
   - La valeur estimée de π est calculée par la formule : $$\pi \approx 4 \times \frac{\text{points dans le cercle}}{\text{points totaux}}$$

6. **Estimation progressive de Pi** :
   - La fonction `estimate_pi_mac` permet de répéter l'expérience plusieurs fois (ici 10 000 itérations). À chaque itération, un nouveau point est généré, et nous calculons progressivement π.

7. **Tracer l'évolution de l'estimation de Pi** :
   - Nous affichons l'évolution de l'estimation de π au fil des itérations. Plus il y a d'itérations, plus l'estimation se rapproche de la vraie valeur de π (représentée par la ligne pointillée).

## Conclusion

- La méthode Monte Carlo est une technique puissante qui permet d'estimer des valeurs en utilisant des points aléatoires et la loi des grands nombres. 
- Plus on génère de points, plus l'estimation devient précise. 
- Ce projet démontre comment cette technique peut être appliquée pour estimer π, tout en offrant une visualisation claire du processus.
