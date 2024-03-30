import requests
from bs4 import BeautifulSoup



#=======================================================================================================================
#====================================== FONCTIONS PRINCIPALES ==========================================================


# La fonction scrape_a_page permet d'extraire le code html d'une page produit et de le parser à partir de l'url
def scrape_a_page(product_page_url) :
    page = requests.get(product_page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

#=======================================================================================================================
#===================================== FONCTIONS TROUVER UN ELEMENT DANS CODE HTML =====================================


# La fonction find_upc permet de trouver l'upc (universal_product_code) dans le code de la page produit (soup)
# Elle repère la balise "th" contenant UPC et extrait la balise "td" soeur qui suit
def find_upc(soup) :
    upc = soup.find("th", string = "UPC").find_next_sibling("td").string
    return upc

# La fonction find_title permet de trouver le titre du produit dans la page produit (soup)
#Elle repère la première balise "h1" contenant le titre
def find_title(soup) :
    title = soup.find("h1").string
    return title

# La fonction find_price_including_tax permet de trouver le prix TTC dans le code de la page produit (soup)
# Elle repère la balise "th" contenant "Price (incl. tax)" et extrait la balise "td" soeur qui suit
def find_price_including_tax(soup) :
    price_including_tax = soup.find("th", string = "Price (incl. tax)").find_next_sibling("td").string
    return price_including_tax

# La fonction find_price_excluding_tax permet de trouver le prix HT dans le code de la page produit (soup)
# Elle repère la balise "th" contenant "Price (excl. tax)" et extrait la balise "td" soeur qui suit
def find_price_excluding_tax(soup) :
    price_excluding_tax = soup.find("th", string = "Price (excl. tax)").find_next_sibling("td").string
    return price_excluding_tax

# La fonction find_number_available permet de trouver la disponibilité du produit dans le code de la page produit (soup)
# Elle repère la balise "th" contenant "Availability" et extrait la balise "td" soeur qui suit puis retourne le nombre
def find_number_available(soup) :
    availability = soup.find("th", string = "Availability").find_next_sibling("td").string
    number_available = availability.split()[2][1:]
    return number_available

# La fonction find_product_description permet de trouver la description du produit dans le code de la page produit (soup)
# Elle repère la balise avec l'id "product_description" et extrait la balise "p" soeur qui suit
def find_product_description(soup) :
    product_description = soup.find(id = "product_description").find_next_sibling("p").string
    return product_description

# La fonction find_category permet de trouver la catégorie du produit dans le code de la page produit (soup)
# Elle extrait la balise avec le lien href correspondant au retour vers la page de la catégorie du produit
def find_category(soup, url) :
    url = "../" + url[37:]
    category = soup.find(href = url).string
    return category

# La fonction find_review_rating permet de trouver la note sur cinq du produit dans le code de la page produit (soup)
# Fonctionnement :
# Elle récupère le bloc html correspondant à la classe "star-rating"
# Dans ce bloc, elle récupère l'intitulé complet de la classe et créée une liste de deux éléments : le string ("star-rating")
# et le string (valeur de la note écrit en lettre)
# Elle sélectionne donc le deuxième élément de la liste puis le retourne
def find_review_rating(soup) :
    soup_class_star_rating = soup.find(class_ = "star-rating")
    list_review_rating = soup_class_star_rating.get("class")
    review_rating = list_review_rating[1]
    return review_rating

# La fonction find_image_url permet de trouver l'url de l'image du produit dans le code de la page produit (soup)
# Fonctionnement :
# Elle extrait le contenu de la balise img
# Elle récupère le lien src de l'image et le concactène pour retourner l'url
def find_image_url(soup) :
    tag_img = soup.find("img")
    src_image = tag_img["src"]
    src_image = src_image[5:]
    image_url = "https://books.toscrape.com" + src_image
    return(image_url)


#=================================================================================================================
#========================================== FONCTION MAIN ========================================================


def scrape_a_product(product_page_url, url) :


    # Extrait le code de la page du produit à scraper
    soup = scrape_a_page(product_page_url)

    # Récupère les données à scraper
    upc = find_upc(soup)
    title = find_title(soup)
    price_including_tax = find_price_including_tax(soup)
    price_excluding_tax = find_price_excluding_tax(soup)
    number_available = find_number_available(soup)
    product_description = find_product_description(soup)
    category = find_category(soup, url)
    review_rating = find_review_rating(soup)
    image_url = find_image_url(soup)

    # Créée une liste avec les données récupérées
    data_product = [product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]

    return data_product






