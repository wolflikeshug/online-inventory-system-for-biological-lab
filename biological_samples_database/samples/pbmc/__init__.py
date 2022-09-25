"""

Pbmc.

All API information related to Pbmc samples

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
from ...model.sample import Pbmc


PBMC = Blueprint(
    'pbmc',
    __name__,
    template_folder='templates'
)
PBMC_CUSTOM_VARIABLES = [
    'visit_number',
    'cell_count',
    'patient_code'
]


class PbmcForm(SampleForm):
    '''Sample specific data'''

    visit_number = StringField('Visit Number')
    cell_count = IntegerField('Cell Count (millions)')
    patient_code = StringField('Patient ID')


@PBMC.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    return sample_create(request, Pbmc, PBMC_CUSTOM_VARIABLES)


@PBMC.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Pbmc data from the SQLite database"""

    return all_samples_page('pbmc', Pbmc, PbmcForm)


@PBMC.route('/create/', methods=['GET'])
def create_pbmc_form():
    """Provide the HTML form for serum creation"""

    sample_title = 'Add PBMC'
    return build_sample_form(sample_title, 'pbmc', PbmcForm)


@PBMC.route('/edit/<pbmc_id>', methods=['GET'])
def edit_pbmc_form(pbmc_id):
    """Provide the HTML form for PBMC creation"""

    sample_title = 'Edit PBMC'
    return build_sample_edit_form(
        sample_title,
        pbmc_id,
        'pbmc',
        PbmcForm,
        Pbmc,
        PBMC_CUSTOM_VARIABLES
    )


@PBMC.route('/delete/<pbmc_id>', methods=['GET'])
def delete_pbmc_form(pbmc_id):
    """Delete a PBMC item using ID"""

    delete_sample(Pbmc, pbmc_id)
