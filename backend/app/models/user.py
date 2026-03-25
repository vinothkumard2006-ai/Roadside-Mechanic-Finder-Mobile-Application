# user.py

from datetime import datetime
from app.config.db_config import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    service_requests = db.relationship('ServiceRequest', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"