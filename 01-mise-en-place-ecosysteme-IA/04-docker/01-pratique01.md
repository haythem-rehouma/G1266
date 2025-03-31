---
title: "Liste des pratiques Docker"
description: "La référence incontournable des commandes Docker avec des exemples concrets et des bonnes pratiques de l'industrie"
---


---
<a name="table-des-matieres"></a>
## Table des matières
---

1. [Introduction](#introduction)
2. [Dépôt Local](#depot-local)
3. [Dépôt Distant](#depot-distant)
4. [Synchronisation avec GitHub](#synchronisation-avec-github)
5. [Connexion à GitHub via des clés SSH](#connexion-a-github-via-des-cles-ssh)
6. [Conclusion](#conclusion)


<br/>
---

<a name="introduction"></a>
# Introduction
---

**Docker** est devenu le standard incontournable de l'industrie pour la conteneurisation des applications. Cette technologie permet d'empaqueter une application avec toutes ses dépendances dans un conteneur isolé, garantissant qu'elle fonctionnera de manière identique quel que soit l'environnement d'exécution. Dans cette pratique, nous allons maîtriser les concepts fondamentaux de Docker ainsi que les commandes essentielles utilisées quotidiennement par les équipes DevOps des plus grandes entreprises technologiques.

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

---
<a name="prerequis"></a>

### Prérequis

- Disposer d'Oracle VM VirtualBox installé.  
- Disposer d'une machine virtuelle (VM) Ubuntu 22.04 installée sur Oracle VM VirtualBox.  
- Attention : Oracle VM VirtualBox peut contenir plusieurs machines virtuelles.  



#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>
---



<a name="preparation-de-l-environnement"></a>
# Préparation de l'environnement
---

#### **Installation d'une machine virtuelle Ubuntu 22.04**
1. **Télécharger Ubuntu 22.04 LTS** :
   - Site officiel : https://ubuntu.com/download/desktop
   - Télécharger l'ISO Ubuntu 22.04 LTS

2. **Installer VirtualBox** :
   - Télécharger depuis : https://www.virtualbox.org/wiki/Downloads
   - Installer sur votre système

3. **Créer VM Ubuntu** :
   - Nom : "Ubuntu-Docker"
   - Type : Linux, Ubuntu 64-bit
   - RAM : 4 Go
   - Disque VDI : 25 Go, allocation dynamique

4. **Installer Ubuntu** :
   - Démarrer la VM avec l'ISO
   - Installation normale
   - Effacer disque
   - Configurer langue, fuseau et compte

5. **Guest Additions (optionnel)** :
   ```bash
   sudo apt update && sudo apt install -y virtualbox-guest-additions-iso
   ```
   - Redémarrer





#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>





---
<a name="se-connecter-via-ssh-a-notre-machine-virtuelle"></a>
# Se connecter via ssh à notre machine virtuelle
---

<a name="manipulation-manuelle"></a>
### 1. Manipulation manuelle :

    > a.	Éteignez la machine virtuelle (choisissez l’option 3 : éteindre la machine).   
    >
    > b.	Accédez à Oracle VM VirtualBox et sélectionnez votre machine virtuelle.
    >
    > c.	Allez dans Configuration et ouvrez le menu Réseaux situé à gauche.
    >
    > d.	Sélectionnez l’option NAT pour l'Adaptateur 1 (première carte réseau).
    >
    > e.	Passez à l'onglet suivant et ajoutez un nouvel adaptateur (une autre carte réseau).
    >
    > f.	Choisissez le mode Host-only Adapter (Réseau privé hôte).
    >
    > g.	Reconnectez-vous à votre machine virtuelle.
    >
    > h.	Exécutez les commandes suivantes pour configurer le serveur SSH et obtenir les informations réseau nécessaires à la connexion à distance :


Ci-dessous les commandes à exécuter dans la machine virtuelle pour mettre en place la connexion SSH :

```bash
sudo apt update
sudo apt install openssh-server
sudo systemctl start ssh
sudo systemctl enable ssh
sudo systemctl status ssh
ip a
```

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>












---
<a name="explications-des-commandes"></a>
### 2. Explications des commandes :

> ##### 2.1. Mettez à jour la liste des paquets :
> ```bash
> sudo apt update
>```
> ##### 2.2. Installez le serveur SSH :
> ```bash
> sudo apt install openssh-server
> ```
> ##### 2.3. Démarrez le service SSH :
> ```bash
> sudo systemctl start ssh
> ```
> ##### 2.4. Activez le démarrage automatique du service SSH au démarrage du système :
> ```bash
> sudo systemctl enable ssh
> ```
> ##### 2.5. Vérifiez l'état du service SSH :
> ```bash
> sudo systemctl status ssh
> ```
> ##### 2.6. Obtenez les informations réseau et identifiez l'adresse IP de la deuxième carte réseau :
> ```bash
> ip a
> ```

Repérez l'adresse IP de la deuxième carte réseau, identifiée par l'attribut inet. Par exemple : 
```bash
inet 192.168.28.101/24 brd 192.168.28.255 scope global eth1
```
- L’adresse IP correspond à celle utilisée pour se connecter à la machine via SSH.


#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

---

<a name="connexion-depuis-votre-machine-windows"></a>
### 3. Connexion depuis votre machine Windows :

> a.	Revenez à votre machine Windows et ouvrez la ligne de commande (CMD) :
> ```bash
> Appuyez sur les touches Win + R, saisissez cmd, puis appuyez sur Entrée.
> ```
> b.	Saisissez la commande suivante pour établir une connexion SSH :
> ```bash
> ssh <nom-de-lutilisateur>@<adresse-ip-recuperee>
> ```
> Par exemple, si votre nom d'utilisateur est eleve et l'adresse IP récupérée est 192.168.28.101, vous saisirez : 
> ```bash
> ssh eleve@192.168.28.101
> ```
> c.	Saisissez le mot de passe associé à l'utilisateur lorsque demandé.
> d.	Passez en mode administrateur dans la machine virtuelle :
> ```bash
> su
> ```
> Entrez le mot de passe de l'utilisateur root.
> ou
> ```bash
> sudo -s
> ```
> Entrez le mot de passe de l'utilisateur courant.
> e.	Vous êtes maintenant connecté à la machine virtuelle avec les privilèges administratifs.


#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>
<br/>
<br/>




























---
<a name="pratique-01-installer-docker-et-docker-compose"></a>
# Pratique 01  - Installer docker et docker-compose
---

<a name="partie11"></a>
### 1.1. Exécutez les commandes suivantes:

Sur votre machine de contrôle (Ubuntu Desktop 22.04 ou Ubuntu Server 22.04), exécutez les commandes suivantes pour installer Docker et Docker Compose :

> *🔔 Note importante :* 
>
> Si vous n'êtes pas root, utilisez `sudo -i` au lieu de `su -`.
> Pour faciliter le copier/coller des commandes, vous avez deux options :
>
> 1. Connectez-vous à votre machine virtuelle via SSH :
>    ```bash
>    ssh <nom-de-lutilisateur>@<adresse-ip-recuperee>
>    ```
>    Entrez le mot de passe de l'utilisateur lorsque demandé.
>
> 2. Si vous préférez travailler directement dans VirtualBox, installez les VirtualBox Guest Additions pour activer le copier/coller :
>    ```bash
>    sudo apt update
>    sudo apt install -y virtualbox-guest-additions-iso
>    ```
>    Redémarrez votre machine virtuelle pour activer les fonctionnalités.


⚠️ *Exécutez attentivement les commandes suivantes :* 🛠️

```bash
su - (sinon sudo -i)
apt update
apt install -y apt-transport-https ca-certificates curl gnupg lsb-release git
git clone https://github.com/SkillFlowCoach/install-docker-ubuntu2204.git
cd install-docker-ubuntu2204/
chmod +x install-docker.sh
./install-docker.sh
apt install docker-compose -y
docker-compose version
```
#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

---

<a name="explications-des-commandes"></a>
### 1.2. Explications des commandes :

- Ces commandes permettent de :

1. Passer en mode administrateur (`su -` ou `sudo -i`)
2. Mettre à jour la liste des paquets disponibles (`apt update`) 
3. Installer les prérequis nécessaires pour Docker :
   - `apt-transport-https` : pour utiliser des dépôts HTTPS
   - `ca-certificates` : pour la gestion des certificats
   - `curl` : pour télécharger des fichiers
   - `gnupg` : pour la gestion des clés GPG
   - `lsb-release` : pour obtenir des informations sur la distribution
   - `git` : pour cloner le dépôt d'installation
4. Cloner le script d'installation de Docker depuis GitHub
5. Se placer dans le répertoire cloné
6. Rendre le script d'installation exécutable
7. Lancer le script d'installation de Docker
8. Installer Docker Compose
9. Vérifier que Docker Compose est bien installé

Une fois ces commandes exécutées, Docker et Docker Compose seront installés et prêts à être utilisés sur votre système.


Vérifiez l'installation en exécutant :

```bash
docker --version
docker-compose --version
```




#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>
<br/>
<br/>


























---
<a name="pratique-02-commandes-de-base"></a>
# Pratique 02 - Commandes de base de docker
---

<a name="partie21"></a>
### 2.1 - Commandes à exécuter sur votre machine virtuelle Ubuntu 22.04

Ci-dessous les commandes de base à exécuter sur votre machine virtuelle Ubuntu 22.04 :

1. Passer en mode administrateur :
   ```bash
   sudo su -
   ```

2. Mettre à jour les paquets :
   ```bash
   apt-get update
   ```

3. Vérifier la version du système :
   ```bash
   cat /etc/os-release
   ```

### 2.2 - Commandes Docker

1. Lister les conteneurs en cours d'exécution :
   ```bash
   docker ps
   ```

2. Lister tous les conteneurs (actifs et arrêtés) :
   ```bash
   docker ps -a
   # ou
   docker ps --all
   ```

3. Tester l'installation Docker avec un conteneur "Hello World" :
   ```bash
   docker run hello-world
   ```

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

---

<a name="partie22"></a>
### 2.3 - Récapitulatif des commandes :

```bash
su -
apt-get update
cat /etc/os-release
docker ps
docker ps -a
docker run hello-world
```

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

---

<a name="partie23"></a>
### 2.4 - Installer un conteneur Ubuntu avec une autre version 22.04


```bash
docker run -d -it --name myapacheubuntu -p 81:80 ubuntu:20.04
docker images
docker ps
docker ps -a
docker exec -it myapacheubuntu bash 
```

Nous sommes maintenant à l'intérieur du conteneur nommé "myapacheubuntu" basé sur l'image Ubuntu 20.04.
Vérifions la version du système d'exploitation installé dans ce conteneur :

```bash
apt update
cat /etc/os-release
```

### 🤔 Ubuntu 20.04 ?
# 💡💡💡
>   La commande affichera Ubuntu 20.04 car nous sommes à l'intérieur du conteneur qui utilise cette version spécifique d'Ubuntu, et non pas dans notre système hôte Ubuntu 22.04.

Sortons du conteneur :

```bash
exit
```

Vérifions la version du système d'exploitation dans notre machine hôte :

```bash
cat /etc/os-release
```
### 🤔 Ubuntu 22.04 ?
# 💡💡💡
>  La commande affichera Ubuntu 22.04 car nous sommes maintenant dans notre système hôte (la machine virtuelle) et non plus dans le conteneur.

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

---

<a name="partie25"></a>
### 2.5 - 🚨 POINT CRITIQUE - LISEZ ATTENTIVEMENT ! 🚨

### 🔍 Comment naviguer entre le conteneur et l'hôte

Pour bien comprendre la différence entre le conteneur et l'hôte, il faut toujours suivre ces étapes :

#### 1. Pour **entrer dans le conteneur** :
    ```bash
    docker exec -it myapacheubuntu bash 
    ```
    Vérifiez la version avec la commande `cat /etc/os-release` qui affichera Ubuntu 20.04, confirmant que nous sommes bien dans le conteneur.

#### 2. Pour **sortir du conteneur** :

    ```bash
    exit
    ```
    Vérifiez la version avec la commande `cat /etc/os-release` qui affichera Ubuntu 22.04, confirmant que nous sommes bien dans la machine virtuelle.

#### 3. Pour **sortir de la machine virtuelle** :    
    ```bash
    exit
    ```

### ⚠️ ⚠️ ⚠️ ATTENTION ! ⚠️ ⚠️ ⚠️

### 🥱 Je vais être un peu lourd ici, mais c'est pour votre bien ! 🔄

> 🎭 Tel un professeur qui répète 100 fois la même chose (oui, oui, comme celui qui vous énervait au lycée), 
> je vais insister sur ce point TRÈS important ! 
>
> 📢 Pourquoi ? Parce que c'est LA source numéro 1 de confusion chez les débutants !
>
> 🎪 Imaginez que vous êtes dans une maison (votre machine hôte), 
> avec une pièce spéciale (le conteneur) qui a sa propre déco différente du reste de la maison.
> Si vous ne savez pas dans quelle pièce vous êtes... c'est le chaos assuré ! 
>
> 🤹‍♂️ Alors oui, je vais être aussi agaçant qu'un jongleur qui fait tomber ses balles exprès,
> mais au moins, vous ne confondrez plus jamais votre conteneur et votre hôte !

Pour naviguer entre le conteneur et l'hôte :
- Entrer dans le conteneur : `docker exec -it <nom_conteneur> bash`
- Sortir du conteneur : `exit`

### 🔴 STOP ! INFORMATION CRUCIALE ! 🔴

### 🎪 ALLEZ, ON RÉPÈTE ENCORE UNE FOIS ! (Oui, je suis têtu...)

> 🤡 Comme disait mon grand-père : "La répétition est la mère de l'apprentissage... 
> et aussi la tante de la migraine !"
> Pour la TROISIÈME fois (oui, oui, vous lisez bien), voici comment naviguer :
> #### 🎭 Pour entrer dans le conteneur (comme un clown dans sa mini-voiture) :
> ```bash
> docker exec -it myapacheubuntu bash 
> ```
> #### 🎭 Pour sortir du conteneur (comme un clown qui sort de sa mini-voiture) :
> ```bash
> exit
> ```

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>





### 🔄 Continuons notre exploration ! ➡️


Bref, pour retourner dans le conteneur, nous allons utiliser la commade suivante :

```bash
docker exec -it myapacheubuntu bash 
```

Je vais installer le serveur web apache2

```bash
apt install apache2
```

### ⚠️ Vérifions que le serveur web fonctionne :

## *Méthode 1*

```bash
curl localhost:80 
```
> Cette commande ne fonctionnera pas pour deux raisons :
> 1. L'utilitaire `curl` n'est pas encore installé dans le conteneur
> 2. Le service Apache2 n'est pas démarré


Pour résoudre ce problème, nous devons installer l'utilitaire curl dans un premier temps :
```bash
apt install curl 
```

Vérifions que le service Apache2 est démarré dans un deuxième temps :

```bash
service apache2 status (il va être inactive)
service apache2 start (et donc l’activer)
service apache2 enable
service apache2 status
```

Vérifions que la commande curl fonctionne dans un troisième temps :



> Exécuter la commande depuis l'intérieur du conteneur pour vérifier qu'Apache fonctionne correctement
> ```bash
> curl localhost:80 
> ```

**Cette commande devrait afficher le contenu HTML de la page d'accueil par défaut d'Apache2. C'est une page statique adns le répertoire /var/www/html qui confirme que le serveur web Apache2 est correctement installé et fonctionne. Le contenu exact peut varier selon la version d'Apache2, mais il contient généralement le message "It works!" ou "Apache2 Ubuntu Default Page".**

> Exécuter la commande depuis l'extérieur du conteneur 
> ```bash
> exit
> ```
> Nous sommes maintenant de retour dans notre machine hôte, ubuntu 22.04.
> Exécuter la commande depuis l'extérieur du conteneur 
>```bash
> curl localhost:81
> ```

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

---

## *Méthode 2*

Testez Votre_adresse_IP:81 (par exemple, dans mon cas, http://localhost:81 depuis votre machine ubuntu 22.04 , firefox de ubuntu 22.04 et non pa svotre navigateur de windows)

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

---

<a name="partie26"></a>
### 2.6 - Remplacer la page d'accueil par celle de Yahoo

1.	Rentrez dans le conteneur

```bash
docker exec -it myapacheubuntu bash 
```

2.	Se déplacer dans le répertoire html
```bash
cd /var/www/html/
```

3.	Lister le contenu du répertoire html
```bash
ls (vous allez trouver la page index.html de apache2 par défaut que vous avez visualisé avec http://localhost:81 )
```

4.	Supprimer la page index.html par défaut
```bash
rm -rf index.html (la supprimer)
```

5.	Lister le contenu du répertoire html
```bash
ls (je ne trouve rien cette fois, je vais la remplacer par la page de yahoo qui va être sauvegardée dans index.html)
```

6.	Installer wget
```bash
apt install wget (wget l'outil qui va me permettre d’aspirer la page web de yahoo)
```


7.	Aspirer la page web de yahoo
```bash
wget www.yahoo.com
```

8.	Lister le contenu du répertoire html
```bash
ls (vous allez trouver la page index.html de nouveau mais celle  de yahoo)
```

9.	Tester la page web
```bash
curl localhost:80 (tester à partir de l’intérieur)
```

10.	Sortir de la machine virtuelle
```bash
exit (sortir vers la machine virtuelle)
```

11.	Tester la page web
```bash
curl http://localhost:81 (même chose que le navigateur Testez http://localhost:81 
```

12.	Sortir du mode administrateur de la machine virtuelle
```bash
exit (pour quitter le mode administrateur de la machine virtuelle)
```

13.	Sortir de la machine virtuelle
```bash
exit (quitter la machine virtuelle)
```



#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

---

<a name="partie27"></a>
### 2.7 - Récapitulatif des commandes :

```bash
docker exec -it myapacheubuntu bash 
cd /var/www/html/
ls
rm -rf index.html
ls
apt install wget
wget www.yahoo.com
ls
curl localhost:80
exit
curl http://localhost:81
exit
```













#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>
<br/>
<br/>



---
<a name="pratique-03-comment-supprimer-des-conteneurs-et-des-images"></a>   
# Pratique 03 - Comment tous supprimer ?
---

### 3.1 - Supprimer les conteneurs

```bash
docker ps
docker ps -a
docker ps -a -q
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

### 3.2 - Supprimer les images

```bash
docker images
docker images -q
docker rmi $(docker images -q)
```





#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>
<br/>
<br/>


























---
<a name="pratique-04-commandes-de-base-1"></a>   
# Pratique 04 - Cycle de vie des conteneurs et prise en main de Docker
---

<a name="partie41"></a>
### 4.1 - commandes de téléchargement des images en local

Dans cette section, nous allons découvrir les commandes fondamentales de Docker qui vous permettront de :

- Télécharger des images Docker officielles depuis Docker Hub
- Créer et lancer des conteneurs à partir de ces images 
- Gérer le cycle de vie des conteneurs (démarrage, arrêt, suppression)
- Comprendre les interactions entre images et conteneurs

Ces manipulations vous donneront une base solide pour travailler avec Docker au quotidien.


```bash
# Distributions Linux
docker pull ubuntu    # Distribution Ubuntu de la famille Debian
docker pull debian    # Distribution Debian de la famille Debian
docker pull centos    # Distribution CentOS de la famille Red Hat
docker pull almalinux # Distribution AlmaLinux de la famille Red Hat
docker pull fedora    # Distribution Fedora de la famille Red Hat

# Serveurs Web
docker pull nginx     # Serveur web NGINX
docker pull httpd     # Serveur web Apache

# Bases de données
docker pull mysql     # Base de données MySQL
docker pull redis     # Base de données Redis
docker pull mongo     # Base de données MongoDB

# Langages de programmation
docker pull php       # PHP de la famille PHP
docker pull python    # Python
docker pull java      # Java
docker pull node      # Node.js

# Applications Web
docker pull wordpress   # CMS WordPress
docker pull phpmyadmin  # Interface d'administration MySQL
```
> Ces commandes permettent de télécharger les images de différentes distributions Linux et de base de données, etc..

```bash
docker images
```
> Cette commande permet de lister les images disponibles sur votre machine.


#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

<a name="partie42"></a>
### 4.2 - commandes de cycle de vie des conteneurs

```bash 
docker run -d --name c1 nginx
```
> Cette commande permet de lancer un conteneur basé sur l'image nginx.

```bash
docker run -d --name c2 nginx
```
> Cette commande permet de lancer un conteneur basé sur l'image nginx.

```bash
docker images 
```
> Cette commande permet de lister les images disponibles sur votre machine.

```bash
docker ps
```
> Cette commande permet de lister les conteneurs en cours d'exécution.

```bash
docker ps -a
```
> Cette commande permet de lister tous les conteneurs, y compris ceux qui sont arrêtés.

```bash
docker stop c1
```
> Cette commande permet d'arrêter le conteneur c1.

```bash
docker start c1
```
> Cette commande permet de démarrer le conteneur c1.

```bash
docker pause c1
```
> Cette comma   nde permet de mettre en pause le conteneur c1.

```bash
docker unpause c1
```
> Cette commande permet de reprendre le conteneur c1.

```bash
docker restart c1
```
> Cette commande permet de redémarrer le conteneur c1.

```bash
docker kill c2 && docker rm c2
```
> Cette commande permet de tuer et de supprimer le conteneur c2.

```bash
docker stop c1 && docker rm c1
```
> Cette commande permet d'arrêter et de supprimer le conteneur c1.


```bash
docker ps
```
> Cette commande permet de lister les conteneurs en cours d'exécution.

```bash
docker ps -a
```
> Cette commande permet de lister tous les conteneurs, y compris ceux qui sont arrêtés.

```bash
docker images
```
> Cette commande permet de lister les images disponibles sur votre machine.



#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>
<br/>
<br/>






























---
<a name="pratique-05-commandes-de-base-2"></a>   
# Pratique 05 -  Cycle de vie des conteneurs partie 2
---
Dans cette section, nous allons continuer à explorer les commandes Docker avancées pour gérer le cycle de vie des conteneurs, notamment le démarrage, l'arrêt et la suppression de plusieurs conteneurs simultanément.

<a name="partie51"></a>
### 5.1 - Supprimer les conteneurs en cours d'exécution
D'abord, nous allons tous supprimer les conteneurs en cours d'exécution :

```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
```


<a name="partie52"></a>
### 5.2 - Création de conteneurs

```bash
docker run -it -d -p 8080:80 --name c1 nginx (testez localhost:8080)
docker run -it -d -p 8081:80 --name c2 nginx (testez localhost:8081)
docker run -it -d -p 8082:80 --name c3 nginx (testez localhost:8082)
docker ps
docker ps -q (donne les ids)
```

<a name="partie53"></a>
### 5.3 - Arrêter les conteneurs en utilisant les ids

```bash
docker stop a69983c1a0d3 
docker stop 262c9da97eb4 
docker stop 66793fb59d9 
```

<a name="partie54"></a>
### 5.4 - Démarrer les conteneurs en utilisant les ids

```bash
docker start a69983c1a0d3 ou docker start c1
docker start 262c9da97eb4 
docker start 66793fb59d9
```

<a name="partie55"></a>
### 5.5 - Arrêter les conteneurs en utilisant les noms
```bash
docker ps
docker stop c1
docker stop c2
docker stop c3
docker ps
```

<a name="partie56"></a>
### 5.6 - Démarrer les conteneurs en utilisant les noms
```bash
docker start c1
docker start c2
docker start c3
```

<a name="partie57"></a>
### 5.7 - Supprimer un conteneur en utilisant son id ou son nom

```bash
docker rm a69983c1a0d3 ou docker rm c1
```
⚠️ Attention ! Cette commande ne fonctionnera pas ! Les conteneurs doivent d'abord être arrêtés avant de pouvoir être supprimés. 
Pour supprimer un conteneur en cours d'exécution, vous devez :
1. 🛑 L'arrêter avec `docker stop <id/nom>`
2. 🗑️ Puis le supprimer avec `docker rm <id/nom>`




<a name="partie58"></a>
### 5.8 - Supprimer tous les conteneurs

```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

> Astuce :  Exécutez cette commande en premier pour comprendre la signification de -q 
> ```bash
> docker ps -a -q (ça donne les ids)
> ```


```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

### ⚠️ Attention ! Vérification importante

Est-ce que nous avons tout supprimé ? ⇒ ❌ Non ! Il reste encore les images Docker sur notre système.

Pour faire un nettoyage complet, nous devons également supprimer les images qui ont servi à créer nos conteneurs.

```bash
docker images
docker images -q
docker rmi $(docker images -q)
docker images
```




#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>
<br/>
<br/>































---
<a name="pratique-06-pratiquer-le-dockerfile"></a>   
# Pratique 06 - Le Dockerfile partie 1
---

###  *Objectif* 
- créer un serveur avec nginx et correction d'une erreur de port

### *Rappel*

- Nous rappelons les commandes pour nettoyer les conteneurs et images existants :

```bash
docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q) && docker rmi $(docker images -q)
```

> Rappel : Commande pour démarrer un conteneur nginx avec sur port 8080 et le supprimer

```bash
docker run -it -d -p 8080:80 --name c1 nginx
docker stop c1 && docker rm c1 && docker nginx
```


### 6.1 - Architecture du projet

```bash
projet_dockerfile_1
├── Dockerfile
├── index.html
```

Créer un répertoire pour notre projet

```bash
mkdir projet_dockerfile_1
cd projet_dockerfile_1
```

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>


### 6.2 -  Contenu du Dockerfile

Créez le fichier Dockerfile sans extension. Ce fichier doit être nommé exactement "Dockerfile" (avec un D majuscule et sans extension). C'est une convention importante de Docker qui doit être respectée.

```bash
nano Dockerfile
```
> Copier le contenu suivant :

```bash
# Utiliser une image Nginx
FROM nginx
# Copier le fichier HTML personnalisé dans le conteneur
COPY index.html /usr/share/nginx/html/index.html
```

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>

### 6.3 -  Contenu de la page web index.html

```bash 
nano index.html 
```
Copiez et coller le contenu suivant :

```html
<html> Hello from nginx </html>
```

Enregistrez le fichier en appuyant sur CTRL+X, puis tapez 'y' (ou 'o' selon votre langue) et appuyez sur Entrée pour confirmer l'enregistrement.


#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>


### 6.4 -  Créer l'image Docker

```bash
docker build -t monsiteweb .
docker images
docker run -d -p 9001:80 --name c1 monsiteweb
docker ps
```

#### 6.4.1 - Vérification

Vérifiez que l'image a été créée et que le conteneur est en cours d'exécution avec les commandes ci-dessus :

- `docker build -t monsiteweb .` : Crée l'image à partir du Dockerfile
- `docker images` : Liste les images pour vérifier que monsiteweb est créée
- `docker run -d -p 9001:80 --name c1 monsiteweb` : Lance un conteneur nommé c1 qui expose le port 80 sur le port 9001
- `docker ps` : Vérifie que le conteneur est bien en cours d'exécution


#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>


### 6.5 -  Testez sur le navigateur firefox de votre VM ubuntu 22.04

Essayez de copier l'url http://localhost:9001.
Une page web s'affiche.

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>


### 6.6 - Exercice de Troubleshooting 

Dans cet exercice, nous allons volontairement créer une erreur de configuration de port pour apprendre à la diagnostiquer et la corriger.

Voici les étapes que nous allons suivre :

1. Lancer un conteneur avec une mauvaise configuration de port
2. Constater que l'accès ne fonctionne pas 
3. Se connecter au conteneur pour corriger la configuration
4. Redémarrer Nginx avec la nouvelle configuration
5. Vérifier que l'accès fonctionne

```bash
docker run -d -p 9001:90 --name c2 monsiteweb
docker ps
```

- Essayez d'accéder à http://localhost:9001 dans votre navigateur.
- Que se passe-t-il ? Pourquoi pensez-vous que ça ne fonctionne pas ?
- Prenez un moment pour réfléchir à la configuration des ports que nous avons utilisée.

#### 6.6.1 - Analyse de l'erreur de port

💡 Cela ne fonctionne pas car il y a une incohérence entre les ports :

- Dans la configuration Nginx par défaut, le port interne est configuré sur 80
- Mais dans la commande docker run, nous utilisons le mauvais port 90 (`-p 9001:90`)

Cette erreur de configuration fait que le trafic n'atteint pas le serveur Nginx qui écoute sur le port 80.


#### 6.6.2 - Correction de l'erreur de port

```bash
docker exec -it c1_site_nginx bash
ls
cd /etc/
cd nginx
nano /etc/nginx/conf.d/default.conf (https://unix.stackexchange.com/questions/355911/trouble-installing-nano)
apt-get update
apt-get install nano
nano /etc/nginx/conf.d/default.conf
```

### Changez le port 80 à 90 🖍️ 

```bash
server {
    listen       90;
    listen  [::]:90;
    server_name  localhost;

```

Après avoir modifié ces deux lignes de 80 à 90, appuyez sur **CTRL+X** pour quitter nano. Lorsque nano vous demande si vous souhaitez sauvegarder les modifications, tapez *"Y"* (ou *"O"* pour Oui) puis appuyez sur Entrée pour confirmer le nom du fichier et enregistrer les changements.

```bash
nginx -s reload 
exit
```

- Accédez maintenant à http://localhost:9001 dans votre navigateur pour vérifier que le site est accessible
- Rédigez un petit paragraphe de ce que vous avez fait et ce que vous avez observé.

#### Références :

(https://docs.nginx.com/nginx/admin-guide/basic-functionality/runtime-control/)

#### [⬆️ retour à la table des matières](#table-des-matieres)
<br/>
<br/>
<br/>



