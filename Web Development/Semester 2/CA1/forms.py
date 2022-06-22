from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, FloatField, RadioField
from wtforms.fields import DateField
from wtforms.validators import InputRequired, EqualTo

class LoginForm(FlaskForm):
    user_id = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Submit")

class RegistrationForm(FlaskForm):
    user_id = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    password2 = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Submit")

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    message = TextAreaField("Message", validators=[InputRequired()])
    submit = SubmitField("Submit")

class AddForm(FlaskForm):
    add_name = StringField("Name", validators=[InputRequired()])
    add_type = StringField("Type", validators=[InputRequired()])
    add_price = FloatField("Price", validators=[InputRequired()])
    add_description = StringField("Description", validators=[InputRequired()])
    image_file = StringField("Image File Name", validators=[InputRequired()])
    submit = SubmitField("Add Product")

class RemoveForm(FlaskForm):
    instrument_id = StringField("Instrument id", validators=[InputRequired()])
    submit = SubmitField("Remove Product")

class OrderForm(FlaskForm):
    discount_code = StringField("Discount Code")
    delivery = RadioField("Delivery", 
    choices= ["Standard Delivery (€3)","Next-Day Delivery (€12)"])
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])
    submit = SubmitField("Order Now")

class RemoveOrderForm(FlaskForm):
    order_no = StringField("Order No.", validators=[InputRequired()])
    submit = SubmitField("Cancel Order")