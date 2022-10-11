"""
Rooms.

Module for populating and altering room data.

"""

# Flask
from flask import Blueprint, redirect, render_template, request, flash

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
from ..model.storage import Building, Freezer, Room
from ..authentication import guest_required, phd_required, staff_required


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
@staff_required
def create():
    """Insert a single dummy dataset into the SQLite database"""

    room_id = request.form.get('id')

    with create_new_session() as session:
        if not room_id:
            room = Room()
            room.name = request.form.get('name')
            room.building_id = request.form.get('building_id')
            session.add(
                room
            )
            session.commit()
        else:
            room = session.query(
                Room
            ).filter(
                Room.id == room_id
            ).first()
        
            if room:
                room.name = request.form.get('name')
                room.building_id = request.form.get('building_id')
            session.commit()

    return redirect(request.referrer)


@ROOM.route('/', methods=['GET'])
@guest_required
def all_rooms():
    """Retrieve all rooms"""

    with create_new_session() as session:

        rooms = session.query(
            Room
        ).all()
        if rooms:
            rooms.sort(key=lambda x: x.name)
        return render_template(
            'room.html',
            rooms=rooms,
            title="Rooms"
        )


@ROOM.route('/<room_id>', methods=['GET'])
@guest_required
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

        if freezers:
            freezers.sort(key=lambda x: x.name)
        return render_template(
            'freezer.html',
            room=room,
            freezers=freezers,
            title="Freezers"
        )


@ROOM.route('/create/', methods=['GET'])
@staff_required
def create_room():
    """Placeholder for retrieving Room data from the SQLite database"""

    form = RoomForm()

    with create_new_session() as session:

        buildings = session.query(
            Building
        ).all()

        if buildings:
            buildings.sort(key=lambda x: x.name)
        return render_template(
            'room_create.html',
            buildings=buildings,
            form=form,
            title="Create Room")

@ROOM.route('/create/<building_id>', methods=['GET'])
@staff_required
def create_room_in_building(building_id):
    """Placeholder for retrieving Room data from the SQLite database"""

    form = RoomForm()

    with create_new_session() as session:

        buildings = session.query(
            Building
        ).filter(
            Building.id == building_id
        ).all()

        return render_template(
            'room_create.html',
            buildings=buildings,
            form=form,
            title="Add Room")

@ROOM.route('/edit/<room_id>', methods=['GET'])
@staff_required
def edit_box(room_id):
    """Edit Room"""
    form = RoomForm()
    with create_new_session() as session:

        room = session.query(
            Room
        ).filter(
            Room.id == room_id
        ).first()

        buildings = [room.building]
        other_buildings = session.query(
            Building
        ).filter(
            Building.id != room.building_id
        ).all()

        if other_buildings:
            other_buildings.sort(key=lambda x: x.name)
            buildings += other_buildings

        form['id'].data = getattr(room, 'id')
        standard_room_columns = [
        'name',
        'building_id'
        ]

        for column_name in standard_room_columns:
            form[column_name].data = getattr(room, column_name)
        
        return render_template(
            'room_create.html',
            form=form,
            buildings=buildings,
            title="Edit Room")


@ROOM.route('/delete/<room_id>', methods=['GET'])
@staff_required
def delete_box(room_id):
    """Delete Room"""

    with create_new_session() as session:

        session.query(
            Room
        ).filter(
            Room.id == room_id
        ).delete()
        
        session.commit()

    flash(f'Room Deleted', 'danger')
    return redirect(request.referrer)
