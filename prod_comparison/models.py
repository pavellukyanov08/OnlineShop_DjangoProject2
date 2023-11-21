from django.db import models
from django.contrib.auth.models import User
from main_page.models import Category, Product


class Compare(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        ordering = ('product',)
        verbose_name = 'Сравнение товара'
        verbose_name_plural = 'Сравнение товаров'

    def __str__(self):
        return f'Сравниваемый товар {self.product} пользователя {self.user}'
