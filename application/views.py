from flask import render_template
from application import app
from application.auth.models import User

@app.route('/')
def index():
    return render_template("index.html", top_three_runners=User.show_top_three_runners())