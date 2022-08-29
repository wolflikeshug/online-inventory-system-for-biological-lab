# Standard Imports
import datetime
import os
import random
import uuid

# Flask
from flask import Blueprint, jsonify, render_template, request

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import BooleanField, HiddenField
from wtforms import SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session, engine, SQLITE_PATH
from ..model.storage import Freezer, Room


FREEZER = Blueprint(
    'freezer',
    __name__,
    template_folder='templates'
)


# Forms
class FreezerForm(FlaskForm):
    """WTF for creating a new box"""

    id = HiddenField('Id', [InputRequired()])
    name = StringField('Name', [InputRequired()])
    room_id = SelectField('Room')
    owner = StringField('Owner', [])


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
        'freezer.html',
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
        'freezer.html',
        freezers=freezers
    )

@FREEZER.route('/create/', methods=['GET'])
def create_box():
    """Provide the HTML form for freezer creation"""

    form = FreezerForm()
    with create_new_session() as session:

        rooms = session.query(
            Room
        ).all()
        
        return render_template(
            'freezer_create.html',
            form=form,
            rooms=rooms)
