"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, Email, AnyOf, URL


class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField("Age", choices=[('select_age', 'Select Age'), ('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')],
                      validators=[InputRequired(), AnyOf(['baby', 'young', 'adult', 'senior'])])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = SelectField('Available', choices=[(True, 'True'), (False, 'False')])