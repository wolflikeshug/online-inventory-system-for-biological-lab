"""

Cell Line

All API information related to Cell Line samples

"""

# Standard Imports
import uuid

# Flask
from flask import Blueprint, render_template, request

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import StringField

# Local Imports
from ..database import create_new_session
from ..model.sample import CellLine


CELL_LINE = Blueprint(
    'cell_line',
    __name__,
    template_folder='templates'
)


class CellLineForm(FlaskForm):
    '''Website link for page holding RSS data'''

    cell_line_name = StringField('Cell Line')


@CELL_LINE.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    cell_line = CellLine()
    cell_line.id = str(uuid.uuid4())

    with create_new_session() as session:

        session.add(
            cell_line
        )

        session.commit()

    return '<div>SUCCESS<div>'


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


