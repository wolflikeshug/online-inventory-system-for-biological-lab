"""

Other

All API information related to Other samples

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
from ...model.sample import Other


OTHER = Blueprint(
    'other',
    __name__,
    template_folder='templates'
)


class OtherForm(SampleForm):
    '''Form for handling Other data'''


@OTHER.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    custom_variables = []

    return sample_create(request, Other, custom_variables)


@OTHER.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Other data from the SQLite database"""

    return all_samples_page('other', Other, OtherForm)


@OTHER.route('/create/', methods=['GET'])
def create_other():
    """Provide the HTML form for other creation"""

    sample_title = 'Add Other'
    return build_sample_form(sample_title, 'other', OtherForm)


@OTHER.route('/edit/<other_id>', methods=['GET'])
def edit_other_form(other_id):
    """Provide the HTML form for Other creation"""

    sample_title = 'Edit Other'
    return build_sample_edit_form(
        sample_title,
        other_id,
        'other',
        OtherForm,
        Other,
        None
    )


@OTHER.route('/delete/<other_id>', methods=['GET'])
def delete_other_form(other_id):
    """Delete a Other item using ID"""

    delete_sample(Other, other_id)
