import requests
import sqlite3
from bs4 import BeautifulSoup
import time
import datetime
sqlite_file = '/var/www/vegan_food_news_links.sqlite'

def saveToDatabase(results):
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	for result in results:
		headline = result[0]
		published_date_unix = time.mktime(datetime.datetime.now().timetuple())
		
		# Let's try to get the redirect url.
		try:
			url = result[1]
			r2 = requests.get(url)
			url = r2.url
			c.execute("INSERT OR IGNORE INTO rss_feed_item (published_date, url, headline, is_posted) VALUES (?, ?, ?, 0)", (published_date_unix, url, headline.decode('utf-8')))
		except requests.ConnectionError as e:
			pass
			continue 
			
		
	conn.commit()
	conn.close()
	print("saved to database success")

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

saveToDatabase(results)