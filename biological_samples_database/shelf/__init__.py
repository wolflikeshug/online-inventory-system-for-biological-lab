"""
Shelves.

Module for populating and altering shelf data.

"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
from ..model.storage import Building, Room, Freezer, Shelf


SHELF = Blueprint(
    'shelf',
    __name__,
    template_folder='templates'
)


class ShelfForm(FlaskForm):
    '''Website link for page holding RSS data'''

    id = HiddenField('Id', [InputRequired()])
    name = StringField('Name', [InputRequired()])
    freezer_id = SelectField('Freezer')


@SHELF.route('/', methods=['POST'])
def create():
    """Insert a single dummy dataset into the SQLite database"""

    shelf = Shelf()
    shelf.name = request.form.get('name')
    shelf.freezer_id = request.form.get('freezer_id')

    with create_new_session() as session:

        session.add(
            shelf
        )

        session.commit()

    return redirect(request.referrer)


@SHELF.route('/', methods=['GET'])
def all_boxes():

    with create_new_session() as session:

        shelves = session.query(
            Shelf
        ).all()

        return render_template(
            'room.html',
            shelves=shelves,
            title="Freezers"
        )


@SHELF.route('/create', methods=['GET'])
def read_all():
    """Placeholder for retrieving Shelf data from the SQLite database"""

    form = ShelfForm()

    with create_new_session() as session:

        freezers = session.query(
            Freezer
        ).all()


        return render_template(
            'shelf_create.html',
            freezers=freezers,
            form=form,
            title="Freezers")
