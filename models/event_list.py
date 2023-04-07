from models.event import *
import datetime

date1 = datetime.date(2000, 1, 1)
date2 = datetime.date(2002, 4, 3)
date3 = datetime.date(1969, 7, 16)

event1 = Event(1, "LAN Party", date1, 10, "Barry's House", "Get on Barry's router and get your keyboard out!", True)
event2 = Event(2, "WWF Wrestle Mania", date2, 50, "X Gym: Floor 2", "Can you smell what the rocks cookin?!", True)
event3 = Event(3, "Moon Landing",date3, 3, "NASA", "Is it made of cheese?", False)

events=[event1,event2,event3]

def find_event_by_id(id):
    for event in events:
        if event.id == id:
            return event
        return None
    
def add_new_event(event):
    events.append(event)