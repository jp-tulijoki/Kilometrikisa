from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3), validators.Length(max=20)])
    username = StringField("Username", [validators.Length(min=3), validators.Length(max=20)])
    password = PasswordField("Password", [validators.length(min=8)])

    class Meta:
        csrf = False
