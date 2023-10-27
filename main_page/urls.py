from django.urls import path
from . import views

app_name = 'main_page'

urlpatterns = [
    # main_page
    path('', views.products_list, name='index'),

    # adding product
    path('add_product/', views.add_product, name='add_product'),

    # editing specific product
    # path('product/<int:id>/<slug:slug>', views.edit_product, name='edit_product'),

    # delete prod
    path('product/<int:prod_id>/delete', views.delete_prod, name='delete'),

    # product category
    path('category/<slug:category_slug>/', views.products_list, name='product_list_by_category'),

    # product availability
    path('<str:product_availability>/', views.products_list, name='product_list_by_availability'),

    # viewing specific product
    path('product/<int:prod_id>/<slug:slug>', views.product_detail, name='product_detail'),
]
