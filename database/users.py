from bson.errors import InvalidId
from bson.objectid import ObjectId
from . import get_client

CLIENT = get_client()
USERS_DB = CLIENT.users


def get_all_users():
    """
    :return list of users
    """
    response = USERS_DB.users.find()
    return list(response)


def get_user_by_id(user_id):
    """
    :return single user
    """
    try:
        response = USERS_DB.users.find({"_id": ObjectId(user_id)})
        return response
    except InvalidId as ex:
        return ex


def get_user_by_username(user_username):
    """
    :return single user
    """
    try:
        response = USERS_DB.users.find({"username": user_username})
        return list(response)
    except Exception as ex:
        return ex


def create_user(user_data):
    """
    :param user_data
    :type dict
    :return user_id
    """
    response = USERS_DB.users.insert_one(user_data)
    return response.inserted_id
