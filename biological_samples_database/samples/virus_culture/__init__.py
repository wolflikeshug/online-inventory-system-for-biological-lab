"""

Virus Culture

All API information related to Virus Culture samples

"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from wtforms import StringField

# Local Imports
from .. import SampleForm, populate_default_values, sample_search
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
