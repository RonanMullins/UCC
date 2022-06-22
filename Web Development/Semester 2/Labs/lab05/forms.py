from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class GuessForm(FlaskForm):
    guess = StringField("Guess:", validators=[InputRequired()])
    submit = SubmitField("Submit:")
