"""

Cell Line

All API information related to Cell Line samples

"""

# Standard Imports
import datetime
import os
import random
import uuid

# Flask
from flask import Blueprint, request

# Local Imports
from ..database import create_new_session, engine, SQLITE_PATH
from ..model import Base, CellLine


CELL_LINE = Blueprint(
    'cell_line',
    __name__,
    template_folder='templates'
)


@CELL_LINE.route('/', methods=['POST'])
def create():
    """Insert a single dummy dataset into the SQLite database"""

    cell_line = CellLine()

    cell_line.id = str(uuid.uuid4())
    cell_line.sample_id = f"TEST SAMPLE ID: {random.randint(0, 100)}"
    cell_line.sample_date = datetime.datetime.now()
    cell_line.cell_type = 'UNKNOWN TYPE'

    session = create_new_session()

    session.add(
        cell_line
    )

    session.commit()


@CELL_LINE.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Cell Line data from the SQLite database"""

    return "TEST CELL LINE RETRIEVAL"


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
