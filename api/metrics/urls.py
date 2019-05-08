# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: urls
# Created: 2019-05-08
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
from api.metrics.views import MetricsView

from flask import Blueprint
from flask_restful import Api


metrics_blueprint = Blueprint('metrics', __name__)
metrics_urls = Api(metrics_blueprint)

# url schema
metrics_urls.add_resource(MetricsView, '/metrics')