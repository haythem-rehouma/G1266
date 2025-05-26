# 1 - CPU vs GPU vs TPU : Quand les utiliser pour vos modèles d'apprentissage automatique ?

La différence entre le CPU, le GPU et le TPU est que le CPU gère toute la logique, les calculs et les entrées/sorties de l'ordinateur, c'est un processeur polyvalent. En comparaison, le GPU est un processeur supplémentaire pour améliorer l'interface graphique et exécuter des tâches de haute performance. Les TPU sont des processeurs personnalisés puissants conçus pour exécuter des projets réalisés sur un framework spécifique, comme TensorFlow.

- CPU : Unité Centrale de Traitement. Gère toutes les fonctions d'un ordinateur.
- GPU : Unité de Traitement Graphique. Améliore les performances graphiques de l'ordinateur.
- TPU : Unité de Traitement Tensoriel. *ASIC* personnalisé pour accélérer les projets TensorFlow.

## 2 - Résumé des caractéristiques du CPU :

- Plusieurs cœurs
- Faible latence
- Spécialisé dans le traitement sériel
- Capable d'exécuter plusieurs opérations à la fois
- Utilisation maximale des FLOPS pour les RNN (réseaux de neurones récurrents)
- Supporte les plus grands modèles grâce à sa grande capacité de mémoire
- Beaucoup plus flexible et programmable pour les calculs irréguliers (par exemple, petits lots non MatMul)

## 3 - Résumé des caractéristiques du GPU :

- Des milliers de cœurs
- Haut débit
- Spécialisé pour le traitement parallèle
- Capable d'exécuter des milliers d'opérations simultanément

## 4 - Résumé des caractéristiques des TPU :

- Matériel spécialisé pour le traitement matriciel
- Haute latence (comparée au CPU)
- Très haut débit
- Calcul avec un parallélisme extrême
- Hautement optimisé pour les grands lots et les CNN (réseaux de neurones convolutionnels)

## 5. Quand utiliser CPU, GPU ou TPU pour exécuter vos modèles d'apprentissage automatique ?

## 5.1. Nombre de cœurs:
- CPU : Plusieurs cœurs, Faible latence, Traitement sériel, Opérations simultanées limitées, Grande capacité de mémoire.
- GPU : Des milliers de Cœurs, Haut débit de données, Calcul parallèle massif, Multitâche limité, Faible mémoire.
- TPU : Charge de travail basée sur les matrices, Haute latence, Haut débit de données, Adapté aux grandes tailles de lots, Modèles de réseaux neuronaux complexes.

## 5.2. CPUs :

- Prototypes nécessitant la plus grande flexibilité
- Entraînement de modèles simples ne nécessitant pas beaucoup de temps
- Entraînement de petits modèles avec des tailles de lots effectives réduites
- Généralement écrits en C++ basés sur des opérations TensorFlow personnalisées
- Modèles avec E/S limitées ou bande passante réseau limitée du système

## 5.3. GPUs :

- Modèles trop difficiles à changer ou sources inexistantes
- Modèles avec de nombreuses opérations TensorFlow personnalisées que le GPU doit supporter
- Modèles non disponibles sur Cloud TPU
- Modèles de taille moyenne ou grande avec des tailles de lots effectives plus grandes

## 5.4. TPUs :

- Entraînement de modèles utilisant principalement des calculs matriciels
- Entraînement de modèles sans opérations TensorFlow personnalisées dans la boucle principale d'entraînement
- Entraînement de modèles nécessitant des semaines ou des mois pour se terminer
- Entraînement de modèles énormes avec de très grandes tailles de lots effectives

### Crédit : Kinnera Kiran
- https://www.linkedin.com/pulse/cpu-vs-gpu-tpu-when-use-your-machine-learning-models-bhavesh-kapil/
- https://www.linkedin.com/pulse/cpu-vs-gpu-tpu-when-use-your-machine-learning-models-bhavesh-kapil/
- https://www.linkedin.com/pulse/cpu-vs-gpu-tpu-heart-ai-karthikeyan-prakash/

# Annexe :
ASIC signifie "Application-Specific Integrated Circuit" en anglais, ce qui se traduit littéralement par "circuit intégré spécifique à une application". 
Il s'agit d'un type de circuit intégré conçu pour une application particulière, par opposition aux circuits intégrés génériques qui peuvent être programmés pour différentes fonctions. 
Les ASIC sont souvent utilisés dans les domaines où une haute performance, une efficacité énergétique et une intégration spécifique sont nécessaires, comme dans les systèmes embarqués, les télécommunications, les réseaux informatiques et les applications spécialisées telles que le minage de crypto-monnaies.
