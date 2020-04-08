from flask_wtf import FlaskForm
from application.league.models import League
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class SignUpForm(FlaskForm):

    league = QuerySelectField(u'Suoritustapa', query_factory=League.get_leagues_with_no_sign_up, get_label='name')

    class Meta:
        csrf = False