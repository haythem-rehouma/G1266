# 1 - Concepts importants : 

La **segmentation**, le **tracking** et l'estimation de **pose** sont trois concepts de vision par ordinateur souvent utilisés dans le traitement et l'analyse des images et des vidéos.

1. **Segmentation** : C'est le processus de division d'une image en parties ou régions, souvent pour identifier et localiser des objets et frontières (lignes, courbes, etc.) dans les images. La segmentation vise à simplifier ou à changer la représentation d'une image en quelque chose de plus significatif et plus facile à analyser. Il existe plusieurs types de segmentation, comme la segmentation sémantique qui catégorise chaque pixel d'une image dans une classe, et la segmentation d'instance qui distingue différents objets de la même classe.

2. **Tracking** : Il s'agit de la détection d'objets dans le temps au sein d'une séquence vidéo. Le tracking suit les mouvements d'un ou plusieurs objets, souvent après leur détection initiale par segmentation ou par d'autres moyens de reconnaissance d'objets. Cette technique est essentielle dans des domaines tels que la surveillance vidéo, où il est nécessaire de suivre les mouvements des personnes ou des véhicules.

3. **Estimation de pose** : C'est l'identification de la position et de l'orientation d'un objet ou d'une personne dans les images ou les vidéos. Pour les êtres humains, cela peut impliquer de déterminer la disposition des membres et du corps. L'estimation de pose est largement utilisée dans les interfaces homme-machine, par exemple, pour interpréter les gestes d'un utilisateur, dans les jeux vidéo, la réalité augmentée, et dans le domaine sportif pour l'analyse de la performance.

# 2 - Résumé 1 : 

- **Segmentation**: Identifie et isole des parties d'une image pour en faciliter l'analyse.
- **Tracking**: Suit des objets ou des personnes au fil du temps dans une séquence vidéo.
- **Estimation de pose**: Détermine la configuration spatiale d'objets ou de personnes dans une image.
- **Détection d'objets**: Reconnaît et localise des objets dans une image ou une vidéo.


![image](https://github.com/hrhouma/YOLO-2/assets/10111526/2bdde992-7f39-4bf6-b2b0-04147e511715)

![image](https://github.com/hrhouma/YOLO-2/assets/10111526/0b2ff9b4-f61d-4a1d-a9f8-ad5f517add49)

![image](https://github.com/hrhouma/YOLO-2/assets/10111526/84664b61-e17a-451b-8c28-176ab6bb1691)

![image](https://github.com/hrhouma/YOLO-2/assets/10111526/b617002a-5ca5-4c68-bbbf-cdf469740d4d)

![image](https://github.com/hrhouma/YOLO-2/assets/10111526/86ec70af-ad1b-47e8-aa38-5ec66b40ee96)

![image](https://github.com/hrhouma/YOLO-2/assets/10111526/4c89d3d8-12a7-4e4d-ab8e-f16726813b40)

![image](https://github.com/hrhouma/YOLO-2/assets/10111526/e6b52b86-319a-406c-ab6c-5f6aa8c34321)

![image](https://github.com/hrhouma/YOLO-2/assets/10111526/6f115b09-765a-417b-b32b-0797a4234d62)

![image](https://github.com/hrhouma/YOLO-2/assets/10111526/450b74da-094a-422f-a07f-5396778cd715)

# 2 - Concepts importants : Introduction aux tâches de la vision par ordinateur

## section 1 : Classification d'image
**Objectif** : Comprendre le processus de catégorisation d'une image.
- Définition : La classification d'images implique d'assigner une catégorie à une image en fonction de son contenu.
- Entrée : Une image contenant un seul objet.
- Sortie : La catégorie identifiée de l'objet et sa probabilité associée.

## section 2 : Localisation
**Objectif** : Apprendre à localiser un objet à l'intérieur d'une image.
- Définition : La localisation consiste à trouver où un objet se trouve dans une image.
- Processus : Elle implique la classification et l'identification de la position de l'objet avec une boîte englobante.

## section 3 : Détection d'objets
**Objectif** : Combiner la classification et la localisation pour identifier plusieurs objets.
- Définition : La détection d'objets vise à localiser et classifier plusieurs objets à l'intérieur d'une image.
- Entrée : Une image avec un ou plusieurs objets.
- Sortie : La localisation des objets à l'aide de boîtes englobantes et la classification de chaque objet.

## section 4 : Segmentation d'image
**Objectif** : Distinguer entre la détection d'objets et la segmentation.
- Définition : La segmentation d'image est une forme avancée de détection d'objets qui fournit des informations plus détaillées.
- Différence : Contrairement à la détection d'objets qui fournit des boîtes englobantes, la segmentation offre la forme exacte de l'objet.
- Types : 
  - **Segmentation d'instance** : Marque les limites d'un objet et étiquette ses pixels.
  - **Segmentation sémantique** : Colore chaque pixel dans l'image, y compris l'arrière-plan, selon la classification.

## section 5 : YOLO (You Only Look Once)
**Objectif** : Explorer l'algorithme YOLO pour la détection et la segmentation d'objets.
- Bases de YOLO : Conçu pour la détection d'objets, offrant des résultats rapides et efficaces.
- Capacités de YOLO v7 : S'étend à la détection d'objets et à la segmentation d'instance.
- Avenir de YOLO v7 : Projets d'incorporer la segmentation sémantique.

## Conclusion
Dans cette partie, nous avons parcouru les bases des tâches de vision par ordinateur, en soulignant l'importance des différentes techniques dans le domaine. Nous avons conclu avec des informations sur l'algorithme YOLO et ses capacités en évolution.

# 3 - Résumé 3: 

- **Détection d'objets** : Reconnaît et localise des éléments spécifiques au sein d'une image ou vidéo.
- **Segmentation** : Divise une image en régions distinctes pour en simplifier l'analyse, avec des types variés comme la segmentation sémantique et d'instance.
- **Tracking** : Suit des objets ou des personnes au fil du temps dans une vidéo, utile pour la surveillance et l'analyse de mouvements.
- **Estimation de pose** : Identifie la position et l'orientation d'objets ou de personnes, utilisée pour les interactions homme-machine et l'analyse de mouvements.

