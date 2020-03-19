from application import app, db
from flask import redirect, render_template, request, url_for
from application.challenge.models import Contestant

@app.route("/challenge/", methods=["GET"])
def list_contestants():
    return render_template("challenge/list_contestants.html", contestants = Contestant.query.all())

@app.route("/challenge/new_contestant/")
def new_contestant():
    return render_template("challenge/new_contestant.html")

@app.route("/challenge/", methods=["POST"])
def create_contestant():
    c = Contestant(request.form.get("Nimi: "))

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("list_contestants"))
