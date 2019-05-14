from app import create_app
from settings.base import DEFAULT_SECRET_KEY


class TestConf(object):
    TESTING = True


def test_empty_config():
    app_without_conf = create_app()

    assert not app_without_conf.testing


def test_test_config():
    app_with_conf = create_app(TestConf)

    assert app_with_conf.testing


def test_app(app):
    assert app.env == 'test'
    assert app.config.get('JWT_SECRET_KEY') != DEFAULT_SECRET_KEY
