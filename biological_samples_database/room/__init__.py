"""
Rooms.

Module for populating and altering room data.

"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
from ..model.storage import  Room


ROOM = Blueprint(
    'room',
    __name__,
    template_folder='templates'
)


class RoomForm(FlaskForm):
    '''Website link for page holding RSS data'''

    id = HiddenField('Id', [InputRequired()])
    name = StringField('Name', [InputRequired()])
    building_id = SelectField('Building')
    owner = StringField('Owner', [])


@ROOM.route('/', methods=['POST'])
def create():
    """Insert a single dummy dataset into the SQLite database"""

    room = Room()
    room.name = request.form.get('name')
    room.building_id = request.form.get('building_id')

    with create_new_session() as session:

        session.add(
            room
        )

        session.commit()

        json_result = jsonify(room.serialize())

        return json_result


@ROOM.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Room data from the SQLite database"""

    form = RoomForm()

    with create_new_session() as session:

        rooms = session.query(
            Room
        ).all()

        print(rooms)

        return render_template(
            'room.html',
            rooms=rooms,
            form=form,
            title="Rooms")
