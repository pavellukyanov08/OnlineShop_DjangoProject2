from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from main_page.models import Product, Menu
from .models import Favourite


@login_required
def get_favourite_products(request):
    menu = Menu.objects.all()
    user = request.user

    cart_prods_counter = user.shoppingcart_set.all()
    favourite_prods_counter = user.favourite_set.all()
    compare_prods_counter = user.compare_set.all()

    favourites_item = request.user.favourite_set.all()
    favourites_item = [item.product for item in favourites_item]

    return render(request, 'favourites/favourites.html', {
        'favourites_item': favourites_item,
        'menu': menu,
        'cart_prods_counter': cart_prods_counter,
        'favourite_prods_counter': favourite_prods_counter,
        'compare_prods_counter': compare_prods_counter,
    })


@login_required
def add_favourite_status(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)

    is_favourite = Favourite.objects.filter(product=product, user=request.user)

    if is_favourite:
        Favourite.objects.filter(user=user, product=product).delete()
    else:
        Favourite.objects.create(user=user, product=product)
    return redirect('main_page:index')


@login_required
def remove_favourite_status(request, product_id):
    fav_prods = Favourite.objects.filter(product_id=product_id).get(user_id=request.user.id)
    products = get_object_or_404(Favourite, id=fav_prods.id, user=request.user)
    if request.method == 'GET':
        products.delete()
    return redirect('favourites:all_products')
