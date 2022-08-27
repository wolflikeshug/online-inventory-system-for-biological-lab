# Standard Imports
import os

# Flask Imports
from flask import Flask, render_template

# Blueprint Imports
from .rooms import CELL_LINE

# App Imports
from .database import engine, SQLITE_PATH
from .model import Base

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('dashboard.html')

@app.route('/rooms')
def rooms():
    return render_template("rooms.html")

@app.route('/inventory')
def inventory():
    return render_template("inventory.html")

@app.route('/people')
def people():
    return render_template("people.html")

@app.route('/freezers')
def freezers():
    return render_template("freezers.html")

@app.route('/samples')
def samples():
    return render_template("samples.html")

# Temporary page to show Allison team forms/may use later
@app.route('/mockup')
def mockup():
    return render_template("mockup.html")

# <--- Simon's code ---
def initialise_sqlite_database():
    """Instantiate the SQLite database if it does not exist"""

    if not os.path.exists(SQLITE_PATH):
        Base.metadata.create_all(engine)


def initialise_app():
    '''Setup and initialise logging and other shared components
    of the Flask app'''

    app.secret_key = 'HUSHHUSHVERYSECRET'
    initialise_sqlite_database()
    app.register_blueprint(CELL_LINE, url_prefix='/samples/cell_line')
    return app
# --- Simon's code --->

if __name__ == "__main__":
    app.run(debug=True)