from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///challenge.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.events import models
from application.events import views

from application.auth import models
from application.auth import views

from application.sign_ups import models
from application.sign_ups import views

from application.league.models import League

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Toiminto vaatii kirjautumisen."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
except:
    pass

try:
    League.initialize_leagues()
except:
    pass