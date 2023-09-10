from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from main_page.models import Product
from .models import ShoppingCart
from django.db.models import Sum, ExpressionWrapper, F, DecimalField


def cart_view(request):
    cart_items = ShoppingCart.objects.filter(user=request.user)
    total_price = cart_items.aggregate(
        total_price=Sum(ExpressionWrapper(F('price') * F('quantity'),
                                          output_field=DecimalField())))
    return render(request, 'shopping_cart/shopping_cart.html',
                  {'cart_items': cart_items,
                   'total_price': total_price['total_price']})


@login_required
def add_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = ShoppingCart.objects.get_or_create(product=product,
                                                            price=product.price,
                                                            img=product.img,
                                                            user=request.user)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('main_page:index')


@login_required
def remove_item(request, product_id):
    item = get_object_or_404(ShoppingCart, id=product_id, user=request.user)
    if request.method == 'GET':
        item.delete()
    return redirect('cart')


@login_required
def update_cart(request):
    if request.method == "POST":
        item_id = request.POST['item_id']
        new_quantity = int(request.POST['quantity'])
        cart_item = ShoppingCart.objects.get(id=item_id)
        cart_item.quantity = new_quantity
        cart_item.save()
        return redirect('cart')