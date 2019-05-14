# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: urls
# Created: 2019-05-08
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
"""
Metrics urls
"""
from api.metrics.views import MetricsView

METRIC_URLS = [
    ('/metrics', MetricsView.as_view('metrics'))
]
