# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: urls
# Created: 2019-05-08
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
from flask import Blueprint
from flask_restful import Api
from api.metrics.views import MetricsView


METRICS_BLUEPRINT = Blueprint('metrics', __name__)
METRICS_URLS = Api(METRICS_BLUEPRINT)

# url schema
METRICS_URLS.add_resource(MetricsView, '/metrics')
