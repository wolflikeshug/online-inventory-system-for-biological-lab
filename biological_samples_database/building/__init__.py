"""
Rooms.

Module for populating and altering room data.

"""

# Flask
from pickle import BUILD
from flask import Blueprint, redirect, render_template, request, flash

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
from ..model.storage import Building, Freezer, Room
from ..authentication import guest_required, phd_required, staff_required


BUILDING = Blueprint(
    'building',
    __name__,
    template_folder='templates'
)


class BuildingForm(FlaskForm):
    '''Sample specific data'''

    id = HiddenField('Id', [InputRequired()])
    name = StringField('Name', [InputRequired()])
    owner = StringField('Owner', [])


@BUILDING.route('/', methods=['POST'])
@staff_required
def create():
    """Insert a single dummy dataset into the SQLite database"""

    building_id = request.form.get('id')

    with create_new_session() as session:
        if not building_id:
            building = Building()
            building.name = request.form.get('name')
            """ This was originally in room's init.py, delete it?
            room.building_id = request.form.get('building_id')
            """
            session.add(
                building
            )
            session.commit()
        else:
            building = session.query(
                Building
            ).filter(
                Building.id == building_id
            ).first()
        
            if building:
                building.name = request.form.get('name')
                """ This was originally in room's init.py, delete it?
                room.building_id = request.form.get('building_id')
                """
            session.commit()

    return redirect(request.referrer)


@BUILDING.route('/', methods=['GET'])
@guest_required
def all_rooms():
    """Retrieve all buildings"""

    with create_new_session() as session:

        buildings = session.query(
            Building
        ).all()

        return render_template(
            'building.html',
            buildings=buildings,
            title="Buildings"
        )


@BUILDING.route('/<building_id>', methods=['GET'])
@guest_required
def building_rooms(building_id):
    """Retrieve freezers in a specific room"""

    with create_new_session() as session:

        rooms = session.query(
            Room
        ).filter(
            Room.building_id == building_id
        ).all()

        building = session.query(
            Building
        ).filter(
            Building.id == building_id
        ).first()

        return render_template(
            'room.html',
            building=building,
            rooms=rooms,
            title="Rooms"
        )


@BUILDING.route('/create', methods=['GET'])
@staff_required
def read_all():
    """Placeholder for retrieving Building data from the SQLite database"""

    """ Following code was copy paste from room, not sure how to translate to building 
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
    """

@BUILDING.route('/edit/<building_id>', methods=['GET'])
@phd_required
def edit_box(building_id):
    """Edit Building"""

    """ Following code was copy paste from room, not sure how to translate to building 
    form = RoomForm()
    with create_new_session() as session:

        room = session.query(
            Room
        ).filter(
            Room.id == room_id
        ).first()

        buildings = session.query(
            Building
        ).all()

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
            title="Room Edit")
    """


@BUILDING.route('/delete/<building_id>', methods=['GET'])
@staff_required
def delete_box(building_id):
    """Delete Building"""

    with create_new_session() as session:

        session.query(
            Building
        ).filter(
            Building.id == building_id
        ).delete()
        
        session.commit()

    flash(f'Buidling Deleted', 'danger')
    return redirect(request.referrer)
