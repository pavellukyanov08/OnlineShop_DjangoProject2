from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    # adding to cart
    path('add_item/<int:product_id>/', views.add_item, name='add_item'),
]