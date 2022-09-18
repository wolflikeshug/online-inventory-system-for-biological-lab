"""

Virus Culture

All API information related to Virus Culture samples

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
from ...model.sample import VirusCulture
from ...model.storage import Box


VIRUS_CULTURE = Blueprint(
    'virus_culture',
    __name__,
    template_folder='templates'
)


class VirusCultureForm(SampleForm):
    '''Form for handling Virus Culture data'''

    pathwest_id = StringField('PathWest ID')
    batch_number = StringField('Batch Number')
    passage_number = StringField('Passage Number')
    growth_media = StringField('Growth Media')


@VIRUS_CULTURE.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    with create_new_session() as session:

        sample_id = request.form.get('db_id')
        virus_culture = sample_search(session, sample_id, VirusCulture)

        populate_default_values(request, virus_culture)
        # Pbmc specific variables
        virus_culture.pathwest_id = request.form.get('pathwest_id')
        virus_culture.batch_number = request.form.get('batch_number')
        virus_culture.passage_number = request.form.get('passage_number')
        virus_culture.growth_media = request.form.get('growth_media')

        if not sample_id:
            session.add(
                virus_culture
            )

        session.commit()
        return redirect(request.referrer)


@VIRUS_CULTURE.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Virus Culture data from the database"""

    form = VirusCultureForm()

    with create_new_session() as session:

        virus_cultures = session.query(
            VirusCulture
        ).all()

        return render_template(
            'virus_culture.html',
            virus_cultures=virus_cultures,
            form=form
        )


@VIRUS_CULTURE.route('/create/', methods=['GET'])
def create_virus_culture():
    """Provide the HTML form for virus_culture creation"""

    sample_title = 'Add VirusCulture'
    sample_action = "/samples/virus_culture/"

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).all()

        form = VirusCultureForm()
        return render_template(
            'virus_culture_create.html',
            form=form,
            boxes=boxes,
            sample_title=sample_title,
            sample_action=sample_action)


@VIRUS_CULTURE.route('/edit/<virus_culture_id>', methods=['GET'])
def edit_virus_culture_form(virus_culture_id):
    """Provide the HTML form for Virus Culture creation"""

    sample_title = 'Edit Virus Culture'
    sample_action = "/samples/virus_culture/"

    with create_new_session() as session:

        # Search for Sample
        virus_culture = sample_search(session, virus_culture_id, VirusCulture)

        # Display error if not found
        if not virus_culture.id:
            return f"Virus Culture with reference ID {virus_culture_id} not found"

        form = VirusCultureForm()
        populate_edit_values(form, virus_culture)

        # VirusCulture specific variables
        form.pathwest_id.data = virus_culture.pathwest_id
        form.batch_number.data = virus_culture.batch_number
        form.passage_number.data = virus_culture.passage_number
        form.growth_media.data = virus_culture.growth_media

        return render_template(
            'virus_culture_create.html',
            form=form,
            sample_title=sample_title,
            sample_action=sample_action)


@VIRUS_CULTURE.route('/delete/<virus_culture_id>', methods=['GET'])
def delete_virus_culture_form(virus_culture_id):
    """Delete a Virus Culture item using ID"""

    with create_new_session() as session:

        session.query(
            VirusCulture
        ).filter(
            VirusCulture.id == virus_culture_id
        ).delete()

        session.commit()
