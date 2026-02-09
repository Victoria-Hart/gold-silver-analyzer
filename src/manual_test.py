from api.metals_client import MetalsClient
from api.cache_manager import CacheManager

def main():
    cache = CacheManager()
    API_KEY = "DUMMY_KEY"
    client = MetalsClient(api_key=API_KEY, cache=cache)

    try:
        gold_price = client.get_price("XAU")
        print(f"Gold price: {gold_price} USD")
    except Exception as e:
        print(f"Could not fetch gold price: {e}")

    try:
        silver_price = client.get_price("XAG")
        print(f"Silver price: {silver_price} USD")
    except Exception as e:
        print(f"Could not fetch silver price: {e}")

if __name__ == "__main__":
    main()
from api.metals_client import MetalsClient
from api.cache_manager import CacheManager

def main():
    # Skapa instanser
    client = MetalsClient(api_key="DUMMY_KEY")
    cache = CacheManager()

    # Fake priser för test
    gold_price = 2000.0
    silver_price = 25.0

    # Skriv ut
    print(f"Gold price: {gold_price} USD")
    print(f"Silver price: {silver_price} USD")

if __name__ == "__main__":
    main()
