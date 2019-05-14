# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: urls
# Created: 2019-05-10
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
"""
Blueprint registration for full 'api' module
"""
from flask import Blueprint
from flask_lazyviews import LazyViews
from api.items.urls import ITEM_URLS
from api.users.urls import USER_URLS
from api.metrics.urls import METRIC_URLS
from api.status.urls import STATUS_URLS

API_BLUEPRINT = Blueprint('api', __name__)
VIEWS = LazyViews(API_BLUEPRINT)

# Add new urls
URLS = []
URLS.extend(ITEM_URLS)
URLS.extend(USER_URLS)
URLS.extend(METRIC_URLS)
URLS.extend(STATUS_URLS)

# load views
for url_name, view_name in URLS:
    VIEWS.add(url_name, view_name)
