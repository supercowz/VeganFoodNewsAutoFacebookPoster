from icalendar import Calendar
from datetime import datetime
from pytz import timezone

import requests
import json
import os

url = "https://www.facebook.com/events/ical/upcoming/?uid=100005885022646&key=219ODd1jNxGCrqhc"

response = requests.get(url)

gcal = Calendar.from_ical(response.text)
events = []
eastern = timezone('US/Eastern')
for component in gcal.walk():
    if component.name == "VEVENT":
		uid = component.get('uid')
		organzier = component.get('organizer')
		date_start = component.get('dtstart')
		date_end = component.get('dtend')
		summary = component.get('summary')
		description = component.get('description')
		
		events.append({ 
        	"date_start": date_start.dt.astimezone(eastern).strftime("%A, %B %d"),
            "date_end": date_end.dt.astimezone(eastern).strftime("%A, %B %d"),
			"time_start": date_start.dt.astimezone(eastern).strftime("%H:%M:00"),
            "time_end": date_end.dt.astimezone(eastern).strftime("%H:%M:00"),
            "summary": summary,
            "description": description
        })

with open("html/vegan_calendar.json", "w") as write_file:
    json.dump(events, write_file)

os.chmod("html/vegan_calendar.json", 0o644)