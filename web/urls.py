"""
Blueprint registration for full 'web' module
"""
from web.common.urls import COMMON_BLUEPRINT
from web.auth.urls import AUTH_BLUEPRINT


def register_web_blueprints(app):
    """
    register urls for 'web' module
    :param app: current Flask app
    :return:
    """

    # common web app views
    app.register_blueprint(COMMON_BLUEPRINT)

    # auth web app views
    app.register_blueprint(AUTH_BLUEPRINT)
