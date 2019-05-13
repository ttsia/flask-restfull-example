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
from flask import Response, current_app
from flask.views import MethodView
from api.metrics.utils import generate_report
from settings.basic_auth import BASIC_AUTH


class MetricsView(MethodView):
    """
    /metrics url handler
    """
    @BASIC_AUTH.required
    def get(self):
        # pylint: disable=R0201
        """
        GET /metrics
        """

        # NOTE! can take a few seconds
        generate_report()

        report = open(os.path.join(
            current_app.static_folder,
            current_app.config.get('PYLINT_SETTINGS').get('report_directory_name'),
            current_app.config.get('PYLINT_SETTINGS').get('report_file_name')))

        return Response(report.read(), mimetype='text/plain')
