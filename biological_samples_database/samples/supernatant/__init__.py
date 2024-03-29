"""

Supernatant

All API information related to Supernatant samples

"""

# Flask
from flask import Blueprint, redirect, request

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
from ...model.sample import Supernatant


SUPERNATANT = Blueprint(
    'supernatant',
    __name__,
    template_folder='templates'
)
SUPERNATANT_CUSTOM_VARIABLES = []


class SupernatantForm(SampleForm):
    '''Form for handling Supernatant data'''


@SUPERNATANT.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    return sample_create(request, Supernatant, SUPERNATANT_CUSTOM_VARIABLES)


@SUPERNATANT.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Supernatant data from the SQLite database"""

    return all_samples_page('supernatant', Supernatant, SupernatantForm)


@SUPERNATANT.route('/create/', methods=['GET'])
def create_supernatant():
    """Provide the HTML form for supernatant creation"""

    sample_title = 'Add Supernatant'
    return build_sample_form(sample_title, 'supernatant', SupernatantForm)

@SUPERNATANT.route('/create/<box_id>/<pos>', methods=['GET'])
def create_supernatant_in_pos(box_id, pos):
    """Provide the HTML form for supernatant creation"""

    sample_title = 'Add Supernatant'
    return build_sample_form_in_pos(sample_title, 'supernatant', SupernatantForm, box_id, pos)


@SUPERNATANT.route('/edit/<supernatant_id>', methods=['GET'])
def edit_supernatant_form(supernatant_id):
    """Provide the HTML form for Supernatant creation"""

    sample_title = 'Edit Supernatant'
    return build_sample_edit_form(
        sample_title,
        supernatant_id,
        'supernatant',
        SupernatantForm,
        Supernatant,
        SUPERNATANT_CUSTOM_VARIABLES
    )

@SUPERNATANT.route('/copy/<supernatant_id>', methods=['GET'])
def copy_supernatant_form(supernatant_id):
    """Provide the HTML form for Supernatant copy"""

    sample_title = 'Copy Sample: Supernatant'
    return build_sample_copy_form(
        sample_title,
        supernatant_id,
        'supernatant',
        SupernatantForm,
        Supernatant,
        SUPERNATANT_CUSTOM_VARIABLES
    )

@SUPERNATANT.route('/delete/<supernatant_id>', methods=['GET'])
def delete_supernatant_form(supernatant_id):
    """Delete a Supernatant item using ID"""

    delete_sample(Supernatant, supernatant_id)

    return redirect(request.referrer)
