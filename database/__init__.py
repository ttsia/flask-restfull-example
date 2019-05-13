"""
Database initialization
"""
from pymongo import MongoClient
from settings import current_config


def get_client():
    """
    Configuration method to return mongodb client
    """
    db_uri = current_config.MONGO_DATABASES['app']['host']
    client = MongoClient(db_uri)
    return client
