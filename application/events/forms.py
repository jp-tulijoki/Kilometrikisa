from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators
from application.league.models import League
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField
from sys import maxsize

class EventForm(FlaskForm):
    date = DateField("Date")
    league = QuerySelectField(u'League', query_factory=League.get_leagues_with_sign_up, get_label='name')
    distance = IntegerField("Distance (kilometers)", [validators.NumberRange(min=1)])
    description = StringField("Description")

    class Meta:
        csrf = False

class EventFilter(FlaskForm):
    league = QuerySelectField(u'Select league', query_factory=League.get_leagues_with_sign_up, get_label='name')
    sort = SelectField('Sort by', choices=[('date', 'Date'), ('distance', 'Distance')])
    order = SelectField('Order', choices=[('asc', 'Ascending'), ('desc', 'Descending')])
    number = SelectField('Number of results', choices=[(10, '10'), (25, '25'), (50, '50'), (maxsize, 'All')])

    class Meta:
        csrf = False