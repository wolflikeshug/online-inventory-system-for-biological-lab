"""

Rna

All API information related to Rna samples

"""

# Flask
from flask import Blueprint, request

# Flask WTF
from wtforms import StringField

# Local Imports
from .. import (
    SampleForm,
    all_samples_page,
    build_sample_edit_form,
    build_sample_form,
    delete_sample,
    sample_create
)
from ...model.sample import Rna


RNA = Blueprint(
    'rna',
    __name__,
    template_folder='templates'
)
RNA_CUSTOM_VARIABLES = []


class RnaForm(SampleForm):
    '''Form for handling Rna data'''

    pathwest_id = StringField('PathWest ID')


@RNA.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    return sample_create(request, Rna, RNA_CUSTOM_VARIABLES)


@RNA.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Rna data from the SQLite database"""

    return all_samples_page('rna', Rna, RnaForm)


@RNA.route('/create/', methods=['GET'])
def create_rna():
    """Provide the HTML form for rna creation"""

    sample_title = 'Add Rna'
    return build_sample_form(sample_title, 'rna', RnaForm)


@RNA.route('/edit/<rna_id>', methods=['GET'])
def edit_rna_form(rna_id):
    """Provide the HTML form for Rna creation"""

    sample_title = 'Edit Rna'
    return build_sample_edit_form(
        sample_title,
        rna_id,
        'rna',
        RnaForm,
        Rna,
        RNA_CUSTOM_VARIABLES
    )


@RNA.route('/delete/<rna_id>', methods=['GET'])
def delete_rna_form(rna_id):
    """Delete a Rna item using ID"""

    delete_sample(Rna, rna_id)
