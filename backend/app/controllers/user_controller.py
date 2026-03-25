from flask import jsonify

def get_users():
    return jsonify({"message": "Get all users"})

def create_user(data):
    return jsonify({"message": "User created", "data": data})