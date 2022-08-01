from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    name=StringField("Pet name")
    species=SelectField("Species", choices=[('cat','cat'),('dog','dog'),('porcupine','porcupine')])
    photo_url=StringField("Photo URL", validators=[Optional(), URL()])
    age=IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes=TextAreaField("Notes")