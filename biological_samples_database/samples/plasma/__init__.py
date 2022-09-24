"""

Plasma.

All API information related to Plasma samples

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
from ...model.sample import Plasma
from ...model.storage import Box


PLASMA = Blueprint(
    'plasma',
    __name__,
    template_folder='templates'
)


class PlasmaForm(SampleForm):
    '''Sample specific data'''

    visit_number = StringField('Visit Number')


@PLASMA.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    with create_new_session() as session:

        sample_id = request.form.get('db_id')
        plasma = sample_search(session, sample_id, Plasma)

        populate_default_values(request, plasma)

        # Plasma specific variables
        plasma.visit_number = request.form.get('visit_number')

        if not sample_id:
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

        samples = session.query(
            Plasma
        ).all()

        return render_template(
            'sample_base.html',
            sample_type='plasma',
            target_sample_header_html_file='plasma_header_stub.html',
            target_sample_data_html_file='plasma_data_stub.html',
            samples=samples,
            form=form
        )


@PLASMA.route('/create/', methods=['GET'])
def create_plasma_form():
    """Provide the HTML form for plasma creation"""

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


@PLASMA.route('/edit/<plasma_id>', methods=['GET'])
def edit_plasma_form(plasma_id):
    """Provide the HTML form for PLASMA creation"""

    sample_title = 'Edit PLASMA'
    sample_action = "/samples/plasma/"

    with create_new_session() as session:

        # Search for Sample
        plasma = sample_search(session, plasma_id, Plasma)

        # Display error if not found
        if not plasma.id:
            return f"PLASMA with reference ID {plasma_id} not found"

        form = PlasmaForm()
        populate_edit_values(form, plasma)

        # Plasma specific variables
        form.visit_number.data = plasma.visit_number

        return render_template(
            'plasma_create.html',
            form=form,
            sample_title=sample_title,
            sample_action=sample_action)


@PLASMA.route('/delete/<plasma_id>', methods=['GET'])
def delete_plasma_form(plasma_id):
    """Delete a PLASMA item using ID"""

    with create_new_session() as session:

        session.query(
            Plasma
        ).filter(
            Plasma.id == plasma_id
        ).delete()

        session.commit()
