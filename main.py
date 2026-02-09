import sys
from pathlib import Path
#SRC BEHÖVER SYNAS
sys.path.append(str(Path(__file__).parent / "src"))

from api.metals_client import MetalsClient
from api.cache_manager import CacheManager
from cli.commands import handle_command

def main():
    API_KEY = "demo
    cache = CacheManager(ttl_minutes=15)
    client = MetalsClient(api_key=API_KEY, cache=cache)
    handle_command(client)

if __name__ == "__main__":
    main()
