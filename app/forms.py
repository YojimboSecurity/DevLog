from flask import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms.validators import Email
from wtforms.validators import Length
from wtforms.validators import Regexp
from wtforms.validators import EqualTo
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log In")
