from flask import Flask
from flask_restful import Api
from api.common import views as common_views
from . import current_config

APP = Flask(__name__)
APP.config.from_object(current_config)

API = Api(APP)

# common app views
API.add_resource(
    common_views.Index,
    '/'
)

# test db connection
API.add_resource(
    common_views.Heartbeat,
    '/heartbeat'
)

# users app views
