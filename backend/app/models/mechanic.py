# mechanic.py

from datetime import datetime
from app.config.db_config import db

class Mechanic(db.Model):
    __tablename__ = 'mechanics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)

    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    is_available = db.Column(db.Boolean, default=True)
    rating = db.Column(db.Float, default=0.0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    service_requests = db.relationship('ServiceRequest', backref='mechanic', lazy=True)

    def __repr__(self):
        return f"<Mechanic {self.name}>"