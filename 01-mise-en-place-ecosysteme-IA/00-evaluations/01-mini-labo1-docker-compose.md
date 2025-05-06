# Énoncé de Lab : Docker Compose avec Dépendance entre Conteneurs

#### Objectif :
L'objectif de ce lab est de vous familiariser avec Docker Compose en vous demandant de configurer un environnement de conteneurs où un service dépend d'un autre pour démarrer correctement. Vous allez configurer deux conteneurs avec une relation de dépendance. Par exemple, une application qui dépend d'une base de données, ou deux services qui doivent interagir, l'un dépendant de l'autre.

#### Instructions :

1. **Pré-requis :**
   - Avoir Docker et Docker Compose installés sur votre machine.
   - Connaître les bases de Docker et Docker Compose.

2. **Création du projet :**
   - Créez un nouveau dossier pour votre projet et naviguez à l'intérieur de celui-ci.

3. **Configuration de Docker Compose :**
   - Dans ce dossier, créez un fichier `docker-compose.yaml`.
   - Configurez deux services dans ce fichier avec une relation de dépendance entre eux.

4. **Choix des conteneurs :**
   - Vous pouvez choisir parmi les exemples suivants ou en proposer d'autres, en respectant les exigences de dépendance :
     - **Wiki.js et PostgreSQL** : Wiki.js dépend de PostgreSQL pour stocker ses données.
     - **WordPress et MySQL** : WordPress dépend de MySQL pour sa base de données.
     - **Redis et une application Node.js** : Une application Node.js dépend de Redis pour le stockage en cache.
     - **Nginx et une application Python (Flask)** : Un serveur Nginx pour servir une application Flask.
     - **Elasticsearch et Kibana** : Kibana dépend d'Elasticsearch pour fournir des visualisations.
     - **Prometheus et Grafana** : Grafana dépend de Prometheus pour la collecte de données de surveillance.

5. **Contenu du fichier `docker-compose.yaml` :**
   - Définissez les services avec les paramètres nécessaires, y compris les images Docker appropriées, les variables d'environnement pour la configuration, et les volumes pour la persistance des données.

# Exemple de Contenu pour Wordpress et MySQL :
```yaml
version: '3.3'

services:
   db:
     image: mysql:5.7
     volumes:
       - db_data:/var/lib/mysql
     restart: always
     environment:
       MYSQL_ROOT_PASSWORD: somewordpress
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD: wordpress

   wordpress:
     depends_on:
       - db
     image: wordpress:latest
     ports:
       - "8000:80"
     restart: always
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_USER: wordpress
       WORDPRESS_DB_PASSWORD: wordpress
       WORDPRESS_DB_NAME: wordpress
volumes:
    db_data: {}

```

# Exemple de Contenu pour Prometheus et Grafana :

```yaml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus
    restart: always
    volumes:
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'

  grafana:
    image: grafana/grafana
    restart: always
    depends_on:
      - prometheus
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=secret

volumes:
  prometheus_data:
```

6. **Testez votre configuration :**
   - Lancez Docker Compose avec la commande `docker-compose up`.
   - Vérifiez que le conteneur dépendant démarre correctement après le conteneur dont il dépend.
   - Accédez à l'interface web de l'application pour confirmer que celle-ci fonctionne correctement.

7. **Documentation :**
   - Rédigez un document expliquant votre configuration et les étapes que vous avez suivies pour créer et tester votre `docker-compose.yaml`.
   - Incluez des captures d'écran montrant les conteneurs en cours d'exécution et l'interface de l'application choisie.

8. **Soumission :**
   - Soumettez votre fichier `docker-compose.yaml` ainsi que votre document de documentation via la plateforme Léa avant la date limite.

#### Critères d'Évaluation :

- **Validité du fichier `docker-compose.yaml` :** Assurez-vous que le fichier est valide et que les services démarrent comme prévu.
- **Documentation :** La clarté et la précision de la documentation seront évaluées.
- **Fonctionnalité :** Vérifiez que l'application fonctionne correctement et peut se connecter à son service dépendant.

#### Date limite : 
Soumettez vos fichiers avant minuit, le mercredi 29 mai 2024.

Bonne chance et n'hésitez pas à poser des questions si vous avez besoin d'aide !
