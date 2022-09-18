"""

Mosquito

All API information related to Mosquito samples

"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from wtforms import StringField

# Local Imports
from .. import (
    SampleForm,
    populate_default_values,
    populate_edit_values,
    sample_search
)
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

    with create_new_session() as session:

        sample_id = request.form.get('db_id')
        mosquito = sample_search(session, sample_id, Mosquito)
        populate_default_values(request, mosquito)

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


@MOSQUITO.route('/edit/<mosquito_id>', methods=['GET'])
def edit_mosquito_form(mosquito_id):
    """Provide the HTML form for Mosquito creation"""

    sample_title = 'Edit Mosquito'
    sample_action = "/samples/mosquito/"

    with create_new_session() as session:

        # Search for Sample
        mosquito = sample_search(session, mosquito_id, Mosquito)

        # Display error if not found
        if not mosquito.id:
            return f"Mosquito with reference ID {mosquito_id} not found"

        form = MosquitoForm()
        populate_edit_values(form, mosquito)

        form.passage_number.data = mosquito.passage_number
        form.cell_count.data = mosquito.cell_count
        form.growth_media.data = mosquito.growth_media
        form.vial_source.data = mosquito.vial_source
        form.lot_number.data = mosquito.lot_number

        return render_template(
            'mosquito_create.html',
            form=form,
            sample_title=sample_title,
            sample_action=sample_action)
