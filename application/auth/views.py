from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm

@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjää ei löydy")
    else:
        if bcrypt.check_password_hash(user.password, form.password.data):
            print("Tervetuloa, " + user.name + "!")
            login_user(user)
            return redirect(url_for("index")) 

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))   

@app.route("/auth/registration", methods=["GET", "POST"])
def auth_registration():
    if request.method == "GET":
        return render_template("auth/registrationform.html", form = RegistrationForm())

    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/registrationform.html", form = form)
    else:
        user = User.query.filter_by(username=form.username.data).first()

        if user:
            return render_template("auth/registrationform.html", form = form, error ="Haluamasi tunnus on jo varattu.")

    user = User(form.name.data, form.username.data, bcrypt.generate_password_hash(form.password.data).decode('utf-8'))

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("index"))



