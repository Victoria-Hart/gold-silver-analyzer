"""
Represents a transaction involving a metal at a given point in time.

A transaction corresponds to a user action (e.g. buying or selling a metal),
and is used as input for analysis such as profit/loss calculations.
"""

from datetime import date, datetime
from typing import Union
from .price import SUPPORTED_CURRENCIES

class Transaction:
    def __init__(
            self,
            metal: str,
            timestamp: Union[date, datetime],
            quantity: float,
            price_per_unit: float,
            currency: str,
    ) -> None:
        if not metal or not metal.strip():
            raise ValueError("Metal name must be a non-empty string")
        
        if not isinstance(timestamp, (date, datetime)):
            raise ValueError("Date must be a datetime.date or datetime.datetime instance")
        
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        
        if price_per_unit <= 0:
            raise ValueError("Price per unit must be greater than 0")
        
        if currency not in SUPPORTED_CURRENCIES:
            raise ValueError(f"Currency must be one of {', '.join(SUPPORTED_CURRENCIES)}")
        
        self.metal = metal
        self.timestamp = timestamp
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.currency = currency