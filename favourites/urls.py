from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites_product, name='favourites_product'),
    path('favourites/<int:product_id>', views.add_to_favourite, name='add_to_favourite')
]