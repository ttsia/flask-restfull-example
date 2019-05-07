import os


class Config(object):
    DEBUG = False

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
