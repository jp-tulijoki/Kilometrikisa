from application import db
from application.models import Base

class Sign_up(Base):

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), nullable=False)

