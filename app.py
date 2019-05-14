"""
App creation
"""
from flask import Flask
from api.status.urls import status_blueprint
from settings import current_config
from settings.basic_auth import BASIC_AUTH
from settings.jwt_auth import JWT
from api.urls import register_api_blueprints
from web.urls import register_web_blueprints


def create_app(config=None):
    """
    :param config:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config)

    # set the absolute path to the static folder
    app.static_folder = app.config.get('STATIC_DIR')

    # blueprints registration
    register_api_blueprints(app)
    register_web_blueprints(app)

    app.register_blueprint(status_blueprint)

    # jwt initialization
    JWT.init_app(app)

    # basic auth initialization
    BASIC_AUTH.init_app(app)

    return app

APP = create_app(current_config)
