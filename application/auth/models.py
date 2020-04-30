from application import db
from application.models import Base
from sqlalchemy import text
from random import randint

from application.league.models import League

class User(Base):

    __tablename__ = "account"
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    role = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    events = db.relationship("Event", backref='account', lazy=True, cascade='all, delete')
    league = db.relationship("League", backref='account', lazy=True, cascade='all, delete')
    sign_ups = db.relationship("Sign_up", backref='account', lazy=True, cascade='all, delete')

    def __init__(self, name, username, role, password):
        self.name = name
        self.username = username
        self.role = role
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_role(self):
        return self.role
