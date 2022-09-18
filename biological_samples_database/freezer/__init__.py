"""
Freezer.

API for handling Freezer data.
"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
from ..model.storage import Box, Freezer, FreezerType, Room


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


@FREEZER.route('/<freezer_id>', methods=['GET'])
def freezer_boxes(freezer_id):
    """Retrieve boxes in a specific freezer"""

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).filter(
            Box.freezer_id == freezer_id
        ).all()

        freezer = session.query(
            Freezer
        ).filter(
            Freezer.id == freezer_id
        ).first()

        return render_template(
            'freezer_boxes.html',
            freezer=freezer,
            boxes=boxes,
            title="Freezers"
        )


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
