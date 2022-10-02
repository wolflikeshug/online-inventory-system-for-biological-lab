"""
Sample.
"""

# Standard
from datetime import datetime

# Flask
from flask import Blueprint, redirect, render_template, request
from flask_login import current_user

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    DateField,
    FloatField,
    HiddenField,
    SelectField,
    StringField,
    TextAreaField
)
from wtforms.validators import InputRequired

# Local Imports
from ..database import create_new_session
from ..model.sample import Vial
from ..model.storage import Box
from ..authentication import guest_required, student_required

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
        #POSSIBLE FUCKUP 
        #default=datetime.strptime(
        #    '1900-01-01',
        #    '%Y-%m-%d'),
        default=datetime.today, 
        format='%Y-%m-%d'
    )
    # POSSIBLE FUCKUP volume_ml = FloatField('Volume (ml)')
    volume_ml = FloatField('Volume')
    user_id = HiddenField('User ID')
    used = BooleanField('Used', default=False)
    # POSSIBLE FUCKUP notes = StringField('Notes')
    notes = TextAreaField('Notes')


def populate_sample_values(request, sample, custom_variables):
    """Populates the default sample values of a sample"""

    standard_vial_columns = [
        'lab_id',
        'box_id',
        'position',
        'volume_ml',
        'notes'
    ]

    standard_vial_columns.extend(custom_variables)

    for column_name in standard_vial_columns:
        sample_value = request.form.get(column_name)
        if sample_value and sample_value != '':
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


def populate_edit_values(form, sample, custom_variables):
    """Populate a form with existing values for editing"""

    form['db_id'].data = getattr(sample, 'id')

    standard_vial_columns = [
        'lab_id',
        'position',
        'sample_date',
        'volume_ml',
        'notes'
    ]
    standard_vial_columns.extend(custom_variables)

    for column_name in standard_vial_columns:
        form[column_name].data = getattr(sample, column_name)

    form.user_id.data = str(current_user)


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


def sample_create(request, sample_class, custom_variables):
    """Generic POST request handler for a sample"""

    with create_new_session() as session:

        sample_id = request.form.get('db_id')
        sample_class = sample_search(session, sample_id, sample_class)

        populate_sample_values(request, sample_class, custom_variables)

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


def build_sample_form_in_pos(sample_title, sample_type, sample_form, box_id, pos):
    """Provide the HTML form for sa,[;e] creation"""
    sample_action = f"/samples/{sample_type}/"
    if box_id and pos:
        with create_new_session() as session:

            box = session.query(
                Box
            ).filter(
                Box.id == box_id
            ).first()
            
            form = sample_form()
            return render_template(
                f'{sample_type}_create.html',
                form=form,
                box=box,
                position = pos,
                sample_title=sample_title,
                sample_action=sample_action,
                title="Inventory")

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


def build_sample_edit_form(sample_title, sample_id, sample_type, sample_form, sample_class, custom_variables):
    """Provide the HTML form for Cell Line creation"""

    sample_action = f"/samples/{sample_type}/"

    with create_new_session() as session:

        # Search for Sample
        sample = sample_search(session, sample_id, sample_class)

        # Display error if not found
        if not sample.id:
            return f"Sample type {sample_type} with reference ID {sample_id} not found"

        form = sample_form()
        populate_edit_values(form, sample, custom_variables)

        
        with create_new_session() as session:
            vial = session.query(
                Vial
            ).filter(
                Vial.id == sample_id
            ).first()

            boxes = [vial.box]
            other_boxes = session.query(
                Box
            ).filter(
                Box.id != boxes[0].id
            ).all()

            boxes = boxes + other_boxes

            return render_template(
                f'{sample_type}_create.html',
                boxes=boxes,
                form=form,
                sample_title=sample_title,
                sample_action=sample_action)


def delete_sample(sample_class, sample_id):
    """Delete a sample"""

    with create_new_session() as session:

        sample = session.query(
            sample_class
        ).filter(
            sample_class.id == sample_id
        ).first()

        session.delete(sample)
        session.commit()


@SAMPLE.route('/<box_id>', methods=['GET'])
@guest_required
def box_samples(box_id):
    """Retrieve box layout of specific boxes"""

    with create_new_session() as session:

        vials = session.query(
            Vial
        ).filter(
            Vial.box_id == box_id
        ).filter(
            Vial.used == False
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
@guest_required
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
                box=box,
                position = pos
            )

        return render_template(
            'sample_add.html',
            box=box,
            position = pos
        )

@SAMPLE.route('remove/<sample_id>')
@student_required
def remove(sample_id):
    """Sets used flag of sample"""

    with create_new_session() as session:

        vial = session.query(
            Vial
        ).filter(
            Vial.id == sample_id
        ).first()

        if vial:
            vial.used = True
            session.commit()
    
    return(redirect(request.referrer))

@SAMPLE.route('reinstate/<sample_id>')
@student_required
def reinstate(sample_id):
    """Unsets used flag of sample"""

    with create_new_session() as session:

        vial = session.query(
            Vial
        ).filter(
            Vial.id == sample_id
        ).first()

        if vial:
            vial.used = False
            session.commit()
    return(redirect(request.referrer))