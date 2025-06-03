
### Peut-on utiliser **PyTorch** et **TensorFlow** sans GPU pour apprendre le deep learning ?

#### Oui, **PyTorch** et **TensorFlow** fonctionnent parfaitement sur CPU.

Les deux frameworks sont conçus pour s’exécuter **soit sur CPU, soit sur GPU**, selon les besoins et les ressources disponibles. Aucune opération de deep learning n'est fondamentalement dépendante du GPU.

---

### Fonctionnement sur CPU

* **PyTorch sur CPU** :

  * Exécute tous les calculs via des bibliothèques optimisées comme **OpenMP**, **MKL**, **OpenBLAS**.
  * Les modèles peuvent être définis, entraînés et évalués sans aucune carte graphique.
  * Exemple :

    ```python
    import torch
    device = torch.device('cpu')  # explicite
    model = MyModel().to(device)
    ```

* **TensorFlow sur CPU** :

  * Utilise également les cœurs CPU via **Eigen**, **XLA**, ou **MKL-DNN**.
  * L'entraînement se fait plus lentement, mais de manière correcte.
  * Exemple :

    ```python
    import tensorflow as tf
    tf.config.set_visible_devices([], 'GPU')  # forçage CPU
    ```

---

### Limites concrètes du CPU en deep learning

| Type de tâche                     | Faisable sur CPU ?  | Remarque technique                          |
| --------------------------------- | ------------------- | ------------------------------------------- |
| Entraîner un MLP ou CNN sur MNIST | Oui                 | En quelques minutes                         |
| Entraîner ResNet sur CIFAR-10     | Oui                 | Mais cela peut durer plusieurs heures       |
| Expérimenter des architectures    | Oui                 | Idéalement avec batchs plus petits          |
| Utiliser BERT / GPT               | Oui (théoriquement) | Très lent, sauf si modèle compressé         |
| Inférence de modèles entraînés    | Oui                 | Suffisant pour démonstrations ou prototypes |

---

### Quand le GPU devient nécessaire

Le GPU est conseillé si l’on souhaite :

* Réduire le temps d'entraînement de manière significative (10× à 50× plus rapide)
* Traiter des volumes de données plus importants (ImageNet, audio, texte long)
* Entraîner des Transformers, LSTM de grande taille ou GANs
* Faire de l'expérimentation intensive (nombreuses variations d’hyperparamètres)

---

### Recommandation pratique

Il est **parfaitement possible de faire tout un cours de deep learning sur CPU** avec PyTorch ou TensorFlow, à condition de :

* Travailler sur des jeux de données modestes (MNIST, CIFAR-10, IMDB, etc.)
* Utiliser des architectures simples (MLP, CNN légers, LSTM courts)
* Limiter les tailles de batch et le nombre d’époques
* S’appuyer sur des outils gratuits comme **Google Colab** pour des tests sur GPU

