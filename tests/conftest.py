import pytest

from app import create_app

from settings import current_config


@pytest.fixture
def app():
    # important step in tests.__init__.py
    # is loading .env variables
    # and setting FLASK_ENV to 'test'
    app = create_app(current_config)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
