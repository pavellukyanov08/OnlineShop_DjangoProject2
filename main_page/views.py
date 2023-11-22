from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, ReviewForm
from .models import *
from django.utils import timezone
from .utils import search_products
from favourites.models import Favourite
from prod_comparison.models import Compare


@login_required(login_url='login')
def products_list(request, category_slug=None, product_availability=None):
    curr_time = timezone.now()

    products, search_query = search_products(request)

    user = request.user

    favourite_prods = user.favourite_set.filter(user=user).values_list('product__id', flat=True)

    # compare_prods = user.compare_set.filter(user=user).values_list('product__id', flat=True)
    compare_prods = user.compare_set.filter(user=user).values_list('product_id', flat=True)
    print(compare_prods)

    menu = Menu.objects.all()
    categories = Category.objects.all()
    availabilities = ProductAvailability.objects.all()

    cart_prods_counter = user.shoppingcart_set.all()
    favourite_prods_counter = user.favourite_set.all()
    compare_prods_counter = user.compare_set.all()

    category, availability = None, None
    # функционал сортировки
    sort_by = request.GET.get('sort_by')

    if sort_by:
        products = Product.objects.order_by(sort_by).all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if product_availability:
        availability = get_object_or_404(ProductAvailability, availability_status=product_availability)
        products = products.filter(availability_status=availability)

    context = {'menu': menu,
               'search_query': search_query,
               'category': category,
               'categories': categories,
               'availability': availability,
               'availabilities': availabilities,
               'products': products,
               'favourite_prods': favourite_prods,
               'compare_prods': compare_prods,
               'cart_prods_counter': cart_prods_counter,
               'favourite_prods_counter': favourite_prods_counter,
               'compare_prods_counter': compare_prods_counter,
               'curr_time': curr_time}
    return render(request, 'main_page/index.html', context)


@login_required
def add_product(request):
    menu = Menu.objects.all()

    cart_prods_counter = request.user.shoppingcart_set.all()
    favourite_prods_counter = request.user.favourite_set.all()
    compare_prods_counter = request.user.compare_set.all()

    if request.method == 'GET':
        return render(request, 'main_page/add_product.html', {'form': ProductForm(), 'menu': menu,
                                                              'cart_prods_counter': cart_prods_counter,
                                                              'favourite_prods_counter': favourite_prods_counter,
                                                              'compare_prods_counter': compare_prods_counter, })
    else:
        try:
            form = ProductForm(request.POST, request.FILES)
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('main_page:index')
        except ValueError:

            context = {
                'form': ProductForm(),
                'error': 'Переданы неверные данные', 'menu': menu,
                'cart_prods_counter': cart_prods_counter,
                'favourite_prods_counter': favourite_prods_counter,
                'compare_prods_counter': compare_prods_counter
            }
            return render(request, 'main_page/add_product.html', context)


@login_required
def product_detail(request, prod_id, slug):
    menu = Menu.objects.all()
    product = Product.objects.get(id=prod_id, slug=slug)

    cart_prods_counter = request.user.shoppingcart_set.all()
    favourite_prods_counter = request.user.favourite_set.all()
    compare_prods_counter = request.user.compare_set.all()

    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'GET':
            form_prod = ProductForm(instance=product)

            context = {
                'menu': menu,
                'product': product,
                'form_prod': form_prod,
                'cart_prods_counter': cart_prods_counter,
                'favourite_prods_counter': favourite_prods_counter,
                'compare_prods_counter': compare_prods_counter
            }
            return render(request, 'main_page/edit_prod.html', context)
        else:
            try:
                form_prod = ProductForm(request.POST, instance=product)
                form_prod.save()

                return redirect('main_page:index')
            except ValueError:

                context = {
                    'product': product,
                    'menu': menu,
                    'cart_prods_counter': cart_prods_counter,
                    'favourite_prods_counter': favourite_prods_counter,
                    'compare_prods_counter': compare_prods_counter
                }
                return render(request, 'main_page/edit_prod.html', context)
    else:
        if request.method == 'GET':
            form_review = ReviewForm(request.GET)
            user_reviews = product.review_set.all()
            user_prof_data = request.user.profile

            context = {
                'product': product,
                'form_review': form_review,
                'menu': menu,
                'user_reviews': user_reviews,
                'user_prof_data': user_prof_data,
                'cart_prods_counter': cart_prods_counter,
                'favourite_prods_counter': favourite_prods_counter,
                'compare_prods_counter': compare_prods_counter
            }
            return render(request, 'main_page/view_prod.html', context)
        else:
            form_review = ReviewForm(request.POST)

            # try:
            review = form_review.save(commit=False)
            review.product = product
            review.owner = request.user.profile
            review.save()
            product.get_vote_count()
            messages.success(request, 'Ваш отзыв успешно сохранен')

            return redirect('main_page:product_detail', prod_id=product.id, slug=product.slug)
            # except IntegrityError:
    # return render(request, 'main_page/view_prod.html',
    #                           {'product': product,
    #                            'form_review': form_review,
    #                            'error': 'Неверные данные!'})


@login_required
def delete_prod(request, prod_id):
    product = get_object_or_404(Product, id=prod_id)
    if request.method == 'POST':
        product.delete()
        return redirect('main_page:index')
