from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    street = StringField("From Street", validators = [DataRequired()])
    city = StringField("From City", validators = [DataRequired()])
    state = StringField("From State", validators = [DataRequired()])
    zip = StringField("From Zip", validators = [DataRequired()])
    name2 = StringField("To Name", validators = [DataRequired()])
    street2 = StringField("To Street", validators = [DataRequired()])
    city2 = StringField("To City", validators = [DataRequired()])
    state2 = StringField("To State", validators = [DataRequired()])
    zip2 = StringField("To Zip", validators = [DataRequired()])
    height = IntegerField("Height", validators = [DataRequired()])
    length = IntegerField("Length", validators = [DataRequired()])
    width = IntegerField("Width", validators = [DataRequired()])
    weight = IntegerField("Weight", validators = [DataRequired()])

    submit = SubmitField("Submit")
