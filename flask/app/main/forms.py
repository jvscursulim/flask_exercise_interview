from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CustomersForm(FlaskForm):
    
    name = StringField("Name: ")
    submit = SubmitField("Submit")

class CarsForm(FlaskForm):
    
    customer = StringField("Customer: ", validators=[DataRequired()])
    model = SelectField("Model", choices=["convertible", "hatch", "sedan"])
    color = SelectField("Color", choices=["blue", "gray", "yellow"])
    submit = SubmitField("Submit")
