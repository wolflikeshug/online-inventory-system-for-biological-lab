"""

Plasma.

All API information related to Plasma samples

"""

# Flask
from flask import Blueprint, redirect, request

# Flask WTF
from wtforms import StringField


# Local Imports
from .. import (
    SampleForm,
    all_samples_page,
    build_sample_edit_form,
    build_sample_form,
    build_sample_form_in_pos,
    delete_sample,
    sample_create
)
from ...model.sample import Plasma


PLASMA = Blueprint(
    'plasma',
    __name__,
    template_folder='templates'
)
PLASMA_CUSTOM_VARIABLES = ['visit_number']


class PlasmaForm(SampleForm):
    '''Sample specific data'''

    visit_number = StringField('Visit Number')


@PLASMA.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    return sample_create(request, Plasma, PLASMA_CUSTOM_VARIABLES)


@PLASMA.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Plasma data from the SQLite database"""

    return all_samples_page('plasma', Plasma, PlasmaForm)


@PLASMA.route('/create/', methods=['GET'])
def create_plasma_form():
    """Provide the HTML form for plasma creation"""

    sample_title = 'Add Plasma'
    return build_sample_form(sample_title, 'plasma', PlasmaForm)

@PLASMA.route('/create/<box_id>/<pos>', methods=['GET'])
def create_plasma_form_in_pos(box_id, pos):
    """Provide the HTML form for plasma creation"""

    sample_title = 'Add Plasma'
    return build_sample_form_in_pos(sample_title, 'plasma', PlasmaForm, box_id, pos)


@PLASMA.route('/edit/<plasma_id>', methods=['GET'])
def edit_plasma_form(plasma_id):
    """Provide the HTML form for Plasma creation"""

    sample_title = 'Edit Plasma'
    return build_sample_edit_form(
        sample_title,
        plasma_id,
        'plasma',
        PlasmaForm,
        Plasma,
        PLASMA_CUSTOM_VARIABLES
    )


@PLASMA.route('/delete/<plasma_id>', methods=['GET'])
def delete_plasma_form(plasma_id):
    """Delete a Plasma item using ID"""

    delete_sample(Plasma, plasma_id)

    return redirect(request.referrer)
