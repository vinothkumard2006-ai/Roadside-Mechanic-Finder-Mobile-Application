# user_routes.py

from flask import Blueprint, request, jsonify
from app.models import User
from app.config.db_config import db

user_bp = Blueprint('user_bp', __name__)

# Register User
@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    user = User(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        password=data['password']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


# Get All Users
@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()

    return jsonify([
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ])