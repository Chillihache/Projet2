import Projet2
from datetime import datetime
import csv

#=======================================================================================================================
#==========================================FONCTIONS PRINCIPALES========================================================


# La fonction find_url_product permet de trouver les URL des produits appartenant à une catégorie dans la page d'une catégorie (soup)
# Fonctionnement :
# Elle récupère toutes les balises "h3"
# Elle créée et retourne une liste avec les liens "href" dans les balises "a"
def find_url_product(soup) :
    list_tags_product = soup.find_all("h3")
    list_url_product = []
    for product in list_tags_product :
        list_url_product.append("https://books.toscrape.com/catalogue" + product.find("a").get("href")[8:])
    return list_url_product

# La fonction scrape_all_product permet de faire appel à la fonction scrape_a_product pour chaque produit
# et créée une liste avec les données de chaque produit
def scrape_all_products(list_url_product, url) :
    list_data = []
    for link in list_url_product :
        list_data.append(Projet2.scrape_a_product(link, url))
    return list_data

def find_next_page(soup, list_url_product) :

    next_page_soup = soup
    while True :
        if next_page_soup.find("li", class_="next") != None :

            next_page = next_page_soup.find("li", class_="next").find("a").get("href")
            next_page_url = url[:-10] + next_page
            next_page_soup = Projet2.scrape_a_page(next_page_url)
            next_page_list_url_product = find_url_product(next_page_soup)
            list_url_product += next_page_list_url_product

        else :
            break

    return list_url_product

# La fonction creation_fichier_csv créée un fichier CSV avec les données récupérées
# Fonctionnement :
# Elle créée le nom du fichier en fonction de la date et de l'heure
# Elle créée une en-tête (header)
#Elle créée le fichier avec l'en-tête et les données contenues dans list_data
def create_csv_file(list_data) :
    name_csv_file = "Extraction_" + datetime.now().strftime("%Y-%m-%d_%H-%M") + ".csv"
    header = ["product_page_url", "universal_product_code (upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
    with open(name_csv_file, "w", encoding="utf-8") as csv_file :
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for data_product in list_data :
            writer.writerow(data_product)


#========================================FONCTION MAIN==================================================================
#=======================================================================================================================

url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"

# Appel la fonction scrape_a_page pour scraper la page d'une catégorie
soup = Projet2.scrape_a_page(url)

# Appel la fonction find_url_product pour créer la liste des URL de chaque produit de la catégorie à partir de la page catégorie (soup)
list_url_product_first_page = find_url_product(soup)

list_url_product = find_next_page(soup, list_url_product_first_page)

# Appel la fonction scrape_all_products pour scraper chaque produit à partir de la liste des URL de chaque produit de la catégorie
list_data = scrape_all_products(list_url_product, url)

print(list_data)

# Appel la fonction create_csv_file pour créer le fichier CSV avec les données de chaque prdoduit de la catégorie
create_csv_file(list_data)









