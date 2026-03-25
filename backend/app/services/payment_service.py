def process_payment(user, amount):
    """
    Dummy payment (Integrate Razorpay / Stripe later)
    """
    print(f"Processing payment of ₹{amount} for {user.name}")
    return {
        "status": "success",
        "amount": amount
    }