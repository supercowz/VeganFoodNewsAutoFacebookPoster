import feedparser
import sqlite3
from dateutil.parser import parse
import time

sqlite_file = 'vegan_food_news_links.sqlite'


def saveToDatabase(entries):
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	for entry in entries:
		headline = entry["title"].encode("utf-8")
		link = entry["links"][0]["href"]
		published = entry["published"]
		published_date = parse(published)
		published_date_unix = time.mktime(published_date.timetuple()) 
		
		c.execute("INSERT OR IGNORE INTO rss_feed_item (published_date, url, headline, is_posted) VALUES (?, ?, ?, 0)", (published_date_unix, link, headline.decode('utf-8')))
		
	conn.commit()
	conn.close()
		
		

feeds = ["https://vegnews.com/feed.rss", "https://www.plantbasednews.org/post/rss.xml", "https://www.onegreenplanet.org/channel/vegan-food/feed/", "https://www.onegreenplanet.org/channel/vegan-food/news-and-trends/feed/", "https://www.livekindly.co/feed/", "http://cok.net/blog/category/veg-eating/feed/"]

for feed in feeds:
	d = feedparser.parse(feed)
	entries = d["entries"]
	saveToDatabase(entries)
	
	
		
		

