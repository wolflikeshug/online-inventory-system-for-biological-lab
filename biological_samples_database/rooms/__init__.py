"""
Rooms.

Module for populating and altering room data.

"""

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
from ..model.storage import Room

# <--- Simon's code ---

ROOM = Blueprint(
    'room',
    __name__,
    template_folder='templates'
)


class RoomForm(FlaskForm):
    '''Website link for page holding RSS data'''

    room_name = StringField('Room')

@ROOM.route('/', methods=['POST'])
def create():
    """Insert a single dummy dataset into the SQLite database"""

    room = Room()

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
            form=form
    )
# --- Simon's code --->