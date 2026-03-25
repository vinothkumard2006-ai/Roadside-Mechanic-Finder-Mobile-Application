# mechanic_routes.py

from flask import Blueprint, request, jsonify
from app.models import Mechanic
from app.config.db_config import db

mechanic_bp = Blueprint('mechanic_bp', __name__)

# Add Mechanic
@mechanic_bp.route('/add', methods=['POST'])
def add_mechanic():
    data = request.get_json()

    mechanic = Mechanic(
        name=data['name'],
        phone=data['phone'],
        latitude=data.get('latitude'),
        longitude=data.get('longitude')
    )

    db.session.add(mechanic)
    db.session.commit()

    return jsonify({"message": "Mechanic added"}), 201


# Get Available Mechanics
@mechanic_bp.route('/', methods=['GET'])
def get_mechanics():
    mechanics = Mechanic.query.filter_by(is_available=True).all()

    return jsonify([
        {
            "id": m.id,
            "name": m.name,
            "phone": m.phone,
            "location": [m.latitude, m.longitude]
        }
        for m in mechanics
    ])