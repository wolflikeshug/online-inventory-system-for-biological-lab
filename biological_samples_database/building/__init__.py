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
from ..authentication import admin_required, guest_required, phd_required, staff_required


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
            session.add(
                building
            )        
        else:
            building = session.query(
                Building
            ).filter(
                Building.id == building_id
            ).first()
        
            if building:
                building.name = request.form.get('name')
        
        session.commit()

    return redirect(request.referrer)


@BUILDING.route('/', methods=['GET'])
@guest_required
def all_buildings():
    """Retrieve all buildings"""

    with create_new_session() as session:

        buildings = session.query(
            Building
        ).all()
        if buildings:
            buildings.sort(key=lambda x: x.name)
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

        if rooms:
            rooms.sort(key=lambda x: x.name)
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

    form = BuildingForm()

    with create_new_session() as session:

        buildings = session.query(
            Building
        ).all()
        if buildings:
            buildings.sort(key=lambda x: x.name)
        return render_template(
            'building_create.html',
            buildings=buildings,
            form=form,
            title="Create Building")
    

@BUILDING.route('/edit/<building_id>', methods=['GET'])
@staff_required
def edit_box(building_id):
    """Edit Building"""

    form = BuildingForm()
    with create_new_session() as session:

        building = session.query(
            Building
        ).filter(
            Building.id == building_id
        ).first()

        form.id.data = building.id
        form.name.data = building.name
        
        return render_template(
            'building_create.html',
            form=form,
            title="Edit Building")


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
