from flask import request, jsonify
from app.models.mechanic import Mechanic
from app import db

# Add Mechanic
def add_mechanic():
    data = request.get_json()

    mechanic = Mechanic(
        name=data['name'],
        phone=data['phone'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        is_available=True
    )

    db.session.add(mechanic)
    db.session.commit()

    return jsonify({"message": "Mechanic added successfully"}), 201


# Get All Mechanics
def get_mechanics():
    mechanics = Mechanic.query.all()

    result = []
    for mech in mechanics:
        result.append({
            "id": mech.id,
            "name": mech.name,
            "phone": mech.phone,
            "location": {
                "lat": mech.latitude,
                "lng": mech.longitude
            },
            "available": mech.is_available
        })

    return jsonify(result)


# Update Availability
def update_availability(mechanic_id):
    mech = Mechanic.query.get(mechanic_id)

    if not mech:
        return jsonify({"message": "Mechanic not found"}), 404

    data = request.get_json()
    mech.is_available = data['is_available']

    db.session.commit()

    return jsonify({"message": "Availability updated"})