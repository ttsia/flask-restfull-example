import os

from settings.test import TestConfig
from settings.develop import DevelopConfig

config = {
    'develop': DevelopConfig,
    'test': TestConfig,
}

config_name = os.environ.get('FLASK_ENV', 'develop')
current_config = config[config_name]
