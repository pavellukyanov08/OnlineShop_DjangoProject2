from django.shortcuts import render
from main_page.models import Menu
from shopping_cart.models import ShoppingCart


def about(request):
    menu = Menu.objects.all()

    cart_prods_counter = request.user.shoppingcart_set.all()
    favourite_prods_counter = request.user.favourite_set.all()
    compare_prods_counter = request.user.compare_set.all()

    return render(request, 'about/about.html', {
        'menu': menu,
        'cart_prods_counter': cart_prods_counter,
        'favourite_prods_counter': favourite_prods_counter,
        'compare_prods_counter': compare_prods_counter,
    })
