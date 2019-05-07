from flask_restful import Resource
from flask import request, Response
from bson.json_util import dumps
from database import interface


class Item(Resource):
    """
    Shows a single item and lets you delete/update a item.
    """
    def get(self, item_id):
        response = interface.get_item(item_id)
        return Response(dumps(response), mimetype='application/json')

    def delete(self, item_id):
        response = interface.delete_item(item_id)
        return Response(response, status=204, mimetype='application/json')

    def put(self, item_id):
        item_data = request.get_json()
        response = interface.update_item(item_id, item_data)
        return Response(dumps(response), mimetype='application/json')


class ItemList(Resource):
    """
    Shows a list of all items, and lets you POST to add new items.
    """
    def get(self):
        response = interface.get_all_items()
        return Response(dumps(response), mimetype='application/json')
    
    def post(self):
        item_data = request.get_json()
        response = interface.create_item(item_data)
        return Response(dumps(response), status=201, mimetype='application/json')