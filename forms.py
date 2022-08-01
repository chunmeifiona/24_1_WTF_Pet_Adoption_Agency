from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import URL, Optional, NumberRange, InputRequired

class AddPetForm(FlaskForm):
    """Form for adding pets."""
    name=StringField("Pet name", validators=[InputRequired()])
    species=SelectField("Species", choices=[('cat','cat'),('dog','dog'),('porcupine','porcupine')])
    photo_url=StringField("Photo URL", validators=[Optional(), URL()])
    age=IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes=TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?")