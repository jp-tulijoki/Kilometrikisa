from application import db
from application.models import Base

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

    def get_league_list():
        return League.query

