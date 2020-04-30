from application import db
from application.models import Base
from application.sign_ups.models import Sign_up
from flask_login import current_user
from random import randint
from sqlalchemy import text

class League(Base):

    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    organizer_account_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete='CASCADE'), nullable=False, index=True)

    event = db.relationship("Event", backref="League", lazy=True, cascade="all, delete")
    sign_up = db.relationship("Sign_up", backref="League", lazy=True, cascade="all, delete")

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def get_all_leagues():
        return League.query.filter()
    
    def get_leagues_with_sign_up():
        return League.query.join(Sign_up).filter(Sign_up.account_id == current_user.id)

    def get_leagues_with_no_sign_up():
        subquery = db.session.query(Sign_up.league_id).filter(Sign_up.account_id == current_user.id)
        return League.query.filter(League.id.notin_(subquery))

    def get_one_league(league_id):
        return League.query.get(league_id)

    # Returns a random league for random stats in index. 
    def get_random_league():
        league_query = db.session.query(League.id).all()
        league_ids = []
        for row in league_query:
            league_ids.append(row[0])
        random = randint(0, len(league_ids) - 1)
        league_id = league_ids[random]

        return League.query.get(league_id)

    #Parametrized standings aggregate query    
    def standings(league_id, limit):

        stmt = text("SELECT Account.name, Sum(Event.distance) as total_distance FROM Account "
                    "LEFT JOIN Event ON Event.account_id = Account.id "
                    "WHERE Event.league_id = :league_id "
                    "GROUP BY Account.name "
                    "ORDER BY total_distance DESC LIMIT :limit").params(league_id = league_id, limit = limit)
        
        result = db.engine.execute(stmt)
        response = []
        for row in result:
            response.append({"name": row[0], "distance":row[1]})

        return response

    #Aggregate query for most popular leagues
    def three_leagues_with_most_sign_ups():

        stmt = text("SELECT League.name, Count(Sign_up.league_id) as sign_ups FROM League "
                    "LEFT JOIN Sign_up ON Sign_up.league_id = League.id "
                    "GROUP BY League.name "
                    "ORDER BY sign_ups DESC LIMIT 3")
        
        result = db.engine.execute(stmt)
        response = []
        for row in result:
            response.append({"league_name": row[0], "sign_ups": row[1]})

        return response

