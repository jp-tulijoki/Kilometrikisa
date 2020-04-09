from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.sign_ups.models import Sign_up
from application.sign_ups.forms import SignUpForm

@app.route("/sign_ups/new_sign_up", methods=["GET"])
@login_required
def new_sign_up():
    return render_template("/sign_ups/new_sign_up.html", form = SignUpForm())

@app.route("/sign_ups", methods=["POST"])
@login_required
def create_sign_up():
    form = SignUpForm(request.form)

    s = Sign_up()
    s.account_id = current_user.id
    s.league_id = form.league.data.id
  
    db.session().add(s)
    db.session().commit()
  
    return redirect(url_for("list_sign_ups"))

@app.route("/sign_ups/list_sign_ups", methods=["GET"])
@login_required
def list_sign_ups():
    return render_template("/sign_ups/list_sign_ups.html", sign_ups = Sign_up.query.filter_by(account_id=current_user.id).all())

@app.route("/sign_ups/remove/<sign_up_id>", methods=["POST"])
@login_required
def remove_sign_up(sign_up_id):
    s = Sign_up.query.get(sign_up_id)
    db.session().delete(s)
    db.session().commit()

    return redirect(url_for("list_sign_ups"))
