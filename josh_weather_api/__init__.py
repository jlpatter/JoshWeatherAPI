import os

from flask import Flask
from flask_caching import Cache

from josh_weather_api.models import db

# Placing this here as per Flasks' pattern: https://flask.palletsprojects.com/en/stable/patterns/packages/

app = Flask(__name__)
config = {
    "SQLALCHEMY_DATABASE_URI": os.environ.get("DATABASE_URL"),
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
}
app.config.from_mapping(config)

cache = Cache(app)
db.init_app(app)

from josh_weather_api import api

with app.app_context():
    db.create_all()
