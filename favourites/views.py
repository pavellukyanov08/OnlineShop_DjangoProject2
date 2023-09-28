from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from main_page.models import Product, Menu
from .models import Favourite


@login_required
def get_favourites_products(request):
    menu = Menu.objects.all()
    favourites_item = Favourite.objects.filter(user=request.user)
    return render(request, 'favourites/favourites.html', {'favourites_item': favourites_item, 'menu': menu})


@login_required
def add_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favourite_item, added = Favourite.objects.get_or_create(product=product,
                                                            slug=product.slug,
                                                            description=product.description,
                                                            width=product.width,
                                                            height=product.height,
                                                            weight=product.weight,
                                                            img=product.img,
                                                            price=product.price,
                                                            user=request.user)
    if not added:
        favourite_item.save()
    return redirect('main_page:index')


@login_required
def remove_item(request, product_id):
    product = get_object_or_404(Favourite, id=product_id, user=request.user)
    if request.method == 'GET':
        product.delete()
    return redirect('favourites:all_products')
