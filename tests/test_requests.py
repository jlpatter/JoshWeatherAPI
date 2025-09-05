import json
from unittest.mock import patch

from tests.utils import FakeResponse


@patch("requests.get")
def test_requests_happy_path(mock_get, client):
    # Mock public API calls
    mock_get.return_value = FakeResponse()

    resp = client.get("/?lat=12.3456&lon=-78.9012")
    assert resp.status_code == 200

    resp = client.get("/requests")
    resp_dict = json.loads(resp.text)
    del resp_dict[0]["requested_at"]
    assert resp_dict == [
        {
            "request_public_api_requests": [
                {
                    "request_url": "https://api.weather.gov/points/12.3456,-78.9012",
                    "status_code": 200,
                },
                {"request_url": "fake-url.com", "status_code": 200},
            ],
            "request_url": "http://localhost/?lat=12.3456&lon=-78.9012",
            "status_code": 200,
        }
    ]
