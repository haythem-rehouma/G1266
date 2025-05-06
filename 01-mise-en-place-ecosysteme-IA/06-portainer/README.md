
# Définition de Portainer

**Portainer** est un outil open-source qui permet de gérer facilement des environnements Docker et Kubernetes via une interface utilisateur graphique (GUI). Il simplifie la gestion des conteneurs en fournissant une interface intuitive pour la création, l'administration, et la surveillance de conteneurs, volumes, réseaux et autres composants Docker. Plutôt que d'utiliser des lignes de commande complexes pour chaque opération, Portainer permet d'exécuter les tâches administratives plus efficacement et visuellement.

Il est particulièrement utile pour les équipes de développement ou les administrateurs système qui doivent superviser et maintenir des environnements Docker à grande échelle. Parmi ses fonctionnalités principales, on retrouve la gestion des stacks, des volumes, des images Docker, et la possibilité de visualiser l'utilisation des ressources.
# Installation de Portainer

*Pour installer et configurer Portainer avec la ligne de commande Linux, voici les étapes à suivre :*

### Prérequis :
- Docker doit être installé sur votre machine.

### Étapes :


1. **Lancer Portainer en tant que container Docker :**
   Exécutez les commandes suivantes pour déployer Portainer en mode `standalone` (pour un usage unique ou sur une petite installation Docker) :

   a. **Créer un volume Docker pour Portainer :**
   ```bash
   docker volume create portainer_data
   ```

   b. **Déployer le conteneur Portainer :**
   ```bash
   docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always \
   -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
   ```

   - `-d` : lance le conteneur en mode détaché (en arrière-plan).
   - `-p 9000:9000` : mappe le port 9000 de votre machine hôte au port 9000 du conteneur (port d'accès à l'interface web de Portainer).
   - `-p 8000:8000` : optionnel, utilisé pour la gestion des agents Docker (si vous utilisez l'agent Portainer sur plusieurs hôtes).
   - `--restart=always` : permet au conteneur de redémarrer automatiquement en cas de redémarrage de votre machine.

2. **Accéder à l'interface web de Portainer :**
   Ouvrez votre navigateur et allez à l'adresse suivante :

   ```
   http://<IP-de-votre-machine>:9000
   ```

   Lors de la première connexion, vous serez invité à créer un utilisateur administrateur.

### Commande complète en une seule étape :
Pour plus de simplicité, voici la commande complète pour déployer Portainer :

```bash
docker volume create portainer_data && docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
```

Après cela, vous pourrez utiliser Portainer pour gérer vos conteneurs Docker à travers une interface graphique intuitive.




```bash
docker ps
docker ps -a
docker system df
docker system prune
docker system prune -a
docker ps -a
docker volume create portainer_data
docker volume ls
docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
docker ps
docker run -it -d -p 8080:80 --name c1 nginx
docker run -it -d -p 8081:80 --name c2 nginx
docker run -it -d -p 8082:80 --name c3 nginx
docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=root -v /opt/mysqldata:/var/lib/mysql mysql
docker network create mynet
docker network ls
docker network --help
docker volume create haythem
docker volume ls
docker images
ls /var/lib/docker/volumes
cd /home/azureuser
history
```
