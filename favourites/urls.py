from django.urls import path
from . import views

app_name = 'favourites'

urlpatterns = [

    path('remove_favourite/<int:product_id>/', views.remove_favourite_status, name='remove_item'),

    path('favourites/<int:product_id>/', views.add_favourite_status, name='add_item'),

    path('', views.get_favourite_products, name='all_products'),

]
