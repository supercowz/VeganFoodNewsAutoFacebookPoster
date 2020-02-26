import sqlite3

sqlite_file = 'vegan_food_news_links.sqlite'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE calendar_event (uid TEXT PRIMARY KEY, organizer TEXT, date_start INTEGER, date_end INTEGER, summary TEXT, description TEXT)')
c.execute('CREATE INDEX date_start_idx on calendar_event (date_start)')

c.execute('SELECT uid, organizer, date_start, date_end, summary, description FROM calendar_event order by date_start desc')

all_rows = c.fetchall()
print('1):', all_rows)

for row in c:
	print(row)
	print("---")
	print("---")

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
