"""
Biological Samples Database.



"""

# Standard Imports
import os

# Flask Imports
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, current_user, login_required


# Blueprint Imports
from .cell_line import CELL_LINE
from .freezer import FREEZER
from .box import BOX

# Database Imports
from .database import engine, IRPD_PATH, create_new_session

# Flask Package and-SQLAlchemy link to Database 
APP = Flask(__name__)
login_man = LoginManager(APP)
bcrypt = Bcrypt(APP)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../biological_samples.sqlite'
db = SQLAlchemy(APP)


# Models and Forms
from .model import storage, Base
from .model.user import User
from .forms import RegistrationForm, LoginForm



@APP.route("/")
def home():
    return render_template("dashboard.html", user=current_user)


@APP.route('/rooms')
@login_required
def rooms():
    return render_template("rooms.html")


@APP.route('/inventory')
@login_required
def inventory():
    return render_template("inventory.html")


@APP.route('/people')
@login_required
def people():
    return render_template("people.html")


@APP.route('/samples')
@login_required
def samples():
    return render_template("samples.html")

@APP.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated and current_user.gid <= 6:
        return redirect(url_for('home'))
    form =  RegistrationForm()
    if form.validate_on_submit():

        hash_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        new_user = User( 
                    username    =   form.username.data
                    ,email      =   form.email.data
                    ,first      =   form.first.data
                    ,last       =   form.last.data
                    ,password   =   hash_pwd
                    ,gid        =   6                       )

        db.session.add(new_user)
        db.session.commit()

        flash(f'Account: {form.username.data} created', 'success')
        return redirect(url_for('home'))

    return render_template("registration.html", form=form)

@APP.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form =  LoginForm()
    if form.is_submitted():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember= form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Incorrect credentials', 'danger')

    return render_template("login.html", form=form)

@APP.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

def initialise_sqlite_database():
    """Instantiate the SQLite database if it does not exist"""

    if not os.path.exists(IRPD_PATH):
        Base.metadata.create_all(engine, checkfirst=True)

        with create_new_session() as session:

            unknown_user = User( 
                    username    =   "UNKNOWN"
                    ,email      =   "UNKNOWN"
                    ,first      =   "UNKNOWN"
                    ,last       =   "UNKNOWN"
                    ,password   =   "UNKNOWN"
                    ,gid    =   9999    )

            session.add(
                unknown_user
            )
            session.flush

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
