import pytest
from src.models.metal import Metal

def test_metal_valid():
    """A metal with a valid name should be created with an empty price list."""
    metal = Metal(name="gold")
    assert metal.name == "gold"
    assert metal.prices == []

def test_metal_invalid_name():
    """Empty metal names should raise a ValueError."""
    with pytest.raises(ValueError):
        Metal(name="")

def test_metal_prices_must_be_price_objects():
    """Prices must be a list of Price instances."""
    with pytest.raises(ValueError):
        Metal(name="gold", prices=["not a price"])