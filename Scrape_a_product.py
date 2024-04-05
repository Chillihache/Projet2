import requests
from bs4 import BeautifulSoup


# Extrait le code html d'une page produit et le parse à partir de l'url
def scrape_a_page(product_page_url) :
    page = requests.get(product_page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

# Trouve l'upc (universal_product_code) dans le code de la page produit (soup) :
# Repère la balise "th" contenant "UPC" et extrait la balise "td" soeur qui suit
def find_upc(soup) :
    upc = soup.find("th", string = "UPC").find_next_sibling("td").string
    return upc

# Trouve le titre du produit dans la page produit (soup) :
# Repère la première balise "h1" contenant le titre
def find_title(soup) :
    title = soup.find("h1").string
    return title

# Trouve le prix TTC dans le code de la page produit (soup) :
# Repère la balise "th" contenant "Price (incl. tax)" et extrait la balise "td" soeur qui suit
def find_price_including_tax(soup) :
    price_including_tax = soup.find("th", string = "Price (incl. tax)").find_next_sibling("td").string
    return price_including_tax

# Trouve le prix HT dans le code de la page produit (soup) :
# Repère la balise "th" contenant "Price (excl. tax)" et extrait la balise "td" soeur qui suit
def find_price_excluding_tax(soup) :
    price_excluding_tax = soup.find("th", string = "Price (excl. tax)").find_next_sibling("td").string
    return price_excluding_tax

# Trouve la disponibilité du produit dans le code de la page produit (soup) :
# Repère la balise "th" contenant "Availability" et extrait la balise "td" soeur qui suit puis retourne le nombre
def find_number_available(soup) :
    availability = soup.find("th", string = "Availability").find_next_sibling("td").string
    number_available = availability.split()[2][1:]
    return number_available

# Trouve la description du produit dans le code de la page produit (soup) :
# Repère la balise avec l'id "product_description" et extrait la balise "p" soeur qui suit
# Retourne "Empty" pour les produits n'ayant pas de description
def find_product_description(soup) :
    product_description = "Empty"
    try :
        product_description = soup.find(id = "product_description").find_next_sibling("p").string
    except :
        AttributeError
    return product_description

# Trouve la catégorie du produit dans le code de la page produit (soup) :
# Extrait la balise avec le lien href correspondant au "retour" vers la page de la catégorie du produit
def find_category(soup, url) :
    url = "../" + url[37:]
    category = soup.find(href = url).string
    return category

# Trouve la note sur cinq du produit dans le code de la page produit (soup) :
# Récupère le bloc html correspondant à la classe "star-rating"
# Récupère l'intitulé complet de la classe et créé une liste de deux éléments : le string ("star-rating") et le string (valeur de la note écrit en lettre)
# Sélectionne le deuxième élément de la liste puis le retourne
def find_review_rating(soup) :
    soup_class_star_rating = soup.find(class_ = "star-rating")
    list_review_rating = soup_class_star_rating.get("class")
    review_rating = list_review_rating[1]
    return review_rating

# Trouve l'url de l'image du produit dans le code de la page produit (soup) :
# Extrait le contenu de la balise img
# Récupère le lien src de l'image et le concatène pour retourner l'url
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

    # Créé une liste avec les données récupérées
    data_product = [product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]

    return data_product






