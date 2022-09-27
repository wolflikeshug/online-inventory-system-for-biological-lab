from flask import render_template, flash, redirect, url_for, Blueprint
from .authentication import guest_required
from flask_bcrypt import Bcrypt


from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

#Authentication Decorators
#from .authentication import adminrequired, staffrequired, phdrequired, studentrequired, guestrequired, current_user

from .database import db
from .forms import CreateAdminForm, DeleteUserForm, RegistrationForm, LoginForm
from .model.user import User

bcrypt = Bcrypt()

MAIN = Blueprint(
    '',
    __name__,
    template_folder='templates'
)


@MAIN.route("/", methods=['GET','POST'])
def home():
    form = CreateAdminForm()
    form2 = DeleteUserForm.new()
    if form.is_submitted():
        if form.submit.data:
            current_user.gid = int(form.group.data)
            db.session.commit()
            flash(f'{current_user.username} now has role {current_user.groupName()}', 'info')

            return redirect(url_for('home'))

        if form2.delete.data and current_user.gid == 1:
            del_user = User.query.filter_by(id=int(form2.deluser.data)).first()
            if del_user and del_user != current_user:
                flash(f'{del_user.username} deleted', 'info')
                db.session.delete(del_user)
                db.session.commit()
            else:
                flash(f'Cannot Delete Self', 'danger')
            return redirect(url_for('home'))
    return render_template("dashboard.html", user=current_user, form=form, form2=form2, title="Dashboard")


@MAIN.route('/samples')
@login_required
def samples():
    # 10x10
    sample_10 = list(range(1,101))

    # 9x9
    sample_9 = list(range(1,30)) + list(range(33,38)) + list(range(50,82))

    # wax standard
    sample_s = list(range(1,221))

    # wax 5ml
    sample_5ml = list(range(1,113))

    # wax large
    sample_l = list(range(1,241))
    return render_template("samplez.html", title="Samples", samples=sample_9, sample_box_id = "9")

@MAIN.route('/register', methods=['GET','POST'])
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
        login_user(new_user)

        flash(f'Welcome {current_user}', 'success')
        return redirect(url_for('home'))

    return render_template("registration.html", form=form, title="Register")

@MAIN.route('/login', methods=['GET','POST'])
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

    return render_template("login.html", form=form, title="Login")

@MAIN.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@MAIN.route("/overview")
@guest_required
def overview():
    return render_template("overview.html")

@MAIN.route("/example")
@guest_required
def example():
    return render_template("examples.html")