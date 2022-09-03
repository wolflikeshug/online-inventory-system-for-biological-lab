"""

Cell Line

All API information related to Cell Line samples

"""

# Standard Imports
import uuid

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from wtforms import IntegerField, StringField

# Local Imports
from .. import SampleForm, populate_default_values
from ...database import create_new_session
from ...model.sample import CellLine
from ...model.storage import Box


CELL_LINE = Blueprint(
    'cell_line',
    __name__,
    template_folder='templates'
)


class CellLineForm(SampleForm):
    '''Website link for page holding RSS data'''

    cell_type = StringField('Cell Type')
    passage_number = StringField('Passage Number')
    cell_count = IntegerField('Cell Count')
    growth_media = StringField('Growth Media')
    vial_source = StringField('Vial Source')
    lot_number = StringField('Lot Number')


@CELL_LINE.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    cell_line = CellLine()
    populate_default_values(request, cell_line)

    # Cell Line specific variables
    cell_line.cell_type = request.form.get('cell_type')
    cell_line.passage_number = request.form.get('passage_number')
    cell_line.cell_count = request.form.get('cell_count')
    cell_line.growth_media = request.form.get('growth_media')
    cell_line.vial_source = request.form.get('vial_source')
    cell_line.lot_number = request.form.get('lot_number')

    with create_new_session() as session:

        session.add(
            cell_line
        )

        session.commit()
        return redirect(request.referrer)


@CELL_LINE.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Cell Line data from the SQLite database"""

    form = CellLineForm()

    with create_new_session() as session:

        cell_lines = session.query(
            CellLine
        ).all()

        print(cell_lines)

        return render_template(
            'cell_lines.html',
            cell_lines=cell_lines,
            form=form
        )


@CELL_LINE.route('/sample_id', methods=['GET'])
def read():
    """Placeholder for retrieving Cell Line data from the SQLite database"""

    args = request.args
    sample_id = args.get('sample_id')

    return f"CELL LINE RETRIEVAL INDIVIDUAL: {sample_id}"


@CELL_LINE.route('/', methods=['PATCH'])
def update():
    """Placeholder for updating Cell Line data in the SQLite database"""

#  May need HTTP POST request and set the X-HTTP-Method-Override


@CELL_LINE.route('/', methods=['DELETE'])
def delete():
    """Placeholder for deleting Cell Line data in the SQLite database"""

#  May need HTTP POST request and set the X-HTTP-Method-Override

@CELL_LINE.route('/create/', methods=['GET'])
def create_cell_line_form():
    """Provide the HTML form for serum creation"""

    sample_title = 'Add Cell Line'
    sample_action = "/samples/cell_line/"

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).all()

        form = CellLineForm()
        return render_template(
            'cell_line_create.html',
            form=form,
            boxes=boxes,
            sample_title=sample_title,
            sample_action=sample_action)