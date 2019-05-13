"""
Items endpoints handling
"""
from flask_restful import Resource
from flask import request, Response
from bson.json_util import dumps
from database import items


class Item(Resource):
    """
    Shows a single item and lets you delete/update a item.
    """

    def get(self, item_id):
        """
        Get item by id
        """
        response = items.get_item(item_id)
        try:
            return Response(dumps(response), mimetype='application/json')
        except Exception as ex:
            response = {
                "error": str(ex)
            }
            return Response(dumps(response), status=400, mimetype='application/json')

    def delete(self, item_id):
        """
        Delete item by id
        """
        items.delete_item(item_id)
        try:
            return Response(status=204)
        except Exception as ex:
            response = {
                "error": str(ex)
            }
            return Response(dumps(response), status=400, mimetype='application/json')

    def put(self, item_id):
        """
        Update item by id
        """
        item_data = request.get_json()
        response = items.update_item(item_id, item_data)
        try:
            return Response(dumps(response), mimetype='application/json')
        except Exception as ex:
            response = {
                "error": str(ex)
            }
            return Response(dumps(response), status=400, mimetype='application/json')


class ItemList(Resource):
    """
    Shows a list of all items, and lets you POST to add new items.
    """

    def get(self):
        """
        Get items list
        """
        # pylint: disable=R0201
        response = items.get_all_items()
        return Response(dumps(response), mimetype='application/json')

    def post(self):
        """
        Create new item
        """
        item_data = request.get_json()
        response = items.create_item(item_data)
        return Response(dumps(response), status=201, mimetype='application/json')
