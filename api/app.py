from api.common.urls import common_blueprint
from api.users.urls import user_blueprint
from api.items.urls import items_blueprint
from flask import Flask
from settings import current_config

from flask_jwt_extended import JWTManager

APP = Flask(__name__)
APP.config.from_object(current_config)

# TODO replace all blueprint registration on separate file

# users app views
APP.register_blueprint(user_blueprint)

# main app views
APP.register_blueprint(common_blueprint)

# items app views
APP.register_blueprint(items_blueprint)

# jwt initialization
jwt = JWTManager(APP)

