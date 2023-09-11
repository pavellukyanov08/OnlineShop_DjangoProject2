from django.shortcuts import render, get_object_or_404, redirect
from main_page.models import Product
from .models import Favourite


def favourites_product(request):
    favourites_item = Favourite.objects.filter(user=request.user)
    return render(request, 'favourites/favourites.html', {'favourites_item': favourites_item})


def add_to_favourite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favourite_item, added = Favourite.objects.get_or_create(product=product,
                                                            description=product.description,
                                                            img=product.img,
                                                            price=product.price,
                                                            user=request.user)
    if not added:
        favourite_item.save()
    return redirect('main_page:index')
