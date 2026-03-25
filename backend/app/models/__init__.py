# models/__init__.py

from .user import User
from .mechanic import Mechanic
from .service_request import ServiceRequest
from .review import Review
from .payment import Payment
__all__ = ['User','Mechanic','ServiceRequest','Review','Payment']
