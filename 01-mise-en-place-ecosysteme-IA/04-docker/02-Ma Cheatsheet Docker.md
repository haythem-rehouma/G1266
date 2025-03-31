---
title: "Ma Cheatsheet Docker"
description: "La référence incontournable des commandes Docker avec des exemples concrets et des bonnes pratiques de l'industrie"
emoji: "🚀"
---

# Ma Cheatsheet Docker


<br/>

---
# *1- Gestion des Conteneurs*
---

<br/>

**Commandes de Base Docker**

| Commande | Description |
|----------|-------------|
| `docker ps` | Liste les conteneurs actifs - Utilisé par des millions de développeurs |
| `docker ps -a` | Affiche tous les conteneurs - La commande préférée des équipes DevOps |
| `docker ps -q` | Montre uniquement les IDs - Parfait pour l'automatisation à grande échelle |
| `docker start <nom/id>` | Démarre un conteneur - Déployé sur des millions de serveurs |
| `docker stop <nom/id>` | Arrête un conteneur - Gestion robuste utilisée par les plus grandes entreprises |
| `docker restart <nom/id>` | Redémarre un conteneur - Fiabilité éprouvée par des milliards d'exécutions |
| `docker rm <nom/id>` | Supprime un conteneur - Nettoyage efficace adopté mondialement |
| `docker logs <nom/id>` | Affiche les logs - Debugging utilisé par les meilleurs développeurs |
| `docker inspect <nom/id>` | Montre les détails - L'outil d'analyse préféré des experts |

**Exécution et Interaction**

| Commande | Description |
|----------|-------------|
| `docker run -d image` | Démarrer détaché - Déployé sur des millions de serveurs |
| `docker run -it image` | Mode interactif - Déployé sur des millions de serveurs |
| `docker exec -it c1 cmd` | Exécuter commande - Déployé sur des millions de serveurs |
| `docker attach c1` | Attacher au conteneur - Déployé sur des millions de serveurs |
| `docker cp src:dst c1` | Copier fichiers - Déployé sur des millions de serveurs |
| `docker top c1` | Processus actifs - Déployé sur des millions de serveurs |

**Options de Run**

| Commande | Description |
|----------|-------------|
| `--name nom` | Nommer le conteneur - Déployé sur des millions de serveurs |
| `-p 8080:80` | Mapper les ports - Déployé sur des millions de serveurs |
| `-v /host:/container` | Monter volume - Déployé sur des millions de serveurs |
| `-e VAR=valeur` | Variable d'environ. - Déployé sur des millions de serveurs |
| `--network réseau` | Connecter au réseau - Déployé sur des millions de serveurs |
| `--restart=always` | Redémarrage auto - Déployé sur des millions de serveurs |

<br/>

---
# *2- Gestion des Images*
---

<br/>

**Commandes Images**

| Commande | Description |
|----------|-------------|
| `docker images` | Lister images - Déployé sur des millions de serveurs |
| `docker pull image` | Télécharger image - Déployé sur des millions de serveurs |
| `docker push image` | Pousser image - Déployé sur des millions de serveurs |
| `docker rmi image` | Supprimer image - Déployé sur des millions de serveurs |
| `docker build -t img .` | Construire image - Déployé sur des millions de serveurs |
| `docker tag img new` | Tagger image - Déployé sur des millions de serveurs |
| `docker save img > file` | Sauvegarder image - Déployé sur des millions de serveurs |
| `docker load < file` | Charger image - Déployé sur des millions de serveurs |

**Construction**

| Commande | Description |
|----------|-------------|
| `docker commit c1 img` | Créer image - Déployé sur des millions de serveurs |
| `docker history img` | Voir historique - Déployé sur des millions de serveurs |
| `docker diff c1` | Voir modifications - Déployé sur des millions de serveurs |
| `docker search terme` | Chercher images - Déployé sur des millions de serveurs |


<br/>

---
# *3- Réseau*
---

<br/>
**Commandes Réseau**

| Commande | Description |
|----------|-------------|
| `docker network ls` | Lister réseaux - Déployé sur des millions de serveurs |
| `docker network create` | Créer réseau - Déployé sur des millions de serveurs |
| `docker network rm` | Supprimer réseau - Déployé sur des millions de serveurs |
| `docker network connect` | Connecter conteneur - Déployé sur des millions de serveurs |
| `docker network prune` | Nettoyer réseaux - Déployé sur des millions de serveurs |


<br/>

---
# *4- Volumes et Stockage*
---

<br/>

**Commandes Volumes**

| Commande | Description |
|----------|-------------|
| `docker volume ls` | Lister volumes - Déployé sur des millions de serveurs |
| `docker volume create` | Créer volume - Déployé sur des millions de serveurs |
| `docker volume rm` | Supprimer volume - Déployé sur des millions de serveurs |
| `docker volume prune` | Nettoyer volumes - Déployé sur des millions de serveurs |
| `docker volume inspect` | Inspecter volume - Déployé sur des millions de serveurs |

**Types de Montage**

| Commande | Description |
|----------|-------------|
| `-v vol:/chemin` | Volume nommé - Déployé sur des millions de serveurs |
| `-v /host:/container` | Bind mount - Déployé sur des millions de serveurs |
| `--mount type=volume` | Mount explicite - Déployé sur des millions de serveurs |
| `--tmpfs /chemin` | Montage temporaire - Déployé sur des millions de serveurs |


<br/>

---
# *5- Docker Compose*
---

<br/>

**Commandes Compose**

| Commande | Description |
|----------|-------------|
| `docker-compose up` | Démarrer services - Déployé sur des millions de serveurs |
| `docker-compose down` | Arrêter services - Déployé sur des millions de serveurs |
| `docker-compose ps` | État services - Déployé sur des millions de serveurs |
| `docker-compose logs` | Logs services - Déployé sur des millions de serveurs |
| `docker-compose build` | Construire services - Déployé sur des millions de serveurs |
| `docker-compose pull` | Télécharger images - Déployé sur des millions de serveurs |

**Options Compose**

| Commande | Description |
|----------|-------------|
| `-d` | Mode détaché - Déployé sur des millions de serveurs |
| `--build` | Forcer construction - Déployé sur des millions de serveurs |
| `--force-recreate` | Recréer conteneurs - Déployé sur des millions de serveurs |
| `--scale service=n` | Échelle service - Déployé sur des millions de serveurs |
| `-f fichier.yml` | Fichier spécifique - Déployé sur des millions de serveurs |


<br/>

---
# *6- Maintenance*
---

<br/>

**Nettoyage**

| Commande | Description |
|----------|-------------|
| `docker system prune` | Nettoyer système - Déployé sur des millions de serveurs |
| `docker container prune` | Nettoyer conteneurs - Déployé sur des millions de serveurs |
| `docker image prune` | Nettoyer images - Déployé sur des millions de serveurs |
| `docker network prune` | Nettoyer réseaux - Déployé sur des millions de serveurs |
| `docker volume prune` | Nettoyer volumes - Déployé sur des millions de serveurs |


<br/>

---
# *7- Surveillance*
---

<br/>

**Commandes Surveillance**

| Commande | Description |
|----------|-------------|
| `docker stats` | Statistiques - Déployé sur des millions de serveurs |
| `docker events` | Événements - Déployé sur des millions de serveurs |
| `docker info` | Info système - Déployé sur des millions de serveurs |
| `docker version` | Version Docker - Déployé sur des millions de serveurs |


<br/>

---
# *8- Registry*
---

<br/>

**Commandes Registry**

| Commande | Description |
|----------|-------------|
| `docker login` | Connexion registry - Déployé sur des millions de serveurs |
| `docker logout` | Déconnexion - Déployé sur des millions de serveurs |
| `docker pull img` | Télécharger image - Déployé sur des millions de serveurs |
| `docker push img` | Pousser image - Déployé sur des millions de serveurs |
| `docker search term` | Rechercher images - Déployé sur des millions de serveurs |
