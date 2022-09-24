"""

Cell Line

All API information related to Cell Line samples

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
from ...model.sample import CellLine


CELL_LINE = Blueprint(
    'cell_line',
    __name__,
    template_folder='templates'
)


class CellLineForm(SampleForm):
    '''Sample specific data'''

    cell_type = StringField('Cell Type')
    passage_number = StringField('Passage Number')
    cell_count = IntegerField('Cell Count (millions)')
    growth_media = StringField('Growth Media')
    vial_source = StringField('Vial Source')
    lot_number = StringField('Lot Number')




def cell_line_form_assignment(form, cell_line):
    """Assign Cell Line data to a form"""

    form.passage_number.data = cell_line.passage_number
    form.cell_count.data = cell_line.cell_count
    form.growth_media.data = cell_line.growth_media
    form.vial_source.data = cell_line.vial_source
    form.lot_number.data = cell_line.lot_number


@CELL_LINE.route('/', methods=['POST'])
def create():
    """Create/Update a single dataset into the SQLite database"""

    custom_variables = [
        'cell_type',
        'passage_number',
        'cell_count',
        'growth_media',
        'vial_source',
        'lot_number'
    ]

    return sample_create(request, CellLine, custom_variables)


@CELL_LINE.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Cell Line data from the SQLite database"""

    return all_samples_page('cell_line', CellLine, CellLineForm)


@CELL_LINE.route('/create/', methods=['GET'])
def create_cell_line_form():
    """Provide the HTML form for serum creation"""

    sample_title = 'Add Cell Line'
    return build_sample_form(sample_title, 'cell_line', CellLineForm)


@CELL_LINE.route('/edit/<cell_line_id>', methods=['GET'])
def edit_cell_line_form(cell_line_id):
    """Provide the HTML form for Cell Line creation"""

    sample_title = 'Edit Cell Line'
    return build_sample_edit_form(
        sample_title,
        cell_line_id,
        'cell_line',
        CellLineForm,
        CellLine,
        cell_line_form_assignment
    )


@CELL_LINE.route('/delete/<cell_line_id>', methods=['GET'])
def delete_cell_line_id_form(cell_line_id):
    """Delete a Cell Line item using ID"""

    delete_sample(CellLine, cell_line_id)
