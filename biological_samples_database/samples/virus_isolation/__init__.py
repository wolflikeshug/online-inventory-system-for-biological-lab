"""

Virus Isolation

All API information related to Virus Isolation samples

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
from ...model.sample import VirusIsolation


VIRUS_ISOLATION = Blueprint(
    'virus_isolation',
    __name__,
    template_folder='templates'
)
VIRUS_ISOLATION_CUSTOM_VARIABLES = [
        'pathwest_id',
        'batch_number',
        'passage_number',
        'growth_media'
    ]


class VirusIsolationForm(SampleForm):
    '''Form for handling Virus Isolation data'''

    pathwest_id = StringField('PathWest ID')
    batch_number = StringField('Batch Number')
    passage_number = StringField('Passage Number')
    growth_media = StringField('Growth Media')


@VIRUS_ISOLATION.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    return sample_create(
        request,
        VirusIsolation,
        VIRUS_ISOLATION_CUSTOM_VARIABLES
    )


@VIRUS_ISOLATION.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Virus Isolation data from the database"""

    return all_samples_page('virus_isolation', VirusIsolation, VirusIsolationForm)


@VIRUS_ISOLATION.route('/create/', methods=['GET'])
def create_virus_isolation():
    """Provide the HTML form for virus_isolation creation"""

    sample_title = 'Add Virus Isolation'
    return build_sample_form(sample_title, 'virus_isolation', VirusIsolationForm)

@VIRUS_ISOLATION.route('/create/<box_id>/<pos>', methods=['GET'])
def create_virus_culture_in_pos(box_id, pos):
    """Provide the HTML form for virus_culture creation"""

    sample_title = 'Add Virus Isolation'
    return build_sample_form_in_pos(sample_title, 'virus_culture', VirusIsolationForm, box_id,pos)


@VIRUS_ISOLATION.route('/edit/<virus_isolation_id>', methods=['GET'])
def edit_virus_isolation_form(virus_isolation_id):
    """Provide the HTML form for Virus Isolation creation"""

    sample_title = 'Edit Virus Isolation'
    return build_sample_edit_form(
        sample_title,
        virus_isolation_id,
        'virus_isolation',
        VirusIsolationForm,
        VirusIsolation,
        VIRUS_ISOLATION_CUSTOM_VARIABLES
    )

@VIRUS_ISOLATION.route('/copy/<virus_isolation_id>', methods=['GET'])
def copy_virus_isolation_form(virus_isolation_id):
    """Provide the HTML form for Virus Isolation copy"""

    sample_title = 'Sample Copy: Virus Isolation'
    return build_sample_copy_form(
        sample_title,
        virus_isolation_id,
        'virus_isolation',
        VirusIsolationForm,
        VirusIsolation,
        VIRUS_ISOLATION_CUSTOM_VARIABLES
    )

@VIRUS_ISOLATION.route('/delete/<virus_isolation_id>', methods=['GET'])
def delete_virus_isolation_form(virus_isolation_id):
    """Delete a Virus Isolation item using ID"""

    delete_sample(VirusIsolation, virus_isolation_id)

    return redirect(request.referrer)
