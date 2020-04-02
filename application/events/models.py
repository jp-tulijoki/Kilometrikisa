from application import db
from application.models import Base



class Event(Base):
    
    date = db.Column(db.String(144), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), nullable= False)
    distance = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, date, league_id, distance, description):
        self.date = date
        self.league_id = league_id
        self.distance = distance
        self.description = description
