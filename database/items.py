from bson.errors import InvalidId
from bson.objectid import ObjectId
from . import get_client

CLIENT = get_client()
ITEMS_DB = CLIENT.items


def get_all_items():
    """
    :return list of items
    """
    response = ITEMS_DB.items.find()
    return list(response)

def get_item(item_id):
    """
    :return single item
    """
    try:
        response = ITEMS_DB.items.find({"_id": ObjectId(item_id)})
        return response
    except InvalidId as ex:
        return ex

def create_item(item_data):
    """
    :param item_data
    :type dict
    :return item_id
    """
    response = ITEMS_DB.items.insert_one(item_data)
    return response.inserted_id

def update_item(item_id, item_data):
    """
    :param item_data
    :type dict
    :return bool
    """
    try:
        response = ITEMS_DB.items.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": item_data}
        )
        return response.acknowledged
    except InvalidId as ex:
        return ex

def delete_item(item_id):
    """
    :return bool
    """
    try:
        response = ITEMS_DB.items.delete_one({"_id": ObjectId(item_id)})
        return response.acknowledged
    except InvalidId as ex:
        return ex
