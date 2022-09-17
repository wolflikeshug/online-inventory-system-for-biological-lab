"""

Plasma.

All API information related to Plasma samples

"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from wtforms import StringField

# Local Imports
from .. import SampleForm, populate_default_values
from ...database import create_new_session
from ...model.sample import Plasma
from ...model.storage import Box


PLASMA = Blueprint(
    'plasma',
    __name__,
    template_folder='templates'
)


class PlasmaForm(SampleForm):
    '''Website link for page holding RSS data'''

    visit_number = StringField('Visit Number')


@PLASMA.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    plasma = Plasma()
    populate_default_values(request, plasma)

    # Plasma specific variables
    plasma.visit_number = request.form.get('visit_number')

    with create_new_session() as session:

        session.add(
            plasma
        )

        session.commit()
        return redirect(request.referrer)


@PLASMA.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Plasma data from the SQLite database"""

    form = PlasmaForm()

    with create_new_session() as session:

        plasmas = session.query(
            Plasma
        ).all()

        return render_template(
            'plasma.html',
            plasmas=plasmas,
            form=form,
            title="Inventory"
        )


@PLASMA.route('/create/', methods=['GET'])
def create_plasma_form():
    """Provide the HTML form for serum creation"""

    sample_title = 'Add Plasma'
    sample_action = "/samples/plasma/"

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).all()

        form = PlasmaForm()
        return render_template(
            'plasma_create.html',
            form=form,
            boxes=boxes,
            sample_title=sample_title,
            sample_action=sample_action,
            title="Inventory")
