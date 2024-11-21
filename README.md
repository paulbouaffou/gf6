# GF6

Cet outil est une futur fonctionnalité de la version 6 de l’outil [GAWA](https://gawa.wikimedia.ci/)

## 1. Préparer l'environnement pour l'application Flask

### a. Installer Python
Assurez-vous que Python est installé sur votre système. Vous pouvez vérifier cela en exécutant la commande suivante dans le terminal (ou l'invite de commandes) :

```bash
python --version
```

Si Python n'est pas installé, vous pouvez le télécharger et l'installer depuis [python.org](https://www.python.org/downloads/).

### b. Créer un environnement virtuel
Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances de votre projet. Voici comment créer un environnement virtuel :

- Ouvrez votre terminal.
- Accédez au répertoire de votre projet Flask (ou créez un nouveau répertoire pour le projet).
- Créez un environnement virtuel en exécutant la commande suivante :

```bash
python -m venv venv
```

Cela crée un répertoire `venv` contenant l'environnement virtuel.

### c. Activer l'environnement virtuel
Une fois l'environnement virtuel créé, vous devez l'activer.

- **Sur Windows** :
  ```bash
  venv\Scripts\activate
  ```

- **Sur macOS/Linux** :
  ```bash
  source venv/bin/activate
  ```

Une fois l'environnement activé, vous verrez `(venv)` dans le terminal.

## 2. Installer Flask

### a. Installer Flask
Dans l'environnement virtuel activé, vous devez installer Flask avec `pip` :

```bash
pip install Flask
```

Cela installera Flask et ses dépendances dans l'environnement virtuel.

## 3. Désactiver l'environnement virtuel

Lorsque vous avez terminé, vous pouvez désactiver l'environnement virtuel en exécutant la commande suivante dans le terminal :

```bash
deactivate
```

Cela vous ramène à votre environnement Python global.

## 4. Installer et exécuter l'application **gf6**

### a. Cloner le dépôt **gf6**
Vous pouvez cloner le dépôt **[gf6](https://github.com/paulbouaffou/gf6)** avec la commande suivante :

```bash
git clone https://github.com/paulbouaffou/gf6.git
```

Accédez ensuite au répertoire cloné :

```bash
cd gf6
```

### b. Installer les dépendances
Assurez-vous que toutes les dépendances nécessaires au bon fonctionnement de l'application sont installées. Si l'application utilise un fichier `requirements.txt`, vous pouvez installer ces dépendances avec :

```bash
pip install -r requirements.txt
```

### c. Exécuter l'application **gf6**
Suivez les instructions du fichier `README.md` du projet **gf6** pour l'exécution spécifique de l'application, qui pourrait inclure des commandes comme :

```bash
python app.py
```

Ou toute autre commande spécifique du projet.

Vous devriez voir un message indiquant que le serveur Flask a démarré, comme ceci :

```bash
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Cela signifie que l'application Flask est en cours d'exécution sur votre machine locale à l'adresse `http://127.0.0.1:5000/`.

### d. Accéder à l'application
Ouvrez un navigateur web et allez à l'adresse suivante :

```
http://127.0.0.1:5000/
```

