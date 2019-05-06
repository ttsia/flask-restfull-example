import os
from settings import config


config_name = os.environ.get('FLASK_ENV', 'develop')
current_config = config[config_name]