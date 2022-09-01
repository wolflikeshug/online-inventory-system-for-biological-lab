"""
Freezer.

API for handling Freezer data.
"""

import uuid

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
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
    freezer.id = str(uuid.uuid4())
    freezer.name = request.form.get('name')
    freezer.room_id = request.form.get('room_id')

    with create_new_session() as session:
        session.add(
            freezer
        )

        session.commit()

        return redirect(request.referrer)


@FREEZER.route('/', methods=['GET'])
def all_freezers():
    """Retrieve all freezers"""

    with create_new_session() as session:

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

    with create_new_session() as session:

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
