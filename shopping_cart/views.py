from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from main_page.models import Product, Menu
from .models import ShoppingCart
from django.db.models import Sum, ExpressionWrapper, F, DecimalField


@login_required
def cart_view(request):
    menu = Menu.objects.all()
    cart_items = ShoppingCart.objects.filter(user=request.user)
    cart_prods_counter = request.user.shoppingcart_set.all()
    favourite_prods_counter = request.user.favourite_set.all()
    compare_prods_counter = request.user.compare_set.all()
    total_price = cart_items.aggregate(
        total_price=Sum(ExpressionWrapper(F('price') * F('quantity'),
                                          output_field=DecimalField())))
    return render(request, 'shopping_cart/shopping_cart.html',
                  {'menu': menu,
                   'cart_items': cart_items,
                   'cart_prods_counter': cart_prods_counter,
                   'favourite_prods_counter': favourite_prods_counter,
                   'compare_prods_counter': compare_prods_counter,
                   'total_price': total_price['total_price']})


@login_required
def add_item(request, product_id):
    name = get_object_or_404(Product, id=product_id)
    cart_item, added = ShoppingCart.objects.get_or_create(name=name,
                                                          price=name.price,
                                                          img=name.img,
                                                          user=request.user)
    if not added:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('main_page:index')


@login_required
def remove_item(request, product_id):
    product = get_object_or_404(ShoppingCart, id=product_id, user=request.user)
    if request.method == 'GET':
        product.delete()
    return redirect('cart:cart')


@login_required
def update_cart(request):
    if request.method == "POST":
        item_id = request.POST['item_id']
        new_quantity = int(request.POST['quantity'])
        cart_item = ShoppingCart.objects.get(id=item_id)
        cart_item.quantity = new_quantity
        cart_item.save()
        return redirect('cart:cart')
