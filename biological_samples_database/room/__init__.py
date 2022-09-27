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
from ..model.storage import Building, Freezer, Room


ROOM = Blueprint(
    'room',
    __name__,
    template_folder='templates'
)


class RoomForm(FlaskForm):
    '''Sample specific data'''

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

    return redirect(request.referrer)


@ROOM.route('/', methods=['GET'])
def all_rooms():
    """Retrieve all rooms"""

    with create_new_session() as session:

        rooms = session.query(
            Room
        ).all()

        return render_template(
            'room.html',
            rooms=rooms,
            title="Rooms"
        )


@ROOM.route('/<room_id>', methods=['GET'])
def room_freezers(room_id):
    """Retrieve freezers in a specific room"""

    with create_new_session() as session:

        freezers = session.query(
            Freezer
        ).filter(
            Freezer.room_id == room_id
        ).all()

        room = session.query(
            Room
        ).filter(
            Room.id == room_id
        ).first()

        return render_template(
            'freezer.html',
            room=room,
            freezers=freezers,
            title="Freezers"
        )


@ROOM.route('/create', methods=['GET'])
def read_all():
    """Placeholder for retrieving Room data from the SQLite database"""

    form = RoomForm()

    with create_new_session() as session:

        buildings = session.query(
            Building
        ).all()

        return render_template(
            'room_create.html',
            buildings=buildings,
            form=form,
            title="Rooms")
