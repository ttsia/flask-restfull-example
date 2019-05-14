"""
Base configuration setup
"""
import os
import string
import random
import datetime
from .secret import SECRET_KEY


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = '{}/{}'.format(BASE_DIR, 'static')


def ensure_secret_key():
    """Checks that secret.py exists in settings dir.
    If not, creates one with a random generated SECRET_KEY setting.
    """

    secret_path = os.path.join(BASE_DIR, 'settings', 'secret.py')
    if not os.path.exists(secret_path):
        secret_key = ''.join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(16)
        )
        with open(secret_path, 'w') as secret_file:
            secret_file.write('SECRET_KEY = \'' + secret_key + '\'\n')

ensure_secret_key()


class Config(object):
    """
    Base configuration
    """
    DEBUG = False

    BASE_DIR = BASE_DIR
    STATIC_DIR = STATIC_DIR

    SECRET_KEY = SECRET_KEY

    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=5)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    MONGO_DATABASES = {
        "app": {
            "username": os.environ.get('MONGO_USER'),
            "password": os.environ.get('MONGO_PASSWORD'),
            "port": 27017,
            "host": 'mongodb+srv://{}:{}@{}/'.format(
                os.environ.get('MONGO_USER'),
                os.environ.get('MONGO_PASSWORD'),
                os.environ.get('MONGO_HOST'),
            ),
        }
    }

    """
    PYLINT SETTINGS.
    Include files to be checked with full path as <file.py>
    Include modules to be checked with full path as <module/.>
    """
    PYLINT_SETTINGS = {
        "include": ['api/.', 'database/.', 'settings/.', 'web/.', 'app.py'],
        "report_directory_name": "data",
        "report_file_name": "report.txt",
        "config_directory_name": "settings",
        "config_file_name": "pylintrc"
    }

    """
    Basic Auth Credentials
    """
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')
