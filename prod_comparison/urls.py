from django.urls import path
from . import views

app_name = 'compare'

urlpatterns = [

    path('remove_item/<int:product_id>/', views.remove_compare_status, name='remove_item'),

    path('add_item/<int:product_id>/', views.add_compare_status, name='add_item'),

    path('', views.get_compare_products, name='all_compare'),

]