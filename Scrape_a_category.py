import Scrape_a_product
from datetime import datetime
import csv
import os
import requests
import re

# Trouve les url des produits appartenant à une catégorie dans la page d'une catégorie (soup) :
# Récupère toutes les balises "h3"
# Créé et retourne une liste avec les liens "href" dans les balises "a"
def find_url_product(soup) :
    list_tags_product = soup.find_all("h3")
    list_url_product_first_page = []
    for product in list_tags_product :
        list_url_product_first_page.append("https://books.toscrape.com/catalogue" + product.find("a").get("href")[8:])
    return list_url_product_first_page

# Vérifie la présence d'autres pages et ajoute les url des produits dans celles-ci :
# Recherche une balise "next" et récupère le lien de la page suivante dans la balise
# Utilise la fonction "scrape_a_page" pour récupérer le code de la page suivante
# Récupère les url des produits dans la page suivante et les ajoute à la liste des url des produits de la catégorie
# Recommence tant qu'il existe une page suivante puis retourne la liste des url complète
def find_next_page(soup, list_url_product, url) :

    next_page_soup = soup
    while True :
        if next_page_soup.find("li", class_="next") != None :

            next_page = next_page_soup.find("li", class_="next").find("a").get("href")
            next_page_url = url[:-10] + next_page
            next_page_soup = Scrape_a_product.scrape_a_page(next_page_url)
            next_page_list_url_product = find_url_product(next_page_soup)
            list_url_product += next_page_list_url_product

        else :
            break

    return list_url_product

# Fait appel à la fonction scrape_a_product pour chaque produit et créé une liste avec les données de tous les produits de la catégorie
def scrape_all_products(list_url_product, url) :
    list_data = []
    for link in list_url_product :
        list_data.append(Scrape_a_product.scrape_a_product(link, url))
    return list_data


# Créé un fichier CSV avec les données récupérées :
# Créé un dossier "Extraction" si il n'existe pas encore, nomme le fichier CSV avec le nom de la catégorie et la date et heure
# Créé une en-tête (header)
# Créé le fichier CSV avec l'en-tête et les données contenues dans list_data
def create_csv_file(list_data) :
    try :
        os.mkdir("Extraction")
    except :
        FileExistsError
    category = list_data[0][7]
    name_csv_file = "Extraction/Extraction_" + category + datetime.now().strftime("_%Y-%m-%d_%H-%M") + ".csv"
    header = ["product_page_url", "universal_product_code (upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
    with open(name_csv_file, "w", encoding="utf-8") as csv_file :
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for data_product in list_data :
            writer.writerow(data_product)

# Télécharge les images des produits de la catégorie :
# Créé un dossier dans "Extraction" avec le nom de la catégorie si il n'existe pas encore
# Télécharge chaque image au format "jpg" dans le dossier créé
def download_images_products(list_data) :
    category = list_data[0][7]
    name_folder_image_category = "Extraction/Images_" + category
    try :
        os.mkdir(name_folder_image_category)
    except :
        FileExistsError
    for i in range(len(list_data)) :
        url_image = list_data[i][-1]
        title = list_data[i][2]
        title = clean_title(title)
        name_image = name_folder_image_category + "/" + title + ".jpg"
        with open(name_image, "wb") as image:
            image.write(requests.get(url_image).content)

# Modifie le titre des produits pour retirer les symboles qui ne sont pas acceptés dans le nommage des fichiers jpg
def clean_title(title) :
    cleaned_title = re.sub(r"""[\\/*?:"<>|]""", "", title)
    return cleaned_title

#========================================FONCTION MAIN==================================================================
#=======================================================================================================================

def scrape_a_category(url) :

    # Extrait le code la page d'une catégorie
    soup = Scrape_a_product.scrape_a_page(url)

    # Créé la liste des url des produits de la catégorie à partir de la page catégorie (soup)
    list_url_product_first_page = find_url_product(soup)

    # Vérifie la présence d'autres pages et ajoute les url des produits de celles-ci
    list_url_product = find_next_page(soup, list_url_product_first_page, url)

    # Scrape tous les produits de la catégorie
    list_data = scrape_all_products(list_url_product, url)

    # Créé le fichier CSV avec les données de chaque produit de la catégorie
    create_csv_file(list_data)

    # Télécharge les images des produits de la catégorie
    download_images_products(list_data)











