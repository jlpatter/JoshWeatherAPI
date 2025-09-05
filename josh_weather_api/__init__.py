import os

from flask import Flask
from flask_caching import Cache

from josh_weather_api.models import db

# Placing this here as per Flasks' pattern: https://flask.palletsprojects.com/en/stable/patterns/packages/

cache = Cache(config={"CACHE_TYPE": "SimpleCache"})


def create_app(db_uri=os.environ.get("DATABASE_URL")):
    app = Flask(__name__)
    config = {
        "SQLALCHEMY_DATABASE_URI": db_uri,
        "DEBUG": True,
        "CACHE_TYPE": "SimpleCache",
        "CACHE_DEFAULT_TIMEOUT": 300,
    }
    app.config.from_mapping(config)

    cache.init_app(app)
    db.init_app(app)

    from josh_weather_api.api import location_bp, requests_bp

    app.register_blueprint(location_bp)
    app.register_blueprint(requests_bp)

    with app.app_context():
        db.create_all()

    return app
