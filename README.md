# Josh's Weather API

## Endpoint Usage

* There are 2 endpoints available at `/` and `/requests`.
* You can use `/` with `lat` and `lon` query parameters to get today's weather forecast (E.g. when running locally: `http://127.0.0.1:5000/?lat=39.120547&lon=-94.590472`).
* You can use `/requests` with the optional `limit` query parameter to get a list of the most recent requests in descending order (E.g. when running locally: `http://127.0.0.1:5000/requests?limit=3`)

## Developer Setup

1. Make sure you have "Docker" and "Docker Compose" installed and either have docker desktop running or a docker daemon.
2. Create a `.env` file in the root of the project and include the following env variables of your choosing: `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB`
3. Run `docker compose build`
4. Run `docker compose up`
5. You should be able to access the site from port `5000`.
