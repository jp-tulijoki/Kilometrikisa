from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sys import maxsize
from sqlalchemy.exc import IntegrityError

from application import app, db, login_required
from application.league.forms import LeagueForm, StandingsFilter
from application.league.models import League

#League creation form
@app.route("/league/create_league", methods=["GET"])
@login_required('Organizer')
def new_league():
    return render_template("/league/new_league.html", form = LeagueForm())

#Saving new league and a check for unique name
@app.route("/league", methods=["POST"])
@login_required('Organizer')
def create_league():
    form = LeagueForm(request.form)

    if not form.validate():
        return render_template("/league/new_league.html", form = form)

    l = League(form.name.data, form.description.data)
    l.organizer_account_id = current_user.id
  
    db.session().add(l)
    try:
        db.session().commit()
    except IntegrityError:
        db.session.rollback()
        return render_template("/league/new_league.html", form = form, error = "League name is already in use. Please choose another league name.")
  
    return redirect(url_for("list_leagues"))

#League list
@app.route("/league/list_leagues", methods=["GET"])
@login_required('Organizer')
def list_leagues():
    return render_template("/league/list_leagues.html", leagues = League.query.filter_by(organizer_account_id=current_user.id).all())

#League edit form
@app.route("/league/<league_id>", methods=["GET"])
@login_required('Organizer')
def edit_league(league_id):
    l = League.query.get(league_id)
    form = LeagueForm()
    form.name.data = l.name
    form.description.data = l.description
    return render_template("/league/edit_league.html", form = form, league_id = league_id)

#Saving edited league and check for unique name
@app.route("/league/<league_id>", methods=["POST"])
@login_required('Organizer')
def save_edited_league(league_id):
    form = LeagueForm(request.form)

    if not form.validate():
        return render_template("/league/edit_league.html", form = form, league_id = league_id)

    l = League.query.get(league_id)
    l.name = form.name.data
    l.description = form.description.data
    
    try:
        db.session().commit()
    except IntegrityError:
        db.session.rollback()
        return render_template("/league/new_league.html", form = form, error = "League name is already in use. Please choose another league name.")
    return redirect(url_for("list_leagues"))

#League deletion function with alert
@app.route("/league/delete/<league_id>", methods=["GET","POST"])
@login_required('Organizer')
def delete_league(league_id):
    league = League.query.get(league_id)
    
    if request.method == "GET":
        return render_template("league/deleteleagueconfirmation.html", league = league)

    db.session().delete(league)
    db.session().commit()

    return redirect(url_for("list_leagues"))

#Function for getting standings of a certain league
@app.route("/league/standingsfilter", methods=["GET"])
def standingsfilter():
    league = League.query.first()

    if not league:
        return render_template("/league/nostandingsavailable.html")

    return render_template("league/standings.html", form = StandingsFilter())

#Returns requested standings
@app.route("/league/standings", methods=["POST"])
def filtered_standings():
    form = StandingsFilter(request.form)
    league_id = form.league.data.id
    league_name = form.league.data.name

    standings = League.standings(league_id, maxsize)

    return render_template("league/standings.html", form = StandingsFilter(), standings = standings, league_name = league_name)
