from django.shortcuts import render
from main_page.models import Menu


def home_page(request):
    menu = Menu.objects.all()

    cart_prods = request.user.shoppingcart_set.all()
    return render(request, 'home_page/home.html',
                  {'menu': menu,
                   'cart_prods': cart_prods})
