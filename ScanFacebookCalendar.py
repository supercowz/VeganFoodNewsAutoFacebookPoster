from icalendar import Calendar
from datetime import *
from pytz import timezone
from collections import OrderedDict

import requests
import json
import os

# Set the timezone we are going to use
eastern = timezone('US/Eastern')

class Event:
    def __init__(self, date_start, date_end, summary, description):
        self.fulldate = date_start.dt
        self.date_start = date_start.dt.astimezone(eastern).strftime("%A, %B %d")
        self.date_end = date_end.dt.astimezone(eastern).strftime("%A, %B %d")
        self.time_start = date_start.dt.astimezone(eastern).strftime("%H:%M:00")
        self.time_end = date_end.dt.astimezone(eastern).strftime("%H:%M:00")
        self.summary = summary
        self.description = description

# We don't want to include events that have already occured.
def removePastEvents(events):
    eventsToReturn = []
    for event in events:
        if (event.fulldate.date() >= date.today()):
            eventsToReturn.append(event)

    return eventsToReturn

# Take a sorted list of class=Event and group it by day and convert it to JSON.
# The reason this won't be sorted is because a dictionary has keys in random order , need to find a way to represent it in an ordered way that is simular to how a dictionary works.
def getEventsInJSONGroupedByDay(events):
    jsonGroupedEvents = {}
    for event in events:
        dKey = event.date_start
        if (not dKey in jsonGroupedEvents):
            jsonGroupedEvents[dKey] = []
        jsonGroupedEvents[dKey].append(event.__dict__)
    return jsonGroupedEvents

def writeJsonFile(events):
    def converter(o):
        if isinstance(o, datetime):
            return o.__str__()

    dictEvents = [event.__dict__ for event in events]
    with open("html/vegan_calendar.json", "w") as write_file:
        json.dump(dictEvents, write_file, default=converter)

    os.chmod("html/vegan_calendar.json", 0o644)

def convertCalendarToListOfEvents(gcal):
    events = []
    for component in gcal.walk():
        if component.name == "VEVENT":
            #uid = component.get('uid')
            #organzier = component.get('organizer')
            date_start = component.get('dtstart')
            date_end = component.get('dtend')
            summary = component.get('summary')
            description = component.get('description')
            events.append(Event(date_start, date_end, summary, description))
    return events

def main():
    url = "https://www.facebook.com/events/ical/upcoming/?uid=100005885022646&key=219ODd1jNxGCrqhc"

    response = requests.get(url)

    gcal = Calendar.from_ical(response.text)
    events = convertCalendarToListOfEvents(gcal)

    # Remove events that have already occured
    events = removePastEvents(events)

    # sort the events by the full date descending
    events = sorted(events, key=lambda o: o.fulldate)

    # group the events by day and convert to JSON
    #jsonGroupedEvents = getEventsInJSONGroupedByDay(events)

    # Write the final JSON write_file
    writeJsonFile(events)

main()
