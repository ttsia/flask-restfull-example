# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: urls
# Created: 2019-05-06
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

from flask import Blueprint
from flask_restful import Api

from api.users.views import UsersView, UsersLoginView, UserLogout

user_blueprint = Blueprint('users', __name__, url_prefix='/users')
user_urls = Api(user_blueprint)

# url schema
user_urls.add_resource(UsersView, '/')
user_urls.add_resource(UsersLoginView, '/login')
user_urls.add_resource(UserLogout, '/logout')