from app.agent import run_agent


def test_refund_payment():
    result = run_agent("I want to refund a payment", "P123")

    assert result["payment_id"] == "P123"
    assert result["status"] == "REFUNDED"


def test_get_payment():
    result = run_agent("I want payment details", "P123")

    assert result["payment_id"] == "P123"
    assert result["status"] == "COMPLETED"


def test_create_payment():
    result = run_agent("I want to create a payment", "500 USD")

    assert result["amount"] == "500 USD"
    assert result["status"] == "CREATED"


def test_missing_value():
    result = run_agent("I want to refund a payment")

    assert result == "Payment ID is required."