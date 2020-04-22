from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm, EditProfileForm

@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Username not found. Please check that you have given your username correctly.")
    else:
        if bcrypt.check_password_hash(user.password, form.password.data):
            print("Tervetuloa, " + user.name + "!")
            login_user(user)
            return redirect(url_for("index"))
        else: 
            return render_template("auth/loginform.html", form = form,
                               error = "Invalid password. Please check that you have given your password correctly") 

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
            return render_template("auth/registrationform.html", form = form, error ="Username is already taken. Please choose other username.")

    user = User(form.name.data, form.username.data, form.role.data, bcrypt.generate_password_hash(form.password.data).decode('utf-8'))

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/auth/edit_profile", methods=["GET"])
@login_required
def edit_profile():
    u = User.query.get(current_user.id)
    form = EditProfileForm()
    form.name.data = u.name
    form.role.data = u.role
    return render_template("/auth/editprofile.html", form = form)


@app.route("/auth/save_edited_profile", methods=["POST"])
@login_required
def save_edited_profile():
    form = EditProfileForm(request.form)

    u = User.query.get(current_user.id)
    u.name = form.name.data
    u.role = form.role.data

    if not form.validate_on_submit():
        return render_template("/auth/editprofile.html", form = form)

    db.session().commit()

    return redirect(url_for("index"))



