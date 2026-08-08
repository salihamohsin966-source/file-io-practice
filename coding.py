import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://quotes.toscrape.com/"

# Website ka HTML download karo
response = requests.get(url)

# HTML ko BeautifulSoup object me convert karo
soup = BeautifulSoup(response.text, "html.parser")

# Sare quote blocks select karo
quotes = soup.select("div.quote")


file = open("quote.txt","w",encoding = "utf-8")    

for quote in quotes:
    text = quote.select_one("span.text").get_text().strip()

    author = quote.select_one("small.author").get_text().strip()

    """
    
    tags = quote.select("a.tag")
    for tag in tags:
        tagg =tag.get_text().strip()
        
        is trah bhe sirf ar sirf aik hi tags print hoga is lia hm list method ka use kre ge
        
        """

    """
    
    tags = quote.select("div.tags")

    for tag in tags:
        print(tag.select("a.tag")[0].get_text().strip())
        print(tag.select("a.tag")[1].get_text().strip())
        print(tag.select("a.tag")[2].get_text().strip())
        print(tag.select("a.tag")[3].get_text().strip())

        
        HM AGR CHAHTE TO IS TRAH BHE LIKH SKTE THE LAIKN YE HMESHA ZROI NI HOGA K HR QUOTE ME ITNI HE TAGS HAI 
        HO SKTA HAI KSI QUOTE ME SIRF 2 TAGS HOTO [2]   IS POINT PR INTERPRETER ERROR THROW KRE GE HMESHA
        
        """

    tags = quote.select("a.tag")

    tag_list = []

    for tag in tags:
        tag_list.append(tag.get_text().strip())

    file.write(f"Text: {text}\n")

    file.write(f"Author:  {author}\n")

    file.write(f"Tags:  {','.join(tag_list)}\n")       # ye tag_list me join krta hai get_text ko   agr , k jagah - lgao to tags k drmian wahi symbol show hoge

    file.write("-" * 50 + "\n")     
file.close()       