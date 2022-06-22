from email.policy import default
from wsgiref.validate import validator
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, RadioField
from wtforms.validators import InputRequired

class AliveForm(FlaskForm):
    alive = BooleanField("Check the box if you think Elvis is still alive:")
    submit = SubmitField("Submit")

class ToppingForm(FlaskForm):
    topping = RadioField("Which topping do you think Elvis prefers?",
        choices= ["anchovies","chocolate", "morphine", "chocolate"],
        default = "morphine")
    submit = SubmitField("Submit")


