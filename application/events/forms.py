from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from application.league.models import League
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class EventForm(FlaskForm):
    date = StringField("PVM")
    league = QuerySelectField(u'Suoritustapa', query_factory=League.get_league_list, get_label='name')
    distance = IntegerField("Kilometrit")
    description = StringField("Kuvaus")

 
    class Meta:
        csrf = False

