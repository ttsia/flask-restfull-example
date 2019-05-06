# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: views
# Created: 2019-05-06
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

from flask import request
from flask_restful import Resource


class UsersView(Resource):

    def get(self):
        data = {
            'method': request.method
        }
        return data

    def post(self):
        data = {
            'method': request.method
        }
        return data