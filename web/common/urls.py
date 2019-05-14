"""
Common web app urls
"""
from flask import Blueprint

from . import views

COMMON_BLUEPRINT = Blueprint('common', __name__, static_folder='static', template_folder='templates')

COMMON_BLUEPRINT.add_url_rule(
    '/', view_func=views.RenderTemplateView.as_view('index', template_name='base.html')
)
