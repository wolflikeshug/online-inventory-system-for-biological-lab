"""
Biological Samples Database.



"""

# Standard Imports
import os

# Flask Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


# Blueprint Sample Imports
from .samples import SAMPLE
from .samples.cell_line import CELL_LINE
from .samples.mosquito import MOSQUITO
from .samples.serum import SERUM
from .samples.pbmc import PBMC
from .samples.plasma import PLASMA
from .samples.virus_culture import VIRUS_CULTURE
from .samples.virus_isolation import VIRUS_ISOLATION

# Blueprint Storage Imports
from .box import BOX
from .freezer import FREEZER
from .room import ROOM



# Flask Package and-SQLAlchemy link to Database 
APP = Flask(__name__)
login_man = LoginManager(APP)
bcrypt = Bcrypt(APP)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../biological_samples.sqlite'
db = SQLAlchemy(APP)

# Database Imports
from .database import engine, IRPD_PATH, create_new_session

# Models and Forms
from .model import storage, Base
from .model.user import User

from biological_samples_database import routes


def initialise_sqlite_database():
    """Instantiate the SQLite database if it does not exist"""

    # TODO - Refactor this function into smaller pieces

    if not os.path.exists(IRPD_PATH):
        Base.metadata.create_all(engine, checkfirst=True)

        with create_new_session() as session:

            unknown_user = User(
                username="UNKNOWN",
                email="UNKNOWN",
                first="UNKNOWN",
                last="UNKNOWN",
                password="UNKNOWN",
                gid=9999)

            session.add(
                unknown_user
            )
            session.flush()

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
            session.flush()

            unknown_building = storage.Building()
            unknown_building.name = 'UNKNOWN'
            session.add(
                unknown_building
            )
            session.flush()

            unknown_room = storage.Room()
            unknown_room.name = 'UNKNOWN'
            unknown_room.building_id = unknown_building.id
            session.add(
                unknown_room
            )
            session.flush()

            initial_freezer_types = [
                "-80c",
                "LN2"
            ]

            for name in initial_freezer_types:
                freezer_type = storage.FreezerType()
                freezer_type.name = name
                session.add(freezer_type)
            session.flush()

            freezer_type = storage.FreezerType
            unknown_freezer = storage.Freezer()
            unknown_freezer.name = 'UNKNOWN'
            unknown_freezer.room_id = unknown_room.id
            unknown_freezer.freezer_type = session.query(
                freezer_type
            ).first().id
            session.add(
                unknown_freezer
            )
            session.flush()

            unknown_box = storage.Box()
            unknown_box.label = 'UNKNOWN'
            unknown_box.freezer_id = unknown_freezer.id

            box_type = storage.BoxType
            unknown_box.box_type = session.query(
                box_type
            ).first().id
            session.add(
                unknown_box
            )
            session.flush()
            session.commit()


def initialise_app():
    '''Setup and initialise logging and other shared components
    of the Flask app'''

    app = APP
    app.secret_key = 'HUSHHUSHVERYSECRET'
    initialise_sqlite_database()
    app.register_blueprint(SAMPLE, url_prefix='/samples')
    app.register_blueprint(CELL_LINE, url_prefix='/samples/cell_line')
    app.register_blueprint(MOSQUITO, url_prefix='/samples/mosquito')
    app.register_blueprint(PLASMA, url_prefix='/samples/plasma')
    app.register_blueprint(PBMC, url_prefix='/samples/pbmc')
    app.register_blueprint(SERUM, url_prefix='/samples/serum')
    app.register_blueprint(VIRUS_CULTURE, url_prefix='/samples/virus_culture')
    app.register_blueprint(
        VIRUS_ISOLATION,
        url_prefix='/samples/virus_isolation')
    app.register_blueprint(FREEZER, url_prefix='/freezer/')
    app.register_blueprint(ROOM, url_prefix='/room/')
    app.register_blueprint(BOX, url_prefix='/box/')
    return app

