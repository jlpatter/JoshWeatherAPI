import json
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, backref


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class BaseModel:
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.id})>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Request(db.Model, BaseModel):
    __tablename__ = "requests"

    request_url: Mapped[str] = mapped_column(db.String(100))
    status_code: Mapped[int] = mapped_column(db.Integer, nullable=True)
    requested_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now())

    def to_json(self):
        # I know there's probably a cleaner more abstract way to do this, but I'm going with this for now.
        return json.dumps({
            "request_url": self.request_url,
            "status_code": self.status_code,
            "requested_at": str(self.requested_at),
        })


class RequestPublicAPIRequest(db.Model, BaseModel):
    __tablename__ = "request_public_api_requests"

    request_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("requests.id"))
    request = db.relationship("Request")

    request_url: Mapped[str] = mapped_column(db.String(100))
    status_code: Mapped[int] = mapped_column(db.Integer)

    def to_json(self):
        return json.dumps({
            "request": self.request.to_json(),
            "request_url": self.request_url,
            "status_code": self.status_code,
        })
