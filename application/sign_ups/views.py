from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.league.models import League

@app.route("/sign_ups/sign_up/<league_id>", methods=["POST"])
@login_required
def sign_up():
    s = Sign_up.query.get(league_id)
    s.account_id = current_user.id
    db.session().add(s)
    db.session().commit()

    return "Hello world!"

@app.route("/sign_ups/list_leagues", methods=["GET"])
@login_required
def list_leagues():
    return render_template("/sign_ups/list_sign_ups.html", leagues = League.query.all())
