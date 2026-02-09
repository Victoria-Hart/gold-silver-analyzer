from pathlib import Path
import json
from datetime import datetime, timedelta


class CacheManager:
    def __init__(self, cache_dir: str = "data/cache", ttl_minutes: int = 10):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.ttl = timedelta(minutes=ttl_minutes)

    def _get_cache_file(self, key: str) -> Path:
        return self.cache_dir / f"{key}.json"

    def is_cache_valid(self, key: str) -> bool:
        cache_file = self._get_cache_file(key)
        if not cache_file.exists():
            return False

        with open(cache_file, "r", encoding="utf-8") as f:
            cached_data = json.load(f)

        timestamp = datetime.fromisoformat(cached_data["timestamp"])
        return datetime.utcnow() - timestamp < self.ttl

    def load(self, key: str):
        cache_file = self._get_cache_file(key)
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)["data"]

    def save(self, key: str, data):
        cache_file = self._get_cache_file(key)
        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "data": data
        }
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
