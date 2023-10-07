from django.forms import ModelForm
from .models import Product
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'description', 'img', 'width', 'height', 'weight', 'price',
                  'discount_price', 'start_date', 'end_date', 'availability_status']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }