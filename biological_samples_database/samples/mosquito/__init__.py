"""

Mosquito

All API information related to Mosquito samples

"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from wtforms import StringField

# Local Imports
from .. import SampleForm, populate_default_values
from ...database import create_new_session
from ...model.sample import Mosquito
from ...model.storage import Box


MOSQUITO = Blueprint(
    'mosquito',
    __name__,
    template_folder='templates'
)


class MosquitoForm(SampleForm):
    '''Form for handling Mosquito data'''

    pathwest_id = StringField('PathWest ID')


@MOSQUITO.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    mosquito = Mosquito()
    populate_default_values(request, mosquito)

    with create_new_session() as session:

        session.add(
            mosquito
        )

        session.commit()
        return redirect(request.referrer)


@MOSQUITO.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Mosquito data from the SQLite database"""

    form = MosquitoForm()

    with create_new_session() as session:

        mosquitoes = session.query(
            Mosquito
        ).all()

        print(mosquitoes)

        return render_template(
            'mosquito.html',
            mosquitoes=mosquitoes,
            form=form
        )


@MOSQUITO.route('/create/', methods=['GET'])
def create_mosquito():
    """Provide the HTML form for mosquito creation"""

    sample_title = 'Add Mosquito'
    sample_action = "/samples/mosquito/"

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).all()

        form = MosquitoForm()
        return render_template(
            'mosquito_create.html',
            form=form,
            boxes=boxes,
            sample_title=sample_title,
            sample_action=sample_action)
