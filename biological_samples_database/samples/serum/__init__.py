"""

Serum

All API information related to Serum samples

"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from wtforms import StringField

# Local Imports
from .. import SampleForm, populate_default_values
from ...database import create_new_session
from ...model.sample import Serum
from ...model.storage import Box


SERUM = Blueprint(
    'serum',
    __name__,
    template_folder='templates'
)


class SerumForm(SampleForm):
    '''Form for handling Serum data'''

    pathwest_id = StringField('PathWest ID')


@SERUM.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    serum = Serum()
    populate_default_values(request, serum)

    with create_new_session() as session:

        session.add(
            serum
        )

        session.commit()
        return redirect(request.referrer)


@SERUM.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Serum data from the SQLite database"""

    form = SerumForm()

    with create_new_session() as session:

        serums = session.query(
            Serum
        ).all()

        return render_template(
            'serum.html',
            serums=serums,
            form=form
        )


@SERUM.route('/create/', methods=['GET'])
def create_serum():
    """Provide the HTML form for serum creation"""

    sample_title = 'Add Serum'
    sample_action = "/samples/serum/"

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).all()

        form = SerumForm()
        return render_template(
            'serum_create.html',
            form=form,
            boxes=boxes,
            sample_title=sample_title,
            sample_action=sample_action)
