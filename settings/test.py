from .base import Config


class TestConfig(Config):
    DEBUG = True
    TEST_DB_NAME = 'test'
