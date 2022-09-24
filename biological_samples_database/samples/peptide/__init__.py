"""

Peptide

All API information related to Peptide samples

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
from ...model.sample import Peptide


PEPTIDE = Blueprint(
    'peptide',
    __name__,
    template_folder='templates'
)


class PeptideForm(SampleForm):
    '''Form for handling Peptide data'''

    cell_type = StringField('Cell Type')
    vial_source = StringField('Vial Source')
    batch_number = IntegerField('Batch Number')
    lot_number = IntegerField('Lot Number')


def peptide_form_assignment(form, peptide):
    """Assign Virus Isolation data to a form"""

    # Virus Culture specific variables
    form.cell_type.data = peptide.cell_type
    form.vial_source.data = peptide.vial_source
    form.batch_number.data = peptide.batch_number
    form.lot_number.data = peptide.lot_number


@PEPTIDE.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    custom_variables = [
        'cell_type',
        'vial_source',
        'batch_number',
        'lot_number'
    ]

    return sample_create(request, Peptide, custom_variables)


@PEPTIDE.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Peptide data from the SQLite database"""

    return all_samples_page('peptide', Peptide, PeptideForm)


@PEPTIDE.route('/create/', methods=['GET'])
def create_peptide():
    """Provide the HTML form for peptide creation"""

    sample_title = 'Add Peptide'
    return build_sample_form(sample_title, 'peptide', PeptideForm)


@PEPTIDE.route('/edit/<peptide_id>', methods=['GET'])
def edit_peptide_form(peptide_id):
    """Provide the HTML form for Peptide creation"""

    sample_title = 'Edit Peptide'
    return build_sample_edit_form(
        sample_title,
        peptide_id,
        'peptide',
        PeptideForm,
        Peptide,
        peptide_form_assignment
    )


@PEPTIDE.route('/delete/<peptide_id>', methods=['GET'])
def delete_peptide_form(peptide_id):
    """Delete a Peptide item using ID"""

    delete_sample(Peptide, peptide_id)
