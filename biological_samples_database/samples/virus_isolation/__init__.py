"""

Virus Isolation

All API information related to Virus Isolation samples

"""

# Flask
from flask import Blueprint, redirect, render_template, request

# Flask WTF
from wtforms import StringField

# Local Imports
from .. import SampleForm, populate_default_values, sample_search
from ...database import create_new_session
from ...model.sample import VirusIsolation
from ...model.storage import Box


VIRUS_ISOLATION = Blueprint(
    'virus_isolation',
    __name__,
    template_folder='templates'
)


class VirusIsolationForm(SampleForm):
    '''Form for handling Virus Isolation data'''

    pathwest_id = StringField('PathWest ID')
    batch_number = StringField('Batch Number')
    passage_number = StringField('Passage Number')
    growth_media = StringField('Growth Media')


@VIRUS_ISOLATION.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    with create_new_session() as session:

        sample_id = request.form.get('db_id')
        virus_isolation = sample_search(session, sample_id, VirusIsolation)

        populate_default_values(request, virus_isolation)
        # Pbmc specific variables
        virus_isolation.pathwest_id = request.form.get('pathwest_id')
        virus_isolation.batch_number = request.form.get('batch_number')
        virus_isolation.passage_number = request.form.get('passage_number')
        virus_isolation.growth_media = request.form.get('growth_media')

        if not sample_id:
            session.add(
                virus_isolation
            )

        session.commit()
        return redirect(request.referrer)


@VIRUS_ISOLATION.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Virus Isolation data from the database"""

    form = VirusIsolationForm()

    with create_new_session() as session:

        virus_isolations = session.query(
            VirusIsolation
        ).all()

        return render_template(
            'virus_isolation.html',
            virus_isolations=virus_isolations,
            form=form
        )


@VIRUS_ISOLATION.route('/create/', methods=['GET'])
def create_virus_isolation():
    """Provide the HTML form for virus_isolation creation"""

    sample_title = 'Add VirusIsolation'
    sample_action = "/samples/virus_isolation/"

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).all()

        form = VirusIsolationForm()
        return render_template(
            'virus_isolation_create.html',
            form=form,
            boxes=boxes,
            sample_title=sample_title,
            sample_action=sample_action)
