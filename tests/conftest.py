import pytest

from josh_weather_api import create_app, db


@pytest.fixture()
def app():
    orig_app = create_app("sqlite:///./test_db.db")
    orig_app.config.update(
        {
            "TESTING": True,
        }
    )

    yield orig_app

    with orig_app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
