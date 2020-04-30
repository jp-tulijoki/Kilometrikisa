from application import db
from application.models import Base

class Sign_up(Base):

    account_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete='CASCADE'), nullable=False, index=True)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id', ondelete='CASCADE'), nullable=False, index=True)
    
    league = db.relationship("League")

