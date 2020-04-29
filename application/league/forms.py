from flask_wtf import FlaskForm
from wtforms import StringField, validators

class LeagueForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3), validators.Length(max=20)])
    description = StringField("Description", [validators.Length(min=3), validators.Length(max=50)])

    class Meta:
        csrf = False