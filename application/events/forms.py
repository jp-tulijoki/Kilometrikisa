from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators
from application.league.models import League

class EventForm(FlaskForm):
    date = StringField("PVM")
    league_id = SelectField("Sarja",coerce=int, choices=[(1, "juoksu"), (2, "kävely"), (3, "pyöräily")])
    distance = IntegerField("Kilometrit")
    description = StringField("Kuvaus")

 
    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    date = StringField("PVM")

    class Meta:
        csrf = False