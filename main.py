import json
from ics import Calendar, Event
from datetime import datetime

def generate_calendar():
    with open("fighters.json", "r", encoding="utf-8") as f:
        fighters = json.load(f)

    cal = Calendar()

    for fighter in fighters:
        event = Event()
        event.name = f"{fighter['name']} vs {fighter['opponent']}"
        event.begin = datetime.strptime(fighter["date"], "%Y-%m-%d %H:%M:%S")
        event.location = fighter["location"]
        event.description = fighter["description"]
        cal.events.add(event)

    with open("calendar.ics", "w", encoding="utf-8") as f:
        f.writelines(cal)

if __name__ == "__main__":
    generate_calendar()
