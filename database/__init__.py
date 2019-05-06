import os
from pymongo import MongoClient
from settings import config

def get_client():
    """
    Configuration method to return mongodb client
    """
    db_uri = 'mongodb+srv://{}:{}@{}/'.format(
        os.environ.get('MONGO_USER'),
        os.environ.get('MONGO_PASSWORD'),
        os.environ.get('MONGO_HOST'),
    )
    client = MongoClient(db_uri)
    return client
