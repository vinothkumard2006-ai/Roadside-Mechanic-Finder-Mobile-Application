# payment_routes.py

from flask import Blueprint, request, jsonify
from app.models import Payment
from app.config.db_config import db

payment_bp = Blueprint('payment_bp', __name__)

# Create Payment
@payment_bp.route('/pay', methods=['POST'])
def make_payment():
    data = request.get_json()

    payment = Payment(
        user_id=data['user_id'],
        request_id=data['request_id'],
        amount=data['amount'],
        payment_method=data.get('payment_method', 'Cash')
    )

    db.session.add(payment)
    db.session.commit()

    return jsonify({"message": "Payment successful"}), 201