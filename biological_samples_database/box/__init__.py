"""
Box

API for handling box data.
"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
from ..model.storage import Box, BoxType, Freezer
from ..model.sample import Vial


BOX = Blueprint(
    'box',
    __name__,
    template_folder='templates'
)


# Forms
class BoxForm(FlaskForm):
    """WTF for creating a new box"""

    id = HiddenField('Id', [InputRequired()])
    label = StringField('Name', [InputRequired()])
    box_type = SelectField('Box Type', [InputRequired()])
    freezer_id = SelectField('Freezer', [InputRequired()])
    owner = StringField('Owner', [])


@BOX.route('/', methods=['POST'])
def new_box():
    """Insert a single dataset into the SQLite database"""

    box = Box()
    box.label = request.form.get('label')
    box.box_type = request.form.get('box_type')
    box.freezer_id = request.form.get('freezer_id')
    box.owner = request.form.get('owner')

    with create_new_session() as session:
        session.add(
            box
        )

        session.commit()

        return redirect(request.referrer)


@BOX.route('/', methods=['GET'])
def all_boxes():
    """Retrieve all boxes"""

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).all()

        return render_template(
            'boxes.html',
            boxes=boxes
        )


@BOX.route('/<box_id>', methods=['GET'])
def box_samples(box_id):
    """Retrieve samples in a specific box"""

    with create_new_session() as session:

        samples = session.query(
            Vial
        ).filter(
            Vial.box_id == box_id
        ).all()

        box = session.query(
            Box
        ).filter(
            Box.id == box_id
        ).first()

        return render_template(
            'samples.html',
            box=box,
            samples=samples,
            title="Samples"
        )


@BOX.route('/create/', methods=['GET'])
def create_box():
    """Provide the HTML form for box creation"""

    with create_new_session() as session:

        freezers = session.query(
            Freezer
        ).all()

        box_types = session.query(
            BoxType
        ).all()

        form = BoxForm()
        return render_template(
            'box_create.html',
            form=form,
            box_types=box_types,
            freezers=freezers)
