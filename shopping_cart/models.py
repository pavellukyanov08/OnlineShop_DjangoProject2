from django.db import models
from main_page.models import Product
from django.contrib.auth.models import User


class ShoppingCart(models.Model):
    product = models.CharField(max_length=50, verbose_name='Наименование')
    price = models.CharField(max_length=20)
    img = models.ImageField(upload_to='main_page/images', null=True)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product
