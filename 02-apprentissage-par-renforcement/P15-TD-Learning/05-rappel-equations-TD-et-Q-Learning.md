# 1 - Équations TD-Learning

### TD(0) — Mise à jour immédiate après chaque étape

$$
V(S_t) \leftarrow (1 - \alpha) V(S_t) + \alpha \left[ R_{t+1} + \gamma V(S_{t+1}) \right]
$$

### TD(1) — Utilisation d'une récompense après une étape supplémentaire

$$
V(S_t) \leftarrow (1 - \alpha) V(S_t) + \alpha \left[ R_{t+1} + \gamma R_{t+2} + \gamma^2 V(S_{t+2}) \right]
$$

### TD(2) — Utilisation de deux étapes supplémentaires

$$
V(S_t) \leftarrow (1 - \alpha) V(S_t) + \alpha \left[ R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \gamma^3 V(S_{t+3}) \right]
$$

### TD(n) — Généralisation pour \(n\) étapes

$$
V(S_t) \leftarrow (1 - \alpha) V(S_t) + \alpha \left[ \sum_{k=1}^{n} \gamma^{k-1} R_{t+k} + \gamma^n V(S_{t+n}) \right]
$$


<br/>

# 2- Équations Q-Learning — Apprentissage des paires état-action

$$
Q(S_t, A_t) \leftarrow (1 - \alpha) Q(S_t, A_t) + \alpha \left[ R_{t+1} + \gamma \max_{a} Q(S_{t+1}, a) \right]
$$



Ces équations reformulées en utilisant **(1 - alpha)** permettent de souligner le rôle du taux d'apprentissage (*alpha*) dans l'actualisation des valeurs tout en conservant une partie de la valeur précédente.

<br/>

# 3 - Pourquoi reformuler en (1 - alpha) ?



La reformulation en (1 - alpha) des équations de mise à jour sert à clarifier l’équilibre entre les valeurs anciennes (déjà apprises) et les nouvelles informations obtenues à chaque itération dans un algorithme d'apprentissage.

### Pourquoi cette reformulation est-elle utile ?

1. **Mise en perspective de l'impact de l’apprentissage** :
   - Dans les équations originales, on voit surtout la composante ajoutée grâce à \(\alpha\), mais on ne voit pas explicitement ce qui arrive à la valeur déjà apprise. En reformulant avec \(1 - \alpha\), on montre directement la part de l'information précédente qui est conservée.
   - Par exemple, dans \(Q(s, a) \leftarrow (1 - \alpha) Q(s, a) + \alpha \times \left( r + \gamma \times \max_{a'} Q(s', a') \right)\), la partie \((1 - \alpha) Q(s, a)\) montre combien de l’ancienne valeur \(Q(s, a)\) est gardée.

2. **Rendre plus intuitif le rôle de \(\alpha\)** :
   - La reformulation aide à visualiser \(\alpha\) comme un facteur de « confiance » dans la nouvelle information par rapport à l’ancienne. Par exemple :
     - Si \(\alpha = 0.1\), \(1 - \alpha = 0.9\), ce qui signifie qu'on conserve 90 % de l'ancienne information, en actualisant seulement de 10 %.
     - Si \(\alpha = 0.9\), \(1 - \alpha = 0.1\), ce qui indique une mise à jour rapide avec seulement 10 % de l'ancienne information conservée.

3. **Mise en évidence de la pondération de l’historique** :
   - En rendant explicite \((1 - \alpha)\), on illustre que l’algorithme fait un compromis entre le nouvel apprentissage et la valeur historique. Cela aide à comprendre comment l'algorithme peut « oublier » les anciennes valeurs si \(\alpha\) est élevé, ou au contraire les « mémoriser » s'il est faible.

4. **Contrôle de la stabilité** :
   - La reformulation permet de mieux contrôler la stabilité de la convergence. Si l’algorithme apprend trop vite (par exemple, avec un \(\alpha\) élevé), il risque de devenir instable. La reformulation aide donc à voir l'impact de \(\alpha\) dans le poids des valeurs passées pour assurer un apprentissage stable et progressif.

En somme, cette reformulation permet d’exprimer l'algorithme de manière plus intuitive, en montrant explicitement la part conservée et celle actualisée à chaque itération.
