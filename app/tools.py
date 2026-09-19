def get_payment(payment_id):
    return {
        "payment_id": payment_id,
        "status": "COMPLETED",
        "amount": "100 USD"
    }


def create_payment(amount):
    return {
        "payment_id": "P1001",
        "status": "CREATED",
        "amount": amount
    }


def refund_payment(payment_id):
    return {
        "payment_id": payment_id,
        "status": "REFUNDED"
    }


def get_customer(customer_id):
    return {
        "customer_id": customer_id,
        "name": "John",
        "status": "ACTIVE"
    }