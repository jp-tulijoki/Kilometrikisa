from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class EventForm(FlaskForm):
    date = StringField("PVM")
    sport = IntegerField("Suoritustapa")
    distance = IntegerField("Kilometrit")
    description = StringField("Kuvaus")

 
    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    date = StringField("PVM")

    class Meta:
        csrf = False