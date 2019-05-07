from .views import ItemList, Item
from flask import Blueprint
from flask_restful import Api


items_blueprint = Blueprint('items', __name__)
items_urls = Api(items_blueprint)

# url schema

items_urls.add_resource(ItemList, '/items')
items_urls.add_resource(Item, '/items/<item_id>')