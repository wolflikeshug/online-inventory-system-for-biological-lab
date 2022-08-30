"""
Biological Samples Database.



"""

# Standard Imports
import os

# Flask Imports
from flask import Flask, render_template, flash, redirect, url_for
from flask_bcrypt import Bcrypt

# Blueprint Imports
from .cell_line import CELL_LINE
from .freezer import FREEZER
from .box import BOX

# App Imports
from .database import engine, IRPD_PATH, create_new_session
from .model import storage, Base
from .model.user import User
from .forms import RegistrationForm, LoginForm

APP = Flask(__name__)

bcrypt = Bcrypt(APP)

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

@APP.route('/register', methods=['GET','POST'])
def register():
    form =  RegistrationForm()
    if form.validate_on_submit():
        hash_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User( username=form.username.data
                    ,email  =   form.email.data
                    ,first  =   form.first.data
                    ,last   =   form.last.data
                    ,password = hash_pwd
                    ,gid    =   5   )
        with create_new_session().begin() as session:
            session.add(new_user)
            session.commit()
        flash(f'Account: {form.username.data} created', 'success')
        return redirect(url_for('home'))
    return render_template("registration.html", form=form)

@APP.route('/login', methods=['GET','POST'])
def login():
    form =  LoginForm()
    if form.is_submitted():
        if form.username.data == 'admin' and form.password.data =='password':
            return redirect(url_for('home'))
        else:
            flash('Incorrect credentials', 'danger')

    return render_template("login.html", form=form)

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
            session.flush()

            unknown_room = storage.Room()
            unknown_room.name = 'UNKNOWN'
            unknown_room.building_id = unknown_building.id
            session.add(
                unknown_room
            )
            session.flush()

            unknown_freezer = storage.Freezer()
            unknown_freezer.name = 'UNKNOWN'
            unknown_freezer.room_id = unknown_room.id
            session.add(
                unknown_freezer
            )
            session.flush()

            unknown_box = storage.Box()
            unknown_box.label = 'UNKNOWN'
            unknown_box.freezer_id = unknown_freezer.id
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
    app.register_blueprint(CELL_LINE, url_prefix='/samples/cell_line')
    app.register_blueprint(FREEZER, url_prefix='/freezer/')
    app.register_blueprint(BOX, url_prefix='/box/')
    return app
