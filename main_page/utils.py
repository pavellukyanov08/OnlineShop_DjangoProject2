from .models import Product
from django.db.models import Q


def search_products(request):
    search_query = request.GET.get('search_query') \
        if request.GET.get('search_query') else ''

    products = Product.objects.distinct().filter(Q(name__icontains=search_query))

    return products, search_query
