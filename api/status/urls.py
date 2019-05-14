# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: urls
# Created: 2019-05-14
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

from flask import Blueprint
from flask_lazyviews import LazyViews
from api.status.views import StatusView

status_blueprint = Blueprint('status', __name__)
views = LazyViews(status_blueprint)

views.add('/status', StatusView.as_view('status'))