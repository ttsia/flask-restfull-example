# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: urls
# Created: 2019-05-10
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
"""
Blueprint registration for full 'api' module
"""
from api.items.urls import ITEMS_BLUEPRINT
from api.metrics.urls import METRICS_BLUEPRINT
from api.users.urls import USERS_BLUEPRINT
from web.common.urls import common_blueprint


def register_blueprints(app):
    """
    register urls for 'api' module
    :param app: current Flask app
    :return:
    """
    # users app views
    app.register_blueprint(USERS_BLUEPRINT)

    # templates app views
    app.register_blueprint(common_blueprint)

    # items app views
    app.register_blueprint(ITEMS_BLUEPRINT)

    # metrics app views
    app.register_blueprint(METRICS_BLUEPRINT)

    return True
