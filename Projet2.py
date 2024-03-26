import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime


#=======================================================================================================================
#====================================== FONCTIONS PRINCIPALES ==========================================================


# La fonction scraper_une_page permet d'extraire le code html d'une page produit et de le parser à partir de l'url
def scraper_une_page(product_page_url) :
    page = requests.get(product_page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

# La fonction creation_fichier_csv créée un fichier CSV avec les données récupérées
# Fonctionnement :
# Elle créée le nom du fichier en fonction de la date et de l'heure
# Elle créée une en-tête
#Elle créée le fichier avec l'en-tête et les données récupérées
def creation_fichier_csv(donnees_produit) :
    nom_fichier_csv = "Extraction_" + datetime.now().strftime("%Y-%m-%d_%H-%M") + ".csv"
    en_tete = ["product_page_url", "universal_product_code (upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
    with open(nom_fichier_csv, "w") as fichier_csv :
        writer = csv.writer(fichier_csv)
        writer.writerow(en_tete)
        writer.writerow(donnees_produit)


#=======================================================================================================================
#===================================== FONCTIONS TROUVER UN ELEMENT DANS CODE HTML =====================================


# La fonction trouver_upc permet de trouver l'upc (universal_product_code) dans le code de la page produit (soup)
# Elle repère la balise "th" contenant UPC et extrait la balise "td" frêre qui suit
def trouver_upc(soup) :
    upc = soup.find("th", string = "UPC").find_next_sibling("td").string
    return upc

# La fonction trouver_title permet de trouver le titre de la page dans la page produit (soup)
# Seul une balise porte le nom "title"
def trouver_title(soup) :
    title = soup.find("h1").string
    return title

# La fonction trouver_price_including_tax permet de trouver le prix avec taxes dans le code de la page produit (soup)
# Elle repère la balise "th" contenant "Price (incl. tax)" et extrait la balise "td" frêre qui suit
def trouver_price_including_tax(soup) :
    price_including_tax = soup.find("th", string = "Price (incl. tax)").find_next_sibling("td").string
    return price_including_tax

# La fonction trouver_price_excluding_tax permet de trouver le prix hors taxes dans le code de la page produit (soup)
# Elle repère la balise "th" contenant "Price (excl. tax)" et extrait la balise "td" frêre qui suit
def trouver_price_excluding_tax(soup) :
    price_excluding_tax = soup.find("th", string = "Price (excl. tax)").find_next_sibling("td").string
    return price_excluding_tax

# La fonction trouver_number_available permet de trouver la disponibilité du produit dans le code de la page produit (soup)
# Elle repère la balise "th" contenant "Availability" et extrait la balise "td" frêre qui suit puis retourne le nombre
def trouver_number_available(soup) :
    availability = soup.find("th", string = "Availability").find_next_sibling("td").string
    number_available = availability.split()[2][1:]
    return number_available

# La fonction trouver_prodcut_description permet de trouver la description du produit dans le code de la page produit (soup)
# Elle repère la balise avec l'id "product_description" et extrait la balise "p" frêre qui suit
def trouver_product_description(soup) :
    product_description = soup.find(id = "product_description").find_next_sibling("p").string
    return product_description

# La fonction trouver_category permet de trouvver la catégorie du produit dans le code de la page produit (soup)
# Elle extrait la balise avec le lien href correspondant au retour vers la page de la catégorie du produit
def trouver_category(soup) :
    category = soup.find(href = "../category/books/travel_2/index.html").string
    return category

# La fonction trouver_review_rating permet de trouver la note sur cinq du produit dans le code de la page produit (soup)
# Fonctionnement :
# Elle récupère le bloc html correspondant à la classe "star-rating"
# Dans ce bloc, elle récupère l'intitulé complet de la classe et créée une liste de deux éléments : le string ("star-rating")
# et le string (valeur de la note écrit en lettre)
# Elle sélectionne donc le deuxième élément de la liste puis le retourne
def trouver_review_rating(soup) :
    soup_class_star_rating = soup.find(class_ = "star-rating")
    liste_review_rating = soup_class_star_rating.get("class")
    review_rating = liste_review_rating[1]
    return review_rating

# La fonction trouver_image_url permet de trouver l'url de l'image du produit dans le code de la page produit (soup)
# Fonctionnement :
# Elle extrait le contenu de la balise img
# Elle récupère le lien src de l'image
# Elle supprime "../.." qui se trouve au début du lien dans le code html
# Elle concatène l'url du site avec le reste de l'url de l'image et retourne le résultat
def trouver_image_url(soup) :
    balise_img = soup.find("img")
    src_image = balise_img["src"]
    src_image = src_image[5:]
    image_url = "https://books.toscrape.com" + src_image
    return(image_url)


#=================================================================================================================
#========================================== MAIN =================================================================


if __name__ == '__main__' :

    #URL du produit à scraper
    product_page_url = "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"

    #extrait le code de la page du produit à scraper
    soup = scraper_une_page(product_page_url)

    #Récupère les données à scraper
    upc = trouver_upc(soup)
    title = trouver_title(soup)
    price_including_tax = trouver_price_including_tax(soup)
    price_excluding_tax = trouver_price_excluding_tax(soup)
    number_available = trouver_number_available(soup)
    product_description = trouver_product_description(soup)
    category = trouver_category(soup)
    review_rating = trouver_review_rating(soup)
    image_url = trouver_image_url(soup)

    #Créée une liste avec les données récupérées
    donnees_produit = [product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]

    #Créée le fichier csv
    creation_fichier_csv(donnees_produit)







