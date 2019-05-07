import os
from .develop import DevelopConfig

config = {
    'develop': DevelopConfig,
}

config_name = os.environ.get('FLASK_ENV', 'develop')
current_config = config[config_name]
