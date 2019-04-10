import feedparser

def saveToDatabase(entries):
	for entry in entries:
		title = entry["title"]
		link = entry["links"][0]["href"]
		published = entry["published"]
		#summary = entry["summary"]
		print(title.encode("utf-8"))
		print(link)
		print(published)
		print("---")
		print("---")

feeds = ["https://vegnews.com/feed.rss", "https://www.plantbasednews.org/post/rss.xml", "https://www.onegreenplanet.org/channel/vegan-food/feed/", "https://www.onegreenplanet.org/channel/vegan-food/news-and-trends/feed/", "https://www.livekindly.co/feed/", "http://cok.net/blog/category/veg-eating/feed/"]

for feed in feeds:
	d = feedparser.parse(feed)
	entries = d["entries"]
	saveToDatabase(entries)
	
	
		
		
