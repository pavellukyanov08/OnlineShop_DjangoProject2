from django.db import models
from django.contrib.auth.models import User
from main_page.models import Category, Product
from shopping_cart.models import ShoppingCart


class Compare(models.Model):
    cart_prods = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Наименование', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('product',)
        verbose_name = 'Сравнение товара'
        verbose_name_plural = 'Сравнение товаров'

    def __str__(self):
        return self.product

