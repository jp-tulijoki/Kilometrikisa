from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class EventForm(FlaskForm):
    date = StringField("PVM")
    sport = IntegerField("Suoritustapa")
    distance = IntegerField("Kilometrit")
    description = StringField("Kuvaus")

 
    class Meta:
        csrf = False