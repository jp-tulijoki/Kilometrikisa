from application import db
from application.models import Base
from sqlalchemy import text

class User(Base):

    __tablename__ = "account"
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    events = db.relationship("Event", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod 
    def show_top_three_runners():
        stmt = text("SELECT Account.name, Sum(Event.distance) as total_distance FROM Account "
                    "LEFT JOIN Event ON Event.account_id = Account.id "
                    "WHERE Event.league_id = 1 "
                    "GROUP BY Account.name "
                    "ORDER BY total_distance DESC LIMIT 3")
        
        result = db.engine.execute(stmt)
        response = []
        for row in result:
            response.append({"name": row[0], "distance":row[1]})

        return response
