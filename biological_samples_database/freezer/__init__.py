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
from ..authentication import guest_required, phd_required, staff_required


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
@guest_required
def create():
    """Insert a single dummy dataset into the SQLite database"""
    freezer_id = request.form.get('id')

    with create_new_session() as session:
        if not freezer_id:
            freezer = Freezer()
            freezer.name = request.form.get('name')
            freezer.freezer_type = request.form.get('freezer_type')
            freezer.room_id = request.form.get('room_id')

            session.add(
                freezer
            )

            session.commit()
        else:
            freezer = session.query(
                Freezer
            ).filter(
                Freezer.id == freezer_id
            ).first()
        
            if freezer:
                freezer.name = request.form.get('name')
                freezer.freezer_type = request.form.get('freezer_type')
                freezer.room_id = request.form.get('room_id')
            session.commit()

    return redirect(request.referrer)


@FREEZER.route('/', methods=['GET'])
@guest_required
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
@guest_required
def freezer_shelves(freezer_id):
    """Retrieve shelves in a specific freezer"""

    with create_new_session() as session:

        freezer = session.query(
            Freezer
        ).filter(
            Freezer.id == freezer_id
        ).first()

        shelves = freezer.shelves
        shelves.sort(key=lambda x: x.name)
        return render_template(
            'freezer_shelves.html',
            freezer=freezer,
            shelves = shelves,
            title="Freezer Shelves"
        )

@FREEZER.route('/a/<freezer_id>', methods=['GET'])
@guest_required
def freezer_boxes(freezer_id):
    """Retrieve boxes in a specific freezer"""

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).filter(
            Box.freezer_id == freezer_id
        ).all()
        
        if boxes:
            boxes.sort(key=lambda x: x.label)

            return render_template(
                'freezer_boxes.html',
                boxes=boxes,
                title="Freezer All Shelves"
            )
        
        flash(f'This freezer currently contains no boxes, Add Boxes via the shelf/tower page', 'danger')
        return redirect(request.referrer)

@FREEZER.route('/create/', methods=['GET'])
@phd_required
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
            title="Create Freezer")

@FREEZER.route('/create/<room_id>', methods=['GET'])
@phd_required
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
            title="Add Freezer")

@FREEZER.route('/edit/<freezer_id>', methods=['GET'])
@phd_required
def edit_box(freezer_id):
    """Edit Freezer"""
    form = FreezerForm()
    with create_new_session() as session:

        freezer = session.query(
            Freezer
        ).filter(
            Freezer.id == freezer_id
        ).first()

        rooms = session.query(
            Room
        ).all()

        freezer_types = session.query(
            FreezerType
        ).all()

        form['id'].data = getattr(freezer, 'id')
        standard_freezer_columns = [
        'name',
        'freezer_type',
        'room_id'
        ]

        for column_name in standard_freezer_columns:
            form[column_name].data = getattr(freezer, column_name)
        
        return render_template(
            'freezer_create.html',
            form=form,
            rooms=rooms,
            freezer_types=freezer_types,
            title="Edit Freezer")


@FREEZER.route('/delete/<freezer_id>', methods=['GET'])
@staff_required
def delete_box(freezer_id):
    """Delete Freezer"""

    with create_new_session() as session:

        session.query(
            Freezer
        ).filter(
            Freezer.id == freezer_id
        ).delete()
        
        session.commit()

    flash(f'Freezer Deleted', 'danger')
    return redirect(request.referrer)