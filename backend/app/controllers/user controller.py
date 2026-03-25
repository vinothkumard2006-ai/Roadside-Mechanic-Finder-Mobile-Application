from flask import request, jsonify
from app.models.user import User
from app import db

# Create User
def create_user():
    data = request.get_json()

    user = User(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        password=data['password']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


# Get All Users
def get_users():
    users = User.query.all()

    result = []
    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone
        })

    return jsonify(result)


# Get Single User
def get_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone
    })


# Delete User
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"})