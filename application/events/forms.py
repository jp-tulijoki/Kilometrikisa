from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from application.league.models import League
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField

class EventForm(FlaskForm):
    date = DateField("Date")
    league = QuerySelectField(u'League', query_factory=League.get_leagues_with_sign_up, get_label='name')
    distance = IntegerField("Distance (kilometers)", [validators.data_required()])
    description = StringField("Description")

 
    class Meta:
        csrf = False

