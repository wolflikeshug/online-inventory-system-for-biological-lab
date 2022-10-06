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
from ..authentication import phd_required, guest_required
from ..database import create_new_session
from ..model.storage import Box, BoxType, Freezer, Shelf
from ..model.sample import Vial
from ..samples import (
    SampleForm,
    all_samples_page,
    build_sample_edit_form,
    build_sample_form,
    delete_sample,
    sample_create
)
from ..samples.cell_line import CellLineForm


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
    shelf_id = SelectField('Shelf/Tower', [InputRequired()])
    owner = StringField('Owner', [])


@BOX.route('/', methods=['POST'])
@phd_required
def new_box():
    """Insert a single dataset into the SQLite database"""

    box = Box()
    box.label = request.form.get('label')
    box.box_type = request.form.get('box_type')
    box.shelf_id = request.form.get('shelf_id')
    box.owner = request.form.get('owner')

    with create_new_session() as session:

        shelf = session.query(
            Shelf
        ).filter(
            Shelf.id == box.shelf_id
        ).first()
        
        box.freezer_id = shelf.freezer.id

        session.add(
            box
        )

        session.commit()

        return redirect(request.referrer)


@BOX.route('/', methods=['GET'])
@guest_required
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
@guest_required
def box_samples(box_id):
    """Retrieve samples in a specific box"""

    with create_new_session() as session:

        samples = session.query(
            Vial
        ).filter(
            Vial.box_id == box_id
        ).filter(
            Vial.used == False
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
@phd_required
def create_box():
    """Provide the HTML form for box creation"""

    with create_new_session() as session:

        box_types = session.query(
            BoxType
        ).all()

        shelves = session.query(
            Shelf
        ).all()

        form = BoxForm()
        return render_template(
            'box_create.html',
            form=form,
            box_types=box_types,
            shelves=shelves) 

@BOX.route('/create/<shelf_id>', methods=['GET'])
@phd_required
def create_box_shelf(shelf_id):
    """Provide the HTML form for box creation"""

    with create_new_session() as session:

        box_types = session.query(
            BoxType
        ).all()

        shelf = session.query(
            Shelf
        ).filter(
            Shelf.id == shelf_id
        ).first()

        form = BoxForm()
        return render_template(
            'box_create.html',
            form=form,
            box_types=box_types,
            shelf=shelf) 