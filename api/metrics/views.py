# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: views
# Created: 2019-05-08
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
"""
GET /metrics url for pylint report online getting
"""
import os
from flask import Response
from flask.views import MethodView
from api.metrics.utils import generate_report


class MetricsView(MethodView):
    """
    /metrics url handler
    """

    def get(self):
        """
        GET /metrics
        """
        from app import APP

        # NOTE! can take a few seconds
        generate_report()

        report = open(os.path.join(
            APP.static_folder,
            APP.config.get('PYLINT_SETTINGS').get('report_directory_name'),
            APP.config.get('PYLINT_SETTINGS').get('report_file_name')))
        return Response(report.read(), mimetype='text/plain')
