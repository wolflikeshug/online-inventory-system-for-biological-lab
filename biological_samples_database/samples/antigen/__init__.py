"""

Antigen

All API information related to Antigen samples

"""

# Flask
from flask import Blueprint, request

# Flask WTF
from wtforms import IntegerField, StringField

# Local Imports
from .. import (
    SampleForm,
    all_samples_page,
    build_sample_edit_form,
    build_sample_form,
    delete_sample,
    sample_create
)
from ...model.sample import Antigen


ANTIGEN = Blueprint(
    'antigen',
    __name__,
    template_folder='templates'
)


class AntigenForm(SampleForm):
    '''Form for handling Antigen data'''

    pathwest_id = StringField('PathWest ID')
    batch_number = IntegerField('Batch Number')
    lot_number = IntegerField('Lot Number')


def antigen_data_assignment(sent_request, antigen):
    """Assign Virus Culture specific form data to VirusCulture class"""

    # Virus Culture specific variables
    antigen.pathwest_id = sent_request.form.get('pathwest_id')
    antigen.batch_number = sent_request.form.get('batch_number')
    antigen.lot_number = sent_request.form.get('lot_number')


def antigen_form_assignment(form, antigen):
    """Assign Virus Isolation data to a form"""

    # Virus Culture specific variables
    form.pathwest_id.data = antigen.pathwest_id
    form.batch_number.data = antigen.batch_number
    form.lot_number.data = antigen.lot_number


@ANTIGEN.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    return sample_create(request, Antigen, antigen_data_assignment)


@ANTIGEN.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Antigen data from the SQLite database"""

    return all_samples_page('antigen', Antigen, AntigenForm)


@ANTIGEN.route('/create/', methods=['GET'])
def create_antigen():
    """Provide the HTML form for antigen creation"""

    sample_title = 'Add Antigen'
    return build_sample_form(sample_title, 'antigen', AntigenForm)


@ANTIGEN.route('/edit/<antigen_id>', methods=['GET'])
def edit_antigen_form(antigen_id):
    """Provide the HTML form for Antigen creation"""

    sample_title = 'Edit Antigen'
    return build_sample_edit_form(
        sample_title,
        antigen_id,
        'antigen',
        AntigenForm,
        Antigen,
        antigen_form_assignment
    )


@ANTIGEN.route('/delete/<antigen_id>', methods=['GET'])
def delete_antigen_form(antigen_id):
    """Delete a Antigen item using ID"""

    delete_sample(Antigen, antigen_id)
