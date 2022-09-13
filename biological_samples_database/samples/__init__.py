"""
Sample.
"""

# Standard
from datetime import datetime

# Flask
from flask import Blueprint

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    FloatField,
    HiddenField,
    IntegerField,
    SelectField,
    StringField
)

SAMPLE = Blueprint(
    'sample',
    __name__,
    template_folder='templates'
)


class SampleForm(FlaskForm):
    '''Website link for page holding RSS data'''

    lab_id = StringField('ID')
    box_id = SelectField('Box')
    position = StringField('Position')
    sample_date = DateField('Sample Date', format='%Y-%m-%d')
    volume_ml = FloatField('Volume (ml)')
    user_id = HiddenField('User ID')
    notes = StringField('Notes')


def populate_default_values(request, sample):
    """Populates the default sample values of a sample"""

    sample.lab_id = request.form.get('lab_id')
    sample.box_id = request.form.get('box_id')
    sample.position = request.form.get('position')
    sample.sample_date = datetime.strptime(
        request.form.get('sample_date'),
        '%Y-%m-%d'
    )
    sample.volume_ml = request.form.get('volume_ml')
    sample.user_id = request.form.get('user_id')
    sample.notes = request.form.get('notes')
