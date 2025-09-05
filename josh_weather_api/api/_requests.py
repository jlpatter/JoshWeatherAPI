from flask import request, Blueprint
from sqlalchemy import desc

from josh_weather_api.models import Request


bp = Blueprint("requests", __name__, url_prefix="/")


@bp.route("/requests")
def requests():
    limit = request.args.get("limit", default=500)

    result = []
    for r in Request.query.order_by(desc(Request.requested_at)).limit(limit).all():
        result.append(r.to_dict())

    return result
