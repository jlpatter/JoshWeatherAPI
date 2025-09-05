from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


class Requests(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    status_code: Mapped[int] = mapped_column(db.Integer)

    def __repr__(self):
        return f"<Request ({self.id})>"
