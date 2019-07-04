import requests
from bs4 import BeautifulSoup
r = requests.get("https://news.google.com/search?q=(\"vegan\" and \"food\") or (\"plant based\" and \"food\")")


soup = BeautifulSoup(r.content, 'html.parser')
results = []

for article in soup.find_all('article'):
    for link in article.find_all('a'):
        linkString = link.string
        linkHref = link.get("href")
        if (linkString != None and linkHref != None and linkHref.startswith("./articles/")):
            linkString = linkString.encode("utf-8")
            linkHref = linkHref.replace("./articles/", "https://news.google.com/articles/")
            results.append([linkString, linkHref])

for result in results:
    #get the headline
    headline = result[0]
    
    # Let's get the redirect url.
    try:
        url = result[1]
        r2 = requests.get(url)
        url = r2.url
    except requests.ConnectionError as e:
        pass
        continue
    
    # Let's just assume that the date is for today.
    # date =
    
    #save to database
    print(headline)
    print(url)
    print("----------")