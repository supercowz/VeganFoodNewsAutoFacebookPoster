import requests
import sqlite3
from icalendar import Calendar

url = ""

response = requests.get(url)
#print(response.text.encode('utf-8', 'ignore'))

sqlite_file = '/var/www/vegan_food_news_links.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

gcal = Calendar.from_ical(response.text)
for component in gcal.walk():
    if component.name == "VEVENT":
		uid = component.get('uid')
		organzier = component.get('organizer')
		date_start = component.get('dtstart').dt
		date_end = component.get('dtend').dt
		summary = component.get('summary')
		description = component.get('description')
		
		c.execute("REPLACE INTO calendar_event (uid, organizer, date_start, date_end, summary, description) VALUES (?, ?, ?, ?, ?, ?)", (uid,organzier,date_start,date_end,summary,description))

conn.commit()
conn.close()
