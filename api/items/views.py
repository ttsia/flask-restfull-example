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
        ---
        tags:
          - items api
        parameters:
          - in: path
            name: item_id
            required: true
            description: The ID of the item
            type: string
        responses:
          200:
            description: The item data
            schema:
              id: Item
              properties:
                title:
                  type: string
                text:
                  type: string
                _id:
                  type: object
                  properties:
                    $oid:
                      type: string
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
        ---
        tags:
          - items api
        parameters:
          - in: path
            name: item_id
            required: true
            description: The ID of the item
            type: string
        responses:
          204:
            description: Item deleted
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
        ---
        tags:
          - items api
        parameters:
          - in: body
            name: body
            schema:
              $ref: '#/definitions/Item'
          - in: path
            name: item_id
            required: true
            description: The ID of the item
            type: string
        responses:
          201:
            description: The item has been updated
            schema:
              $ref: '#/definitions/Item'
        """
        item_data = request.get_json()
        response = items.update_item(item_id, item_data)
        try:
            return Response(dumps(response), status=201, mimetype='application/json')
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
        ---
        tags:
          - items api
        responses:
          200:
            description: The item data list
            schema:
              id: Items
              type: array
              items:
                $ref: '#/definitions/Item'
        """
        response = items.get_all_items()
        return Response(dumps(response), mimetype='application/json')

    def post(self):
        """
        Create new item
        ---
        tags:
          - items api
        parameters:
          - in: body
            name: body
            schema:
              $ref: '#/definitions/Item'
        responses:
          201:
            description: The item has been created
            schema:
              $ref: '#/definitions/Item'
        """
        item_data = request.get_json()
        response = items.create_item(item_data)
        return Response(dumps(response), status=201, mimetype='application/json')
