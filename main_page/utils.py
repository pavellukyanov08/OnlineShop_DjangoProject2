from .models import Product
from django.db.models import Q


def search_products(request):
    search_query = request.GET.get('search_query') \
        if request.GET.get('search_query') else ''

    products = Product.objects.filter(name__iexact=search_query)

    return products