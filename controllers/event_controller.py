from app import app
from flask import render_template, request
from models.event_list import events, add_new_event, find_event_by_id
from models.event import Event

@app.route('/')
def index():
    return render_template('index.html', title='E&B Events', events=events)

@app.route('/events/<int:id>')
def single_event(id):
    return render_template('event_details.html', title='Single Event', events=events[id])

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['event_name']
    event_date = request.form['event_date']
    number_of_guests = request.form['number_of_guests']
    location = request.form['location']
    description = request.form['description']
    new_id = len(events) + 1
    new_event = Event(new_id, event_name, event_date, number_of_guests, location, description)
    add_new_event(new_event)
    return render_template('index.html', events=events)