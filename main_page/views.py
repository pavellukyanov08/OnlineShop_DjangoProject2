from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, ReviewForm
from .models import *
from django.utils import timezone


def products_list(request, category_slug=None, product_availability=None):
    curr_time = timezone.now()

    menu = Menu.objects.all()
    categories = Category.objects.all()
    availabilities = ProductAvailability.objects.all()
    products = Product.objects.all()

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

    return render(request, 'main_page/index.html', {'menu': menu,
                                                    'category': category,
                                                    'categories': categories,
                                                    'availability': availability,
                                                    'availabilities': availabilities,
                                                    'products': products,
                                                    'curr_time': curr_time})


def add_product(request):
    menu = Menu.objects.all()
    if request.method == 'GET':
        return render(request, 'main_page/add_product.html', {'form': ProductForm(), 'menu': menu})
    else:
        try:
            form = ProductForm(request.POST, request.FILES)
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('main_page:index')
        except ValueError:
            return render(request, 'main_page/add_product.html',
                          {'form': ProductForm(),
                           'error': 'Переданы неверные данные', 'menu': menu})


def product_detail(request, prod_id, slug):
    menu = Menu.objects.all()
    product = get_object_or_404(Product, id=prod_id, slug=slug)
    form_prod = ProductForm(instance=product)
    form_review = ReviewForm()

    if request.method == 'GET':
        if request.user.is_staff or request.user.is_superuser:
            return render(request, 'main_page/edit_prod.html', {'product': product, 'form_prod': form_prod, 'menu': menu})
        else:
            return render(request, 'main_page/view_prod.html', {'product': product, 'form_review': form_review, 'menu': menu})
    else:
        try:
            if form_prod:
                form_prod = ProductForm(request.POST, instance=product)
                form_prod.save()
                return redirect('main_page:index')
            elif form_review:
                form_review = ReviewForm(request.POST)
                review = form_review.save(commit=False)
                review.product = product
                review.reviewer = request.user.profile
                review.save()
                product.get_vote_count()

                messages.success(request, 'Ваш отзыв успешно сохранен')
                return redirect('product_detail', id=prod_id, slug=slug)
        except ValueError:
            return render(request, 'main_page/view_prod.html',
                          {'form_prod': form_prod,
                           'form_review': form_review,
                           'error': 'Неверные данные!'})


def delete_prod(request, prod_id):
    product = get_object_or_404(Product, id=prod_id)
    if request.method == 'POST':
        product.delete()
        return redirect('main_page:index')
