from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from main_page.models import Product, Menu
from .models import Compare


@login_required
def get_compare_products(request):
    menu = Menu.objects.all()

    cart_prods_counter = request.user.shoppingcart_set.all()
    favourite_prods_counter = request.user.favourite_set.all()
    compare_prods_counter = request.user.compare_set.all()

    compare_items = request.user.compare_set.all()
    compare_items = [item.product for item in compare_items]
    return render(request, 'prod_compare/compare_prod.html', {
        'compare_items': compare_items,
        'menu': menu,
        'cart_prods_counter': cart_prods_counter,
        'favourite_prods_counter': favourite_prods_counter,
        'compare_prods_counter': compare_prods_counter,
    })


@login_required
def add_compare_status(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    is_compare = Compare.objects.filter(product=product, user=request.user)

    if is_compare:
        Compare.objects.filter(user=user, product=product).delete()
    else:
        Compare.objects.create(user=user, product=product)
    return redirect('main_page:index')


@login_required
def remove_compare_status(request, product_id):
    fav_prods = Compare.objects.filter(product_id=product_id).get(user_id=request.user.id)
    products = get_object_or_404(Compare, id=fav_prods.id, user=request.user)
    if request.method == 'GET':
        products.delete()
    return redirect('compare:all_compare')
