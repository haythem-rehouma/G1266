# Comment fonctionnent les méthodes de Monte Carlo pour réaliser des estimations numériques ?

Dans cette section, nous allons approfondir le fonctionnement de la méthode de Monte Carlo pour les estimations numériques, en mettant en lumière les principes fondamentaux de cette approche.

## Explication du processus

1. **Principe de base** : Nous générons des points aléatoires dans un carré de côté 2 (chaque point a des coordonnées $$x$$ et $$y$$ comprises entre -1 et 1). Les points sont alors placés dans un graphique.

2. **Lois des grands nombres (LLN)** : La méthode Monte Carlo s'appuie sur la **Loi des Grands Nombres**. Selon cette loi, plus nous répétons un grand nombre d'événements aléatoires, plus la moyenne de ces événements converge vers la valeur attendue. Dans notre cas, cela signifie que :

$$
4 \times \left( \frac{\text{points dans le cercle}}{\text{points totaux}} \right)
$$

   convergera progressivement vers la valeur réelle de **π**.

3. **Résultat attendu** : Par exemple, avec 1 000 points, nous pouvons obtenir une estimation de **π** proche de **3.156**. Avec plus d'itérations, l'estimation deviendra plus précise et se rapprochera de la vraie valeur de **π** (3.14159...).


![image](https://github.com/user-attachments/assets/331d2232-eb3d-4ff1-b678-1fd5b1cfed85)



## Améliorer l'estimation avec plus d'itérations

Nous pouvons améliorer l'estimation en augmentant le nombre d'itérations. Au lieu de 1 000 points, nous pouvons expérimenter avec **10 000 points**.

À chaque itération, un point est généré aléatoirement dans le carré. Ensuite, nous vérifions si ce point est à l'intérieur du cercle. L'estimation de **π** est calculée à chaque étape à partir du rapport entre les points dans le cercle et le nombre total de points.

Voici la fonction qui implémente ce processus :

```python
def estimate_pi_mc(n_iteration):
    n_point_circle = 0
    pi_iteration = []
    for i in range(1, n_iteration + 1):
        point = torch.rand(2) * 2 - 1
        r = torch.sqrt(point[0] ** 2 + point[1] ** 2)
        if r <= 1:
            n_point_circle += 1
        pi_iteration.append(4 * (n_point_circle / i))
    
    # Tracer l'historique de l'estimation
    plt.plot(pi_iteration)
    plt.plot([math.pi] * n_iteration, '--')
    plt.xlabel('Itérations')
    plt.ylabel('Estimation de Pi')
    plt.title('Historique de l\'estimation')
    plt.show()

    print('La valeur estimée de Pi est :', pi_iteration[-1])

# Appel de la fonction avec 10 000 itérations
estimate_pi_mc(10000)
```

## Résultat

En lançant cette fonction avec **10 000 itérations**, vous obtiendrez un graphique montrant l'évolution de l'estimation de **π** au fur et à mesure des itérations. Plus nous avons d'itérations, plus l'estimation se rapproche de la valeur réelle de **π**.

![image](https://github.com/user-attachments/assets/31516b3a-88c9-4d6b-b959-dab649ff0a33)



## Conclusion

- La méthode Monte Carlo repose sur la puissance de la **Loi des Grands Nombres**, et avec suffisamment d'itérations, elle permet d'obtenir des estimations très proches des valeurs réelles. 
- Ce type de méthode est largement utilisé en science et en ingénierie pour estimer des valeurs lorsque les calculs analytiques directs sont complexes ou impossibles.
