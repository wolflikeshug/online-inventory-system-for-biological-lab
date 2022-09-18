"""

Pbmc.

All API information related to Pbmc samples

"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from wtforms import IntegerField, StringField


# Local Imports
from .. import (
    SampleForm,
    populate_default_values,
    populate_edit_values,
    sample_search
)
from ...database import create_new_session
from ...model.sample import Pbmc
from ...model.storage import Box


PBMC = Blueprint(
    'pbmc',
    __name__,
    template_folder='templates'
)


class PbmcForm(SampleForm):
    '''Website link for page holding RSS data'''

    visit_number = StringField('Visit Number')
    cell_count = IntegerField('Cell Count (millions)')
    patient_code = StringField('Patient ID')


@PBMC.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    with create_new_session() as session:

        sample_id = request.form.get('db_id')
        pbmc = sample_search(session, sample_id, Pbmc)

        populate_default_values(request, pbmc)

        # PBMC specific variables
        pbmc.visit_number = request.form.get('visit_number')
        pbmc.cell_count = request.form.get('cell_count')
        pbmc.patient_code = request.form.get('patient_code')

        if not sample_id:
            session.add(
                pbmc
            )

        session.commit()
        return redirect(request.referrer)


@PBMC.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Pbmc data from the SQLite database"""

    form = PbmcForm()

    with create_new_session() as session:

        pbmcs = session.query(
            Pbmc
        ).all()

        return render_template(
            'pbmc.html',
            pbmcs=pbmcs,
            form=form,
            title="Inventory"
        )


@PBMC.route('/create/', methods=['GET'])
def create_pbmc_form():
    """Provide the HTML form for serum creation"""

    sample_title = 'Add PBMC'
    sample_action = "/samples/pbmc/"

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).all()

        form = PbmcForm()
        return render_template(
            'pbmc_create.html',
            form=form,
            boxes=boxes,
            sample_title=sample_title,
            sample_action=sample_action,
            title="Inventory")


@PBMC.route('/edit/<pbmc_id>', methods=['GET'])
def edit_pbmc_form(pbmc_id):
    """Provide the HTML form for PBMC creation"""

    sample_title = 'Edit PBMC'
    sample_action = "/samples/pbmc/"

    with create_new_session() as session:

        # Search for Sample
        pbmc = sample_search(session, pbmc_id, Pbmc)

        # Display error if not found
        if not pbmc.id:
            return f"PBMC with reference ID {pbmc_id} not found"

        form = PbmcForm()
        populate_edit_values(form, pbmc)

        # Cell Line specific variables
        pbmc.patient_code = request.form.get('patient_code')
        pbmc.visit_number = request.form.get('visit_number')
        pbmc.cell_count = request.form.get('cell_count')

        return render_template(
            'pbmc_create.html',
            form=form,
            sample_title=sample_title,
            sample_action=sample_action)
