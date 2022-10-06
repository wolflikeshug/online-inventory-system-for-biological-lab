"""
User

"""


# Flask
from flask import Blueprint, render_template, flash, redirect, url_for

# Local Imports
from ..database import db
from ..forms import CreateAdminForm, DeleteUserForm
from ..model.user import User
from flask_login import current_user
from ..authentication import admin_required, guest_required, student_required
USERS = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)


@USERS.route("/", methods=['GET','POST'])
@student_required
def home():
    return redirect(url_for('users.people'))

@USERS.route("/people/edit/<userid>", methods=['GET','POST'])
@admin_required
def edit_user(userid):
    user = User.query.filter_by(id=userid).first()
    form = CreateAdminForm()
    del_user_form = DeleteUserForm()
    if form.is_submitted():
        if form.submit.data:
            user.gid = int(form.group.data)
            db.session.commit()
            flash(f'{user.username} now has role {user.groupName()}', 'info')
            return redirect(url_for('users.people'))
        if del_user_form.delete.data and current_user.gid == 1:
            if user != current_user:
                flash(f'{user.username} deleted', 'danger')
                db.session.delete(user)
                db.session.commit()
            else:
                flash(f'Cannot Delete Self', 'danger')
            return redirect(url_for('users.people'))


    return render_template(
            'people_edit.html',
            user=user,
            form=form,
            del_user_form = del_user_form,
            title="People")

@USERS.route("/people/info/<userid>", methods=['GET','POST'])
@student_required
def info_user(userid):
        user = User.query.filter_by(id=userid).first()
        return render_template('people_info.html', user=user)


@USERS.route('/people')
@student_required
def people():
    people = User.query.all()
    return render_template("people.html", title="People", people=people)

