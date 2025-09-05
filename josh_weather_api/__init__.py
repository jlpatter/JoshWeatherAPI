from flask import Flask

from josh_weather_api.models import db

# Placing this here as per Flasks' pattern: https://flask.palletsprojects.com/en/stable/patterns/packages/

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./base_db.db"
db.init_app(app)

from josh_weather_api import api

with app.app_context():
    db.create_all()
