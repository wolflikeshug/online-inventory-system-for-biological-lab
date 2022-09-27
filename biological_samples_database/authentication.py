from flask_login import current_user
from flask import flash, redirect, request, current_app
from functools import wraps 


def guest_required(func):
    gid=5
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated and current_user.gid <= gid:
            pass
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif current_user.gid > gid:
            flash('Permission Denied', 'danger')
            return redirect(request.referrer)

        # flask 1.x compatibility
        # current_app.ensure_sync is only available in Flask >= 2.0
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view

def student_required(func):
    gid=4
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated and current_user.gid <= gid:
            pass
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif current_user.gid > gid:
            flash('Permission Denied', 'danger')
            return redirect(request.referrer)

        # flask 1.x compatibility
        # current_app.ensure_sync is only available in Flask >= 2.0
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view

def phd_required(func):
    gid=3
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated and current_user.gid <= gid:
            pass
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif current_user.gid > gid:
            flash('Permission Denied', 'danger')
            return redirect(request.referrer)

        # flask 1.x compatibility
        # current_app.ensure_sync is only available in Flask >= 2.0
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view

def staff_required(func):
    gid=2
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated and current_user.gid <= gid:
            pass
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif current_user.gid > gid:
            flash('Permission Denied', 'danger')
            return redirect(request.referrer)

        # flask 1.x compatibility
        # current_app.ensure_sync is only available in Flask >= 2.0
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view

def admin_required(func):
    gid=1
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated and current_user.gid <= gid:
            pass
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif current_user.gid > gid:
            flash('Permission Denied', 'danger')
            return redirect(request.referrer)

        # flask 1.x compatibility
        # current_app.ensure_sync is only available in Flask >= 2.0
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view
