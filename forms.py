from flask_wtf import FlaskForm
from wtforms import StringField,  SelectField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField(
        'Species', 
        choices =[
            ('cat','cat'),
            ('dog','dog'),
            ('porcupine', 'porcupine')
        ],
        validators = [InputRequired()]
    )
    photo_url = StringField('Photo', validators=[Optional(),URL()])
    age = SelectField(
        'Age',
        choices=[
            ('baby', 'baby'),
            ('young', 'young'),
            ('adult', 'adult'),
            ('senior', 'senior')],
        validators=[InputRequired()])
    notes = StringField('Notes', validators=[Optional()])
    available = SelectField(
        'Availability', 
        choices =[
            ('true','True'),
            ('false','False')],
        validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for updating pets"""

    photo_url = StringField('Photo', validators=[Optional(),URL()])
    notes = StringField('Notes', validators=[Optional()])
    available = SelectField(
        'Availability', 
        choices =[
            ('true','True'),
            ('false','False')],
        validators=[Optional()])
