from flask import render_template, flash, redirect, url_for, request
from biological_samples_database import APP, bcrypt, db
from flask_login import (
    login_user,
    logout_user,
    current_user,
    login_required
)
from .forms import CreateAdminForm, DeleteUserForm, RegistrationForm, LoginForm
from .model.user import User


@APP.route("/", methods=['GET','POST'])
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
    return render_template("dashboard.html", user=current_user, form=form, form2=form2)

@APP.route("/people/edit/<userid>", methods=['GET','POST'])
def edit_user(userid):
    user = User.query.filter_by(id=userid).first()
    form = CreateAdminForm()
    del_user_form = DeleteUserForm()
    if form.is_submitted():
        if form.submit.data:
            user.gid = int(form.group.data)
            db.session.commit()
            flash(f'{user.username} now has role {user.groupName()}', 'info')
            return redirect(url_for('people'))
        if del_user_form.delete.data and current_user.gid == 1:
            if user != current_user:
                flash(f'{user.username} deleted', 'danger')
                db.session.delete(user)
                db.session.commit()
            else:
                flash(f'Cannot Delete Self', 'danger')
            return redirect(url_for('people'))


    return render_template(
            'people_edit.html',
            user=user,
            form=form,
            del_user_form = del_user_form,
            title="People")


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
    people = User.query.all()
    return render_template("people.html", title="People", people=people)


@APP.route('/samples')
@login_required
def samples():
    # 10x10
    sample_10 = list(range(1,101))

    # 9x9
    sample_9 = list(range(1,82))

    # wax standard
    sample_s = list(range(1,221))

    # wax 5ml
    sample_5ml = list(range(1,113))

    # wax large
    sample_l = list(range(1,241))
    return render_template("samples.html", title="Samples", samples=sample_9, sample_box_id = "9")

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
        login_user(new_user)

        flash(f'Welcome {current_user}', 'success')
        return redirect(url_for('home'))

    return render_template("registration.html", form=form, title="Register")

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

    return render_template("login.html", form=form, title="Login")

@APP.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))