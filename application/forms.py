from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Optional, EqualTo

class LineupForm(FlaskForm):
    email = StringField(
        "Email", [Length(min = 6), Email(message = "Invalid email address"), DataRequired()]
    )
    phone = StringField("Phone (Optional)", [Optional()])
    submit = SubmitField("Lineup")
    recaptcha = RecaptchaField()


class SignupForm(FlaskForm):
    email = StringField(
        "Email", [Length(min = 6), Email(message = "Invalid email address"), DataRequired()]
        )
    password = PasswordField(
        "Password", [Length(min = 8, message="Password too short"), DataRequired()]
    )
    confirm = PasswordField(
        "Confirm", [EqualTo("password", message="Passwords donot match"), DataRequired()]
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField(
        "Email", [Email(message="Invalid email address"), DataRequired()]
    )
    password = PasswordField(
        "Password", [DataRequired()]
    )
    submit = SubmitField("Log In")