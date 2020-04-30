from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.events.models import Event
from application.events.forms import EventForm, EventFilter
from application.league.models import League
from application.sign_ups.models import Sign_up
from sqlalchemy import desc

#Form for new event
@app.route("/events/new_event", methods=["GET"])
@login_required
def new_event():
    return render_template("/events/new_event.html", form = EventForm(), sign_ups = Sign_up.query.filter_by(account_id=current_user.id).all())

#Saving new event to the database
@app.route("/events", methods=["POST"])
@login_required
def create_event():
    form = EventForm(request.form)

    if not form.validate():
        return render_template("/events/new_event.html", form = form, sign_ups = Sign_up.query.filter_by(account_id=current_user.id).all())

    e = Event(form.date.data, form.league.data.id, form.distance.data, form.description.data, form.league.data)
    e.account_id = current_user.id
  
    db.session().add(e)
    db.session().commit()
  
    return redirect(url_for("list_events"))

#Events list
@app.route("/events/list_events", methods=["GET"])
@login_required
def list_events():
    return render_template("/events/list_events.html", form = EventFilter(), events = Event.query.filter_by(account_id=current_user.id).all())

#Events filter function
@app.route("/events/filter_events", methods=["POST"])
@login_required
def filter_events():
    form = EventFilter(request.form)
    league_id = form.league.data.id
    sort = form.sort.data
    order = form.order.data
    number = form.number.data

    if order == "asc":
        return render_template("/events/list_events.html", form = form, events = Event.query.filter_by(league_id = league_id).\
        filter_by(account_id=current_user.id).order_by(sort).limit(number))

    return render_template("/events/list_events.html", form = form, events = Event.query.filter_by(league_id = league_id).\
        filter_by(account_id=current_user.id).order_by(desc(sort)).limit(number))

#Edit event form
@app.route("/events/<event_id>", methods=["GET"])
@login_required
def edit_event(event_id):
    e = Event.query.get(event_id)
    form = EventForm()
    form.date.data = e.date
    form.league.data = e.league
    form.distance.data = e.distance
    form.description.data = e.description
    return render_template("/events/edit_event.html", form = form, event_id = event_id)

#Saving edited event
@app.route("/events/<event_id>", methods=["POST"])
@login_required
def save_event(event_id):
    form = EventForm(request.form)

    if not form.validate():
        return render_template("/events/edit_event.html", form = form, event_id = event_id)

    e = Event.query.get(event_id)
    e.date = form.date.data
    e.league_id = form.league.data.id
    e.distance = form.distance.data
    e.description = form.description.data
    e.league = form.league.data
    db.session().commit()

    return redirect(url_for("list_events"))

#Deletes event directly, no alert
@app.route("/events/delete/<event_id>", methods=["POST"])
@login_required
def delete_event(event_id):
    e = Event.query.get(event_id)
    db.session().delete(e)
    db.session().commit()

    return redirect(url_for("list_events"))