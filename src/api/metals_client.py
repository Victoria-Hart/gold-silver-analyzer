import requests
from api.cache_manager import CacheManager

class MetalsClient:
    def __init__(self, api_key, cache=None):
        self.api_key = api_key
        self.base_url = "https://metals-api.com/api"
        self.cache = cache
    
    def get_price(self, metal_code):
        """ämtar priset på metallen (symbol: XAU för guld, XAG för silver)
        Använder cache om giltig"""
        cache_key = f"price_{metal_code}"
        if self.cache and self.cache.is_cache_valid(cache_key):
            cached = self.cache.load(cache_key)
            return cached
        url = f"{self.base_url}/latest?access_key={self.api_key}&symbols={metal_code}"
        try:
            response = requests.get(url)
            data = response.json()
            price = data.get('rates', {}).get(metal_code)
            if self.cache and price:
                self.cache.save(cache_key, price)
            
            return price
        except Exception as e:
            print(f"Error fetching price: {e}")
            return None