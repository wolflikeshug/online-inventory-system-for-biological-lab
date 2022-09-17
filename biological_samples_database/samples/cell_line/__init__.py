"""

Cell Line

All API information related to Cell Line samples

"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from wtforms import IntegerField, StringField

# Local Imports
from .. import SampleForm, populate_default_values, populate_edit_values
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
    """Create/Update a single dataset into the SQLite database"""

    sample_id = request.form.get('db_id')

    with create_new_session() as session:

        # If ID exists update else create new
        cell_line = None
        if sample_id:
            cell_line = session.query(
                CellLine
            ).filter(
                CellLine.id == sample_id
            ).first()
        else:
            cell_line = CellLine()

        populate_default_values(request, cell_line)

        # Cell Line specific variables
        cell_line.cell_type = request.form.get('cell_type')
        cell_line.passage_number = request.form.get('passage_number')
        cell_line.cell_count = request.form.get('cell_count')
        cell_line.growth_media = request.form.get('growth_media')
        cell_line.vial_source = request.form.get('vial_source')
        cell_line.lot_number = request.form.get('lot_number')

        if not sample_id:
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

        return render_template(
            'cell_lines.html',
            cell_lines=cell_lines,
            form=form,
            title="Inventory"
        )


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
            sample_action=sample_action,
            title="Inventory")


@CELL_LINE.route('/edit/<cell_line_id>', methods=['GET'])
def edit_cell_line_form(cell_line_id):
    """Provide the HTML form for Cell Line creation"""

    sample_title = 'Edit Cell Line'
    sample_action = "/samples/cell_line/"

    with create_new_session() as session:
        cell_line = session.query(
            CellLine
        ).filter(
            CellLine.id == cell_line_id
        ).first()

        if not cell_line:
            return f"Cell Line with reference ID {cell_line_id} not found"

        with create_new_session() as session:

            boxes = session.query(
                Box
            ).all()

            form = CellLineForm()
            populate_edit_values(form, cell_line)

            form.passage_number.data = cell_line.passage_number
            form.cell_count.data = cell_line.cell_count
            form.growth_media.data = cell_line.growth_media
            form.vial_source.data = cell_line.vial_source
            form.lot_number.data = cell_line.lot_number

            return render_template(
                'cell_line_create.html',
                form=form,
                boxes=boxes,
                sample_title=sample_title,
                sample_action=sample_action,
                title="Inventory")
