from . import views
from flask import Blueprint

common_blueprint = Blueprint('common', __name__, template_folder='templates')

common_blueprint.add_url_rule('/', view_func=views.RenderTemplateView.as_view('/', template_name='index.html'))
