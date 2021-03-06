from application import db
from application.models import Base

class Event(Base):
    
    date = db.Column(db.Date, default=db.func.current_timestamp(), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id', ondelete='CASCADE'), nullable= False, index=True)
    distance = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete='CASCADE'), nullable=False, index=True)

    league = db.relationship("League")

    def __init__(self, date, league_id, distance, description, league):
        self.date = date
        self.league_id = league_id
        self.distance = distance
        self.description = description
        self.league = league
