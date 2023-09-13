from django.urls import path
from . import views

app_name = 'compare'

urlpatterns = [
    path('', views.get_all_products, name='all_compare'),

    path('add_item/<int:product_id>/', views.add_item, name='add_item')
]