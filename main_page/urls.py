from django.urls import path
from . import views

app_name = 'main_page'

urlpatterns = [
    # main_page
    path('', views.products_list, name='index'),

    # adding product
    path('add_product/', views.add_product, name='add_product'),

    # edit product page
    path('product/<int:prod_id>/<slug:slug>', views.product_detail, name='product_detail'),

    # delete prod
    path('product/<int:prod_id>/delete', views.delete_prod, name='delete'),

    # product category
    path('category/<slug:category_slug>/', views.products_list, name='product_list_by_category'),

    # product availability
    path('<str:product_availability>/', views.products_list, name='product_list_by_availability'),

    # view product page
    # path('product/<int:prod_id>/<slug:slug>', views.view_product, name='view_product'),
]
