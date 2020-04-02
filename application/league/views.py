from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.league import models

@app.route("/league/sign_up/<league_id>", methods=["POST"])
@login_required
def sign_up():
    l = League.query.get(league_id)
    l.account_id = current_user.id 

    def __init__



