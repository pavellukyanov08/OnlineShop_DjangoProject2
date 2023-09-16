from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from favourites.models import Favourite
from main_page.models import Product
from .models import Compare


def get_all_products(request):
    compare_items = Compare.objects.filter(user=request.user)
    return render(request, 'prod_compare/compare_prod.html', {'compare_items': compare_items})


@login_required
def add_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    compare_item, added = Compare.objects.get_or_create(product=product,
                                                        slug=product.slug,
                                                        img=product.img,
                                                        height=product.height,
                                                        weight=product.weight,
                                                        width=product.width,
                                                        price=product.price,
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
