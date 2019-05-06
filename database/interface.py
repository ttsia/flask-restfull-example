from . import get_client

CLIENT = get_client()
ITEMS_DB = CLIENT.items


def get_items():
    items = ITEMS_DB.items.find({})
    return items

def create_item(item_data):
    item = ITEMS_DB.items.insert_one(item_data)
    return item