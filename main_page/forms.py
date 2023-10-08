from django.forms import ModelForm
from .models import Product, Review
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'value']

        labels = {
            'body': 'Добавьте комментарий к своему голосу',
            'value': 'Оставьте свой голос',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'description', 'img', 'width', 'height', 'weight', 'price',
                  'discount_price', 'start_date', 'end_date', 'availability_status']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }