from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, Category
from django.utils import timezone


def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    curr_time = timezone.now()
    products = Product.objects.filter(available=True)
    # функционал сортировки
    sort_by = request.GET.get('sort_by')

    if sort_by:
        products = Product.objects.order_by(sort_by).all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'main_page/index.html', {'category': category,
                                                    'categories': categories,
                                                    'products': products,
                                                    'curr_time': curr_time})


def add_product(request):
    if request.method == 'GET':
        return render(request, 'main_page/add_product.html', {'form': ProductForm()})
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
                           'error': 'Переданы неверные данные'})


def product_detail(request, prod_id, slug):
    product = get_object_or_404(Product, id=prod_id, slug=slug, available=True)
    form = ProductForm(instance=product)
    if request.method == 'GET':
        return render(request, 'main_page/product_detail.html', {'product': product, 'form': form})
    else:
        try:
            form = ProductForm(request.POST, instance=product)
            form.save()
            return redirect('main_page:index')
        except ValueError:
            return render(request, 'main_page/product_detail.html',
                          {'form': form,
                           'error': 'Неверные данные!'})


def delete_prod(request, prod_id):
    product = get_object_or_404(Product, id=prod_id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
