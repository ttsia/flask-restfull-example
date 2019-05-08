from .base import Config


class DevelopConfig(Config):
    DEBUG = True
    JWT_SECRET_KEY = "jwt-key"
    JWT_BLACKLIST_ENABLED = True
