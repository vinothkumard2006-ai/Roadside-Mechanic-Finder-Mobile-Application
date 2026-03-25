# request_routes.py

from flask import Blueprint, request, jsonify
from app.models import ServiceRequest
from config import db

request_bp = Blueprint('request_bp', __name__)

# Create Service Request
@request_bp.route('/create', methods=['POST'])
def create_request():
    data = request.get_json()

    request_obj = ServiceRequest(
        user_id=data['user_id'],
        issue_description=data['issue_description'],
        latitude=data['latitude'],
        longitude=data['longitude']
    )

    db.session.add(request_obj)
    db.session.commit()

    return jsonify({"message": "Request created"}), 201


# Get All Requests
@request_bp.route('/', methods=['GET'])
def get_requests():
    requests = ServiceRequest.query.all()

    return jsonify([
        {
            "id": r.id,
            "status": r.status,
            "issue": r.issue_description
        }
        for r in requests
    ])