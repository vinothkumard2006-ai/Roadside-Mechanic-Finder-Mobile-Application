from app.models.service_request import ServiceRequest
from app.services.notification_service import notify_mechanic

def create_service_request(user, mechanic, issue, location, db):
    """
    Create new service request
    """
    new_request = ServiceRequest(
        user_id=user.id,
        mechanic_id=mechanic.id,
        issue=issue,
        location=location,
        status="pending"
    )

    db.session.add(new_request)
    db.session.commit()

    # notify mechanic
    notify_mechanic(mechanic, {"location": location})

    return new_request


def update_request_status(request, status, db):
    """
    Update request status (accepted, completed, cancelled)
    """
    request.status = status
    db.session.commit()

    return request