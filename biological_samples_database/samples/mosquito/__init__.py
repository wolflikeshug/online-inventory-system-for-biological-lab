"""

Mosquito

All API information related to Mosquito samples

"""

# Flask
from flask import Blueprint, request

# Local Imports
from .. import (
    SampleForm,
    all_samples_page,
    build_sample_edit_form,
    build_sample_form,
    delete_sample,
    sample_create
)
from ...model.sample import Mosquito


MOSQUITO = Blueprint(
    'mosquito',
    __name__,
    template_folder='templates'
)

MOSQUITO_CUSTOM_VARIABLES = []


class MosquitoForm(SampleForm):
    '''Form for handling Mosquito data'''


@MOSQUITO.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    return sample_create(request, Mosquito, MOSQUITO_CUSTOM_VARIABLES)


@MOSQUITO.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Mosquito data from the SQLite database"""

    return all_samples_page('mosquito', Mosquito, MosquitoForm)


@MOSQUITO.route('/create/', methods=['GET'])
def create_mosquito():
    """Provide the HTML form for mosquito creation"""

    sample_title = 'Add Mosquito'
    return build_sample_form(sample_title, 'mosquito', MosquitoForm)


@MOSQUITO.route('/edit/<mosquito_id>', methods=['GET'])
def edit_mosquito_form(mosquito_id):
    """Provide the HTML form for Mosquito creation"""

    sample_title = 'Edit Mosquito'
    return build_sample_edit_form(
        sample_title,
        mosquito_id,
        'mosquito',
        MosquitoForm,
        Mosquito,
        MOSQUITO_CUSTOM_VARIABLES
    )


@MOSQUITO.route('/delete/<mosquito_id>', methods=['GET'])
def delete_mosquito_id(mosquito_id):
    """Delete a Mosquito item using ID"""

    delete_sample(Mosquito, mosquito_id)
