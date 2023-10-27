from django.shortcuts import render
from main_page.models import Menu
from shopping_cart.models import ShoppingCart


def about(request):
    menu = Menu.objects.all()

    cart_prods = request.user.shoppingcart_set.all()
    return render(request, 'about/about.html', {'menu': menu, 'cart_prods': cart_prods})
