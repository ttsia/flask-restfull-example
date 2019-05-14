"""
Common web app urls
"""
from flask import Blueprint, g, session

from database import users as users_db

from . import views

AUTH_BLUEPRINT = Blueprint('auth', __name__, template_folder='templates')

AUTH_BLUEPRINT.add_url_rule('/login', view_func=views.WebLoginView.as_view('login'))
AUTH_BLUEPRINT.add_url_rule('/logout', view_func=views.WebLogoutView.as_view('logout'))


@AUTH_BLUEPRINT.before_app_request
def load_logged_in_user():
    """
    Get user by user id from session and load to app context.
    """
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = users_db.get_user_by_id(user_id)[0]
