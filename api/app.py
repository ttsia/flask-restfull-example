from api.common.urls import common_blueprint
from api.users.urls import user_blueprint
from flask import Flask
from . import current_config

APP = Flask(__name__)
APP.config.from_object(current_config)

# TODO replace all blueprint registration on separate file

# users app views
APP.register_blueprint(user_blueprint)

# main app views
APP.register_blueprint(common_blueprint)