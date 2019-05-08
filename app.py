from api.metrics.urls import metrics_blueprint
from api.users.urls import user_blueprint
from api.items.urls import items_blueprint
from web_apps.common.urls import common_blueprint
from flask import Flask
from settings import current_config

from flask_jwt_extended import JWTManager

APP = Flask(__name__)
APP.config.from_object(current_config)

# set the absolute path to the static folder
APP.static_folder = APP.config.get('STATIC_DIR')

# TODO replace all blueprint registration on separate file

# users app views
APP.register_blueprint(user_blueprint)

# templates app views
APP.register_blueprint(common_blueprint)

# items app views
APP.register_blueprint(items_blueprint)

# metrics app views
APP.register_blueprint(metrics_blueprint)

# jwt initialization
jwt = JWTManager(APP)
blacklist = set()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist
