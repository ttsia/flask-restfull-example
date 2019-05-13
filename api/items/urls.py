"""
Item urls
"""
from flask import Blueprint
from flask_restful import Api
from .views import ItemList, Item


ITEMS_BLUEPRINT = Blueprint('items', __name__)
ITEMS_URLS = Api(ITEMS_BLUEPRINT)

# url schema

ITEMS_URLS.add_resource(ItemList, '/items')
ITEMS_URLS.add_resource(Item, '/items/<item_id>')
