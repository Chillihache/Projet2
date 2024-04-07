import scrape_product
import scrape_category

# Extrait la liste des url des catégories à partir du code de la page principale du site (soup) :
# Extrait les balises "li" et récupère tous les liens dans les balises "a"
# Enlève les liens qui ne correspondent pas aux catégories et créé la liste des url
def find_all_categories_url(soup):

    list_tag_li = soup.find_all("li")
    list_categories = []
    for tag in list_tag_li:
        tag_a = tag.find("a")
        if tag_a:
            list_categories.append(tag_a.get("href"))
    list_categories = list_categories[2:52]
    for i in range(len(list_categories)):
        list_categories[i] = "https://books.toscrape.com/" + list_categories[i]
    return list_categories


#=======================================================================================================================
#=============================================== MAIN ==================================================================

if __name__ == "__main__":

    url = "https://books.toscrape.com/index.html"

    # Extrait le code de la page principale du site "books to scrape"
    soup = scrape_product.scrape_a_page(url)

    # Récupère la liste des catégories dans la page principale (soup)
    list_categories_url = find_all_categories_url(soup)

    # Execute le script "scrape_category" pour chaque catégorie
    for url in list_categories_url:
        scrape_category.main(url)






