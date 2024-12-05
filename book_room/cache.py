from django.core.cache import cache

_24_HOURS = 60 * 60 * 24


class CacheManager:

    def set(self, key, value, timeout):
        cache.set(key, value, timeout)

    def get(self, key):
        return cache.get(key)

    def clear_cache(self, cache_key):
        cache.delete(cache_key)
