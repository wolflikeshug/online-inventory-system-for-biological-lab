"""

Serum

All API information related to Serum samples

"""

# Flask
from flask import Blueprint, redirect, request

# Flask WTF
from wtforms import StringField

# Local Imports
from .. import (
    SampleForm,
    all_samples_page,
    build_sample_copy_form,
    build_sample_edit_form,
    build_sample_form,
    build_sample_form_in_pos,
    delete_sample,
    sample_create
)
from ...model.sample import Serum


SERUM = Blueprint(
    'serum',
    __name__,
    template_folder='templates'
)
SERUM_CUSTOM_VARIABLES = ['pathwest_id']


class SerumForm(SampleForm):
    '''Form for handling Serum data'''

    pathwest_id = StringField('PathWest ID')


@SERUM.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    return sample_create(request, Serum, SERUM_CUSTOM_VARIABLES)


@SERUM.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Serum data from the SQLite database"""

    return all_samples_page('serum', Serum, SerumForm)


@SERUM.route('/create/', methods=['GET'])
def create_serum():
    """Provide the HTML form for serum creation"""

    sample_title = 'Add Serum'
    return build_sample_form(sample_title, 'serum', SerumForm)

@SERUM.route('/create/<box_id>/<pos>', methods=['GET'])
def create_serum_in_pos(box_id, pos):
    """Provide the HTML form for serum creation"""
    sample_title = 'Add Serum'
    return build_sample_form_in_pos(sample_title, 'serum', SerumForm, box_id, pos)

@SERUM.route('/edit/<serum_id>', methods=['GET'])
def edit_serum_form(serum_id):
    """Provide the HTML form for Serum creation"""

    sample_title = 'Edit Serum'
    return build_sample_edit_form(
        sample_title,
        serum_id,
        'serum',
        SerumForm,
        Serum,
        SERUM_CUSTOM_VARIABLES
    )

@SERUM.route('/copy/<serum_id>', methods=['GET'])
def copy_serum_form(serum_id):
    """Provide the HTML form for Serum copy"""

    sample_title = 'Copy Sample: Serum'
    return build_sample_copy_form(
        sample_title,
        serum_id,
        'serum',
        SerumForm,
        Serum,
        SERUM_CUSTOM_VARIABLES
    )



@SERUM.route('/delete/<serum_id>', methods=['GET'])
def delete_serum_form(serum_id):
    """Delete a Serum item using ID"""

    delete_sample(Serum, serum_id)

    return redirect(request.referrer)
