"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, Email

class AddPetForm(FlaskForm):

  name = StringField("Pet Name", validators=[InputRequired()])
  species = StringField("Species", validators=[InputRequired()])
  photo_url = StringField("Photo URL")
  age = SelectField("Age", choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')],
                    validators=[InputRequired()])
  notes = StringField("Notes")
  