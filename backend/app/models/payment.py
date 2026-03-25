# payment.py

from datetime import datetime
from config import db

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    request_id = db.Column(db.Integer, db.ForeignKey('service_requests.id'), nullable=False)

    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='pending')  # paid, failed

    payment_method = db.Column(db.String(50))  # UPI, Card, Cash

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Payment {self.amount}>"