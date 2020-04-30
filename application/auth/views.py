from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm, EditProfileForm, ChangePasswordForm

#Login function with username check.
@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "Username not found. Please check that you have given your username correctly.")
    else:
        if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("index"))
        else: 
            return render_template("auth/loginform.html", form = form, error = "Invalid password. Please check that you have given your password correctly") 

#Logout
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))   

#Registation with unique username check
@app.route("/auth/registration", methods=["GET", "POST"])
def auth_registration():
    if request.method == "GET":
        return render_template("auth/registrationform.html", form = RegistrationForm())

    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/registrationform.html", form = form)

    user = User(form.name.data, form.username.data, form.role.data, bcrypt.generate_password_hash(form.password.data).decode('utf-8'))

    db.session().add(user)
    try:
        db.session().commit()
    except IntegrityError:
        db.session().rollback()
        return render_template("auth/registrationform.html", form = form, error ="Username is already taken. Please choose other username.")

    return redirect(url_for("index"))

#Profile edit form
@app.route("/auth/edit_profile", methods=["GET"])
@login_required
def edit_profile():
    user = User.query.get(current_user.id)
    form = EditProfileForm()
    form.name.data = user.name
    form.role.data = user.role
    return render_template("/auth/editnameandrole.html", form = form)

#Saving edited profile
@app.route("/auth/save_edited_profile", methods=["POST"])
@login_required
def save_edited_profile():
    form = EditProfileForm(request.form)

    user = User.query.get(current_user.id)
    user.name = form.name.data
    user.role = form.role.data

    if not form.validate_on_submit():
        return render_template("/auth/editnameandrole.html", form = form)

    db.session().commit()

    return redirect(url_for("index"))

#Change password function
@app.route("/auth/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "GET":
        return render_template("/auth/changepassword.html", form = ChangePasswordForm())
    
    form = ChangePasswordForm(request.form)
    user = User.query.get(current_user.id)

    if not form.validate_on_submit():
        return render_template("/auth/changepassword.html", form = form)

    if not bcrypt.check_password_hash(user.password, form.old_password.data):
        return render_template("/auth/changepassword.html", form = form, error = "Incorrect old password. Please check that you give correct old password")

    user.password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')

    db.session().commit()

    return redirect(url_for("index"))

#Delete user function with alert.
@app.route("/auth/delete_user", methods=["GET", "POST"])
@login_required
def delete_user():
    if request.method == "GET":
        return render_template("auth/deleteuserconfirmation.html")

    user = User.query.get(current_user.id)
    db.session().delete(user)
    db.session().commit()

    return redirect(url_for("index"))
