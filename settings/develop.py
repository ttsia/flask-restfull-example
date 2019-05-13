"""
Developer env configuration
"""
from .base import Config


class DevelopConfig(Config):
    """
    Development configuration
    """
    DEBUG = True
