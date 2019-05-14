# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: urls
# Created: 2019-05-06
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
"""
Users urls
"""
from api.users.views import UsersView, UsersLoginView, UserLogout, UserView, TokenRefresh

USER_URLS = [
    ('/users', UsersView.as_view('users')),
    ('/users/login', UsersLoginView.as_view('users/login')),
    ('/users/logout', UserLogout.as_view('users/logout')),
    ('/user', UserView.as_view('user')),
    ('/user/refresh', TokenRefresh.as_view('user/refresh'))
]
