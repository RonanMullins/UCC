from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, BooleanField, FloatField, RadioField
from wtforms.validators import InputRequired, NumberRange


class CipherForm(FlaskForm):

    plaintext = StringField("Plaintext:", validators=[InputRequired()])
    shift = IntegerField("Shift:", validators=[InputRequired(), NumberRange(1,25)])
    ciphertext = StringField("Ciphertext:")
    submit = SubmitField("Submit")

class ConversionForm(FlaskForm):

    fahrenheit_from = BooleanField("Fahrenheit:")
    celsius_from = BooleanField("Celsius:")
    kelvin_from = BooleanField("Kelvin:")

    input = FloatField()

    fahrenheit_to = BooleanField("Fahrenheit:")
    celsius_to = BooleanField("Celsius:")
    kelvin_to = BooleanField("Kelvin:")

    answer = FloatField()

    submit = SubmitField("Submit")
