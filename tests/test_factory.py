from app import create_app


def test_config():
    class Test(object):
        TESTING = True
    assert not create_app().testing
    assert create_app(Test).testing

