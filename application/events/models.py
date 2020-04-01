from application import db
from application.models import Base

class Event(Base):
    
    date = db.Column(db.String(144), nullable=False)
    sport = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, date, sport, distance, description):
        self.date = date
        self.sport = sport
        self.distance = distance
        self.description = description
