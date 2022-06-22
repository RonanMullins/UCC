from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class BMIForm(FlaskForm):

    weight = DecimalField("Weight in kg:", validators=[InputRequired(), NumberRange(10, 100)])
    height = DecimalField("height in metres:", validators=[InputRequired(), NumberRange(1,25)])
    bmi = DecimalField("BMI:")
    submit = SubmitField("Submit")

