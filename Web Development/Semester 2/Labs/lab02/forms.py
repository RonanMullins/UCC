from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, StringField
from wtforms.validators import InputRequired, NumberRange

class DSMForm(FlaskForm):

    inches = DecimalField("Inches:", validators=[InputRequired(), NumberRange(0, 999999)])
    centimetres = DecimalField("Centimetres:", validators=[InputRequired(), NumberRange(0,999999)])
    error = StringField("")
    submit = SubmitField("Submit")

