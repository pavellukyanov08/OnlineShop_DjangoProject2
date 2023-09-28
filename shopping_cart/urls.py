from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [

    path('', views.cart_view, name='cart'),

    # adding to cart
    path('add_item/<int:product_id>/', views.add_item, name='add_item'),

    # remove item
    path('remove_item/<int:product_id>/', views.remove_item, name='remove_item'),

    # update_item
    path('update_item/', views.update_cart, name='update_cart'),
]
