"""
Represents a metal and its price history.

This model groups price observations under a single metal name (gold, silver).
It contains no business logic beyond basic validation.
"""

from typing import List, Optional
from .price import Price


class Metal:
    def __init__(
            self,
            name: str,
            prices: Optional[List[Price]] = None,
    ) -> None:
        if not name or not name.strip():
            raise ValueError("Metal name must be a non-empty string")
        
        if prices is None:
            prices = []

        if not isinstance(prices, list):
            raise ValueError("Prices must be provided as a list")
        
        for price in prices:
            if not isinstance(price, Price):
                raise ValueError("All items in prices must be Price instances")
            
        self.name = name
        self.prices = prices