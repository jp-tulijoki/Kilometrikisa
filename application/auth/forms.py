from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Tunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3)])
    username = StringField("Tunnus", [validators.Length(min=3)])
    password = PasswordField("Salasana")

    class Meta:
        csrf = False
