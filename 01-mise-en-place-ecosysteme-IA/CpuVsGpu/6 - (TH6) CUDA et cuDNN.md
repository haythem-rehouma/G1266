# CUDA et cuDNN 

Ce sont deux technologies développées par NVIDIA qui jouent un rôle clé dans le domaine du calcul parallèle, surtout utilisées pour l'accélération des applications de deep learning et de vision par ordinateur.

# CUDA ?
**CUDA (Compute Unified Device Architecture)** est une plateforme de calcul parallèle et un modèle de programmation inventés par NVIDIA. 
- Elle permet aux développeurs de logiciels d'utiliser les processeurs graphiques (GPU) pour le calcul général (au lieu de simplement traiter des graphiques).
- En simplifiant, CUDA permet à votre programme d'effectuer de nombreuses opérations en même temps en utilisant la puissance de traitement du GPU.
- *Analogie* : C'est comme si vous aviez une équipe de milliers de personnes travaillant simultanément sur un problème, plutôt qu'une seule.
- **Utilité:** Cette approche est particulièrement efficace pour les calculs mathématiques complexes et les tâches qui peuvent être exécutées en parallèle, comme le traitement d'images ou les opérations sur les matrices, ce qui est courant dans l'apprentissage automatique et le deep learning.

## cuDNN ?
**cuDNN (CUDA Deep Neural Network library)**, quant à elle, est une bibliothèque (un ensemble d'outils préfabriqués) qui offre des primitives hautement optimisées pour les réseaux de neurones profonds (deep learning).
- Ces primitives fournissent des fonctions standard qui sont essentielles dans le développement d'applications d'intelligence artificielle, comme la **convolution**, la **normalisation**, et les opérations de **pooling** (qui sont des blocs de construction fondamentaux des réseaux de neurones).
- Les opérations de **convolution**, la **normalisation**, et les opérations de **pooling** sont très coûteux en calcul mathématique.
- En gros, cuDNN prend beaucoup des opérations complexes et répétitives du deep learning et les simplifie, les rendant plus rapides et plus efficaces en tirant parti de la puissance de CUDA et des GPU NVIDIA. Cela permet aux chercheurs et développeurs de créer des modèles de deep learning plus rapidement et plus facilement.

En résumé, CUDA est comme avoir une énorme équipe travaillant en parallèle pour résoudre des problèmes rapidement avec l'aide de GPU, tandis que cuDNN est un ensemble d'outils spécialisés qui aide cette équipe à construire et à optimiser des modèles de deep learning de manière plus efficace.
1
