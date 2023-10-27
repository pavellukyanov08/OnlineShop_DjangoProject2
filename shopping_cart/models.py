from django.db import models
from django.contrib.auth.models import User


class ShoppingCart(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    price = models.FloatField(max_length=20, verbose_name='Цена')
    img = models.ImageField(upload_to='main_page/images', null=True, verbose_name='Изображение')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Корзины'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return self.name
