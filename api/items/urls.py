"""
Item urls
"""
from .views import ItemList, Item

ITEM_URLS = [
    ('/items', ItemList.as_view('items')),
    ('/items/<item_id>', Item.as_view('item'))
]
