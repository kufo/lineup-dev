from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional

class LineupForm(FlaskForm):
    email = StringField(
        "Email", [Length(min = 6), Email(message = "Invalid email address"), DataRequired()]
    )
    phone = StringField("Phone (Optional)", [Optional()])
    submit = SubmitField("Lineup")