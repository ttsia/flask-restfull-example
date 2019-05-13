"""
COMMON urls
"""
from flask import Blueprint
from . import views

COMMON_BLUEPRINT = Blueprint('common', __name__, template_folder='templates')

COMMON_BLUEPRINT.add_url_rule(
    '/', view_func=views.RenderTemplateView.as_view('/', template_name='index.html')
)
