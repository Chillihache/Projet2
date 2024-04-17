Books online - Scraper Books to scrape
-
Dans le cadre de l'analyse concurrentielle du secteur de la vente en ligne de livres d'occasion, ce projet est un programme (Scraper) qui a pour but d'extraire les données du site "Books to scrape" en vue de
l'appliquer à d'autres site.
Ce projet a débuté en mars 2024 et sera soumis pour validation début avril 2024.

Le dépôt comprend les fichiers suivants :
- Script Python "scrape_books_to_scrape.py"
- Script Python "scrape_category.py"
- Script Python "scrape_product.py"
- Fichier ".gitignore"
- Fichier "requirements.txt"
- Fichier "readme.md"

Prérequis 
-
Afin d'exécuter le programme, vous devez installer python et récupérer le répertoire github sur votre machine.

Comment exécuter le programme sur Windows ?
-
Dans votre terminal, dans le répertoire récupéré, vous pouvez exécuter les commandes suivantes.

Créer un environnement virtuel :

    python -m venv env

Activer l'environnement virtuel :

    env\Scripts\activate.bat

Installer les packages python dans l'environnement virtuel :

    pip install -r requirements.txt

Lancer le programme :

    pyhton scrape_books_to_scrape.py

Fonctionnement des scripts
-
Ce programme est composé de trois scripts Pyhton. Il est séparé selon les étapes de l'élaboration du projet.
L'ensemble du code est en anglais cependant pour une compréhension interne plus précise, les commentaires sont en français.
Le programme s'execute environ en 35 minutes.

Le script "scrape_product.py" récupère des informations sur un produit du site "Books to scrape" à partir de l'URL de la page produit.
Les informations récupérées sont l'url, le code upc, le titre, le prix TTC, le prix HT, le nombre d'exemplaires disponibles, la description, la catégorie, la note sur cinq et l'url de
l'image associée.

Le script "scrape_category.py" récupère tous les url des produits appartenant à une catégorie et fait appel au script "scrape_product" pour récupérer les données de chacun d'entre eux puis,
il créé un fichier CSV avec les données de ces produits et télécharge les images liés dans un dossier.

Le script "scrape_books_to_scrape.py" est le fichier à exécuter.
Ce programme récupère les url de l'ensemble des catégories et appel le script "scrape_category" pour chacune d'entre elles.

Les données générées sont un dossier nommé "Extraction" comprenant :
- Les fichier CSV nommés : "Extraction_catégorie_date_heure"
- Les dossiers nommés : "Images_catégorie" comprenant les images en format .jpg nommées selon le titre du produit correspondant.


	


