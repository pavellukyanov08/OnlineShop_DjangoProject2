from django.db import models
from django.contrib.auth.models import User
from shopping_cart.models import ShoppingCart
from main_page.models import Product


class Favourite(models.Model):
    cart_prod = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, verbose_name='Описание', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('product',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return self.product

