# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: urls
# Created: 2019-05-06
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>

from flask import Blueprint
from flask_restful import Api
from api.users.views import UsersView, UsersLoginView, UserLogout, UserView, TokenRefresh

USERS_BLUEPRINT = Blueprint('users', __name__)
USERS_URLS = Api(USERS_BLUEPRINT)

# url schema
USERS_URLS.add_resource(UsersView, '/users')
USERS_URLS.add_resource(UsersLoginView, '/users/login')
USERS_URLS.add_resource(UserLogout, '/users/logout')
USERS_URLS.add_resource(UserView, '/user')
USERS_URLS.add_resource(TokenRefresh, '/user/refresh')
