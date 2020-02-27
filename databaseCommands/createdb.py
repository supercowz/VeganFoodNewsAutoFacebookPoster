import sqlite3

sqlite_file = 'vegan_food_news_links.sqlite'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
#c.execute('DROP table rss_feed_item')
c.execute('CREATE TABLE rss_feed_item (published_date INTEGER, url TEXT primary key, headline TEXT, is_posted INTEGER)')
c.execute('CREATE INDEX published_date_idx on rss_feed_item (published_date)')

#c.execute("INSERT INTO rss_feed_item (published_date, url, headline, is_posted) VALUES (1554923716, 'https://www.unixtimestamp.com/', 'This is the headline', 0)")

c.execute('SELECT headline, url, published_date FROM rss_feed_item where is_posted = 0 order by published_date desc')
#c.execute('update rss_feed_item set is_posted = 1 where is_posted = 0')
all_rows = c.fetchall()
print('1):', all_rows)

for row in c:
	print(row)
	print("---")
	print("---")

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
