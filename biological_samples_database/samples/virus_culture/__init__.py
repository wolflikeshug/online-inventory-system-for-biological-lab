"""

Virus Culture

All API information related to Virus Culture samples

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
from ...model.sample import VirusCulture


VIRUS_CULTURE = Blueprint(
    'virus_culture',
    __name__,
    template_folder='templates'
)


class VirusCultureForm(SampleForm):
    '''Form for handling Virus Culture data'''

    pathwest_id = StringField('PathWest ID')
    batch_number = StringField('Batch Number')
    passage_number = StringField('Passage Number')
    growth_media = StringField('Growth Media')



def virus_culture_form_assignment(form, virus_culture):
    """Assign Cell Line data to a form"""

    # Virus Culture specific variables
    form.pathwest_id.data = virus_culture.pathwest_id
    form.batch_number.data = virus_culture.batch_number
    form.passage_number.data = virus_culture.passage_number
    form.growth_media.data = virus_culture.growth_media


@VIRUS_CULTURE.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    custom_variables = [
        'pathwest_id',
        'batch_number',
        'passage_number',
        'growth_media'
    ]

    return sample_create(request, VirusCulture, custom_variables)


@VIRUS_CULTURE.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Virus Culture data from the database"""

    return all_samples_page('virus_culture', VirusCulture, VirusCultureForm)


@VIRUS_CULTURE.route('/create/', methods=['GET'])
def create_virus_culture():
    """Provide the HTML form for virus_culture creation"""

    sample_title = 'Add Virus Culture'
    return build_sample_form(sample_title, 'virus_culture', VirusCultureForm)


@VIRUS_CULTURE.route('/edit/<virus_culture_id>', methods=['GET'])
def edit_virus_culture_form(virus_culture_id):
    """Provide the HTML form for Virus Culture creation"""

    sample_title = 'Edit Virus Culture'
    return build_sample_edit_form(
        sample_title,
        virus_culture_id,
        'virus_culture',
        VirusCultureForm,
        VirusCulture,
        virus_culture_form_assignment
    )


@VIRUS_CULTURE.route('/delete/<virus_culture_id>', methods=['GET'])
def delete_virus_culture_form(virus_culture_id):
    """Delete a Virus Culture item using ID"""

    delete_sample(VirusCulture, virus_culture_id)
