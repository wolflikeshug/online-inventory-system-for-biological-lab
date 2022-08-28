"""
Biological Samples Database.



"""

# Standard Imports
import os

# Flask Imports
from flask import Flask, render_template

# Blueprint Imports
from .cell_line import CELL_LINE
from .freezer import FREEZER

# App Imports
from .database import engine, IRPD_PATH, create_new_session
from .model import sample, storage, Base


APP = Flask(__name__)


@APP.route("/")
def home():
    return render_template("dashboard.html")


@APP.route('/rooms')
def rooms():
    return render_template("rooms.html")


@APP.route('/inventory')
def inventory():
    return render_template("inventory.html")


@APP.route('/people')
def people():
    return render_template("people.html")


@APP.route('/samples')
def samples():
    return render_template("samples.html")


def initialise_sqlite_database():
    """Instantiate the SQLite database if it does not exist"""

    if not os.path.exists(IRPD_PATH):
        Base.metadata.create_all(engine, checkfirst=True)

        with create_new_session() as session:

            unknown_building = storage.Building()
            unknown_building.name = 'UNKNOWN'
            session.add(
                unknown_building
            )
            
            unknown_freezer = storage.Freezer()
            unknown_freezer.name = 'UNKNOWN'
            unknown_freezer.building_id = unknown_building.id
            session.add(
                unknown_freezer
            )
            
            unknown_box = storage.Box()
            unknown_box.label = 'UNKNOWN'
            unknown_box.freezer_id = unknown_freezer.id
            session.add(
                unknown_box
            )

            session.commit()                


def initialise_app():
    '''Setup and initialise logging and other shared components
    of the Flask app'''

    app = APP
    app.secret_key = 'HUSHHUSHVERYSECRET'
    initialise_sqlite_database()
    app.register_blueprint(CELL_LINE, url_prefix='/samples/cell_line')
    app.register_blueprint(FREEZER, url_prefix='/freezer/')
    return app