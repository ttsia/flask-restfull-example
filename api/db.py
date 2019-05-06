from flask import current_app
from pymongo import MongoClient
from settings import config

def get_client():
    """
    Configuration method to return mongodb client
    """
    db_uri = current_app.config['MONGO_DATABASES']['app']['host']
    client = MongoClient(db_uri)
    return client
