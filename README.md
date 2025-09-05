# Josh's Weather API

## Endpoint Usage

* There are 2 endpoints available at `/` and `/requests`.
* You can use `/` with `lat` and `lon` query parameters to get today's weather forecast (E.g. when running locally: `http://127.0.0.1:5000/?lat=39.120547&lon=-94.590472`).
* You can use `/requests` with the optional `limit` query parameter to get a list of the most recent requests in descending order (E.g. when running locally: `http://127.0.0.1:5000/requests?limit=3`)

## Developer Setup

1. Create a python virtualenv (E.g. `python -m .venv .`) and activate it (E.g. `source .venv/bin/activate`)
2. Install python requirements (E.g. `pip install -r requirements.txt`).
3. Make sure to set your `FLASK_APP` env variable (E.g. `export FLASK_APP=josh_weather_api.app`)
4. Run `flask run` to run the project locally.
