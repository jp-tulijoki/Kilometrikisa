from application import db
from application.models import Base
from application.sign_ups.models import Sign_up
from flask_login import current_user

class League(Base):

    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    organizer_account_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete='CASCADE'), nullable=False)

    event = db.relationship("Event", backref="League", lazy=True, cascade="all, delete")
    sign_up = db.relationship("Sign_up", backref="League", lazy=True, cascade="all, delete")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_leagues_with_sign_up():
        return League.query.join(Sign_up).filter(Sign_up.account_id == current_user.id)

    def get_leagues_with_no_sign_up():
        subquery = db.session.query(Sign_up.league_id).filter(Sign_up.account_id == current_user.id)
        return League.query.filter(League.id.notin_(subquery))

    def get_one_league(league_id):
        return League.query.get(league_id)
