from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, Category


def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'main_page/index.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def sort_products(request):
    sort_by = request.GET.get('sort_by')
    sort_prods = Product.objects.order_by('price')
    # if sort_by == 'name':
    #     sort_prods = Product.objects.order_by('name')
    # elif sort_by == 'price':
    #     sort_prods = Product.objects.order_by('price')

    context = {'items': sort_prods}

    return render(request, 'main_page/index.html', context)


def add_product(request):
    if request.method == 'GET':
        return render(request, 'main_page/add_product.html', {'form': ProductForm()})
    else:
        try:
            form = ProductForm(request.POST, request.FILES)
            new_product = form.save(commit=True)
            new_product.user = request.user
            new_product.save()
            return redirect('index')
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
            return redirect('index')
        except ValueError:
            return render(request, 'main_page/product_detail.html',
                          {'form': form,
                           'error': 'Неверные данные!'})


def delete_prod(request, prod_id):
    product = get_object_or_404(Product, id=prod_id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
