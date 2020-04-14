from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.events.models import Event
from application.events.forms import EventForm
from application.league.models import League
from application.sign_ups.models import Sign_up

@app.route("/events/new_event", methods=["GET"])
@login_required
def new_event():
    return render_template("/events/new_event.html", form = EventForm(), sign_ups = Sign_up.query.filter_by(account_id=current_user.id).all())

@app.route("/events", methods=["POST"])
@login_required
def create_event():
    form = EventForm(request.form)

    if not form.validate():
        return render_template("/events/new_event.html", form = form)

    e = Event(form.date.data, form.league.data.id, form.distance.data, form.description.data, form.league.data)
    e.account_id = current_user.id
  
    db.session().add(e)
    db.session().commit()
  
    return redirect(url_for("list_events"))

@app.route("/events/list_events", methods=["GET"])
@login_required
def list_events():
    return render_template("/events/list_events.html", events = Event.query.filter_by(account_id=current_user.id).all())

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


@app.route("/events/<event_id>", methods=["POST"])
@login_required
def save_event(event_id):
    form = EventForm(request.form)
    e = Event.query.get(event_id)
    e.date = form.date.data
    e.league_id = form.league.data.id
    e.distance = form.distance.data
    e.description = form.description.data
    e.league = form.league.data
    db.session().commit()

    return redirect(url_for("list_events"))

@app.route("/events/delete/<event_id>", methods=["POST"])
@login_required
def delete_event(event_id):
    e = Event.query.get(event_id)
    db.session().delete(e)
    db.session().commit()

    return redirect(url_for("list_events"))