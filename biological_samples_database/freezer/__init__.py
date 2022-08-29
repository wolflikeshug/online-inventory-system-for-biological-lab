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
from ..model.storage import Freezer


FREEZER = Blueprint(
    'freezer',
    __name__,
    template_folder='templates'
)


class CellLineForm(FlaskForm):
    '''Website link for page holding RSS data'''

    cell_line_name = StringField('Cell Line')


@FREEZER.route('/', methods=['POST'])
def create():
    """Insert a single dummy dataset into the SQLite database"""

    freezer = Freezer()
    freezer.name = request.form.get('name')
    freezer.building_id = request.form.get('building_id')

    session = create_new_session()
    session.add(
        freezer
    )

    session.commit()


@FREEZER.route('/', methods=['GET'])
def all_freezers():
    """Retrieve all freezers"""

    session = create_new_session()

    freezers = session.query(
        Freezer
    ).all()

    return render_template(
        'room.html',
        freezers=freezers
    )

@FREEZER.route('/<building_id>', methods=['GET'])
def building_freezers(building_id):
    """Retrieve freezers in a specific building"""

    session = create_new_session()

    freezers = session.query(
        Freezer
    ).filter(
        Freezer.building_id == building_id
    ).all()

    return render_template(
        'room.html',
        freezers=freezers
    )
