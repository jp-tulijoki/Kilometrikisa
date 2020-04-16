from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db, login_required
from application.league.forms import LeagueForm
from application.league.models import League

@app.route("/league/create_league", methods=["GET"])
@login_required('Organizer')
def new_league():
    return render_template("/league/new_league.html", form = LeagueForm())

@app.route("/league", methods=["POST"])
@login_required('Organizer')
def create_league():
    form = LeagueForm(request.form)

    l = League(form.name.data, form.description.data)
    l.organizer_account_id = current_user.id
  
    db.session().add(l)
    db.session().commit()
  
    return redirect(url_for("list_leagues"))

@app.route("/league/list_leagues", methods=["GET"])
@login_required('Organizer')
def list_leagues():
    return render_template("/league/list_leagues.html", leagues = League.query.filter_by(organizer_account_id=current_user.id).all())

@app.route("/league/delete/<league_id>", methods=["POST"])
@login_required('Organizer')
def delete_league(league_id):
    l = League.query.get(league_id)
    
    db.session().delete(l)
    db.session().commit()

    return redirect(url_for("list_leagues"))