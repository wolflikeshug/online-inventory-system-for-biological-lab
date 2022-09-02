# Standard Imports
import datetime
import os
import random
import uuid

# Flask
from flask import Blueprint, jsonify, render_template, request

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import StringField

# Local Imports
from ..database import create_new_session, engine, SQLITE_PATH
from ..model.sample import Base, CellLine

# <--- Simon's code ---

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
    """Insert a single dummy dataset into the SQLite database"""

    cell_line = CellLine()
    cell_line.sample_id = f"TEST SAMPLE ID: {random.randint(0, 100)}"
    cell_line.sample_date = datetime.datetime.now()
    cell_line.cell_type = 'UNKNOWN TYPE'

    with create_new_session() as session:

        session.add(
            cell_line
        )

        session.commit()

        json_result = jsonify(cell_line.serialize())
        
        return json_result


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
            'room.html',
            cell_lines=cell_lines,
            form=form
    )
# --- Simon's code --->