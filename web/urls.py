"""
Blueprint registration for full 'web' module
"""
from web.common.urls import COMMON_BLUEPRINT


def register_web_blueprints(app):
    """
    register urls for 'web' module
    :param app: current Flask app
    :return:
    """

    # metrics app views
    app.register_blueprint(COMMON_BLUEPRINT)
