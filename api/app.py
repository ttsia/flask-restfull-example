from api.common.urls import common_blueprint
from api.users.urls import user_blueprint
from api.items.urls import items_blueprint
from flask import Flask
from settings import current_config


def create_app(config=None):
    config = config or {}

    app = Flask(__name__)
    app.config.from_object(config)

    # TODO replace all blueprint registration on separate file

    # users app views
    app.register_blueprint(user_blueprint)

    # main app views
    app.register_blueprint(common_blueprint)

    # items app views
    app.register_blueprint(items_blueprint)
    return app


APP = create_app(current_config)
