from flask import request, jsonify
from app.models.service_request import ServiceRequest
from app.models.mechanic import Mechanic
from app import db

# Create Service Request
def create_request():
    data = request.get_json()

    request_obj = ServiceRequest(
        user_id=data['user_id'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        issue=data['issue'],
        status="pending"
    )

    db.session.add(request_obj)
    db.session.commit()

    return jsonify({
        "message": "Service request created",
        "request_id": request_obj.id
    }), 201


# Get All Requests
def get_requests():
    requests = ServiceRequest.query.all()

    result = []
    for req in requests:
        result.append({
            "id": req.id,
            "user_id": req.user_id,
            "issue": req.issue,
            "status": req.status
        })

    return jsonify(result)


# Assign Mechanic
def assign_mechanic(request_id):
    data = request.get_json()
    mechanic_id = data['mechanic_id']

    req = ServiceRequest.query.get(request_id)
    mech = Mechanic.query.get(mechanic_id)

    if not req or not mech:
        return jsonify({"message": "Invalid request or mechanic"}), 404

    req.mechanic_id = mechanic_id
    req.status = "assigned"

    db.session.commit()

    return jsonify({"message": "Mechanic assigned successfully"})


# Update Request Status
def update_status(request_id):
    req = ServiceRequest.query.get(request_id)

    if not req:
        return jsonify({"message": "Request not found"}), 404

    data = request.get_json()
    req.status = data['status']

    db.session.commit()

    return jsonify({"message": "Status updated"})