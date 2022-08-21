"""
Biological Samples Database.



"""

# Standard Imports
import os

# Flask Imports
from flask import Flask, render_template

# Blueprint Imports
from .cell_line import CELL_LINE

# App Imports
from .database import engine, SQLITE_PATH
from .model import Base


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


@APP.route('/freezers')
def freezers():
    return render_template("freezers.html")


@APP.route('/samples')
def samples():
    return render_template("samples.html")


def initialise_sqlite_database():
    """Instantiate the SQLite database if it does not exist"""

    if not os.path.exists(SQLITE_PATH):
        Base.metadata.create_all(engine)


def initialise_app():
    '''Setup and initialise logging and other shared components
    of the Flask app'''

    app = APP
    initialise_sqlite_database()
    app.register_blueprint(CELL_LINE, url_prefix='/samples/cell_line')
    return app
