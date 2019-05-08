# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: views
# Created: 2019-05-08
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
from api.metrics.utils import generate_report
import os
from flask import Response
from flask.views import MethodView


class MetricsView(MethodView):

    def get(self):
        from app import APP

        # NOTE! can take a few seconds
        generate_report()

        f = open(os.path.join(
            APP.static_folder,
            APP.config.get('PYLINT_SETTINGS').get('report_directory_name'),
            APP.config.get('PYLINT_SETTINGS').get('report_file_name')))
        return Response(f.read(), mimetype='text/plain')
