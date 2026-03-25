def send_notification(user, message):
    """
    Simulated notification (extend with Twilio / Firebase later)
    """
    print(f"Notification to {user.name}: {message}")
    return True


def notify_mechanic(mechanic, request_details):
    message = f"New service request at location {request_details['location']}"
    return send_notification(mechanic, message)


def notify_user(user, status):
    message = f"Your request status: {status}"
    return send_notification(user, message)