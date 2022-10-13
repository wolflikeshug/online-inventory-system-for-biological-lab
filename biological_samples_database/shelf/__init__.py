"""
Shelves.

Module for populating and altering shelf data.

"""

# Flask
from flask import Blueprint, redirect, render_template, request, flash

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
from ..model.storage import Building, Room, Freezer, Shelf, Box
from ..authentication import guest_required, phd_required, staff_required


SHELF = Blueprint(
    'shelf',
    __name__,
    template_folder='templates'
)


class ShelfForm(FlaskForm):
    '''Sample specific data'''

    id = HiddenField('Id', [InputRequired()])
    name = StringField('Name', [InputRequired()])
    freezer_id = SelectField('Freezer')


@SHELF.route('/', methods=['POST'])
@staff_required
def create():
    """Insert a single dummy dataset into the SQLite database"""
    shelf_id = request.form.get('id')

    with create_new_session() as session:
        if not shelf_id:
            shelf = Shelf()
            shelf.name = request.form.get('name')
            shelf.freezer_id = request.form.get('freezer_id')
            session.add(
                shelf
            )
            session.commit()
        else:
            shelf = session.query(
                Shelf
            ).filter(
                Shelf.id == shelf_id
            ).first()
        
            if shelf:
                shelf.name = request.form.get('name')
                shelf.freezer_id = request.form.get('freezer_id')
                session.commit()

        return redirect(request.referrer)


@SHELF.route('/', methods=['GET'])
@guest_required
def all_boxes():

    with create_new_session() as session:

        shelves = session.query(
            Shelf
        ).all()

        return render_template(
            'shelf.html',
            shelves=shelves,
            title="Freezers"
        )


@SHELF.route('/create/', methods=['GET'])
@phd_required
def create_box():
    """ Create a Shelf """

    form = ShelfForm()

    with create_new_session() as session:

        freezers = session.query(
            Freezer
        ).all()


        return render_template(
            'shelf_create.html',
            freezers=freezers,
            form=form,
            title="Create Shelf")

@SHELF.route('/create/<freezer_id>', methods=['GET'])
@staff_required
def create_box_freezer(freezer_id):
    """Create a Shelf on a specified freezer page"""

    form = ShelfForm()

    with create_new_session() as session:

        freezer = session.query(
            Freezer
        ).filter(
            Freezer.id == freezer_id
        ).first()


        return render_template(
            'shelf_create.html',
            freezer=freezer,
            form=form,
            title="Add Shelf")

@SHELF.route('/<shelf_id>', methods=['GET'])
@guest_required
def shelf_boxes(shelf_id):
    """Retrieve boxes in a specific shelf"""

    with create_new_session() as session:

        shelf = session.query(
            Shelf
        ).filter(
            Shelf.id == shelf_id
        ).first()

        boxes = session.query(
            Box
        ).filter(
            Box.shelf_id == shelf.id
        ).all()

        if boxes:            
            boxes.sort(key=lambda x: x.label)

        return render_template(
            'shelf_boxes.html',
            freezer=shelf.freezer,
            boxes=boxes,
            shelf=shelf,
            title="Freezers"
        )


@SHELF.route('/edit/<shelf_id>', methods=['GET'])
@staff_required
def edit_box(shelf_id):
    """Edit Freezer"""
    form = ShelfForm()
    with create_new_session() as session:

        shelf = session.query(
            Shelf
        ).filter(
            Shelf.id == shelf_id
        ).first()

        freezer= shelf.freezer
        '''
        BOXES ARE DOUBLY LINKED TO SHELF AND FREEZER, 
        REMOVED OPTION TO CHANGE SHELF TO ANOTHER FREEZER TO AVOID SYSTEM CORRUPTION
        freezers= [shelf.freezer]
        other_freezers= session.query(
            Freezer
        ).filter(
            Freezer.id != shelf.freezer_id
        ).all()
        if other_freezers:
            other_freezers.sort(key=lambda x: x.name)
            freezers += other_freezers
        
        standard_shelf_columns = [
        'name',
        'freezer_id'
        ]

        for column_name in standard_shelf_columns:
            form[column_name].data = getattr(shelf, column_name)
        
        '''
        form['name'].data = getattr(shelf,'name')
        form['id'].data = getattr(shelf, 'id')
        return render_template(
            'shelf_create.html',
            form=form,
            freezer=freezer,
            title="Edit Shelf")


@SHELF.route('/delete/<shelf_id>', methods=['GET'])
@staff_required
def delete_box(shelf_id):
    """Delete Shelf"""

    with create_new_session() as session:
        box_check = session.query(
            Box
        ).filter(
            Box.shelf_id == shelf_id
        ).all()

        if box_check:
            flash("This shelf contains Boxes, move them first!", "danger")
            return redirect(request.referrer)
            
        session.query(
            Shelf
        ).filter(
            Shelf.id == shelf_id
        ).delete()
        
        session.commit()

    flash(f'Shelf Deleted', 'danger')
    return redirect(request.referrer)