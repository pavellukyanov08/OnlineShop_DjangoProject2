from django.db import models
from django.contrib.auth.models import User


class ShoppingCart(models.Model):
    product = models.CharField(max_length=50, verbose_name='Наименование')
    price = models.FloatField(max_length=20)
    img = models.ImageField(upload_to='main_page/images', null=True)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('product',)
        verbose_name = 'Корзины'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return self.product
