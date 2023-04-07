

class Event():

    def __init__(self, id, event_name, event_date, number_of_guests, location, description, recurring):
        self.id = id
        self.event_name = event_name
        self.event_date = event_date
        self.number_of_guests = number_of_guests
        self.location = location
        self.description = description 
        self.reccuring = recurring
