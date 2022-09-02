"""

Serum

All API information related to Serum samples

"""

# Standard Imports
import uuid

# Flask
from flask import Blueprint, render_template, request

# Flask WTF
from flask_wtf import FlaskForm
from wtforms import StringField

# Local Imports
from ...database import create_new_session
from ...model.sample import Serum


SERUM = Blueprint(
    'serum',
    __name__,
    template_folder='templates'
)


class SerumForm(FlaskForm):
    '''Website link for page holding RSS data'''

    serum_name = StringField('Serum')


@SERUM.route('/', methods=['POST'])
def create():
    """Insert a single dataset into the SQLite database"""

    serum = Serum()    
    serum.lab_id = None
    serum.box_id = None
    serum.position = None
    serum.sample_date = None
    serum.volume_ml = None
    serum.user_id = None
    serum.notes = None

    with create_new_session() as session:

        session.add(
            serum
        )

        session.commit()

    return '<div>SUCCESS<div>'


@SERUM.route('/', methods=['GET'])
def read_all():
    """Placeholder for retrieving Serum data from the SQLite database"""

    form = SerumForm()

    with create_new_session() as session:

        serums = session.query(
            Serum
        ).all()

        print(serums)

        return render_template(
            'serums.html',
            serums=serums,
            form=form
        )


@SERUM.route('/sample_id', methods=['GET'])
def read():
    """Placeholder for retrieving Serum data from the SQLite database"""

    args = request.args
    sample_id = args.get('sample_id')

    return f"SERUM RETRIEVAL INDIVIDUAL: {sample_id}"


@SERUM.route('/', methods=['PATCH'])
def update():
    """Placeholder for updating Serum data in the SQLite database"""

#  May need HTTP POST request and set the X-HTTP-Method-Override


@SERUM.route('/', methods=['DELETE'])
def delete():
    """Placeholder for deleting Serum data in the SQLite database"""

#  May need HTTP POST request and set the X-HTTP-Method-Override
