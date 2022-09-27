"""
Freezer.

API for handling Freezer data.
"""

# Flask
from flask import Blueprint, redirect, render_template, request, flash

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
from ..model.storage import Box, Freezer, FreezerType, Room, Shelf


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
    freezer_type = SelectField('Freezer Type', [InputRequired()])
    room_id = SelectField('Room')
    owner = StringField('Owner', [])


@FREEZER.route('/', methods=['POST'])
def create():
    """Insert a single dummy dataset into the SQLite database"""

    freezer = Freezer()
    freezer.name = request.form.get('name')
    freezer.freezer_type = request.form.get('freezer_type')
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
            freezers=freezers,
            title="Freezers"
        )

@FREEZER.route('/s/<freezer_id>', methods=['GET'])
def freezer_shelves(freezer_id):
    """Retrieve shelves in a specific freezer"""

    with create_new_session() as session:

        freezer = session.query(
            Freezer
        ).filter(
            Freezer.id == freezer_id
        ).first()

        shelves = freezer.shelves
        
        return render_template(
            'freezer_shelves.html',
            freezer=freezer,
            shelves = shelves,
            title="Freezers"
        )

@FREEZER.route('/a/<freezer_id>', methods=['GET'])
def freezer_boxes(freezer_id):
    """Retrieve boxes in a specific freezer"""

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).filter(
            Box.freezer_id == freezer_id
        ).all()
        
        if boxes:
            return render_template(
                'freezer_boxes.html',
                boxes=boxes,
                title="Freezers"
            )
        
        flash(f'This freezer currently contains no boxes, Add Boxes via the shelf/tower page', 'danger')
        return redirect(request.referrer)

        


@FREEZER.route('/create/', methods=['GET'])
def create_box():
    """Provide the HTML form for freezer creation"""

    form = FreezerForm()
    with create_new_session() as session:

        rooms = session.query(
            Room
        ).all()

        freezer_types = session.query(
            FreezerType
        ).all()

        return render_template(
            'freezer_create.html',
            form=form,
            rooms=rooms,
            freezer_types=freezer_types,
            title="Freezers")

@FREEZER.route('/create/<room_id>', methods=['GET'])
def create_box_in_room(room_id):
    """Provide the HTML form for freezer creation"""

    form = FreezerForm()
    with create_new_session() as session:

        room = session.query(
            Room
        ).filter(
            Room.id == room_id
        ).first()

        freezer_types = session.query(
            FreezerType
        ).all()

        return render_template(
            'freezer_create.html',
            form=form,
            room=room,
            freezer_types=freezer_types,
            title="Freezers")