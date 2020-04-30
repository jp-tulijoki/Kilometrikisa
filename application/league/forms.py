from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField, validators

from application.league.models import League

class LeagueForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3), validators.Length(max=20)])
    description = StringField("Description", [validators.Length(min=3), validators.Length(max=50)])

    class Meta:
        csrf = False

class StandingsFilter(FlaskForm):
    league = QuerySelectField(u'League', query_factory=League.get_all_leagues, get_label='name')

    class Meta:
        csrf = False