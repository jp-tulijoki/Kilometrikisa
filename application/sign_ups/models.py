from application import db
from application.models import Base

class Sign_up(Base):

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(account_id, league_id):
        self.account_id = account_id
        self.league_id = league_id 