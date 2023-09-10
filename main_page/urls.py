from django.urls import path
from . import views

app_name = 'main_page'

urlpatterns = [
    # main_page
    path('index/', views.products_list, name='index'),

    # path('index/', views.sort_products, name='index'),

    path('<slug:category_slug>/', views.products_list, name='product_list_by_category'),

    path('<int:prod_id>/<slug:slug>', views.product_detail, name='product_detail'),



    # path('sort_products/', views.sort_products, name='sort_products'),

    # add product
    path('add_product/', views.add_product, name='add_product'),

    # view prod
    path('product/<int:prod_pk>', views.product_detail, name='view_prod'),

    # delete prod
    path('product/<int:prod_id>/delete', views.delete_prod, name='delete')

]

