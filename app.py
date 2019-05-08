from api.users.urls import user_blueprint
from api.items.urls import items_blueprint
from web.common.urls import common_blueprint
from flask import Flask
from settings import current_config

from flask_jwt_extended import JWTManager


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)

    # set the absolute path to the static folder
    app.static_folder = app.config.get('STATIC_DIR')

    # TODO replace all blueprint registration on separate file

    # users app views
    app.register_blueprint(user_blueprint)

    # templates app views
    app.register_blueprint(common_blueprint)

    # items app views
    app.register_blueprint(items_blueprint)

    # jwt initialization
    jwt = JWTManager(app)
    blacklist = set()

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in blacklist

    return app


APP = create_app(current_config)
