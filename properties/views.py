# properties/views.py
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties  # import the new utility function

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()  # get cached or DB queryset
    data = list(properties.values())    # convert QuerySet to list of dicts
    return JsonResponse({"data": data})
   