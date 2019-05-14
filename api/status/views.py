# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: views
# Created: 2019-05-14
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
from flask import Response
from flask_restful import Resource
import datetime
from bson.json_util import dumps


class StatusView(Resource):
    """
    Status check
    """

    def get(self):
        """
        Get status
        """
        response = {
            'local time': str(datetime.datetime.utcnow())
        }
        return Response(dumps(response), mimetype='application/json')