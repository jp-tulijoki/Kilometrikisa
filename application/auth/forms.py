from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3), validators.Length(max=20)])
    username = StringField("Username", [validators.Length(min=3), validators.Length(max=20)])
    role = SelectField('Role', choices=[('User', 'Normal user'), ('Organizer', 'Organizer')])
    password = PasswordField("Password", [validators.length(min=8)])

    class Meta:
        csrf = False

class EditProfileForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3), validators.Length(max=20)])
    role = SelectField('Role', choices=[('User', 'Normal user'), ('Organizer', 'Organizer')])

    class Meta:
        csrf = False

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old password", [validators.data_required])
    new_password = PasswordField("New password", [validators.length(min=8), validators.data_required])

    class Meta:
        csrf = False
