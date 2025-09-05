from . import _location, _requests

from ._location import bp as location_bp
from ._requests import bp as requests_bp

__all__ = ["location_bp", "requests_bp"]
