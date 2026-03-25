from flask import Flask
from config import db

from app.routes.user_routes import user_bp
from app.routes.mechanic_routes import mechanic_bp
from app.routes.request_routes import request_bp
from app.routes.review_routes import review_bp
from app.routes.payment_routes import payment_bp


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(mechanic_bp, url_prefix='/mechanics')
    app.register_blueprint(request_bp, url_prefix='/requests')
    app.register_blueprint(review_bp, url_prefix='/reviews')
    app.register_blueprint(payment_bp, url_prefix='/payments')

    return app