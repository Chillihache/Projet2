Books online - Scraper Books to scrape
-
Dans le cadre de l'analyse concurrentielle du secteur de la vente en ligne de livres d'occasion, ce projet est un programme (Scraper) qui a pour but d'extraire les données du site "Books to scrape" en vue de
l'appliquer à d'autres site.
Ce projet a débuté en mars 2024 et sera soumis pour validation début avril 2024.

Le repository comprend les fichiers suivants :
- Script python "Scrape_books_to_scrape.py"
- Script python "Scrape_a_category.py"
- Script python "Scrape_a_product.py"
- Fichier ".gitignore"
- Fichier "requirements.txt"
- Fichier "readme.md"

Prérequis 
-
Afin d'executer correctement le script, il est nécessaire de créer un environnement virtuel avec les packages listés dans le fichier "requirements.txt" avec les versions correspondantes.

Fonctionnement des scripts
-
Ce programme est composé de trois scripts pyhton. Il est séparé selon les étapes de l'élaboration du projet.
L'ensemble du code est en anglais cependant pour une compréhension interne plus précise, les commentaires sont en français.
Le programme s'execute environ en 35 minutes.

Le script "Scrape_a_product.py" n'est composé que de fonctions, dont une fonction main qui fait appel aux autres, il n'est donc pas executable seul. 
Ce programme sert à récupérer des informations sur un produit du site "Books to scrape" à partir de l'URL de la page produit. 
Les informations récupérées sont l'url, le code upc, le titre, le prix TTC, le prix HT, le nombre d'exemplaires disponibles, la description, la catégorie, la note sur cinq et l'url de
l'image associée.

Le script "Scrape_a_category.py" n'est composé que de fonctions, dont une fonction main qui fait appel aux autre, il n'est donc pas executable seul.
Ce programme permet de récupérer tous les url des produits appartenant à une catégorie et fait appel au script "Scrape_a_product" pour récupérer les données de chacun d'entre eux puis,
il créé un fichier CSV avec les données de ces produits et télécharge les images liés dans un dossier.

Le script "Scrape_books_to_scrape.py" est le fichier à executer.
 Ce programme récupère les url de l'ensemble des catégories et appel le script "Scrape_a_category" pour chacune d'entre elles.

Les données générées sont un dossier nommé "Extraction" comprenant :
- Les fichier CSV du nom : "Extraction_catégorie_date_heure"
- Les dossiers du nom : "Images_catégories" comprenant les images en format .jpg nommées selon le titre du produit correspondant.


	


