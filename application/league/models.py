from application import db
from application.models import Base
import enum
from sqlalchemy import Integer, Enum

class LeagueTypes(enum.Enum):
    
    juoksu = 1
    kävely = 2
    pyöräily = 3

class League(Base):

    id = db.Column(Integer, primary_key=True)
    league = db.Column(Enum(LeagueTypes))

    def get_league_list():
        return League.query

