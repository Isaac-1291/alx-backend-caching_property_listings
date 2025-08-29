# properties/utils.py
from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    # Try to get properties from cache
    properties = cache.get('all_properties')
    
    if not properties:
        # If not in cache, fetch from database
        properties = Property.objects.all()
        # Store in Redis for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
    
    return properties


def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    Returns a dictionary with hits, misses, and hit_ratio.
    """
    redis_conn = get_redis_connection("default")  # uses your default Redis cache
    info = redis_conn.info()  # get Redis INFO dictionary

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else 0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio,
    }

    logger.info(f"Redis Cache Metrics: Hits={hits}, Misses={misses}, Hit Ratio={hit_ratio:.2f}")
    return metrics