# properties/utils.py
from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Try to get properties from cache
    properties = cache.get('all_properties')
    
    if not properties:
        # If not in cache, fetch from database
        properties = Property.objects.all()
        # Store in Redis for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
    
    return properties