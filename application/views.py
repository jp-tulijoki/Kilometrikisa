from flask import render_template
from flask_login import current_user
from application import app
from application.auth.models import User
from application.league.models import League

@app.route('/')
def index():
    league = League.get_random_league()
    league_name = league.name
    top_three = League.show_top_three_in_random_league(league.id)

    return render_template("index.html", top_three=top_three, league_name = league_name)