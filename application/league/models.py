from application import db
from application.models import Base
from application.sign_ups.models import Sign_up
from flask_login import current_user

class League(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def initialize_leagues():
        l1 = League(1, "juoksu")
        l2 = League(2, "kävely")
        l3 = League(3, "pyöräily")
        db.session().add(l1)
        db.session().add(l2)
        db.session().add(l3)
        db.session().commit()

    def get_leagues_with_sign_up():
        return League.query.join(Sign_up).filter(Sign_up.account_id == current_user.id)

    def get_leagues_with_no_sign_up():
        subquery = db.session.query(Sign_up.league_id).filter(Sign_up.account_id == current_user.id)
        return League.query.filter(League.id.notin_(subquery))

    def get_one_league(league_id):
        return League.query.get(league_id)
