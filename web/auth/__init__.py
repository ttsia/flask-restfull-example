from flask import g, session

from database import users as users_db
from urls import AUTH_BLUEPRINT


@AUTH_BLUEPRINT.before_app_request
def load_logged_in_user():
    """
    Get user by user id from session and load to app context.
    """
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = users_db.get_user_by_id(user_id)[0]