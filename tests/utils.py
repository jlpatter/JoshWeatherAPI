import json


class FakeResponse:
    def __init__(self, status_code=200):
        self.status_code = status_code
        resp_text = {
            "properties": {
                "forecast": "fake-url.com",
                "periods": [
                    {
                        "name": "Today",
                        "someForecast": "It's going to rain today :(",
                    }
                ],
            },
        }
        self.text = json.dumps(resp_text)
