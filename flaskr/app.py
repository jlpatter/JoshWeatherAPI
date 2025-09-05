from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def weather_at_location():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    if lat is None or lon is None:
        return "HTTP Status 400: Please specify the 'lat' and 'lon' query parameters on this endpoint. E.g. '/?lat=38.8648&lon=-94.6674'", 400
    return f"{lat}, {lon}"


if __name__ == '__main__':
    app.run()
