from .user_routes import user_bp
from .mechanic_routes import mechanic_bp
from .request_routes import request_bp
from .review_routes import review_bp
from .payment_routes import payment_bp

__all__ = [
    "user_bp",
    "mechanic_bp",
    "request_bp",
    "review_bp",
    "payment_bp"
]