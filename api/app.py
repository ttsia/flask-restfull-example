from flask import Flask
from flask_restful import Api
from api.common import views as common_views

APP = Flask(__name__)
API = Api(APP)

# common app views
API.add_resource(
    common_views.Index,
    '/'
)

# users app views
