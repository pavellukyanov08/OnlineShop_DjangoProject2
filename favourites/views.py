from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from main_page.models import Product
from .models import Favourite


@login_required
def get_favourites_products(request):
    favourites_item = Favourite.objects.filter(user=request.user)
    return render(request, 'favourites/favourites.html', {'favourites_item': favourites_item})


@login_required
def add_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favourite_item, added = Favourite.objects.get_or_create(product=product,
                                                            description=product.description,
                                                            img=product.img,
                                                            price=product.price,
                                                            user=request.user)
    if not added:
        favourite_item.save()
    return redirect('main_page:index')


@login_required
def remove_item(request, product_id):
    item = get_object_or_404(Favourite, id=product_id, user=request.user)
    if request.method == 'GET':
        item.delete()
    return redirect('favourites:all_products')
