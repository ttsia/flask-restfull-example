"""
Common web app urls
"""
from flask import Blueprint

from . import views

AUTH_BLUEPRINT = Blueprint('auth', __name__, template_folder='templates')

AUTH_BLUEPRINT.add_url_rule('/login', view_func=views.WebLoginView.as_view('login'))
AUTH_BLUEPRINT.add_url_rule('/logout', view_func=views.WebLogoutView.as_view('logout'))


