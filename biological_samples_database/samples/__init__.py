"""
Sample.
"""

# Standard
from datetime import datetime

# Flask
from flask import Blueprint, render_template

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    FloatField,
    HiddenField,
    SelectField,
    StringField
)

# Local Imports
from ..database import create_new_session
from ..model.sample import Vial
from ..model.storage import Box

SAMPLE = Blueprint(
    'sample',
    __name__,
    template_folder='templates'
)


class SampleForm(FlaskForm):
    '''Website link for page holding RSS data'''

    db_id = HiddenField('db_id')
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


def populate_edit_values(form, sample):
    """Populate a form with existing values for editing"""

    form.db_id.data = sample.id
    form.lab_id.data = sample.lab_id
    form.position.data = sample.position
    form.sample_date.data = sample.sample_date
    form.volume_ml.data = sample.volume_ml
    form.user_id.data = sample.user_id
    form.notes.data = sample.notes


def sample_search(session, sample_id, sample_class):
    """Find a sample if it exists or create a new instance"""

    sample = None
    if sample_id:
        sample = session.query(
            sample_class
        ).filter(
            sample_class.id == sample_id
        ).first()
    else:
        sample = sample_class()

    return sample


@SAMPLE.route('/<box_id>', methods=['GET'])
def box_samples(box_id):
    """Retrieve box layout of specific boxes"""

    with create_new_session() as session:

        vials = session.query(
            Vial
        ).filter(
            Vial.box_id == box_id
        ).all()

        box = session.query(
            Box
        ).filter(
            Box.id == box_id
        ).first()

        return render_template(
            'samples.html',
            samples=vials,
            box=box
        )


@SAMPLE.route('info/<box_id>/<pos>', methods=['GET'])
def samp_info(box_id, pos):
    """Return samples in a box location"""

    with create_new_session() as session:

        vials = session.query(
            Vial
        ).filter(
            Vial.box_id == box_id
        ).filter(
            Vial.position == pos
        ).all()

        return render_template(
            'sample_info.html',
            samples=vials
        )
