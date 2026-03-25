# review_routes.py

from flask import Blueprint, request, jsonify
from app.models import Review
from config import db

review_bp = Blueprint('review_bp', __name__)

# Add Review
@review_bp.route('/add', methods=['POST'])
def add_review():
    data = request.get_json()

    review = Review(
        user_id=data['user_id'],
        mechanic_id=data['mechanic_id'],
        rating=data['rating'],
        comment=data.get('comment')
    )

    db.session.add(review)
    db.session.commit()

    return jsonify({"message": "Review added"}), 201