from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.challenge.events.models import Event
from application.challenge.events.forms import EventForm

@app.route("/challenge/events/new_event", methods=["GET"])
def new_event():
    return render_template("challenge/events/new_event.html", form = EventForm())

@app.route("/challenge/events", methods=["POST"])
def create_event():
    form = EventForm(request.form)

    e = Event(form.date.data, form.sport.data, form.distance.data, form.description.data)
    e.account_id = current_user.id
  
    db.session().add(e)
    db.session().commit()
  
    return redirect(url_for("list_events"))

@app.route("/challenge/events/list_events", methods=["GET"])
def list_events():
    return render_template("/challenge/events/list_events.html", events = Event.query.all())