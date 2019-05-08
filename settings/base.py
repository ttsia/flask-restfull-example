import os


class Config(object):
    DEBUG = False

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_DIR = '{}/{}'.format(BASE_DIR, 'static')

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
        "include": ['api/.', 'database/.', 'settings/.', 'web_apps/.', 'app.py'],
        "report_directory_name": "data",
        "report_file_name": "report.txt"
    }