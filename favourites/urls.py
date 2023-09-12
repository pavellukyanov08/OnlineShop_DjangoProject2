from django.urls import path
from . import views

app_name = 'favourites'

urlpatterns = [
    path('', views.get_favourites_products, name='all_products'),
    path('favourites/<int:product_id>/', views.add_item, name='add_item'),
    path('remove_favourite/<int:product_id>/', views.remove_item, name='remove_item')
]