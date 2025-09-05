import json

import requests
from flask import Flask, request

from flaskr.models import db, Requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./base_db.db"
db.init_app(app)

with app.app_context():
    db.create_all()


def check_status_code(resp):
    if resp.status_code != 200:
        return (
            f"HTTP Status 500: Received unexpected status from {resp.request.url}, status was {resp.status_code}",
            500,
        )
    return None


@app.route("/")
def weather_at_location():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    if lat is None or lon is None:
        return (
            "HTTP Status 400: Please specify the 'lat' and 'lon' query parameters on this endpoint. "
            "E.g. '/?lat=12.3456&lon=-78.9012'",
            400,
        )

    # TODO: Do other lat/lon validation checks here!

    # Get the 'point' information so we can get the forecast later
    resp = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
    # I'm just a fan of the walrus operator, had to find some way to include it :)
    if error := check_status_code(resp) is not None:
        return error
    resp_json = json.loads(resp.text)

    # Get the forecast at this particular location
    resp = requests.get(resp_json["properties"]["forecast"])
    if error := check_status_code(resp) is not None:
        return error
    resp_json = json.loads(resp.text)

    # Filter results by forecast for today.
    result = [
        p
        for p in resp_json["properties"]["periods"]
        if p["name"] in ("Today", "Tonight")
    ]

    request_instance = Requests(status_code=200)
    db.session.add(request_instance)
    db.session.commit()

    print(db.session.query(Requests).all())

    return result


if __name__ == "__main__":
    app.run()
