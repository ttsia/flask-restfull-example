from .base import Config


class DevelopConfig(Config):
    DEBUG = True
    SECRET_KEY = "70c7d757fe48a6635bf61d8fe9236a6ad572c562d1178fbc96"
    JWT_SECRET_KEY = "jwt-key"