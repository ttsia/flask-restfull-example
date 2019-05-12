import os

from settings.test import TestConfig
from settings.develop import DevelopConfig

config = {
    'development': DevelopConfig,
    'test': TestConfig,
}

config_name = os.environ.get('FLASK_ENV', 'development')
current_config = config[config_name]
