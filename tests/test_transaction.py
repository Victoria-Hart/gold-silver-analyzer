import pytest
from datetime import date
from src.models.transaction import Transaction

def test_transaction_valid():
    """Valid transaction data should create a Transaction object."""
    tx = Transaction(
        metal="gold",
        timestamp=date.today(),
        quantity=2.0,
        price_per_unit=500.0,
        currency="SEK"
    )
    assert tx.quantity == 2.0

def test_transaction_invalid_quantity():
    """Transaction quantity must be greater than zero."""
    with pytest.raises(ValueError):
        Transaction(
            metal="gold",
            timestamp=date.today(),
            quantity=0,
            price_per_unit=500.0,
            currency="SEK"
        )

