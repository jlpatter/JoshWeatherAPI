from flask import request
from sqlalchemy import desc

from josh_weather_api import app
from josh_weather_api.models import Request


@app.route("/requests")
def requests():
    limit = request.args.get("limit", default=500)

    result = []
    for r in Request.query.order_by(desc(Request.requested_at)).limit(limit).all():
        result.append(r.to_dict())

    return result
