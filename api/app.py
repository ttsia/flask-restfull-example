from api.users.urls import user_blueprint
from flask import Flask
from flask_restful import Api
from api.common import views as common_views

APP = Flask(__name__)
API = Api(APP)

APP.register_blueprint(user_blueprint)

# common app views
API.add_resource(
    common_views.Index,
    '/'
)