"""
Box

API for handling box data.
"""

# Flask
from flask import Blueprint, flash, redirect, render_template, request

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..authentication import phd_required, guest_required, staff_required
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
    shelf_id = SelectField('Freezer (Shelf/Tower)', [InputRequired()])
    owner = StringField('Owner', [])


@BOX.route('/', methods=['POST'])
@phd_required
def new_box():
    """Insert a single dataset into the SQLite database"""
    box_id = request.form.get('id')
    with create_new_session() as session:
        #Check if request is an edit or a creation:
        if not box_id:
            box = Box()
        else:
            box = session.query(
                Box
            ).filter(
                Box.id == box_id
            ).first()
        #Assign form values to object
        box.label = request.form.get('label')
        box.box_type = request.form.get('box_type')
        box.shelf_id = request.form.get('shelf_id')
        box.owner = request.form.get('owner')
        shelf = session.query(
            Shelf
        ).filter(
            Shelf.id == box.shelf_id
        ).first()
        box.freezer_id = shelf.freezer.id        
        #If its a creation add it to DB
        if not box_id:
            session.add(
                box
            )
        #commit changes
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

@BOX.route('/edit/<box_id>', methods=['GET'])
@phd_required
def edit_box(box_id):
    """Edit Box Details"""
    form = BoxForm()
    with create_new_session() as session:

        box = session.query(
            Box
        ).filter(
            Box.id == box_id
        ).first()

        shelves=[box.shelf]
        other_shelves = session.query(
            Shelf
        ).filter(
            Shelf.id != box.shelf_id
        ).all()
        shelves += other_shelves
        box_types = session.query(
            BoxType
        ).all()

        form['id'].data = getattr(box, 'id')
        standard_freezer_columns = [
        'label',
        'box_type',
        'shelf_id',
        'owner'
        ]

        for column_name in standard_freezer_columns:
            form[column_name].data = getattr(box, column_name)
        
        return render_template(
            'box_create.html',
            form=form,
            box_types=box_types,
            shelves=shelves)

@BOX.route('/delete/<box_id>', methods=['GET'])
@staff_required
def delete_box(box_id):
    """Delete Box"""

    with create_new_session() as session:

        session.query(
            Box
        ).filter(
            Box.id == box_id
        ).delete()
        
        session.commit()

    flash(f'Box Deleted', 'danger')
    return redirect(request.referrer)