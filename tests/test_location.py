from unittest.mock import patch

import requests

from tests.utils import FakeResponse


def test_weather_at_location_missing_params(client):
    # Ideally this would be in a class with a `setUp` method, but we'll do this for now instead.

    # Test missing query parameters
    resp = client.get("/")
    assert resp.status_code == 400
    assert resp.text == (
        "HTTP Status 400: Please specify the 'lat' and 'lon' query parameters on this endpoint. "
        "E.g. '/?lat=12.3456&lon=-78.9012'"
    )


@patch("requests.get")
def test_weather_at_location_happy_path(mock_get, client):
    # Mock public API calls
    mock_get.return_value = FakeResponse()

    resp = client.get("/?lat=12.3456&lon=-78.9012")
    assert resp.status_code == 200
    assert requests.get.call_count == 2
    assert "someForecast" in resp.text
    assert "rain" in resp.text
