"""
Represents a price observation for a metal at a single point in time.

This model is used across the project:
- Created by the API layer
- Used by analysis logic
- Visualized in plots

It contains no business logic beyond basic validation.
"""

from datetime import date, datetime
from typing import Union


SUPPORTED_CURRENCIES = {"SEK", "EUR", "USD"}


class Price:
    def __init__(
        self,
        metal: str,
        timestamp: Union[date, datetime],
        price: float,
        currency: str,
    ) -> None:
        if not metal or not metal.strip():
            raise ValueError("Metal name must be a non-empty string")

        if not isinstance(timestamp, (date, datetime)):
            raise ValueError(
                "Date must be a datetime.date or datetime.datetime instance"
            )

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        if currency not in SUPPORTED_CURRENCIES:
            raise ValueError(
                f"Currency must be one of {', '.join(SUPPORTED_CURRENCIES)}"
            )

        self.metal = metal
        self.date = timestamp
        self.price = price
        self.currency = currency