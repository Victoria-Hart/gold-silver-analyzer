import pytest
from datetime import date
from src.models.price import Price

def test_price_valid():
    """Valid price data should create a Price object."""
    price = Price(
        metal="gold",
        timestamp=date.today(),
        price=1000.0,
        currency="SEK"
    )
    assert price.price == 1000.0

def test_price_invalid_negative_price():
    """Negative prices are not allowed."""
    with pytest.raises(ValueError):
        Price(
            metal="gold",
            timestamp=date.today(),
            price=-10.0,
            currency="SEK"
        )

def test_price_invalid_currency():
    """Unsupported currencies should raise a ValueError."""
    with pytest.raises(ValueError):
        Price(
            metal="gold",
            timestamp=date.today(),
            price=1000.0,
            currency="BTC"
        )