"""
Biological Samples Database.

"""

# Standard Imports

# Flask Imports
from flask import Flask

from sqlalchemy.exc import IntegrityError

# Blueprint Storage Imports
from .building import BUILDING
from .box import BOX
from .freezer import FREEZER
from .room import ROOM
from .shelf import SHELF

# Blueprint Sample Imports
from .samples import SAMPLE
from .samples.cell_line import CELL_LINE
from .samples.mosquito import MOSQUITO
from .samples.other import OTHER
from .samples.pbmc import PBMC
from .samples.peptide import PEPTIDE
from .samples.plasma import PLASMA
from .samples.rna import RNA
from .samples.serum import SERUM
from .samples.supernatant import SUPERNATANT
from .samples.virus_culture import VIRUS_CULTURE
from .samples.virus_isolation import VIRUS_ISOLATION
from .samples.antigen import ANTIGEN

# Blueprint General Imports
from .search import SEARCH
from .users import USERS
from .routes import MAIN
from .upload import UPLOAD

# Database Imports
from .database import db, engine, create_new_session

# Models and Forms
from .model import storage, Base
from .model.user import login_man, User
from .routes import bcrypt


# Flask Package and-SQLAlchemy link to Database
APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../biological_samples.sqlite'
APP.config['UPLOAD_FOLDER'] = 'static/excels'

bcrypt.init_app(APP)
login_man.init_app(APP)
db.init_app(APP)


def initialise_sqlite_database():
    """Instantiate the SQLite database if it does not exist"""
    # TODO - Refactor this function into smaller pieces

    Base.metadata.create_all(engine, checkfirst=True)

    with create_new_session() as session:

        unknown_user = User(
            username="admin",
            email=" ",
            first=" ",
            last=" ",
            password="$2b$12$5.BOBrLHc6N/XLFBLrEXg.sQmy4tzOOtMtStAI6BbsjfANdNsjVqa", # == biological
            gid=1)

        session.add(
            unknown_user
        )
        try:
            session.flush()
        except IntegrityError:
            session.rollback()

        initial_box_types = {
            "9x9": [9, 9],
            "10x10": [10, 10],
            "Wax Box (Standard)": [10, 22],
            "Wax Box (5ml)": [7, 16],
            "Wax Box (Large)": [10, 24]
        }

        for name, dimensions in initial_box_types.items():
            box_type = storage.BoxType()
            box_type.name = name
            box_type.height = dimensions[0]
            box_type.width = dimensions[1]
            session.add(box_type)

        try:
            session.flush()
        except IntegrityError:
            session.rollback()

        initial_freezer_types = [
            "-80c",
            "LN2"
        ]

        for name in initial_freezer_types:
            freezer_type = storage.FreezerType()
            freezer_type.name = name
            session.add(freezer_type)
        
        try:
            session.flush()
        except IntegrityError:
            session.rollback()

        session.commit()


def initialise_app():
    '''Setup and initialise logging and other shared components
    of the Flask app'''

    app = APP
    app.secret_key = 'HUSHHUSHVERYSECRET'
    initialise_sqlite_database()
    app.register_blueprint(MAIN, url_prefix='')
    app.register_blueprint(UPLOAD, url_prefix='/upload')
    app.register_blueprint(USERS, url_prefix='/users')
    app.register_blueprint(SAMPLE, url_prefix='/samples')
    app.register_blueprint(SEARCH, url_prefix='/search')
    
    app.register_blueprint(ANTIGEN, url_prefix='/samples/antigen')
    app.register_blueprint(CELL_LINE, url_prefix='/samples/cell_line')
    app.register_blueprint(MOSQUITO, url_prefix='/samples/mosquito')
    app.register_blueprint(OTHER, url_prefix='/samples/other')
    app.register_blueprint(PLASMA, url_prefix='/samples/plasma')
    app.register_blueprint(PBMC, url_prefix='/samples/pbmc')
    app.register_blueprint(PEPTIDE, url_prefix='/samples/peptide')
    app.register_blueprint(RNA, url_prefix='/samples/rna')
    app.register_blueprint(SERUM, url_prefix='/samples/serum')
    app.register_blueprint(SUPERNATANT, url_prefix='/samples/supernatant')
    app.register_blueprint(VIRUS_CULTURE, url_prefix='/samples/virus_culture')
    app.register_blueprint(
        VIRUS_ISOLATION,
        url_prefix='/samples/virus_isolation')
    
    app.register_blueprint(BUILDING, url_prefix='/building/')
    app.register_blueprint(FREEZER, url_prefix='/freezer/')
    app.register_blueprint(ROOM, url_prefix='/room/')
    app.register_blueprint(BOX, url_prefix='/box/')
    app.register_blueprint(SHELF, url_prefix='/shelf/')
    return app
