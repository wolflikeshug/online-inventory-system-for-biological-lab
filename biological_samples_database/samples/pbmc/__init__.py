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


class PbmcForm(SampleForm):
    '''Sample specific data'''

    visit_number = StringField('Visit Number')
    cell_count = IntegerField('Cell Count (millions)')
    patient_code = StringField('Patient ID')


def pbmc_form_assignment(form, pbmc):
    """Assign Cell Line data to a form"""

    # PBMC specific variables
    form.patient_code.data = pbmc.patient_code
    form.visit_number.data = pbmc.visit_number
    form.cell_count.data = pbmc.cell_count


@PBMC.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    custom_variables = [
        'visit_number',
        'cell_count',
        'patient_code'
    ]

    return sample_create(request, Pbmc, custom_variables)


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
        pbmc_form_assignment
    )


@PBMC.route('/delete/<pbmc_id>', methods=['GET'])
def delete_pbmc_form(pbmc_id):
    """Delete a PBMC item using ID"""

    delete_sample(Pbmc, pbmc_id)
