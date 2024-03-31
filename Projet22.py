import Projet2
import Projet21

#=======================================================================================================================
#============================================== FONCTIONS PRINCIPALES ==================================================

def find_all_categories_url(soup) :

    list_tag_li = soup.find_all("li")
    list_categories = []
    for tag in list_tag_li :
        tag_a = tag.find("a")
        if tag_a is not None :
            list_categories.append(tag_a.get("href"))
    list_categories = list_categories[2:52]
    for i in range(len(list_categories)) :
        list_categories[i] = "https://books.toscrape.com/" + list_categories[i]
    return list_categories


#=======================================================================================================================
#=============================================== MAIN ==================================================================

url = "https://books.toscrape.com/index.html"

soup =Projet2.scrape_a_page(url)

list_categories = find_all_categories_url(soup)

for url in list_categories :
    Projet21.scrape_a_category(url)






