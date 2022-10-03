"""

Cell Line

All API information related to Cell Line samples

"""

# Flask
from flask import Blueprint, redirect, request

# Flask WTF
from wtforms import IntegerField, StringField

# Local Imports
from .. import (
    SampleForm,
    all_samples_page,
    build_sample_edit_form,
    build_sample_form,
    build_sample_form_in_pos,
    delete_sample,
    sample_create
)
from ...model.sample import CellLine


CELL_LINE = Blueprint(
    'cell_line',
    __name__,
    template_folder='templates'
)

CELL_LINE_CUSTOM_VARIABLES = [
    'cell_type',
    'passage_number',
    'cell_count',
    'growth_media',
    'vial_source',
    'lot_number'
]


class CellLineForm(SampleForm):
    '''Sample specific data'''

    cell_type = StringField('Cell Type')
    passage_number = StringField('Passage Number')
    # POSSIBLE FUCKUP cell_count = IntegerField('Cell Count (millions)')
    cell_count = IntegerField('Cell Count')
    growth_media = StringField('Growth Media')
    vial_source = StringField('Vial Source')
    lot_number = StringField('Lot Number')


@CELL_LINE.route('/', methods=['POST'])
def create():
    """Create/Update a single dataset into the SQLite database"""

    return sample_create(request, CellLine, CELL_LINE_CUSTOM_VARIABLES)


@CELL_LINE.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Cell Line data from the SQLite database"""

    return all_samples_page('cell_line', CellLine, CellLineForm)


@CELL_LINE.route('/create/', methods=['GET'])
def create_cell_line_form():
    """Provide the HTML form for serum creation"""

    sample_title = 'Add Cell Line'
    return build_sample_form(sample_title, 'cell_line', CellLineForm)

@CELL_LINE.route('/create/<box_id>/<pos>', methods=['GET'])
def create_cell_line_form_in_pos(box_id, pos):
    """Provide the HTML form for serum creation"""
    sample_title = 'Add Cell Line'
    if box_id == "" or pos == "":
        return build_sample_form(sample_title, 'cell_line', CellLineForm)
    return build_sample_form_in_pos(sample_title, 'cell_line', CellLineForm, box_id, pos)

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
        CELL_LINE_CUSTOM_VARIABLES
    )


@CELL_LINE.route('/delete/<cell_line_id>', methods=['GET'])
def delete_cell_line_id_form(cell_line_id):
    """Delete a Cell Line item using ID"""

    delete_sample(CellLine, cell_line_id)

    return redirect(request.referrer)
