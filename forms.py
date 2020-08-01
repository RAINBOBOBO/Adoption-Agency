"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, Email, AnyOf, URL

#can move these to models to make it cleaner
age_choices = [('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')]
ages = [choice[0] for choice in age_choices]


#docstrings for these

class AddPetForm(FlaskForm):
    #set constants for long lists

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField("Age", choices=[('select_age', 'Select Age')] + age_choices,
                      validators=[InputRequired(), AnyOf(ages)])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = SelectField('Available', choices=[(True, 'True'), (False, 'False')])
    #BooleanField instead of SelectField