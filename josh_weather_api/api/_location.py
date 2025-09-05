import json

import requests
from flask import request

from josh_weather_api import app
from josh_weather_api.models import Requests, db
from josh_weather_api.utils import check_status_code, StatusCodeException


def _get_from_public_api(url):
    resp = requests.get(url)
    check_status_code(resp)
    return json.loads(resp.text)


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

    try:
        # Get the 'point' information so we can get the forecast later
        resp_json = _get_from_public_api(f"https://api.weather.gov/points/{lat},{lon}")
        # Get the forecast at this particular location
        resp_json = _get_from_public_api(resp_json["properties"]["forecast"])
    except StatusCodeException as e:
        return f"HTTP Status 500: {e.message}", 500

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