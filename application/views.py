from flask import render_template
from flask_login import current_user
from application import app
from application.auth.models import User
from application.league.models import League

@app.route('/')
def index():
    league = League.query.first()

    if not league:
        return render_template("index.html")

    random_league = League.get_random_league()
    random_league_name = random_league.name
    random_top_three = League.standings(random_league.id, 3)
    top_three_leagues = League.three_leagues_with_most_sign_ups()

    return render_template("index.html", random_top_three=random_top_three, random_league_name = random_league_name, top_three_leagues = top_three_leagues)