"""
Sample.
"""

# Standard
from datetime import datetime

# Flask
from flask import Blueprint, redirect, render_template
from flask_login import current_user

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    DateField,
    FloatField,
    HiddenField,
    SelectField,
    StringField
)
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
from ..model.sample import Vial
from ..model.storage import Box

SAMPLE = Blueprint(
    'sample',
    __name__,
    template_folder='templates'
)


class SampleForm(FlaskForm):
    '''Sample specific data'''

    db_id = HiddenField('db_id')
    lab_id = StringField('ID', validators=[InputRequired()])
    box_id = SelectField('Box', [InputRequired()])
    position = StringField('Position')
    sample_date = DateField(
        'Sample Date',
        default=datetime.strptime(
            '1900-01-01',
            '%Y-%m-%d'),
        format='%Y-%m-%d'
    )
    volume_ml = FloatField('Volume (ml)')
    user_id = HiddenField('User ID')
    used = BooleanField('Used', default=False)
    notes = StringField('Notes')


def populate_default_values(request, sample):
    """Populates the default sample values of a sample"""

    standard_vial_columns = [
        'lab_id',
        'box_id',
        'position',
        'volume_ml',
        'notes'
    ]

    for column_name in standard_vial_columns:

        if request.form.get(column_name):
            setattr(
                sample,
                column_name,
                request.form.get(column_name)
            )

    if request.form.get('sample_date'):

        raw_date = request.form.get('sample_date')

        try:
            sample.sample_date = datetime.strptime(
                raw_date,
                '%Y-%m-%d'
            )
        except ValueError:
            # Code will fall back to model default value
            pass

    sample.user_id = str(current_user)  


def populate_edit_values(form, sample):
    """Populate a form with existing values for editing"""

    form.db_id.data = sample.id
    form.lab_id.data = sample.lab_id
    form.position.data = sample.position
    form.sample_date.data = sample.sample_date
    form.volume_ml.data = sample.volume_ml
    form.user_id.data = str(current_user)
    form.notes.data = sample.notes


def sample_search(session, sample_id, sample_class):
    """Find a sample if it exists or create a new instance"""

    sample = None
    if sample_id:
        sample = session.query(
            sample_class
        ).filter(
            sample_class.id == sample_id
        ).first()
    else:
        sample = sample_class()

    return sample


def sample_create(request, sample_class, custom_variable_assignment):
    """Generic POST request handler for a sample"""

    with create_new_session() as session:

        sample_id = request.form.get('db_id')
        sample_class = sample_search(session, sample_id, sample_class)

        populate_default_values(request, sample_class)

        if custom_variable_assignment:
            custom_variable_assignment(request, sample_class)

        if not sample_id:
            session.add(
                sample_class
            )

        session.commit()
        return redirect(request.referrer)


def all_samples_page(sample_type, sample_class, sample_form):
    """Placeholder for retrieving sample data from the SQLite database"""

    form = sample_form()

    with create_new_session() as session:

        samples = session.query(
            sample_class
        ).all()

        return render_template(
            'sample_base.html',
            sample_type=f'{sample_type}',
            target_sample_header_html_file=f'{sample_type}_header_stub.html',
            target_sample_data_html_file=f'{sample_type}_data_stub.html',
            samples=samples,
            form=form
        )


def build_sample_form(sample_title, sample_type, sample_form):
    """Provide the HTML form for sa,[;e] creation"""

    sample_action = f"/samples/{sample_type}/"

    with create_new_session() as session:

        boxes = session.query(
            Box
        ).all()

        form = sample_form()
        return render_template(
            f'{sample_type}_create.html',
            form=form,
            boxes=boxes,
            sample_title=sample_title,
            sample_action=sample_action,
            title="Inventory")


def build_sample_edit_form(sample_title, sample_id, sample_type, sample_form, sample_class, custom_form_data_assignment):
    """Provide the HTML form for Cell Line creation"""

    sample_action = f"/samples/{sample_type}/"

    with create_new_session() as session:

        # Search for Sample
        sample = sample_search(session, sample_id, sample_class)

        # Display error if not found
        if not sample.id:
            return f"Sample type {sample_type} with reference ID {sample_id} not found"

        form = sample_form()
        populate_edit_values(form, sample)

        if custom_form_data_assignment:
            custom_form_data_assignment(form, sample)

        return render_template(
            f'{sample_type}_create.html',
            form=form,
            sample_title=sample_title,
            sample_action=sample_action)


def delete_sample(sample_class, sample_id):
    """Delete a sample"""

    with create_new_session() as session:

        session.query(
            sample_class
        ).filter(
            sample_class.id == sample_id
        ).delete()

        session.commit()


@SAMPLE.route('/<box_id>', methods=['GET'])
def box_samples(box_id):
    """Retrieve box layout of specific boxes"""

    with create_new_session() as session:

        vials = session.query(
            Vial
        ).filter(
            Vial.box_id == box_id
        ).all()

        box = session.query(
            Box
        ).filter(
            Box.id == box_id
        ).first()

        return render_template(
            'samples.html',
            samples=vials,
            box=box
        )


@SAMPLE.route('info/<box_id>/<pos>', methods=['GET'])
def samp_info(box_id, pos):
    """Return samples in a box location"""

    with create_new_session() as session:

        box = session.query(
            Box
        ).filter(
            Box.id == box_id
        ).first()

        vials = session.query(
            Vial
        ).filter(
            Vial.box_id == box_id
        ).filter(
            Vial.position == pos
        ).all()

        if vials:
            return render_template(
                'sample_info.html',
                samples=vials,
                box=box
            )

        return render_template(
            'sample_add.html',
            box=box
        )
