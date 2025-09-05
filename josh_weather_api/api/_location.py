import json

import requests
from cachetools import cached, TTLCache
from flask import request

from josh_weather_api import app
from josh_weather_api.models import Request, RequestPublicAPIRequest
from josh_weather_api.utils import check_status_code, StatusCodeException


# Cache responses for 15 minutes
@cached(cache=TTLCache(maxsize=1024, ttl=900))
def _get_from_cache_or_api(url):
    return requests.get(url)


def _get_from_public_api(url, request_instance):
    resp = _get_from_cache_or_api(url)
    pub_api_req_instance = RequestPublicAPIRequest(
        request=request_instance, request_url=url, status_code=resp.status_code
    )
    pub_api_req_instance.save()
    check_status_code(resp)
    return json.loads(resp.text)


@app.route("/")
def weather_at_location():
    # TODO: Need to not use '.save()' and commit everything in 1 transaction!
    request_instance = Request(request_url=request.url)
    request_instance.save()
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    if lat is None or lon is None:
        request_instance.status_code = 400
        request_instance.save()
        return (
            "HTTP Status 400: Please specify the 'lat' and 'lon' query parameters on this endpoint. "
            "E.g. '/?lat=12.3456&lon=-78.9012'",
            400,
        )

    # TODO: Do other lat/lon validation checks here!

    try:
        # Get the 'point' information so we can get the forecast later
        resp_json = _get_from_public_api(
            f"https://api.weather.gov/points/{lat},{lon}", request_instance
        )

        # Get the forecast at this particular location
        resp_json = _get_from_public_api(
            resp_json["properties"]["forecast"], request_instance
        )
    except StatusCodeException as e:
        request_instance.status_code = 500
        request_instance.save()
        return f"HTTP Status 500: {e.message}", 500

    # Filter results by forecast for today.
    result = [
        p
        for p in resp_json["properties"]["periods"]
        if p["name"] in ("Today", "Tonight")
    ]

    request_instance.status_code = 200
    request_instance.save()

    return result
