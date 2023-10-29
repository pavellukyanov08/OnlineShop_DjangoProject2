from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from main_page.models import Product, Menu
from .models import Compare


@login_required
def get_all_products(request):
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
def add_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    compare_item, added = Compare.objects.get_or_create(product=product,
                                                        user=request.user)
    if not added:
        compare_item.save()
    return redirect('main_page:index')


@login_required
def remove_item(request, product_id):
    product = get_object_or_404(Compare, id=product_id, user=request.user)
    if request.method == 'GET':
        product.delete()
    return redirect('compare:all_compare')
