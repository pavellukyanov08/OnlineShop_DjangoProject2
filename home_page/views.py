from django.shortcuts import render
from main_page.models import Menu


def home_page(request):
    menu = Menu.objects.all()

    cart_prods_counter = request.user.shoppingcart_set.all()
    favourite_prods_counter = request.user.favourite_set.all()
    compare_prods_counter = request.user.compare_set.all()

    return render(request, 'home_page/home_page.html',
                  {'menu': menu,
                   'cart_prods_counter': cart_prods_counter,
                   'favourite_prods_counter': favourite_prods_counter,
                   'compare_prods_counter': compare_prods_counter,
                   })
