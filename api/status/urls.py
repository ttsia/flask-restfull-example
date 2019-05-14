# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: urls
# Created: 2019-05-14
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
"""
Status urls
"""
from api.status.views import StatusView

STATUS_URLS = [
    ('/status', StatusView.as_view('status'))
]
