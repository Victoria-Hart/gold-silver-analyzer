import requests
from typing import Optional
from .cache_manager import CacheManager


class MetalsClient:
    BASE_URL = "https://metals-api.com/api/latest"  # Exempel-API, byt om ni har riktig

    def __init__(self, api_key: str, cache: Optional[CacheManager] = None):
        self.api_key = api_key
        self.cache = cache or CacheManager()

    def get_price(self, symbol: str) -> Optional[float]:
        """
        Hämtar priset på metallen (symbol: XAU för guld, XAG för silver)
        Använder cache om giltig
        """
        key = f"price_{symbol}"

        # Kolla cache först
        if self.cache.is_cache_valid(key):
            return self.cache.load(key)

        # Annars, hämta från API
        params = {
            "access_key": self.api_key,
            "base": "USD",
            "symbols": symbol
        }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            price = data.get("rates", {}).get(symbol)

            if price is not None:
                # Spara i cache
                self.cache.save(key, price)

            return price

        except Exception as e:
            print(f"Could not fetch {symbol} price: {e}")
            return None
