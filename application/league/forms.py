from flask_wtf import FlaskForm
from wtforms import StringField

class LeagueForm(FlaskForm):
    name = StringField("Name")
    description = StringField("Description")

    class Meta:
        csrf = False